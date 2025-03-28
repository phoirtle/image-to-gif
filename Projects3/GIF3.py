import imageio.v3 as iio

filenames = [r"C:\Users\Lenovo\Pemkom\.vscode\Python\Projects3\Karin1.jpg", 
             r"C:\Users\Lenovo\Pemkom\.vscode\Python\Projects3\Karin2.jpg", 
             r"C:\Users\Lenovo\Pemkom\.vscode\Python\Projects3\Karin3.jpg"]

images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

  iio.imwrite('karina.gif', images, duration = 1000, loop = 0)

