# Let's build a python API for Bible Gateway

# Available classes
## Bible
* open(book, chapter, verse) := _returns bible text_
## API
* fetch(book, chapter, verse) := _returns API response_
## Parser
This class will be used to parse response returned from the API gateway.

Parser(response) := _an instance of the Parser_
* content := _bible text_

# Installation
```bash
git clone https://github.com/andela-dJames/python pyble
cd pyble
```

# Usage
```bash
pyble open Genesis 1:1
```

# Libraries
* Beautiful Soup 4
* requests
* nosetests

# APIs
* Bible Gateway