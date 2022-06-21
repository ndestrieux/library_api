from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    publisher = serializers.CharField(source='publisher.name')
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'publication_year',
            'publisher',
        ]