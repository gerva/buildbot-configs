HGURL = 'http://hg.mozilla.org/'
CONFIG_REPO_URL = 'http://hg.mozilla.org/build/buildbot-configs'
CONFIG_SUBDIR = 'thunderbird'
LOCALE_REPO_URL = 'http://hg.mozilla.org/releases/l10n-mozilla-1.9.1/%(locale)s'
OBJDIR = 'objdir-tb'
STAGE_USERNAME = 'tbirdbld'
STAGE_SERVER = 'stage.mozilla.org'
STAGE_GROUP = 'thunderbird'
STAGE_SSH_KEY = 'tbirdbld_dsa'
AUS2_USER = 'tbirdbld'
AUS2_HOST = 'aus2-staging.mozilla.org'
DOWNLOAD_BASE_URL = 'http://ftp.mozilla.org/pub/mozilla.org/thunderbird'
PRODUCT = 'mail'
MOZ_APP_NAME = 'thunderbird'
BRAND_NAME = 'Shredder'

BUILDERS = {
    'linux': {
        'momo': [ 'momo-vm-%02i' % x for x in [2,7,12]],
        'moco': [ 'tb-linux-tbox' ],
    },
    'macosx': {
        '10.4': {
            'momo': [ 'momo-vm-osx-tiger-%02i' % x for x in [1,2] ],
            'moco': [ 'bm-xserve07' ], 
        },
        '10.5': {
            'momo': [ 'momo-vm-osx-leopard-%02i' % x for x in [1] ],
        },
    },
    'win32': {
        'momo': [ 'momo-vm-%02i' % x for x in [4,6,13,15,16] ] + [ 'momo-vm-win2k3-%02i' % x for x in [ 1 ] ],
        'moco': [ 'tbnewref-win32-tbox' ],
    },
}

DEFAULTS = {
    'factory':                'build',
    'hgurl':                  HGURL,
    'master_branch':          'comm-central',
    'branch_name':            'comm-central',
    'stage_base_path':        '/home/ftp/pub/mozilla.org/thunderbird',
    'mozilla_central_branch': 'releases/mozilla-1.9.1',
    'add_poll_branches':      [ 'dom-inspector' ],
    'period':                 60 * 60 * 8,
    'irc':                    True,
    'clobber_url':            "http://build.mozillamessaging.com/clobberer/",
    'builder_type':           "build",
    'tinderbox_tree':         "ThunderbirdTest",
    'codesighs':               False,
    
    # Unit Test
    'poll_branch':          'comm-central',
    'client_py_args':       ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--hg-options=--verbose --time --traceback'],
    'platforms': {
      'linux':  "Linux", 
      'win32':  "Win2k3",
      'osx':    "MacOSX 10.4",
    },

    'clobber_url':  "http://build.mozillamessaging.com/clobberer/",
    'build_tools_repo': "build/tools",
    'hg_rev_shortnames': {
      'mozilla-central':        'm-c',
      'comm-central':           'rev',
      'dom-inspector':          'domi',
      'releases/mozilla-1.9.1': 'moz',
    }
}

# All branches that are to be built MUST be listed here.
BRANCHES = {
    'comm-central': {},
    'comm-central-trunk': {},
    'comm-central-bloat': {},
    'comm-central-trunk-bloat': {},
    'comm-central-calendar': {},
    'comm-central-sunbird': {},
    'comm-1.9.1-unittest': {},
    'comm-central-unittest': {},
}

# thunderbird-unittest

