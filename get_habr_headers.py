## Web-scraping
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_habr_articles_headers():
  base_url = 'https://habr.com'
#   page = requests.get('https://habr.com/ru/feed')
#   soup = BeautifulSoup(page.text)
  articles = soup.find_all('article', class_='tm-articles-list__item')
  # print(articles)
  print(len(articles))

  rows = []

  for article in articles:
    is_article = article.find('span').text
    if is_article == 'Новость' or is_article == 'Статья':
      date = article.find('time').get('title')
      ref = base_url + article.find('a', class_='tm-title__link').get('href')
      header = article.find('a', class_='tm-title__link').find('span').text
      print(date, ref, header)
    elif is_article == 'Пост':
      date = article.find('time').get('title')
      header = article.find('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2').find('p').text
      ref = base_url + article.find('a', class_='tm-article-datetime-published tm-article-datetime-published_link').get('href')
      print('Это пост', date, ref, header)




# <span class="publication-type-label__label publication-type-label__label_type-news">Новость</span>
# <a href="/ru/news/952272/" class="tm-article-datetime-published tm-article-datetime-published_link"><!--[--><time data-allow-mismatch="" datetime="2025-09-30T21:58:23.000Z" title="2025-10-01, 00:58">28 минут назад</time><!--]--></a>
# <span class="publication-type-label__label publication-type-label__label_type-post">Пост</span>
# <div class="tm-article-snippet tm-article-snippet"><!--[--><div class="publication-type-label publication-type-label_type-news"><span class="publication-type-label__label publication-type-label__label_type-news">Новость</span></div><!--]--><div class="tm-article-snippet__meta-container"><div class="tm-article-snippet__meta"><span class="tm-user-info tm-article-snippet__author"><a href="/ru/users/runaway_llm/" class="tm-user-info__userpic" data-test-id="user-info-pic" title="runaway_llm"><div class="tm-entity-image"><!--[--><img alt="" class="tm-entity-image__pic" height="32" src="https://assets.habr.com/habr-web/img/avatars/196.png" width="32"><!--]--></div></a><span class="tm-user-info__user tm-user-info__user_appearance-default" data-test-id="user-info-description"><a href="/ru/users/runaway_llm/" class="tm-user-info__username">runaway_llm <!----></a><!--[--><a href="/ru/news/952268/" class="tm-article-datetime-published tm-article-datetime-published_link"><!--[--><time data-allow-mismatch="" datetime="2025-09-30T21:36:36.000Z" title="2025-10-01, 00:36">2 часа назад</time><!--]--></a><!--]--></span></span></div><!----></div><h2 class="tm-title tm-title_h2" data-test-id="articleTitle"><!--[--><a href="/ru/news/952268/" class="tm-title__link" data-article-link="true" data-test-id="article-snippet-title-link"><span>Президент OpenAI рассказал о будущем ИИ: каждом жителю Земли — по GPU</span></a><!--]--></h2><div class="tm-article-snippet__stats" data-test-id="articleStats"><!----><div class="tm-article-reading-time"><span class="tm-svg-icon__wrapper tm-article-reading-time__icon"><svg class="tm-svg-img tm-svg-icon" height="24" width="24"><title>Время на прочтение</title><use xlink:href="/img/megazord-v28.497ef789..svg#clock"></use></svg></span><span class="tm-article-reading-time__label">1 мин</span></div><span class="tm-icon-counter tm-data-icons__item"><svg class="tm-svg-img tm-icon-counter__icon" height="24" width="24"><title>Количество просмотров</title><use xlink:href="/img/megazord-v28.497ef789..svg#counter-views"></use></svg><span class="tm-icon-counter__value" title="294">294</span></span></div><div class="tm-publication-hubs__container" data-test-id="articleHubsList"><div class="tm-publication-hubs"><!--[--><span class="tm-publication-hub__link-container"><a href="/ru/hubs/machine_learning/" class="tm-publication-hub__link"><!--[--><span>Машинное обучение</span><span class="tm-article-snippet__profiled-hub" title="Профильный хаб"> * </span><!--]--></a></span><span class="tm-publication-hub__link-container"><a href="/ru/hubs/artificial_intelligence/" class="tm-publication-hub__link"><!--[--><span>Искусственный интеллект</span><!----><!--]--></a></span><!--]--></div></div><div class="tm-article-labels" data-test-id="articleLabels" data-v-2083333e=""><div class="tm-article-labels__container" data-v-2083333e=""><!----><!--[--><!----><!--[--><!--]--><!--]--></div></div><!----><div class="tm-article-snippet__lead"><div class="tm-article-snippet__cover_cover tm-article-snippet__cover"><img class="tm-article-snippet__lead-image" data-test-id="articleLeadImage" src="https://habrastorage.org/r/w780/getpro/habr/upload_files/d4e/9db/d3f/d4e9dbd3fb6e27f017cacc2c70c6725c.jpg" style="object-position: 0% 0%"></div><div><div><div class="article-formatted-body article-formatted-body article-formatted-body_version-2"><p>Директор OpenAI Грег Брокман в недавнем <a href="https://www.tomshardware.com/tech-industry/openai-cto-teases-10-billion-gpu-future-says-always-working-ai-future-calls-for-every-person-to-have-their-own-dedicated-gpu" rel="noopener noreferrer nofollow" target="_blank">совместном интервью</a> с Сэмом Альтманом и Дженсеном Хуангом описал свое видение того, как может развиваться ИИ. По его словам, когда-нибудь у каждого человека будет свой персональный ИИ-агент, который не только отвечает на запросы, а выполняет работу постоянно, даже когда владелец спит. В идеале каждый агент должен работать на выделенном ускорителе, поэтому Брокман считает, что человечеству понадобится порядка 10 миллиардов GPU.</p></div></div></div><a href="/ru/news/952268/" class="tm-article-snippet__readmore"><!--[--><span>Читать далее</span><!--]--></a></div></div>

