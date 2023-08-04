# Prompt
Edge detection is a crucial stage in numerous image processing applications. One of the most challenging goals in computer vision is to develop algorithms that can process visual information reliably. To ensure that an edge detection technique is reliable, it needs to be rigorously assessed before being used in a computer vision application.

Using OpenCV, generate a synthetic image that contains exactly one filled-in square and one filled-in circle. The placement and color intensities of these shapes are up to you. The background intensity is up to you as well. You should know precisely the locations of the discontinuities. The rest of the image should be without edges.

Implement Canny, Sobel, and then Laplacian edge detection on this image. Define a measure to evaluate the performance of each method. Repeat this experiment by adding noise to the image using a random number generator and changing the intensity values of the objects and the background. Change the threshold values for your detection step and then evaluate the performance once again. 

In your post, write at least a paragraph discussing the following:

Describe the evaluation method you developed and the factors you considered in its definition.
Compare your evaluation method to at least two other edge detection evaluation methods you have researched.  Provide the references for your researched methods and cite them in your summary using correct APA styling. 
Which edge detection method worked best under each of the conditions (original image vs adding noise and varying intensity values)? Substantiate your claim with evaluation method metrics.
Attach your synthetic image to your post.

# Response

Because time is an important consideration when processing big data collections that may contain millions--or even billions--of images, I chose time as my performance metric (OpenCV: Performance Measurement and Improvement Techniques, 2023). My results were as follows:

## Canny Edge Detection: Minimum threshold for hysteresis 100; maximum values 200 and 300

![image](https://github.com/cactusflatscoder/MDanish_Portfolio_PY/assets/101354414/9ca625df-1c11-470b-a0ce-1942d6b62f33)

## Sobel and Laplacian Edge Detection: Kernel Sizes 3 and 5

![image](https://github.com/cactusflatscoder/MDanish_Portfolio_PY/assets/101354414/6e29f15f-dbd9-476b-a5fe-27393166c9db)

Other metrics we could use to evaluate image segmentation preprocessing performance are Peak Noise to Signal Ratio and Mean Squared Error. PNSR and MSE would both provide us with data about the quality of noise reduction. PSNR would give us the ratio of the maximum power of the signal to the maximum power of the noise in the image, while MSE would give us an error measurement that is assumed to correlate directly with the visual quality of the image (Signal, 2023).   

## Output

![image](https://github.com/cactusflatscoder/MDanish_Portfolio_PY/assets/101354414/91b9a42e-56ac-4fa1-9c7c-4dbabaf1ae53)

 

In terms of speed, Sobel edge detection was the clear winner for both the original and noisy image, and it outperformed other methods on the noisy image even with the change to a larger kernel size. Canny edge detection was the second best for both images, with Laplacian being the slowest edge detection method.

 

## References

*OpenCV: Performance Measurement and Improvement Techniques.* (2023). Opencv.org. https://docs.opencv.org/3.4/dc/d71/tutorial_py_optimization.html

Signal, D. (2023). *Digital Signal Processing Techniques - Image Processing Performance Metrics.* Google.com. https://sites.google.com/site/digitalsignaltechniques/image-filtering-performance-metrics
