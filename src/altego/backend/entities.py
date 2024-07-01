# backend/entities.py

from .core import Entity, EntityData
from dataclasses import dataclass

@dataclass
class PersonData(EntityData):
    first_name: str = ""
    last_name: str = ""

@dataclass
class PhoneNumberData(EntityData):
    number: str = ""
    country_code: str = ""

@dataclass
class EmailAddressData(EntityData):
    email: str = ""

@dataclass
class AliasData(EntityData):
    alias: str = ""

@dataclass
class OrganisationData(EntityData):
    name: str = ""
    industry: str = ""

ENTITIES = [
    Entity("Person", "An individual", PersonData(), "resources/logo.png"),
    Entity("Phone Number", "A telephone number", PhoneNumberData(), "resources/logo.png"),
    Entity("Email Address", "An email address", EmailAddressData(), "resources/logo.png"),
    Entity("Alias", "An alternative name", AliasData(), "resources/logo.png"),
    Entity("Organisation", "A company or group", OrganisationData(), "resources/logo.png"),
]