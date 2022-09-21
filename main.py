from abc import abstractmethod
import json
import pickle


class Meta(type):
    num_of_classes_created = 0

    def __new__(mcs, name, base, ns):
        class_instance = type.__new__(mcs, name, base, ns)
        class_instance.order_of_creation = mcs.num_of_classes_created
        mcs.num_of_classes_created += 1
        return class_instance

    def __init__(cls, name, base, ns):
        type.__init__(cls, name, base, ns)


class SerializationInterface(metaclass=Meta):

    @abstractmethod
    def save_data(self, data):
        pass

    @abstractmethod
    def load_data(self, data):
        pass


class JsonSerializer(SerializationInterface):

    def __init__(self):
        self.backup_file = "backup_data.json"

    def save_data(self, data):
        with open(self.backup_file) as json_backup_file:
            json.dump(data, json_backup_file)
            return "Your data was saved successfully!"

    def load_data(self, data):
        with open(self.backup_file) as json_backup_file:
            data = json.load(json_backup_file)
            return data


class BinSerializer(SerializationInterface):

    def __init__(self):
        self.backup_file = "backup_data.bin"

    def save_data(self, data):
        with open(self.backup_file) as bin_backup_file:
            pickle.dump(data, bin_backup_file)
            return "Your data was saved successfully!"

    def load_data(self, data):
        with open(self.backup_file) as bin_backup_file:
            data = pickle.load(bin_backup_file)
            return data

if __name__ == '__main__':
    assert (SerializationInterface.order_of_creation, JsonSerializer.order_of_creation, BinSerializer.order_of_creation) \
           == (0, 1, 2)
    a, b = JsonSerializer(), BinSerializer()
    assert (a.order_of_creation, b.order_of_creation) == (1, 2)
