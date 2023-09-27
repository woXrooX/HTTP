if __name__ != "__main__":
    import json

    class Parser:
        request_JSON = {
            "requestLine": {
                "method": None,
                "URL": None,
                "HTTP_version": None
            },
            "headers": {},
            "body": ''
        }

        response_JSON = {
            "statusLine": {
                "HTTP_version": None,
                "status_code": None,
                "status_message": None
            },
            "headers": {},
            "body": ''
        }

        ######### APIs
        @staticmethod
        def parseRequest(RAW):
            # Converting to string
            RAW = RAW.decode()

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

            if Parser.handleRequestLine(headers[0]) is False: return False

            # If request line is valid then remove it from the lines
            headers.pop(0)

            if Parser.handleRequestHeaders(headers) is False: return False

            Parser.handleRequestBody(body)

            # Returns parsed HTTP data as DICT
            return Parser.request_JSON

        @staticmethod
        def parseResponse(RAW):
            # Converting to string
            RAW = RAW.decode()

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

            if Parser.handleStatusLine(headers[0]) is False: return False

            # If request line is valid then remove it from the lines
            headers.pop(0)

            if Parser.handleResponseHeaders(headers) is False: return False

            Parser.handleResponseBody(body)

            # Returns parsed HTTP data as DICT
            return Parser.response_JSON



        ######### Helpers
        #### HTTP Request
        @staticmethod
        def handleRequestLine(requestLine):
            parts = requestLine.split(' ')
            if len(parts) != 3:
                print("Invalid HTTP request line")
                return False

            Parser.request_JSON["requestLine"]["method"] = parts[0]
            Parser.request_JSON["requestLine"]["URL"] = parts[1]
            Parser.request_JSON["requestLine"]["HTTP_version"] = parts[2]

        @staticmethod
        def handleRequestHeaders(headers):
            for header in headers:
                splitted_header = header.split(': ')
                if len(splitted_header) != 2:
                    print("Invalid HTTP header: ", splitted_header)
                    return False

                Parser.request_JSON["headers"][splitted_header[0]] = splitted_header[1]

        @staticmethod
        def handleRequestBody(body):
            if body is None:
                Parser.request_JSON["body"] = ''
                return

            # Check if content type is json then set body to json data from raw body
            if(
                "Content-Type" in Parser.request_JSON["headers"] and
                Parser.request_JSON["headers"]["Content-Type"] == "application/json"
            ): Parser.request_JSON["body"] = json.loads(body)

            else: Parser.request_JSON["body"] = body

        #### HTTP Response
        def handleStatusLine(statusLine):
            parts = statusLine.split(' ')
            if len(parts) != 3:
                print("Invalid HTTP status line")
                return False

            Parser.response_JSON["statusLine"]["HTTP_version"] = parts[0]
            Parser.response_JSON["statusLine"]["status_code"] = parts[1]
            Parser.response_JSON["statusLine"]["status_message"] = parts[2]

        @staticmethod
        def handleResponseHeaders(headers):
            for header in headers:
                splitted_header = header.split(': ')
                if len(splitted_header) != 2:
                    print("Invalid HTTP header: ", splitted_header)
                    return False

                Parser.response_JSON["headers"][splitted_header[0]] = splitted_header[1]

        @staticmethod
        def handleResponseBody(body):
            if body is None:
                Parser.response_JSON["body"] = ''
                return

            Parser.response_JSON["body"] = body

