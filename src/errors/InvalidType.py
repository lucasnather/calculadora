class InvalidType(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'Bad Request'
        self.statusCode = 404