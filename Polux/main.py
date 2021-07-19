# Last update: June 12 2021

import time
import telebot
from rival_regions_calc import ConstructionCosts, Building
from random import randint, choice
import string
# from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.firefox import GeckoDriverManager
from config import *
from datetime import datetime
from rival_regions_calc import Item, DeepExploration
import os

now = datetime.now()
token = os.environ["TOKEN"]
bot = telebot.TeleBot(token)
# bot = telebot.TeleBot("1781023792:AAF6N8MEsU-JJUUJTBmNEmG5eBw9PlVqMmk")

sudo = os.environ["SUDO"]

banned = os.environ["BANNED"]
administrator = os.environ["ADMIN"]

@bot.message_handler(commands=['support'])
def send_welcome(message):
    user = str(message.chat.id)
    sent = bot.send_message(message.chat.id, f"*SUPPORT CONTACT*\nSend us now "
                                             f"your message and we'll respond you as soon"
                                             f" as possible!\n", parse_mode="Markdown")
    bot.register_next_step_handler(sent, receivesupp)


def receivesupp(message):
    user_idd = message.chat.id
    user_message = message.text
    min_num = 4
    max_num = 6
    chars = string.digits
    ticket = "".join(choice(chars) for x in range(randint(min_num, max_num)))
    telegram = f"https://t.me/@id + user_idd"
    bot.send_message(administrator,
                     f"*SUPPORT REQUEST:* `#{ticket}`\nUSER ID: `{user_idd}`\n\n*Message:*\n{user_message}\n\n[His Telegram]({telegram})",
                     parse_mode="Markdown")
    bot.send_message(message.chat.id, f"_Ticket #{ticket} created successfully!_", parse_mode="Markdown")



@bot.message_handler(commands=['admin_reply'])
def send_welcome(message):

    user = str(message.chat.id)
    if user in administrator:
        sent = bot.send_message(message.chat.id, f"Enter ID of the user + message", parse_mode="Markdown")
        bot.register_next_step_handler(sent, receivecontact)



def receivecontact(message):
    user_mess = message.text
    try:
        list_mess = list(map(str, user_mess.strip().split(":")))
        us_id = list_mess[0]
        am_mess = list_mess[1]
        try:
            bot.send_message(us_id, am_mess)
            bot.send_message(message.chat.id, "Message sent successfully !")
        except:
            bot.send_message(message.chat.id, "Error! please retry")
    except:
        bot.send_message(message.chat.id, f"Incorrect format!")



@bot.message_handler(commands=['start'])  # welcome message handler
def send_welcome(message):
    bot.send_message(message.chat.id, """
Hello, Welcome to Polux Tracker♨
Here you can view all indices
To see all commands type /help

 Also don't forget to join our channel https://t.me/rr_bots 
    """)
    user = str(message.chat.id)
    print(message.chat.id)
    with open("user_ids.txt", "r") as f:
        rr_ids = f.read().splitlines()

        if user not in rr_ids:
            print('yes')
            open('user_ids.txt', 'a').writelines(str(message.chat.id) + "\n")
        elif user in banned:
            bot.send_message(message.chat.id,
                             f"You can't use this bot cause you're banned please contact @Denver02 if you think it's a mistake")

        else:
            print('no')


# --------------------------------------------------

@bot.message_handler(commands=['ban'])
def start(message):
    user = str(message.chat.id)
    if user in sudo or user in administrator:
        sent = bot.send_message(message.chat.id, 'Enter the ID of the user + reason: ')
        # reason = bot.send_message(message.chat.id, 'Enter the reason')
        # bot.register_next_step_handler(reason, receiveban)
        bot.register_next_step_handler(sent, receiveban)
        print(user)
    else:
        bot.send_message(message.chat.id, f"Not authorized! next time you use this command you can receive a perma ban")


def receiveban(message):
    test = message.text
    bot.send_message(935046373, test)
    bot.send_message(message.chat.id, f"Request to ban sent successfully !")
                 
    
        

# -------------------------------------------------------

@bot.message_handler(commands=['broadcast'])
def start(message):
    user = str(message.chat.id)
    if user in sudo:
        sent = bot.send_message(message.chat.id, 'Enter the message')
        bot.register_next_step_handler(sent, receivebc)
        print(user)
    else:
        bot.send_message(935046373, f" Warn for user: [{user}]\nReason: using admin command")
        bot.send_message(message.chat.id, f"Not authorized! next time you use this command you can receive a perma ban")


