def get_file():
    import tkinter
    from tkinter import filedialog
    import os

    root = tkinter.Tk()
    root.withdraw()
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory in which your file is situated or has to be saved')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    file_path_variable = tempdir
    return file_path_variable