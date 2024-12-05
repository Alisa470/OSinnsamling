#! /usr/bin/python
# -*- coding: UTF-8 -*-

# program som henter hardware og software informasjon fra en maskin
import platform
import psutil
import getpass
import socket
import subprocess


# funskjon som henter info om OS og versjon
def func_GetOSandVers():
    try:
        return (
            f"Operativsystem og versjon: {platform.system()} "
            f"{platform.version()}"
        )
    except Exception as fail:
        print("Noe gikk galt ved innhenting av info om OS og versjon...")
        print("Full informasjon om feilen:")
        print(fail)


# funskjon som henter info om ledig plass på disk
def func_GetFreeDiskSpace():
    try:
        var_infoDisk = psutil.disk_usage("/")
        return (f"Ledig plass på disk: "
                f"{round(var_infoDisk.free / (1024 ** 3), 2)} GB"
                )
    except Exception as fail:
        print("Noe gikk galt ved innhenting av info om ledig plass på disken...")
        print("Full informasjon om feilen:")
        print(fail)


# funskjon som henter info om bruker som er logget inn
def func_GetUser():
    try:
        return f"Bruker: {getpass.getuser()}"
    except Exception as fail:
        print("Noe gikk galt ved innhenting av info om bruker...")
        print("Full informasjon om feilen:")
        print(fail)


# funskjon som henter info om IP-adresse
def func_GetIPaddress():
    try:
        return f"IP-adresse: {socket.gethostbyname(socket.gethostname())}"
    except Exception as fail:
        print("Noe gikk galt ved innhenting av info om IP-adresse...")
        print("Full informasjon om feilen:")
        print(fail)


# funskjon som henter info om innstallert programvare
def func_GetInstalledSW():
    try:
        if platform.system() == "Windows":
            var_cmd = ("powershell \"Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName\"")
            return (f"Installert programvare: "
                    f"{subprocess.check_output(var_cmd, shell=True, text=True)}"
                    )
        elif platform.system() == "Linux":
            var_cmd = "sudo /usr/bin/dpkg --get-selections"
            return (f"Installert programvare: "
                    f"{subprocess.check_output(var_cmd, shell=True, text=True)}"
                    )
        elif platform.system() == "Darwin":
            var_cmd = "ls /Applications"
            return (f"Installert programvare: "
                    f"{subprocess.check_output(var_cmd, shell=True, text=True)}"
                    )
        else:
            return "Din OS støttes ikke"
    except Exception as fail:
        print("Noe gikk galt ved innhenting av info om innstalert programvare...")
        print("Full informasjon om feilen:")
        print(fail)


# funskjon som lagrer denne informasjonen i en fil på PC
def func_SaveToFile(var_FileName, var_Data):
    try:
        with open(var_FileName, "w") as obj_FileName:
            obj_FileName.write(var_Data)
        return f"Data lagret i filen {var_FileName}"
    except Exception as fail:
        print("Noe gikk galt ved lagring av filen...")
        print("Full informasjon om feilen:")
        print(fail)


# funskjon som samler inn alle funksjoner
def func_Main():
    global var_PCname, var_FileName, var_Data
    try:
        var_PCname = socket.gethostname()
        var_OSandVers = func_GetOSandVers()
        var_DiskFreeSpace = func_GetFreeDiskSpace()
        var_User = func_GetUser()
        var_IPaddress = func_GetIPaddress()
        var_InnstaledSW = func_GetInstalledSW()

        var_Data = (f"PC navn: {var_PCname}\n"
                    f"{var_OSandVers}\n"
                    f"{var_DiskFreeSpace}\n"
                    f"{var_User}\n"
                    f"{var_IPaddress}\n"
                    f"{var_InnstaledSW}\n"
                    )
        var_FileName = f"{var_PCname}_info.txt"
        var_Result = func_SaveToFile(var_FileName, var_Data)
        return var_Result
    except Exception as fail:
        print("Noe gikk galt...")
        print("Full informasjon om feilen:")
        print(fail)


if __name__ == "__main__":
    func_Main()
    print(f'Ferdig, data lagret i filen "{var_PCname}_info.txt"')
