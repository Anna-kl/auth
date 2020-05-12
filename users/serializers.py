from rest_framework import  serializers
from .models import  User

class UserSerializer(serializers.ModelSerializer):
    data_joined=serializers.ReadOnlyField()

    class Meta(object):
        model=User
        fields=('id', 'email','first_name','last_name','date_joined','password')
        extra_kwards={'password':{'write_only': True}}