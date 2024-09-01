from PIL import Image
import numpy as np
import os

class Captcha(object):
    def __init__(self, threshold=128):
        self.threshold = threshold
        self.matrix_dict = {}

    def process_image(self, image_path):
        """Load an image, convert to grayscale, and apply a binary threshold."""
        image = Image.open(image_path).convert("L")
        pixel_values = np.array(image)
        return (pixel_values > self.threshold).astype(int)

    def extract_columns(self, binary_values):
        """Extract columns with binary representation of characters."""
        matrix_list = []
        matrix = []
        for j in range(binary_values.shape[1]):
            if 0 in binary_values[:, j]:
                matrix.append(binary_values[:, j])
            else:
                if matrix:
                    matrix_list.append(np.vstack(matrix))
                    matrix = []
        return matrix_list

    def build_char_matrix_dict(self, image_paths, labels_paths):
        """Build a dictionary mapping characters to their matrix representations."""
        for img_path, lbl_path in zip(image_paths, labels_paths):
            binary_values = self.process_image(img_path)
            matrix_list = self.extract_columns(binary_values)
            with open(lbl_path, 'r') as file:
                string = file.read().strip()
            for char, mat in zip(string, matrix_list):
                self.matrix_dict[char] = mat

    def infer(self, image_path):
        """Infer the text from a captcha image using the pre-built matrix dictionary."""
        binary_values = self.process_image(image_path)
        matrix_list = self.extract_columns(binary_values)
        output = ""
        for mat in matrix_list:
            for key in self.matrix_dict:
                if np.array_equal(self.matrix_dict[key], mat):
                    output += key
        return output

    def __call__(self, im_path, save_path):
        """Process an image and save the result to a file."""
        result = self.infer(im_path)
        with open(save_path, 'w') as file:
            file.write(result)
        return result
    

# Example usage:
captcha = Captcha()
# Build the character matrix dictionary
captcha.build_char_matrix_dict(
    [f"sampleCaptchas/input/input{i:02d}.jpg" for i in range(25)],
    [f"sampleCaptchas/output/output{i:02d}.txt" for i in range(25)]
)
# Process an example captcha image
output = captcha("sampleCaptchas/input/input100.jpg", "sampleCaptchas/output/output100.txt")
print("Inferred captcha:", output)