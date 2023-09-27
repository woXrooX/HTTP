if __name__ != "__main__":
	import json

	class Parser:
		JSON = {}

		######### APIs
		@staticmethod
		def parseRequest(RAW):
			# Converting to string
			RAW = RAW.decode()

			# Clean up JSON
			Parser.JSON = {}

			# Split RAW HTTP to head and body
			head = None
			body = None
			head_body_splitted = RAW.split("\r\n\r\n")

			# If RAW HTTP is splittable to two parts then head and body exists
			if len(head_body_splitted) == 2: head, body = head_body_splitted

			# Else only head exists
			else: head = RAW

			headers = head.split("\r\n")

			# No headers
			if len(headers) == 0:
				print("Invalid HTTP")
				return False

			Parser.JSON["requestLine"] = Parser.handleRequestLine(headers[0])

			# If request line is valid then remove it from the lines
			headers.pop(0)

			Parser.JSON["headers"] = Parser.handleHeaders(headers)

			Parser.JSON["body"] = Parser.handleBody(body)

			# Returns parsed HTTP data as DICT
			return Parser.JSON

		@staticmethod
		def parseResponse(RAW):
			# Converting to string
			RAW = RAW.decode()

			# Clean up JSON
			Parser.JSON = {}

			# Split RAW HTTP to head and body
			head = None
			body = None
			head_body_splitted = RAW.split("\r\n\r\n")

			# If RAW HTTP is splittable to two parts then head and body exists
			if len(head_body_splitted) == 2: head, body = head_body_splitted

			# Else only head exists
			else: head = RAW

			headers = head.split("\r\n")

			# No headers
			if len(headers) == 0:
				print("Invalid HTTP")
				return False

			Parser.JSON["statusLine"] = Parser.handleStatusLine(headers[0])

			# If status line is valid then remove it from the lines
			headers.pop(0)

			Parser.JSON["headers"] = Parser.handleHeaders(headers)

			Parser.JSON["body"] = Parser.handleBody(body)

			# Returns parsed HTTP data as DICT
			return Parser.JSON


		######### Helpers
		#### HTTP Request
		@staticmethod
		def handleRequestLine(requestLine):
			parts = requestLine.split(' ')
			if len(parts) != 3: return {}

			JSON = {
				"method": None,
				"URL": None,
				"HTTP_version": None
			}

			JSON["method"] = parts[0]
			JSON["URL"] = parts[1]
			JSON["HTTP_version"] = parts[2]

			return JSON

		#### HTTP Response
		def handleStatusLine(statusLine):
			parts = statusLine.split(' ')
			if len(parts) != 3: return {}

			JSON = {
				"HTTP_version": None,
				"status_code": None,
				"status_message": None
			}

			JSON["HTTP_version"] = parts[0]
			JSON["status_code"] = parts[1]
			JSON["status_message"] = parts[2]

			return JSON

		@staticmethod
		def handleHeaders(headers):
			JSON = {}

			for header in headers:
				splitted_header = header.split(': ')

				# Check if invalid header
				if len(splitted_header) != 2: continue

				JSON[splitted_header[0]] = splitted_header[1]

			return JSON

		@staticmethod
		def handleBody(body):
			if body is None: return ''

			# Check if content type is json then set body to json data from raw body
			if(
				"Content-Type" in Parser.JSON["headers"] and
				Parser.JSON["headers"]["Content-Type"] == "application/json"
			): return json.loads(body)

			else: return body

