from django import forms

class QuestionForm(forms.Form):
    name = forms.CharField(label='名前', max_length=10)
    title = forms.CharField(label='タイトル', max_length=50)
    content = forms.CharField(label='内容', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"})
        self.fields['title'].widget.attrs.update({'class': "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"})
        self.fields['content'].widget.attrs.update({'class': "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"})

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.strip() == '':
            raise forms.ValidationError('タイトルを入力してください')
        return name
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip() == '':
            raise forms.ValidationError('タイトルを入力してください')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if content.strip() == '':
            raise forms.ValidationError('質問を入力してください')
        return content
        


class ReplyForm(forms.Form):
    name = forms.CharField(label='名前', max_length=10)
    content = forms.CharField(label='内容', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"})
        self.fields['content'].widget.attrs.update({'class': "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"})

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.strip() == '':
            raise forms.ValidationError('タイトルを入力してください')
        return name

    def clean_content(self):
        content = self.cleaned_data['content']
        if content.strip() == '':
            raise forms.ValidationError('質問を入力してください')
        return content