from rest_framework import serializers

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
    authors = AuthorSerializer(many=True, source='author_set', required=False)
    publisher = PublisherSerializer(required=False)

    class Meta:
        model = Book
        fields = [
            'title',
            'authors',
            'publication_year',
            'publisher',
        ]

    def create(self, validated_data):
        """
        Overwriting create function to manage nested data (authors and publisher)
        """
        book = Book.objects.create(**validated_data)
        if 'author_set' in validated_data.keys():
            author_data = validated_data.pop('author_set')
            for a in author_data:
                book.author_set.add(Author.objects.create(**a))
        if 'publisher' in validated_data.keys():
            publisher_data = validated_data.pop('publisher')
            book.publisher = Publisher.objects.create(**publisher_data)
        return book
