__author__ = 'svalleru'


class Installer(object):
    installed = []
    def __init__(self, name):
        # Basically a graph data structure
        self.name = name
        self.deps = []

    def make_dep(self, node):
        if node not in self.deps:
            self.deps.append(node)

    def install(self):
        # install all depedencies & pkg
        resolved = []
        Installer.resolver(self, resolved, [])
        for node in resolved:
            print "Installing..", node.name
            Installer.installed.append(node.name)

    def remove(self):
        # remove all depedencies & pkg
        # TBD: olny remove unshared deps
        resolved = []
        Installer.resolver(self, resolved, [])
        for node in resolved:
            print "Removing..", node.name
            Installer.installed.remove(node.name)

    def resolver(node, resolved, unresolved):
        unresolved.append(node)
        for dep in node.deps:
            if dep not in resolved:  # check if a dep is already resolved
                if dep in unresolved:  # check for circular depedency
                    raise Exception('Circular depedencies detected: %s -> %s' % (node.name, dep.name))
                Installer.resolver(dep, resolved, unresolved)
        resolved.append(node)
        unresolved.remove(node)


# a = Installer('a')
# b = Installer('b')
# c = Installer('c')
# d = Installer('d')
# e = Installer('e')
#
# a.make_dep(b)    # a depends on b
# a.make_dep(d)    # a depends on d
# b.make_dep(c)    # b depends on c
# b.make_dep(e)    # b depends on e
# c.make_dep(d)    # c depends on d
# c.make_dep(e)    # c depends on e
#
# b.install()
# print Installer.installed
# b.remove()
# print Installer.installed
