# Features for Organoid Project

## G4G Demo

I was looking at the g4g demo on cancer cell classification 
[Link](https://www.geeksforgeeks.org/machine-learning/ml-cancer-cell-classification-using-scikit-learn/)
they only use computationally quantified data, they don't use the images

compare using image with features vs just features

feature categories from cancer dataset (mean, error, worst & max)
- Radius
- Texture
- Perimeter
- Area
- Smoothness
- Compactness
- Concavity
- Concave Points
- Symmetry
- Fractal Dimension

## Feature Ideas

Per Pixel
- Border

Per Organoid
- Radius
- x/y passthrough
- x/y congruency test
- Border congruency
    - Check all border pixels, check if they're all connected

## To Impliment

- Axis Scan
    for Border Analysis
    to get list of all pixels with certain value
- Color Select
    bfs on a selected pixel, get the list of all connected pixels
    within the color threshold
    with sensitivity variable 
- check slide background
    check top 5x5 area for background color
    color might differ per slide
    staining may differ
    maybe check per color peak

