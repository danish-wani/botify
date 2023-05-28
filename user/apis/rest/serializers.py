from rest_framework import serializers

from user.models import BotifyUser


class BotifyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = BotifyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        """
            Creates the Botify User, and uses `set_password` to set the password of the user.
        :param validated_data: Dictionary containing the validated data
        :return: New created BotifyUser instance
        """
        password = validated_data.pop('password')
        user = BotifyUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
            Updates the Botify User instance with the new values provided and uses `set_password` to set the password.
        :param instance: BotifyUser instance which is being updated
        :param validated_data: Dictionary containing the validated data
        :return: Updated BotifyUser instance
        """
        password = validated_data.pop('password')
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.set_password(password)
        instance.save()
        return instance

