# from texttable import Texttable


# class CreateView:
#     def __init__(self):
#         self.t = Texttable()

#     def createView(self, headers, data):
#         self.t.add_row(headers)
#         for row in data:
#             row_values = [row[column] for column in headers]
#             self.t.add_row(row_values)
#         return self.t.draw()

#     def createSingleView(self, data):
#         for row in data:
#             self.t.add_row([row, data[row]])
#         return self.t.draw()
from texttable import Texttable

class CreateView:
    def __init__(self):
        self.t = Texttable()

    def createSingleView(self, data):
        self._add_data_rows(data)
        return self.t.draw()

    def _add_data_rows(self, data, parent_key=''):
        for key, value in data.items():
            if isinstance(value, dict):
                if key in ('address', 'company'):
                    self._add_nested_rows(key, value, parent_key)
                else:
                    self._add_data_rows(value, f"{parent_key}.{key}")
            else:
                self.t.add_row([f"{parent_key}.{key}", value])

    def _add_nested_rows(self, nested_key, nested_value, parent_key):
        for sub_key, sub_value in nested_value.items():
            if isinstance(sub_value, dict):
                self._add_nested_rows(sub_key, sub_value, f"{parent_key}.{nested_key}")
            else:
                self.t.add_row([f"{parent_key}.{nested_key}.{sub_key}", sub_value])
