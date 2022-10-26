# Selenium script main loop

import download
import exceltransformation
import openpyxl


def main():
    download.download_initire()
    download.download_publiciare()
    download.change_directory()
    exceltransformation.software()
    exceltransformation.servicii()
    exceltransformation.hardware()


if __name__ == '__main__':
    main()
