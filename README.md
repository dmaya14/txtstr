<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://pingui.tk">
    <img src="https://imgur.com/bHPrNF3.png" alt="Logo" width="320">

  </a>

  <h1 align="center">TxtStr</h1>

  <p align="center">
    Edit text file, encrypt and decrypt with python!
    <br />
    <br />
    <a href="https://github.com/pinguimaya/txtstr"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/pinguimaya/txtstr/issues">Report Bug</a>
    ·
    <a href="https://github.com/pinguimaya/txtstr/issues">Request Feature</a>
  
    
  
  </p>
</p>

[![Downloads](https://pepy.tech/badge/txtstr)](https://pepy.tech/project/txtstr)

<!-- ABOUT THE PROJECT -->
## About The Project

[![miniatura][miniatura]](https://github.com/pinguimaya/txtstr)

If you want the explanation ask me in **Twitch** [link](https://twitch.tv/pinguimaya)

<br/>

<!-- release notes -->
## Release notes
Hi!, the new update of **txtstr** brings new commands that were necessary for this library to be useful, some commands have been modified to make it even easier to obtain the information they give you, below you will see the list of new and updated commands, Thanks so much for welcoming **txtstr**, good luck coding!

## Bug fix
We have fixed a bug that causes the word encrypt to be displayed in the console while decrypting, all fixed!
<br/>
<br/>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You need to make sure you have installed the following modules. **The requirements are installed automatically, but for any errors here are the commands to install each dependency**
* Cryptography
  ```s
  pip install cryptography
  ```
  
* Docx
  ```s
  pip install docx
  ```
* Fpdf
  ```s
  pip install fpdf
  ```

### Installation

```python
pip install txtstr
```
<br/>

<!-- USAGE EXAMPLES -->
## Usage

* **txtstr.\_\_init__()**
    ```python
    import txtstr

    txtstr.__init__()
    
    ```
  This starts all the functions to encrypt and decrypt the txt files, it creates a folder for you and the decryption key also starts the modules
<br/>
<br/>
<br/>
<br/>

* **txtstr.newkey(name)**

    ```python
    import txtstr

    txtstr.newkey(name)
    
    ```
  Create a new UNIQUE key to be able to encrypt and decrypt the files if you want someone to decrypt your files you have to pass them this key
<br/>
<br/>
<br/>
<br/>

* **txtstr.loadkey(name)**
    ```python
    import txtstr

    key = txtstr.loadkey(name)
    print(key)
    
    ```
  Here you can see your UNIQUE key to share it and use it in your programs when you think it is necessary
<br/>
<br/>
<br/>
<br/>

* **txtstr.encrypt(file, CUSTOM_KEY, times)**
  ```python
    import txtstr
    
    file = "file.txt"
    
    txtstr.encrypt(file,None,5)
    
    ```
  That this function can encrypt your file, the FILE section is where you can find the path of your .TXT file, CUSTOM_KEY if you put None it is because you want to use the default txtstr key, it is always advisable to create yours beforehand, to locate yours just type the name of the key (if it is in the same folder), but if it is in another folder, use the path of said file. Remember not to lose these keys since without this it will be IMPOSSIBLE to decrypt it. TIMES indicates the number of times you want this file to be encrypted remember the number as it will be the same number of times to decrypt them.
<br/>
<br/>
<br/>
<br/>

* **txtstr.decrypt(file, CUSTOM_KEY, times)**
  ```python
    import txtstr

    file = "file.txt"
    
    txtstr.decrypt(file, None, 5)
    
    ```
  Here you can decrypt your file, the FILE section is for the path of your file and the CUSTOM_KEY if you put None it is because you want to use the default txtstr key, it is always advisable to create yours beforehand, to locate yours just type the name of the key (if it is in the same folder), but if it is in another folder, use the path of said file. TIMES here you must put the number of times you want to decrypt it this must be the same as the time you encrypted it.
<br/>
<br/>
<br/>
<br/>

* **txtstr.write(name,text,add)**
  ```python
    import txtstr

    text = "the develpoer of txtstr is the best UnU"
    name = "isTRUE"
    
    txtstr.write(name, text, True)
  
  ```
  If ADD is True the text will be added to the file but if it is False it will be rewritten


<br/>
<br/>
<br/>
<br/>

* **txtstr.newtxt(name)**

  ```python
    import txtstr

    name = "file.txt"
    
    txtstr.newtxt(name)
  
  ```
  This will create a new text file, you can change the name to an address where this file will be saved


<br/>
<br/>
<br/>
<br/>

* **txtstr.search(name,searchfor,advanced)**

  ```python
    import txtstr

    name = "file.txt"
    searchfor = "hi"
    
    info = txtstr.search(name, searchfor, True)
  
  ```
  If ADVANCED is **True**, you must define a **single variable** as in this case "info" will return a dictionary where "isin" is if it was found, "quantity" is the number of times it appears, "linesamount" the number of lines your file has, "lineappear" is a list where you will find the line number where it is located
<br/>
<br/>

  ```python
    import txtstr

    name = "file.txt"
    searchfor = "hi"
    
    IsIn, quantity, linesamount, lineappear = txtstr.search(name, searchfor, False)
  
  ```
  If ADVANCED is **False**, you must define **three variables to give the following values** ​​"isin" is if it was found, "quantity" is the number of times it appears, "linesamount" the number of lines your file has, "lineappear" is a list where you will find the line number where it is located



<br/>
<br/>
<br/>
<br/>


* **txtstr.read(file)**

  ```python
    import txtstr

    file = "file.txt"
    
    text = txtstr.read(file)
    print(text)
  ```
<br/>
<br/>
<br/>
<br/>

* **txtstr.readlines(file)**

  ```python
    import txtstr

    file = "file.txt"
    
    text = txtstr.readlines(file)
    print(lines)
  ```
  This is similar to **txtstr.read()** but here each line of your file will be saved to a list remember that it starts counting from zero if you want to print a specific line you can do ```print(lines[ 10])```

<br/>
<br/>
<br/>
<br/>

* **txtstr.addline(name,line)**

  ```python
    import txtstr

    line = "Hi ty for supporting txtstr!"
    
    txtstr.addline(name,line)
  ```
<br/>
<br/>
<br/>
<br/>

* **txtstr.rename(file,new_name)**

  ```python
    import txtstr

    file = "file.txt"
    new_name = "txtstr"
    
    txtstr.rename(file,new_name)
  ```
<br/>

<!-- USAGE EXAMPLES -->
## Experimental functions
<br/>


* **txtstr.toword(file)**

  ```python
    import txtstr

    file = "file.txt"
    
    txtstr.toword(file)
  ```
<br/>
<br/>
<br/>
<br/>

* **txtstr.topdf(file)**

  ```python
    import txtstr

    file = "file.txt"
    
    txtstr.topdf(file)
  ```
<br/>
<br/>
<br/>
<br/>

* **txtstr.checkupdate()**

  ```python
    import txtstr

    txtstr.checkupdate()
  ```
  With this you can automatically install any new version of **txtstr**
  
<br/>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Discord: [PingüiMaya14#2055](https://discord.com/invite/KfkA4MPME3)

WebSite: [pingui.tk](https://pingui.tk/)









[miniatura]: https://imgur.com/iehVgKR.png
