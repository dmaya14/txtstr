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

<!-- ABOUT THE PROJECT -->
## About The Project

[![miniatura][miniatura]](https://github.com/pinguimaya/txtstr)

If you want the explanation ask me in **Twitch** [link](https://twitch.tv/pinguimaya)




<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You need to make sure you have installed the following modules.
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
* **txtstr.encrypt(file, CUSTOM_KEY)**
  ```python
    import txtstr
    
    file = "file.txt"
    
    txtstr.encrypt(file,None)
    
    ```
  That this function can encrypt your file, the FILE section is where you can find the path of your .TXT file, CUSTOM_KEY if you put None it is because you want to use the default txtstr key, it is always advisable to create yours beforehand, to locate yours just type the name of the key (if it is in the same folder), but if it is in another folder, use the path of said file. Remember not to lose these keys since without this it will be IMPOSSIBLE to decrypt it
<br/>
<br/>
<br/>
<br/>
* **txtstr.decrypt(file, CUSTOM_KEY)**
  ```python
    import txtstr

    file = "file.txt"
    
    txtstr.decrypt(file, CUSTOM_KEY)
    
    ```
  Here you can decrypt your file, the FILE section is for the path of your file and the CUSTOM_KEY if you put None it is because you want to use the default txtstr key, it is always advisable to create yours beforehand, to locate yours just type the name of the key (if it is in the same folder), but if it is in another folder, use the path of said file
<br/>
<br/>
<br/>
<br/>

* **txtstr.write(text,name)**
  ```python
    import txtstr

    text = "the develpoer of txtstr is the best UnU"
    name = "isTRUE"
    
    txtstr.write(textname)
  
  ```
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


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Discord: [PingüiMaya14#2055](https://discord.com/invite/KfkA4MPME3)

WebSite: [pingui.tk](https://pingui.tk/)









[miniatura]: https://imgur.com/iehVgKR.png
