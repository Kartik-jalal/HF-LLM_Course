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
Lastly, if you would like to check if the GPU is being utalised after the above installation is done with the default libs, simply run `python3 gpu_check.py`.
Lastly, to deactive the venv simply run:
```
deactivate
```

Now everytime you open any of the jupyter notebooks, e.g., *Chapter_1.ipynb*, simply select the *Kernel* '__.venv (Python {version})__' using the '*Select Kernel*' option.


## [Chapter 1](chapter_1.ipynb) | [Hugging Face - Chapter 1](https://huggingface.co/learn/llm-course/chapter1/1?fw=pt)
In Chapter 1, we go over the *transformer’s* **pipeline** method, **tokenization**, and the issue of **bias** when *fine-tuning* a pre-trained model.

## [Chapter 2](chapter_2.ipynb) | [Hugging Face - Chapter 2](https://huggingface.co/learn/llm-course/chapter2/1?fw=pt)
In Chapter 2, we go over how the **pipeline** method really works and also discuss the *optimized* way to *deploy* an LLM model.

## [Chapter 3](chapter_3.ipynb) | [Hugging Face - Chapter 3](https://huggingface.co/learn/llm-course/chapter3/1?fw=pt)
In Chapter 3, we go over the modern *data pre-processing techniques*, *fine-tuning* and *evaluating* a model using the `Trainer` API, implementing a *complete custom training loop* from sctach with *PyTorch*, use of `Accelerate` lib to make our training code work seamlessly on multiple *GPUs* or *TPUs* and finally about *learning curves*.

## [Chapter 4](chapter_4.ipynb) | [Hugging Face - Chapter 4](https://huggingface.co/learn/llm-course/chapter4/1?fw=pt)
In Chapter 4, we learned how to simply upload a model to the **Hugging Face Hub**.

## [Chapter 5](chapter_5.ipynb) | [Hugging Face - Chapter 5](https://huggingface.co/learn/llm-course/chapter5/1?fw=pt)
In Chapter 5, we learned how to load and stream datasets from anywhere. Perform preprocessing using `Dataset.map()` and `Dataset.filter()` functions and quickly switch their formats using `Dataset.set_format()`. Lastly, embed data using a Transformer model and build a *semantic search engine* using *FAISS*.


## [Chapter 6](chapter_6.ipynb) | [Hugging Face - Chapter 5](https://huggingface.co/learn/llm-course/chapter6/1?fw=pt)
Upcoming!


# Latest Update
### 7th of Aug, 2025
- New python libs added to the [requirements.txt](requirements.txt) file. After activating the *venv* (`source .venv/bin/activate`), please do:
  ```
    pip install --upgrade -r requirements.txt
  ```
  > This time I have also added the `pip-tool` lib. So, from next time we can run the `pip-sync requirements.txt` command instead to update the python venv whenever there is a new lib added or removed or needs to be upgraded.

- Finished the Simantic search section and also corrected a mistake regarding embeddings.
- Chapter 5 is Done!!!


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




