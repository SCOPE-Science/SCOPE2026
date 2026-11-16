# Sharp quadratic and cubic Walsh sampling spectra at the first Catalan-matroid tomography obstruction

## Finding
For the \(14\) Dyck paths of semilength four, let \(M_d\) denote the restriction of all Boolean Walsh characters of degree at most \(d\) to the length-eight up-step indicators. With the counting-measure normalization, the two sampling Gram matrices \(G_d=M_dM_d^{\mathsf T}\) have the following **complete** characteristic polynomials:
\[
\begin{aligned}
\det(zI-G_2)={}&z(z-12)^3(z-32)^3(z-52)(z-64)^3\\
&\qquad\cdot(z^3-142z^2+5576z-58112),\\[2pt]
\det(zI-G_3)={}&(z-64)(z-96)^3(z-104)\\
&\qquad\cdot(z^2-184z+8192)^3\\
&\qquad\cdot(z^3-294z^2+28528z-912896).
\end{aligned}
\]
The degree-two observation map has rank \(13\), with an explicitly generated one-dimensional kernel; degree three has full rank \(14\). Denote by \(\alpha\) the largest root of \(z^3-142z^2+5576z-58112\) and by \(\beta\) the largest root of \(z^3-294z^2+28528z-912896\). The sharp nonzero sampling singular-value condition numbers and optimal quotient/inverse bounds are
\[
\kappa_2=\sqrt{\alpha/12}\approx2.6400840186,\qquad
\kappa_3=\sqrt{\beta/64}\approx1.3344406198;
\quad \|M_2^{\dagger}\|_2=1/\sqrt{12},\quad\|M_3^{\dagger}\|_2=1/8.
\]
Here \(\dagger\) denotes the Moore--Penrose inverse and the norm is Euclidean. The first claim concerns stability only on the observable quotient; degree-two data cannot recover arbitrary distributions. These exact spectral polynomials and sharp constants, rather than the separately known Catalan enumeration or ordinary graded rank, are the finding.

## Assumptions and scope
Let \(\mathcal D_4\subset\{0,1\}^8\) consist of words \(w\) with exactly four ones, four zeros, and \(\sum_{i=1}^j(2w_i-1)\ge0\) for every \(1\le j\le8\). The one indicates an up-step; \(|\mathcal D_4|=\tfrac15\binom84=14\). For \(S\subseteq\{1,\ldots,8\}\), define \(\chi_S(w)=(-1)^{\sum_{i\in S}w_i}\). Rows of \(M_d\) are indexed by all \(w\in\mathcal D_4\), columns by **each** \(S\) with \(|S|\le d\), without normalizing the columns or dividing by the number of paths. Thus \(M_2\) has \(37\) columns and \(M_3\) has \(93\) columns. The dimensions and constants are for real Euclidean coefficient spaces under this precise normalization, not for an unspecified probability-normalized frame.

## Proof
**1. Exhaustive but exact finite input.** Generate every \(8\)-bit word having four ones; discard any word for which a prefix has more zeros than ones. This tests all \(\binom84=70\) candidates and leaves exactly \(14\). It constructs \(M_d\) from the defining formula, not from a data file or guessed numerical spectrum.

