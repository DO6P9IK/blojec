from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        required=True,
        label="Имя",
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "Ваше Имя"}
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "E-Mail"}
        ),
    )
    to = forms.EmailField(
        required=True,
        label="Кому",
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "Кому отправить"}
        ),
    )
    comments = forms.CharField(
        required=False,
        label="Комментарий",
        widget=forms.Textarea(
            attrs={"class": "form-control mb-1", "placeholder": "Ваш комментарий"}
        ),
    )


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label="Имя",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ваше Имя"}
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )
    body = forms.CharField(
        required=True,
        label="Текст",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Ваш комментарий"}
        ),
    )

    class Meta:
        model = Comment
        fields = ["name", "email", "body"]


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "Введите форазу для поиска...",
            }
        )
    )
