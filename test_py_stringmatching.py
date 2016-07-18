import py_stringmatching as sm
print('install path : ' + sm.get_install_path())
print('version : ' + sm.__version__)
l = sm.Levenshtein()
print('edit dist : ' + str(l.get_raw_score('ag', 'dg')))
q = sm.QgramTokenizer()
print('prefix pad : ' + q.get_prefix_pad())

