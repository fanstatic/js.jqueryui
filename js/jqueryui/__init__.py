from fanstatic import Library, Resource, Group
import js.jquery

# This code is auto-generated and not PEP8 compliant

library = Library('jqueryui', 'resources')

ui_core = Resource(
    library,
    'ui/core.js',
    depends=[js.jquery.jquery],
    minified='ui/core.min.js')
ui_datepicker = Resource(
    library,
    'ui/widgets/datepicker.js',
    depends=[ui_core],
    minified='ui/widgets/datepicker.min.js')
ui_position = Resource(
    library,
    'ui/position.js',
    depends=[js.jquery.jquery],
    minified='ui/position.min.js')
ui_widget = Resource(
    library,
    'ui/widget.js',
    depends=[js.jquery.jquery],
    minified='ui/widget.min.js')
ui_menu = Resource(
    library,
    'ui/widgets/menu.js',
    depends=[ui_core, ui_widget, ui_position],
    minified='ui/widgets/menu.min.js')
ui_accordion = Resource(
    library,
    'ui/widgets/accordion.js',
    depends=[ui_core, ui_widget],
    minified='ui/widgets/accordion.min.js')
ui_autocomplete = Resource(
    library,
    'ui/widgets/autocomplete.js',
    depends=[ui_core, ui_position, ui_widget, ui_menu],
    minified='ui/widgets/autocomplete.min.js')
ui_button = Resource(
    library,
    'ui/widgets/button.js',
    depends=[ui_core, ui_widget],
    minified='ui/widgets/button.min.js')
ui_dialog = Resource(
    library,
    'ui/widgets/dialog.js',
    depends=[ui_core, ui_position, ui_widget],
    minified='ui/widgets/dialog.min.js')
ui_mouse = Resource(
    library,
    'ui/widgets/mouse.js',
    depends=[ui_core, ui_widget],
    minified='ui/widgets/mouse.min.js')
ui_draggable = Resource(
    library,
    'ui/widgets/draggable.js',
    depends=[ui_core, ui_mouse, ui_widget],
    minified='ui/widgets/draggable.min.js')
ui_droppable = Resource(
    library,
    'ui/widgets/droppable.js',
    depends=[ui_core, ui_draggable, ui_mouse, ui_widget],
    minified='ui/widgets/droppable.min.js')
ui_progressbar = Resource(
    library,
    'ui/widgets/progressbar.js',
    depends=[ui_core, ui_widget],
    minified='ui/widgets/progressbar.min.js')
ui_resizable = Resource(
    library,
    'ui/widgets/resizable.js',
    depends=[ui_core, ui_mouse, ui_widget],
    minified='ui/widgets/resizable.min.js')
ui_selectable = Resource(
    library,
    'ui/widgets/selectable.js',
    depends=[ui_core, ui_mouse, ui_widget],
    minified='ui/widgets/selectable.min.js')
ui_slider = Resource(
    library,
    'ui/widgets/slider.js',
    depends=[ui_core, ui_mouse, ui_widget],
    minified='ui/widgets/slider.min.js')
ui_sortable = Resource(
    library,
    'ui/widgets/sortable.js',
    depends=[ui_core, ui_mouse, ui_widget],
    minified='ui/widgets/sortable.min.js')
ui_spinner = Resource(
    library,
    'ui/widgets/spinner.js',
    depends=[ui_core, ui_widget, ui_button],
    minified='ui/widgets/spinner.min.js')
ui_tabs = Resource(
    library,
    'ui/widgets/tabs.js',
    depends=[ui_core, ui_widget],
    minified='ui/widgets/tabs.min.js')
ui_tooltip = Resource(
    library,
    'ui/widgets/tooltip.js',
    depends=[ui_core, ui_widget, ui_position],
    minified='ui/widgets/tooltip.min.js')

effects_core = Resource(
    library,
    'ui/effect.js',
    depends=[js.jquery.jquery],
    minified='ui/effect.min.js')
effects_blind = Resource(
    library,
    'ui/effects/effect-blind.js',
    depends=[effects_core],
    minified='ui/effects/effect-blind.min.js')
effects_bounce = Resource(
    library,
    'ui/effects/effect-bounce.js',
    depends=[effects_core],
    minified='ui/effects/effect-bounce.min.js')
