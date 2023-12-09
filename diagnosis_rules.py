from dataclasses import Field
from experta import Fact, Rule, KnowledgeEngine, AND, OR


class Symptom(Fact):
    name = Field(str, mandatory=True)
    severity = Field(int, mandatory=True)
    duration = Field(int, mandatory=True)
    pass


class NeurologicalDisorder(Fact):
    name = Field(str, mandatory=True)
    probability = Field(float, mandatory=True)
    pass


class NeurologicalDiagnosis(KnowledgeEngine):
    @Rule(
        OR(
            Symptom(name='desorientacion'),
            Symptom(name='dificultad_para_resolver_problemas'),
            Symptom(name='perdida_de_memoria')
        )
    )
    def alzheimer(self):
        self.declare(NeurologicalDisorder(name='Alzheimer'))

    @Rule(
        OR(
            Symptom(name='movimientos_involuntarios'),
            Symptom(name='rigidez_muscular'),
            Symptom(name='temblor_en_las_manos')
        )
    )
    def parkinson(self):
        self.declare(NeurologicalDisorder(name='Parkinson'))

    @Rule(
        OR(
            Symptom(name='convulsiones'),
            Symptom(name='perdida_de_conciencia'),
            Symptom(name='aura_visual')
        )
    )
    def epilepsy(self):
        self.declare(NeurologicalDisorder(name='Epilepsia'))

    @Rule(
        OR(
            Symptom(name='debilidad_muscular'),
            Symptom(name='dolor_muscular'),
            Symptom(name='dificultad_para_respirar')
        )
    )
    def myasthenia_gravis(self):
        self.declare(NeurologicalDisorder(name='Miastenia gravis'))

    @Rule(
        OR(
            Symptom(name='dolor_de_cabeza'),
            Symptom(name='nauseas'),
            Symptom(name='vomitos'),
            Symptom(name='dificultad_para_hablar')
        )
    )
    def migraine(self):
        self.declare(NeurologicalDisorder(name='Migraña'))

    @Rule(
        OR(
            Symptom(name='agitacion'),
            Symptom(name='alucinaciones'),
            Symptom(name='cambios_de_personalidad')
        )
    )
    def delirium(self):
        self.declare(NeurologicalDisorder(name='Delirium'))
