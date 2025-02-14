from requests_html import HTMLSession

def weather():
    s = HTMLSession()
    query = "Kalutara"
    url = f"https://www.google.com/search?q=weather+{query}"
    
    
    r = s.get(url, headers= {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"})
    

    temp_element = r.html.find('span#wob_tm', first=True)
    if temp_element:
        temp = temp_element.text
        print(temp)
    else:
        print("Temperature not found!")
        return None
    
    unit_element = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
    if unit_element:
        unit = unit_element.text
        print(unit)
    else:
        print("Unit not found!")
        return None
    
    
    desc_element = r.html.find('span#wob_dc', first=True)
    if desc_element:
        desc = desc_element.text
        print(desc)
    else:
        print("Description not found!")
        return None
    
    return temp + " " + unit + " " + desc

weather()
