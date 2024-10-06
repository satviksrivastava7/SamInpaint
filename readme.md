# SAM Inpaint - A segmented approach towards AI based image editing 

## About this repository

This repository documents and maintains the solution for the Scene-Composition Assignment (H3) provided by Avataar. Completing this task has been an invaluable learning experience, allowing me to explore advanced generative AI techniques for object segmentation and image manipulation. By working through real-world applications such as repositioning objects in product scenes, I gained hands-on experience with cutting-edge models like SAM (Segment Anything Model) and Stable Diffusion Inpainting. This project showcases my ability to creatively solve complex image-editing tasks using AI tools and existing models. 

## About this project

Recent advancements in generative AI have enabled the development of creative workflows for image editing. One such workflow is leveraging generative AI techniques to modify product photographs after they've been captured in a studio setting. For example, e-commerce platforms often require adjustments to product scenes, such as repositioning objects within the scene for better display.

This project involves two primary tasks to achieve a user-friendly functionality for moving objects in a scene. The first task is to segment an object (identified by a user-provided class prompt) in a given image. This segmentation step is critical for creating an intuitive editing experience. The second task is to reposition the segmented object based on user inputs, such as specifying the number of pixels to shift horizontally and vertically. The final output should be a realistic and well-composited image where the object appears in its new location.

## Approach to edit segmented prompts

To complete this assignment, I used a combination of pre-trained generative AI models to segment and reposition objects in images. By leveraging Segment Anything Model (SAM) for object segmentation and Stable Diffusion Inpainting for seamless background reconstruction and object repositioning, I was able to create a user-friendly solution. This approach focused on utilizing existing models to achieve accurate results without the need for extensive model training or fine-tuning, allowing for efficient and effective manipulation of product scenes. Below is a detailed explanation of the steps taken to solve both tasks.

__Task 1: Object Segmentation__
<img src="https://github.com/satviksrivastava7/SamInpaint/assets/sam.png" alt="Original" width="auto" height="auto" style="margin: 0px;">
To segment an object from an image based on a user-provided class prompt, I utilized the Segment Anything Model (SAM). Here’s how the process works:
1. Image and Prompt Input: The user provides an image and a class prompt (e.g., "shelf"). This prompt helps SAM focus on the relevant object in the scene.
2. SAM Model: The SAM model, pre-trained on a variety of datasets, generates a segmentation mask for the object described in the prompt. The model is able to generalize well to different objects and images, so no fine-tuning was required.
3. Output: The model generates a red mask overlay on the image, highlighting all pixels where the object is detected. This mask is saved as an output image.

__Task 2: Object Repositioning__
<img src="https://github.com/satviksrivastava7/SamInpaint/assets/inpaint.png" alt="Original" width="auto" height="auto" style="margin: 0px;">
Once the object is segmented, the second task involves moving it to a different location in the image. For this, I used Stable Diffusion Inpainting to seamlessly handle the removal and repositioning:
1. Object Removal: The segmented object is removed from its original position using Stable Diffusion Inpainting. This model reconstructs the background behind the object, filling in the missing details to make the removal look natural.
2. Object Repositioning: The object is then shifted to a new position in the image, based on user input for the x and y pixel shifts. This allows for flexibility in adjusting the object's placement.
3. Composite Image: The final output is a composite image where the object is moved to its new position without leaving artifacts or distortions behind.

## Demo

Demonstration of some generated outputs. 
<div align="center">
  <h2>Prompt: "No curtains"</h2>
   <img src="https://github.com//satviksrivastava7/SamInpaint/assets/test_img_1.jpg" alt="Original" width="300" style="margin-right: 20px;">
  <img src="https://github.com//satviksrivastava7/SamInpaint/assets/result_img_1.jpg" alt="Original" width="300" style="margin-right: 20px;">
</div>

<div align="center">
  <h2>Prompt: "Blue wall"</h2>
  <img src="https://github.com//satviksrivastava7/SamInpaint/assets/test_img_1.jpeg" alt="Original" width="300" style="margin-right: 20px;">
  <img src="https://github.com//satviksrivastava7/SamInpaint/assets/result_img_2.png" alt="Segment 1" width="300" style="margin-right: 20px;">
</div>

<div align="center">
  <h2>Prompt: "Small flower vase"</h2>
  <img src="https://github.com//satviksrivastava7/SamInpaint/assets/images/test_img_3.jpeg" alt="Original" width="300" style="margin-right: 20px;">
  <img src="https://github.com//satviksrivastava7/SamInpaint/assets/images/result_img_3.png" alt="Segment 1" width="300" style="margin-right: 20px;">
</div>

## Installation and usage

1. Create a virtual environment in your system.
2. Downnload the repository (either by git clone or zip download). You can use the git clone command and follow the given instructions -
    ```
    git clone https://github.com/satviksrivastava7/SamInpaint.git
    cd SamInpaint/
    ```
3. Create a conda virtual environment and activate the venv
   ```
   conda create --name=samInpaint python=3.14
   conda activate samInpaint
   ```
4. Install the required dependencies using the below given commands.
   ```
   python -m pip install torch torchvision torchaudio
   python -m pip install -e segment_anything
   python -m pip install -r lama/requirements.txt 
   ```
4. Install the desired SAM model checkpoint check points. The script uses __"sam_vit_h_4b8939.pth"__ check points.
5. Place the data in the respective folder.
6. Run the command.
    ```
    python yolo_script.py --image ./example.jpg --class "chair" --output ./generated.png
    ```

## References

* [Stable Diffusion Inpainting](https://huggingface.co/runwayml/stable-diffusion-inpainting)
* [Segment anything model (SAM)](https://segment-anything.com)
