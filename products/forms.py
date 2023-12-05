from django import forms
from .models import Post ,GiftCard

class AddProduct(forms.ModelForm):
    title = forms.CharField(max_length=255)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    postimage = forms.ImageField()
    product_type = forms.ChoiceField(choices=Post.PRODUCT_TYPES)

    class Meta:
        model = Post
        fields = ['title', 'author', 'product_type', 'postimage', 'amount','youtubeurl','showcaseimage1','showcaseimage2','showcaseimage3','showcaseimage4','aboutgame','genre','releasedate','publisher','developer','language','platform']


    def save(self, commit=True, user=None):
        # Save the form data to the database
        instance = super().save(commit=False)
        if user:
            instance.author = user
        if commit:
            instance.save()

class AddGiftCard(forms.ModelForm):
    class Meta:
        model = GiftCard
        fields = ['title', 'giftcardimage', 'region', 'price', 'giftcard_type']


    def save(self, commit=True, user=None):
        # Save the form data to the database
        instance = super().save(commit=False)
        if user:
            instance.author = user
        if commit:
            instance.save()
