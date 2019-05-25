from datetime import datetime, timedelta
import json

def get_data(log_path):
    delimiter = '|'

    with open(log_path) as fp:
        text = fp.read()
        bits = text.split(delimiter)
        # throw away empty thing
        bits = bits[:-1]
        
    data = [json.loads(bit) for bit in bits]
    return data

def count_open_deliveries(data):
    n_starts = 0
    n_ends = 0
    for rec in data:
        if rec['type'] == 'delivery-started':
            n_starts += 1
        elif rec['type'] == 'delivery-ended':
            n_ends += 1
        else:
            raise ValueError

    n_open = n_starts - n_ends
    return n_open

def find_deliveries_started_in(data, date_range):
    # parse each timestamp and cmp to range ends
    return []

def find_deliveries_started_in_last_hour(data):
    now = datetime.now()
    date_range = [
        now - timedelta(hours=1),
        now
    ]
    return find_deliveries_started_in(data, date_range)

def print_info(data):
    n0 = len(find_deliveries_started_in_last_hour(data))
    n1 = count_open_deliveries(data)

    print("deliveries started in last hour: {}".format(n0))
    print("deliveries started but not ended: {}".format(n1))
    
def main(args):
    log_path = 'event-logger/events.txt'
    data = get_data(log_path)
    # print(data[0])
    print_info(data)
    return data[0]

if __name__ == '__main__':
    main(1)
