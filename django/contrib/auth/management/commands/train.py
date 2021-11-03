from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Train the chatbot with CorpusTrainer'

    def handle(self, *args, **options):

        chatbot = ChatBot(
            "Health Care Bot",
            trainer = 'chatterbot.trainers.ChatterBotCorpusTrainer',
            storage_adapter='chatterbot.storage.DjangoStorageAdapter',
        )

        trainer = ChatterBotCorpusTrainer(chatbot)

        trainer.train(
            'chatterbot.corpus.my_corpus'
        )

        self.stdout.write(self.style.SUCCESS('Successfully trained!'))