# ./picdef.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e879668f01fce2c06e252084699d6bc0827cd581
# Generated 2017-09-27 17:50:38.342662 by PyXB version 1.2.6 using Python 3.5.2.final.0
# Namespace sptdf

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9b8f1d94-a39b-11e7-8d5f-f8b156a007f6')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('sptdf', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {sptdf}attributeTypes
class attributeTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'attributeTypes')
    _XSDLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 55, 2)
    _Documentation = None
attributeTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=attributeTypes)
attributeTypes.integer = attributeTypes._CF_enumeration.addEnumeration(unicode_value='integer', tag='integer')
attributeTypes.float = attributeTypes._CF_enumeration.addEnumeration(unicode_value='float', tag='float')
attributeTypes.boolean = attributeTypes._CF_enumeration.addEnumeration(unicode_value='boolean', tag='boolean')
attributeTypes.string = attributeTypes._CF_enumeration.addEnumeration(unicode_value='string', tag='string')
attributeTypes._InitializeFacetMap(attributeTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'attributeTypes', attributeTypes)
_module_typeBindings.attributeTypes = attributeTypes

# Complex type {sptdf}scenePic with content type ELEMENT_ONLY
class scenePic (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {sptdf}scenePic with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scenePic')
    _XSDLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 14, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {sptdf}object uses Python identifier object
    __object = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'object'), 'object', '__sptdf_scenePic_sptdfobject', True, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 16, 2), )

    
    object = property(__object.value, __object.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__sptdf_scenePic_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 18, 2)
    __id._UseLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 18, 2)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __object.name() : __object
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.scenePic = scenePic
Namespace.addCategoryObject('typeBinding', 'scenePic', scenePic)


# Complex type {sptdf}objectPic with content type ELEMENT_ONLY
class objectPic (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {sptdf}objectPic with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'objectPic')
    _XSDLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 21, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {sptdf}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__sptdf_objectPic_sptdfattributes', False, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 23, 4), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {sptdf}object uses Python identifier object
    __object = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'object'), 'object', '__sptdf_objectPic_sptdfobject', True, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 24, 4), )

    
    object = property(__object.value, __object.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__sptdf_objectPic_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 26, 3)
    __id._UseLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 26, 3)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute num uses Python identifier num
    __num = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'num'), 'num', '__sptdf_objectPic_num', pyxb.binding.datatypes.string, required=True)
    __num._DeclarationLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 27, 3)
    __num._UseLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 27, 3)
    
    num = property(__num.value, __num.set, None, None)

    
    # Attribute visible uses Python identifier visible
    __visible = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'visible'), 'visible', '__sptdf_objectPic_visible', pyxb.binding.datatypes.boolean, required=True)
    __visible._DeclarationLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 28, 3)
    __visible._UseLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 28, 3)
    
    visible = property(__visible.value, __visible.set, None, None)

    
    # Attribute group uses Python identifier group
    __group = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'group'), 'group', '__sptdf_objectPic_group', pyxb.binding.datatypes.boolean, required=True)
    __group._DeclarationLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 29, 3)
    __group._UseLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 29, 3)
    
    group = property(__group.value, __group.set, None, None)

    
    # Attribute differs uses Python identifier differs
    __differs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'differs'), 'differs', '__sptdf_objectPic_differs', pyxb.binding.datatypes.boolean, required=True)
    __differs._DeclarationLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 30, 3)
    __differs._UseLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 30, 3)
    
    differs = property(__differs.value, __differs.set, None, None)

    _ElementMap.update({
        __attributes.name() : __attributes,
        __object.name() : __object
    })
    _AttributeMap.update({
        __id.name() : __id,
        __num.name() : __num,
        __visible.name() : __visible,
        __group.name() : __group,
        __differs.name() : __differs
    })
_module_typeBindings.objectPic = objectPic
Namespace.addCategoryObject('typeBinding', 'objectPic', objectPic)