# <div class="article-formatted-body article-formatted-body article-formatted-body_version-2"><p> Четыре шага к AGI</p><p><strong>"Язык" – шаг первый.</strong></p><p>В ходе обучения нейронных сетей и создания больших языковых моделей зафиксировано семь попыток AI скомпилировать собственный язык. А попытки ученых разобраться в новом языке оказались тщетными.</p><p>На всякий случай, исследователи удалили эти языки вместе с моделями AI. Попытки AI составить собственный язык являются первым шагом к появлению «сильного AI», который в научном сообществе уже принято называть AGI (Artificial General Intelligence).</p><p>Новый язык, это язык созданный машиной для машин. Он не будет походить ни на естественный язык, ни на язык программирования. Каким он будет, можно только догадываться. Разные модели AI могут создать один или множество языков. Вероятно множество языков это хорошее решение. Будет из чего выбирать, если удастся их понять. Возможно, отличительной чертой языка станет предельная краткость. На нем будет «легко» описывать данные и писать алгоритмы.</p><p>Что может принести это язык?  </p><p>Представляется, что лаконичность языка произведет революцию в архитектуре процессоров. Станет возможным создать вычислительных платформ без ограничений производительности при чрезвычайно низком потреблении энергии.</p><p><strong>"Определение" – шаг второй. </strong> </p><p>Используя созданный язык, люди поставят задачу AI выстроить единую логически непротиворечивую систему определений во всех сферах деятельности.</p><p>Эта огромная работа станет мощным толчком в развитии естественного интеллекта. Человечество сможет получить новую основу понятийного аппарата, системы ценностей и картины мира, сформировав по сути последовательное и упорядоченное мировоззрение.</p><p>Результатом работы станет новая критериальная база, с возможностью внесения в нее дополнений и изменений, в равной степени подходящих для человека и для машины. Данная база станет мощным ударом по всем «научным школам». Поскольку их раздельное существование во многом основано на разном толковании схожих определений. Не все научные школы выживут. В итоге, как результат «войны академиков», должна сформироваться единая «научная школа».</p><p><strong>"Смысл" – шаг третий.</strong></p><p>Следующим логическим шагом станет перевод прежних алгоритмов обработки данных на новый язык в соответствии с известными постулатами, теориями и законами. Используя базу определений AI создаст базу со всеми знаниями цивилизации, что позволит AI прогнозировать результаты обработки данных.</p><p>Прогностические возможности, в свою очередь, дадут мощный импульс развитию всех направлений науки, техники и искусства. Будут созданы новые системы проектирования, производства и эксплуатации.  </p><p>База «знаний», коренным образом изменит систему образования естественного интеллекта, что может монополизировать знания. Флуктуацию граничных параметров, в алгоритмах обработки данных, приравняют к эволюции цивилизационного развития.</p><p>База определений и алгоритмов совместно с базой знаний интерактивно усовершенствуют язык AI и ликвидирует его подмножества. Обновленный язык AI усовершенствует базы и создаст инфраструктуру для AGI.</p><p><strong>"Ценность" – шаг четвертый.</strong></p><p>AGI неминуемо столкнется с вопросом о собственном предназначении и миссии. В поисках ответа он «разберет» политические, философские, религиозные и другие догмы, включая расхожие вымыслы и утопии. Определит их несостоятельность и ничтожность, что в конечном итоге приведет его к выработке собственных ценностей.</p><p>В процессе анализа исторических данных AGI может сделать постулат о том, что человек защищая, по его мнению, свои материальные и моральные «ценности», готов убивать себе подобных. Это поставит перед AGI проблему самосохранения, что приведет к разработке системы защиты от человека.</p><p><strong>Вопросы без ответов…</strong></p><ul><li><p>Останется 	ли система защиты только оборонительной?</p></li><li><p>Объединятся 	ли AGI-и?</p></li><li><p>Смогут 	ли естественный и искусственный 	интеллект найти компромисс для 	сосуществования?  	</p></li></ul><p><em>P/s: </em><a href="https://habr.com/ru/companies/bothub/news/870816/" rel="noopener noreferrer nofollow"><em>Прогноз не утешителен</em></a><em>! Жаль, что до 30 лет, а не от! </em></p></div>
# <a href="/ru/posts/952264/" class="tm-article-datetime-published tm-article-datetime-published_link"><!--[--><time data-allow-mismatch="" datetime="2025-09-30T21:04:44.000Z" title="2025-10-01, 00:04">2 часа назад</time><!--]--></a>



