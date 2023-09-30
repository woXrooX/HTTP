from HTTP import HTTP
import json

if __name__ == "__main__":
	RAW_HTTP_Request_JSON = b"""POST /api/users HTTP/1.1\r\nHost: www.example.com\r\nContent-Type: application/json\r\nContent-Length: 56\r\n\r\n{"username": "john_doe", "email": "john_doe@example.com", "password": "secretpassword123"}"""

	RAW_HTTP_Request_multipartFormData = b"""POST /logIn HTTP/1.1\r\nAccept: */*\r\nConnection: keep-alive\r\nContent-Length: 326\r\nContent-Type: multipart/form-data; boundary=----WebKitFormBoundary889OWpkVcMRuBHFj\r\n\r\n------WebKitFormBoundary889OWpkVcMRuBHFj\r\nContent-Disposition: form-data; name="eMail"\r\n\n\r\n------WebKitFormBoundary889OWpkVcMRuBHFj\r\nContent-Disposition: form-data; name="password"\r\n\n\r\n------WebKitFormBoundary889OWpkVcMRuBHFj\r\nContent-Disposition: form-data; name="for"\r\n\nlogIn\r\n------WebKitFormBoundary889OWpkVcMRuBHFj--"""

	RAW_HTTP_Response = b"""HTTP/1.1 201 Created\r\nDate: Wed, 04 May 2022 15:30:00 GMT\r\nContent-Type: application/json\r\nContent-Length: 36\r\n\r\n{"id": "123456", "message": "User created successfully"}"""


	print("Request with body: JSON "+"-"*40)
	print(json.dumps(HTTP.parseRequest(RAW_HTTP_Request_JSON), indent=4))

	print("Request with body: multipart/form-data "+"-"*30)
	print(json.dumps(HTTP.parseRequest(RAW_HTTP_Request_multipartFormData), indent=4))

	print("Response "+"-"*40)
	print(json.dumps(HTTP.parseResponse(RAW_HTTP_Response), indent=4))
