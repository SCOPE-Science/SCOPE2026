# A sharp support gap and complete hexaphase cross-ambiguity spectrum on the five-cycle

## Finding

Write \(\xi=e^{2\pi i/6}\), \(\omega=e^{2\pi i/5}\), and let \(f,g:\mathbb Z/5\mathbb Z\to\{1,\xi,\ldots,\xi^5\}\). Their (unnormalized) cyclic cross-short-time Fourier transform is
\[
V_g f(x,k)=\sum_{t=0}^4 f(t)\overline{g(t-x)}\omega^{-kt},\qquad x,k\in\mathbb Z/5\mathbb Z.
\]
**Theorem.** Its support has cardinality in, and attains every member of, the set
\[
\boxed{\{5,19,20,21,22,23,24,25\}.}
\]
The following census is complete, with both signals normalized by \(f(0)=g(0)=1\), and therefore with exactly \(6^8=1,679,616\) ordered coefficient pairs. The second column counts normalized pairs; the final column is the sorted five-tuple of numbers of zero frequencies in each time-shift row (so \(0,0,1,1,4\) means exactly six zeros).

| Support cardinality | Normalized pairs | Sorted row-zero profile |
|---:|---:|:---|
| 5 | 1 | \((4,4,4,4,4)\) |
| 19 | 600 | \((0,0,1,1,4)\) |
| 20 | 120 | \((1,1,1,1,1)\) |
| 21 | 5,875 | \((0,0,0,0,4)\) |
| 22 | 1,200 | \((0,0,1,1,1)\) |
| 23 | 30,600 | \((0,0,0,1,1)\) |
| 24 | 322,200 | \((0,0,0,0,1)\) |
| 25 | 1,319,020 | \((0,0,0,0,0)\) |

In particular, **every pair except the unique normalized constant pair has at least 19 nonzero time-frequency coefficients**, and 19 is sharp. Exactly 600 normalized pairs attain 19. They are the translated-proportional pairs \(f(t)=\xi^c g(t-x_0)\) for which the window has exactly two vanishing off-origin cyclic autocorrelations (the exponents and scalar constrained by the two normalizations). There are exactly 120 normalized windows with this property. The support-20 pairs have exactly one constant signal and a zero-mean partner.

## Assumptions and scope

The group is the five-element cyclic group; every coefficient has magnitude one and is a sixth root of unity. The window and signal are ordered and may coincide. Global scalars in the sixth-root alphabet are divided out separately by setting their zeroth coefficients to one. No restriction on whether the sequences have fundamental period five is imposed; constant sequences are included. Fourier support means exact complex zeros, not floating-point near-zeros. There are 25 time-frequency locations. This theorem makes no assertion for arbitrary continuous phases, unequal magnitudes, longer cycles, or other alphabets.

## Proof

### 1. Cyclotomic row rigidity

For each shift \(x\), define the sixth-root sequence \(c_x(t)=f(t)\overline{g(t-x)}\). The extensions \(\mathbb Q(\xi,\omega)/\mathbb Q(\xi)\) have degree four since \(\gcd(5,6)=1\), so the minimal polynomial of \(\omega\) over \(\mathbb Q(\xi)\) is \(1+X+X^2+X^3+X^4\). Consequently, for every nonzero \(k\pmod5\),
\[
\sum_{t=0}^4c_x(t)\omega^{-kt}=0
\quad\Longleftrightarrow\quad
c_x(0)=c_x(1)=\cdots=c_x(4).
\]
When constant, that row contains exactly four zeros (all nonzero modulations), while its zero-modulation value has magnitude five. Otherwise, the row has either zero or one zero, the latter precisely when \(\sum_t c_x(t)=0\). Thus every row has zero count \(0,1,\) or \(4\); there is never a five-zero row.

A nonconstant window of prime period five can be proportional to a translate of the signal in at most one way, because two such shifts would give the window a nontrivial translational period. Consequently two four-zero rows are impossible unless both sequences are constant, in which case all five rows have four zeros.

### 2. Exact sixth-root zero-sum classification

Represent \(\xi\) by the relation \(\xi^2=\xi-1\). The coefficient-vector pairs for \(1,\xi,\ldots,\xi^5\) in the basis \(1,\xi\) are respectively
\[
(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1).
\]
Solving the two integer coordinate equations for five summands shows that zero occurs exactly for the six unordered exponent multisets
\[
\begin{gathered}
(0,0,2,3,4),\ (0,1,2,4,4),\ (0,1,3,3,5),\\
(0,2,2,4,5),\ (1,1,3,4,5),\ (1,2,3,5,5).
\end{gathered}
\]
Equivalently, each multiset comprises one equilateral triangle of roots and one opposite pair. Every such multiset has \(5!/2=60\) ordered realizations. The total number of zero-sum length-five sixth-root sequences is \(6\cdot60=360\), or exactly 60 after global scalar normalization.

### 3. Structural extremizers for the two exceptional support sizes