**2. Independent distance formulation.** If \(h=h(w,w')\) is Hamming distance, then summing characters over the support size gives
\[
G_d(w,w')=\sum_{k=0}^d K_k^{(8)}(h),\qquad
K_k^{(8)}(h)=\sum_{j=0}^k(-1)^j\binom hj\binom{8-h}{k-j},
\]
where binomial coefficients outside their natural range vanish. In particular
\[
G_2(w,w')=37-18h+2h^2,\quad
G_3(w,w')=37-18h+2h^2+\frac{(8-2h)^3-22(8-2h)}6.
\]
The distance expression follows by grouping Walsh characters according to how many of their supported coordinates differ between \(w\) and \(w'\). It provides a second independent construction of the same \(14\)-by-\(14\) integer matrices.

**3. Exact characteristic-polynomial certificate.** The supplied deterministic `verify_direct.py` forms every Walsh column and computes the symbolic integer characteristic polynomial \(\det(zI-G_d)\). The independently written `verify_distance.py` generates the words recursively, evaluates the Krawtchouk formula, and checks the same fully factored polynomials. Both also compute exact rational ranks. All matrices are fully determined by the explicitly stated finite definitions. The code performs exact integer/symbolic operations, not floating-point eigenvalue fitting; its complete, finite enumeration makes the certificate exhaustive for \(\mathcal D_4\).

**4. The single quadratic ambiguity.** For each \(t=(t_1,t_2,t_3)\in\{0,1\}^3\), form a Dyck word by an initial up-step, three length-two blocks equal to up-down when \(t_i=0\) and down-up when \(t_i=1\), and a final down-step. All eight are valid Dyck words. Give the resulting word coefficient \((-1)^{t_1+t_2+t_3}\), and give each of the other six words coefficient zero. For a character supported on at most two coordinates, at least one of the three disjoint blocks is untouched. Summing the signed eight terms over that block cancels, so this vector is in \(\ker(M_2^{\mathsf T})\). The single factor \(z\) in the computed characteristic polynomial proves that this nonzero vector spans **the entire** kernel. Its four positive and four negative entries, normalized separately, are two distinct probability laws with identical quadratic marginals. The absence of a zero factor for \(G_3\) proves cubic recovery for all signed measures.

**5. Sharp stability.** The cubic factor of \(G_2\) has one root in each of \((16,17)\), \((41,42)\), \((83,84)\); its other positive eigenvalues are \(12,32,52,64\), so the smallest nonzero eigenvalue is \(12\) and the largest is \(\alpha\). The quadratic factor of \(G_3\) has roots in \((75,76)\) and \((108,109)\), while its cubic has roots in \((80,81)\), \((99,100)\), \((113,114)\); its remaining eigenvalues are \(64,96,104\). Each interval sign change is checked over the integers, and its polynomial has exactly the displayed degree, certifying all real roots. Hence the minimum and maximum eigenvalues of \(G_3\) are \(64\) and \(\beta\), respectively. The singular values are square roots of the positive Gram eigenvalues, giving the asserted **sharp** constants by the spectral theorem.

## Verification
The complete reproducibility artifacts are `verify_direct.py` and `verify_distance.py`. Run `python3 verify_direct.py` and `python3 verify_distance.py` in an environment with Python 3 and SymPy. Their success markers are `DIRECT_DYCK_WALSH_SPECTRA_PASS` and `DISTANCE_DYCK_WALSH_SPECTRA_PASS`. Both were run successfully against the package contents. The first enumerates by binary masks and forms a literal Walsh matrix; the second uses recursive ballot-word generation and exact Krawtchouk distances. Both check the characteristic polynomials and ranks; the first also checks the explicit kernel, and the second certifies the exact real-root intervals. A separate check finds full degree-two rank for semilengths one, two and three, so semilength four is the first degree-two failure in this natural sequence. These are finite exhaustive checks; no extrapolation to larger semilengths is made.

## Relationship to prior work
Ardila established the Catalan matroid and the interpretation of Dyck up-step sets as its bases; that structure and the count \(14\) are pre-existing. Engström--Sanyal--Stump develop standard monomial complexes and related graded interpolation for lattice-path matroids, which is stronger prior coverage of **rank/hilbert-function** questions. A published analysis of Dyck-coordinate shattering supports likewise determines a different graded combinatorial invariant. None of the inspected materials supplies the two exact **counting-normalized Walsh Gram characteristic polynomials**, their full eigenvalue multiplicities or their sharp quadratic-versus-cubic conditioning constants. The present assertion is restricted to this spectral/stability refinement, not a claim of priority for the rank obstruction or for the elementary eight-term cube construction.

## Limitations
The result is exact only for the fourteen Dyck paths of semilength four. The polynomial factors are certified by reproducible finite symbolic calculation, rather than a closed-form all-semilength diagonalization. Other normalizations change the singular values. Rank and sampling-condition statements apply to **all** observations of each degree, with each frequency counted once, not to a selected minimal sampling subset. The novelty comparison is bounded to material actually inspected; alternative unpublished or unindexed exact eigenvalue tables may exist. There has been no independent external mathematical audit.

## References
1. F. Ardila, *The Catalan matroid*, arXiv:math/0209354, first public version 2002-09-25, https://arxiv.org/abs/math/0209354.
2. A. Engström, R. Sanyal and C. Stump, *Standard complexes of matroids and lattice paths*, arXiv:1911.12290, first public version 2019-11-27, https://arxiv.org/abs/1911.12290; Vietnam Journal of Mathematics, DOI:10.1007/s10013-021-00546-z.
3. *Strip-walk shattering polynomial of Catalan up-step concepts*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-strip-walk-shattering-polynomial-of-catalan-up-step-concepts--900e52ee307a. The cited result concerns shattering supports, not these Gram spectra.
