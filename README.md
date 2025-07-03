# HF-LLM_Course
This Repo is for working through the [LLMs course](https://huggingface.co/learn/llm-course/chapter0/1?fw=pt) by HuggingFace, to help me refamiliarise myself with NLP.

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
Lastly, if you would like to check if the GPU is being utalised after the above installation is done with the default libs, simply run `python3 gpu_check.py`. <br /><br />
Furthermore, to update the venv with the new lib added in the requirements.txt file please do `pip install --upgrade -r requirements.txt`_

Lastly, to deactive the venv simply run:
```
deactivate
```

Now everytime you open any of the jupyter notebooks, e.g., *Chapter_1.ipynb*, simply select the *Kernel* '__.venv (Python {version})__' using the '*Select Kernel*' option.


## [Chapter 1](chapter_1.ipynb) | [Hugging Face - Chapter 1](https://huggingface.co/learn/llm-course/chapter1/1?fw=pt)
In Chapter 1, we go over the *transformer’s* **pipeline** method, **tokenization**, and the issue of **bias** when *fine-tuning* a pre-trained model.

## [Chapter 2](chapter_2.ipynb) | [Hugging Face - Chapter 2](https://huggingface.co/learn/llm-course/chapter2/1?fw=pt)
In Chapter 2, we go over how the **pipeline** method really works and also discuss the *optimized* way to *deploy* an LLM model.

## [Chapter 3]() | [Hugging Face - Chapter 3](https://huggingface.co/learn/llm-course/chapter3/1?fw=pt)
Upcoming!

# Reference
```
@misc{huggingfacecourse,
  author = {Hugging Face},
  title = {The Hugging Face Course, 2022},
  howpublished = "\url{https://huggingface.co/course}",
  year = {2022},
  note = "[Online; accessed <today>]"
}
```




