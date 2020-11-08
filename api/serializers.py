#serializers.py
#모델로 만든 데이터를 json 형태로 바꿈
from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length= 10)
    phone_number = serializers.CharField(max_length=13)
    address = serializers.ModelSerializer

    class Meta:
        model = Member
        fields = ('name','phone_number','address')
        read_only_fields = ['created']


    #RestfulAPI는 HTML로 렌더링 된 Django Template를 사용할수없음
    # 해당 필드를 json으로 바꿔 출력
