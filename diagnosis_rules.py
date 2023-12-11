from experta import Fact, Rule, KnowledgeEngine, AND, OR, Field, NOT


class Symptom(Fact):
    name = Field(str)


class NeurologicalDisorder(Fact):
    name = Field(str)


class NeurologicalDiagnosis(KnowledgeEngine):
    diagnoses = set()
    diagnosis_found = False

    @Rule(
        OR(
            Symptom(name='desorientacion'),
            Symptom(name='dificultad para resolver problemas'),
            Symptom(name='perdida de memoria')
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
            Symptom(name='movimientos involuntarios'),
            Symptom(name='rigidez muscular'),
            Symptom(name='temblor en las manos')
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
            Symptom(name='perdida de conciencia'),
            Symptom(name='aura visual')
        ),
        NOT(NeurologicalDisorder(name='Epilepsia'))
    )
    def epilepsy(self):
        self.declare(NeurologicalDisorder(name='Epilepsia'))
        self.diagnoses.add('Epilepsia')
        self.diagnosis_found = True

    @Rule(
        OR(
            Symptom(name='debilidad muscular'),
            Symptom(name='dolor muscular'),
            Symptom(name='dificultad para respirar')
        ),
        NOT(NeurologicalDisorder(name='Miastenia gravis'))
    )
    def myasthenia_gravis(self):
        self.declare(NeurologicalDisorder(name='Miastenia gravis'))
        self.diagnoses.add('Miastenia gravis')
        self.diagnosis_found = True

    @Rule(
        OR(
            Symptom(name='dolor de cabeza'),
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
            Symptom(name='cambios de personalidad')
        ),
        NOT(NeurologicalDisorder(name='Esquizofrenia'))

    )
    def delirium(self):
        self.declare(NeurologicalDisorder(name='Esquizofrenia'))
        self.diagnoses.add('Esquizofrenia')
        self.diagnosis_found = True
