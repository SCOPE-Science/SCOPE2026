# Exact affine-geometry failure probabilities for four-column Hadamard sketches

## Finding

Fix an integer \(d\ge3\), let \(N=2^d\), and let \(H_N\) denote the normalized real Walsh–Hadamard matrix with rows and columns indexed by \(\mathbb F_2^d\):
\[
(H_N)_{t,j}=N^{-1/2}(-1)^{t\cdot j}.
\]
Draw a subset \(I\subset\mathbb F_2^d\) uniformly among all \(m\)-subsets, where \(4\le m\le N\). Let \(R_I\) extract precisely those rows, in any order, let \(D\) be any diagonal sign matrix, and set \(S=\sqrt{N/m}\,R_IH_ND\). For a four-element coordinate index set \(T=\{j_1,j_2,j_3,j_4\}\), let \(U_T\) contain the corresponding four standard unit vectors and define
\[
q_T(N,m)=\Pr\bigl(\operatorname{rank}(SU_T)<4\bigr).
\]
Adopt the convention \(\binom rm=0\) when \(m>r\) or \(m<0\). There are **exactly two** rank-failure laws, distinguished by one affine invariant.

**Affine-plane column set.** If \(j_1+j_2+j_3+j_4=0\) in \(\mathbb F_2^d\), equivalently if the four columns form an affine two-plane, then
\[
\boxed{q_T(N,m)=\frac{4\binom{3N/4}{m}-6\binom{N/2}{m}+4\binom{N/4}{m}}{\binom Nm}.}
\]

**Affine-independent column set.** If \(j_1+j_2+j_3+j_4\ne0\), then
\[
\boxed{q_T(N,m)=\frac{12\binom{N/2}{m}+8\binom{3N/8}{m}-68\binom{N/4}{m}+72\binom{N/8}{m}}{\binom Nm}.}
\]

Both column classes have exactly the same leverage profile \(4/N\) at every row before subsampling. Nevertheless, at \(N=8\), \(m=4\), their singularity probabilities are \(27/35\) and \(6/35\), respectively, a ratio of \(9/2\). Moreover, for powers of two \(N\to\infty\) with \(m\to\infty\) and \(m^2/N\to0\),
\[
q_{\mathrm{plane}}(N,m)\sim4(3/4)^m,\qquad
q_{\mathrm{indep}}(N,m)\sim12(1/2)^m,\qquad
\frac{q_{\mathrm{plane}}}{q_{\mathrm{indep}}}\sim\frac13(3/2)^m.
\]
Thus equally incoherent four-dimensional coordinate subspaces can have exponentially different probabilities of exact rank failure under uniform row-subsampled Hadamard sketches.

## Assumptions and scope

All additions and dot products in the four-index criterion are over \(\mathbb F_2\), while matrix ranks are over \(\mathbb R\). The four column indices are distinct. Sampling is **uniform without replacement**; duplicated rows are excluded. Any order of sampled rows and any diagonal signs, including the usual independently chosen Rademacher signs, give the same rank event. The event is loss of algebraic rank, not a condition-number threshold or a norm-distortion event. The matrix \(U_T\) has orthonormal columns. The normalization \(\sqrt{N/m}\) does not affect rank. The sample size includes the endpoints \(m=4\) and \(m=N\).

## Proof

**1. Affine reduction and leverage equality.** Multiplying the four selected columns by the nonzero signs from \(D\), or multiplying each sampled row by a nonzero sign, preserves rank. Translate the four frequencies so the first is zero; the common character factor is a nonzero row multiplier. A linear automorphism of \(\mathbb F_2^d\), dualized on the row index, permutes the rows. Consequently the multiset of row types depends only on the affine span of \(T\). Four distinct points in characteristic two have affine dimension two exactly when their sum vanishes; otherwise their affine dimension is three. The two canonical frequency sets are \(\{0,e_1,e_2,e_1+e_2\}\) and \(\{0,e_1,e_2,e_3\}\). Every row of \(H_NDU_T\) has four entries of magnitude \(N^{-1/2}\), hence squared leverage \(4/N\) in both families.

