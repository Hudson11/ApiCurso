from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializers(serializers.ModelSerializer):

    class Meta:

        extra_kwargs = {
            'email':{
                'write_only': True
            }
        }

        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'ativo'
        )

class CursoSerializers(serializers.ModelSerializer):

    # Nested Relation
    # se caso para um curso houver avaliacoes, este relacionamento irar nos retorar os dados das avaliacoes
    #   apenas para leitura no método GET.
    #avaliacoes = AvaliacaoSerializers(many=True, read_only=True)

    # HYperLink Relation Field
    # Cria um link para visualizar avaliaçoes do curso
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # Primary Key Relation
    # retorna as chaves primárias das avaliações para os cursos
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:

        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )

