import tensorflow as tf
import torch

# Check if CUDA is available for pytorch
print("PyTorch CUDA available:", torch.cuda.is_available())
# List all physical devices for tensorflow
gpus = tf.config.list_physical_devices('GPU')
print("TensorFlow GPUs found:", gpus)

# If yes, get device name
if torch.cuda.is_available():
    print("PyTorch GPU in use:", torch.cuda.get_device_name(0))
else:
    print("PyTorch running on CPU")


# Optional: Get more info
if gpus:
    print("TensorFlow is using GPU:", gpus[0].name)
else:
    print("TensorFlow running on CPU")
