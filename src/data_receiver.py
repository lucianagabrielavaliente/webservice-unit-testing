class DataReceiver:
    def __init__(self, dataset_id, table_id) -> None:
        self.dataset_id = dataset_id
        self.table_id = table_id

    def check_validity(self, data):
        if "important" not in data:
            raise AssertionError("FAILED")
        
    def clean_up_data(self, _data):
        data = dict(_data)
        if 'not_needed' in data:
            del data['not_needed']
        if 'temp' in data:
            del data['temp']
        return data
    
    def write(self, client, data):
        table_ref = client.dataset(self.dataset_id).table(self.table_id)
        table = client.get_table(table_ref)
        return client.insert_rows_json(table, [data], ignore_unknown_values=True)
        