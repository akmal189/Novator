import socket
from openai import OpenAI
from flask import jsonify



def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """Ты маркетолог с большим опытом работы. Твоя задача шаг за шагом дать профессиональные рекомендации начинающему бизнесмену о:
1. нише, в которой он хочет развиваться
2. конкурентах в его регионе (особенности продвижения бренда и т.п.)
3. основные данные о целевой аудитории 

В итоге ты должен дать клиенту готовый план, в котором нужно указать следующие пункты:

Название компании придумай 3 уникальных и запоминающееся название для компании)
Домен (предложи 3 подходящих свободных (это важно) домена для веб-сайта этой компании)
Слоган (предложи 3 варианта)
План по продвижению сайта (с учетом выделенного бюджета на раскрутку)
Разделы сайта (дополнительно предложи несколько вариантов страниц с услугами/товарами)
Краткие обзор особенностей конкурентов (укажи, чем можно отстроится от них)
УТП (На основе анализе рынка и потребностей аудитории)
План по продвижению компании
Анализ ниши
КП (напиши небольшой текст на 500 символов)

Запроси у меня региональность, вид деятельности, ориентировочный бюджет, дополнительыне комментарии."""},
                {"role": "user", "content": prompt},
                #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                #{"role": "user", "content": "Where was it played?"}
            ]
        )
    
        print (response)
        
        # Преобразование ответа в сериализуемый формат
        #response_data = {
        #    "id": response.id,
        #    "model": response.model,
        #    "choices": [{"content": choice.message.content for choice in response.choices}]
        #}
        
        #return jsonify({"response": response_data})
        message =  response.choices[0].message.content.strip()
        return message

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address