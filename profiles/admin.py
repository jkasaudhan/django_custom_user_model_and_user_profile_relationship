from django.contrib import admin
from profiles.models import User, CandidateProfileModel

admin.site.register(User)
admin.site.register(CandidateProfileModel)