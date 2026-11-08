# Scientific review

## Correctness — PASS

The statement is limited to cyclic permutation \(i\mapsto i+1\) plus unitary \(0\mapsto r\). The arithmetic trajectory identity \(\delta(i,w)=i+A+rh_i\pmod n\) forces all \(n\) effective-jump counts to be distinct modulo \(n\) under synchronization. One trajectory must make at least \(n-1\) jumps, with \(n-r\) cyclic increments between each; this gives the exact lower bound on each letter count. The explicit word meets it, as shown by an induction on missing image states. Equality forces every jump to be effective for the extremal trajectory and consumes all cyclic increments in forced return intervals, proving **uniqueness**, including the \(n=2\) boundary. An independent subset-automaton BFS with dynamic shortest-path counts checked all 66 pairs through \(n=12\), and larger witness replays corroborated existence. Finite tests do not prove the unbounded statement.

## Originality — PASS with bibliographic risk

The nearest primary source is Martyugin (2009), Proposition 6.2 and its Figure 5 (full text, p. 532), which **already establishes** non-synchronizability for noncoprime parameters and the exact reset threshold for coprime parameters and exhibits a shortest word. This material is therefore prior, not claimed as novel. It does **not** state or prove that **every** shortest reset word equals its exhibited one. Existence of one shortest word and its length does not entail uniqueness. Don (2016), Proposition 15, provides broad coprime circular-automaton synchronization and an upper bound, not exact optimizer multiplicities. Rystsov–Szykuła (2023) treats general unitary/permutational synchronization criteria and monoid upper bounds, likewise not optimizer enumeration. General shortest-word algorithms treat instances but do not supply the same all-parameter singleton theorem. Relevant database findings about Černý compression profiles and other automata do not imply this enumeration. A differently phrased previously published proof could remain; novelty has not been independently certified.

## Mathematical value — PASS

The count of distinct optimal reset words is a natural, mathematically motivated exact invariant of a synchronizing automaton. Unlike the old threshold formula, **uniqueness is not a numerical consequence**: multiple words can attain the same minimum in related automata. This gives a complete rigidity classification for the canonical two-generator cyclic/unitary family over all parameters, based on a sharp trajectory lower bound and an equality-case proof. It supplies a stringent benchmark for algorithms enumerating shortest reset words and distinguishes this family from known slow families with many optimizers. The result does not assert any new general synchronization bound.

## Sources and limits

Martyugin, *Acta Cybernetica* 19 (2009), Proposition 6.2; Don, *Electronic Journal of Combinatorics* 23(3) (2016), Proposition 15; Rystsov–Szykuła, arXiv:2307.01302v1 and arXiv:2309.08321v1; Szykuła–Zyzik, ESA 2022. General or unindexed uniqueness claims elsewhere cannot be definitively excluded. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
