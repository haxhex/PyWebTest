from bs4 import BeautifulSoup

import requests
# Open file - w : write
with open("data_country.txt", "w") as file:
    string1 = """Country,Total Cases,New Cases,Total Deaths,New Deaths,Total Recovered,New Recovered,Active Cases,Serious Critical,Tot Cases/1M pop"""
    file.write(string1+'\n')
    response = requests.get('https://www.worldometers.info/coronavirus/')
    # # print(response)
    print('response status code:', response.status_code)
    # print('text:', response.text)
    text_website = response.text
    soup = BeautifulSoup(text_website, 'html.parser')
    table_list = soup.find_all('table', attrs={"id": "main_table_countries_today"})
    print("table list numbers:", len(table_list))
    table = table_list[0]
    tbody = table.find('tbody')
    tr_list = tbody.find_all('tr')
    for j in range(8, 232):
        tr = tr_list[j] # 8 - 231
        td_list = tr.find_all('td')
        # print("USA tds:", td_list)
        td_list_text = []
        for i in range(1, len(td_list)-11):
            this_td_text = td_list[i].text
            td_list_text += [this_td_text]
        # print(td_list_text)
        for i in range(len(td_list_text)):
            if td_list_text[i] == '' or td_list_text[i] == ' ':
                td_list_text[i] = "unKnown"
            else:
                if i not in [0, 2, 4, 6]:
                    if td_list_text[i] != 'N/A' and td_list_text[i] != '' and td_list_text[i] != ' ':
                        td_list_text[i] = int(td_list_text[i].replace(",", ""))
        print(td_list_text)
        # write data in file 
        for i in td_list_text:
            file.write(str(i) + ',')
        file.write('\n')
        # first_td = td_list[1]
        # first_td_text = first_td.text
        # print("first_td_text:", first_td_text)
        # for i in range(len(tr_list)):
        #     print("tr_list:",i,'\n', tr_list[i])
        #     print("------------------")