**2. Plane case: complete occupancy.** Write \(x,y\in\{-1,1\}\) for the evaluations of the first two independent characters. The four-column row is, up to nonzero scaling, \((1,x,y,xy)\). Each of its four possible types occurs exactly \(N/4\) times among the \(N\) rows. The resulting four distinct row types form an invertible order-four Walsh matrix; any proper subset spans fewer than four dimensions. Thus the sample has full rank if and only if it meets each of the four types. Applying inclusion–exclusion to the event that at least one type is entirely missed gives
\[
\Pr(\operatorname{rank}<4)
=\frac{\sum_{k=1}^{4}(-1)^{k+1}\binom4k\binom{N-kN/4}{m}}{\binom Nm},
\]
which reduces to the first displayed formula. The term for missing all four types vanishes because \(m\ge4\).

**3. Independent case: cube coplanarity.** The eight row types now have the form \((1,x,y,z)\), for the eight vertices \((x,y,z)\in\{-1,1\}^3\), each repeated exactly \(N/8\) times. The rank of the sampled matrix equals one plus the affine dimension of the distinct cube vertices observed. Any three distinct cube vertices are noncollinear. Four vertices are affinely dependent precisely when they lie in a plane. There are exactly twelve coplanar four-vertex subsets: six square faces \(x=\pm1,y=\pm1,z=\pm1\) and six diagonal rectangles \(x=\pm y,x=\pm z,y=\pm z\).

For completeness, suppose four distinct cube vertices lie in a plane. If any two are adjacent in the cube graph, subtracting their plane equations shows that the coefficient of the coordinate on which they differ is zero. The plane is then a product of a line intersecting a two-dimensional square in two vertices with the free sign of the remaining coordinate. Such a line containing two square vertices is either a boundary edge or a diagonal, giving exactly the twelve named planes. If there is no adjacent pair, the four vertices form a maximum independent set in the cube graph. The only independent four-sets are the two parity tetrahedra; each yields a nonsingular \(4\times4\) matrix with rows \((1,x,y,z)\), so neither is coplanar. This proves the classification without relying on numerical enumeration.

**4. Counting exact observed supports.** Denote the common multiplicity of each cube type by \(h=N/8\). For a **fixed** set of \(r\) cube types, the number of \(m\)-subsets of underlying rows whose set of observed types is exactly that set equals
\[
a_r=\sum_{k=1}^{r}(-1)^{r-k}\binom rk\binom{kh}{m}.
\]
This is inclusion–exclusion on missing types. The numbers of rank-deficient type supports of sizes \(1,2,3,4\) are \(8,28,56,12\), respectively; no support with at least five types can have affine dimension below three. Hence the number of failing row samples is
\[
8a_1+28a_2+56a_3+12a_4
=72\binom h m-68\binom{2h}m+8\binom{3h}m+12\binom{4h}m.
\]
Divide by \(\binom Nm\) and substitute \(h=N/8\). This is exactly the second claimed formula, including all endpoint sample sizes.

**5. Exact separation and asymptotics.** At \(N=8\), \(m=4\), the plane count is \(54\) of the \(70\) four-row choices while the independent count is \(12\) of \(70\). The exact ratio is therefore \(54/12=9/2\). For any fixed \(0<\alpha<1\), the elementary product formula gives, when \(m^2/N\to0\),
\[
\frac{\binom{\alpha N}{m}}{\binom Nm}
=\prod_{k=0}^{m-1}\frac{\alpha N-k}{N-k}
=\alpha^m\exp\bigl(O(m^2/N)\bigr).
\]
In the first exact formula the leading base is \(3/4\), and in the second it is \(1/2\); all other terms have strictly smaller exponential bases. The three asserted asymptotic equivalents follow. This proves the complete claim.

## Verification

The standalone Python 3 checker `verify.py` uses only exact integer arithmetic. It constructs Walsh rows and computes ranks modulo the prime \(101\). This equals rational rank for matrices with four sign columns: every nonzero \(4\times4\) minor is an integer with absolute value at most \(16\) (by the Hadamard determinant bound), so reduction modulo \(101\) cannot turn a nonzero maximal minor into zero. For \(N=8\), it exhausts all \(70\) four-column index sets and every row-sampling size from four through eight. For \(N=16\), it exhausts every row subset for one representative of each affine class. It also counts all \(12\) coplanar cube quadruples directly and checks the exact benchmark. The saved output in `verify_output.txt` ends with `PASSED 450 assertions`.

