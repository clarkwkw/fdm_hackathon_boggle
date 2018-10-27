from transport import FDMBrowser
from main import main
import algorithms
import json

USERNAME = "clarktest"
PASSWORD = "fdmclarkabc"
FDMURL = "http://192.168.100.69:8080/FDMWordament"
QUESTION_NO = 6
IS_PRACTICE = True
ANS_FILE = "output.json"

browser = FDMBrowser(FDMURL)
print("Logging in..")
browser.login(USERNAME, PASSWORD)
print("Loading problem..")
board = browser.load_problem(QUESTION_NO, IS_PRACTICE)

print("Problem %s:"%QUESTION_NO, board)

ans = main(algorithms.brute_force.solve, board)

with open(ANS_FILE, "w") as f:
	json.dump({"words": ans}, f, indent = 4)

print("Answer outputted to %s"%ANS_FILE)
browser.upload_solution(" ".join(ans))