import cv2
import numpy as np
from PIL import Image
from transformers import pipeline
import mrmeshpy as mr

# ==========================
# Load Depth Model
# ==========================
print("Loading depth model...")

depth_estimator = pipeline(
    "depth-estimation",
    model="depth-anything/Depth-Anything-V2-Base-hf"
)

# ==========================
# Load Image
# ==========================
image_path = "your_image.jpg"

image = Image.open(image_path).convert("RGB")
width, height = image.size

# ==========================
# Estimate Depth
# ==========================
print("Estimating depth...")

depth = depth_estimator(image)["depth"]
depth = np.array(depth)

# Resize if needed
depth = cv2.resize(depth, (width, height))

# Normalize
depth = depth.astype(np.float32)
depth = (depth - depth.min()) / (depth.max() - depth.min())

# ==========================
# Create Vertices
# ==========================
print("Creating mesh...")

vertices = []
triangles = []

for y in range(height):
    for x in range(width):
        z = float(depth[y, x]) * 50.0
        vertices.append(mr.Vector3f(float(x), float(y), z))

# ==========================
# Create Faces
# ==========================
for y in range(height - 1):
    for x in range(width - 1):

        v0 = y * width + x
        v1 = v0 + 1
        v2 = v0 + width
        v3 = v2 + 1

        triangles.append(mr.Triangle3i(v0, v2, v1))
        triangles.append(mr.Triangle3i(v1, v2, v3))

# ==========================
# Build Mesh
# ==========================
mesh = mr.Mesh()

mesh.points.vec.resize(len(vertices))
for i, v in enumerate(vertices):
    mesh.points.vec[i] = v

mesh.topology.build(len(vertices), triangles)

# ==========================
# Save OBJ
# ==========================
mr.saveMesh(mesh, "depth_mesh.obj")

print("Saved depth_mesh.obj")