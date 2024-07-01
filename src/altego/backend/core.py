from dataclasses import dataclass

@dataclass
class EntityData:
    """
    Base class for entity-related data. This class can be extended to include
    any specific data attributes related to an entity.

    Attributes
    ----------
    Any attributes specific to the entity can be added to subclasses.
    """
    pass

class Entity:
    """
    A class to represent an entity with a name, description, associated data, and an optional icon path.

    Attributes
    ----------
    name : str
        The name of the entity, limited to 38 characters.
    description : str
        A brief description of the entity, limited to 255 characters.
    data : EntityData
        Custom data associated with the entity.
    icon_path : str, optional
        The file path to the entity's icon (default is None).

    Methods
    -------
    __init__(self, name: str, description: str, entity_data: EntityData, icon_path: str = None)
        Constructs all the necessary attributes for the entity object.
    name(self) -> str
        Gets the name of the entity.
    name(self, value: str)
        Sets the name of the entity with a length check.
    description(self) -> str
        Gets the description of the entity.
    description(self, value: str)
        Sets the description of the entity with a length check.
    icon_path(self) -> str
        Gets the icon path of the entity.
    icon_path(self, value: str)
        Sets the icon path of the entity.
    data(self) -> EntityData
        Gets the custom data associated with the entity.
    data(self, value: EntityData)
        Sets the custom data associated with the entity.
    __repr__(self)
        Returns a string representation of the entity object.
    """

    def __init__(self, name: str, description: str, entity_data: EntityData, icon_path: str = None):
        """
        Constructs all the necessary attributes for the entity object.

        Parameters
        ----------
        name : str
            The name of the entity, limited to 38 characters.
        description : str
            A brief description of the entity, limited to 255 characters.
        entity_data : EntityData
            Custom data associated with the entity.
        icon_path : str, optional
            The file path to the entity's icon (default is None).
        """
        self.name = name
        self.description = description
        self.data = entity_data
        self.icon_path = icon_path

    @property
    def name(self) -> str:
        """
        Gets the name of the entity.

        Returns
        -------
        str
            The name of the entity.
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """
        Sets the name of the entity.

        Parameters
        ----------
        value : str
            The name of the entity, limited to 38 characters.

        Raises
        ------
        ValueError
            If the name is longer than 38 characters.
        """
        if len(value) > 38:
            raise ValueError("Name cannot be longer than 38 characters.")
        self._name = value

    @property
    def description(self) -> str:
        """
        Gets the description of the entity.

        Returns
        -------
        str
            The description of the entity.
        """
        return self._description

    @description.setter
    def description(self, value: str):
        """
        Sets the description of the entity.

        Parameters
        ----------
        value : str
            The description of the entity, limited to 255 characters.

        Raises
        ------
        ValueError
            If the description is longer than 255 characters.
        """
        if len(value) > 255:
            raise ValueError("Description cannot be longer than 255 characters.")
        self._description = value

    @property
    def icon_path(self) -> str:
        """
        Gets the icon path of the entity.

        Returns
        -------
        str
            The file path to the entity's icon.
        """
        return self._icon_path

    @icon_path.setter
    def icon_path(self, value: str):
        """
        Sets the icon path of the entity.

        Parameters
        ----------
        value : str
            The file path to the entity's icon.
        """
        self._icon_path = value

    @property
    def data(self) -> EntityData:
        """
        Gets the custom data associated with the entity.

        Returns
        -------
        EntityData
            The custom data associated with the entity.
        """
        return self._entity_data

    @data.setter
    def data(self, value: EntityData):
        """
        Sets the custom data associated with the entity.

        Parameters
        ----------
        value : EntityData
            The custom data associated with the entity.
        """
        self._entity_data = value

    def __repr__(self):
        """
        Returns a string representation of the entity object.

        Returns
        -------
        str
            A string representation of the entity.
        """
        return f"Entity(name={self.name}, description={self.description}, icon_path={self.icon_path}, data={self.data})"