effects_clip = Resource(
    library,
    'ui/effects/effect-clip.js',
    depends=[effects_core],
    minified='ui/effects/effect-clip.min.js')
effects_drop = Resource(
    library,
    'ui/effects/effect-drop.js',
    depends=[effects_core],
    minified='ui/effects/effect-drop.min.js')
effects_explode = Resource(
    library,
    'ui/effects/effect-explode.js',
    depends=[effects_core],
    minified='ui/effects/effect-explode.min.js')
effects_fade = Resource(
    library,
    'ui/effects/effect-fade.js',
    depends=[effects_core],
    minified='ui/effects/effect-fade.min.js')
effects_fold = Resource(
    library,
    'ui/effects/effect-fold.js',
    depends=[effects_core],
    minified='ui/effects/effect-fold.min.js')
effects_highlight = Resource(
    library,
    'ui/effects/effect-highlight.js',
    depends=[effects_core],
    minified='ui/effects/effect-highlight.min.js')
effects_pulsate = Resource(
    library,
    'ui/effects/effect-pulsate.js',
    depends=[effects_core],
    minified='ui/effects/effect-pulsate.min.js')
effects_scale = Resource(
    library,
    'ui/effects/effect-scale.js',
    depends=[effects_core],
    minified='ui/effects/effect-scale.min.js')
effects_shake = Resource(
    library,
    'ui/effects/effect-shake.js',
    depends=[effects_core],
    minified='ui/effects/effect-shake.min.js')
effects_slide = Resource(
    library,
    'ui/effects/effect-slide.js',
    depends=[effects_core],
    minified='ui/effects/effect-slide.min.js')
effects_transfer = Resource(
    library,
    'ui/effects/effect-transfer.js',
    depends=[effects_core],
    minified='ui/effects/effect-transfer.min.js')

jqueryui = Resource(
    library,
    'ui/jquery-ui.js',
    depends=[js.jquery.jquery],
    minified='ui/jquery-ui.min.js',
    supersedes=[effects_blind, effects_bounce, effects_clip, effects_core,
                effects_drop, effects_explode, effects_fade, effects_fold,
                effects_highlight, effects_pulsate, effects_scale,
                effects_shake, effects_slide, effects_transfer, ui_accordion,
                ui_autocomplete, ui_button, ui_core, ui_datepicker, ui_dialog,
                ui_draggable, ui_droppable, ui_menu, ui_mouse, ui_position,
                ui_progressbar, ui_resizable, ui_selectable, ui_slider,
                ui_sortable, ui_spinner, ui_tabs, ui_tooltip, ui_widget])

base = Resource(
    library,
    'themes/base/jquery-ui.css',
    minified='themes/base/jquery-ui.min.css')
black_tie = Resource(
    library,
    'themes/black-tie/jquery-ui.css',
    minified='themes/black-tie/jquery-ui.min.css')
blitzer = Resource(
    library,
    'themes/blitzer/jquery-ui.css',
    minified='themes/blitzer/jquery-ui.min.css')
cupertino = Resource(
    library,
    'themes/cupertino/jquery-ui.css',
    minified='themes/cupertino/jquery-ui.min.css')
dark_hive = Resource(
    library,
    'themes/dark-hive/jquery-ui.css',
    minified='themes/dark-hive/jquery-ui.min.css')
dot_luv = Resource(
    library,
    'themes/dot-luv/jquery-ui.css',
    minified='themes/dot-luv/jquery-ui.min.css')
eggplant = Resource(
    library,
    'themes/eggplant/jquery-ui.css',
    minified='themes/eggplant/jquery-ui.min.css')
excite_bike = Resource(
    library,
    'themes/excite-bike/jquery-ui.css',
    minified='themes/excite-bike/jquery-ui.min.css')
flick = Resource(
    library,
    'themes/flick/jquery-ui.css',
    minified='themes/flick/jquery-ui.min.css')
hot_sneaks = Resource(
    library,
    'themes/hot-sneaks/jquery-ui.css',
    minified='themes/hot-sneaks/jquery-ui.min.css')
humanity = Resource(
    library,
    'themes/humanity/jquery-ui.css',
    minified='themes/humanity/jquery-ui.min.css')
le_frog = Resource(
    library,
    'themes/le-frog/jquery-ui.css',
    minified='themes/le-frog/jquery-ui.min.css')
