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
        print("Noe gikk galt...")
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
        print("Noe gikk galt...")
        print("Full informasjon om feilen:")
        print(fail)


# funskjon som henter info om bruker som er logget inn
def func_GetUser():
    try:
        return f"Bruker: {getpass.getuser()}"
    except Exception as fail:
        print("Noe gikk galt...")
        print("Full informasjon om feilen:")
        print(fail)


# funskjon som henter info om IP-adresse
def func_GetIPaddress():
    try:
        return f"IP-adresse: {socket.gethostbyname(socket.gethostname())}"
    except Exception as fail:
        print("Noe gikk galt...")
        print("Full informasjon om feilen:")
        print(fail)


# funskjon som henter info om innstallert programvare
def func_GetInstalledSW():
    try:
        if platform.system() == "Windows":
            var_cmd = ("powershell "
                       "'Get-ItemProperty HKLM:\\Software\\Microsoft"
                       "\\Windows\\CurrentVersion\\Uninstall\\* "
                       "| Select-Object DisplayName'"
                       )
        elif platform.system() == "Linux":
            var_cmd = "dpkg --get-selections"
        elif platform.system() == "Darwin":
            var_cmd = "ls /Applications"
        else:
            return "Din OS støttes ikke"
        return (f"Installert programvare: "
                f"{subprocess.check_output(var_cmd, shell=True, text=True)}"
                )
    except Exception as fail:
        print("Noe gikk galt...")
        print("Full informasjon om feilen:")
        print(fail)


# funskjon som lagrer denne informasjonen i en fil på PC
def func_SaveToFile(var_FileName, var_Data):
    try:
        with open(var_FileName, "w"):
            var_FileName.write(var_Data)
    except Exception as fail:
        print("Noe gikk galt...")
        print("Full informasjon om feilen:")
        print(fail)


if __name__ == "__main__":
    var_OSandVers = func_GetOSandVers()
    var_DiskFreeSpace = func_GetFreeDiskSpace()
    var_User = func_GetUser()
    var_IPaddress = func_GetIPaddress()
    var_InnstaledSW = func_GetInstalledSW
