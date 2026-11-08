# Quinary rank-two weight-isospectral codes: a complete projective-orbit classification

## Finding
Fix an integer \(n\ge 2\). Within the set of dimension-two linear codes in \(\mathbb F_5^n\) having a prescribed **Hamming weight enumerator**, the number of classes under \(\mathbb F_5\)-linear monomial equivalence depends only on the equality pattern of six recovered projective multiplicities. The eleven possible patterns have respectively \(1,1,1,1,1,1,1,2,2,3,6\) classes, as detailed below. Consequently the largest possible number of inequivalent codes with one weight enumerator is \(1\) for \(2\le n\le 5\), \(2\) for \(6\le n\le 9\), \(3\) for \(10\le n\le 14\), and \(6\) for \(n\ge15\).

The first ambiguity occurs at length \(6\). It comprises exactly two classes, sharing the weight enumerator \(1+8t^4+8t^5+8t^6\); their exact minimum Hamming distortion in the sense of Bennett--Fox--Morrell is \(36/25\).

## Assumptions and scope
A code is a two-dimensional \(\mathbb F_5\)-subspace of \(\mathbb F_5^n\). Two such codes are monomially equivalent if a coordinate permutation followed by independent nonzero coordinate scalings takes one code onto the other. No arbitrary symbol bijections are admitted. A weight enumerator is \(W_C(t)=\sum_{c\in C}t^{\mathrm{wt}(c)}\). Coordinates identically zero in the code are permitted, and the number of these coordinates is included in \(n\).

For a rank-two generator matrix, let \(z\) be its number of zero columns, \(N=n-z\), and let \(m_0,\ldots,m_5\) be the multiplicities of its six projective nonzero column directions in \(\mathbb P^1(\mathbb F_5)\). They are nonnegative integers summing to \(N\), with at least two positive entries. The **equality pattern** is the partition of \(6\) consisting of the counts of equal entries among these six integers. For example, \((2,2,2)\) means three different multiplicity values, each occurring twice; the multiplicity value zero is counted among the six entries. This is distinct from counting zero generator columns.

For a linear isomorphism \(T:C\to E\), its Hamming distortion is
\[
\mathcal D_T(C,E)=\frac{\max_{c\in C\setminus\{0\}}\mathrm{wt}(Tc)/\mathrm{wt}(c)}{\min_{c\in C\setminus\{0\}}\mathrm{wt}(Tc)/\mathrm{wt}(c)},\qquad \mathcal D(C,E)=\min_T \mathcal D_T(C,E).
\]
All denominators are positive because \(T\) is an isomorphism.

## Proof
**Recovering the multiplicity multiset.** The six one-dimensional subspaces of \(\mathbb F_5^2\) each contain four nonzero messages. The words from one such message direction vanish exactly at the generator columns perpendicular to it. As projective annihilation is a bijection between the six message directions and the six column directions, the six weights, each repeated four times, are precisely \(N-m_0,\ldots,N-m_5\). Therefore
\[
W_C(t)=1+4\sum_{i=0}^{5}t^{N-m_i}.
\]
Every nonzero column is evaluated nontrivially by exactly \(20\) of the \(25\) messages, so \(\sum_{c\in C}\mathrm{wt}(c)=20N\). Hence \(W_C\) determines \(N\), then \(z=n-N\), and then the unordered multiset \(\{m_0,\ldots,m_5\}\) with multiplicities. Conversely those data determine \(W_C\).

**Equivalence and the six-point action.** Changing the message basis acts on projective column directions as \(\operatorname{PGL}_2(5)\); independent column scalings and column permutations change neither the projective multiset nor its orbit. Conversely, a projective transformation matching two multiplicity functions lifts to a nonsingular row change, after which column permutations and scalings identify the generator matrices. This is the established projective-multiset correspondence. Consequently the number of inequivalent codes with a fixed spectrum is exactly the number of \(\operatorname{PGL}_2(5)\)-orbits of assignments of the six specified multiplicities to the six projective points. Rank two and zero columns are preserved.

**Cycle index and classification.** The group has order \(5(5^2-1)=120\). The cycle-type counts in its faithful action on the six projective points are
\[
\begin{array}{c|rrrrrrr}
\text{cycle type}&1^6&1^22^2&2^3&3^2&1^24&1\,5&6\\
\text{elements}&1&15&10&20&30&24&20.
\end{array}
\]
For proof of completeness: fixing two distinct points pointwise gives a cyclic group of order \(4\); there are \(\binom62=15\) unordered pairs, each supporting one split involution and two order-four elements, with unique fixed-point pairs. There are ten nonsplit cyclic tori of order \(6\), each containing one order-two, two order-three, and two order-six nonidentity elements, all acting without fixed points. Finally, each of the six projective points is the unique fixed point of four unipotent order-five elements. Together with the identity, this counts all \(120\) elements.

Thus the cycle-index polynomial is
\[
Z=\frac{X_1^6+15X_1^2X_2^2+10X_2^3+20X_3^2+30X_1^2X_4+24X_1X_5+20X_6}{120}.
\]
If the equality pattern is \(\lambda=(\lambda_1,\ldots,\lambda_s)\), then the requested orbit number is the coefficient of \(y_1^{\lambda_1}\cdots y_s^{\lambda_s}\) in \(Z\) after the substitution \(X_j=\sum_{i=1}^s y_i^j\). This is Burnside's lemma applied to assignments with the prescribed counts. Evaluating these eleven finite coefficients yields:

| Equality patterns \(\lambda\) | Number of classes |
|---|---:|
| \((6),(5,1),(4,2),(4,1,1),(3,3),(3,2,1),(3,1,1,1)\) | 1 each |
| \((2,2,2),(2,2,1,1)\) | 2 each |
| \((2,1,1,1,1)\) | 3 |
| \((1,1,1,1,1,1)\) | 6 |

The least sum of six **nonnegative** multiplicities with any given pattern is obtained by assigning \(0,1,\ldots,s-1\) to its \(s\) distinct values, with larger multiplicity counts paired with smaller values. Hence the first nonzero-column counts allowing respectively \(2\), \(3\), and \(6\) classes are \(6\), \(10\), and \(15\). All are attained by valid rank-two codes. Appending arbitrarily many identically-zero columns preserves the equality pattern and the number of classes, proving the all-length maximum formula. The cases below the first threshold have only one class, by the exhaustive equality-pattern table.

**Sharp first ambiguity and distortion.** Enumerate the projective directions as \(0,1,2,3,4,\infty\), represented by columns \((1,j)^{\mathsf T}\) for finite \(j\), and \((0,1)^{\mathsf T}\) for infinity. Use the multiplicity vectors
\[
 m^A=(0,0,1,1,2,2),\qquad m^B=(0,0,1,2,1,2).
\]
The corresponding six-column generators can be constructed by repeating each representative according to its entry. Each has weight enumerator \(1+8t^4+8t^5+8t^6\). The ninety arrangements of \(\{0,0,1,1,2,2\}\) split into two projective orbits of sizes \(60\) and \(30\), respectively, by their stabilizer sizes \(2\) and \(4\), independently verified by direct orbit enumeration. The coefficient calculation above establishes that these are the only two orbits. In particular, these two codes are not equivalent.

Any linear isomorphism between these codes permutes their six message directions. Since the two weight multisets agree, the six weight ratios have product \(1\). A nontrivial alignment necessarily has an increase and a decrease; its maximum ratio is at least \(6/5\) and its minimum ratio at most \(5/6\), because the only distinct possible weights are \(4,5,6\). Therefore the distortion is at least \((6/5)^2\). The projective permutation induced by \(j\mapsto 2j\) and fixing infinity sends the six source weights \((6,6,5,5,4,4)\) to target weights \((6,5,5,6,4,4)\), whose ratios are \((1,5/6,1,6/5,1,1)\). Its distortion is \(36/25\), proving equality.

## Verification
Run `python3 check.py` using Python 3 with no external dependencies. The program independently forms all \(120\) projective maps from nonsingular \(2\times2\) matrices over \(\mathbb F_5\), checks their cycle-type counts, exhaustively calculates all eleven orbit partitions in two ways (orbit decomposition and Burnside fixed-point counting), enumerates the \(25\) codewords of each six-column generator, determines the two orbit sizes, and exhaustively checks all \(120\) projective alignments using exact rational arithmetic for the distortion. It asserts each value and prints `ALL CHECKS PASSED` only after the checks succeed.

The finite checker is not substituted for the all-length argument: the all-length conclusion follows from the rank-two projective correspondence, the Burnside table, the minimum-sum argument, and zero-coordinate padding.

## Relationship to prior work
Dodunekov and Simonis established the general equivalence between full-length linear codes and projective multisets, and the link between projective weight functions and Hamming spectra. Their general framework supplies an essential premise, but the inspected article does not state the eleven quinary multiplicity-pattern orbit counts, the sharp length thresholds, or the distortion of the first pair.

Bouyukliev, Bouyuklieva, and Kurz give general algorithms and numerical classifications of linear codes; their numerical section concerns principally fields of cardinalities two, three, and four and does not give these quinary same-spectrum numbers. Bennett, Fox, and Morrell define and analyze code distortion with general approximation and exact enumeration algorithms; their inspected paper does not determine the present quinary rank-two isospectral classification or this first-pair distortion.

## Limitations
This classification is for dimension two over the **prime field of five elements** and Hamming weight spectra. It does not classify higher-dimensional codes, weight-distinct pairs, or inequivalence under nonlinear coordinate transformations. The novelty assessment is based on the inspected accessible works; unindexed projective-configuration literature may contain equivalent enumerations. The finite checker is independent of external scientific review, but the result has not undergone independent mathematical audit.

## References
1. H. Bennett, M. Fox, B. Morrell, *The Code Distortion Problem*, APPROX/RANDOM 2026, DOI: 10.4230/LIPIcs.APPROX/RANDOM.2026.24; earliest available arXiv version https://arxiv.org/abs/2607.26261 (2026-07-28).
2. S. Dodunekov, J. Simonis, *Codes and Projective Multisets*, Electronic Journal of Combinatorics 5 (1998), R37, https://doi.org/10.37236/1375.
3. I. Bouyukliev, S. Bouyuklieva, S. Kurz, *Computer classification of linear codes*, 2020, https://epub.uni-bayreuth.de/id/eprint/4618/.
