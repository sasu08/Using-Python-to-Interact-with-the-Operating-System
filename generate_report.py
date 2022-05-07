#!/usr/bin/env python3
#3
import csv

def read_employees(csv_file_location):
    """read_employees

    Keyword arguments:
    csv_file_location -- ruta del archivo csv
    Return: lista de empleados con todos sus datos.
    """
    with open(csv_file_location, 'r') as f:
        # Para facilitar la especificación del formato de los registros de entrada y salida, los parámetros de formato específicos se agrupan en dialectos.
        # skipinitialspace -- salta los espacios iniciales.
        # strict -- arroja error si existe un mal csv input.
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        # Crea una instancia de DictReader
        # DictReader es una clase que lee un archivo csv y devuelve una lista de diccionarios.
        reader = csv.DictReader(f, dialect='empDialect')
        employee_list = []
        
        for data in reader:
            employee_list.append(data)
        
        return employee_list
    

def process_data(employee_list):
    """process_data

    Keyword arguments:
    employee_list -- lista de empleados
    Return: diccionario con los datos de los departamentos y la cantidad de empleados por departamento.
    """
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
        
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data


def write_report(dictionary, report_file):
    """write_report

    Keyword arguments:
    dictionary -- diccionario con los datos de los departamentos y la cantidad de empleados por departamento.
    report_file -- ruta del archivo de salida
    """
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')

# Ejecución del programa
if(__name__ == "__main__"):
    employee_list = read_employees('/home/student-00-f7585db6fcae/data/employees.csv')
    dictionary = process_data(employee_list)
    write_report(dictionary, '/home/student-00-f7585db6fcae/data/report.txt')