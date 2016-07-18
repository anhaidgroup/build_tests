import py_stringsimjoin as ssj

if __name__ == '__main__':
    print('install path : ' + ssj.get_install_path())
    print('version : ' + ssj.__version__)
    A, B = ssj.load_books_dataset()
    C = ssj.edit_distance_join(A, B, 'ID', 'ID', 'Title', 'Title', 2)
    print('testing edit dist join (single core) : ' + str(len(C)))
    C = ssj.edit_distance_join(A, B, 'ID', 'ID', 'Title', 'Title', 2, n_jobs=-1)
    print('testing edit dist join (multi core) : ' + str(len(C)))                  
