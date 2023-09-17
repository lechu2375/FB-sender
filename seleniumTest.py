from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import os
import openai
#gpt config
openai.organization = "org-YpsxlYOd3L4eGJyQLBfPrt40"
openai.api_key = "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"





driver = webdriver.Chrome()
driver.get('https://www.facebook.com/messages/t/100003896509329')

#Sends text to the actual messenger talker
# Definicja funkcji Send_Text, która wysyła tekst na stronie za pomocą przeglądarki.
def Send_Text(text:str): 
    # Znajduje przycisk do wysyłania wiadomości na stronie.
    send_button = driver.find_element(By.CSS_SELECTOR,"div[aria-label='Wiadomość']")
    # Wprowadza tekst do pola wysyłania wiadomości.
    send_button.send_keys(text)
    # Symuluje naciśnięcie klawisza "Enter" aby wysłać wiadomość.
    send_button.send_keys(Keys.RETURN)

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

# Główna pętla programu, która działa dopóki program jest aktywny.
while program_alive:
    print("Myślę...")
    sleep(5.0)
    old_message = newest_message
    # Pobiera najnowszą wiadomość z strony.
    newest_message =  driver.find_elements(By.CSS_SELECTOR,"[style*='background-color: var(--wash)']")[-1].text
    # Jeśli najnowsza wiadomość jest taka sama jak poprzednia, kontynuuje pętlę.
    if(newest_message == old_message):
        continue

    to_send='Odpowiedz na wiadomość:'+newest_message
    # Używa modelu GPT-4 do wygenerowania odpowiedzi na wiadomość.
    response = openai.ChatCompletion.create(
              model="gpt-4",
              messages=[{"role": "system", "content": 'Jesteś wulgarnym mieszkańcem biednej dzielnicy na Śląsku '},
                        {"role": "user", "content": to_send}
              ])
    response_text = response["choices"][0]["message"]["content"]
    # Wyświetla i wysyła wygenerowaną odpowiedź
    print("\n")
    print(response_text) 
    Send_Text(response_text)
    print("\n")
    


