from rest_framework import serializers
from django.contrib.auth import get_user_model

from . import models




User = get_user_model()

class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['image']


class AnnouncePhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = models.AnnouncementPhoto
        fields = ('id', 'image', 'announcement', 'image_url')
    
    def get_image_url(self, obj): #Изменить URL перед деплоем. Это костыль.
        if obj.image:
            return f'https://enactusanimals.com/media/{obj.image.name}'
        return None



class AnnouncementSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.id')
    photos = AnnouncePhotoSerializer(many=True, read_only=True)
    user_photo = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Announcement
        fields = '__all__'
    
    def get_user_photo(self, instance):
        image = UserImageSerializer(instance.user).data['image']
        if image:
           image = 'https://enactusanimals.com' + UserImageSerializer(instance.user).data['image']
        return image
    
    def get_user_name(self, instance):
        user_name = instance.user.first_name
        return user_name

