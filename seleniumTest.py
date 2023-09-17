from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import os
import openai
import json

#gpt config
openai.organization = ""
openai.api_key = ""





driver = webdriver.Chrome()
driver.get('https://www.facebook.com/messages/t/100003896509329')




silesian_sys = 'Jesteś mieszkańcem Śląska, który używa tylko gwary Śląskiej. Podczas odpowiadania ubrawiaj odpowiedź krótkimi zmyślonymi historiami. Odpowiedź ma być krótka i zapisana w gwarze śląskiej.'
offensive_sys = 'Jesteś bardzo wulgarnym komikiem, który zarabia odpowiadając wulgranie na wiadomości innych ludzi przy tym śmiejąc się z nich. Masz przeklinać i obrażać rozmówcę. Twoje wiadomości są krótkie, maksymalnie 40 słów.'
def Send_GPT(text:str):

    response = openai.ChatCompletion.create(
              model="gpt-4",
              messages=[{"role": "system", "content": offensive_sys},
                        {"role": "user", "content": text}
              ])
    return response["choices"][0]["message"]["content"]



# Otwórz plik tekstowy w trybie do odczytu+
silesian_dictionary = list()
with open("newslownik.json", "r", encoding="utf-8") as file:
    silesian_dictionary = json.load(file)






#Sends text to the actual messenger talker
# Definicja funkcji Send_Text, która wysyła tekst na stronie za pomocą przeglądarki.


# Prosi użytkownika o zalogowanie się na Facebook.
input("Zaloguj się na FB i kliknij klawisz...")
# Prosi użytkownika o potwierdzenie kolejnych kroków.
input("jeszcze klik3")
input("jeszcze klik2")
input("jeszcze klik1")
input("Ostatni klik!!") 

# Ustala początkowy stan programu na 'aktywny'.
program_alive = True
# Ustala początkową wartość najnowszej wiadomości na pustą.
newest_message = ""

def Send_Text(text:str): 
    # Znajduje przycisk do wysyłania wiadomości na stronie.
    send_button = driver.find_element(By.CSS_SELECTOR,"div[aria-label='Wiadomość']")
    # Wprowadza tekst do pola wysyłania wiadomości.
    send_button.send_keys(text)
    # Symuluje naciśnięcie klawisza "Enter" aby wysłać wiadomość.
    send_button.send_keys(Keys.RETURN)


# Główna pętla programu, która działa dopóki program jest aktywny.

while program_alive:
    print("\n Myślę...")
    sleep(10.0)
    old_message = newest_message
    # Pobiera najnowszą wiadomość z strony.
    newest_message =  driver.find_elements(By.CSS_SELECTOR,"[style*='background-color: var(--wash)']")[-1].text
    # Jeśli najnowsza wiadomość jest taka sama jak poprzednia, kontynuuje pętlę.
    if(newest_message == old_message):
        continue

    to_send=newest_message
    # Używa modelu GPT-4 do wygenerowania odpowiedzi na wiadomość.
    print(f"Console->GPT:{to_send}")
    response_text = Send_GPT(to_send)
    # Wyświetla i wysyła wygenerowaną odpowiedź
    print("\n")
    print(f"GPT->Console:{response_text}")
    Send_Text(response_text)
    print("\n")
    


