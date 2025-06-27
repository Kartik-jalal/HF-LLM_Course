# HF-LLM_Course
This Repo is for the work-through of [LLMs](https://huggingface.co/learn/llm-course/chapter0/1?fw=pt) by HuggingFace.

## Setup

JupyterNotebook and Python venv is used as the setup enviornment here. To create a venv, run the following command inside the repo dir:
```
python3 -m vevn .venv
```
Then, activate the venv simply by:
```
source .venv/bin/activate
```
Now, install the required python libs by:
```
pip install -r requirements.txt
```
> _Note: The requirements.txt install the **pytorch** cuda compatible lib to utalise the gpu. If you don't have a gpu simply comment out the **line 2** in the requirements.txt file and uncomment **line 3**.<br />
Furthermore, if you would like to use **tensorflow** instead of **pytorch**, just uncomment the **line 14** and either **line 10** or **line 11** (depending on if you have a gpu or not), and after, comment out the lines from **2-6**.  <br />
Lastly, if you would like to check if the GPU is being utalised after the above installation is done with the default libs, simply run `python3 gpu_check.py`._

Lastly, to deactive the venv simply run:
```
deactivate
```

Now everytime you open any of the jupyter notebooks, e.g., *Chapter_1.ipynb*, simply select the *Kernel* '__.venv (Python {version})__' using the '*Select Kernel*' option.



