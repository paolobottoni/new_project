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


###############
#  GUI MODEL  #
###############

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: GUI_Module

# Screen: wrapper
wrapper = Screen(name="wrapper", description="Home", view_elements=set(), is_main_page=True, route_path="/home", screen_size="Medium")
wrapper.view_elements = set()

gui_module = Module(
    name="GUI_Module",
    screens={wrapper}
)

# GUI Model
gui_model = GUIModel(
    name="GUI",
    package="",
    versionCode="1.0",
    versionName="1.0",
    modules={gui_module},
    description="GUI"
)
