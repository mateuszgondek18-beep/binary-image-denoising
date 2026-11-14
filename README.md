# binary-image-denoising
Custom implementation of median filter and morphological operations in Python without OpenCV.

## Implemented Functions

- **`frame(matrix, value)`** – Adds a 1-pixel border (padding) around the binary matrix to prevent `IndexError` when analyzing edge pixels.
- **`denoising(matrix)`** – Custom 3x3 median filter that removes salt-and-pepper noise by majority voting of neighboring pixels.
- **`erosion(matrix)`** – Morphological erosion that shrinks object boundaries and removes remaining isolated white pixels from the background.
- **`dilation(matrix)`** – Expands foreground (white) regions using a structuring element to fill small internal holes and smooth jagged object boundaries.


## Requirements

- Python 3.x
- `numpy`
- `Pillow`

## How to Run

1. Install required libraries:
   ```bash
   pip install numpy Pillow
2. Place your input image (currently supports `.bmp` format) in the project directory and update the filename in the script if needed.
3. Run the script: `python binary_image_denoising.py`


## Results
| Before | After |
| :---: | :---: |
| <img width="170" height="170" alt="Before" src="https://github.com/user-attachments/assets/00eb7b01-1e19-41f3-a4a7-17de3c73cb11" /> | <img width="170" height="170" alt="BateriesAfter" src="https://github.com/user-attachments/assets/5ad9e9a1-3ec5-45c0-9505-4f88a16c069d" /> |
