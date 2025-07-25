from rest_framework import serializers

from watchlist_app.models import Movie


def name_lenght(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name too Short")
    else:
        return value


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_lenght])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, value):
        if value['name'] == value['description']:
            raise serializers.ValidationError("Name and Description should not be the same")
        else:
            return value

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name too short")
    #     return value