These finite checks corroborate rather than replace the proof in arbitrary dimensions and arbitrary admissible sample sizes.

## Relationship to prior work

Tropp, *Improved analysis of the subsampled randomized Hadamard transform* (arXiv:1011.1595), constructs the same kind of randomized orthogonal sketch and proves a high-probability subspace-embedding bound via matrix concentration. That general sufficient bound does not state the exact rank-failure probability for each affine orbit of four coordinate columns. Balabanov, Beaupère, Grigori and Lederer (arXiv:2210.11295, first submitted 20 October 2022) explicitly define the classical with- or without-replacement SRHT in their Section 2, then study **block** SRHT oblivious-embedding guarantees. Neither formula nor the leverage-identical comparison appears in the inspected relevant statements and proofs.

Ipsen and Wentworth (arXiv:1203.4809) establish general rank/conditioning bounds for uniform row sampling in terms of coherence and leverage scores. Their accessible abstract gives a **bound**, not the present class-specific exact probability; the complete text was not accessible for an exhaustive comparison. The earlier Huckle–Kravvaritis study of Sylvester-Hadamard submatrices addresses spectra of leading principal submatrices, not random four-column row-restriction success, according to its accessible abstract; full text was not inspected.

Two related published finite-Walsh results concern, respectively, exact Fourier support sizes of functions with four **nonzero** coefficients and the number of orthogonal eight-column spectra on eight-point subsets of the Boolean four-cube. Neither assertion determines the sampled four-column rank-failure distribution. In particular, the plane and diagonal rank dependencies in the present cube arise from null vectors with zero entries, so the exact-support-four theorem does not directly cover the counting problem. A general singular-minor classification in specialist literature remains a possible publication-precedence risk.

## Limitations

The classification concerns **exact** rank loss, not small singular values, finite-precision numerical rank, least-squares error, or embedding distortion for arbitrary subspaces. It assumes four distinct coordinate columns, uniformly selected distinct Walsh rows, and a power-of-two ambient size. The asymptotic separation additionally assumes \(m^2/N\to0\). The result has not received independent specialist audit. Existing literature may contain an equivalent counting formulation under another terminology; nonidentification in the checked sources alone is not proof of publication novelty.

## References

1. J. A. Tropp, *Improved analysis of the subsampled randomized Hadamard transform*, arXiv:1011.1595; https://arxiv.org/abs/1011.1595 (first public version, November 2010).
2. O. Balabanov, M. Beaupère, L. Grigori, V. Lederer, *Block subsampled randomized Hadamard transform for low-rank approximation on distributed architectures*, arXiv:2210.11295v1, 20 October 2022; https://arxiv.org/abs/2210.11295.
3. I. C. F. Ipsen, T. Wentworth, *The Effect of Coherence on Sampling from Matrices with Orthonormal Columns, and Preconditioned Least Squares Problems*, arXiv:1203.4809; https://arxiv.org/abs/1203.4809 (complete text unavailable in this review).
4. T. K. Huckle, C. D. Kravvaritis, *Properties of submatrices of Sylvester Hadamard matrices*, Linear and Multilinear Algebra 65 (2017), 1629–1642; https://doi.org/10.1080/03081087.2016.1250863 (complete text not inspected).
5. *Four-sparse Walsh spectra are controlled by affine dimension on \((\mathbb Z/2\mathbb Z)^d\)*, publicly available mathematical note, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-four-sparse-walsh-spectra-are-controlled-by-affine-dimension-on--1491c27461f4 (mathematical statement only).
6. *Exact Walsh-spectrum multiplicities for eight-point subsets of the Boolean four-cube*, publicly available mathematical note, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-walsh-spectrum-multiplicities-for-eight-point-subsets-of-t--b981e436a3b1 (mathematical statement only).
