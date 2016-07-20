import webapp2
from DOB_fn import main as dob
import sys
sys.path.insert(0,'/usr/lib/python2.7/dist-packages')

# def convert_temp(cel_temp):
#     ''' convert Celsius temperature to Fahrenheit temperature '''
#     if cel_temp == "":
#         return ""
#     try:
#         far_temp = float(cel_temp) * 9 / 5 + 32
#         far_temp = round(far_temp, 3)  # round to three decimal places
#         return str(far_temp)
#     except ValueError:  # user entered non-numeric temperature
#         return "invalid input"


class MainPage(webapp2.RequestHandler):
    def get(self):
        indte = self.request.get("indate")
        event = dob(indate)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>What excited your moma and dad :P </title></head>

            <body>
              <form action="/" method="get">
                Your DOB in ddmmyyyy: <input type="number"
                                        name="indate" value={}>
                <input type="submit" value="Convert"><br>
                Fahrenheit temperature: {}
              </form>
            </body>
          </html>""".format(indate, event))

routes = [('/', MainPage)]

my_app = webapp2.WSGIApplication(routes, debug=True)
