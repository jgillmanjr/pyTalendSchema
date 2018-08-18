"""
This thing probably sucks, so please improve it if possible

I mean, this thing *is really rough*.
"""

import xml.etree.ElementTree as ET
from html import escape as hte


class TalendSchema:

    def _attr_prep(self, key, value):
        if not isinstance(value, str):
            value = str(value)

        if key in self.attr_bool:
            return {key: str(value).lower()}

        if key == 'label':
            return {
                'label': hte(value),
                'originalDbColumnName': hte(value)
            }

        if key == 'length':
            return {
                'length': hte(value),
                'originalLength': hte(value)
            }

        return {key: hte(value)}

    def __init__(self):
        self.header = '<?xml version="1.0" encoding="UTF-8"?>'
        self.schema = ET.Element('schema')
        self.columns = []

        self.type_map = {
            'boolean': 'id_Boolean',
            'byte': 'id_Byte',
            'byte[]': 'id_byte[]',
            'character': 'id_Character',
            'date': 'id_Date',
            'double': 'id_Double',
            'float': 'id_Float',
            'bigdecimal': 'id_BigDecimal',
            'integer': 'id_Integer',
            'long': 'id_Long',
            'object': 'id_Object',
            'short': 'id_Short',
            'string': 'id_String',
            'list': 'id_List',
            'document': 'id_Document'
        }

        self.attrs = {
            'comment': '',
            'default': '',
            'key': False,
            'label': 'newColumn',
            'length': -1,
            'nullable': True,
            'pattern': '',
            'precision': -1,
            'type': '',
        }

        self.attr_bool = [
            'key',
            'nullable'
        ]

    def add_column(self, talendType, **properties):
        local_attrs = {'talendType': self.type_map[talendType]}

        for key in self.attrs.keys():
            if key not in properties:
                raw_value = self.attrs[key]
            else:
                raw_value = properties[key]

            d = self._attr_prep(key, raw_value)

            local_attrs = {
                **local_attrs,
                **d
            }

        ET.SubElement(self.schema, 'column', attrib=local_attrs)

    def dump_schema(self):
        print(self.header)
        ET.dump(self.schema)

    def write_schema(self, filename):
        with open(filename, 'w') as sf:
            sf.write(self.header)
            sf.write(ET.tostring(self.schema, encoding='unicode'))
