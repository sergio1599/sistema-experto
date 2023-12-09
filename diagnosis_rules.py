from experta import Fact, Rule, KnowledgeEngine, AND, OR, Field, NOT


class Symptom(Fact):
    name = Field(str)
    severity = Field(int)
    duration = Field(int)


class NeurologicalDisorder(Fact):
    name = Field(str)
    probability = Field(float)


class NeurologicalDiagnosis(KnowledgeEngine):
    diagnoses = set()
    diagnosis_found = False

    @Rule(
        OR(
            Symptom(name='desorientacion'),
            Symptom(name='dificultad_para_resolver_problemas'),
            Symptom(name='perdida_de_memoria')
        ),
        NOT(NeurologicalDisorder(name='Alzheimer'))
    )
    def alzheimer(self):
        print("Regla - Alzheimer")
        self.diagnoses.add('Alzheimer')
        self.declare(NeurologicalDisorder(name='Alzheimer'))
        self.diagnosis_found = True

    @Rule(
        OR(
            Symptom(name='movimientos_involuntarios'),
            Symptom(name='rigidez_muscular'),
            Symptom(name='temblor_en_las_manos')
        ),
        NOT(NeurologicalDisorder(name='Parkinson'))
    )
    def parkinson(self):
        self.declare(NeurologicalDisorder(name='Parkinson'))
        self.diagnoses.add('Parkinson')
        self.diagnosis_found = True

    @Rule(
        OR(
            Symptom(name='convulsiones'),
            Symptom(name='perdida_de_conciencia'),
            Symptom(name='aura_visual')
        ),
        NOT(NeurologicalDisorder(name='Epilepsia'))
    )
    def epilepsy(self):
        self.declare(NeurologicalDisorder(name='Epilepsia'))
        self.diagnoses.add('Epilepsia')
        self.diagnosis_found = True

    @Rule(
        OR(
            Symptom(name='debilidad_muscular'),
            Symptom(name='dolor_muscular'),
            Symptom(name='dificultad_para_respirar')
        ),
        NOT(NeurologicalDisorder(name='Miastenia gravis'))
    )
    def myasthenia_gravis(self):
        self.declare(NeurologicalDisorder(name='Miastenia gravis'))
        self.diagnoses.add('Miastenia gravis')
        self.diagnosis_found = True

    @Rule(
        OR(
            Symptom(name='dolor_de_cabeza'),
            Symptom(name='nauseas'),
            Symptom(name='vomitos'),
        ),
        NOT(NeurologicalDisorder(name='Migraña'))
    )
    def migraine(self):
        self.declare(NeurologicalDisorder(name='Migraña'))
        self.diagnoses.add('Migraña')
        self.diagnosis_found = True

    @Rule(
        OR(
            Symptom(name='agitacion'),
            Symptom(name='alucinaciones'),
            Symptom(name='cambios_de_personalidad')
        ),
        NOT(NeurologicalDisorder(name='Esquizofrenia'))

    )
    def delirium(self):
        self.declare(NeurologicalDisorder(name='Esquizofrenia'))
        self.diagnoses.add('Esquizofrenia')
        self.diagnosis_found = True
