from fanstatic import Library, Resource
import js.jquery

library = Library('jqueryui', 'resources')

# CDN info from http://blog.jqueryui.com/2011/01/jquery-ui-1-8-8/
version = '1.8.8'
google = '//ajax.googleapis.com/ajax/libs/jqueryui/' + version
microsoft = '//ajax.aspnetcdn.com/ajax/jquery.ui/' + version

def cdnify(path):
    return {
        'google': '%s/%s/' % (google, path),
        'microsoft': '%s/%s/' % (microsoft, path),
    }

_jqueryui_minified = Resource(library, 'ui/minified/jquery-ui.min.js',
    depends=[js.jquery.jquery], cdns=cdnify('jquery-ui.min.js'))
jqueryui = Resource(library, 'ui/jquery-ui.js', minified=_jqueryui_minified,
    depends=[js.jquery.jquery], cdns=cdnify('jquery-ui.js'))

_base_minified = Resource(library, 'themes/base/minified/jquery-ui.min.css',
     cdns=cdnify('themes/base/minified/jquery-ui.min.css'))
base = Resource(library, 'themes/base/jquery-ui.css', minified=_base_minified,
     cdns=cdnify('themes/base/jquery-ui.css'))

black_tie = Resource(library, 'themes/black-tie/jquery-ui.css',
    cdns=cdnify('themes/black-tie/jquery-ui.css'))
blitzer = Resource(library, 'themes/blitzer/jquery-ui.css',
    cdns=cdnify('themes/blitzer/jquery-ui.css'))
cupertino = Resource(library, 'themes/cupertino/jquery-ui.css',
    cdns=cdnify('themes/cupertino/jquery-ui.css'))
dark_hive = Resource(library, 'themes/dark-hive/jquery-ui.css',
    cdns=cdnify('themes/dark-hive/jquery-ui.css'))
dot_luv = Resource(library, 'themes/dot-luv/jquery-ui.css',
    cdns=cdnify('themes/dot-luv/jquery-ui.css'))
eggplant = Resource(library, 'themes/eggplant/jquery-ui.css',
    cdns=cdnify('themes/eggplant/jquery-ui.css'))
excite_bike = Resource(library, 'themes/excite-bike/jquery-ui.css',
    cdns=cdnify('themes/excite-bike/jquery-ui.css'))
flick = Resource(library, 'themes/flick/jquery-ui.css',
    cdns=cdnify('themes/flick/jquery-ui.css'))
hot_sneaks = Resource(library, 'themes/hot-sneaks/jquery-ui.css',
    cdns=cdnify('themes/hot-sneaks/jquery-ui.css'))
humanity = Resource(library, 'themes/humanity/jquery-ui.css',
    cdns=cdnify('themes/humanity/jquery-ui.css'))
le_frog = Resource(library, 'themes/le-frog/jquery-ui.css',
    cdns=cdnify('themes/le-frog/jquery-ui.css'))
mint_choc = Resource(library, 'themes/mint-choc/jquery-ui.css',
    cdns=cdnify('themes/mint-choc/jquery-ui.css'))
overcast = Resource(library, 'themes/overcast/jquery-ui.css',
    cdns=cdnify('themes/overcast/jquery-ui.css'))
pepper_grinder = Resource(library, 'themes/pepper-grinder/jquery-ui.css',
    cdns=cdnify('themes/pepper-grinder/jquery-ui.css'))
redmond = Resource(library, 'themes/redmond/jquery-ui.css',
    cdns=cdnify('themes/redmond/jquery-ui.css'))
smoothness = Resource(library, 'themes/smoothness/jquery-ui.css',
    cdns=cdnify('themes/smoothness/jquery-ui.css'))
south_street = Resource(library, 'themes/south-street/jquery-ui.css',
    cdns=cdnify('themes/south-street/jquery-ui.css'))
start = Resource(library, 'themes/start/jquery-ui.css',
    cdns=cdnify('themes/start/jquery-ui.css'))
sunny = Resource(library, 'themes/sunny/jquery-ui.css',
    cdns=cdnify('themes/sunny/jquery-ui.css'))
swanky_purse = Resource(library, 'themes/swanky-purse/jquery-ui.css',
    cdns=cdnify('themes/swanky-purse/jquery-ui.css'))
trontastic = Resource(library, 'themes/trontastic/jquery-ui.css',
    cdns=cdnify('themes/trontastic/jquery-ui.css'))
ui_darkness = Resource(library, 'themes/ui-darkness/jquery-ui.css',
    cdns=cdnify('themes/ui-darkness/jquery-ui.css'))
ui_lightness = Resource(library, 'themes/ui-lightness/jquery-ui.css',
    cdns=cdnify('themes/ui-lightness/jquery-ui.css'))
vader = Resource(library, 'themes/vader/jquery-ui.css',
    cdns=cdnify('themes/vader/jquery-ui.css'))
