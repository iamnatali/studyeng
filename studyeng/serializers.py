from rest_framework import serializers
from .models import Category, Level, Theme, Word

class WordSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    translation = serializers.CharField(max_length=50)
    transcription = serializers.CharField(max_length=50)
    example = serializers.CharField(max_length=200)
    sound = serializers.SerializerMethodField()

    def get_sound(self, word):
        request = self.context.get('request')
        if word.sound and hasattr(word.sound, 'url'):
            sound = word.sound.url
            return request.build_absolute_uri(sound)
        else:
            return None

    class Meta:
        model = Word
        fields = ('id',
                  'name', 'translation','transcription',
                  'example', 'sound')

    def create(self, validated_data):
        return Word.objects.create(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    icon = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'icon')

    def get_icon(self, category):
        request = self.context.get('request')
        if category.icon and hasattr(category.icon, 'url'):
            icon = category.icon.url
            return request.build_absolute_uri(icon)
        else:
            return None

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class LevelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    code = serializers.CharField(max_length=2)

    class Meta:
        model = Level
        fields = ('id', 'name', 'code')

    def create(self, validated_data):
        return Level.objects.create(**validated_data)

class ShortWordSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)

    class Meta:
        model = Word
        fields = ('id', 'name')

class ShortWordField(serializers.RelatedField):
    def to_representation(self, value):
        serial = ShortWordSerializer(value)
        return serial.data

class ThemeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    photo = serializers.SerializerMethodField()
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    level = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Theme
        fields = ('id', 'name','photo',
                  'category', 'level' )

    def get_photo(self, theme):
        request = self.context.get('request')
        if theme.photo and hasattr(theme.photo, 'url'):
            photo = theme.photo.url
            return request.build_absolute_uri(photo)
        else:
            return None

    def create(self, validated_data):
        return Theme.objects.create(**validated_data)

class ThemeIDSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    photo = serializers.SerializerMethodField()
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    level = serializers.PrimaryKeyRelatedField(read_only=True)
    word_set = ShortWordField(queryset=Word.objects.all(),
                              many=True)

    class Meta:
        model = Theme
        depth = 1
        fields = ('id', 'name','photo',
                  'category', 'level', 'word_set')

    def get_photo(self, theme):
        request = self.context.get('request')
        if theme.photo and hasattr(theme.photo, 'url'):
            photo = theme.photo.url
            return request.build_absolute_uri(photo)
        else:
            return None

    def create(self, validated_data):
        return Theme.objects.create(**validated_data)