For \(g(0)=1\), put \(d_t=g(t)\overline{g(t-1)}\), so \(\prod_td_t=1\). If the lag-one autocorrelation vanishes, the five \(d_t\) have a zero-sum multiset. Only \((0,1,3,3,5)\) among the six listed multisets has product one. Its 60 permutations determine exactly 60 normalized windows, and the converse is immediate. By replacing lag one by lag two, one obtains another 60. These classes are disjoint: among five derivative exponents in \((0,1,3,3,5)\), precisely one is even. The five adjacent pair products \(d_td_{t-1}\) therefore have exactly two odd exponents, whereas every product-one zero-sum five-tuple needs four odd exponents. Hence lag two cannot vanish at the same time as lag one. There are exactly 120 normalized windows with one pair of vanishing off-origin autocorrelations, never all four.

If one shift is proportional, the associated row contributes four zeros and all other zeros are precisely those of the window autocorrelation. Thus 120 windows, each with five possible normalized relative shifts, produce exactly 600 support-19 pairs. The other \(5(6^4-1)-600=5,875\) nonconstant translated-proportional pairs have support 21. The constant pair alone has support 5.

If all five zero-frequency correlations vanish, their discrete Fourier transform gives \(\widehat f(k)\overline{\widehat g(k)}=0\) for every frequency. By the row-rigidity argument, a nonconstant sixth-root signal has nonzero Fourier transform at each of the four nonzero frequencies; hence one sequence must be constant, and the other must have zero mean. The 60 normalized zero-mean sequences occur in either order, yielding exactly 120 support-20 pairs.

### 4. Exhaustive certification of the remaining cases

The remaining zero-frequency correlation patterns are certified by two complete, separately implemented exact enumerations. Each ranges independently over the \(6^4=1,296\) possible normalized windows and the 1,296 possible normalized signals and examines all five shifts. The first checker uses the two-component ring \(\mathbb Z[\xi]\) and the row-rigidity lemma, classifying each row by its Eisenstein zero sum and its constant-coefficient status.

The second checker evaluates **all 25 Fourier coefficients directly**, without using that lemma to decide zeros. With \(Z=e^{2\pi i/30}\), it computes coefficient sums \(\sum_tZ^{5e_t-6kt}\) in the exact free integer basis \(1,Z,\ldots,Z^7\), reducing every exponent via
\[
\Phi_{30}(Z)=Z^8+Z^7-Z^5-Z^4-Z^3+Z+1=0.
\]
A coefficient is zero exactly when all eight reduced integer coordinates are zero. This is valid because \(\Phi_{30}\) is the degree-eight minimal polynomial of \(Z\). Both independent tables return the eight rows of the theorem identically, with counts summing to \(1,679,616\), and exactly the stated eight sorted profiles. Thus the finite enumeration is exhaustive and mathematically exact, rather than a sampling experiment.

## Verification

From the directory containing the two attached standalone source files, execute

```sh
g++ -std=c++17 -O2 -Wall -Wextra verify_structural.cpp -o verify_structural
./verify_structural
g++ -std=c++17 -O2 -Wall -Wextra verify_spectrum.cpp -o verify_spectrum
./verify_spectrum
```

Each program has literal expected tables for all eight support sizes and all eight profiles, prints a `PASS` message only after verifying each integer count, and exits nonzero on a discrepancy. The second program checks each formal Fourier coefficient in \(\mathbb Z[Z]/(\Phi_{30})\) and does not rely on numerical complex comparisons. The first program additionally emits explicit witness pairs for every possible support category. The computations were executed on the source files included here.

## Relationship to prior work

Fabio Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1 (public April 29, 2022), proves the general lower bound \(|\operatorname{supp}V_gf|\ge N\) and classifies equality by subgroup-coset phase-space supports and chirps. For \(N=5\), this explains the extreme support-five boundary but **does not determine** the nonextremal 19–25 values, hexaphase row profiles, or their multiplicities. The present theorem identifies that additional phase-alphabet structure.

Lam and Leung, *On vanishing sums of roots of unity* (2000), establish the general admissible lengths of zero sums of root-of-unity alphabets. Here the five-term sixth-root case is proved directly and then combined with all-shift compatibility; the length criterion alone does not give an STFT support census. Other work on cyclic Gabor uncertainty, composite-alphabet Gabor lifting ranks, and phase-only ambiguity support gaps concerns different objects or weaker bounds. Specialized historical polyphase sequence tables have not all been eliminated as a priority risk.

## Limitations

The exact support classification is for ordered, full-length sixth-root pairs on the five-cycle only. It is not a classification of individual coefficient-pair symmetry orbits beyond the two exceptional structural cases explained above. The zero-sum and cyclotomic lemmas are exact, and the finite global census is a reproducible exhaustive computation, not a universal prime-order theorem. No noise tolerance, near-zero numerical conditioning, or non-sixth-root extension is established. Historical novelty is provisional pending independent literature audit.

## References

1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1, April 29, 2022, https://arxiv.org/abs/2204.14176, subsequently J. Funct. Anal. 284 (2023), article 109924, https://doi.org/10.1016/j.jfa.2023.109924.
2. T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*, J. Algebra 224 (2000), 91–109, https://doi.org/10.1006/jabr.1999.8089.
3. The two exact-reproducibility source files `verify_structural.cpp` and `verify_spectrum.cpp` attached to this result.
