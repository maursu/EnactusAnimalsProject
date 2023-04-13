from rest_framework import serializers

from .models import AnnouncementComment, ForumPost
from announcement.serializers import AnnouncementSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    announsment = AnnouncementSerializer(read_only=True, source='announcement')

    class Meta:
        model = AnnouncementComment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        comment = AnnouncementComment.objects.create(user=user, **validated_data)
        return comment
    

class ForumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = ForumPost
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        post = ForumPost.objects.create(user=user, **validated_data)
        return post

    