import os
from dataclasses import dataclass

class IGIModels:
    
    @dataclass
    class ModelData:
        model_name: str
        model_id: str

    #Globals.
    models_data = None
    models_file,qeditor_path = '',''
    models_list = []
    
    def __init__(self):
        appdata_path = os.getenv('APPDATA')
        self.qeditor_path = appdata_path + '\\QEditor'
        self.models_file = self.qeditor_path + '\\IGIModels.txt'
        datalines = self.read_file(self.models_file,True)
        
        for datal in datalines:
            data = datal.strip()
            model_list = [l.split('=') for l in data.split(',') if l]
            model_data = self.ModelData(model_list[0][0].strip(),model_list[0][1].strip())
            self.models_list.append(model_data)
        
    def read_file(self,filename:str,lines:bool=False,mode:str='r'):    
        fp = open(filename,mode=mode)
        if not lines:
            data = fp.read()
        else:
            data = fp.readlines()
        fp.close()
        return data


    def get_model_name(self,model_id:str,verbose=False):
        if self.models_list:
            for model in self.models_list:
                if model.model_id == model_id:
                    if verbose:
                        print("Model: ",model.model_name,end='\t')
                        print("Id:" + model.model_id + ".mef")
                    return model.model_name
        return None

    def get_model_id(self,model_name:str,verbose=False):
        if self.models_list:
            for model in self.models_list:
                if model.model_name == model_name:
                    if verbose:
                        print("Model Id: ",model.model_id,end='\t')
                        print("Name:" + model.model_name + ".mef")
                    return model.model_id
        return None
#Class Ends.