# Bug Hunter Notifications - By Pointy#5565
# https://github.com/PointyDev/discord-bughunternotifs

import sys

try:
    from discord.ext import commands
    import discord
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
except ImportError:
    print("1 or more dependancies not installed, exiting.\nPlease check the repo for more information.")
    sys.exit()

try:
    sys.dont_write_bytecode = True
    from settings import *
except ImportError:
    print("No settings file present, exiting.\nPlease check the repo for more information.")
    sys.exit()

print("\nBug Hunter Notifications made by Pointy#5565 (99914384989519872).")
print("For support, DM me (via Discord Testers) or email me at pointy@ratelimited.me.")
print("Repo: https://github.com/PointyDev/discord-bughunternotifs")

bot = commands.Bot(command_prefix="You're a selfbot, dummy.", description="Bug Hunter Notifications - Made by Pointy#5565")


@bot.event
async def on_ready():
    bhg = discord.utils.get(bot.get_all_channels(), id="217764019661045761")
    if bhg.permissions_for(discord.utils.get(bot.get_all_members(), id=bot.user.id, server__id="197038439483310086")).read_messages is False:
        print("\nYou are not a Discord Bug Hunter, logging out.")
        bot.logout()
    else:
        print("\nBug Hunter Notifications now running on {} ({}).".format(str(bot.user), bot.user.id))


@bot.event
async def on_message(message):
    if message.type is discord.MessageType.default:
        reportchannels = ["197038744908333066", "232568032394870784", "202491590390841344", "238073742624948225"]
        messagelines = message.content.splitlines()
        if message.channel.id == "253923313460445184" and message.author.id == "240545475118235648":
            reporttype = None
            try:
                if messagelines[0].startswith("**#") and deniedEnabled:
                    reporttype = "Denied"
                elif messagelines[1].startswith("<#197038744908333066>") and newEnabled and generalEnabled:  # General report
                    reporttype = "General"
                elif messagelines[1].startswith("<#232568032394870784>") and newEnabled and androidEnabled:  # Android report
                    reporttype = "Android"
                elif messagelines[1].startswith("<#202491590390841344>") and newEnabled and iOSEnabled:  # iOS report
                    reporttype = "iOS"
                elif messagelines[1].startswith("<#238073742624948225>") and newEnabled and linuxEnabled:  # Linux report
                    reporttype = "Linux"
                else:
                    pass
            except IndexError:
                pass
            if reporttype == "Denied":
                reportid = messagelines[0].split("|")[0][3:-3]
                title = messagelines[0].split("|")[1][2:-21]
                print("\n-- Report Denied --\nID: {}\nTitle: {}".format(reportid, title))
                toaster.show_toast(title="Discord Testers - Report Denied",
                                   msg="ID: {}\nTitle: {}".format(reportid, title),
                                   icon_path="discordbugreport-denied.ico", duration=8)
                return
            elif reporttype:
                author = messagelines[1][24:-12]
                title = messagelines[3][23:]
                reportids = []
                for l in messagelines:
                    if l.startswith("Report ID: "):
                        reportids.append(l)
                reportid = reportids[-1][13:-2]
                print("\n-- New Report --\nCategory: {}\nID: {}\nAuthor: {}\nTitle: {}".format(reporttype, reportid, author, title))
                toaster.show_toast(title="Discord Testers - New Bug Report",
                                   msg="Category: {}\nID: {}\nAuthor: {}\nTitle: {}".format(reporttype, reportid, author, title),
                                   icon_path="discordbugreport-new.ico", duration=8)
                return
            else:
                return
        elif message.channel.id in reportchannels and message.author.id == "240545475118235648" and "trello.com/c/" in message.content:
            if approvedEnabled:
                channeltype = message.channel.name.split("-")[0]
                if channeltype == "general" and generalEnabled:
                    reporttype = "General"
                elif channeltype == "android" and androidEnabled:
                    reporttype = "Android"
                elif channeltype == "ios" and iOSEnabled:
                    reporttype = "iOS"
                elif channeltype == "linux" and linuxEnabled:
                    reporttype = "Linux"
                author = messagelines[1][14:-2]
                title = messagelines[2][23:]
                reportids = []
                for l in messagelines:
                    if l.startswith("<https://trello.com/c/"):
                        reportids.append(l)
                reportid = reportids[-1].split(" ")[2][3:-2]
                reportid += " - "
                reportid += reportids[-1].split(" ")[0].split("/")[-1][:-1]
                print("\n-- Approved Report --\nCategory: {}\nID: {}\nAuthor: {}\nTitle: {}".format(reporttype, reportid, author, title))
                toaster.show_toast(title="Discord Testers - Report Approved",
                                   msg="Category: {}\nID: {}\nAuthor: {}\nTitle: {}".format(reporttype, reportid, author, title),
                                   icon_path="discordbugreport-approved.ico", duration=8)
                return
        else:
            return
    else:
        return


@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass


try:
    print("\nLogging into Discord...")
    bot.run(token, bot=False)
except discord.LoginFailure:
    print("Login failed, please check your configuration.")