mint_choc = Resource(
    library,
    'themes/mint-choc/jquery-ui.css',
    minified='themes/mint-choc/jquery-ui.min.css')
overcast = Resource(
    library,
    'themes/overcast/jquery-ui.css',
    minified='themes/overcast/jquery-ui.min.css')
pepper_grinder = Resource(
    library,
    'themes/pepper-grinder/jquery-ui.css',
    minified='themes/pepper-grinder/jquery-ui.min.css')
redmond = Resource(
    library,
    'themes/redmond/jquery-ui.css',
    minified='themes/redmond/jquery-ui.min.css')
smoothness = Resource(
    library,
    'themes/smoothness/jquery-ui.css',
    minified='themes/smoothness/jquery-ui.min.css')
south_street = Resource(
    library,
    'themes/south-street/jquery-ui.css',
    minified='themes/south-street/jquery-ui.min.css')
start = Resource(
    library,
    'themes/start/jquery-ui.css',
    minified='themes/start/jquery-ui.min.css')
sunny = Resource(
    library,
    'themes/sunny/jquery-ui.css',
    minified='themes/sunny/jquery-ui.min.css')
swanky_purse = Resource(
    library,
    'themes/swanky-purse/jquery-ui.css',
    minified='themes/swanky-purse/jquery-ui.min.css')
trontastic = Resource(
    library,
    'themes/trontastic/jquery-ui.css',
    minified='themes/trontastic/jquery-ui.min.css')
ui_darkness = Resource(
    library,
    'themes/ui-darkness/jquery-ui.css',
    minified='themes/ui-darkness/jquery-ui.min.css')
ui_lightness = Resource(
    library,
    'themes/ui-lightness/jquery-ui.css',
    minified='themes/ui-lightness/jquery-ui.min.css')
vader = Resource(
    library,
    'themes/vader/jquery-ui.css',
    minified='themes/vader/jquery-ui.min.css')

ui_datepicker_af = Resource(
    library,
    'ui/i18n/datepicker-af.js',
    minified='ui/i18n/datepicker-af.min.js',
    depends=[ui_datepicker])
ui_datepicker_ar = Resource(
    library,
    'ui/i18n/datepicker-ar.js',
    minified='ui/i18n/datepicker-ar.min.js',
    depends=[ui_datepicker])
ui_datepicker_ar_DZ = Resource(
    library,
    'ui/i18n/datepicker-ar-DZ.js',
    minified='ui/i18n/datepicker-ar-DZ.min.js',
    depends=[ui_datepicker])
ui_datepicker_az = Resource(
    library,
    'ui/i18n/datepicker-az.js',
    minified='ui/i18n/datepicker-az.min.js',
    depends=[ui_datepicker])
ui_datepicker_be = Resource(
    library,
    'ui/i18n/datepicker-be.js',
    minified='ui/i18n/datepicker-be.min.js',
    depends=[ui_datepicker])
ui_datepicker_bg = Resource(
    library,
    'ui/i18n/datepicker-bg.js',
    minified='ui/i18n/datepicker-bg.min.js',
    depends=[ui_datepicker])
ui_datepicker_bs = Resource(
    library,
    'ui/i18n/datepicker-bs.js',
    minified='ui/i18n/datepicker-bs.min.js',
    depends=[ui_datepicker])
ui_datepicker_ca = Resource(
    library,
    'ui/i18n/datepicker-ca.js',
    minified='ui/i18n/datepicker-ca.min.js',
    depends=[ui_datepicker])
ui_datepicker_cs = Resource(
    library,
    'ui/i18n/datepicker-cs.js',
    minified='ui/i18n/datepicker-cs.min.js',
    depends=[ui_datepicker])
ui_datepicker_cy_GB = Resource(
    library,
    'ui/i18n/datepicker-cy-GB.js',
    minified='ui/i18n/datepicker-cy-GB.min.js',
    depends=[ui_datepicker])
ui_datepicker_da = Resource(
    library,
    'ui/i18n/datepicker-da.js',
    minified='ui/i18n/datepicker-da.min.js',
    depends=[ui_datepicker])
ui_datepicker_de = Resource(
    library,
    'ui/i18n/datepicker-de.js',
    minified='ui/i18n/datepicker-de.min.js',
    depends=[ui_datepicker])
ui_datepicker_el = Resource(
    library,
    'ui/i18n/datepicker-el.js',
    minified='ui/i18n/datepicker-el.min.js',
    depends=[ui_datepicker])
