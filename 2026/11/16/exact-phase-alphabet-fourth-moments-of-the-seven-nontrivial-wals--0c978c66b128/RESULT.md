# Exact phase-alphabet fourth moments of the seven nontrivial Walsh characters

## Finding

Let \(G=\mathbb F_2^3\), with eight elements written as binary integers \(0,\ldots,7\), and let \(S=G\setminus\{0\}\). For a positive integer \(q\), let \(\mu_q=\{e^{2\pi i k/q}:0\le k<q\}\), and for \(a_s\in\mu_q\) define
\[
P_a(x)=\sum_{s\in S}a_s(-1)^{s\cdot x},\qquad
M_4(a)=\frac18\sum_{x\in G}|P_a(x)|^4.
\]
Here \(s\cdot x\) is the binary dot product. The sharp minima for the five alphabets \(q=2,3,4,5,6\), together with all minimizer counts modulo a common element of \(\mu_q\), are:

| Alphabet | Exact minimum of \(M_4\) | Normalized minimizers | \(\operatorname{GL}(3,2)\) orbit sizes |
|:--:|:--:|--:|:--|
| \(\mu_2\) | \(109\) | 56 | \(7,21,28\) |
| \(\mu_3\) | \(67\) | 168 | \(84,84\) |
| \(\mu_4\) | \(61\) | 224 | \(28,28,84,84\) |
| \(\mu_5\) | \(66-3\sqrt5\) | 336 | \(168,168\) |
| \(\mu_6\) | \(61\) | 2688 | sixteen orbits of size \(168\) |

Normalized means \(a_1=1\); this represents each scalar-phase class exactly once. The two fifth-root orbits are exchanged by complex conjugation. Representatives, giving the exponents of \((a_2,\ldots,a_7)\) with \(a_1=1\), are
\[
(0,1,1,2,4,2),\qquad (0,2,1,1,2,3).
\]
In particular, five-phase coefficients have a strictly smaller sharp fourth moment than either four- or six-phase coefficients:
\[
66-3\sqrt5<61.
\]
All minima, numbers of minimizers, and orbit sizes above are exact; no claim is made for continuous phases or alphabets outside these five orders.

## Assumptions and scope

Haar measure on the eight-point group \(G\) has total mass one; the Fourier characters are unnormalized signs. Every one of the seven nontrivial coefficients has modulus exactly one and belongs to the *same* specified root-of-unity alphabet. The zero-frequency coefficient vanishes. The theorem fixes this seven-character support and the exact finite alphabet set \(\{2,3,4,5,6\}\). Frequency labels \(1,2,4\) are the standard coordinate basis of \(G\); addition is bitwise XOR. In the orbit count the group acts by permuting the seven frequencies through invertible binary-linear coordinate changes, followed by scalar normalization.

## Proof

Write \(a_0=0\) and set the periodic autocorrelation
\[
C_h=\sum_{s\in G}a_{s+h}\overline{a_s}\qquad(h\in G).
\]
Fourier-character orthogonality, applied to the Fourier transform of \(|P_a|^2\), gives the exact identity
\[
M_4(a)=\sum_{h\in G}|C_h|^2.
\]
We have \(C_0=7\). Each nonzero \(h\) splits the six admissible ordered pairs into three unordered pairs, so, because \(G\) has exponent two,
\[
C_h=\sum_{\substack{1\le s<t\le7\\s\mathbin{\mathrm{xor}}t=h}}
2\operatorname{Re}(a_s\overline{a_t}),\qquad
M_4(a)=49+\sum_{h=1}^7 C_h^2.
\]
This formula is the exact reduction underlying the complete finite certificate. Multiplying every coefficient by the inverse of \(a_1\) preserves the moment, and there are exactly \(q^6\) normalized exponent vectors. The five exhaustive search sizes are \(64,729,4096,15625,46656\), totaling \(67170\).

