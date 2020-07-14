# Discord Bot for BDO Bosses

## Table of Contents

- [ Introduction ](#intro)
- [ Technologies ](#tech)
- [ Usage ](#usage)

<a name="intro"></a>
## Intro

A project made for a friend, who wanted a list of bosses, which will appear at certain time in game of BDO. 

<a name="tech"></a>
## Technologies

- Python
- Discord

<a name="usage"></a>
## Usage

The bot works on a basic notion of sending information based on the command, which has been invoked while it's running on the Discord sever. By running the command: 

```
.b
```

All the bosses for that particular day, will be showcased, with next boss being highlighted. In Python the command uses asynchronous call to the server, which its connected to
to send all the information. An example of Pythonic command for Discord bot would be:

```
@client.command()
async def b(ctx):
    await ctx.send(functions.all_todays_bosses())
```

All the functions that are used by the bot are defined within bot_functions.py Every time the function is called, a software accesses given function, to send it back to the server 
and display accordingly. 


### Currently available functions

- `.b`
