import helper

import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()

file_path = tkFileDialog.askopenfilename()

pic = helper.PencilSketch()

pic.render(file_path.encode('utf-8'))

exit()

