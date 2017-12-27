import json

data_file_path = "/home/gabrielf/dev/EXP/data/data.json"

def jsonify_events(string):
    string = "[" + string + "]"
    floating_index = 0
    for char in string:
        if char == '}' and string[floating_index + 1] == '\n':
            if string[floating_index + 2] != ']':
                print "char is %s and index is %i" % (char, floating_index)
                string = string[:floating_index + 1] + ',' + string[floating_index + 1:]
                floating_index += 1
        floating_index += 1
    return string


def get_latest_time(dicts):
    print dicts
    times = [a_dict['time'] for a_dict in dicts]
    return max(times)

            

with open(data_file_path, 'rw') as datafile:
    data = datafile.read()
    formated_data = jsonify_events(data)
    json_data = json.loads(formated_data)
    dicts = []
    for event in json_data:
        dicts.append({k: event[k] for k in ('id', 'time')})
    print "latest time is %s" % get_latest_time(dicts)
    print "dics are %s" % str(dicts)


#        filtered_data = filter(get_id_n_time, json_data)

#    json_data = jsonify(data)
#    filtered_data = 
