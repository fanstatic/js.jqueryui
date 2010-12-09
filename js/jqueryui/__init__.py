from fanstatic import Library, ResourceInclusion
import js.jquery

library = Library('jqueryui', 'resources')

jqueryui = ResourceInclusion(library, 'ui/jquery-ui.js',
    minified='ui/minified/jquery-ui.min.js',
    depends=[js.jquery.jquery])

base = ResourceInclusion(library, 'themes/base/jquery-ui.css',
                         minified='themes/base/minified/jquery-ui.min.css')
black_tie = ResourceInclusion(library, 'themes/black-tie/jquery-ui.css')
blitzer = ResourceInclusion(library, 'themes/blitzer/jquery-ui.css')
cupertino = ResourceInclusion(library, 'themes/cupertino/jquery-ui.css')
dark_hive = ResourceInclusion(library, 'themes/dark-hive/jquery-ui.css')
dot_luv = ResourceInclusion(library, 'themes/dot-luv/jquery-ui.css')
eggplant = ResourceInclusion(library, 'themes/eggplant/jquery-ui.css')
excite_bike = ResourceInclusion(library, 'themes/excite-bike/jquery-ui.css')
flick = ResourceInclusion(library, 'themes/flick/jquery-ui.css')
hot_sneaks = ResourceInclusion(library, 'themes/hot-sneaks/jquery-ui.css')
humanity = ResourceInclusion(library, 'themes/humanity/jquery-ui.css')
le_frog = ResourceInclusion(library, 'themes/le-frog/jquery-ui.css')
mint_choc = ResourceInclusion(library, 'themes/mint-choc/jquery-ui.css')
overcast = ResourceInclusion(library, 'themes/overcast/jquery-ui.css')
pepper_grinder = ResourceInclusion(library, 'themes/pepper-grinder/jquery-ui.css')
redmond = ResourceInclusion(library, 'themes/redmond/jquery-ui.css')
smoothness = ResourceInclusion(library, 'themes/smoothness/jquery-ui.css')
south_street = ResourceInclusion(library, 'themes/south-street/jquery-ui.css')
start = ResourceInclusion(library, 'themes/start/jquery-ui.css')
sunny = ResourceInclusion(library, 'themes/sunny/jquery-ui.css')
swanky_purse = ResourceInclusion(library, 'themes/swanky-purse/jquery-ui.css')
trontastic = ResourceInclusion(library, 'themes/trontastic/jquery-ui.css')
ui_darkness = ResourceInclusion(library, 'themes/ui-darkness/jquery-ui.css')
ui_lightness = ResourceInclusion(library, 'themes/ui-lightness/jquery-ui.css')
vader = ResourceInclusion(library, 'themes/vader/jquery-ui.css')
