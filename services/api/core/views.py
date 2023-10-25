from rest_framework import viewsets, mixins, status
from core.models import Book, Client, Allocation
from core.serializers import BookSerializer, ClientSerializer, AllocationSerializer
from datetime import datetime
from rest_framework.response import Response
from core.services import verify_active_allocations
import json


class BookViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Book.objects.filter(deleted_at__isnull=True).order_by("-title")
    serializer_class = BookSerializer

    def destroy(self, request, pk):
        """
        Apply soft delete to book and related allocations
        """
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response(
                { "message": "Book does not exist!" },
                status=status.HTTP_404_NOT_FOUND,
            )

        has_allocations = verify_active_allocations(instance=book)

        if not has_allocations:
            book.deleted_at = datetime.now()
            book.save()

            return Response(
                { "message": "Book deleted with success!" },
                status=status.HTTP_204_NO_CONTENT,
            )

        return Response(
            { "message": "Book not deleted!" },
            status=status.HTTP_400_BAD_REQUEST,
        )

class ClientViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Client.objects.filter(deleted_at__isnull=True)
    serializer_class = ClientSerializer

    def destroy(self, request, pk):
        """
        Apply soft delete to client and related allocations
        """
        try:
            client = Client.objects.get(id=pk)
        except Client.DoesNotExist:
            return Response(
                { "message": "Book does not exist!" },
                status=status.HTTP_404_NOT_FOUND,
            )

        has_allocations = verify_active_allocations(instance=client)

        if not has_allocations:
            client.deleted_at = datetime.now()
            client.save()

            return Response(
                { "message": "Client deleted with success!" },
                status=status.HTTP_204_NO_CONTENT,
            )

        return Response(
            { "message": "Client not deleted!" },
            status=status.HTTP_400_BAD_REQUEST,
        )


class AllocationViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Allocation.objects.filter(deleted_at__isnull=True)
    serializer_class = AllocationSerializer

    def destroy(self, request, pk):
        """
        Apply soft delete to allocation
        """
        Allocation.objects.filter(id=pk).update(deleted_at=datetime.now())

        return Response(
            { "message": "Allocation deleted with success!" },
            status=status.HTTP_204_NO_CONTENT,
        )