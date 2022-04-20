from typing import Dict, Any


class BaseDAO:

    def get_all(self):
        raise NotImplementedError

    def get_one(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def create(self):
        raise NotImplementedError

    def delete  (self):
        raise NotImplementedError

