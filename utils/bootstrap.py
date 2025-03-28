from django import forms

class BootStrapForm:
    exclude_field_list = []

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        #{'title':对象,'percent’:对象}
        for name,field in self.fields.items():
            if name in self.exclude_field_list:
                continue
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入{}'.format(field.label)


from django import forms


class BootStrap:
    exclude_field_list = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段，给每个字段的插件设置
        for name, field in self.fields.items():
            if name in self.exclude_field_list:
                continue
            # 字段中有属性，保留原来的属性，没有属性，才增加。
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


# class BootStrapForm(BootStrap, forms.Form):
#     pass
