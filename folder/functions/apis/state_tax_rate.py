from requests import get, codes
from dotenv import load_dotenv;
import os;
import json;

load_dotenv();
api_key = os.getenv("api_key");

def SalesTax(zip=88901):
   zip_code = zip
   api_url = 'https://api.api-ninjas.com/v1/salestax?zip_code={}'.format(zip_code)
   try:
      response = get(api_url, headers={'X-Api-Key': api_key});

      if response.status_code == codes.ok:
         #response.text = [{"zip_code": "60639", "total_rate": "0.102500", "state_rate": "0.062500", "city_rate": "0.012500", "county_rate": "0.017500", "additional_rate": "0.010000"}] 
         return float(json.loads(response.text)[0]["state_rate"]); #MUST PARSE JSON!!!!!
      else: raise Exception()
   except Exception as err:
      return f"ERROR!!! {dict(message=response.text, statusCode=response.status_code, Exception=err)}";
