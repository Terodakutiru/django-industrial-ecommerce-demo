class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField(default=0)


class Order(models.Model):
    customer_email = models.EmailField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(default=1)
