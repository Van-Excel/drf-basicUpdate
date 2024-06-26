from rest_framework import serializers
from snippets.models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippets
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    def create(self, validated_data):

        return Snippets.objects.create(**validated_data)
        

    def update( self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance