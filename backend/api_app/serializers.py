from rest_framework import serializers

from .models import Book, Author, Publisher, Album, Artist, Film, FilmDirector


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name"]


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["name"]


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, source="author_set", required=False)
    publisher = PublisherSerializer(required=False, allow_null=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "authors",
            "publication_year",
            "publisher",
        ]

    def create(self, validated_data):
        """
        Overwriting create function to manage nested data (authors and publisher)
        """
        authors = validated_data.pop("author_set", None)
        publisher = validated_data.pop("publisher", None)
        if publisher:
            publisher = Publisher.objects.get_or_create(**publisher)
            validated_data["publisher"] = publisher[0]
        book = Book.objects.create(**validated_data)
        if authors:
            for author in authors:
                book.author_set.add(Author.objects.get_or_create(**author)[0])
        return book

    def update(self, instance, validated_data):
        """
        Overwriting update function to manage nested data (authors and publisher)
        """
        instance.title = validated_data.get("title", instance.title)
        instance.publication_year = validated_data.get(
            "publication_year", instance.publication_year
        )
        authors = validated_data.get("author_set", None)
        publisher = validated_data.get("publisher", None)
        if authors:
            for author in authors:
                instance.author_set.add(Author.objects.get_or_create(**author)[0])
        else:
            instance.author_set.clear()
        if publisher:
            instance.publisher = Publisher.objects.get_or_create(**publisher)[0]
        instance.save()
        return instance


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["name"]


class AlbumSerializer(serializers.ModelSerializer):
    performer = ArtistSerializer()
    composer = ArtistSerializer()

    class Meta:
        model = Album
        fields = [
            "id",
            "title",
            "performer",
            "composer",
            "release_year",
            "genre",
            "format",
        ]

    def create(self, validated_data):
        """
        Overwriting create function to manage nested data (performer and composer)
        """
        performer = validated_data.pop("performer", None)
        composer = validated_data.pop("composer", None)
        if performer:
            performer = Artist.objects.get_or_create(**performer)
            validated_data["performer"] = performer[0]
        if performer:
            composer = Artist.objects.get_or_create(**composer)
            validated_data["composer"] = composer[0]
        album = Album.objects.create(**validated_data)
        return album

    def update(self, instance, validated_data):
        """
        Overwriting update function to manage nested data (performer and composer)
        """
        instance.title = validated_data.get("title", instance.title)
        instance.release_year = validated_data.get(
            "release_year", instance.release_year
        )
        instance.genre = validated_data.get("genre", instance.genre)
        instance.format = validated_data.get("format", instance.format)
        performer = validated_data.get("performer", None)
        composer = validated_data.get("composer", None)
        if performer:
            instance.performer = Artist.objects.get_or_create(**performer)[0]
        if composer:
            instance.composer = Artist.objects.get_or_create(**composer)[0]
        instance.save()
        return instance


class FilmDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmDirector
        fields = ["first_name", "last_name"]


class FilmSerializer(serializers.ModelSerializer):
    film_directors = FilmDirectorSerializer(
        many=True, source="filmdirector_set", required=False
    )

    class Meta:
        model = Film
        fields = [
            "id",
            "title",
            "film_directors",
            "release_year",
            "description",
        ]

    def create(self, validated_data):
        """
        Overwriting create function to manage nested data (authors and publisher)
        """
        film_directors = validated_data.pop("filmdirector_set", None)
        film = Film.objects.create(**validated_data)
        if film_directors:
            for film_director in film_directors:
                film.filmdirector_set.add(
                    FilmDirector.objects.get_or_create(**film_director)[0]
                )
        return film

    def update(self, instance, validated_data):
        """
        Overwriting update function to manage nested data (authors and publisher)
        """
        instance.title = validated_data.get("title", instance.title)
        instance.release_year = validated_data.get(
            "release_year", instance.release_year
        )
        instance.description = validated_data.get("description")
        film_directors = validated_data.get("filmdirector_set", None)
        if film_directors:
            for film_director in film_directors:
                instance.filmdirector_set.add(
                    FilmDirector.objects.get_or_create(**film_director)[0]
                )
        else:
            instance.filmdirector_set.clear()
        instance.save()
        return instance
