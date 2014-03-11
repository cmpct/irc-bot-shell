import imp
import os

plugindir= "./plugins"
main = "plugin"

def getPlugins():
    plugins = []
    findplugins = os.listdir(plugindir)
    for i in findplugins:
        location = os.path.join(plugindir, i)
        if not os.path.isdir(location) or not main + ".py" in os.listdir(location):
            continue
        info = imp.find_module(main, [location])
        plugins.append({"name": i, "info": info})
    return plugins

def loadPlugin(plugin):
    return imp.load_module(main, *plugin["info"])
