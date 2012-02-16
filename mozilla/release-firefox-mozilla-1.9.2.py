releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True

# Release Notification
releaseConfig['AllRecipients']       = ['release@mozilla.com','akeybl@mozilla.com','Callek@gmail.com']
releaseConfig['ImportantRecipients'] = ['release-drivers@mozilla.org',]
releaseConfig['AVVendorsRecipients'] = ['av-vendor-release-announce@mozilla.org',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'firefox'
releaseConfig['appName']             = 'browser'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
#  Current version info
releaseConfig['version']             = '3.6.27'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = '1.9.2.27'
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_3_6_27'
#  Old version info
releaseConfig['oldVersion']          = '3.6.26'
releaseConfig['oldAppVersion']       = releaseConfig['oldVersion']
releaseConfig['oldBuildNumber']      = 2
releaseConfig['oldBaseTag']          = 'FIREFOX_3_6_26'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = '3.6.28pre'
releaseConfig['nextMilestone']       = '1.9.2.28pre'
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        'name': 'mozilla-1.9.2',
        'path': 'releases/mozilla-1.9.2',
        'revision': 'fd6d19a5ae84',
        'relbranch': None,
        'bumpFiles': {
            'browser/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
            'js/src/config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
        }
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'releases/l10n-mozilla-1.9.2'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-1.9.2'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_0_8_2',
    'build/buildbot': 'production-0.8',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'win32', 'macosx')
releaseConfig['notifyPlatforms']      = ('linux', 'win32', 'macosx')
releaseConfig['talosTestPlatforms']  = releaseConfig['enUSPlatforms']
releaseConfig['xulrunnerPlatforms']  = releaseConfig['enUSPlatforms']

# Unittests
releaseConfig['enableUnittests']     = True
# this variable adds unit tests on the builders
releaseConfig['unittestPlatforms']   = releaseConfig['enUSPlatforms']

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['l10nChunks']          = 6
releaseConfig['mergeLocales']        = False

# Mercurial account
releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['cvsroot']             = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
releaseConfig['patcherConfig']       = 'moz192-branch-patcher2.cfg'
releaseConfig['commitPatcherConfig'] = True
releaseConfig['patcherToolsTag']     = 'UPDATE_PACKAGING_R11_1'
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus2.mozilla.org'
releaseConfig['ausHost']             = 'aus2-staging.mozilla.org'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = True
releaseConfig['useBetaChannelForRelease'] = True
releaseConfig['verifyConfigs']       = {
    'linux':  'moz192-firefox-linux.cfg',
    'macosx': 'moz192-firefox-mac.cfg',
    'win32':  'moz192-firefox-win32.cfg'
}
releaseConfig['snippetSchema']       = 1
releaseConfig['releaseChannel']      = 'release'

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'

# Major update configuration
releaseConfig['majorUpdateRepoPath'] = 'releases/mozilla-release'
releaseConfig['majorUpdateToVersion']   = '10.0.2'
releaseConfig['majorUpdateAppVersion']  = releaseConfig['majorUpdateToVersion']
releaseConfig['majorUpdateBuildNumber'] = 1
releaseConfig['majorUpdateBaseTag']     = 'FIREFOX_10_0_2'
releaseConfig['majorUpdateReleaseNotesUrl']  = 'https://www.mozilla.org/%locale%/firefox/latest/details/from-3.6.html'
releaseConfig['majorUpdatePatcherConfig']    = 'moz192-branch-major-update-patcher2.cfg'
releaseConfig['majorPatcherToolsTag']        = 'UPDATE_PACKAGING_R11_1_MU'
releaseConfig['majorUpdateVerifyConfigs']    = {
    'linux':  'moz192-firefox-linux-major.cfg',
    'macosx': 'moz192-firefox-mac-major.cfg',
    'win32':  'moz192-firefox-win32-major.cfg'
}
releaseConfig['majorFakeMacInfoTxt'] = True
releaseConfig['majorSnippetSchema']  = 1

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api/'
releaseConfig['extraBouncerPlatforms'] = ('solaris-sparc', 'solaris-i386',
                                          'opensolaris-sparc',
                                          'opensolaris-i386')

# Misc configuration
releaseConfig['enable_repo_setup'] = False
releaseConfig['enableSigningAtBuildTime'] = False
releaseConfig['enablePartialMarsAtBuildTime'] = False
