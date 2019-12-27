import json
import requests 

import re
from requests_oauthlib import OAuth1

class Tweets:
    def filtro(nome):
        nome = str(nome.replace(" ", "-"))  
        
        URL = 'https://api.twitter.com/1.1/search/tweets.json'
        parametros ={'q':nome}

        auth = OAuth1('VrC9fO2JZ6MSQXoazJz1yq7ws', 'cYzFS8VAWcGRnGebpwbMAUB19q3RTYigkEu9eU1ta7Udfuj8CU',
     '794212942866710528-lgKDDz5Tlxipm8Quf1At8n2wgFyXV7l', 'X2i0Lo5Po1r7EnnybWIaFzDbG3yjvoqn4hvi2QmaSa5TU')

        resposta = requests.get(URL, auth=auth, params=parametros)  
        lista_tweets = resposta.text
        json_retorno = json.loads(lista_tweets)
        result_json = json_retorno['statuses'][0]

        
        B={}
        if 'created_at' in result_json and result_json['created_at']:
            B['data_do_tweet'] = result_json['created_at']  
        
        if 'text' in result_json and result_json['text']:   
            B['texto'] = result_json['text']     
    
        
        
       
       
        if 'entities' in result_json and result_json['entities']:
            entidades=[]
            for OBJETO in result_json['entities']['user_mentions']:
                D= {}   
                
                
                D['nickname_mencionado'] = OBJETO['screen_name']
                D['nome_mencionado'] = OBJETO['name']
                D['identificador_mencionado'] = OBJETO ['id']
                
                entidades.append(D)
            B['Usuários_mencionados'] = entidades
        
        if 'metadata' in result_json and result_json['metadata']:
            B['língua_do_tweet'] = result_json['metadata']['iso_language_code'] 

        if 'user' in result_json and result_json['user']:
            B['nome_do_usuário'] = result_json['user']['name']
            B['id_do_usuário'] = result_json['user']['id']
            B['nickname_do_usuário'] = result_json['user']['screen_name']
            B['localização_do_usuario'] = result_json['user']['location']
            B['total_de_seguidores'] = result_json['user']['followers_count']

        


        
           



        return B


                


               

            

        





       

       



   



