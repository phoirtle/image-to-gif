import imageio.v3 as iio

filenames = [r"C:\Users\Lenovo\Pemkom\.vscode\Python\Projects2\nyan-cat1.png", 
             r"C:\Users\Lenovo\Pemkom\.vscode\Python\Projects2\nyan-cat2.png", 
             r"C:\Users\Lenovo\Pemkom\.vscode\Python\Projects2\nyan-cat3.png"]

images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

  iio.imwrite('cat.gif', images, duration = 500, loop = 0)