BRANCHES['comm-1.9.1-unittest'] = {
    'factory': 'CCUnitTestFactory',
    'builder_type': 'check',
    'nightly': False,
    'hg_branch': 'comm-central',
    'branch_name': 'comm-1.9.1',
    'tinderbox_tree': 'Thunderbird3.0',
    'irc_nick': 'thunderbot',
    'irc_channels': ['maildev'],
    'platforms': {
        'linux': {
            'base_name': 'Linux comm-1.9.1',
            'slaves': BUILDERS['linux']['momo'],
        },
        'win32': {
            'base_name': 'Win2k3 comm-1.9.1',
            'slaves': BUILDERS['win32']['momo'],
        },
       'macosx': {
            'base_name': 'MacOSX 10.4 comm-1.9.1',
            'slaves': BUILDERS['macosx']['10.4']['momo'],
        },
        'macosx-10.5': {
            'base_name': 'MacOSX 10.5 comm-1.9.1',
            'slaves': BUILDERS['macosx']['10.5']['momo'],
        }
    }
}

BRANCHES['comm-central-unittest'] = {
    'factory': 'CCUnitTestFactory',
    'builder_type': 'check',
    'hg_branch': 'comm-central',
    'mozilla_central_branch': 'mozilla-central',
    'nightly': False,
    'tinderbox_tree': 'Thunderbird',
    'irc_nick': 'thunderbot-trunk',
    'irc_channels': ['maildev'],
    'client_py_args': DEFAULTS['client_py_args'] + ['--mozilla-repo=http://hg.mozilla.org/mozilla-central'],
    'platforms': {
        'linux': {
            'base_name': 'Linux comm-central',
            'slaves': BUILDERS['linux']['momo'],
        },
        'win32': {
            'base_name': 'Win2k3 comm-central',
            'slaves': BUILDERS['win32']['momo'],
        },
       'macosx': {
            'base_name': 'MacOSX 10.4 comm-central',
            'slaves': BUILDERS['macosx']['10.4']['momo'],
        },
        'macosx-10.5': {
            'base_name': 'MacOSX 10.5 comm-central',
            'slaves': BUILDERS['macosx']['10.5']['momo'],
        },

    },
}

