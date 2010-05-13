# pipestrconcat.py  #aka stringbuilder
#

from pipe2py import util

def pipe_strconcat(context, _INPUT, conf, **kwargs):
    """This source builds a string and yields it forever.
    
    Keyword arguments:
    context -- pipeline context
    _INPUT -- not used
    conf:
        part -- parts
    
    Yields (_OUTPUT):
    string
    """
    s = ""
    for part in conf['part']:
        if "subkey" in part:
            pass   #todo get from _INPUT e.g {u'type': u'text', u'subkey': u'severity'}
        else:
            s += util.get_value(part, kwargs)

    while True:
        yield s

