
import cli
import datetime

now=str(datetime.datetime.now()).replace(" ","-")
now=now.replace(":","-")

cli.executep("copy run tftp://10.0.99.136/backup-config-%s"%now)
