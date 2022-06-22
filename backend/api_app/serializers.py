from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, source='author_set')
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = [
            'title',
            'authors',
            'publication_year',
            'publisher',
        ]

    def create(self, validated_data):
        author_data = validated_data.pop('author_set')
        publisher_data = validated_data.pop('publisher')
        book = Book.objects.create(**validated_data)
        for a in author_data:
            book.author_set.add(Author.objects.create(**a))
        book.publisher = Publisher.objects.create(**publisher_data)
        return book
