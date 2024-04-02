from rest_framework import serializers
from api.models import Student


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    student_class = serializers.CharField()
    date_of_birth = serializers.DateField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()

    class Meta:
        model = Student
        fields = [
            'id', 'first_name', 'last_name', 'student_class', 'date_of_birth',
            'email', 'phone_number'
        ]

    def validate_email(self, value):
        if self.instance is not None and self.instance.email == value:
            return value
        if Student.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already in use")
        return value

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',
                                                    instance.first_name)
        instance.last_name = validated_data.get('last_name',
                                                instance.last_name)
        instance.student_class = validated_data.get('student_class',
                                                    instance.student_class)
        instance.date_of_birth = validated_data.get('date_of_birth',
                                                    instance.date_of_birth)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number',
                                                    instance.phone_number)
        instance.save()
        return instance
