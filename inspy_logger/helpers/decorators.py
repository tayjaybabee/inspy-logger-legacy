"""

A module to hold any decorator patterns we need

"""


def singleton(targClass):
    instances = {}

    def getInstance(*args, **kwargs):
        if targClass not in instances:
            instances[targClass] = targClass(*args, **kwargs)

        return instances[targClass]
    return getInstance
