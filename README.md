_Due to the nature of this project, it is classified as a "userbot" (a user account that automatically responds to users other than itself). "Userbots" are not allowed on Discord, and therefore I must state that I am not liable for any damages done to your account (i.e. warnings and bans) while using this program, as per the [license](https://github.com/PointyDev/discord-bughunternotifs/blob/master/LICENSE). Find out more [here](https://discordapp.com/terms)._
# Discord Bug Hunter Notifications
Small bot for Discord Bug Hunters that has custom configurable notifications for bug reports.

## Features
* Get notifications for only reports (meaning no commands or command outputs).
* Enable/disable new, denied and approved reports individually.
* Enable/disable different report categories individually (general, android, iOS, linux)

## Requirements
The last 4 can be installed by running `installdependancies.bat` if you have `pip` in your PATH.
* Be in [Discord Testers](https://discord.gg/discord-testers).
* Be a Discord Bug Hunter
* Windows 10
* Python 3.5+
* `discord.py` 0.16.8+ (may not be compatible after rewrite v1)
* `pypiwin32` (win10toast dependency)
* `setuptools` (win10toast dependency)
* `win10toast` 0.8+

## Installation instructions
* [Download the repo](https://github.com/PointyDev/discord-bughunternotifs/archive/master.zip)
* Install dependancies (see above)
* Duplicate `default_settings.py` and rename to `settings.py`
* Open `settings.py` IN A TEXT EDITOR and configure as wanted (see next section)
* Run `start.bat`

## How to configure
* Login token -  This can be found by following these steps:
> 1. Open desktop app or browser
> 2. Type `Ctrl`-`Shift`-`I`
> 3. Go to the Application tab
> 4. Under **Storage**, select **Local Storage**, and then **discordapp.com**
> 5. Find the `token` row and copy the value that is in quotes.
* If you want to enable a report platform, you must first enable the type of notification in the settings before
