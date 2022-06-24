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
        authors = validated_data.pop('author_set', None)
        publisher = validated_data.pop('publisher', None)
        if publisher:
            publisher = Publisher.objects.get_or_create(**publisher)
            validated_data['publisher'] = publisher[0]
        book = Book.objects.create(**validated_data)
        if authors:
            for author in authors:
                book.author_set.add(Author.objects.get_or_create(**author)[0])
        return book

    def update(self, instance, validated_data):
        """
        Overwriting update function to manage nested data (authors and publisher)
        """
        instance.title = validated_data.get('title', instance.title)
        print(instance.title)
        instance.publication_year = validated_data.get('publication_year', instance.publication_year)
        print(instance.publication_year)
        authors = validated_data.get('author_set', instance.author_set)
        publisher = validated_data.get('publisher', instance.publisher)
        for author in authors:
            instance.author_set.add(Author.objects.get_or_create(**author)[0])
        instance.publisher = Publisher.objects.get_or_create(**publisher)[0]
        instance.save()
        return instance