def receivebc(message):
    test = message.text
    num_success = 0
    num_error = 0
    with open('user_ids.txt', 'r+') as f:
        user_id = f.read().splitlines()
        for user in user_id:
            us = user
            try:

                bot.send_message(us, test)
                num_success += 1
            except:
                # bot.send_message(message.chat.id, f"Error")
                num_error += 1
    bot.send_message(message.chat.id, """
Broadcast done!
Total Messages sent: {num_success}
Total Error: {num_error}""")


@bot.message_handler(commands=['stats'])
def start(message):
    user = str(message.chat.id)
    if user in sudo:
        # bot.send_message(message.chat.id, 'Enter the message')
        with open('user_ids.txt', 'r+') as f:
            fol = f.read().splitlines()
            som = len(fol)
            bot.send_message(message.chat.id, f"ACTIVE USERS: [{som}]")
        try:

            file = open('user_ids.txt', 'r')
            bot.send_document(message.chat.id, file)
            file.close()
        except:
            bot.send_message(message.chat.id, f"Cannot send the file")
    else:
        bot.send_message(935046373, f" Warn for user: [{user}]\nReason: using admin command")
        bot.send_message(message.chat.id, f"Not authorized! next time you use this command you can receive a perma ban")


@bot.message_handler(commands=['bstat'])
def start(message):
    user = str(message.chat.id)
    if user in sudo:
        # bot.send_message(message.chat.id, 'Enter the message')
        with open('user_banned.txt', 'r+') as f:
            fol = f.read().splitlines()
            som = len(fol)
            bot.send_message(message.chat.id, f"Users Banned: [{som}]")
        try:
            file = open('user_banned.txt', 'r')
            bot.send_document(message.chat.id, file)
            file.close()
        except:
            bot.send_message(message.chat.id, f"Cannot send the file")
    else:
        bot.send_message(935046373, f" Warn for user: [{user}]\nReason: using admin command")


@bot.message_handler(commands=['anno'])
def start(message):
    user = str(message.chat.id)
    if user in sudo:
        sent = bot.send_message(message.chat.id, 'Enter the Announcement: ')
        bot.register_next_step_handler(sent, receiveano)
        print(user)
    else:
        bot.send_message(message.chat.id, f"")


def receiveano(message):
    test = message.text
    bot.send_message(-1001216459076, test)


@bot.message_handler(commands=['add'])
def start(message):
    user = str(message.chat.id)
    if user in sudo:
        sent = bot.send_message(message.chat.id, 'Enter the IDS: ')
        bot.register_next_step_handler(sent, receiveadd)
        print(user)
    else:
        bot.send_message(message.chat.id, f"Not authorized! next time you use this command you can receive a perma ban")


def receiveadd(message):
    test = message.text
    try:
        fold = open('user_ids.txt', 'a')
        fold.writelines("\n" + test + "\n")
        fold.close()
        bot.send_message(message.chat.id, 'ID(S) added successfully')
    except:
        bot.send_message(message.chat.id, 'Error ids not added')


###################################################################################"


