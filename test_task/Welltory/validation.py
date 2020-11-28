import json
import jsonschema
import os

filename_events=os.listdir('task_folder/event')
filename_schemas=os.listdir('task_folder/schema/')

import logging
logging.basicConfig(
    filename='readme.log', filemode='w', level=logging.INFO, format = '%(levelname)s: [%(asctime)s] %(message)s')



def searcherror(event, data, filename_event):    
    logging.debug(f'Поиск схемы для события {event}, файл {filename_event}')  
    try: 
        with open('task_folder/schema/'+event + '.schema') as f:                
            schema=json.loads(f.read())
            logging.debug(f'файл схемы для {event} существует.') 
        v=jsonschema.Draft7Validator(schema) 
        
        # Не понимаю что именно здесь имеется ввиду " Часть схем 100% правильных, часть нет.", 
        # но на всякий случай добавил проверку. 
        #----------------
        try:
            v.check_schema(schema)
        except Exception as e:
            logging.error(f'В файле "task_folder/schema/{event}.schema" ошибка! Текст ошибки: {e}')
        # ---------------
        if v.is_valid(data):
            logging.info(f'Отлично!!! Данные события {event}, из файла {filename_event} не содержат ошибок!!!')
        else:
            errors = sorted(v.iter_errors(data), key=lambda e: e.path)
            for error in errors:
                logging.warning(f'Данные {event} в файле {filename_event} содержат ошибку: {error.message}')
#                     print(error.absolute_path)
                if len(error.context)>0:
                    for suberror in sorted(error.context, key=lambda e: e.schema_path):
                        logging.warning(
                            f'Данные {event} в файле {filename_event} содержат ошибку: {suberror.schema_path}, {suberror.message}')
    except:
        logging.error(f'Для события {event} из файла {filename_event} не найдена схема!')         
        

# чтение json
for filename_event in filename_events:    
    with open('task_folder/event/'+filename_event) as f:
        js=json.loads(f.read())
    logging.info(f'Проверка файла {filename_event}')  
    try:
        data=js['data']
        event=js['event']
    except Exception as e:
        logging.error(f'В файле {filename_event} ошибка, возомжно он пустой!!! Текст ошибки: {e}')
        continue
    searcherror(event, data, filename_event)
    
    