ui_datepicker_en_AU = Resource(
    library,
    'ui/i18n/datepicker-en-AU.js',
    minified='ui/i18n/datepicker-en-AU.min.js',
    depends=[ui_datepicker])
ui_datepicker_en_GB = Resource(
    library,
    'ui/i18n/datepicker-en-GB.js',
    minified='ui/i18n/datepicker-en-GB.min.js',
    depends=[ui_datepicker])
ui_datepicker_en_NZ = Resource(
    library,
    'ui/i18n/datepicker-en-NZ.js',
    minified='ui/i18n/datepicker-en-NZ.min.js',
    depends=[ui_datepicker])
ui_datepicker_eo = Resource(
    library,
    'ui/i18n/datepicker-eo.js',
    minified='ui/i18n/datepicker-eo.min.js',
    depends=[ui_datepicker])
ui_datepicker_es = Resource(
    library,
    'ui/i18n/datepicker-es.js',
    minified='ui/i18n/datepicker-es.min.js',
    depends=[ui_datepicker])
ui_datepicker_et = Resource(
    library,
    'ui/i18n/datepicker-et.js',
    minified='ui/i18n/datepicker-et.min.js',
    depends=[ui_datepicker])
ui_datepicker_eu = Resource(
    library,
    'ui/i18n/datepicker-eu.js',
    minified='ui/i18n/datepicker-eu.min.js',
    depends=[ui_datepicker])
ui_datepicker_fa = Resource(
    library,
    'ui/i18n/datepicker-fa.js',
    minified='ui/i18n/datepicker-fa.min.js',
    depends=[ui_datepicker])
ui_datepicker_fi = Resource(
    library,
    'ui/i18n/datepicker-fi.js',
    minified='ui/i18n/datepicker-fi.min.js',
    depends=[ui_datepicker])
ui_datepicker_fo = Resource(
    library,
    'ui/i18n/datepicker-fo.js',
    minified='ui/i18n/datepicker-fo.min.js',
    depends=[ui_datepicker])
ui_datepicker_fr = Resource(
    library,
    'ui/i18n/datepicker-fr.js',
    minified='ui/i18n/datepicker-fr.min.js',
    depends=[ui_datepicker])
ui_datepicker_fr_CA = Resource(
    library,
    'ui/i18n/datepicker-fr-CA.js',
    minified='ui/i18n/datepicker-fr-CA.min.js',
    depends=[ui_datepicker])
ui_datepicker_fr_CH = Resource(
    library,
    'ui/i18n/datepicker-fr-CH.js',
    minified='ui/i18n/datepicker-fr-CH.min.js',
    depends=[ui_datepicker])
ui_datepicker_gl = Resource(
    library,
    'ui/i18n/datepicker-gl.js',
    minified='ui/i18n/datepicker-gl.min.js',
    depends=[ui_datepicker])
ui_datepicker_he = Resource(
    library,
    'ui/i18n/datepicker-he.js',
    minified='ui/i18n/datepicker-he.min.js',
    depends=[ui_datepicker])
ui_datepicker_hi = Resource(
    library,
    'ui/i18n/datepicker-hi.js',
    minified='ui/i18n/datepicker-hi.min.js',
    depends=[ui_datepicker])
ui_datepicker_hr = Resource(
    library,
    'ui/i18n/datepicker-hr.js',
    minified='ui/i18n/datepicker-hr.min.js',
    depends=[ui_datepicker])
ui_datepicker_hu = Resource(
    library,
    'ui/i18n/datepicker-hu.js',
    minified='ui/i18n/datepicker-hu.min.js',
    depends=[ui_datepicker])
ui_datepicker_hy = Resource(
    library,
    'ui/i18n/datepicker-hy.js',
    minified='ui/i18n/datepicker-hy.min.js',
    depends=[ui_datepicker])
ui_datepicker_id = Resource(
    library,
    'ui/i18n/datepicker-id.js',
    minified='ui/i18n/datepicker-id.min.js',
    depends=[ui_datepicker])
ui_datepicker_is = Resource(
    library,
    'ui/i18n/datepicker-is.js',
    minified='ui/i18n/datepicker-is.min.js',
    depends=[ui_datepicker])
ui_datepicker_it = Resource(
    library,
    'ui/i18n/datepicker-it.js',
    minified='ui/i18n/datepicker-it.min.js',
    depends=[ui_datepicker])
