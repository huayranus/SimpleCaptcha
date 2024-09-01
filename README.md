
# Captcha Processing Class

This Python module defines a `Captcha` class that is designed to process CAPTCHA images, extract characters from them, and interpret these characters by comparing to previously processed CAPTCHA patterns.

## Features

- **Image Processing**: Converts CAPTCHA images to a binary format based on a threshold value.
- **Character Extraction**: Identifies distinct character patterns in CAPTCHA images.
- **Dictionary Building**: Builds a dictionary that maps character patterns to their respective alphanumeric characters.
- **CAPTCHA Inference**: Uses pre-built character pattern dictionaries to decode new CAPTCHA images.

## Setup

To use this module, ensure that you have Python installed along with the following packages:
- `PIL` (Pillow)
- `numpy`

## Usage

### Initializing the Captcha Class

First, create an instance of the `Captcha` class. Optionally, you can specify a binary threshold:

```py
from captcha_processor import Captcha

captcha = Captcha(threshold=128)
```

### Building the Character Matrix Dictionary

Before inferring CAPTCHA texts from images, you need to build a dictionary that maps characters to their binary representations:

```py
captcha.build_char_matrix_dict(
    [f"sampleCaptchas/input/input{i:02d}.jpg" for i in range(25)],
    [f"sampleCaptchas/output/output{i:02d}.txt" for i in range(25)]
)
```

### Processing an Image

To process an image and infer the CAPTCHA text, use the class as a callable:

```py
output = captcha("sampleCaptchas/input/input100.jpg", "sampleCaptchas/output/output100.txt")
print("Inferred captcha:", output)
```

### Saving Output

The output inferred from the CAPTCHA image is automatically saved to the specified file path.

## Note

Ensure that the paths to the input images and output text files are correctly set according to your directory structure.

## Contributing

Contributions to this module are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