For \(q=2,3,4,6\), the values of \(2\operatorname{Re}(e^{2\pi i k/q})\) as \(k\) runs from zero to \(q-1\) are respectively
\[
(2,-2),\quad (2,-1,-1),\quad (2,0,-2,0),\quad
(2,1,-1,-2,-1,1).
\]
Consequently every tested moment is an integer. For \(q=5\), the corresponding five values are
\[
2,\quad\frac{-1+\sqrt5}{2},\quad\frac{-1-\sqrt5}{2},
\quad\frac{-1-\sqrt5}{2},\quad\frac{-1+\sqrt5}{2}.
\]
Represent each autocorrelation as \(C_h=(A_h+B_h\sqrt5)/2\) with integers \(A_h,B_h\). Then
\[
4M_4=196+\sum_{h=1}^7(A_h^2+5B_h^2)
+2\sqrt5\sum_{h=1}^7 A_hB_h.
\]
Two values \(A+B\sqrt5\) are ordered exactly by signs and integer squared comparisons; no floating-point approximation is needed. The standalone code enumerates all normalized exponent vectors and updates the minimum and the complete minimizing set in this exact ordered ring. The resulting fifth-root certificate is \(4M_{4,\min}=264-12\sqrt5\).

The invertible linear maps on \(G\) are enumerated by the images of the basis \(1,2,4\): there are exactly \(7\cdot6\cdot4=168\) admissible choices. Applying each map to each minimum and normalizing its first coefficient partitions the minimizing set into disjoint orbits. The resulting orbit sizes are exactly those stated in the table. The Python certificate `verify_fano.py` implements these loops as standalone, terminating, exact-integer computations; hence its exhaustive comparisons and orbit partitions constitute finite proofs, not statistical evidence. It independently recomputes the moment at all eight Walsh sample points for every minimizer, checking the autocorrelation normalization and arithmetic by a second formula.

## Verification

Execute `python3 verify_fano.py` with standard-library Python 3.10 or newer. The complete run checks \(67170\) phase choices, independently recomputes all \(3472\) normalized minimizing moments at eight Walsh sample points each, and verifies five complete symmetry-orbit partitions. All assertions passed. The computational domain is finite and explicitly exhausted; there are no stochastic searches, numerical tolerances, external dependencies, or unverified solver outputs.

## Relationship to prior work

The work of Fan and Xu on Fourier transforms and bent functions on finite group actions provides the ambient Fourier and derivative viewpoint, but does not state a five-alphabet exact optimization for the seven nontrivial characters of \(\mathbb F_2^3\). Their earlier full-text study develops a general bentness characterization and is likewise not an extremizer census for this fixed punctured Walsh spectrum. Haemers and Parsaei Majd study *real* symmetric conference and Seidel matrices, rather than root-of-unity minimizers for this Fourier objective. A published sharp \(\Lambda(4)\) constant for a co-singleton spectrum concerns the *maximum* over unrestricted magnitudes, not the minimum with every coefficient modulus fixed. Related finite-alphabet results for planar square and hexagonal apertures have different additive character relations and do not imply the present seven-character minima.

The 2021 Fan–Xu journal article was available as publisher metadata and abstract, not full text, during this comparison; the earlier related Fan–Xu full preprint and the full open-access conference-matrix study were inspected. A historical-priority risk remains for specialized Walsh-array optimization or tabulations not found by these searches. No claim of independent priority verification is made.

## Limitations

The theorem does not optimize the unrestricted complex phase torus, optimize the peak rather than fourth moment, establish noise robustness, or extrapolate to other group orders and phase alphabets. It is an exact finite computation backed by a transparent complete arithmetic algorithm and a mathematical reduction; it is not a general asymptotic phase-design theorem. The orbit counts use only \(\operatorname{GL}(3,2)\) after scalar normalization, not a larger equivalence group. External historical completeness has not been independently verified.

## References

- Y. Fan and B. Xu, *Fourier transforms on finite group actions and bent functions*, *Journal of Algebraic Combinatorics* **55** (2022), 429–460, first published 22 September 2021, https://doi.org/10.1007/s10801-021-01057-3.
- Y. Fan and B. Xu, *Fourier Transforms and Bent Functions on Finite Abelian Group-Acted Sets*, arXiv:1406.1049, https://arxiv.org/abs/1406.1049 (earlier related background).
- W. H. Haemers and L. Parsaei Majd, *Spectral symmetry in conference matrices*, arXiv:2004.05829, https://arxiv.org/abs/2004.05829 (different real-matrix problem).
- Published mathematical record, *Sharp \(\Lambda(4)\) constant for the co-singleton spectrum of a finite abelian group*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-lambda-4-constant-for-the-co-singleton-spectrum-of-a-finit--dba95505302c (different extremal direction).
