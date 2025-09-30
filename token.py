import requests, json

API_URL='https://token-api67.vercel.app/cleanest/token' #free token gen

def get_token():
    print('req token...')
    try:
        r=requests.post(API_URL,headers={'Content-Type':'application/json'},timeout=10)
        d=r.json()
        print(json.dumps(d,indent=2))
        return d
    except Exception as e:
        print("Error:",e)
        try: 
            print("Status:",r.status_code,"Resp:",r.text)
        except: pass
        return None

if __name__=='__main__':
    t=get_token()
    print("\nDone!" if t else "\nFail!")
