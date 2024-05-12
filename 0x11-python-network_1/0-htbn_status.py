 #!/usr/bin/python3
  2 """Fetches https://alx-intranet.hbtn.io/status."""
  3 import urllib.request
  4
  5
  6 if __name__ == "__main__":
  7     request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
  8     with urllib.request.urlopen(request) as response:
  9         body = response.read()
 10         print("Body response:")
 11         print("\t- type: {}".format(type(body)))
 12         print("\t- content: {}".format(body))
 13         print("\t- utf8 content: {}".format(body.decode("utf-8")))
