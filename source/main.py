from HTTP import HTTP

if __name__ == "__main__":
  RAW_HTTP_Request = b"""POST /api/users HTTP/1.1\r\nHost: www.example.com\r\nContent-Type: application/json\r\nContent-Length: 56\r\n\r\n{"username": "john_doe", "email": "john_doe@example.com", "password": "secretpassword123"}"""

  RAW_HTTP_Response = b"""HTTP/1.1 201 Created\r\nDate: Wed, 04 May 2022 15:30:00 GMT\r\nContent-Type: application/json\r\nContent-Length: 36\r\n\r\n{"id": "123456", "message": "User created successfully"}"""

  print(HTTP.parseRequest(RAW_HTTP_Request))
  print(HTTP.parseResponse(RAW_HTTP_Response))
