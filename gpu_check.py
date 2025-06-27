# Try importing TensorFlow
try:
    import tensorflow as tf
    tf_available = True
except ImportError:
    print("TensorFlow is not installed.")
    tf_available = False

# Try importing PyTorch
try:
    import torch
    torch_available = True
except ImportError:
    print("PyTorch is not installed.")
    torch_available = False

# Check CUDA availability for PyTorch
if torch_available:
    print("PyTorch CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("PyTorch GPU in use:", torch.cuda.get_device_name(0))
    else:
        print("PyTorch running on CPU")

# Check GPU devices for TensorFlow
if tf_available:
    gpus = tf.config.list_physical_devices('GPU')
    print("TensorFlow GPUs found:", gpus)
    if gpus:
        print("TensorFlow is using GPU:", gpus[0].name)
    else:
        print("TensorFlow running on CPU")
