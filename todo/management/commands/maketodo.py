from django.core.management import BaseCommand
from todo.models import Todo
from random import choice
import sys


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("make todo start :)")

        for i in range(1, 101):
            # todo = Todo.objects.create(
            #     name=f"테스트 todo {i}")  # f String

            # get_or_create는 created라는 boolean 값이 함께 넘어온다.
            todo, created = Todo.objects.get_or_create(name=f"테스트 todo {i}")
            if created:
                print(f"{i}번째 todo 생성 완료")
            else:
                print(f"{i}번째 todo 이미 존재")

        sys.stdout.write(self.style.SUCCESS("make todo end :)"))
