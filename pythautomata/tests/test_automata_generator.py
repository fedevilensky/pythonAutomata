from unittest import TestCase
from utilities.automata_generator import AutomataGenerator
from base_types.alphabet import Alphabet
from base_types.symbol import SymbolChar
from teachers.automaton_teacher import AutomatonTeacher
from learners.nlstar_learner import NLStarLearner


class TestAutomataGenerator(TestCase):

    def test_generated_correctly_1(self):
        binaryAlphabet = Alphabet(
            frozenset([SymbolChar('0'), SymbolChar('1')]))
        generated_automata = AutomataGenerator.generate_dfa(binaryAlphabet, 80)
        self._assert_correctness(generated_automata)

    def test_generated_correctly_2(self):
        binaryAlphabet = Alphabet(
            frozenset([SymbolChar('0'), SymbolChar('1')]))
        generated_automata = AutomataGenerator.generate_dfa(binaryAlphabet, 49)
        self._assert_correctness(generated_automata)

    def test_generated_correctly_3(self):
        abcdAlphabet = Alphabet(frozenset(
            [SymbolChar('a'), SymbolChar('b'), SymbolChar('c'), SymbolChar('d')]))
        generated_automata = AutomataGenerator.generate_dfa(abcdAlphabet, 49)
        self._assert_correctness(generated_automata)

    def test_generated_correctly_4(self):
        alphabet012 = Alphabet(
            frozenset([SymbolChar('0'), SymbolChar('1'), SymbolChar('2')]))
        generated_automata = AutomataGenerator.generate_dfa(alphabet012, 1)
        self._assert_correctness(generated_automata)

    def _assert_correctness(self, automaton):
        self.assertTrue(automaton.is_deterministic)
        self.assertTrue(self._all_states_are_rechable(automaton))
        self.assertTrue(len(automaton.initial_states) == 1)
        self.assertTrue(self._has_final_state(automaton))

    def _all_states_are_rechable(self, automaton):
        unrechable = automaton.states.copy()
        for state in unrechable.copy():
            for destinations in state.transitions.values():
                unrechable = unrechable - destinations
        return len(unrechable) == 1  # Hole

    def _has_final_state(self, automaton):
        return any(state.is_final for state in automaton.states)