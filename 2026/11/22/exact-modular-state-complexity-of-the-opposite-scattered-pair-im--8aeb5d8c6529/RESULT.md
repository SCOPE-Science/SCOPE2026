# Exact modular state complexity of the opposite scattered-pair imbalance

## Finding

For each integer \(m\ge2\), let \(\binom{w}{uv}\) denote the number of pairs of positions in a finite binary word \(w\) that spell \(uv\) in increasing order. Put
\[
I(w)=\binom{w}{01}-\binom{w}{10},\qquad
L_m=\{w\in\{0,1\}^{*}:I(w)\equiv0\pmod m\}.
\]
The exact state complexity of a **complete deterministic finite automaton** for this language is
\[
\operatorname{sc}(L_m)=\frac{m^3}{\gcd(m,2)}.
\]
Thus the state complexity is \(m^3\) when \(m\) is odd and \(m^3/2\) when \(m\) is even. This is an exact all-modulus theorem, not an asymptotic estimate.

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\); all inputs are finite words, including the empty word. Distinct embeddings of a two-letter pattern are counted with multiplicity. The modulus is an arbitrary integer \(m\ge2\), prime or composite. Automata are deterministic, complete and recognize the zero-residue language rather than report the count after each prefix. State complexity means the number of distinct Myhill–Nerode right quotients.

Set \(g=\gcd(2,m)\). For any word \(w\), let \(a(w)\) be the number of zeros modulo \(m\), \(b(w)\) its number of ones modulo \(m\), and \(d(w)=I(w)\bmod m\).

## Proof

**1. A complete automaton and its reachable state set.** Every cross-symbol pair is either \(01\) or \(10\), so
\[
\binom{w}{01}+\binom{w}{10}=|w|_0|w|_1,\qquad
I(w)=2\binom{w}{01}-|w|_0|w|_1.
\]
Consequently \(d(w)+a(w)b(w)\equiv0\pmod g\). Appending \(0\) creates one new \(10\) for each prior one, and appending \(1\) creates one new \(01\) for each prior zero. Thus the transitions on \((a,b,d)\), modulo \(m\), are
\[
0:(a,b,d)\mapsto(a+1,b,d-b),\qquad
1:(a,b,d)\mapsto(a,b+1,d+a).
\]
The states are
\[
Q_m=\{(a,b,d)\in(\mathbb Z/m\mathbb Z)^3:d+ab\equiv0\pmod g\}.
\]
There are \(m^3/g\) states, since for fixed \(a,b\) exactly \(m/g\) values of \(d\) are allowed. The start state is \((0,0,0)\); a state accepts exactly when \(d=0\). This is a complete recognizer.

All states of \(Q_m\) are reachable. Fix \(a,b\), take actual numbers of zeros and ones equal to the canonical representatives \(a+m,b+m\). Every integer from zero through their product is a possible scattered \(01\)-count: the ordered word with all ones before all zeros has count zero, and repeatedly interchanging an adjacent \(10\) to \(01\) increases this count by one until the fully sorted word reaches the product. In particular, all residues of \(\binom{w}{01}\) modulo \(m\) are attained (the product is at least \(m^2\)). By \(d=2\binom{w}{01}-ab\), these are exactly the allowed values of \(d\). Therefore every state is reached by a finite word.

**2. Which suffix residues can be realized?** Let \(z\) be a suffix with zero/one counts \((A,B)\pmod m\), and let \(E=I(z)\pmod m\). The same pair identity shows that a triple \((A,B,E)\) is realized by a suffix if and only if
\[
E+AB\equiv0\pmod g.
\]
Necessity was proved above. For sufficiency, choose actual counts \(A+m\) and \(B+m\), using canonical representatives; their product is at least \(m^2\). The attainable \(01\)-counts span every integer from zero to that product, and multiplication by two modulo \(m\) has image exactly the multiples of \(g\). Hence the demanded \(E\) is achieved.

