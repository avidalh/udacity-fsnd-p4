#!/usr/bin/env python

import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from conference import ConferenceApi
from lib import queries


class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()


class SetFeaturedSpeaker(webapp2.RequestHandler):
    def post(self):
        """Set Announcement in Memcache."""
        wsck = self.request.get("wsck")
        speaker = self.request.get("speaker")
        queries.set_featured_speaker(wsck, speaker)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % ( app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created the following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )

app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/set_featured_speaker', SetFeaturedSpeaker),
], debug=True)
