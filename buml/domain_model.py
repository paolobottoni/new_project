####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Classes
FirstClass = Class(name="FirstClass", is_abstract=True)

# FirstClass class attributes and methods
FirstClass_counter: Property = Property(name="counter", type=IntegerType, visibility="private")
FirstClass_id: Property = Property(name="id", type=IntegerType, visibility="private", is_id=True)
FirstClass_m_getCounter: Method = Method(name="getCounter", parameters={}, type=IntegerType, implementation_type=MethodImplementationType.NONE)
FirstClass_m_increment: Method = Method(name="increment", parameters={}, implementation_type=MethodImplementationType.CODE)
FirstClass_m_increment.code = """def increment(self):
    \"\"\"Add your docstring here.\"\"\"
    # Add your implementation here
    self.counter++
"""
FirstClass_m_run: Method = Method(name="run", parameters={}, implementation_type=MethodImplementationType.STATE_MACHINE)
try:
    FirstClass_m_run.state_machine = sm
except NameError:
    pass
FirstClass.attributes={FirstClass_counter, FirstClass_id}
FirstClass.methods={FirstClass_m_getCounter, FirstClass_m_increment, FirstClass_m_run}

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={FirstClass},
    associations={},
    generalizations={},
    metadata=None
)