######## thunderbird-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
    'macosx-shark': {},
}
BRANCHES['comm-central']['mozilla_central_branch'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-central']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--hg-options=--verbose --time --traceback']
BRANCHES['comm-central']['cvsroot'] = ':ext:tbirdbld@cvs.mozilla.org:/cvsroot'
BRANCHES['comm-central']['mozconfig'] = 'mozconfig'
BRANCHES['comm-central']['package'] = True
BRANCHES['comm-central']['branch_name'] = 'comm-1.9.1'
#Disable when producing release builds
#BRANCHES['comm-central']['nightly'] = False
BRANCHES['comm-central']['upload_stage'] = True
BRANCHES['comm-central']['milestone'] = 'comm-1.9.1'
BRANCHES['comm-central']['codesighs'] = True
BRANCHES['comm-central']['l10n'] = True
BRANCHES['comm-central']['platforms']['macosx-shark']['l10n'] = False
BRANCHES['comm-central']['irc_nick'] = 'thunderbuild'
BRANCHES['comm-central']['irc_channels'] = [ 'maildev' ]
BRANCHES['comm-central']['platforms']['linux']['base_name'] = 'Linux comm-1.9.1'
BRANCHES['comm-central']['platforms']['win32']['base_name'] = 'Win2k3 comm-1.9.1'
BRANCHES['comm-central']['platforms']['macosx']['base_name'] = 'MacOSX 10.4 comm-1.9.1'
BRANCHES['comm-central']['platforms']['macosx-shark']['base_name'] = 'MacOSX 10.5 comm-1.9.1 shark'
BRANCHES['comm-central']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-central']['platforms']['macosx-shark']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central']['create_snippet'] = True
BRANCHES['comm-central']['platforms']['macosx-shark']['create_snippet'] = False
BRANCHES['comm-central']['create_l10n_snippets'] = False
BRANCHES['comm-central']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Thunderbird/trunk'
BRANCHES['comm-central']['aus'] = {
    'user': 'tbirdbld',
    'host': 'aus-staging.mozillamessaging.com',
    'base_upload_dir': '/opt/aus/build/0/Thunderbird/comm-1.9.1',
}
BRANCHES['comm-central-trunk']['aus2_base_upload_dir'] = '/opt/aus/build/0/Thunderbird/comm-central'
BRANCHES['comm-central']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
BRANCHES['comm-central']['platforms']['macosx-shark']['update_platform'] = 'Darwin_Universal-gcc3-shark'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-central']['platforms']['macosx-shark']['upload_symbols'] = False
BRANCHES['comm-central']['tinderbox_tree'] = 'Thunderbird3.0'
BRANCHES['comm-central']['platforms']['linux']['slaves'] = [
    'tb-linux-tbox',
]
BRANCHES['comm-central']['platforms']['win32']['slaves'] = [
    'tbnewref-win32-tbox'
]
BRANCHES['comm-central']['platforms']['macosx']['slaves'] = [
    'bm-xserve07'
]
BRANCHES['comm-central']['platforms']['macosx-shark']['slaves'] = BUILDERS['macosx']['10.5']['momo']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central']['platforms']['macosx-shark']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central']['platforms']['macosx-shark']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## thunderbird-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-trunk']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
    'macosx-10.5' : {},
}
BRANCHES['comm-central-trunk']['mozilla_central_branch'] = 'mozilla-central'
BRANCHES['comm-central-trunk']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--mozilla-repo=http://hg.mozilla.org/mozilla-central','--hg-options=--verbose --time --traceback']
BRANCHES['comm-central-trunk']['cvsroot'] = ':ext:tbirdbld@cvs.mozilla.org:/cvsroot'
BRANCHES['comm-central-trunk']['mozconfig'] = 'mozconfig'
BRANCHES['comm-central-trunk']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-trunk']['package'] = True
#Disable when producing release builds
#BRANCHES['comm-central-trunk']['nightly'] = False
BRANCHES['comm-central-trunk']['upload_stage'] = True
BRANCHES['comm-central-trunk']['platforms']['macosx-10.5']['upload_stage'] = False
BRANCHES['comm-central-trunk']['milestone'] = 'comm-central-trunk'
BRANCHES['comm-central-trunk']['platforms']['macosx-10.5']['milestone'] = 'comm-central-trunk-10.5-test'
BRANCHES['comm-central-trunk']['codesighs'] = True
BRANCHES['comm-central-trunk']['l10n'] = False
BRANCHES['comm-central-trunk']['irc_nick'] = 'thunderbuild-trunk'
BRANCHES['comm-central-trunk']['irc_channels'] = [ 'maildev' ]
BRANCHES['comm-central-trunk']['platforms']['linux']['base_name'] = 'Linux comm-central'
BRANCHES['comm-central-trunk']['platforms']['win32']['base_name'] = 'Win2k3 comm-central'
BRANCHES['comm-central-trunk']['platforms']['macosx']['base_name'] = 'MacOSX 10.4 comm-central'
BRANCHES['comm-central-trunk']['platforms']['macosx-10.5']['base_name'] = 'MacOSX 10.5 comm-central'
BRANCHES['comm-central-trunk']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-central-trunk']['platforms']['macosx-10.5']['profiled_build'] = False

# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-trunk']['create_snippet'] = True
BRANCHES['comm-central-trunk']['create_l10n_snippets'] = False
BRANCHES['comm-central-trunk']['aus2_host'] = 'aus-staging.sj.mozillamessaging.com'
BRANCHES['comm-central-trunk']['aus2_base_upload_dir'] = '/opt/aus/build/0/Thunderbird/comm-central'
BRANCHES['comm-central-trunk']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-trunk']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-trunk']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
BRANCHES['comm-central-trunk']['platforms']['macosx-10.5']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-trunk']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-central-trunk']['platforms']['macosx-10.5']['upload_symbols'] = False
BRANCHES['comm-central-trunk']['tinderbox_tree'] = 'Thunderbird'
BRANCHES['comm-central-trunk']['platforms']['linux']['slaves'] = BUILDERS['linux']['momo']
BRANCHES['comm-central-trunk']['platforms']['win32']['slaves'] = BUILDERS['win32']['momo']
BRANCHES['comm-central-trunk']['platforms']['macosx']['slaves'] = BUILDERS['macosx']['10.4']['momo']
BRANCHES['comm-central-trunk']['platforms']['macosx-10.5']['slaves'] = BUILDERS['macosx']['10.5']['momo']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-trunk']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central-trunk']['platforms']['macosx-10.5']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central-trunk']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

