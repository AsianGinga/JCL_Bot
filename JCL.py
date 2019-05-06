import discord
from discord.ext import commands
import random
import string
import time

jcl = commands.Bot(command_prefix='>')

@jcl.event
async def on_ready():
    print('JCL Bot: Version 1.22102_Update, type ">commands".')

@jcl.command()
async def gay(ctx):
    await ctx.send('no u')

@jcl.command()
async def say(ctx, amount: int, *message: str):
    for i in range(amount):
        message_sent=[]
        message_to_send=''
        for word in message:
            message_sent.append(word)
            message_to_send = message_to_send + ' ' + word
        print(message)
        print(message_sent)
        print(message_to_send)
        await ctx.send(message_to_send)

@jcl.command()
async def echo(ctx, *message):
    for word in message:
        message_send=message_send + word + ' '
    await ctx.send(message_send)

@jcl.command()
async def ping(ctx):
    await ctx.send(':ping_pong:')

@jcl.command()
async def gay_me(ctx):
    gay_percent=random.randint(0, 100)
    await ctx.send('You are: {}% gay. ;('.format(gay_percent))

@jcl.command()
async def gay_other(ctx, *other: str):
    gay_percent=random.randint(0, 100)
    gay_boi=''
    for word in other:
        gay_boi=gay_boi + word + ' '
    await ctx.send('@{} is {}% gay.'.format(gay_boi, gay_percent))

@jcl.command()
async def commands(ctx):
    await ctx.send('Commands prefix is \">\". Commands: gay, say(amount, message), echo(message), clear(amount), ping, gay_me, gay_other(member), choose(choices), token(length), roll(a, b), slots, coinflip, beg, error, oof, commands. Version 1.22102_Update')

@jcl.command()
async def i_made_a_bot_with_your_name_jacob(ctx):
    await ctx.send('yeah, he did.')

@jcl.command()
async def choose(ctx, *choices):
    choice = random.choice(choices)
    await ctx.send(choice)

@jcl.command()
async def token(ctx, length: int):
    token = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
    await ctx.send(token)

@jcl.command()
async def roll(ctx, a: int, b: int):
    num=random.randint(a, b)
    await ctx.send('You rolled a {}!'.format(num))

@jcl.command()
async def slots(ctx):
    win=0
    slot1=random.randint(1, 9)
    slot2=random.randint(1, 9)
    slot3=random.randint(1, 9)
    await ctx.send(slot1)
    time.sleep(1)
    await ctx.send(slot2)
    time.sleep(1)
    await ctx.send(slot3)
    if slot1==slot2==slot3:
        await ctx.send('Congratulations! You hit the jackpot (all slots match)!')
        win=1
    if slot1==slot2:
        await ctx.send('Congratulations! Both slot 1 and slot 2 are matching!')
        win=1
    if slot1==slot3:
        await ctx.send('Congratulations! Both slot 1 and slot 3 are matching!')
        win=1
    if slot2==slot3:
        await ctx.send('Congratulations! Both slot 2 and slot 3 are matching!')
        win=1
    if win==0:
        await ctx.send('Sorry, you lost. ;(')

@jcl.command()
async def coinflip(ctx):
    flip=random.randint(1, 2)
    if flip==2:
        await ctx.send('The coin landed on heads!')
    else:
        await ctx.send('The coin landed on tails!')

@jcl.command()
async def beg(ctx):
    decide=random.randint(1, 5)
    if decide==4:
        await ctx.send('Beg is still being developed, please wait for the dev to finish this command.')
    else:
        await ctx.send('Beg is still being developed, please wait for the dev to finish this command.')

@jcl.command()
async def error(ctx, *report):
    log=open('errorLog.txt', 'a')
    log.write('\n')
    log.write('NEW REPORT:')
    log.write('\n')
    report_to_send=''
    for word in report:
        report_to_send=report_to_send + word + ' '
    log.write(report_to_send)
    log.write('\n')
    await ctx.send('Thanks for reporting this error! My master will get right to it!')

@jcl.command()
async def clear(ctx, amount: int):
    deleted = await ctx.channel.purge(limit=100)
    await channel.send('Deleted {} message(s)'.format(len(deleted)))

@jcl.command()
async def oof(ctx):
    await ctx.send('https://www.roblox.com')

@jcl.command()
async def offline(ctx):
    if ctx.message.author.id==349011811728621568:
        await ctx.send('Exiting..')
        exit()
    else:
        await ctx.send('You don\'t have the required permissions to do this!')
    print(ctx.message.author.id)
    print(type(ctx.message.author.id))

jcl.run('NTY5MzY3NTk1ODAzODY5MTk1.XLvnFA.vLIoXQhwk9TRgtA4C8kzySxz5po')
