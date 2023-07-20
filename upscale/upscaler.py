import argparse
import cv2
from cv2 import dnn_superres
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, default='data/monalisa.jpg', help='input image path')
parser.add_argument('-n', '--model_name', type=str, default='EDSR_x2', help='Model names: EDSR_x2 | EDSR_x3 | EDSR_x4')
parser.add_argument('-o', '--output', type=str, default='output', help='output')
args = parser.parse_args()

print("Input Image:", args.input)
print("Model Name:", args.model_name)
print("Output Folder:", args.output)

path = f"weights/{args.model_name}.pb"
sr = dnn_superres.DnnSuperResImpl_create()
sr.readModel(path)
sr.setModel("edsr", 2)

image = cv2.imread(args.input)

result = sr.upsample(image)

output_folder = args.output
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(output_folder, f"{args.model_name}.jpg")
cv2.imwrite(output_path, result)
cv2.imshow(args.model_name, result)

cv2.waitKey(0)
cv2.destroyAllWindows()