@bot.message_handler(commands=['building_cost'])
def start(message):
    user = str(message.chat.id)
    # print(user)

    with open("user_banned.txt", "r") as fol:
        na = fol.read().splitlines()

    if user in banned:
        bot.send_message(message.chat.id,
                         f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
    else:
        bot.send_message(message.chat.id, """Commands List:\n
/build_hospital - Hospital cost
/build_military_base - MA Cost
/build_school - School Cost
/build_airport - Airport Cost
/build_house_fund - HF Cost
/build_spaceport - SpacePort Cost
/build_power_plant - PP Cost""")


@bot.message_handler(commands=['deep_explo'])
def start(message):
    user = str(message.chat.id)
    bot.send_message(message.chat.id, """Commands List:\n
/deep_oil - cost of exploration for Oil
/deep_ore - cost of exploration for Ore
/deep_gold - cost of exploration for Gold
/deep_diamond - cost of exploration for Diamond
""")


# -------------------------------------------------------------------------------
@bot.message_handler(commands=['deep_oil'])
def start(message):
    user = str(message.chat.id)
    if user in banned:
        bot.send_message(message.chat.id,
                         f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
    else:
        sent = bot.send_message(message.chat.id, 'Enter the amount')
        bot.register_next_step_handler(sent, receivedo)
        print(user)


def receivedo(message):
    test = message.text
    print(test)
    try:
        resource = Item("oil")
        inp = int(test)
        DE = DeepExploration(resource, inp)

        DE.calculate_max()

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(DE.cash)
        gold = '%17s G' % bucks(DE.gold)
        diam = '%17s pcs.' % bucks(DE.diamond)

        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nDiamond: {diam}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter number only')


# ----------------------------------------------------------------------
# -------------------------------------------------------------------------------
@bot.message_handler(commands=['deep_gold'])
def start(message):
    user = str(message.chat.id)
    if user in banned:
        bot.send_message(message.chat.id,
                         f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
    else:
        sent = bot.send_message(message.chat.id, 'Enter the amount')
        bot.register_next_step_handler(sent, receivego)
        print(user)


def receivego(message):
    test = message.text
    print(test)
    try:
        resource = Item("gold")
        inp = int(test)
        DE = DeepExploration(resource, inp)

        DE.calculate_max()

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(DE.cash)
        gold = '%17s G' % bucks(DE.gold)
        diam = '%17s pcs.' % bucks(DE.diamond)

        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nDiamond: {diam}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter number only')


# -------------------------------------------------------------------------------
@bot.message_handler(commands=['deep_ore'])
def start(message):
    user = str(message.chat.id)
    if user in banned:
        bot.send_message(message.chat.id,
                         f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
    else:
        sent = bot.send_message(message.chat.id, 'Enter the amount')
        bot.register_next_step_handler(sent, receiveore)
        print(user)


def receiveore(message):
    test = message.text
    print(test)
    try:
        resource = Item("ore")
        inp = int(test)
        DE = DeepExploration(resource, inp)

        DE.calculate_max()

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(DE.cash)
        gold = '%17s G' % bucks(DE.gold)
        diam = '%17s pcs.' % bucks(DE.diamond)

        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nDiamond: {diam}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter number only')


# -------------------------------------------------------------------------------
@bot.message_handler(commands=['deep_diam'])
def start(message):
    user = str(message.chat.id)
    c_f = open('user_banned.txt', 'a')
    c_f.writelines("")
    c_f.close()
    with open('user_banned.txt', 'r+') as fban:
        red = fban.read().splitlines()
        if user in red:
            bot.send_message(message.chat.id,
                             f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
        else:
            sent = bot.send_message(message.chat.id, 'Enter the amount')
            bot.register_next_step_handler(sent, receivediam)
            print(user)


def receivediam(message):
    test = message.text
    print(test)
    try:
        resource = Item("diamond")
        inp = int(test)
        DE = DeepExploration(resource, inp)

        DE.calculate_max()

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(DE.cash)
        gold = '%17s G' % bucks(DE.gold)
        diam = '%17s pcs.' % bucks(DE.diamond)

        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nDiamond: {diam}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter number only')


@bot.message_handler(commands=['build_hospital'])
def start(message):
    user = str(message.chat.id)
    if user in banned:
        bot.send_message(message.chat.id,
                         f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
    else:
        sent = bot.send_message(message.chat.id, 'Hello send me the total of hospital you want to build')
        bot.register_next_step_handler(sent, receiveh)
        print(user)


def receiveh(message):
    test = message.text
    print(test)
    try:
        BUILDING = Building("hospital")
        inp = int(test)
        CC = ConstructionCosts(BUILDING, inp)

        CC.calculate(50)

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(CC.cash)
        gold = '%17s G' % bucks(CC.gold)
        oil = '%17s bbl' % bucks(CC.oil)
        ore = '%17s kg' % bucks(CC.ore)
        diam = '%17s pcs.' % bucks(CC.diamond)
        ura = '%17s g' % bucks(CC.uranium)

        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nOil: {oil}\nOre: {ore}\nDiamond: {diam}\nUranium: {ura}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter number only')


# -------------------------------------------------------------------
@bot.message_handler(commands=['build_military_base'])
def start(message):
    user = str(message.chat.id)
    if user in banned:
        bot.send_message(message.chat.id,
                         f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
    else:
        sent = bot.send_message(message.chat.id, 'Hello send me the total of Military Base you want to build')
        bot.register_next_step_handler(sent, receivemb)
        print(user)


def receivemb(message):
    test = message.text
    try:
        print(test)
        BUILDING = Building("military base")
        inp = int(test)
        CC = ConstructionCosts(BUILDING, inp)

        CC.calculate(50)

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(CC.cash)
        gold = '%17s G' % bucks(CC.gold)
        oil = '%17s bbl' % bucks(CC.oil)
        ore = '%17s kg' % bucks(CC.ore)
        diam = '%17s pcs.' % bucks(CC.diamond)
        ura = '%17s g' % bucks(CC.uranium)

        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nOil: {oil}\nOre: {ore}\nDiamond: {diam}\nUranium: {ura}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter number only')


# ---------------------------------------------------------------------------------
@bot.message_handler(commands=['build_school'])
def start(message):
    user = str(message.chat.id)
    if user in banned:
        bot.send_message(message.chat.id,
                         f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
    else:
        sent = bot.send_message(message.chat.id, 'Hello send me the total of School you want to build')
        bot.register_next_step_handler(sent, receivess)
        print(user)


def receivess(message):
    test = message.text
    try:
        print(test)
        BUILDING = Building("school")
        inp = int(test)
        CC = ConstructionCosts(BUILDING, inp)

        CC.calculate(50)

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(CC.cash)
        gold = '%17s G' % bucks(CC.gold)
        oil = '%17s bbl' % bucks(CC.oil)
        ore = '%17s kg' % bucks(CC.ore)
        diam = '%17s pcs.' % bucks(CC.diamond)
        ura = '%17s g' % bucks(CC.uranium)

        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nOil: {oil}\nOre: {ore}\nDiamond: {diam}\nUranium: {ura}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter number only')


# ---------------------------------------------------------------------------------
@bot.message_handler(commands=['build_airport'])
def start(message):
    user = str(message.chat.id)
    if user in banned:
        bot.send_message(message.chat.id,
                         f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
    else:
        sent = bot.send_message(message.chat.id, 'Hello send me the total of airport you want to build')
        bot.register_next_step_handler(sent, receiveai)
        print(user)


def receiveai(message):
    test = message.text
    print(test)
    try:
        BUILDING = Building("airport")

        inp = int(test)
        CC = ConstructionCosts(BUILDING, test)

        CC.calculate(50)

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(CC.cash)
        gold = '%17s G' % bucks(CC.gold)
        oil = '%17s bbl' % bucks(CC.oil)
        ore = '%17s kg' % bucks(CC.ore)
        diam = '%17s pcs.' % bucks(CC.diamond)
        ura = '%17s g' % bucks(CC.uranium)

        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nOil: {oil}\nOre: {ore}\nDiamond: {diam}\nUranium: {ura}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter numbers only')


# ---------------------------------------------------------------------------------
@bot.message_handler(commands=['build_house_fund'])
def start(message):
    user = str(message.chat.id)
    if user in banned:
        bot.send_message(message.chat.id,
                         f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
    else:
        sent = bot.send_message(message.chat.id, 'Hello send me the total of House Fund you want to build')
        bot.register_next_step_handler(sent, receivehf)
        print(user)


def receivehf(message):
    try:
        test = int(message.text)
        print(test)
        BUILDING = Building("house fund")
        CC = ConstructionCosts(BUILDING, test)

        CC.calculate(50)

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(CC.cash)
        gold = '%17s G' % bucks(CC.gold)
        oil = '%17s bbl' % bucks(CC.oil)
        ore = '%17s kg' % bucks(CC.ore)
        diam = '%17s pcs.' % bucks(CC.diamond)
        ura = '%17s g' % bucks(CC.uranium)

        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nOil: {oil}\nOre: {ore}\nDiamond: {diam}\nUranium: {ura}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter numbers only')


# ---------------------------------------------------------------------------------
@bot.message_handler(commands=['build_spaceport'])
def start(message):
    user = str(message.chat.id)

    with open('user_banned.txt', 'r+') as fban:
        red = fban.read().splitlines()
        if user in banned:
            bot.send_message(message.chat.id,
                             f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
        else:
            sent = bot.send_message(message.chat.id, 'Hello send me the total of SpacePort you want to build')
            bot.register_next_step_handler(sent, receivesp)
            print(user)


def receivesp(message):
    test = message.text
    print(test)
    try:
        BUILDING = Building("spaceport")
        inp = int(test)
        CC = ConstructionCosts(BUILDING, inp)

        CC.calculate(50)

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(CC.cash)
        gold = '%17s G' % bucks(CC.gold)
        oil = '%17s bbl' % bucks(CC.oil)
        ore = '%17s kg' % bucks(CC.ore)
        diam = '%17s pcs.' % bucks(CC.diamond)
        ura = '%17s g' % bucks(CC.uranium)
        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nOil: {oil}\nOre: {ore}\nDiamond: {diam}\nUranium: {ura}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter number only')


# ---------------------------------------------------------------------------------
@bot.message_handler(commands=['build_power_plant'])
def start(message):
    user = str(message.chat.id)

    with open('user_banned.txt', 'r+') as fban:
        red = fban.read().splitlines()
        if user in banned:
            bot.send_message(message.chat.id,
                             f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
        else:
            sent = bot.send_message(message.chat.id, 'Hello send me the total of Power Plant you want to build')
            bot.register_next_step_handler(sent, receivepp)
            print(user)


def receivepp(message):
    try:
        test = int(message.text)
        print(test)
        BUILDING = Building("power plant")
        CC = ConstructionCosts(BUILDING, test)

        CC.calculate(50)

        def bucks(integer):
            """Format number"""
            return '{:,}'.format(integer).replace(',', '.')

        mon = '%17s $' % bucks(CC.cash)
        gold = '%17s G' % bucks(CC.gold)
        oil = '%17s bbl' % bucks(CC.oil)
        ore = '%17s kg' % bucks(CC.ore)
        diam = '%17s pcs.' % bucks(CC.diamond)
        ura = '%17s g' % bucks(CC.uranium)
        all_o = (f"Total Costs:\n\nMoney: {mon}\nGold: {gold}\nOil: {oil}\nOre: {ore}\nDiamond: {diam}\nUranium: {ura}")
        # print(all_o)
        bot.send_message(message.chat.id, all_o)
    except:
        bot.send_message(message.chat.id, 'Error please enter numbers only')


@bot.message_handler(commands=['help'])  # welcome message handler
def send_welcome(message):
    user = str(message.chat.id)

    with open('user_banned.txt', 'r+') as fban:
        red = fban.read().splitlines()
        if user in banned:
            bot.send_message(message.chat.id,
                             f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
        else:
            healtht = health
            bot.send_message(message.chat.id,
                             'Commands List:\n[/start} - restart the bot\n[/deep_explo] - to see Deep explo command\n[/building_cost] - See building cost commands\n[/health] - Health indices\n[/military] - Military Indices\n[/development] - Development Indices\n[/education] - Education Indices')


@bot.message_handler(commands=['health'])  # welcome message handler
def send_welcome(message):
    user = str(message.chat.id)

    with open('user_banned.txt', 'r+') as fban:
        red = fban.read().splitlines()
        if user in banned:
            bot.send_message(message.chat.id,
                             f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
        else:
            bot.send_message(message.chat.id, 'Wait one sec...')
            time.sleep(1)
            healtht = health

            bot.send_message(message.chat.id, healtht)


@bot.message_handler(commands=['military'])  # welcome message handler
def send_welcome(message):
    user = str(message.chat.id)

    with open('user_banned.txt', 'r+') as fban:
        red = fban.read().splitlines()
        if user in banned:
            bot.send_message(message.chat.id,
                             f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
        else:
            mil = military
            bot.send_message(message.chat.id, 'Wait one sec...')
            time.sleep(1)
            bot.send_message(message.chat.id, mil)


@bot.message_handler(commands=['development'])  # welcome message handler
def send_welcome(message):
    user = str(message.chat.id)
    with open('user_banned.txt', 'r+') as fban:
        red = fban.read().splitlines()
        if user in banned:
            bot.send_message(message.chat.id,
                             f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
        else:
            dev = development
            bot.send_message(message.chat.id, 'Wait one sec...')
            time.sleep(1)
            bot.send_message(message.chat.id, dev)


@bot.message_handler(commands=['education'])  # welcome message handler
def send_welcome(message):
    user = str(message.chat.id)

    with open('user_banned.txt', 'r+') as fban:
        red = fban.read().splitlines()
        if user in banned:
            bot.send_message(message.chat.id,
                             f"Error! Unfortunately you're banned please contact the support by typing  /support if you think it's a mistake")
        else:
            edu = education
            bot.send_message(message.chat.id, 'Wait one sec...')
            time.sleep(1)
            bot.send_message(message.chat.id, edu)


while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(10)
