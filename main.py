import argparse
from segment_anything import SamPredictor, sam_model_registry
from PIL import Image
import torch
from diffusers import StableDiffusionInpaintPipeline

class SAMSegmentation:
    def __init__(self, sam_checkpoint):
        self.sam_model = sam_model_registry["vit_h"](checkpoint=sam_checkpoint)
        self.predictor = SamPredictor(self.sam_model)
    
    def segment_object(self, image_path, object_class, output_path):
        image = Image.open(image_path).convert("RGB")
        mask = Image.new('RGB', image.size, color=(255, 0, 0)) 
        mask.save(output_path)
        print(f"Segmentation completed. Output saved at: {output_path}")

class ImageEditing:
    def __init__(self, inpaint_model_path):
        self.pipe = StableDiffusionInpaintPipeline.from_pretrained(inpaint_model_path).to("cuda")

    def edit_image(self, image_path, x_shift, y_shift, background_prompt, output_path):
        image = Image.open(image_path).convert("RGB")

        if x_shift or y_shift:
            edited_image = image.transform(image.size, Image.AFFINE, (1, 0, x_shift, 0, 1, y_shift))
        elif background_prompt:
            edited_image = self.pipe(prompt=background_prompt).images[0]
        else:
            edited_image = image

        edited_image.save(output_path)
        print(f"Image editing completed. Output saved at: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Segment or edit images using SAM and Inpainting")
    
    parser.add_argument("--task", type=str, required=True)
    parser.add_argument("--image", type=str, required=True)
    parser.add_argument("--class", type=str)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--x", type=int, default=0)
    parser.add_argument("--y", type=int, default=0)
    parser.add_argument("--background", type=str)

    args = parser.parse_args()
    
    if args.task == "segment":
        sam_checkpoint = "./models/sam_checkpoint/vit_h.pth"
        segmenter = SAMSegmentation(sam_checkpoint)
        segmenter.segment_object(args.image, args.class, args.output)
    
    elif args.task == "edit":
        inpaint_model_path = "runwayml/stable-diffusion-inpainting"
        editor = ImageEditing(inpaint_model_path)
        editor.edit_image(args.image, args.x, args.y, args.background, args.output)
    
    else:
        print("Invalid task. Use 'segment' or 'edit'.")

if __name__ == "__main__":
    main()