ui_datepicker_ja = Resource(
    library,
    'ui/i18n/datepicker-ja.js',
    minified='ui/i18n/datepicker-ja.min.js',
    depends=[ui_datepicker])
ui_datepicker_ka = Resource(
    library,
    'ui/i18n/datepicker-ka.js',
    minified='ui/i18n/datepicker-ka.min.js',
    depends=[ui_datepicker])
ui_datepicker_kk = Resource(
    library,
    'ui/i18n/datepicker-kk.js',
    minified='ui/i18n/datepicker-kk.min.js',
    depends=[ui_datepicker])
ui_datepicker_km = Resource(
    library,
    'ui/i18n/datepicker-km.js',
    minified='ui/i18n/datepicker-km.min.js',
    depends=[ui_datepicker])
ui_datepicker_ko = Resource(
    library,
    'ui/i18n/datepicker-ko.js',
    minified='ui/i18n/datepicker-ko.min.js',
    depends=[ui_datepicker])
ui_datepicker_ky = Resource(
    library,
    'ui/i18n/datepicker-ky.js',
    minified='ui/i18n/datepicker-ky.min.js',
    depends=[ui_datepicker])
ui_datepicker_lb = Resource(
    library,
    'ui/i18n/datepicker-lb.js',
    minified='ui/i18n/datepicker-lb.min.js',
    depends=[ui_datepicker])
ui_datepicker_lt = Resource(
    library,
    'ui/i18n/datepicker-lt.js',
    minified='ui/i18n/datepicker-lt.min.js',
    depends=[ui_datepicker])
ui_datepicker_lv = Resource(
    library,
    'ui/i18n/datepicker-lv.js',
    minified='ui/i18n/datepicker-lv.min.js',
    depends=[ui_datepicker])
ui_datepicker_mk = Resource(
    library,
    'ui/i18n/datepicker-mk.js',
    minified='ui/i18n/datepicker-mk.min.js',
    depends=[ui_datepicker])
ui_datepicker_ml = Resource(
    library,
    'ui/i18n/datepicker-ml.js',
    minified='ui/i18n/datepicker-ml.min.js',
    depends=[ui_datepicker])
ui_datepicker_ms = Resource(
    library,
    'ui/i18n/datepicker-ms.js',
    minified='ui/i18n/datepicker-ms.min.js',
    depends=[ui_datepicker])
ui_datepicker_nb = Resource(
    library,
    'ui/i18n/datepicker-nb.js',
    minified='ui/i18n/datepicker-nb.min.js',
    depends=[ui_datepicker])
ui_datepicker_nl = Resource(
    library,
    'ui/i18n/datepicker-nl.js',
    minified='ui/i18n/datepicker-nl.min.js',
    depends=[ui_datepicker])
ui_datepicker_nl_BE = Resource(
    library,
    'ui/i18n/datepicker-nl-BE.js',
    minified='ui/i18n/datepicker-nl-BE.min.js',
    depends=[ui_datepicker])
ui_datepicker_no = Resource(
    library,
    'ui/i18n/datepicker-no.js',
    minified='ui/i18n/datepicker-no.min.js',
    depends=[ui_datepicker])
ui_datepicker_nn = Resource(
    library,
    'ui/i18n/datepicker-nn.js',
    minified='ui/i18n/datepicker-nn.min.js',
    depends=[ui_datepicker])
ui_datepicker_pl = Resource(
    library,
    'ui/i18n/datepicker-pl.js',
    minified='ui/i18n/datepicker-pl.min.js',
    depends=[ui_datepicker])
ui_datepicker_pt = Resource(
    library,
    'ui/i18n/datepicker-pt.js',
    minified='ui/i18n/datepicker-pt.min.js',
    depends=[ui_datepicker])
ui_datepicker_pt_BR = Resource(
    library,
    'ui/i18n/datepicker-pt-BR.js',
    minified='ui/i18n/datepicker-pt-BR.min.js',
    depends=[ui_datepicker])
ui_datepicker_rm = Resource(
    library,
    'ui/i18n/datepicker-rm.js',
    minified='ui/i18n/datepicker-rm.min.js',
    depends=[ui_datepicker])
ui_datepicker_ro = Resource(
    library,
    'ui/i18n/datepicker-ro.js',
    minified='ui/i18n/datepicker-ro.min.js',
    depends=[ui_datepicker])
