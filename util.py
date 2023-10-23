import os
from dotenv import load_dotenv
from splitwise import Splitwise


class Util:
    def __init__(self):
        self.my_id = None
        self.client = None

    def get_my_id(self):
        if self.my_id is None:
            client = self.get_splitwise_client()
            self.my_id = client.getCurrentUser().getId()
        return self.my_id

    def get_my_spending(self, user_expenses):
        for user_expense in user_expenses:
            if user_expense.getId() == self.get_my_id():
                return float(user_expense.getOwedShare())
        return 0

    def get_splitwise_client(self):
        if self.client is None:
            load_dotenv()
            self.client = Splitwise(consumer_key=os.getenv("CONSUMER_KEY"),
                                    consumer_secret=os.getenv("CONSUMER_SECRET"),
                                    api_key=os.getenv("API_KEY"))
        return self.client