# Complex type {sptdf}attributes with content type ELEMENT_ONLY
class attributes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {sptdf}attributes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'attributes')
    _XSDLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {sptdf}color uses Python identifier color
    __color = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'color'), 'color', '__sptdf_attributes_sptdfcolor', True, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 35, 4), )

    
    color = property(__color.value, __color.set, None, None)

    
    # Element {sptdf}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__sptdf_attributes_sptdfname', True, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 36, 4), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {sptdf}property_of uses Python identifier property_of
    __property_of = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'property_of'), 'property_of', '__sptdf_attributes_sptdfproperty_of', False, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 37, 4), )

    
    property_of = property(__property_of.value, __property_of.set, None, None)

    
    # Element {sptdf}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__sptdf_attributes_sptdflocation', True, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 38, 4), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element {sptdf}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__sptdf_attributes_sptdfx', False, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 39, 4), )

    
    x = property(__x.value, __x.set, None, None)

    
    # Element {sptdf}y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'y'), 'y', '__sptdf_attributes_sptdfy', False, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 40, 4), )

    
    y = property(__y.value, __y.set, None, None)

    
    # Element {sptdf}radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'radius'), 'radius', '__sptdf_attributes_sptdfradius', False, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 41, 4), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Element {sptdf}property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'property'), 'property_', '__sptdf_attributes_sptdfproperty', True, pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 42, 2), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __color.name() : __color,
        __name.name() : __name,
        __property_of.name() : __property_of,
        __location.name() : __location,
        __x.name() : __x,
        __y.name() : __y,
        __radius.name() : __radius,
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.attributes = attributes
Namespace.addCategoryObject('typeBinding', 'attributes', attributes)


# Complex type {sptdf}property_of with content type SIMPLE
class property_of (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {sptdf}property_of with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'property_of')
    _XSDLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 46, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute prep uses Python identifier prep
    __prep = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'prep'), 'prep', '__sptdf_property_of_prep', pyxb.binding.datatypes.string, required=True)
    __prep._DeclarationLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 49, 4)
    __prep._UseLocation = pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 49, 4)
    
    prep = property(__prep.value, __prep.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __prep.name() : __prep
    })
_module_typeBindings.property_of = property_of
Namespace.addCategoryObject('typeBinding', 'property_of', property_of)


scene = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scene'), scenePic, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 11, 2))
Namespace.addCategoryObject('elementBinding', scene.name().localName(), scene)

object = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'object'), objectPic, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 12, 2))
Namespace.addCategoryObject('elementBinding', object.name().localName(), object)



scenePic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'object'), objectPic, scope=scenePic, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 16, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(scenePic._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'object')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 16, 2))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
scenePic._Automaton = _BuildAutomaton()




objectPic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributes, scope=objectPic, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 23, 4)))

objectPic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'object'), objectPic, scope=objectPic, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 24, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 24, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(objectPic._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 23, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(objectPic._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'object')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 24, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
objectPic._Automaton = _BuildAutomaton_()




attributes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'color'), pyxb.binding.datatypes.string, scope=attributes, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 35, 4)))

attributes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=attributes, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 36, 4)))

attributes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'property_of'), property_of, scope=attributes, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 37, 4)))

attributes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), pyxb.binding.datatypes.string, scope=attributes, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 38, 4)))

attributes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), pyxb.binding.datatypes.integer, scope=attributes, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 39, 4)))

attributes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'y'), pyxb.binding.datatypes.integer, scope=attributes, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 40, 4)))

attributes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'radius'), pyxb.binding.datatypes.integer, scope=attributes, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 41, 4)))

attributes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'property'), pyxb.binding.datatypes.string, scope=attributes, location=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 42, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 35, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 36, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 38, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 42, 2))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(attributes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'color')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 35, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(attributes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 36, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(attributes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'property_of')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 37, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(attributes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 38, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(attributes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 39, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(attributes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'y')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 40, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(attributes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'radius')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 41, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(attributes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'property')), pyxb.utils.utility.Location('/NOBACKUP/jdlopes/spotTheDifferenceAnalyzer/picdef.xsd', 42, 2))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
attributes._Automaton = _BuildAutomaton_2()

