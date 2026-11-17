# Sharp three-basis support uncertainty for the standard MUBs of dimension five

## Finding
Let \(\mathcal B_\infty,\mathcal B_0,\ldots,\mathcal B_4\) be the standard complete set of six mutually unbiased bases of \(\mathbb C^5\), consisting of the coordinate basis and five quadratic finite-field Fourier bases. For every triple of distinct bases, the sharp total-support inequality is
\[
\min_{v\in\mathbb C^5\setminus\{0\}}\sum_{\mathcal B\text{ in the triple}}|\operatorname{supp}_{\mathcal B}(v)|=10.
\]
Equivalently, any nonzero state has at most five zero amplitude coordinates across the selected three bases, and equality is achievable for every triple. This is an exact dimension-five theorem, not an arbitrary-prime assertion.

## Definitions and normalization
Put \(\omega=e^{2\pi i/5}\). The coordinate basis \(\mathcal B_\infty\) comprises \(\delta_t\), \(t\in\mathbb F_5\); for \(a\in\mathbb F_5\), let
\[
\phi_{a,b}(t)=5^{-1/2}\omega^{at^2+bt},\qquad b,t\in\mathbb F_5.
\]
These six bases are mutually unbiased by the quadratic Gauss-sum identity. Support counts the number of nonzero complex inner-product coefficients, irrespective of amplitude normalization. The state coefficients are unrestricted complex numbers.

## Proof
Each zero coordinate is a homogeneous linear constraint on the five-dimensional state. In the basis \(\mathcal B_a\) its row, up to complex conjugation of the exponents and a nonzero scale, is \((\omega^{at^2+bt})_{t\in\mathbb F_5}\); the coordinate basis contributes standard unit rows. If at least six of fifteen outcomes vanished, a selection of six analysis rows would have rank at most four.

To prove this impossible, specialize cyclotomic integers by the ring homomorphism \(\mathbb Z[\omega]\longrightarrow\mathbb F_{101}\) given by \(\omega\mapsto95\), whose image has exact multiplicative order five. For each of the \(\binom63=20\) basis triples and each of the \(\binom{15}{6}=5005\) six-row subsets, perform exact modular Gaussian elimination. The accompanying original `CHECK.cpp` implements this computation; an independently implemented modular rank checker also enumerated all \(20\cdot5005=100100\) cases without a deficient rank. A maximal minor nonzero modulo 101 was nonzero as a cyclotomic integer over \(\mathbb C\). Therefore every selection of six rows has rank five, and no nonzero state has six vanishing outcomes. Total support is at least \(15-5=10\).

To establish sharpness for every triple, the finite-field Fourier transform and multiplication by chirps \(D_c:v(t)\mapsto\omega^{ct^2}v(t)\) permute these six bases; their action is transitive on the basis labels. Move one chosen basis to the coordinate basis, with the other two distinct quadratic bases. Set \(v=\delta_0-\delta_1\). It has three coordinate zeros, and its analysis coefficients in every quadratic basis are proportional to \(1-\omega^{-(a+b)}\), which has exactly one zero in \(b\). The three supports are \((2,4,4)\), sum ten. Unitary transport gives an extremizer for every original triple.

This finite exact rank certificate proves exactly the dimension-five statement. It is not a computation of all complex equality rays, a stability inequality, or an infinite-prime proof.

## Verification
Compile the original accompanying `CHECK.cpp` with a C++17 compiler; the `p=5` branch computes all 100100 ranks, with `CHECK_OK p=5 modulus=101 root=95 triples=20 rank_certificates=100100`. An independently authored C++ Gaussian elimination using the same finite field and independently assembled matrices reproduced this count. The original source also computes a dimension-seven certificate, but that extra historical computation is not asserted here as novel mathematics.

## Relationship to prior work and limited novelty
Fiorentino and Weigert, *Uncertainty relations for the support of quantum states*, J. Phys. A 55 (2022), 495305, arXiv:2209.09817, prove the pairwise support inequalities, discuss the triple lower bound \(3(p+1)/2\), and analyze complete \(p+1\)-basis support. Their prime-five complete-family sharp bound does not imply this exact arbitrary-three-basis value.

The earlier published *A sharp three-basis support law for the seven-point Fourier and quadratic-chirp transforms*, https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-a-sharp-three-basis-support-law-for-the-seven-point-fourier-and--22c716053510, establishes the seven-dimensional fixed-triple support bound fourteen. Its theorem, combined with the fact that the projective \(SL_2(\mathbb F_7)\) action on the eight standard MUB labels is transitive on unordered triples, already gives the all-triple dimension-seven corollary. Consequently, the seven-dimensional part of the original combined five-and-seven assertion is **not** presented here as new. The surviving new statement is exclusively the exact arbitrary-triple theorem in dimension five; the two PSL2(5) triple orbits are both checked by the finite certificate.

Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030, treats complete-MUB/parabola support conditions, not this five-dimensional arbitrary-triple classification. Unindexed equivalent computations remain a historical-priority risk.

## Limitations
Only standard finite-field MUBs of dimension five are considered; arbitrary unrelated Hadamard triples need not satisfy this result. The proof relies on exact exhaustive modular rank checks. The theorem neither determines all equality rays nor gives an approximate-sparsity inequality. Earlier dimension-seven work is explicitly credited; no independent verification or formal proof is claimed by this public scientific statement.
