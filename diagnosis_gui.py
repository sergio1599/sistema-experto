import tkinter as tk
from diagnosis_rules import NeurologicalDisorder, Symptom, NeurologicalDiagnosis

window = tk.Tk()
window.title("Sistema Experto de Diagnóstico Neurológico")

symptom1_entry = tk.Entry(window)
symptom1_entry.pack()

symptom2_entry = tk.Entry(window)
symptom2_entry.pack()

symptom3_entry = tk.Entry(window)
symptom3_entry.pack()


def run_expert_system():
    symptom1 = symptom1_entry.get()
    symptom2 = symptom2_entry.get()
    symptom3 = symptom3_entry.get()

    engine = NeurologicalDiagnosis()
    engine.reset()
    engine.declare(Symptom(name=symptom1))
    engine.declare(Symptom(name=symptom2))
    engine.declare(Symptom(name=symptom3))
    engine.run()

    for disorder in engine.facts.filter(NeurologicalDisorder):
        print("El paciente puede tener:", disorder["name"])


run_button = tk.Button(window, text="Diagnosticar", command=run_expert_system)
run_button.pack()

window.mainloop()
