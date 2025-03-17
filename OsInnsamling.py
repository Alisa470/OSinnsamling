#! /usr/bin/python
# -*- coding: UTF-8 -*-

# program som henter hardware og software informasjon fra en maskin
import platform
import psutil
import getpass
import socket
import subprocess


# funksjon som henter info om OS og versjon
def func_GetOSandVers():
    try:
        # returnerer operativsystem og versjon
        return (
            f"Operativsystem og versjon: {platform.system()} "
            f"{platform.version()}"
        )
    except Exception as fail:
        print("Noe gikk galt ved innhenting av info om OS og versjon...")
        print("Full informasjon om feilen:")
        print(fail)


# funksjon som henter info om ledig plass på disk
def func_GetFreeDiskSpace():
    try:
        # henter diskbruk informasjon
        var_infoDisk = psutil.disk_usage("/")
        # returnerer ledig plass på disken i GB
        return (f"Ledig plass på disk: "
                f"{round(var_infoDisk.free / (1024 ** 3), 2)} GB"
                )
    except Exception as fail:
        print("Noe gikk galt ved innhenting av info om ledig plass på disken...")
        print("Full informasjon om feilen:")
        print(fail)


# funksjon som henter info om bruker som er logget inn
def func_GetUser():
    try:
        # returnerer brukernavn til den innloggede brukeren
        return f"Bruker: {getpass.getuser()}"
    except Exception as fail:
        print("Noe gikk galt ved innhenting av info om bruker...")
        print("Full informasjon om feilen:")
        print(fail)


# funksjon som henter info om IP-adresse
def func_GetIPaddress():
    try:
        # returnerer IP-adressen til maskinen
        return f"IP-adresse: {socket.gethostbyname(socket.gethostname())}"
    except Exception as fail:
        print("Noe gikk galt ved innhenting av info om IP-adresse...")
        print("Full informasjon om feilen:")
        print(fail)


# funksjon som henter info om installert programvare
def func_GetInstalledSW():
    try:
        if platform.system() == "Windows":
            # kommando for å hente installert programvare på Windows
            var_cmd = ("powershell \"Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName\"")
            return (f"Installert programvare: "
                    f"{subprocess.check_output(var_cmd, shell=True, text=True)}"
                    )
        elif platform.system() == "Linux":
            # kommando for å hente installert programvare på Linux
            var_cmd = "sudo /usr/bin/dpkg --get-selections"
            return (f"Installert programvare: "
                    f"{subprocess.check_output(var_cmd, shell=True, text=True)}"
                    )
        elif platform.system() == "Darwin":
            # kommando for å hente installert programvare på macOS
            var_cmd = "ls /Applications"
            return (f"Installert programvare: "
                    f"{subprocess.check_output(var_cmd, shell=True, text=True)}"
                    )
        else:
            return "Din OS støttes ikke"
    except Exception as fail:
        print("Noe gikk galt ved innhenting av info om installert programvare...")
        print("Full informasjon om feilen:")
        print(fail)


# funksjon som lagrer denne informasjonen i en fil på PC
def func_SaveToFile(var_FileName, var_Data):
    try:
        # åpner filen i skrive-modus og skriver data til filen
        with open(var_FileName, "w") as obj_FileName:
            obj_FileName.write(var_Data)
        return f"Data lagret i filen {var_FileName}"
    except Exception as fail:
        print("Noe gikk galt ved lagring av filen...")
        print("Full informasjon om feilen:")
        print(fail)


# funksjon som samler inn alle funksjoner
def func_Main():
    global var_PCname, var_FileName, var_Data
    try:
        # henter maskinnavn
        var_PCname = socket.gethostname()
        # henter OS og versjon
        var_OSandVers = func_GetOSandVers()
        # henter ledig diskplass
        var_DiskFreeSpace = func_GetFreeDiskSpace()
        # henter innlogget bruker
        var_User = func_GetUser()
        # henter IP-adresse
        var_IPaddress = func_GetIPaddress()
        # henter installert programvare
        var_InnstaledSW = func_GetInstalledSW()

        # samler all data i en streng
        var_Data = (f"PC navn: {var_PCname}\n"
                    f"{var_OSandVers}\n"
                    f"{var_DiskFreeSpace}\n"
                    f"{var_User}\n"
                    f"{var_IPaddress}\n"
                    f"{var_InnstaledSW}\n"
                    )
        # setter filnavn basert på maskinnavn
        var_FileName = f"{var_PCname}_info.txt"
        # lagrer data til fil
        var_Result = func_SaveToFile(var_FileName, var_Data)
        return var_Result
    except Exception as fail:
        print("Noe gikk galt...")
        print("Full informasjon om feilen:")
        print(fail)


if __name__ == "__main__":
    # kaller hovedfunksjonen og skriver ut resultatet
    result = func_Main()
    print(f'Ferdig, data lagret i filen "{var_PCname}_info.txt"')
    print(result)
