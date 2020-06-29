from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Daniel',
         'habilidades':['Python', 'Django']
    },

    {
        'id':'1',
        'nome':'Thor',
        'habilidades':['Python', 'Django']
    }
]

#devolve um desenvolverdor pelo ID pelo método GET, também altera (PUT) e deleta (DELETE) um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Erro', 'mensagem': 'Desenvolvedor de ID {} não existe'.format(id)}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return response
#não precisa mais do jsonify. O restful já converte automaticamente

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}

#lista todos os desenvolvedores e permite incluir/registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')              #(classe, caminho)

if __name__ == '__main__':
    app.run(debug=True)