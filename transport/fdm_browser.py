import http.cookiejar as cookielib
from urllib import request, parse
import re

LETTER_REGEX = r'<p class="fdm-letter">(\w)</p>'
TIMER_REGEX = r'<p id="future_timer" hidden>(.*)</p>'

class FDMBrowser:
	def __init__(self, url):
		self.__cookie_jar = cookielib.CookieJar()
		handler = request.HTTPCookieProcessor(self.__cookie_jar)
		self.__opener = request.build_opener(handler)

		self.__url = url

	def login(self, team_name, password):
		fields = {
			"teamName": team_name,
			"password": password
		}

		with self.__opener.open(self.__url+"/login", data = parse.urlencode(fields).encode()) as page:
			page_content = page.read().decode("utf-8")
			if "no such user!" in page_content:
				raise Exception("Cannot login to FDM")

		print("cookies generated:")
		for cookie in self.__cookie_jar:
   			print(cookie.name, cookie.value, cookie.domain)

	def load_problem(self, problem_id, is_practice = True):
		if is_practice:
			return self.load_practice_problem(problem_id)
		else:
			return self.load_contest_problem(problem_id)


	def upload_solution(self, solution):
		fields = {
			"hacker_input": solution,
			"hacker_result": ""
		}
		with self.__opener.open(self.__url+"/game/landing", data = parse.urlencode(fields).encode()) as page:
			page_content = page.read().decode("utf-8")
			if page.getcode() != 200:
				raise Exception("Unknown error, check html content:\n"+page_content)

			finish_time = re.search(TIMER_REGEX, page_content).groups()[0]
			print("Check leadboard after %s"%finish_time)

	def load_practice_problem(self, problem_id):
		board = []

		with self.__opener.open(self.__url+"/game/%s"%problem_id) as page:
			page_content = page.read().decode("utf-8")
			
			for match in re.finditer(LETTER_REGEX, page_content):
				board.append(match.group(1))

		if len(board) == 0:
			raise Exception("Cannot load problem, check html content:\n"+page_content)
		return board

	def load_contest_problem(self, problem_id):
		raise NotImplementedError()

	def logout(self):
		with self.__opener.open(self.__url+"logout") as page:
			page_content = page.read().decode("utf-8")
			if page.getcode() != 200:
				raise Exception("Unknown error, check html content:\n"+page_content)