from django.core.management import BaseCommand
from strategies.macd import MacdStrategy
from datetime import date


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('signal', nargs='+', type=str)

    def handle(self, *args, **options):
        signal = options['signal'][0]
        # trigger_date = date(2017, 7, i)
        # MacdStrategy(trigger_date=trigger_date).get_signals(signal_type=signal)
        MacdStrategy().get_signals(signal_type=signal)
