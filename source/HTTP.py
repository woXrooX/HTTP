if __name__ != "__main__":
	from Parser import Parser

	class HTTP:
		@staticmethod
		def parseRequest(RAW): return Parser.parseRequest(RAW)

		@staticmethod
		def parseResponse(RAW): return Parser.parseResponse(RAW)
