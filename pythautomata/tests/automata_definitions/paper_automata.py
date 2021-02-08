from base_types.state import State
from base_types.symbol import SymbolChar
from base_types.alphabet import Alphabet
from utilities.automata_convertor import AutomataConvertor
from queryable_models.finite_automaton import FiniteAutomaton

abAlphabet = Alphabet(frozenset((SymbolChar('a'), SymbolChar('b'))))
abcAlphabet = Alphabet(frozenset((SymbolChar('a'), SymbolChar('b'), SymbolChar('c'))))

#TODO: REFERENCIAR PAPER
class PaperAutomata:

    @staticmethod
    def get_all_automata():
        return [
            PaperAutomata.get_first_example_automaton(),
            PaperAutomata.get_more_membership_queries_automaton(),
            PaperAutomata.get_more_equivalence_queries_automaton(),
            PaperAutomata.get_state_count_does_not_increase_automaton(),
            PaperAutomata.get_intermediate_hypothesis_automaton(),
            PaperAutomata.get_algorithm_would_not_terminate_automaton(),
            PaperAutomata.get_evolution_of_the_measure_automaton()
        ]

    # Σ*aΣ^n
    @staticmethod
    def get_first_example_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2")
        state3 = State("State 3", True)
        state4 = State("State 4", True)
        state5 = State("State 5", True)
        state6 = State("State 6")
        state7 = State("State 7", True)

        state0.add_transition(a, state1)
        state0.add_transition(b, state0)
        state1.add_transition(a, state2)
        state1.add_transition(b, state6)
        state2.add_transition(a, state3)
        state2.add_transition(b, state4)
        state3.add_transition(a, state3)
        state3.add_transition(b, state4)
        state4.add_transition(a, state5)
        state4.add_transition(b, state7)
        state5.add_transition(a, state2)
        state5.add_transition(b, state6)
        state6.add_transition(a, state5)
        state6.add_transition(b, state7)
        state7.add_transition(a, state1)
        state7.add_transition(b, state0)

        return FiniteAutomaton(abAlphabet, frozenset({state0}),
                               set([state0, state1, state2, state3,
                                    state4, state5, state6, state7]), "Paper - first example automaton")

    # Σ*aΣ
    @staticmethod
    def get_more_membership_queries_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = State("State 0", True)
        state1 = State("State 1", True)
        state2 = State("State 2", True)
        state3 = State("State 3", True)
        state4 = State("State 4")

        state0.add_transition(a, state1)
        state0.add_transition(b, state1)
        state1.add_transition(a, state2)
        state1.add_transition(b, state2)
        state2.add_transition(a, state3)
        state2.add_transition(b, state3)
        state3.add_transition(a, state4)
        state3.add_transition(b, state0)
        state4.add_transition(a, state4)
        state4.add_transition(b, state4)

        return FiniteAutomaton(abAlphabet, frozenset({state0}),
                               set([state0, state1,
                                    state2, state3, state4]), "Paper - More membership queries automaton")

    @staticmethod
    def get_more_equivalence_queries_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = State("State 0", True)
        state1 = State("State 1", True)
        state2 = State("State 2", True)
        state3 = State("State 3", True)
        state4 = State("State 4", True)
        state5 = State("State 5")

        state0.add_transition(a, state2)
        state0.add_transition(b, state1)
        state1.add_transition(a, state3)
        state1.add_transition(b, state1)
        state2.add_transition(a, state2)
        state2.add_transition(b, state4)
        state3.add_transition(a, state5)
        state3.add_transition(b, state5)
        state4.add_transition(a, state5)
        state4.add_transition(b, state4)
        state5.add_transition(a, state5)
        state5.add_transition(b, state5)

        return FiniteAutomaton(abAlphabet, frozenset({state0}),
                               set([state0, state1, state2,
                                    state3, state4, state5]), "Paper - More equivalence queries automaton")

    @staticmethod
    def get_state_count_does_not_increase_automaton():
        a = abcAlphabet['a']
        b = abcAlphabet['b']
        c = abcAlphabet['c']

        state0 = State("State 0", True)
        state1 = State("State 1")
        state2 = State("State 2", True)
        state3 = State("State 3")

        state0.add_multiple_transitions(a, [state0, state1, state2])
        state0.add_multiple_transitions(b, [state1, state3])
        state0.add_transition(c, state3)

        state1.add_transition(a, state2)
        state1.add_multiple_transitions(b, [state0, state1, state2])
        state1.add_multiple_transitions(c, [state1, state3])

        state2.add_transition(a, state1)
        state2.add_transition(b, state3)
        state2.add_transition(c, state3)

        state3.add_transition(a, state2)
        state3.add_transition(b, state3)
        state3.add_transition(c, state2)

        result = FiniteAutomaton(abcAlphabet, frozenset({state0, state2}),
                                 set([state0, state1, state2, state3]),
                                 "Paper - State count does not increase automaton")
        result._queryable_self = AutomataConvertor.convert_nfa_to_dfa(result)
        return result

    @staticmethod
    def get_intermediate_hypothesis_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = State("State 0")
        state1 = State("State 1", True)
        state2 = State("State 2", True)
        state3 = State("State 3")
        state4 = State("State 4")

        state0.add_transition(a, state4)
        state0.add_transition(b, state1)
        state1.add_transition(a, state2)
        state1.add_transition(b, state1)
        state2.add_transition(a, state4)
        state2.add_transition(b, state3)
        state3.add_transition(a, state2)
        state3.add_transition(b, state2)
        state4.add_transition(a, state4)
        state4.add_transition(b, state4)

        return FiniteAutomaton(abAlphabet, frozenset({state0}),
                               set([state0, state1, state2, state3, state4]),
                               "Paper - Intermediate hypothesis automaton")

    @staticmethod
    def get_algorithm_would_not_terminate_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = State("State 0", True)
        state1 = State("State 1", True)
        state2 = State("State 2")
        state3 = State("State 3")
        state4 = State("State 4")
        state5 = State("State 5")
        state6 = State("State 6", True)
        state7 = State("State 7")
        state8 = State("State 8", True)
        state9 = State("State 9", True)

        state0.add_transition(a, state1)
        state0.add_transition(b, state9)
        state1.add_transition(a, state2)
        state1.add_transition(b, state7)
        state2.add_transition(a, state3)
        state3.add_transition(a, state2)
        state3.add_transition(b, state4)
        state4.add_transition(b, state5)
        state5.add_transition(b, state6)
        state7.add_transition(b, state8)
        state8.add_transition(b, state6)
        state9.add_transition(b, state9)

        return FiniteAutomaton(abAlphabet, frozenset({state0}),
                               set([state0, state1, state2, state3, state4,
                                    state5, state6, state7, state8, state9]),
                               "Paper - Algorithm would not terminate automaton")

    @staticmethod
    def get_evolution_of_the_measure_automaton():
        a = abAlphabet['a']
        b = abAlphabet['b']

        state0 = State("State 0")
        state1 = State("State 1")
        state2 = State("State 2")
        state3 = State("State 3", True)
        state4 = State("State 4")
        state5 = State("State 5", True)
        state6 = State("State 6")

        state0.add_transition(b, state1)
        state1.add_transition(a, state2)
        state2.add_transition(a, state3)
        state3.add_transition(a, state5)
        state3.add_transition(b, state4)
        state4.add_transition(a, state5)

        return FiniteAutomaton(abAlphabet, frozenset({state0}),
                               set([state0, state1, state2,
                                    state3, state4, state5, state6]),
                               "Paper - Evolution of the measure automaton")