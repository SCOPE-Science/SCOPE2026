# Three visits sharply identify a stationary three-state Markov chain up to time reversal

## Finding
Let \((X_1,X_2,X_3)\) be three consecutive observations of an irreducible, time-homogeneous discrete-time Markov chain on the labelled set \(\{1,2,3\}\), started in its stationary distribution. Let \(C_i=\sum_{t=1}^{3}\mathbf 1\{X_t=i\}\), and suppose only the joint law of the unordered count vector \(C=(C_1,C_2,C_3)\) is known.

**Theorem.** That law determines the stationary distribution and the transition matrix \(P\) exactly up to its stationary time reversal \(P^*=D_\pi^{-1}P^{\mathsf T}D_\pi\). This includes irreducible chains with zero transition probabilities, including periodic and reversible cases. In particular, it determines every principal minor of \(P\) and of \(I-P\). Three visits are optimal: two consecutive stationary visits do not determine even the two-by-two principal minors for strictly positive three-state chains. For an irreducible two-state chain two visits suffice, while one does not.

## Assumptions and scope
The state labels are observed but **temporal order is discarded**. The entire probability distribution of the length-three count vector is available, not one realized count vector. Every state has positive stationary mass because \(P\) is irreducible; there is no assumption of reversibility, positivity of all entries, aperiodicity, spectral simplicity, or known stationary probabilities. The conclusion is structural identifiability of the probability law, not consistent estimation from one sample or numerical stability near a boundary.

Write \(\pi_i=\Pr(X_t=i)\), \(F_{ij}=\pi_iP_{ij}\), \(S_{ij}=F_{ij}+F_{ji}\) for distinct labels and \(J_{ij}=F_{ij}-F_{ji}\). For distinct \(i,j\), let \(b_{ij}=\Pr(C_i=2,C_j=1,C_k=0)\), with \(k\) the remaining label.

## Proof

**1. Stationary masses and loops.** By stationarity and linearity of expectation,
\[
\pi_i=\frac{\mathbb E C_i}{3}>0,\qquad
\Pr(C_i=3)=\pi_iP_{ii}^{2}.
\]
Consequently \(q_i=P_{ii}=\sqrt{\Pr(C_i=3)/\pi_i}\), with the **nonnegative** square root (including \(q_i=0\)).

**2. Symmetric stationary flows.** Row conservation and stationarity give \(\sum_{j\ne i}F_{ij}=\sum_{j\ne i}F_{ji}=\pi_i(1-q_i)\). Hence the three known row sums
\[
\sum_{j\ne i} S_{ij}=u_i,\qquad u_i=2\pi_i(1-q_i)
\]
determine all unordered pair flows:
\[
S_{ij}=\frac{u_i+u_j-u_k}{2}\quad(\{i,j,k\}=\{1,2,3\}).
\]

**3. Two-way transition products.** Exactly the paths \((i,i,j)\), \((i,j,i)\), and \((j,i,i)\) contribute to \(b_{ij}\), so
\[
b_{ij}=q_i(\pi_iP_{ij}+\pi_jP_{ji})+\pi_iP_{ij}P_{ji}
=q_iS_{ij}+\pi_iP_{ij}P_{ji}.
\]
Therefore each \(r_{ij}=P_{ij}P_{ji}\) is identified as
\[
r_{ij}=\frac{b_{ij}-q_iS_{ij}}{\pi_i}.
\]
The corresponding statistic \(b_{ji}\) gives the same \(r_{ij}\), an observable compatibility check.

