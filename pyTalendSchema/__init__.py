"""
This thing probably sucks, so please improve it if possible

I mean, this thing *is really rough*.
"""

import xml.etree.ElementTree as ET


class TalendSchema:

    def _bool_to_text(self, b_val):
        str(b_val).lower()

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
            'length': '-1',
            'nullable': True,
            'originalDbColumnName': 'newColumn',
            'originalLength': '-1',
            'pattern': '',
            'precision': '-1'
        }

        self.attr_special = {  # Do things
            'key': _
        }

    def add_column(self, **properties):

