from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator

from abc import ABC, abstractmethod

############################################
# Enumerations are defined here
############################################

############################################
# Classes are defined here
############################################
class FirstClassCreate(ABC, BaseModel):
    counter: int
    id: int  # the id


