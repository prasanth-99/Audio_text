# Audio_text
___
For this Audio to text converting tool. I used Whisper launced by Open_AI
Following are the requirements of tools and the installation steps for to configure whisper

**Tool Requirements:**
___

**Python-version-3.10**

[**Pytorch**]([URL](https://pytorch.org/get-started/locally/))

![image](https://user-images.githubusercontent.com/46361620/215275070-0619b767-7ff9-4e54-8af9-f8faff539f81.png)

[**CUDA-11.6**]([**URL](https://pytorch.org/get-started/locally/))

![image](https://user-images.githubusercontent.com/46361620/215275136-fbd66a14-be4c-498a-8425-3aa3092d9dea.png)

```
!pip install ffmpeg
```

**Whisper Installation**
```
!pip install -U openai-whisper
```

**Upgrade the package:**
___

```
!pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

pip install setuptools-rust
```
This marks completion of setup. 

After this set the root directory with the destination where the Audio files are stored. 
Change the format of the Audio files if necessary.