**4. One circulation sign.** For each pair, \(F_{ij}F_{ji}=\pi_i\pi_jr_{ij}\), hence
\[
|J_{ij}|=\sqrt{S_{ij}^{2}-4\pi_i\pi_jr_{ij}}.
\]
The stationarity balances at all three vertices force
\[
J_{12}=J_{23}=J_{31}=:J.
\]
Thus their identified magnitudes coincide; the only possible unknown is a common sign. For either sign \(J=\pm |J_{12}|\), recover the two directional flows on the oriented cycle \(1\to2\to3\to1\):
\[
F_{ij}=\frac{S_{ij}+J}{2},\qquad F_{ji}=\frac{S_{ij}-J}{2},
\]
with \(F_{ii}=\pi_iq_i\), followed by \(P_{ij}=F_{ij}/\pi_i\). Replacing the sign replaces every \(F_{ij}\) with \(F_{ji}\), exactly the stationary reversal. A stationary path and the reversed path have identical unordered counts, so the stationary time-reversed chain has the same count law. These two options are genuine (and equal for \(J=0\)); no other irreducible chain has this count law. Finally, reversal acts by diagonal similarity of the transpose and therefore preserves all principal determinants of \(P\) and \(I-P\).

**5. Sharpness with positive chains.** For \(0\le\delta<1/4\), define
\[
P_\delta=\begin{pmatrix}
1/2&1/4+\delta&1/4-\delta\\
1/4-\delta&1/2&1/4+\delta\\
1/4+\delta&1/4-\delta&1/2
\end{pmatrix}.
\]
Every matrix is strictly positive and doubly stochastic, so \(\pi=(1/3,1/3,1/3)\). With two consecutive observations, each of the three count vectors concentrated at one label and each of the three vectors with one visit to each of two distinct labels has probability exactly \(1/6\), independent of \(\delta\). But each two-by-two principal minor of \(P_\delta\) equals
\[
\frac{3}{16}+\delta^2.
\]
For example, \(\delta=0\) and \(\delta=1/8\) have identical two-visit count laws and different principal minors, proving the sharp lower bound.

For two states, the one-visit law is merely \(\pi\) and cannot determine transition rates, whereas two-visit probabilities satisfy \(\Pr(C_i=2)=\pi_iP_{ii}\); therefore all entries follow from the row sums. This completes the theorem.

## Verification
The accompanying standalone `checker.py` enumerates every three-step path using exact rational arithmetic, reconstructs both transition candidates from the unordered count law, and verifies both reconstruction and reversal on a finite suite of symmetric and asymmetric stationary-flow matrices, including directed zero-loop and zero-edge cases. It also independently enumerates the two-visit counterexample at \(\delta=0\) and \(\delta=1/8\). The script reports `PASS: 1368 exact-rational assertions`. The proof above, rather than the finite checker, establishes the universal and boundary statements.

For direct reproduction, run `python3 checker.py` using only the Python 3 standard library.

## Relationship to prior work
Pemmasani (2026), Section 5, explicitly asks how many visits of a discrete Markov chain suffice for a stationary unordered count law to determine principal minors. Its principal theorems describe occupation **times** of continuous-time chains and equivalence classes under reversal; they do not give this sharp finite-visit answer for discrete three-state chains. The result here supplies an explicit inversion and a strict two-visit obstruction in the smallest dimension where nonzero stationary circulation is possible.

The paper *Occupancy distributions in Markov chains via Doeblin's ergodicity coefficient* (Chestnut and Lladser, 2010) concerns approximation of occupancy distributions rather than the inverse reconstruction from one count law. Classical time reversal of stationary Markov chains is used, not claimed as new. Related two-state count-only survey identifiability and binary spatial-window inversion results do not cover a fully observed, three-state, time-discarded trajectory or its circular current ambiguity. No uniqueness claim beyond the inspected literature is made.

## Limitations
This is a three-state result; no finite-visit threshold for general \(d\ge4\) is established. Identifiability is up to time reversal only, not orientation of irreversible flux. The theorem assumes the exact population distribution of the counts, a fixed stationary starting law, and a known labelled three-state space. Finite experiments support the formulas but do not replace the proof. Searches of accessible literature and published research records cannot exclude equivalent unindexed or unpublished results; independent external assessment has not been performed.

## References
1. A. Pemmasani, *What the occupation law of a finite Markov chain determines: time reversal and principal minors*, arXiv:2611.14587v1, 2026-11-10. https://arxiv.org/abs/2611.14587
2. S. Chestnut and M. Lladser, *Occupancy distributions in Markov chains via Doeblin's ergodicity coefficient*, arXiv:1003.2649, 2010. https://arxiv.org/abs/1003.2649
