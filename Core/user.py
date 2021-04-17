class User:
    def __init__(self, user_name:str, user_id:str=None, friendly_name:str=None, connector_user_object=None):
        self.user_name = user_name
        self.user_id = user_id
        self.friendly_name = friendly_name
        self.connector_user_object = connector_user_object