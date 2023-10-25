from rest_framework import serializers
from core.models import Book, Client, Allocation


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "edition",
            "description",
            "quantity",
            "rating",
            "isBestseller",
            "deleted_at"
        )

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "name",
            "cpf",
            "tel",
            "address",
            "deleted_at"
        )

class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = (
            "id",
            "start_time",
            "end_time",
            "can_renovate",
            "book",
            "client",
            "deleted_at"
        )