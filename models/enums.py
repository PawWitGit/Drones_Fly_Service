import enum


class RoleType(enum.Enum):
    admin = "admin"
    user = "user"
    verify_person = "verify_person"


class State(enum.Enum):
    created = "created"
    edited = "edited"
    deleted = "deleted"
    verified = "verified"
