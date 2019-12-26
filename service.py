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
            for OBJETO in result_json['entities']:
                D= {}
                
                D['Símbolos'] = OBJETO['symbols']
                D['Usuário_mencionado'] = OBJETO['user_mentions']
                entidades.append(D)
            B['Entidades'] = entidades


        return B


                


               

            

        





       

       



   



