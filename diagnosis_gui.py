# gui.py
import tkinter as tk
from tkinter import ttk
from experta import Fact

from diagnosis_rules import NeurologicalDiagnosis, Symptom


def run_expert_system(symptom1, symptom2, symptom3):
    print("Síntomas ingresados:", symptom1.get(),
          symptom2.get(), symptom3.get())

    engine = NeurologicalDiagnosis()
    engine.reset()

    # Llama al método get() para obtener el valor seleccionado del Combobox
    engine.declare(Symptom(name=symptom1.get()))
    engine.declare(Symptom(name=symptom2.get()))
    engine.declare(Symptom(name=symptom3.get()))

    engine.run()

    diagnoses = engine.diagnoses

    print("Diagnósticos encontrados:", diagnoses)
    return diagnoses


def on_diagnose_button_click():
    symptom1 = symptom1_combobox
    symptom2 = symptom2_combobox
    symptom3 = symptom3_combobox

    diagnoses = run_expert_system(symptom1, symptom2, symptom3)

    if diagnoses:
        result_label.config(
            text="El paciente puede tener: " + ", ".join(diagnoses))
    else:
        result_label.config(text="No se encontraron diagnósticos.")


# Crear la ventana principal
window = tk.Tk()
window.title("Sistema Experto de Diagnóstico Neurológico")

# Crear widgets ComboBox
symptoms = ['desorientacion', 'dificultad para resolver problemas', 'perdida de memoria',
            'movimientos involuntarios', 'rigidez muscular', 'temblor en las manos',
            'convulsiones', 'perdida de conciencia', 'aura visual',
            'debilidad muscular', 'dolor muscular', 'dificultad para respirar',
            'dolor de cabeza', 'nauseas', 'vomitos', 'agitacion', 'alucinaciones', 'cambios de personalidad']

symptom1_combobox = ttk.Combobox(window, values=symptoms)
symptom1_combobox.pack()

symptom2_combobox = ttk.Combobox(window, values=symptoms)
symptom2_combobox.pack()

symptom3_combobox = ttk.Combobox(window, values=symptoms)
symptom3_combobox.pack()

run_button = tk.Button(window, text="Diagnosticar",
                       command=on_diagnose_button_click)
run_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Iniciar la aplicación
window.mainloop()
