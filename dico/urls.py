from django.conf.urls import patterns, url

from dico import views

urlpatterns = patterns(
	'',
    url(r'^$', views.index, name='index'),
    # ex: /dico/signin/
    url(r'^signin/', views.signin, name='signin'),
    # ex: /dico/submitsignin/
    url(r'^submitsignin/', views.submitsignin, name='submitsignin'),
    # ex: /dico/signout/
    url(r'^signout/', views.signout, name='signout'),
    # ex: /dico/editinterests/
    url(r'^editinterests/', views.editInterests, name='editInterests'),
    # ex: /dico/account/
    url(r'^account/', views.account, name='account'),
    # ex: /dico/password/
    url(r'^password/', views.password, name='password'),
    # ex: /dico/forgotpassword/
    url(r'^forgotpassword/', views.forgotPassword, name='forgotpassword'),
    # ex: /dico/resetpassword/
    url(r'^resetpassword/', views.resetPassword, name='resetPassword'),
    # ex: /dico/passwordreset/
    url(r'^passwordreset/', views.passwordReset, name='passwordReset'),
    # ex: /dico/passwordreset/
    url(r'^setresetpassword/', views.setResetPassword, name='setResetPassword'),
	# ex: /dico/issue/5/
	url(r'^(?P<issue_id>\d+)/issue/$', views.issue, name='issue'),
	# ex: /dico/petition/5/
	url(r'^(?P<petition_id>\d+)/petition/$', views.petition, name='petition'),
	# ex: /dico/createPetition/
	url(r'^createpetition/$', views.createPetition, name='createPetition'),
	# ex: /dico/addpetitionissue/5/
	url(r'^(?P<petition_id>\d+)/addpetitionissue/$', views.addPetitionIssue, name='addPetitionIssue'),
    # ex: /dico/newinterest/
    url(r'^newinterest/', views.newInterest, name='newInterest'),
    # ex: /dico/submitdeleteinterest/
    url(r'^submitdeleteinterest/', views.submitdeleteinterest, name='deleteinterest'),
	# ex: /dico/createConstituent/
    url(r'^createConstituent/', views.createConstituent, name='createConstituent'),
	# ex: /dico/newconstituent/
	url(r'^newconstituent/', views.newConstituent, name='newConstituent'),
	# ex: /dico/updateconstituent/
	url(r'^updateconstituent/', views.updateConstituent, name='updateConstituent'),
	# ex: /dico/updatepassword/
	url(r'^updatepassword/', views.updatePassword, name='updatePassword'),
    # ex: /dico/getissuepetitions/
    url(r'^getissuepetitions/', views.getIssuePetitions, name='getissuepetitions'),
    # ex: /dico/newpetition/
    url(r'^newpetition/', views.newPetition, name='newpetition'),
    # ex: /dico/deletepetition/
    url(r'^deletepetition/', views.deletePetition, name='deletepetition'),
    # ex: /dico/updatepetition/
    url(r'^updatepetition/', views.updatePetition, name='updatepetition'),
    # ex: /dico/getpetitionissues/
    url(r'^getpetitionissues/', views.getPetitionIssues, name='getpetitionissues'),
    # ex: /dico/getpetitionarguments/
    url(r'^getpetitionarguments/', views.getPetitionArguments, name='getpetitionarguments'),
    # ex: /dico/newpetitionissue/
    url(r'^newpetitionissue/', views.newPetitionIssue, name='newpetitionissue'),
    # ex: /dico/deletepetitionissue/
    url(r'^deletepetitionissue/', views.deletePetitionIssue, name='deletepetitionissue'),
    # ex: /dico/getpetitionvotes/
    url(r'^getpetitionvotes/', views.getPetitionVotes, name='getpetitionvotes'),
    # ex: /dico/newpetitionvote/
    url(r'^newpetitionvote/', views.newPetitionVote, name='newpetitionvote'),
    # ex: /dico/deletepetitionvote/
    url(r'^deletepetitionvote/', views.deletePetitionVote, name='deletepetitionvote'),
    # ex: /dico/updatepetitionvote/
    url(r'^updatepetitionvote/', views.updatePetitionVote, name='updatepetitionvote'),
	# ex: /dico/addsupportingargument/5/
	url(r'^(?P<petition_id>\d+)/addsupportingargument/$', views.addSupportingArgument, name='addSupportingArgument'),
	# ex: /dico/addopposingargument/5/
	url(r'^(?P<petition_id>\d+)/addopposingargument/$', views.addOpposingArgument, name='addOpposingArgument'),
    # ex: /dico/newargument/
    url(r'^newargument/', views.newArgument, name='newArgument'),
    # ex: /dico/deleteargument/
    url(r'^deleteargument/', views.deleteArgument, name='deleteArgument'),
    # ex: /dico/rateargument/
    url(r'^rateargument/', views.rateArgument, name='rateArgument'),
    # ex: /dico/unrateargument/
    url(r'^unrateargument/', views.unrateArgument, name='unrateArgument'),
	# ex: /dico/5/
	url(r'^(?P<constituent_id>\d+)/$', views.dashboard, name='dashboard'),
	# ex: /dico/5/addissue/
	url(r'^(?P<constituent_id>\d+)/addissue/$', views.addissue, name='addissue'),
	# ex: /dico/5/mcdashboard/
	url(r'^(?P<mc_id>\d+)/mcdashboard/$', views.mcdashboard, name='mcdashboard'),
	# ex: /dico/5/mcaddissue/
	url(r'^(?P<mc_id>\d+)/mcaddissue/$', views.mcaddissue, name='mcaddissue'),
	# ex: /dico/member/?bioguide_id=.../
	url(r'^member/', views.member, name='member'),
	# ex: /dico/getissues -- Get all of the issues with a specified minimum level of interest.
	url(r'^getissues/', views.getIssues, name='getIssues'),
	# ex: /dico/getissueinterests -- Get the interest in a particular issue ID.
	url(r'^getissueinterests/', views.getIssueInterests, name='getIssueInterests'),
	# ex: /dico/getmyinterests -- Get all of the interests of the current logged-in user.
	url(r'^getmyinterests/', views.getMyInterests, name='getMyInterests'),
	# ex: /dico/getmynews -- Get all of the news items of the current logged-in user.
	url(r'^getmynews/', views.getMyNews, name='getMyNews'),
)
