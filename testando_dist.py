from image_processing.utils import io, plot
from image_processing.processing import combination, transformation

image1 = io.read_image(r'C:\Users\stock\OneDrive\Python\04_boot_camp\01_suzano_python_developer\image-processing-package\img\imagem_1.jpg')
image2 = io.read_image(r'C:\Users\stock\OneDrive\Python\04_boot_camp\01_suzano_python_developer\image-processing-package\img\imagem_2.jpg')

plot.plot_image(image1)
plot.plot_image(image2)

result_image = combination.transfer_histogram(image1, image2)
plot.plot_image(result_image)