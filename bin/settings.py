# Settings for the installer

# type:  restapi-web   - REST API from a LayerIndex-web
#        restapi-files - REST API, but only from files
#        export        - Exported DB from a LayerIndex-web -- reads file(s)

# url/path may contain:
#  #INSTALL_DIR# which is replaced by the setup directory
#  #BASE_URL# which is replaced by the base url for setup directory
#  #BASE_BRANCH# which is replaced by the base branch for the setup directory

# Since we know the url below will be mirrored to our
# internal git mirrors, change format so it can be replaced
# with the proper value(s)
REPLACE = [
    ( 'git://git.wrs.com', '#BASE_URL#' )
]

INDEXES = [
    {
        'DESCRIPTION' : 'Wind River Developer Layer Index',
        'TYPE' : 'restapi-web',
        'URL' : 'http://layers.wrs.com/layerindex/api/',
        'CACHE' : 'config/index-cache/layers_wrs_com',
    },
#    {
#        'DESCRIPTION' : 'Wind River Linux Index',
#        'TYPE' : 'export',
#        'URL' : '#INSTALL_DIR#/data/index',
#    },
#    {
#        'DESCRIPTION' : 'OpenEmbedded Layer Index',
#        'TYPE' : 'restapi-web',
#        'URL' : 'http://layers.openembedded.org/layerindex/api/',
#        'CACHE' : 'config/index-cache/layers_openembedded_org',
#        'BRANCH' : 'master'
#    },
]

# Bitbake URL on the same server at openembedded-core
BITBAKE = "bitbake"

# Base Layers (these layers and their dependencies are -always- included)
BASE_LAYERS = "wr-base"

DEFAULT_DISTRO = "wrlinux"
DEFAULT_MACHINE = "qemux86-64"
DEFAULT_KTYPE = "standard"