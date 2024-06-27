# Different-Denoising-Techniques

# Image Denoising using Various Techniques

This repository contains code examples for denoising images using various techniques including Wavelet Denoising, Non-Local Means Denoising, Median Filter Denoising, and Gaussian Filter Denoising. The code demonstrates these techniques on different types of images such as natural images, low-light images, medical MRI images, underwater images, CCTV footage, and satellite images.

## Table of Contents

- [Introduction](#introduction)
- [Denoising Techniques](#denoising-techniques)
  - [Wavelet Denoising](#wavelet-denoising)
  - [Non-Local Means Denoising](#non-local-means-denoising)
  - [Median Filter Denoising](#median-filter-denoising)
  - [Gaussian Filter Denoising](#gaussian-filter-denoising)
- [Examples](#examples)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Image denoising is the process of removing noise from an image. Noise can occur during image capture, transmission, or processing. This repository provides implementations of different denoising algorithms to improve the quality of images affected by noise.

## Denoising Techniques

### Wavelet Denoising

Wavelet denoising is a method that uses wavelet transforms to separate noise from the image signal. It is effective in removing Gaussian noise and preserving image details.

### Non-Local Means Denoising

Non-Local Means (NLM) denoising is a technique that reduces noise by averaging pixel values with similar patches in the image. It is effective in maintaining textures and fine details.

### Median Filter Denoising

Median filtering is a simple and effective way to remove salt-and-pepper noise. It works by replacing each pixel value with the median value of its neighboring pixels.

### Gaussian Filter Denoising

Gaussian filtering smooths the image by averaging pixel values with a Gaussian kernel. It is useful for reducing Gaussian noise but can blur image details.

## Examples

The repository includes code examples for denoising various types of images:

1. **Natural Image Denoising**
2. **Low-Light Image Denoising**
3. **Medical Image Denoising (MRI)**
4. **Underwater Image Denoising**
5. **Surveillance - CCTV Footage Denoising**
6. **Satellite Image Denoising**

Each example is provided as a separate Python script.

## Installation

To run the code examples, you need to have Python installed. You can install the required Python libraries using `pip`.

pip install numpy matplotlib scikit-image scipy
Usage
Each example is provided as a separate Python script. You can run these scripts to see the denoising results for different types of images.

cd image-denoising
Run the desired example script. For instance, to run the natural image denoising example:

python natural_image_denoising.py
Example Scripts
Natural Image Denoising: natural_image_denoising.py
Low-Light Image Denoising: low_light_image_denoising.py
Medical Image Denoising (MRI): medical_image_denoising.py
Underwater Image Denoising: underwater_image_denoising.py
Surveillance - CCTV Footage Denoising: cctv_image_denoising.py
Satellite Image Denoising: satellite_image_denoising.py
Contributing
Contributions are welcome! If you have any improvements or additional denoising techniques to add, please open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

### Example Directory Structure

image-denoising/
│
├── README.md
├── natural_image_denoising.py
├── low_light_image_denoising.py
├── medical_image_denoising.py
├── underwater_image_denoising.py
├── cctv_image_denoising.py
└── satellite_image_denoising.py

### How to Use the README

1. Save the provided text as `README.md` in the root directory of your GitHub repository.

This README provides a clear overview of your project, instructions for installation and usage, and a brief explanation of each denoising technique without including the actual code. You can ensure each script file (e.g., `natural_image_denoising.py`) contains the corresponding code example provided earlier.