For a prefix state \((a,b,d)\), the imbalance after appending such a suffix is
\[
d+E+aB-bA\pmod m.
\]
Therefore a suffix with letter-count residues \((A,B)\) can make this prefix accepting precisely when the required residue \(E=-d-aB+bA\) is achievable; by the parity constraint above this holds when
\[
(a+A)(b+B)\equiv0\pmod g.
\]
This criterion is automatic if \(m\) is odd. If \(m\) is even, it holds whenever at least one of the two final letter counts is even.

**3. Every two states are distinguishable.** Fix any two states \(s=(a,b,d)\), \(s'=(a',b',d')\), and write \(\Delta a=a-a'\), \(\Delta b=b-b'\), \(\Delta d=d-d'\) modulo \(m\). Consider the following three suffix count-residue choices:
\[
(A,B)=(-a,0),\quad(-a,1),\quad(-a+1,-b).
\]
For each choice, \((a+A)(b+B)\equiv0\pmod g\), because either \(a+A=0\) or \(b+B=0\) modulo \(m\). Thus a suffix with these counts can always be selected so that it accepts \(s\). If it also accepted \(s'\), the two final imbalances would agree. Their difference is
\[
\Delta d+\Delta a B-\Delta b A.
\]
If this vanished at all three listed choices, subtraction of the first two equations would give \(\Delta a=0\). Subtracting the first from the third would then give \(\Delta b=0\), and either equation would give \(\Delta d=0\). Therefore distinct states cannot satisfy all three equalities: at least one of the feasible suffix classes admits an actual suffix that accepts exactly one state. Every pair of distinct reachable states is Myhill–Nerode distinguishable, proving that the complete automaton is minimal.

## Verification

The companion standalone Python 3 program `verify_modular_pair_balance.py` independently enumerates length-at-most-12 binary words to compare the DFA's counter against direct pair enumeration. For every modulus \(2\le m\le17\), it builds the reachable automaton and performs partition-refinement minimization. For \(2\le m\le6\), it also explicitly constructs a distinguishing suffix for every unordered pair of different reachable states by the three-class argument and checks acceptance and rejection directly. Its recorded execution passed 8,191 word checks, 18,224 cumulative reachable state instances, and 14,381 explicit state-pair separators. These finite computations corroborate the proof but do not replace it.

Reproduce with `python3 verify_modular_pair_balance.py` using only the standard library.

## Relationship to prior work

Scattered-pair counts and their sum relation belong to standard Parikh-matrix theory; Proposition 2.2 of Poovanandran, Simpson and Teh states the general permutation-sum identity. The present theorem determines **minimal complete deterministic state complexity** for a modular *difference* of two oppositely ordered scattered pairs. Their 2021 work concerns counting and ambiguity for circular words, not this quotient problem. Grobler, Sabellek and Siebertz (2023) study automata enriched with semilinear constraints on infinite words; their machine-model and decision-problem results do not give this exact minimal finite-DFA count. Rauch and Holzer (2022) examine accepting-state complexity under operations on permutation automata, a different complexity measure.

The result also differs from published formulas for modular counts of a single scattered pattern such as \(0^j1\): taking the difference of opposite two-letter patterns changes the state invariant and creates a parity-dependent quotient, which does not follow from the single-pattern statement alone.

## Limitations

The theorem is only about binary words, one fixed modulus, the indicated pair-count difference and the zero residue. It does not determine syntactic monoids, nondeterministic state complexity, or optimal machines reporting the complete statistic rather than testing one residue. The finite checker is not a proof for all moduli. A literature comparison is not a guarantee that every equivalent result in unindexed work has been excluded. The result has received no independent audit.

## References

1. G. Poovanandran, J. Simpson, W. C. Teh, *Counting Subwords in Circular Words and Their Parikh Matrices*, arXiv:2110.14858v1 (28 October 2021), https://arxiv.org/abs/2110.14858 .
2. C. Rauch, M. Holzer, *On the Accepting State Complexity of Operations on Permutation Automata*, arXiv:2208.14731v1 (31 August 2022), https://arxiv.org/abs/2208.14731 .
3. M. Grobler, L. Sabellek, S. Siebertz, *Parikh Automata on Infinite Words*, arXiv:2301.08969v1 (21 January 2023), https://arxiv.org/abs/2301.08969 .
