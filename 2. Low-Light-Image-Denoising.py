#Natural Image Denoising
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.util import random_noise
from skimage.restoration import denoise_wavelet, denoise_nl_means, estimate_sigma
from scipy.ndimage import median_filter, gaussian_filter

def add_noise(image, noise_level=0.1):
    return random_noise(image, mode='gaussian', var=noise_level**2)

def display_images(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(20, 5))
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img)
        ax.set_title(title)
        ax.axis('off')
    plt.show()

original_image = img_as_float(data.astronaut())
noisy_image = add_noise(original_image)

# Wavelet Denoising
denoised_wavelet = denoise_wavelet(noisy_image, channel_axis=-1)

# Non-Local Means Denoising
sigma_est = np.mean(estimate_sigma(noisy_image, channel_axis=-1))
denoised_nl_means = denoise_nl_means(noisy_image, h=1.15 * sigma_est, fast_mode=True, patch_size=5, patch_distance=3, channel_axis=-1)

# Median Filter Denoising
denoised_median = median_filter(noisy_image, size=3)

# Gaussian Filter Denoising
denoised_gaussian = gaussian_filter(noisy_image, sigma=1)

images = [original_image, noisy_image, denoised_wavelet, denoised_nl_means, denoised_median, denoised_gaussian]
titles = ['Original Image', 'Noisy Image', 'Wavelet Denoising', 'Non-Local Means Denoising', 'Median Filter Denoising', 'Gaussian Filter Denoising']

display_images(images, titles)

#2. Low-Light Image Denoising

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.util import random_noise
from skimage.restoration import denoise_wavelet, denoise_nl_means, estimate_sigma
from scipy.ndimage import median_filter, gaussian_filter

def add_noise(image, noise_level=0.1):
    return random_noise(image, mode='gaussian', var=noise_level**2)

def display_images(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(20, 5))
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img, cmap='gray')
        ax.set_title(title)
        ax.axis('off')
    plt.show()

original_image = img_as_float(data.camera())
noisy_image = add_noise(original_image)

# Wavelet Denoising
denoised_wavelet = denoise_wavelet(noisy_image, channel_axis=None)

# Non-Local Means Denoising
sigma_est = np.mean(estimate_sigma(noisy_image, channel_axis=None))
denoised_nl_means = denoise_nl_means(noisy_image, h=1.15 * sigma_est, fast_mode=True, patch_size=5, patch_distance=3, channel_axis=None)

# Median Filter Denoising
denoised_median = median_filter(noisy_image, size=3)

# Gaussian Filter Denoising
denoised_gaussian = gaussian_filter(noisy_image, sigma=1)

images = [original_image, noisy_image, denoised_wavelet, denoised_nl_means, denoised_median, denoised_gaussian]
titles = ['Original Image', 'Noisy Image', 'Wavelet Denoising', 'Non-Local Means Denoising', 'Median Filter Denoising', 'Gaussian Filter Denoising']

display_images(images, titles)
#3. Medical Image Denoising (MRI)

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.util import random_noise
from skimage.restoration import denoise_wavelet, denoise_nl_means, estimate_sigma
from scipy.ndimage import median_filter, gaussian_filter

def add_noise(image, noise_level=0.1):
    return random_noise(image, mode='gaussian', var=noise_level**2)

def display_images(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(20, 5))
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img, cmap='gray')
        ax.set_title(title)
        ax.axis('off')
    plt.show()

original_image = img_as_float(data.brain())
noisy_image = add_noise(original_image)

# Wavelet Denoising
denoised_wavelet = denoise_wavelet(noisy_image, channel_axis=None)

# Non-Local Means Denoising
sigma_est = np.mean(estimate_sigma(noisy_image, channel_axis=None))
denoised_nl_means = denoise_nl_means(noisy_image, h=1.15 * sigma_est, fast_mode=True, patch_size=5, patch_distance=3, channel_axis=None)

# Median Filter Denoising
denoised_median = median_filter(noisy_image, size=3)

# Gaussian Filter Denoising
denoised_gaussian = gaussian_filter(noisy_image, sigma=1)

images = [original_image, noisy_image, denoised_wavelet, denoised_nl_means, denoised_median, denoised_gaussian]
titles = ['Original Image', 'Noisy Image', 'Wavelet Denoising', 'Non-Local Means Denoising', 'Median Filter Denoising', 'Gaussian Filter Denoising']

display_images(images, titles)
#4. Underwater Image Denoising

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.util import random_noise
from skimage.restoration import denoise_wavelet, denoise_nl_means, estimate_sigma
from scipy.ndimage import median_filter, gaussian_filter

def add_noise(image, noise_level=0.1):
    return random_noise(image, mode='gaussian', var=noise_level**2)

def display_images(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(20, 5))
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img)
        ax.set_title(title)
        ax.axis('off')
    plt.show()

original_image = img_as_float(data.immunohistochemistry())
noisy_image = add_noise(original_image)

# Wavelet Denoising
denoised_wavelet = denoise_wavelet(noisy_image, channel_axis=-1)

# Non-Local Means Denoising
sigma_est = np.mean(estimate_sigma(noisy_image, channel_axis=-1))
denoised_nl_means = denoise_nl_means(noisy_image, h=1.15 * sigma_est, fast_mode=True, patch_size=5, patch_distance=3, channel_axis=-1)

# Median Filter Denoising
denoised_median = median_filter(noisy_image, size=3)

# Gaussian Filter Denoising
denoised_gaussian = gaussian_filter(noisy_image, sigma=1)

images = [original_image, noisy_image, denoised_wavelet, denoised_nl_means, denoised_median, denoised_gaussian]
titles = ['Original Image', 'Noisy Image', 'Wavelet Denoising', 'Non-Local Means Denoising', 'Median Filter Denoising', 'Gaussian Filter Denoising']

display_images(images, titles)
#5. Surveillance - CCTV Footage Denoising

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.util import random_noise
from skimage.restoration import denoise_wavelet, denoise_nl_means, estimate_sigma
from scipy.ndimage import median_filter, gaussian_filter

def add_noise(image, noise_level=0.1):
    return random_noise(image, mode='gaussian', var=noise_level**2)

def display_images(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(20, 5))
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img)
        ax.set_title(title)
        ax.axis('off')
    plt.show()

original_image = img_as_float(data.coffee())
noisy_image = add_noise(original_image)

# Wavelet Denoising
denoised_wavelet = denoise_wavelet(noisy_image, channel_axis=-1)

# Non-Local Means Denoising
sigma_est = np.mean(estimate_sigma(noisy_image, channel_axis=-1))
denoised_nl_means = denoise_nl_means(noisy_image, h=1.15 * sigma_est, fast_mode=True, patch_size=5, patch_distance=3, channel_axis=-1)

# Median Filter Denoising
denoised_median = median_filter(noisy)
