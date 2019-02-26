
# Drawin Text ChatBot

This is a chatbot program that converts text to letter-wide text, in which each letter consists of several characters

## How it's work

Query:

```Hello World!```

Answer:

```
╔╗╔╗╔═╗╔╗─╔╗─╔══╗─╔╗──╔╗╔══╗╔══╗─╔╗───╔╗╔╗
║║║║║╔╝║║─║║─║╔╗║─║║╔╗║║║╔╗║║╔╗║─║║───║║║║
║╚╝║║╚╗║║─║║─║║║║─║║║║║║║║║║║╚╝║─║║─╔═╝║║║
║╔╗║║╔╝║║─║║─║║║║─║║║║║║║║║║║╔╗║─║║─║╔╗║╚╝
║║║║║╚╗║╚╗║╚╗║╚╝║─║╚╝╚╝║║╚╝║║║║╚╗║╚╗║╚╝║╔╗
╚╝╚╝╚═╝╚═╝╚═╝╚══╝─╚════╝╚══╝╚╝╚═╝╚═╝╚══╝╚╝
```

## Link on working bot

[Here](https://vk.com/im?sel=-146168940) - You must be authenticated on vk.com to use it

### How can I use it?

You can run your own bot on vk.com using all ```pyfiles``` or use only functions in file ```messageHandler.py``` to covert the text only in program

## Istalling

If you want run bot on [vk.com](vk.com) you should set a ```token```, ```group_id ``` and ```confirmation_token``` in ```settings.py``` on your group values and run this FlaskApp on your server.

If you want use it only as text converter, copy only ```get_answer(body)``` (where ```body``` - text that you convert) from ```messageHandler.py``` and other functions which calles from ```get_answer(body)```

## Author

* **Maxim Shakura** - [M2000h](https://github.com/M2000h)

## License

This project is licensed under the MIT License - see the [license website](https://opensource.org/licenses/MIT) file for details
