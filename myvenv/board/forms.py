from django import forms
from board.models import Post, Answer


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['subject', 'content', 'image']  # PostForm에서 사용할 Post 모델의 속성
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
            'image': '이미지',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }