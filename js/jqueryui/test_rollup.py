"""

To trigger it, you just need to include in a project jqueryui.jqueryui and
jqueryui.jqueryui_i18n.

The bug is really easy: jqueryui.jqueryui is a rollup containing
jqueryui.ui_core, jqueryui.ui_datepicker and other things.
jqueryui.jqueryui_i18n is a rollup container all jquery.ui_datepicker_language,
and depends on jqueryui.ui_datepicker (who itself depends on jqueryui.ui_core).

Now when you include both of them you end-up with the jquery-ui rollup, after
jqueryui-core (already contained in the rollup) and jqueryui-datepicker
(already contained in the rollup) before the rollup with the datepicker
translations. So at the end you have two times jquery-core and jquery-datetime
(one time in the rollup and one time after).

My problem is that if you include two times those files, like it is done now,
this breaks the z-Index option of jqueryui dialogs on Internet Explorer.

"""

from fanstatic import Inclusion, NeededResources
from js.jqueryui import jqueryui, jqueryui_i18n

def test_rollup_resources():
    needed = NeededResources(resources=[jqueryui, jqueryui_i18n])
    incl = Inclusion(needed)
    assert incl.render() == '''<script type="text/javascript" src="/fanstatic/jquery/jquery.js"></script>
<script type="text/javascript" src="/fanstatic/jqueryui/ui/jquery-ui.js"></script>
<script type="text/javascript" src="/fanstatic/jqueryui/ui/i18n/jquery-ui-i18n.js"></script>'''

