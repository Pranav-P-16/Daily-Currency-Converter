from bs4 import BeautifulSoup
import requests
from PySimpleGUI import *
from urllib.request import urlopen

def currencyconverter():
    def net_connection():
        try:
            urlopen('https://www.google.com',timeout=5)
            return True
        except:
            SystemTray.notify('No Internet Connection',"Can't Sync Currency Values")
            currencyconverter()
    def about():
        lt=[[Text("## ABOUT ##",font=("Helvetica",20))],
            [Text("---------------------------",font=("Helvetica",20))],
            [Text("* Created and Compiled by PR@16 Creations\n* Thank you for Downloading\n* Requires Internet Connection\n* All Informations are collected from Internet\n* We don't have any responsibility regarding the accuracy of data\n* Credits: PR@16 Creations",font=("Helvetica",15))],
            [Text("---------------------------",font=("Helvetica",20))],
            [Button("OK",size=(80,2),button_color=("black","lightblue"))]]
        wn=Window("About",lt,keep_on_top=True)
        e,v=wn.read()
        wn.close()
        currencyconverter()
    def mn():
        theme("Topanga")
        layout1=[[Text("\nDAILY",font=("Helvetica",20))],[Text("CURRENCY CONVERTER\n",font=("Helvetica",20))],[Button("Convert Currency",font=("Helvetica",20),button_color=("black","green"),size=(100,1),bind_return_key=True)],
                         [Button("Crypto Currency",button_color=("black","orange"),font=("Helvetica",20),size=(100,1),bind_return_key=True)],
                         [Button("About",font=("Helvetica",20),size=(100,1),button_color=("black","lightblue"),bind_return_key=True)],
                         [Button("Exit",font=("Helvetica",20),size=(100,1),button_color=("black","red"),bind_return_key=True)],
                         [Text("\nVersion 2.6.0")]]
        window1=Window("Daily Currency Converter",layout1,size=(390, 400),element_justification="c",keep_on_top=True)
        event,values=window1.read()
        window1.close()
        if event==None or event=="Exit":
            exit()
        elif event=="About":
            about()
        elif event=="Crypto Currency":
            return "c"
        else:
            return "n"
    data_crypto={'Central African CFA Franc BEAC': 'XAF', 'Silver Ounce': 'XAG', 'Gold Ounce': 'XAU', 'Bitcoin': 'XBT', 'East Caribbean Dollar': 'XCD',
                     'IMF Special Drawing Rights': 'XDR', 'CFA Franc': 'XOF', 'Palladium Ounce': 'XPD', 'CFP Franc': 'XPF', 'Platinum Ounce': 'XPT','Emirati Dirham': 'AED', 'Afghan Afghani': 'AFN', 'Albanian Lek': 'ALL', 'Armenian Dram': 'AMD', 'Dutch Guilder': 'ANG', 'Angolan Kwanza': 'AOA',
          'Argentine Peso': 'ARS', 'Australian Dollar': 'AUD', 'Aruban or Dutch Guilder': 'AWG', 'Azerbaijan Manat': 'AZN', 'Bosnian Convertible Mark': 'BAM',
          'Barbadian or Bajan Dollar': 'BBD', 'Bangladeshi Taka': 'BDT', 'Bulgarian Lev': 'BGN', 'Bahraini Dinar': 'BHD', 'Burundian Franc': 'BIF',
          'Bermudian Dollar': 'BMD', 'Bruneian Dollar': 'BND', 'Bolivian Bolíviano': 'BOB', 'Brazilian Real': 'BRL', 'Bahamian Dollar': 'BSD',
          'Bhutanese Ngultrum': 'BTN', 'Botswana Pula': 'BWP', 'Belarusian Ruble': 'BYR', 'Belizean Dollar': 'BZD', 'Canadian Dollar': 'CAD', 'Congolese Franc': 'CDF',
          'Swiss Franc': 'CHF', 'Chilean Peso': 'CLP', 'Chinese Yuan Renminbi': 'CNY', 'Colombian Peso': 'COP', 'Costa Rican Colon': 'CRC',
          'Cuban Convertible Peso': 'CUC', 'Cuban Peso': 'CUP', 'Cape Verdean Escudo': 'CVE', 'Czech Koruna': 'CZK', 'Djiboutian Franc': 'DJF',
          'Danish Krone': 'DKK', 'Dominican Peso': 'DOP', 'Algerian Dinar': 'DZD', 'Estonian Kroon': 'EEK', 'Egyptian Pound': 'EGP', 'Eritrean Nakfa': 'ERN',
          'Ethiopian Birr': 'ETB', 'Euro': 'EUR', 'Fijian Dollar': 'FJD', 'Falkland Island Pound': 'FKP', 'British Pound': 'GBP', 'Georgian Lari': 'GEL',
          'Guernsey Pound': 'GGP', 'Ghanaian Cedi': 'GHS', 'Gibraltar Pound': 'GIP', 'Gambian Dalasi': 'GMD', 'Guinean Franc': 'GNF', 'Guatemalan Quetzal': 'GTQ',
          'Guyanese Dollar': 'GYD', 'Hong Kong Dollar': 'HKD', 'Honduran Lempira': 'HNL', 'Croatian Kuna': 'HRK', 'Haitian Gourde': 'HTG', 'Hungarian Forint': 'HUF',
          'Indonesian Rupiah': 'IDR', 'Israeli Shekel': 'ILS', 'Isle of Man Pound': 'IMP', 'Indian Rupee': 'INR', 'Iraqi Dinar': 'IQD', 'Iranian Rial': 'IRR',
          'Icelandic Krona': 'ISK', 'Jersey Pound': 'JEP', 'Jamaican Dollar': 'JMD', 'Jordanian Dinar': 'JOD', 'Japanese Yen': 'JPY', 'Kenyan Shilling': 'KES',
          'Kyrgyzstani Som': 'KGS', 'Cambodian Riel': 'KHR', 'Comorian Franc': 'KMF', 'North Korean Won': 'KPW', 'South Korean Won': 'KRW',
          'Kuwaiti Dinar': 'KWD', 'Caymanian Dollar': 'KYD', 'Kazakhstani Tenge': 'KZT', 'Lao Kip': 'LAK', 'Lebanese Pound': 'LBP',
          'Sri Lankan Rupee': 'LKR', 'Liberian Dollar': 'LRD', 'Basotho Loti': 'LSL', 'Lithuanian Litas': 'LTL', 'Latvian Lat': 'LVL',
          'Libyan Dinar': 'LYD', 'Moroccan Dirham': 'MAD', 'Moldovan Leu': 'MDL', 'Malagasy Ariary': 'MGA', 'Macedonian Denar': 'MKD', 'Burmese Kyat': 'MMK',
          'Mongolian Tughrik': 'MNT', 'Macau Pataca': 'MOP', 'Mauritanian Ouguiya': 'MRU', 'Mauritian Rupee': 'MUR', 'Maldivian Rufiyaa': 'MVR',
          'Malawian Kwacha': 'MWK', 'Mexican Peso': 'MXN', 'Malaysian Ringgit': 'MYR', 'Mozambican Metical': 'MZN', 'Namibian Dollar': 'NAD',
          'Nigerian Naira': 'NGN', 'Nicaraguan Cordoba': 'NIO', 'Norwegian Krone': 'NOK', 'Nepalese Rupee': 'NPR', 'New Zealand Dollar': 'NZD', 'Omani Rial': 'OMR',
          'Panamanian Balboa': 'PAB', 'Peruvian Sol': 'PEN', 'Papua New Guinean Kina': 'PGK', 'Philippine Peso': 'PHP', 'Pakistani Rupee': 'PKR', 'Polish Zloty': 'PLN',
          'Paraguayan Guarani': 'PYG', 'Qatari Riyal': 'QAR', 'Romanian Leu': 'RON', 'Serbian Dinar': 'RSD', 'Russian Ruble': 'RUB', 'Rwandan Franc': 'RWF',
          'Saudi Arabian Riyal': 'SAR', 'Solomon Islander Dollar': 'SBD', 'Seychellois Rupee': 'SCR', 'Sudanese Pound': 'SDG', 'Swedish Krona': 'SEK',
          'Singapore Dollar': 'SGD', 'Saint Helenian Pound': 'SHP', 'Sierra Leonean Leone': 'SLL', 'Somali Shilling': 'SOS', 'Seborgan Luigino': 'SPL',
          'Surinamese Dollar': 'SRD', 'Sao Tomean Dobra': 'STN', 'Salvadoran Colon': 'SVC', 'Syrian Pound': 'SYP', 'Swazi Lilangeni': 'SZL', 'Thai Baht': 'THB',
          'Tajikistani Somoni': 'TJS', 'Turkmenistani Manat': 'TMT', 'Tunisian Dinar': 'TND', "Tongan Pa'anga": 'TOP', 'Turkish Lira': 'TRY', 'Trinidadian Dollar': 'TTD',
          'Tuvaluan Dollar': 'TVD', 'Taiwan New Dollar': 'TWD', 'Tanzanian Shilling': 'TZS', 'Ukrainian Hryvnia': 'UAH', 'Ugandan Shilling': 'UGX', 'US Dollar': 'USD',
          'Uruguayan Peso': 'UYU', 'Uzbekistani Som': 'UZS', 'Venezuelan Bolívar': 'VES', 'Vietnamese Dong': 'VND', 'Ni Vanuatu Vatu': 'VUV', 'Samoan Tala': 'WST',
          'Yemeni Rial': 'YER', 'South African Rand': 'ZAR', 'Zambian Kwacha': 'ZMW', 'Zimbabwean Dollar': 'ZWD','Central African CFA Franc BEAC': 'XAF', 'Silver Ounce': 'XAG', 'Gold Ounce': 'XAU', 'Bitcoin': 'XBT', 'East Caribbean Dollar': 'XCD',
          'IMF Special Drawing Rights': 'XDR', 'CFA Franc': 'XOF', 'Palladium Ounce': 'XPD', 'CFP Franc': 'XPF', 'Platinum Ounce': 'XPT'}
    vl=mn()
    data={'Emirati Dirham': 'AED', 'Afghan Afghani': 'AFN', 'Albanian Lek': 'ALL', 'Armenian Dram': 'AMD', 'Dutch Guilder': 'ANG', 'Angolan Kwanza': 'AOA',
          'Argentine Peso': 'ARS', 'Australian Dollar': 'AUD', 'Aruban or Dutch Guilder': 'AWG', 'Azerbaijan Manat': 'AZN', 'Bosnian Convertible Mark': 'BAM',
          'Barbadian or Bajan Dollar': 'BBD', 'Bangladeshi Taka': 'BDT', 'Bulgarian Lev': 'BGN', 'Bahraini Dinar': 'BHD', 'Burundian Franc': 'BIF',
          'Bermudian Dollar': 'BMD', 'Bruneian Dollar': 'BND', 'Bolivian Bolíviano': 'BOB', 'Brazilian Real': 'BRL', 'Bahamian Dollar': 'BSD',
          'Bhutanese Ngultrum': 'BTN', 'Botswana Pula': 'BWP', 'Belarusian Ruble': 'BYR', 'Belizean Dollar': 'BZD', 'Canadian Dollar': 'CAD', 'Congolese Franc': 'CDF',
          'Swiss Franc': 'CHF', 'Chilean Peso': 'CLP', 'Chinese Yuan Renminbi': 'CNY', 'Colombian Peso': 'COP', 'Costa Rican Colon': 'CRC',
          'Cuban Convertible Peso': 'CUC', 'Cuban Peso': 'CUP', 'Cape Verdean Escudo': 'CVE', 'Czech Koruna': 'CZK', 'Djiboutian Franc': 'DJF',
          'Danish Krone': 'DKK', 'Dominican Peso': 'DOP', 'Algerian Dinar': 'DZD', 'Estonian Kroon': 'EEK', 'Egyptian Pound': 'EGP', 'Eritrean Nakfa': 'ERN',
          'Ethiopian Birr': 'ETB', 'Euro': 'EUR', 'Fijian Dollar': 'FJD', 'Falkland Island Pound': 'FKP', 'British Pound': 'GBP', 'Georgian Lari': 'GEL',
          'Guernsey Pound': 'GGP', 'Ghanaian Cedi': 'GHS', 'Gibraltar Pound': 'GIP', 'Gambian Dalasi': 'GMD', 'Guinean Franc': 'GNF', 'Guatemalan Quetzal': 'GTQ',
          'Guyanese Dollar': 'GYD', 'Hong Kong Dollar': 'HKD', 'Honduran Lempira': 'HNL', 'Croatian Kuna': 'HRK', 'Haitian Gourde': 'HTG', 'Hungarian Forint': 'HUF',
          'Indonesian Rupiah': 'IDR', 'Israeli Shekel': 'ILS', 'Isle of Man Pound': 'IMP', 'Indian Rupee': 'INR', 'Iraqi Dinar': 'IQD', 'Iranian Rial': 'IRR',
          'Icelandic Krona': 'ISK', 'Jersey Pound': 'JEP', 'Jamaican Dollar': 'JMD', 'Jordanian Dinar': 'JOD', 'Japanese Yen': 'JPY', 'Kenyan Shilling': 'KES',
          'Kyrgyzstani Som': 'KGS', 'Cambodian Riel': 'KHR', 'Comorian Franc': 'KMF', 'North Korean Won': 'KPW', 'South Korean Won': 'KRW',
          'Kuwaiti Dinar': 'KWD', 'Caymanian Dollar': 'KYD', 'Kazakhstani Tenge': 'KZT', 'Lao Kip': 'LAK', 'Lebanese Pound': 'LBP',
          'Sri Lankan Rupee': 'LKR', 'Liberian Dollar': 'LRD', 'Basotho Loti': 'LSL', 'Lithuanian Litas': 'LTL', 'Latvian Lat': 'LVL',
          'Libyan Dinar': 'LYD', 'Moroccan Dirham': 'MAD', 'Moldovan Leu': 'MDL', 'Malagasy Ariary': 'MGA', 'Macedonian Denar': 'MKD', 'Burmese Kyat': 'MMK',
          'Mongolian Tughrik': 'MNT', 'Macau Pataca': 'MOP', 'Mauritanian Ouguiya': 'MRU', 'Mauritian Rupee': 'MUR', 'Maldivian Rufiyaa': 'MVR',
          'Malawian Kwacha': 'MWK', 'Mexican Peso': 'MXN', 'Malaysian Ringgit': 'MYR', 'Mozambican Metical': 'MZN', 'Namibian Dollar': 'NAD',
          'Nigerian Naira': 'NGN', 'Nicaraguan Cordoba': 'NIO', 'Norwegian Krone': 'NOK', 'Nepalese Rupee': 'NPR', 'New Zealand Dollar': 'NZD', 'Omani Rial': 'OMR',
          'Panamanian Balboa': 'PAB', 'Peruvian Sol': 'PEN', 'Papua New Guinean Kina': 'PGK', 'Philippine Peso': 'PHP', 'Pakistani Rupee': 'PKR', 'Polish Zloty': 'PLN',
          'Paraguayan Guarani': 'PYG', 'Qatari Riyal': 'QAR', 'Romanian Leu': 'RON', 'Serbian Dinar': 'RSD', 'Russian Ruble': 'RUB', 'Rwandan Franc': 'RWF',
          'Saudi Arabian Riyal': 'SAR', 'Solomon Islander Dollar': 'SBD', 'Seychellois Rupee': 'SCR', 'Sudanese Pound': 'SDG', 'Swedish Krona': 'SEK',
          'Singapore Dollar': 'SGD', 'Saint Helenian Pound': 'SHP', 'Sierra Leonean Leone': 'SLL', 'Somali Shilling': 'SOS', 'Seborgan Luigino': 'SPL',
          'Surinamese Dollar': 'SRD', 'Sao Tomean Dobra': 'STN', 'Salvadoran Colon': 'SVC', 'Syrian Pound': 'SYP', 'Swazi Lilangeni': 'SZL', 'Thai Baht': 'THB',
          'Tajikistani Somoni': 'TJS', 'Turkmenistani Manat': 'TMT', 'Tunisian Dinar': 'TND', "Tongan Pa'anga": 'TOP', 'Turkish Lira': 'TRY', 'Trinidadian Dollar': 'TTD',
          'Tuvaluan Dollar': 'TVD', 'Taiwan New Dollar': 'TWD', 'Tanzanian Shilling': 'TZS', 'Ukrainian Hryvnia': 'UAH', 'Ugandan Shilling': 'UGX', 'US Dollar': 'USD',
          'Uruguayan Peso': 'UYU', 'Uzbekistani Som': 'UZS', 'Venezuelan Bolívar': 'VES', 'Vietnamese Dong': 'VND', 'Ni Vanuatu Vatu': 'VUV', 'Samoan Tala': 'WST',
          'Yemeni Rial': 'YER', 'South African Rand': 'ZAR', 'Zambian Kwacha': 'ZMW', 'Zimbabwean Dollar': 'ZWD','Central African CFA Franc BEAC': 'XAF', 'Silver Ounce': 'XAG', 'Gold Ounce': 'XAU', 'Bitcoin': 'XBT', 'East Caribbean Dollar': 'XCD',
          'IMF Special Drawing Rights': 'XDR', 'CFA Franc': 'XOF', 'Palladium Ounce': 'XPD', 'CFP Franc': 'XPF', 'Platinum Ounce': 'XPT'}

    def cnvrt(v,typ="normal"):
        if typ=="crypto":
            for i in data_crypto:
                if i==v:
                    return data_crypto[i]
        for i in data:
            if i==v:
                return data[i]
            
    while True:
        k=[]
        for i in data:
            if i=="Central African CFA Franc BEAC":
                break
            k.append(i)
        if vl=="c":
            kr=[]
            for i in data_crypto:
                if i=="Emirati Dirham":
                    break
                kr.append(i)
            layout=[[Text('Choose Currency',size=(20, 1),text_color="yellow", font=('Lucida',20),justification='left')],
                    [Text("Enter 1st Value ",font=("Lucida",13))]+[Input(size=(10,1))]+
                    [Combo(k,default_value='Indian Rupee',key='board')],
                    [Text("Converted to    ",font=("Lucida",13))]+[Combo(kr,default_value='Bitcoin',key='board2')]+
                    [Button(' ',image_filename="refresh_button.png", image_size=(20, 30), image_subsample=2, border_width=0)], 
                    [Button("<< Back",button_color=("black","red"),size=(10,1))]+[Text("\t\t\t\t")]+
                    [Button("Convert",button_color=("black","green2"),size=(10,1))]]
                    
        else:
            layout=[[Text('Choose Currency',size=(20, 1),text_color="yellow", font=('Lucida',20),justification='left')],
                    [Text("Enter 1st Value ",font=("Lucida",13))]+[Input(size=(10,1))]+
                    [Combo(k,default_value='Indian Rupee',key='board')],
                    [Text("    Convert to    ",font=("Lucida",13))]+[Combo(k,default_value='US Dollar',key='board2')]+
                    [Button(' ',image_filename="refresh_button.png", image_size=(20, 30), image_subsample=2, border_width=0)],
                    [Button("<< Back",button_color=("black","red"),size=(10,1))]+[Text("\t\t\t\t")]+
                    [Button("Convert",button_color=("black","green2"),size=(10,1))]]
        win =Window('Currency Converter',layout,keep_on_top=True)
        #Read  values entered by user
        while True:
            e,v=win.read()
            if e==None or e=="<< Back":
                win.close()
                currencyconverter()
            if e==" ":
                v1=v["board"]
                v2=v["board2"]
                win.find_element("board").update(value=v2)
                win.find_element("board2").update(value=v1)
            else:
                break
        from_currency=cnvrt(v["board"])
        if vl=="c":
            to_currency=cnvrt(v["board2"],"crypto")
        else:
            to_currency=cnvrt(v["board2"])
        #close first window
        def ext(tx,length):
            theme("Topanga")
            lyt=[[Text("\t")]+[Text(tx,font=("Helvetica",15))]+[Text("\t")],
                 [Button("OK",button_color="green",size=(length,1))]]
            wnd=Window("Rate",lyt,element_justification="c",keep_on_top=True)
            event,values=wnd.read()
            wnd.close()
        def ext_re(tx):
            theme("Topanga")
            lyt=[[Text("\t")]+[Text(tx,font=("Helvetica",15))]+[Text("\t")],
                 [Button("OK",button_color="red",size=(10,1))]]
            wnd=Window("Alert !!!",lyt,element_justification="c",keep_on_top=True)
            event,values=wnd.read()
            wnd.close()
            currencyconverter()
        win.close()
        rp=v[0]
        if rp.isdigit()==False:
            ext_re("\nEnter Value in Digits only !!!\n")
        internet=net_connection()
        if internet==True:
            url="https://www.xe.com/currencyconverter/convert/?Amount="+rp+"&From="+from_currency+"&To="+to_currency
            page2=requests.get(url)
            soup2=BeautifulSoup(page2.content,"html.parser")
            results2=soup2.find(class_="tab-box__MainTabContainer-sc-28io75-0 eTaaZi")
            price=results2.find_all("p",class_="result__BigRate-sc-1bsijpp-1 iGrAod")
            price=str(price)
            freeze=1
            k=0
            rate=""
            for i in price:
                if i=="<":
                    if k==1:
                        freeze=1
                        break
                if freeze==0:
                    rate+=i
                if i==">":
                    k=1
                    freeze=0
            rate+=" "+to_currency
            ext("\n"+rate+"\n",len(rate))
currencyconverter()
