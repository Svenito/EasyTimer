import os
env = Environment(ENV = os.environ )

uic_builder_py = Builder(
        action = 'pyuic4 $SOURCE -o $TARGET',
        suffix = '.py',
        src_suffix = '.ui',
        single_source = True)

res_builder_py = Builder(
        action = 'pyrcc4 $SOURCE -o $TARGET',
        suffix = '.py',
        src_suffix = '.qrc',
        single_source = True)

env.Append( BUILDERS = { 'ResPy': res_builder_py } )
env.Append( BUILDERS = { 'FormPy': uic_builder_py } )

uis = []
uis.append(env.FormPy( 'ui/timerUI.py', source = 'timer.ui' ) )

res = []
