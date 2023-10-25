from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True)

    class Meta:
        abstract = True

class Book(BaseModel):
    title = models.CharField(max_length=255, null=False, default='')
    author = models.CharField(max_length=255, null=False, default='')
    edition = models.PositiveIntegerField(null=False, default=1)
    description = models.CharField(max_length=455, blank=True)
    quantity = models.PositiveIntegerField(
        null=False,
        default=0,
        help_text="Quantity available for allocation"
    )
    rating = models.DecimalField(
        default=0,
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    isBestseller = models.BooleanField(default=False)

    def isAvailable(self):
        return True if self.quantity > 0 else False

    def __str__(self) -> str:
        return f"{self.title} - {self.author} - {self.edition}"


class Client(BaseModel):
    name = models.CharField(max_length=255, null=False, default='')
    cpf = models.IntegerField(unique=True, null=False, default=0)
    tel = models.CharField(max_length=255, null=False, default='')
    address = models.CharField(max_length=355, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Allocation(BaseModel):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='allocations',
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='allocations',
    )
    start_time = models.DateTimeField(null=True, blank=True)
    end_time  = models.DateTimeField(null=True, blank=True)
    can_renovate = models.BooleanField(default=True, null=False)

    def __str__(self) -> str:
        return f"Allocation: {self.book.title} - {self.client.name}"