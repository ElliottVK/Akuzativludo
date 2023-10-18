import csv
import json

def generate_word_options(word):
    base = word.rstrip("ojn")
    
    pronouns_list = ["lin", "monujon", "min", "vin", "linon", "minon", "vinon", "tiun", "tiunon", "nin", "cin", "sin", "ĝin", "ilin"]
    if word in pronouns_list:
        base = word.rstrip("on")
        return [base, word, base + "o", base + "oj"]
    
    return [base + end for end in ["o", "on", "oj", "ojn"]]

def transform_csv_to_parsed_data(filename="output.csv"):
    transformed_data = []
    
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sentence = row["Sentence"].strip('"')
            noun_positions = [int(pos.strip()) for pos in row["Positions of Nouns"].strip('[]').split(',')]
            
            noun_data = []
            for pos in noun_positions:
                noun = sentence.split(" ")[pos - 1].rstrip(".")
                word_options = generate_word_options(noun)
                
                noun_data.append({
                    "correct_noun": noun,
                    "word_options": word_options
                })
            
            entry = {
                "num_nouns": int(row["Number of Nouns"]),
                "sentence": sentence,
                "noun_data": noun_data
            }
            
            transformed_data.append(entry)
    
    return transformed_data

def save_as_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

# Sample usage:
csv_filename = "C:\\Users\\Will\\Documents\\GitHub\\Akuzativludo\\output.csv"
new_parsed_data = transform_csv_to_parsed_data(csv_filename)

json_filename = "C:\\Users\\Will\\Documents\\GitHub\\Akuzativludo\\parsed_data_output.json"
save_as_json(new_parsed_data, json_filename)
