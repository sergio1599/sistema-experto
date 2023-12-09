import tkinter as tk
from tkinter import ttk

from diagnosis_rules import NeurologicalDiagnosis, Symptom


def run_expert_system(symptom1, symptom2, symptom3):
    print("Síntomas ingresados:", symptom1.get(),
          symptom2.get(), symptom3.get())

    engine = NeurologicalDiagnosis()
    engine.reset()

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
            text="El paciente puede tener: " + ", ".join(diagnoses),
            foreground="blue"
        )
    else:
        result_label.config(
            text="No se encontraron diagnósticos.",
            foreground="red"
        )


# Crear la ventana principal
window = tk.Tk()
window.title("Sistema Experto de Diagnóstico Neurológico")
window.geometry("500x300")

subtitulo = tk.Label(
    text="Taller desarrollado por: Britne Vargas y Sergio Quintana", font=("Helvetica", 14))
subtitulo.pack(pady=10)

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 14), foreground='blue')

symptoms = [
    'agitación', 'alucinaciones', 'aura visual', 'cambios de personalidad',
    'convulsiones', 'desorientación', 'debilidad muscular', 'dificultad para respirar',
    'dificultad para resolver problemas', 'dolor de cabeza', 'dolor muscular',
    'movimientos involuntarios', 'nauseas', 'pérdida de conciencia',
    'pérdida de memoria', 'rigidez muscular', 'temblor en las manos',
    'vómitos'
]

symptom1_combobox = ttk.Combobox(window, values=symptoms)
symptom1_combobox.pack(pady=10)

symptom2_combobox = ttk.Combobox(window, values=symptoms)
symptom2_combobox.pack(pady=10)

symptom3_combobox = ttk.Combobox(window, values=symptoms)
symptom3_combobox.pack(pady=10)

run_button = ttk.Button(window, text="Diagnosticar",
                        command=on_diagnose_button_click)
run_button.pack(pady=20)

result_label = ttk.Label(window, text="", foreground='blue')
result_label.pack(pady=10)

# Iniciar la aplicación
window.mainloop()
