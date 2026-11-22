# Sharp half-sampling ranks for the twelve-point Fourier transform

## Finding
For \(\zeta=e^{2\pi i/12}\), let \(F_{12}=(\zeta^{rc})_{r,c=0}^{11}\). Among the \(\binom{12}{6}^{2}=853{,}776\) ordered pairs of six-element row and column sets \((R,C)\), the exact complex ranks of \(F_{12}[R,C]\) have the distribution
\[
\begin{array}{c|rrrr}
\operatorname{rank}F_{12}[R,C]&3&4&5&6\\\hline
\#(R,C)&76&5{,}376&150{,}564&697{,}760.
\end{array}
\]
No lower ranks occur. The sharp rank-three pairs are **exactly** those for which one of \(R,C\) is the even or odd residue class in \(\mathbb Z_{12}\), and the other is a union of three of the six antipodal pairs \(\{j,j+6\}\), \(0\le j<6\). These 76 ordered pairs lose exactly three of the six independent Fourier sampling directions.

The structural mechanism is valid for every finite abelian group \(G\): for nonempty row set \(R\subset\widehat G\) and nonempty column set \(C\subset G\), the unnormalized Fourier restriction \(F_G[R,C]\) satisfies
\[
\operatorname{rank}F_G[R,C]\ge\frac{|R|\,|C|}{|G|}.
\]
Equality holds **if and only if** \(C\) is a union of cosets of the annihilator in \(G\) of the translation stabilizer \(H_R=\{\eta\in\widehat G:\eta R=R\}\). Equivalently, \(R\) is a union of cosets of the annihilator in \(\widehat G\) of the stabilizer of \(C\). Thus saturation is characterized by a dual periodicity condition, not merely by an existence witness.

## Assumptions and scope
The group \(G\) is finite abelian, \(\widehat G\) is its character group, and \(F_G=(\chi(x))_{\chi\in\widehat G,x\in G}\); multiplying all entries by \(|G|^{-1/2}\) does not change rank. All ranks are over \(\mathbb C\). A stabilizer is the *full* subgroup preserving a set, and \(H^{\perp}=\{x\in G:\eta(x)=1\ \forall\eta\in H\}\). The order-twelve table counts sets rather than their orderings, with the row and column roles distinguished. There are no frequency multiplicities or numerical rank tolerances.

## Proof
**1. Universal rank bound and equality criterion.** Put \(N=|G|\), let \(U=N^{-1/2}F_G\) be unitary, and let \(P_R,P_C\) be orthogonal coordinate projections. The nonzero singular values of \(P_RUP_C\) coincide with those of the normalized restricted matrix. Every singular value is at most one. Its squared Frobenius norm is \(|R||C|/N\), because each nonzero matrix entry has squared magnitude \(1/N\). Therefore rank is at least \(|R||C|/N\). Equality forces every nonzero singular value to equal one.

Write \(Q=UP_CU^*\), an orthogonal projection. The nonzero squared singular values of \(P_RUP_C\) are the eigenvalues of \(P_RQP_R\). This operator is a projection precisely when \(P_R\) and \(Q\) commute. For completeness, the projection identity gives
\[
P_RQP_R-(P_RQP_R)^2=P_RQ(I-P_R)QP_R
=\bigl((I-P_R)QP_R\bigr)^*\bigl((I-P_R)QP_R\bigr),
\]
so equality forces the off-diagonal block to vanish, and self-adjointness gives commutation. The converse is immediate.

The matrix entries of \(Q\) are
\[
Q_{\chi,\psi}=N^{-1}\sum_{x\in C}\chi(x)\overline{\psi(x)}
=N^{-1}\widehat{1_C}(\chi\psi^{-1}).
\]
Commutation says these entries vanish whenever \(\chi\in R\) and \(\psi\notin R\). The set of differences \(\chi\psi^{-1}\) for such pairs is exactly \(\widehat G\setminus H_R\): a difference is absent precisely when translating the complement of \(R\) by that difference preserves it, equivalently when it preserves \(R\). Thus equality is equivalent to \(\operatorname{supp}\widehat{1_C}\subseteq H_R\). By Fourier inversion this holds precisely when the indicator \(1_C\) is invariant under every translation in \(H_R^\perp\), i.e. when \(C\) is a union of its cosets. Interchanging the two projections proves the symmetric formulation.

**2. The order-twelve minimum and its 76 extremizers.** Take \(G=\mathbb Z_{12}\) with \(|R|=|C|=6\). The rank bound is three. If rank is three, the stabilizer \(H_R\) has order dividing \(|R|=6\), so it has order \(1,2,3\), or \(6\). The dual-period condition requires \(C\) to be a union of cosets of \(H_R^\perp\), whose size is \(12/|H_R|\). Since \(|C|=6\), its size must divide six. Hence \(|H_R|\) is either two or six.

If \(|H_R|=6\), \(R\) is one of the two parity classes, while \(H_R^\perp=\{0,6\}\); the other set \(C\) is any union of three antipodal pairs, giving \(2\binom63=40\) pairs. If \(|H_R|=2\), \(R\) is a union of three antipodal pairs but not one of the parity classes, giving \(\binom63-2=18\) choices; then \(H_R^\perp\) is the even subgroup, so \(C\) must be one of the two parity cosets, giving \(18\cdot2=36\) further pairs. The two cases are disjoint and total \(40+36=76\). This proves the exact extremal classification independently of computer enumeration.

