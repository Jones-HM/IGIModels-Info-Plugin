"""
Info: IGI Models info with multiple data support, 
this is plugin for `IGI 1 Editor` available here: https://github.com/IGI-Research-Devs/I.G.I-1-Editor
Output the models in CSV,JSON Format.
Author: @HM.
Date: 20/05/2022.
"""
#Import the libraries.
import re
import sys
import csv
import json
import os
from IGIModelsClass import IGIModels

#Global Variables
header_tag = ['Model Name', 'Model Id']
curr_dir = os.getcwd()

def get_level_models(data: str, distinct=True):
    data = re.findall('\d{3}_\d{2}_\d{1}', data)
    datalist = list(dict.fromkeys(data))
    if distinct:
        return datalist
    else:
        return data

#List utilities methods.
def list_to_json(datalist: list, filename: str, indent: int = 4):
    out_file_path = curr_dir + "\\" + filename+".json"
    with open(out_file_path, 'w', encoding='utf-8') as jsonf:
        json.dump(datalist, fp=jsonf, indent=indent)

def list_to_csv(datalist: list, filename: str):
    out_file_path = curr_dir + "\\" + filename+".csv"
    with open(out_file_path, 'w', newline='\n') as fp:
        wr = csv.writer(fp, quoting=csv.QUOTE_ALL)
        wr.writerow(header_tag)
        wr.writerows(datalist)

#Main method.
if __name__ == '__main__':

    try:
        argc = len(sys.argv)
        if argc <= 1:
            raise Exception("\nUsage " + sys.argv[0] + " level output-file output-format distinct-models" +
                            "\nExamples Below:\nLevel 1 JSON Models:\n" + sys.argv[0] + " 1 'Level-1-Models' 'json' 'true'" + 
                            "\nLevel 5 CSV Models:\n" + sys.argv[0] + " 5 'Level-5-Models' 'csv'")
        if argc < 4:
            raise Exception(
                "Application expected '5' parameters but only '" + str(argc) + "' were passed.")

        # Get the arguments from cmd.
        level = int(sys.argv[1])
        out_file = str(sys.argv[2])
        out_fmt = str(sys.argv[3])
        out_distinct = 'true' if argc == 4 else str(sys.argv[4])

        # Get curr working dir.
        curr_dir = os.path.abspath(os.getcwd())
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        curr_dir = os.path.dirname(os.path.abspath(__file__))

        # Instantiate IGI Models.
        igimodel = IGIModels()
        objects_qsc = "\objects.qsc"

        objects_file = igimodel.qeditor_path + r"\QFiles\IGI_QSC\missions\location0\level" + str(level) + objects_qsc

        #print("FILE PATH: ", objects_file)
        data = igimodel.read_file(objects_file, False, 'r')

        ai_count = 0
        level_models = get_level_models(data, out_distinct == 'true')

        out_data_list = []
        for model in level_models:
            model_name = igimodel.get_model_name(model, False)
            # Append data list for output.

            #Setting list for CSV output.
            if out_fmt == 'csv':
                models_list = []
                models_list.append(model_name)
                models_list.append(model)
                out_data_list.append(models_list)

            #Setting Dict for JSON output.
            if out_fmt == 'json':
                models_dict = {
                    header_tag[0]: model_name,
                    header_tag[1]: model,
                }
                out_data_list.append(models_dict)

            if model_name is None:
                print("Error Model: ", model)

            elif "AITYPE" in model_name:
                ai_count += 1

        if out_fmt == 'csv':
            list_to_csv(out_data_list, out_file)

        if out_fmt == 'json':
            list_to_json(out_data_list, out_file)

        print("Level #" + str(level) + " Total Models: " + str(len(level_models)) + " A.I Count: " + str(ai_count))

    except Exception as e:
        print("Exception in main: " + str(e))
