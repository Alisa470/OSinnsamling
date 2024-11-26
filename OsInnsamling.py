import platform
import psutil
import getpass
import socket
import subprocess


def func_GetOSandVersion():
    try:
        return (
            f"Operativsystem og versjon: {platform.system()} "
            f"{platform.version()}"
        )
    except Exception as fail:
        print("Noe gikk galt...")
        print("Full informasjon om feilen:")
        print(fail)  # Full feilmelding


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


def func_GetBruker():
    try:
        return f"Bruker: {getpass.getuser()}"
    except Exception as fail:
        print("Noe gikk galt...")
        print("Full informasjon om feilen:")
        print(fail)


def func_GetIPaddress():
    try:
        return f"IP-adresse: {socket.gethostbyname(socket.gethostname())}"
    except Exception as fail:
        print("Noe gikk galt...")
        print("Full informasjon om feilen:")
        print(fail)


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