BRANCHES['comm-central-trunk']['platforms']['macosx-10.5']['env'] = BRANCHES['comm-central-trunk']['platforms']['macosx']['env']

######## lightning-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-calendar']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}

BRANCHES['comm-central-calendar']['mozilla_central_branch'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-central-calendar']['branch_name'] = 'comm-1.9.1'
BRANCHES['comm-central-calendar']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman']
BRANCHES['comm-central-calendar']['cvsroot'] = ':ext:calbld@cvs.mozilla.org:/cvsroot'
BRANCHES['comm-central-calendar']['mozconfig'] = 'mozconfig-calendar'
BRANCHES['comm-central-calendar']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-calendar']['period'] = 60 * 60 * 6
BRANCHES['comm-central-calendar']['package'] = True
BRANCHES['comm-central-calendar']['upload_stage'] = True
BRANCHES['comm-central-calendar']['upload_complete_mar'] = False
#Might be better off per-platform instead of per-branch here.
BRANCHES['comm-central-calendar']['upload_glob'] = "mozilla/dist/xpi-stage/{lightning,gdata-provider}.xpi"
BRANCHES['comm-central-calendar']['stage_username'] = 'calbld'
BRANCHES['comm-central-calendar']['stage_base_path'] = '/home/ftp/pub/mozilla.org/calendar/lightning'
BRANCHES['comm-central-calendar']['stage_group'] = 'calendar'
BRANCHES['comm-central-calendar']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-central-calendar']['codesighs'] = False
BRANCHES['comm-central-calendar']['l10n'] = False
BRANCHES['comm-central-calendar']['irc_nick'] = 'calbuild'
BRANCHES['comm-central-calendar']['irc_channels'] = [ 'maildev', 'calendar' ]
BRANCHES['comm-central-calendar']['platforms']['linux']['base_name'] = 'Linux comm-1.9.1 lightning'
BRANCHES['comm-central-calendar']['platforms']['win32']['base_name'] = 'Win2k3 comm-1.9.1 lightning'
BRANCHES['comm-central-calendar']['platforms']['macosx']['base_name'] = 'MacOSX 10.4 comm-1.9.1 lightning'
BRANCHES['comm-central-calendar']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-calendar']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-calendar']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-central-calendar']['platforms']['linux']['milestone'] = "comm-1.9.1/linux-xpi"
BRANCHES['comm-central-calendar']['platforms']['win32']['milestone'] = "comm-1.9.1/win32-xpi"
BRANCHES['comm-central-calendar']['platforms']['macosx']['milestone'] = "comm-1.9.1/macosx-xpi"
BRANCHES['comm-central-calendar']['platforms']['macosx']['upload_glob'] = "mozilla/dist/universal/xpi-stage/{lightning,gdata-provider}.xpi"

# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-calendar']['create_snippet'] = False
BRANCHES['comm-central-calendar']['create_l10n_snippets'] = False
BRANCHES['comm-central-calendar']['aus2_base_upload_dir'] = False
BRANCHES['comm-central-calendar']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-calendar']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-calendar']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-calendar']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-central-calendar']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-central-calendar']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-central-calendar']['tinderbox_tree'] = 'Sunbird'
BRANCHES['comm-central-calendar']['platforms']['linux']['slaves'] = [
    'cb-sb-linux-tbox',
]
BRANCHES['comm-central-calendar']['platforms']['win32']['slaves'] = [
    'cb-sb-win32-tbox',
]
BRANCHES['comm-central-calendar']['platforms']['macosx']['slaves'] = [
    'cb-xserve03',
]
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-calendar']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-calendar']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-calendar']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central-calendar']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-calendar']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-calendar']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## sunbird-hg
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-sunbird']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {}
}
BRANCHES['comm-central-sunbird']['mozilla_central_branch'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-central-sunbird']['branch_name'] = 'comm-1.9.1'
BRANCHES['comm-central-sunbird']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman']
BRANCHES['comm-central-sunbird']['cvsroot'] = ':ext:calbld@cvs.mozilla.org:/cvsroot'
BRANCHES['comm-central-sunbird']['mozconfig'] = 'mozconfig-sunbird'
BRANCHES['comm-central-sunbird']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-sunbird']['period'] = 60 * 60 * 6
BRANCHES['comm-central-sunbird']['package'] = True
BRANCHES['comm-central-sunbird']['upload_stage'] = True
BRANCHES['comm-central-sunbird']['milestone'] = 'comm-1.9.1'
BRANCHES['comm-central-sunbird']['stage_username'] = 'calbld'
BRANCHES['comm-central-sunbird']['stage_base_path'] = '/home/ftp/pub/mozilla.org/calendar/sunbird'
BRANCHES['comm-central-sunbird']['stage_group'] = 'calendar'
BRANCHES['comm-central-sunbird']['stage_ssh_key'] = 'calbld_dsa'
BRANCHES['comm-central-sunbird']['codesighs'] = False
BRANCHES['comm-central-sunbird']['l10n'] = True
BRANCHES['comm-central-sunbird']['l10n_mozconfig'] = 'mozconfig-sunbird-l10n'
BRANCHES['comm-central-sunbird']['product'] = 'calendar'
BRANCHES['comm-central-sunbird']['appname'] = 'sunbird'
BRANCHES['comm-central-sunbird']['brand_name'] = 'Calendar'
BRANCHES['comm-central-sunbird']['irc_nick'] = 'sunbuild'
BRANCHES['comm-central-sunbird']['irc_channels'] = [ 'maildev','calendar' ]
BRANCHES['comm-central-sunbird']['platforms']['linux']['base_name'] = 'Linux comm-1.9.1 sunbird'
BRANCHES['comm-central-sunbird']['platforms']['win32']['base_name'] = 'Win2k3 comm-1.9.1 sunbird'
BRANCHES['comm-central-sunbird']['platforms']['macosx']['base_name'] = 'MacOSX 10.4 comm-1.9.1 sunbird'
BRANCHES['comm-central-sunbird']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-sunbird']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-sunbird']['platforms']['macosx']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-sunbird']['create_snippet'] = True
BRANCHES['comm-central-sunbird']['aus2_host'] = 'aus2-community.mozilla.org'
BRANCHES['comm-central-sunbird']['aus2_user'] = 'calbld'
BRANCHES['comm-central-sunbird']['create_l10n_snippets'] = False
BRANCHES['comm-central-sunbird']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Sunbird/trunk'
BRANCHES['comm-central-sunbird']['download_base_url'] = 'http://ftp.mozilla.org/pub/mozilla.org/calendar/sunbird'
BRANCHES['comm-central-sunbird']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-sunbird']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-sunbird']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-sunbird']['platforms']['linux']['upload_symbols'] = True
BRANCHES['comm-central-sunbird']['platforms']['win32']['upload_symbols'] = True
BRANCHES['comm-central-sunbird']['platforms']['macosx']['upload_symbols'] = True
BRANCHES['comm-central-sunbird']['tinderbox_tree'] = 'Sunbird'
BRANCHES['comm-central-sunbird']['platforms']['linux']['slaves'] = [
    'cb-sb-linux-tbox',
]
BRANCHES['comm-central-sunbird']['platforms']['win32']['slaves'] = [
    'cb-sb-win32-tbox',
]
BRANCHES['comm-central-sunbird']['platforms']['macosx']['slaves'] = [
    'cb-xserve03',
]

# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-sunbird']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-sunbird']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-sunbird']['platforms']['macosx']['platform_objdir'] = '%s/ppc' % OBJDIR
BRANCHES['comm-central-sunbird']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'calbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/calbld/.ssh/calbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-sunbird']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'calbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/calbld/.ssh/calbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-sunbird']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'calbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_sbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/calbld/.ssh/calbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}


######## thunderbird-bloat
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-bloat']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
}

BRANCHES['comm-central-bloat']['mozilla_central_branch'] = 'releases/mozilla-1.9.1'
BRANCHES['comm-central-bloat']['branch_name'] = 'comm-1.9.1'
BRANCHES['comm-central-bloat']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--hg-options=--verbose --time --traceback']
BRANCHES['comm-central-bloat']['cvsroot'] = ':pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot'
BRANCHES['comm-central-bloat']['mozconfig'] = 'mozconfig-bloat'
BRANCHES['comm-central-bloat']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-bloat']['nightly'] = False
BRANCHES['comm-central-bloat']['leak'] = True
BRANCHES['comm-central-bloat']['package'] = False
BRANCHES['comm-central-bloat']['upload_stage'] = False
BRANCHES['comm-central-bloat']['codesighs'] = False
BRANCHES['comm-central-bloat']['l10n'] = False
BRANCHES['comm-central-bloat']['irc_nick'] = 'thunderbloat'
BRANCHES['comm-central-bloat']['irc_channels'] = [ 'maildev' ]
BRANCHES['comm-central-bloat']['builder_type'] = 'bloat'
BRANCHES['comm-central-bloat']['platforms']['linux']['base_name'] = 'Linux comm-1.9.1'
BRANCHES['comm-central-bloat']['platforms']['win32']['base_name'] = 'Win2k3 comm-1.9.1'
BRANCHES['comm-central-bloat']['platforms']['macosx']['base_name'] = 'MacOSX 10.4 comm-1.9.1'
BRANCHES['comm-central-bloat']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-bloat']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-bloat']['platforms']['macosx']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-bloat']['create_snippet'] = False
BRANCHES['comm-central-bloat']['create_l10n_snippets'] = False
BRANCHES['comm-central-bloat']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Thunderbird/trunk'
BRANCHES['comm-central-bloat']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-bloat']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-bloat']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-bloat']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-central-bloat']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-central-bloat']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-central-bloat']['tinderbox_tree'] = 'Thunderbird3.0'
BRANCHES['comm-central-bloat']['platforms']['linux']['leak_threshold'] = 970000
BRANCHES['comm-central-bloat']['platforms']['macosx']['leak_threshold'] = 1400000
BRANCHES['comm-central-bloat']['platforms']['win32']['leak_threshold'] =  110000
BRANCHES['comm-central-bloat']['platforms']['linux']['slaves'] = BUILDERS['linux']['momo']
BRANCHES['comm-central-bloat']['platforms']['win32']['slaves'] = BUILDERS['win32']['momo']
BRANCHES['comm-central-bloat']['platforms']['macosx']['slaves'] = BUILDERS['macosx']['10.4']['momo']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-bloat']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-bloat']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-bloat']['platforms']['macosx']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-bloat']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/home/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
}
BRANCHES['comm-central-bloat']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-bloat']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'SYMBOL_SERVER_HOST': 'dm-symbolpush01.mozilla.org',
    'SYMBOL_SERVER_USER': 'tbirdbld',
    'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_tbrd/',
    'SYMBOL_SERVER_SSH_KEY': "/Users/tbirdbld/.ssh/tbirdbld_dsa",
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}

######## thunderbird-bloat (mozilla-central)
# All platforms being built for this branch MUST be listed here.
BRANCHES['comm-central-trunk-bloat']['platforms'] = {
    'linux': {},
    'win32': {},
    'macosx': {},
    'macosx-10.5': {},
}

