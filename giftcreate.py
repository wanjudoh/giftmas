import os
import sys
import urllib.request
os.environ.setdefault("DJANGO_SETTINGS_MODULE","letterProject.settings")
import django
django.setup()
from letter.models import Gift
import pandas as pd

if __name__ == '__main__':
    f = pd.read_excel('gift.xlsx')

    for l in range(len(f)):
        num = f.loc[l, 'id']
        title = f.loc[l, 'title']
        image = f.loc[l, 'img']
        
        Gift.objects.create(
            id = num,
            title = title,
            img = image
        )
        print(title)
        
print('저장완료')