**3. Exact higher-rank census.** Independent row and column translations preserve rank: they multiply the restricted columns and rows, respectively, by nonzero phases. Among the 924 six-element subsets of \(\mathbb Z_{12}\), there are 80 translation orbits. The attached integer certificate evaluates ranks for their \(80^2=6400\) representative pairs, weighting each by the product of its two orbit sizes.

To prove this computation determines **complex** rank rather than only modular rank, use the two distinct primes \(p_1=1{,}000{,}033\) and \(p_2=1{,}001{,}017\), with primitive 12th roots \(385966\) and \(72098\) modulo the respective primes. The certificate checks primality and primitivity and Gaussian-eliminates each restriction over both fields. Every representative pair has identical ranks over the two fields.

For any \(k\times k\) Fourier minor with \(1\le k\le6\), its determinant is an algebraic integer in \(\mathbb Q(\zeta)\), which has degree four. Each of its four Galois conjugates is a determinant of a unit-modulus matrix, and Hadamard's inequality bounds each absolute value by \(k^{k/2}\). Therefore the absolute norm of a nonzero determinant, a nonzero integer, is at most \(k^{2k}\le6^{12}=2{,}176{,}782{,}336\). Vanishing modulo each chosen prime forces this integer norm to be divisible by their product \(1{,}001{,}050{,}033{,}561\), exceeding the bound, so a determinant vanishing in both reductions must vanish over \(\mathbb C\). A modularly nonvanishing determinant cannot vanish over \(\mathbb C\). Consequently matching two-prime ranks are the exact complex ranks, by the rank-minor criterion.

Summing the weighted 6400 rank entries gives exactly \(76,5376,150564,697760\). The independent Python checker regenerates all translation orbits, recomputes both modular rank tests by a distinct elimination implementation, checks every weighted census entry, and independently recovers the rank-three classification by the subgroup-period criterion.

## Verification
Compile and run `verify_rank12.cpp` with a C++17 compiler, using `./verify_rank12 rank_orbits.csv`; the program writes the 6400-row certificate and prints `VERIFY_OK`. Then run `python3 verify_period12.py` beside the generated CSV. Both use integer arithmetic throughout. Their successful captured outputs are supplied as `check_cpp.txt` and `check_python.txt`. The CSV is the full representative-pair rank table. The modular rank check is logically exact only in conjunction with the cyclotomic norm argument above; mere agreement of two computations, without this bound, would not prove an infinite-field statement.

## Relationship to prior work
Classical Donoho–Stark uncertainty and Meshulam's divisor-interpolation theorem bound support sizes and describe subgroup equality witnesses; they do not give the rank of every restricted Fourier matrix. Delvaux and Van Barel construct low-rank Fourier submatrices and derive extremal Hamming-number profiles. Their documented subgroup-block constructions are closely related, and the possibility of an implicit derivation is a priority risk, but their inspected result does not state the sharp projection-commutation equivalence or the 76 labelled half-sampling pairs.

Earlier order-twelve full-spark classifications decide which row sets admit a singular maximal minor; fifth-order and fourth-order incidence tables count ranks at those *different sampling cardinalities*. The exact-support uncertainty profile for \(\mathbb Z_{12}\) determines support-size minima, not this half-sampling row/column rank incidence. A general-audience enumeration of zero Fourier minors records an aggregate count across *all sizes*, but does not distinguish rank-three, rank-four and rank-five order-six failures. None of these statements alone implies the exact six-by-six distribution or the sharp parity/antipodal equality classification.

## Limitations
The numeric full-rank histogram is specific to order twelve; the universal theorem classifies only restrictions saturating the stated lower bound, not all ranks for general groups. The finite certificate is reproducible but does not imply new results for arbitrary Fourier orders or numerical conditioning of the nonzero singular values. Earlier unindexed computations or implicit consequences of subgroup tiling theories are residual historical-priority risks. No independent mathematical audit is claimed.

## References
1. R. Meshulam, *An Uncertainty Inequality for Finite Abelian Groups*, arXiv:math/0312407v1, first publicly posted 2003-12-22; https://arxiv.org/abs/math/0312407.
2. S. Delvaux and M. Van Barel, *Rank-deficient Submatrices of Kronecker Products of Fourier Matrices*, KU Leuven Report TW477 (November 2006); *Linear Algebra and its Applications* 426 (2007), 349–367; https://citeseerx.ist.psu.edu/document?doi=8e34019b75494fa56d9b8791527fcaed304a7ff9&repid=rep1&type=pdf.
3. A. Bonami and S. Ghobber, *Equality Cases for the Uncertainty Principle in Finite Abelian Groups*, arXiv:1003.5060v1, first posted 2010-03-26; https://arxiv.org/abs/1003.5060.
4. *Complete fifth-order Fourier rank incidence on the twelve-cycle*, published mathematical record (2026-11-16); https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-complete-fifth-order-fourier-rank-incidence-on-the-twelve-cycle--db3ff8f3dd64.
5. *Complete full-spark classification for the order-12 DFT*, published mathematical record (2026-10-04); https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-complete-full-spark-classification-for-the-order-12-dft--81a97859d04e.
6. *Exact-support Fourier uncertainty profile on the cyclic group of order twelve*, published mathematical record (2026-10-04); https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-support-fourier-uncertainty-profile-on-the-cyclic-group-of--0b9ac16390cf.
7. *A prime leaves no room for a comb*, Matpic, https://www.matpic.com/essays/a-prime-leaves-no-room-for-a-comb/ (undated aggregate census; not a priority-date source).
