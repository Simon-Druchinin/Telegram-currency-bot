class Data():
    """Обработка данных для вывода"""
    def __init__(self, values):
        del values[3::4]
        self.names = values[::3]

        del values[::3]

        self.buys = values[::2]
        self.sells = values[1::2]

        self.best_buy_value = max(self.buys)
        self.best_sell_value = min(self.sells)
    
    def get_all_list(self):
        message = ''
        i = 0
        while i < len(self.names):
            message += f'{self.names[i]}: \nПокупка:{self.buys[i]} \nПродажа:{self.sells[i]} \n\n'
            i += 1
        
        message = message.rstrip()

        return message
    
    def __get_best_values(self, values, best_value):
        message = ''

        i = 0
        while i < len(values):
            if values[i] == best_value:
                message += f'{self.names[i]} - {best_value}\n'
            i += 1
            
        message = message.rstrip()

        return message
    
    def get_best_buy_value(self):
        return self.__get_best_values(self.buys, self.best_buy_value)
    
    def get_best_sell_value(self):
        return self.__get_best_values(self.sells, self.best_sell_value)
    
    def get_data_names(self):
        names = self.names
        return names

class Data_address(Data):

    def __init__(self, values):
        self.bank_names = []
        self.all_address_list = values

        for value in self.all_address_list:
            if 'Отделения' in value:
                self.bank_names.append(value) 
    
    def get_your_bank_address(self, bank_name):

        bank_address_list = ''

        if self.bank_names.index(bank_name)+1 != len(self.bank_names):

            bank_name_index = self.bank_names.index(bank_name)
            bank_name_index += 1
            bank_stop_name = self.bank_names[bank_name_index]

            start_point = self.all_address_list.index(bank_name)
            stop_point = self.all_address_list.index(bank_stop_name)

            for address in range(start_point, stop_point):
                # bank_address_list.append(self.all_address_list[address])
                bank_address_list += f'{self.all_address_list[address]}\n\n'

        else:
            start_point = self.all_address_list.index(bank_name)
            for address in range(start_point, len(self.all_address_list)):
                bank_address_list += f'{self.all_address_list[address]}\n\n'

        return bank_address_list
    
    def get_bank_names(self):
        return self.bank_names