BRANCHES['comm-central-trunk-bloat']['mozilla_central_branch'] = 'mozilla-central'
BRANCHES['comm-central-trunk-bloat']['client_py_args'] = ['--skip-comm', '--skip-chatzilla', '--skip-venkman', '--mozilla-repo=http://hg.mozilla.org/mozilla-central', '--hg-options=--verbose --time --traceback']
BRANCHES['comm-central-trunk-bloat']['cvsroot'] = ':pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot'
BRANCHES['comm-central-trunk-bloat']['mozconfig'] = 'mozconfig-bloat'
BRANCHES['comm-central-trunk-bloat']['hg_branch'] = 'comm-central'
BRANCHES['comm-central-trunk-bloat']['builder_type'] = 'bloat'
BRANCHES['comm-central-trunk-bloat']['nightly'] = False
BRANCHES['comm-central-trunk-bloat']['leak'] = True
BRANCHES['comm-central-trunk-bloat']['package'] = False
BRANCHES['comm-central-trunk-bloat']['upload_stage'] = False
BRANCHES['comm-central-trunk-bloat']['codesighs'] = False
BRANCHES['comm-central-trunk-bloat']['l10n'] = False
BRANCHES['comm-central-trunk-bloat']['irc_nick'] = 'thunderbloat-trunk'
BRANCHES['comm-central-trunk-bloat']['irc_channels'] = [ 'maildev' ]
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['base_name'] = 'Linux comm-central'
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['base_name'] = 'Win2k3 comm-central'
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['base_name'] = 'MacOSX 10.4 comm-central'
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx-10.5']['base_name'] = 'MacOSX 10.5 comm-central'
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['profiled_build'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['profiled_build'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['profiled_build'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx-10.5']['profiled_build'] = False
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['comm-central-trunk-bloat']['create_snippet'] = False
BRANCHES['comm-central-trunk-bloat']['create_l10n_snippets'] = False
BRANCHES['comm-central-trunk-bloat']['aus2_base_upload_dir'] = '/opt/aus2/build/0/Thunderbird/trunk'
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['update_platform'] = 'Linux_x86-gcc3'
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['update_platform'] = 'WINNT_x86-msvc'
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['update_platform'] = 'Darwin_Universal-gcc3'
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx-10.5']['update_platform'] = 'Darwin_Universal-gcc3'
# If True, 'make buildsymbols' and 'make uploadsymbols' will be run
# SYMBOL_SERVER_* variables are setup in the environment section below
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['upload_symbols'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['upload_symbols'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['upload_symbols'] = False
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx-10.5']['upload_symbols'] = False
BRANCHES['comm-central-trunk-bloat']['tinderbox_tree'] = 'Thunderbird'
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['leak_threshold'] = 970000
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['leak_threshold'] = 1400000
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx-10.5']['leak_threshold'] = 1400000
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['leak_threshold'] =  110000
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['slaves'] = BUILDERS['linux']['momo']
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['slaves'] = BUILDERS['win32']['momo']
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['slaves'] = BUILDERS['macosx']['10.4']['momo']
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx-10.5']['slaves'] = BUILDERS['macosx']['10.5']['momo']
# This is used in a bunch of places where something needs to be run from
# the objdir. This is necessary because of universal builds on Mac
# creating subdirectories inside of the objdir.
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx-10.5']['platform_objdir'] = OBJDIR
BRANCHES['comm-central-trunk-bloat']['platforms']['linux']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'LD_LIBRARY_PATH': '%s/mozilla/dist/bin' % OBJDIR,
}
BRANCHES['comm-central-trunk-bloat']['platforms']['win32']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['env'] = {'CVS_RSH': 'ssh',
    'MOZ_OBJDIR': OBJDIR,
    'TINDERBOX_OUTPUT': '1',
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
}
BRANCHES['comm-central-trunk-bloat']['platforms']['macosx-10.5']['env'] = BRANCHES['comm-central-trunk-bloat']['platforms']['macosx']['env']
