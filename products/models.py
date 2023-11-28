from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField 

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)






class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    postimage = models.ImageField(upload_to='files/', default='/logo.png', null=True, blank=False)
    PRODUCT_TYPES = [
        ('top_sellers', 'Top Sellers'),
        ('new_releases', 'New Releases'),
        ('old_releases' ,'Old Releases'),
        ('top', 'Top'),
        ('Event', 'Event'),
        ('gadget','Gadget'),
    ]
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