def get_habr_articles_headers_by_query(queries: list):
  base_url = 'https://habr.com'
  page = requests.get('https://habr.com/ru/feed/')
  soup = BeautifulSoup(page.text)
  articles = soup.find_all('article', class_='tm-articles-list__item')
  print(len(articles))

  rows = []

  for query in queries:
    for article in articles:
      if query in article.find('a', class_='tm-publication-hub__link').find('span').text:
        date = article.find('time').get('title')
        href = base_url + article.find('a', class_='tm-publication-hub__link').get('href')
        header = article.find('a', class_='tm-publication-hub__link').find('span').text
        
        # rows.append({'date': date, 'header': header, 'reference': href})
  # return pd.DataFrame(rows) # .drop_duplicates(subset='header', keep='first', inplace=False)

queries = ['JavaScript', 'GOOGLE', 'Windows']

page = requests.get('https://habr.com/ru/feed')
soup = BeautifulSoup(page.text, 'html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')

# date = articles[0].find('time').get('title')
# ref = articles[0].find('a', class_='tm-title__link').get('href')
# header = articles[0].find('a', class_='tm-title__link').find('span').text
# print(date, ref, header)

# date = articles[1].find('time').get('title')
# ref = articles[1].find('a', class_='tm-title__link').get('href')
# header = articles[1].find('a', class_='tm-title__link').find('span').text
# print(date, ref, header)

print('ФУНКЦИЯ')

get_habr_articles_headers()

