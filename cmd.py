import sys,getopt
import subprocess
from multiprocessing import Process
def main(argv):
	try:
		opts, args = getopt.getopt(argv, "ht", ["help","time="])
		for opt, arg in opts:
			if opt in ("-h", "--help"):
				print("vk auto messanger v 1.0 Vladislav Rogovsky")
				sys.exit()
			elif opt in ("-t", "--time"):
				if args:
					time = args
					return time
	except getopt.GetoptError:
			print ("No such paramet, all set to default")


if __name__ == "__main__":
	main(sys.argv[1:])
	Process(target=subprocess.call, args=(('ls', '-l', ), )).start()
	print(main(sys.argv[1:]))