# The sharp fourteen-point ambiguity of least-period mean and variance

## Finding

For a permutation \(f\) of \(M\) points, choose an initial point uniformly and let \(P_f\) be its **least positive period**. Denote its mean and variance by \(\mu(f)=\mathbb E[P_f]\) and \(v(f)=\operatorname{Var}(P_f)\).

**Theorem (sharp fixed-cardinality identifiability).** For every fixed \(1\le M\le13\), the pair \((\mu(f),v(f))\) determines the permutation up to topological conjugacy. For \(M=14\), there is exactly one unordered pair of distinct permutation conjugacy classes with identical mean and variance: those with disjoint least-period supports and cycle partitions

\[
(7,4,3)\quad\text{and}\quad(6,6,1,1).
\]

Their common moment pair is

\[
\boxed{\mu=\frac{37}{7},\qquad v=\frac{150}{49}.}
\]

For **every** \(M\ge14\), the moment pair fails to distinguish all cycle types, as the two counterexamples extend by adjoining \(M-14\) fixed points. In particular, two finite dynamical systems can have exactly the same first two least-period moments despite having no least period in common.

## Assumptions and scope

The phase space is a finite discrete set, the dynamics is a permutation, and the sampling measure is uniform on points. Two such finite systems are topologically conjugate if and only if their multisets of cycle lengths agree. The comparison is **at a fixed size** \(M\). No assumption about a Markov partition or mixing is needed.

Write \(\lambda=(\lambda_1,\ldots,\lambda_r)\) for the cycle lengths, which form an integer partition of \(M\). The probability of observing a cycle of length \(j\) equals \(j\) times its number of cycles, divided by \(M\). Set \(S_k(\lambda)=\sum_{i=1}^r\lambda_i^k\). Direct summation yields

\[
\mu=\frac{S_2}{M},\qquad
v=\frac{S_3}{M}-\left(\frac{S_2}{M}\right)^2.
\]

This is a natural coarse observational summary of the least-period sets and period-count sequences studied in [1,2]. The two formulas themselves are elementary identities, not asserted as new results.

## Proof

**Moment-equivalence reduction.** For two permutations on the same \(M\)-point space, their means coincide exactly when their squared cycle-length sums \(S_2\) coincide. Given equality of \(S_2\), their variances coincide exactly when their cubed cycle-length sums \(S_3\) coincide. Thus, the desired inverse problem is the collision problem for the map

\[
\lambda\longmapsto(S_2(\lambda),S_3(\lambda))
\]

on integer partitions of each fixed \(M\).

**Finite exhaustive recurrence.** Let \(C_k(m,u,v)\) be the number of partitions of \(m\) with parts at most \(k\) whose squared and cubed part sums are respectively \(u\) and \(v\). Set \(C_0(0,0,0)=1\), with all other base or negative-index entries zero. A partition either has no part equal to \(k\), or deleting one part equal to \(k\) leaves a partition again using parts at most \(k\). These disjoint possibilities give

\[
\boxed{C_k(m,u,v)=C_{k-1}(m,u,v)+C_k(m-k,u-k^2,v-k^3).}
\]

Induction on \(k\) and \(m\) proves that this recurrence counts every partition exactly once. The finite computation for \(m\le14\) is therefore exhaustive, not random testing. The included standalone `verify.py` evaluates every integer coefficient independently by this recurrence and a distinct direct descending-part enumeration. Both methods produce the following complete fiber counts:

| \(M\) | Partitions | Distinct moment signatures | Colliding signature fibers |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 2 | 2 | 0 |
| 3 | 3 | 3 | 0 |
| 4 | 5 | 5 | 0 |
| 5 | 7 | 7 | 0 |
| 6 | 11 | 11 | 0 |
| 7 | 15 | 15 | 0 |
| 8 | 22 | 22 | 0 |
| 9 | 30 | 30 | 0 |
| 10 | 42 | 42 | 0 |
| 11 | 56 | 56 | 0 |
| 12 | 77 | 77 | 0 |
| 13 | 101 | 101 | 0 |
| 14 | 135 | 134 | 1 |

At \(M=14\), the sole nonsingleton signature is \((S_2,S_3)=(74,434)\), and it has precisely the two stated cycle partitions. They satisfy

\[
7^2+4^2+3^2=6^2+6^2+1^2+1^2=74,
\]

\[
7^3+4^3+3^3=6^3+6^3+1^3+1^3=434.
\]

Thus \(\mu=74/14=37/7\) and \(v=434/14-(74/14)^2=150/49\). The cycle-length supports \(\{3,4,7\}\) and \(\{1,6\}\) are disjoint. The exhaustive recurrence proves minimality and uniqueness.

**All larger sizes.** Appending \(M-14\) singleton cycles to both types yields distinct cycle partitions satisfying

\[
S_2=74+(M-14)=M+60,\qquad S_3=434+(M-14)=M+420
\]

for every integer \(M\ge14\). The moment formulas then agree identically, while the presence of a \(7\)-cycle in one system and a \(6\)-cycle in the other prevents conjugacy. This infinite extension is proved symbolically, not inferred from a finite test. \(\square\)

## Verification

Run `python3 verify.py` after extracting the included checker. The script computes all signature multiplicities using exact integer arithmetic, independently enumerates all partitions through \(14\), compares every dictionary entry, isolates the unique collision, and checks the rational moment values. Its finite checks are exhaustive; the separate symbolic argument proves every larger-cardinality claim.

## Relationship to prior work

De Jong [1], first publicly available in October 2025, studies the set of least periods of orbits, with realization and classification results for finitely presented dynamical systems. Byszewski, Graff and Ward [2] study the complete periodic-point count sequence and its dynamical realizability. Both provide richer period data than the two moment statistics of a point sampled uniformly from a finite system.

Neither the least-period-set classification in [1] nor the full count-sequence theory in [2] implies that **just two moments** determine every finite permutation through thirteen points, lose injectivity uniquely at fourteen points, and thereafter fail at every size. The present theorem pinpoints the first loss of information from compressing orbit-length data to mean and variance. The existence of least-period sets and the basic moment identities are not claimed as discoveries.

## Limitations

This theorem concerns same-cardinality comparisons of uniformly sampled finite permutations, not pairs of systems with different numbers of points, nonuniform invariant measures, infinite systems, or noninvertible maps. For \(M>14\), it shows noninjectivity but does not classify all collisions. The finite certificate is exhaustive for the stated cutoff, though independent external mathematical validation remains unperformed. Potential older combinatorial work on partition power-sum collisions is a historical-priority risk.

## References

[1] H. de Jong, *On Sets of Periodic Orbit Lengths in Finitely Presented Dynamical Systems*, arXiv:2510.10848v1, first posted 12 October 2025; Ergodic Theory and Dynamical Systems 46 (2026), 2452–2484. https://arxiv.org/abs/2510.10848 ; https://doi.org/10.1017/etds.2026.10313 .

[2] J. Byszewski, G. Graff and T. Ward, *Dold sequences, periodic points, and dynamics*, Bulletin of the London Mathematical Society 53 (2021), 1263–1298, DOI:10.1112/blms.12531. https://doi.org/10.1112/blms.12531 .
