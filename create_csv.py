import csv
import random

field_dict = {
    "cpu": {
        "eval": [1,2,4,6,8,10]
    },
    "frequency": {
        "eval": [i/10 for i in range(25,40)]
    },
    "ram": {
        "eval": [0.5, 1, 2, 4, 8, 16, 32, 64, 128]
    },
    "rating": {
        "min_val": 1,
        "max_val": 5
    },
    "price": {
        "min_val": 500,
        "max_val": 4000
    }
}


def create_sample(fields:dict):
    sample = []
    for field, val in fields.items():
        if "eval" in val.keys():
            sample_val = random.sample(val["eval"],1)[0]
        else:
            sample_val = random.uniform(val["min_val"], val["max_val"])
        sample.append(sample_val)
    
    return sample

def create_samples(field_dict:dict, n_samples:int, file_name:str):
    fields = list(field_dict.keys())
    fields.insert(0, "id")
    rows = []
    
    for i in range(n_samples):
        sample = create_sample(field_dict)
        sample.insert(0, i)
        rows.append(sample)

    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(rows)

if __name__ == "__main__":
    create_samples(field_dict, 100, "example.csv")