ui_datepicker_ru = Resource(
    library,
    'ui/i18n/datepicker-ru.js',
    minified='ui/i18n/datepicker-ru.min.js',
    depends=[ui_datepicker])
ui_datepicker_sk = Resource(
    library,
    'ui/i18n/datepicker-sk.js',
    minified='ui/i18n/datepicker-sk.min.js',
    depends=[ui_datepicker])
ui_datepicker_sl = Resource(
    library,
    'ui/i18n/datepicker-sl.js',
    minified='ui/i18n/datepicker-sl.min.js',
    depends=[ui_datepicker])
ui_datepicker_sq = Resource(
    library,
    'ui/i18n/datepicker-sq.js',
    minified='ui/i18n/datepicker-sq.min.js',
    depends=[ui_datepicker])
ui_datepicker_sr = Resource(
    library,
    'ui/i18n/datepicker-sr.js',
    minified='ui/i18n/datepicker-sr.min.js',
    depends=[ui_datepicker])
ui_datepicker_sr_SR = Resource(
    library,
    'ui/i18n/datepicker-sr-SR.js',
    minified='ui/i18n/datepicker-sr-SR.min.js',
    depends=[ui_datepicker])
ui_datepicker_sv = Resource(
    library,
    'ui/i18n/datepicker-sv.js',
    minified='ui/i18n/datepicker-sv.min.js',
    depends=[ui_datepicker])
ui_datepicker_ta = Resource(
    library,
    'ui/i18n/datepicker-ta.js',
    minified='ui/i18n/datepicker-ta.min.js',
    depends=[ui_datepicker])
ui_datepicker_th = Resource(
    library,
    'ui/i18n/datepicker-th.js',
    minified='ui/i18n/datepicker-th.min.js',
    depends=[ui_datepicker])
ui_datepicker_tj = Resource(
    library,
    'ui/i18n/datepicker-tj.js',
    minified='ui/i18n/datepicker-tj.min.js',
    depends=[ui_datepicker])
ui_datepicker_tr = Resource(
    library,
    'ui/i18n/datepicker-tr.js',
    minified='ui/i18n/datepicker-tr.min.js',
    depends=[ui_datepicker])
ui_datepicker_uk = Resource(
    library,
    'ui/i18n/datepicker-uk.js',
    minified='ui/i18n/datepicker-uk.min.js',
    depends=[ui_datepicker])
ui_datepicker_vi = Resource(
    library,
    'ui/i18n/datepicker-vi.js',
    minified='ui/i18n/datepicker-vi.min.js',
    depends=[ui_datepicker])
ui_datepicker_zh_CN = Resource(
    library,
    'ui/i18n/datepicker-zh-CN.js',
    minified='ui/i18n/datepicker-zh-CN.min.js',
    depends=[ui_datepicker])
ui_datepicker_zh_HK = Resource(
    library,
    'ui/i18n/datepicker-zh-HK.js',
    minified='ui/i18n/datepicker-zh-HK.min.js',
    depends=[ui_datepicker])
ui_datepicker_zh_TW = Resource(
    library,
    'ui/i18n/datepicker-zh-TW.js',
    minified='ui/i18n/datepicker-zh-TW.min.js',
    depends=[ui_datepicker])
jqueryui_i18n = Group([
    ui_datepicker_af, ui_datepicker_ar, ui_datepicker_ar_DZ,
    ui_datepicker_az, ui_datepicker_bg, ui_datepicker_bs,
    ui_datepicker_ca, ui_datepicker_cs, ui_datepicker_da,
    ui_datepicker_de, ui_datepicker_el, ui_datepicker_en_AU,
    ui_datepicker_en_GB, ui_datepicker_en_NZ, ui_datepicker_eo,
    ui_datepicker_es, ui_datepicker_et, ui_datepicker_eu,
    ui_datepicker_fa, ui_datepicker_fi, ui_datepicker_fo,
    ui_datepicker_fr, ui_datepicker_fr_CH, ui_datepicker_gl,
    ui_datepicker_he, ui_datepicker_hr, ui_datepicker_hu,
    ui_datepicker_hy, ui_datepicker_id, ui_datepicker_is,
    ui_datepicker_it, ui_datepicker_ja, ui_datepicker_ko,
    ui_datepicker_lt, ui_datepicker_lv,
    ui_datepicker_ml, ui_datepicker_ms, ui_datepicker_nl,
    ui_datepicker_no, ui_datepicker_pl, ui_datepicker_pt,
    ui_datepicker_pt_BR, ui_datepicker_rm, ui_datepicker_ro,
    ui_datepicker_ru, ui_datepicker_sk, ui_datepicker_sl,
    ui_datepicker_sq, ui_datepicker_sr, ui_datepicker_sr_SR,
    ui_datepicker_sv, ui_datepicker_ta, ui_datepicker_th,
    ui_datepicker_tj, ui_datepicker_tr, ui_datepicker_uk,
    ui_datepicker_vi, ui_datepicker_zh_CN, ui_datepicker_zh_HK,
    ui_datepicker_zh_TW, ui_datepicker_cy_GB, ui_datepicker_hi,
    ui_datepicker_ka, ui_datepicker_kk, ui_datepicker_km,
    ui_datepicker_lb, ui_datepicker_mk, ui_datepicker_nl_BE])

ui_datepicker_locales = {
    "af": ui_datepicker_af,
    "ar": ui_datepicker_ar,
    "ar_DZ": ui_datepicker_ar_DZ,
    "az": ui_datepicker_az,
    "be": ui_datepicker_be,
    "bg": ui_datepicker_bg,
    "bs": ui_datepicker_bs,
    "ca": ui_datepicker_ca,
    "cs": ui_datepicker_cs,
    "cy_GB": ui_datepicker_cy_GB,
    "da": ui_datepicker_da,
    "de": ui_datepicker_de,
    "el": ui_datepicker_el,
    "en_AU": ui_datepicker_en_AU,
    "en_GB": ui_datepicker_en_GB,
    "en_NZ": ui_datepicker_en_NZ,
    "eo": ui_datepicker_eo,
    "es": ui_datepicker_es,
    "et": ui_datepicker_et,
    "eu": ui_datepicker_eu,
    "fa": ui_datepicker_fa,
    "fi": ui_datepicker_fi,
    "fo": ui_datepicker_fo,
    "fr": ui_datepicker_fr,
    "fr_CA": ui_datepicker_fr_CA,
    "fr_CH": ui_datepicker_fr_CH,
    "gl": ui_datepicker_gl,
    "he": ui_datepicker_he,
    "hi": ui_datepicker_hi,
    "hr": ui_datepicker_hr,
    "hu": ui_datepicker_hu,
    "hy": ui_datepicker_hy,
    "id": ui_datepicker_id,
    "is": ui_datepicker_is,
    "it": ui_datepicker_it,
    "ja": ui_datepicker_ja,
    "ka": ui_datepicker_ka,
    "kk": ui_datepicker_kk,
    "km": ui_datepicker_km,
    "ko": ui_datepicker_ko,
    "ky": ui_datepicker_ky,
    "lb": ui_datepicker_lb,
    "lt": ui_datepicker_lt,
    "lv": ui_datepicker_lv,
    "mk": ui_datepicker_mk,
    "ml": ui_datepicker_ml,
    "ms": ui_datepicker_ms,
    "nb": ui_datepicker_nb,
    "nl": ui_datepicker_nl,
    "nl_BE": ui_datepicker_nl_BE,
    "nn": ui_datepicker_nn,
    "no": ui_datepicker_no,
    "pl": ui_datepicker_pl,
    "pt": ui_datepicker_pt,
    "pt_BR": ui_datepicker_pt_BR,
    "rm": ui_datepicker_rm,
    "ro": ui_datepicker_ro,
    "ru": ui_datepicker_ru,
    "sk": ui_datepicker_sk,
    "sl": ui_datepicker_sl,
    "sq": ui_datepicker_sq,
    "sr": ui_datepicker_sr,
    "sr_SR": ui_datepicker_sr_SR,
    "sv": ui_datepicker_sv,
    "ta": ui_datepicker_ta,
    "th": ui_datepicker_th,
    "tj": ui_datepicker_tj,
    "tr": ui_datepicker_tr,
    "uk": ui_datepicker_uk,
    "vi": ui_datepicker_vi,
    "zh_CN": ui_datepicker_zh_CN,
    "zh_HK": ui_datepicker_zh_HK,
    "zh_TW": ui_datepicker_zh_TW,
}
