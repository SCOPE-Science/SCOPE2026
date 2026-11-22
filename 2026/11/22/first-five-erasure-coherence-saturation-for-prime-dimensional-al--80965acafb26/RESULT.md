# First five-erasure coherence saturation for prime-dimensional Alltop Gabor frames

## Finding

Let \(p\ge5\) be prime, write \(\omega=\exp(2\pi i/p)\), and form the full family of unit vectors
\[
 v_{a,b}(x)=p^{-1/2}\omega^{(x-a)^3+bx},\qquad a,b,x\in\mathbb F_p.
\]
For any five distinct labelled indices \(E\subset\mathbb F_p^2\), write \(A_E\) for the least eigenvalue of the frame operator of the \(p^2-5\) retained vectors. Then
\[
 \boxed{A_E\ge p-1-\frac4{\sqrt p}.}
\]
**Sharp arithmetic threshold:** equality for some five-erasure set occurs **if and only if** \(p\equiv1\pmod4\) and \(p\ge29\). In those dimensions, therefore,
\[
 \boxed{\min_{|E|=5}A_E=p-1-\frac4{\sqrt p},\qquad
 \kappa_{\max}=\sqrt{\frac{p}{p-1-4/\sqrt p}}.}
\]
Here \(\kappa_{\max}\) is the maximal condition number of the surviving *analysis* matrix over all five-erasure masks; the displayed formula is asserted only in the equality regime.

All equality masks are characterized as follows. For each erased index \((a,b)\), put \(u=-3a\) and \(v=3a^2+b\) in \(\mathbb F_p\). The five \(u\)-coordinates must be pairwise distinct, the five points \((u,v)\) must lie on a single affine nonvertical line \(v=su+t\), and for every three distinct \(u_i,u_j,u_k\) in the set,
\[
 \boxed{\chi\bigl((u_j-u_i)(u_k-u_j)(u_k-u_i)\bigr)=1,}
\]
where \(\chi\) is the quadratic character. Equivalently, the Paley graph induced on these five \(u\)-coordinates must be a disjoint union of at most two cliques with no edges between them. The first admissible prime is \(29\); neither \(13\) nor \(17\) permits an equality mask. All primes congruent to three modulo four give strict inequality.

## Assumptions and scope

All scalar products use the usual counting inner product on \(\mathbb C^p\), with the displayed unit-vector normalization. The erasure set contains five **distinct** time-frequency shifts; no restrictions are imposed on translations or modulations. The result concerns linear frame coefficients, not phaseless measurement recovery. The prime \(p=3\) is excluded because the Alltop cubic window does not provide the distinct quadratic-chirp bases used in the proof. The theorem does **not** determine the exact worst five-erasure lower bound in the strict-inequality prime classes.

## Proof

**1. Frame reduction and sharp equality condition.** For each fixed \(a\), the \(p\) vectors \(v_{a,b}\) as \(b\) varies are an orthonormal basis, so the complete frame operator is \(pI\). For the deleted synthesis matrix \(V_E\), let \(G_E=V_E^*V_E\). The surviving operator is \(pI-V_EV_E^*\), hence
\[
 A_E=p-\lambda_{\max}(G_E).
\]
Expanding \((x-a)^3+bx=x^3+ux^2+vx-a^3\) with \(u=-3a\), \(v=3a^2+b\) shows that distinct translations correspond to distinct quadratic slopes. The quadratic Gauss sum proves that the inner product of two vectors with distinct \(u\)-coordinates has magnitude \(p^{-1/2}\), while two distinct vectors with the same \(u\) are orthogonal. Therefore the Rayleigh quotient and triangle inequality give \(\lambda_{\max}(G_E)\le1+4/\sqrt p\).

Equality requires every off-diagonal magnitude to be \(p^{-1/2}\), so the erased translations must be distinct. Equality in the triangle inequality forces a unit-modulus diagonal change of phase taking all ten off-diagonal Gram entries to the positive number \(p^{-1/2}\). Conversely this phase alignment has largest Gram eigenvalue \(1+4/\sqrt p\). Alignment is equivalent to all triangular cycle products of the Gram phases being \(1\) (fix the first vertex's gauge, then verify each remaining edge).

**2. Gaussian cycle calculation and collinearity.** Suppress the irrelevant constants \(-a^3\) and write \(w_{u,v}(x)=p^{-1/2}\omega^{x^3+ux^2+vx}\). For distinct \(u_i,u_j\), quadratic Gauss summation gives
\[
 \langle w_i,w_j\rangle
 =p^{-1/2}\varepsilon_p\chi(u_j-u_i)
 \omega^{-(v_j-v_i)^2/[4(u_j-u_i)]},
\]
where \(\varepsilon_p=1\) for \(p\equiv1\pmod4\), and \(\varepsilon_p=i\) for \(p\equiv3\pmod4\). For any three distinct slopes, their normalized cyclic Gram product is \(\varepsilon_p^3\chi(P)\omega^{-U/4}\), with
\[
 P=(u_j-u_i)(u_k-u_j)(u_i-u_k),\qquad
 U=\frac{(v_j-v_i)^2}{u_j-u_i}
   +\frac{(v_k-v_j)^2}{u_k-u_j}
   +\frac{(v_i-v_k)^2}{u_i-u_k}.
\]
Put \(d_1=u_j-u_i\), \(d_2=u_k-u_j\) and secant slopes \(r_1=(v_j-v_i)/d_1\), \(r_2=(v_k-v_j)/d_2\). Direct simplification gives
\[
 U=\frac{d_1d_2}{d_1+d_2}(r_1-r_2)^2.
\]
The denominator is nonzero because the three \(u\)'s are distinct. Thus \(U=0\) precisely when the three planar points are collinear. For \(p\equiv3\pmod4\), the factor \(\varepsilon_p^3=-i\) cannot be cancelled by a quadratic-character sign and a \(p\)-th root of unity, so alignment is impossible. For \(p\equiv1\pmod4\), since \(-1\) is not a \(p\)-th root of unity, alignment requires \(\chi(P)=1\) and \(U=0\). All triples collinear forces the five points onto the same affine line. Since \(\chi(-1)=1\), the sign of \(P\) equals the stated order-independent triple difference sign. This proves the **necessary and sufficient** equality characterization, including the graph formulation: fix one slope, then the signs of its four incident Paley edges determine a partition into two cliques, with all cross edges negative.

**3. Exact small-prime exclusions.** The only primes \(p\equiv1\pmod4\) below \(29\) are \(5,13,17\). The standalone checker enumerates every five-subset of the \(p\)-element slope field: respectively \(1\), \(1287\), and \(6188\) subsets, in total \(7476\). Every one has a negative triangle sign, so no coherent five-subset exists. The enumeration uses integer modular exponentiation only for these exclusion tests; no numerical eigenvalue comparison is needed for the nonexistence claim.

**4. Explicit existence in the finite intermediate range.** For every prime \(p\equiv1\pmod4\) with \(29\le p<109\), the following five slope coordinates have all ten triple signs positive. They are checked directly by the executable certificate:
\[
\begin{array}{c|l}
 p& (u_1,u_2,u_3,u_4,u_5)\\\hline
29&(0,1,3,5,19)\\
37&(0,1,4,6,18)\\
41&(0,1,2,10,33)\\
53&(0,1,3,32,37)\\
61&(0,1,4,32,33)\\
73&(0,1,2,3,4)\\
89&(0,1,2,10,11)\\
97&(0,1,2,3,96)\\
101&(0,1,3,5,97)
\end{array}
\]
Choosing \(v=0\) for all five coordinates converts each witness to actual time-frequency indices via \(a=-u/3\), \(b=-3a^2\); the resulting Gram matrix has eigenvalues \(1+4/\sqrt p\) once and \(1-1/\sqrt p\) four times. These nine checked witnesses exhaust all relevant primes in the interval.

**5. Existence for every larger eligible prime.** Suppose \(p\equiv1\pmod4\) and \(p\ge109\). The Paley graph has degree \((p-1)/2\), common-neighbor number \((p-5)/4\) for an adjacent pair, and nontrivial adjacency eigenvalues \((-1\pm\sqrt p)/2\). It therefore contains a triangle \(T=\{a,b,c\}\); Hoffman's eigenvalue bound gives independence number \(\alpha(P_p)\le\sqrt p\).

Let \(M_T\) count vertices simultaneously **nonadjacent** to all three vertices of \(T\), excluding \(T\). With
\[
 \tau_T=\sum_{x\in\mathbb F_p}\chi\bigl((x-a)(x-b)(x-c)\bigr),
\]
expanding the three nonadjacency indicators and using \(\sum_x\chi((x-u)(x-v))=-1\) for distinct \(u,v\) gives the *exact* identity
\[
 \boxed{M_T=\frac{p-3-\tau_T}{8}.}
\]
Because \(a,b,c\) are distinct, \(y^2=(x-a)(x-b)(x-c)\) is a nonsingular elliptic curve. Hasse's classical bound gives \(|\tau_T|\le2\sqrt p\). For \(p\ge109\), the strict elementary inequality \(p-3>10\sqrt p\) yields
\[
 M_T\ge\frac{p-3-2\sqrt p}{8}>\sqrt p\ge\alpha(P_p).
\]
Hence the common-nonneighbor set cannot be independent: it contains two adjacent vertices \(d,e\). The induced five-vertex graph on \(T\cup\{d,e\}\) is precisely the disjoint union \(K_3\sqcup K_2\), with all cross edges absent. Every triangle product is therefore positive. Taking \(v=0\) produces a saturating five-erasure mask. This argument proves existence for **all** eligible primes beyond the finite certificate and completes the threshold proof.

**6. Surviving analysis conditioning.** In the equality regime, \(p\ge29>5\), so \(V_EV_E^*\) has rank at most five and the surviving frame operator retains the eigenvalue \(p\). Its smallest eigenvalue is the established \(p-1-4/\sqrt p\), giving the stated exact largest analysis condition number. This statement does not replace the strict nonattainment cases by an unproved formula.

## Verification

Run `python CHECK.py` in this package. It uses Python 3.10 or newer plus NumPy. It (i) exhausts all \(7476\) distinct five-subsets at the three smaller admissible primes \(5,13,17\) in exact modular arithmetic, (ii) validates all ten triangle signs of nine explicit witnesses for every admissible prime between \(29\) and \(101\), (iii) reconstructs their actual Alltop Gabor Gram matrices and checks the predicted spectra, and (iv) checks tightness of the full Gabor family in the same nine dimensions. The observed terminal marker is

`CHECK_OK excluded_five_sets=7476 explicit_witnesses=9`

The infinite-prime portion follows from the classical quadratic-character, elliptic Hasse, and Hoffman estimates established in the proof, not from finite experiments. Numerical Gram checks supplement the exact arithmetic witnesses.

## Relationship to prior work

Salanevich and Strachan (arXiv:2509.01325, first public September 1, 2025) study robustness of finite Gabor frames and Alltop windows; their Theorems 1.5 and 5.5 give general erasure guarantees, and their numerical Table 1 includes small-dimensional erasure tests. Those bounds do not identify the first prime at which the five-erasure coherence limit is attained.

Hoffman and Solazzo (arXiv:1107.2267) and Bodmann–Paulsen provide the general Seidel-switching criterion for saturating coherence bounds of equiangular tight frames; **that general criterion is prior work**, not the contribution here. A published exact four-column census for symmetric Paley real harmonic frames determines the four-vertex triangle-sign profiles and their counts, but does not imply the existence or nonexistence of coherent **five**-point sets at the sharp prime cutoff, nor the Alltop quadratic-chirp collinearity condition. A separately published five-column classification for *skew* conference matrices has hypotheses of the opposite quadratic-character parity. The previously established Alltop **three**-erasure theorem has no five-erasure analysis. These comparisons concern statement implication, field parity, and graph size—not title similarity.

The contribution is the exact **five-point onset at prime \(29\)** and its all-prime proof, via a new link between Alltop mask alignment, induced \(K_3\sqcup K_2\) in Paley graphs, an elliptic character-sum bound, and a finite exact boundary certificate. No claim of novel Gauss sums, Hoffman's bound, Hasse's theorem, or general ETF switching inequalities is made.

## Limitations

The result is a **sharp equality/non-equality classification** for the universal five-erasure coherence bound, not a formula for the strict-case worst lower frame bounds. It does not enumerate the number of equality masks at each eligible prime, treat composite dimensions, extend to six or more erasures, or give nonlinear phase-retrieval guarantees. The three small-prime exclusions are exhaustively checked by an executable integer certificate rather than a uniform symbolic classification. Priority comparison is strongest for the stated Gabor and Paley results; older equivalent five-vertex Seidel-switching or conference-matrix existence statements may remain undiscovered. No independent mathematical audit has been performed.

## References

1. P. Salanevich and N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, first publicly posted September 1, 2025, arXiv:2509.01325. https://arxiv.org/abs/2509.01325
2. T. R. Hoffman and J. P. Solazzo, *Complex Equiangular Tight Frames and Erasures*, first publicly posted July 8, 2011, arXiv:1107.2267, Proposition 3.8 and Corollary 3.9. https://arxiv.org/html/1107.2267v1
3. M. Fickus and D. G. Mixon, *Numerically erasure-robust frames*, first publicly posted February 21, 2012, arXiv:1202.4525. https://arxiv.org/html/1202.4525v2
4. *Sharp three-erasure stability of Alltop Gabor frames*, published mathematical result, November 8, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-three-erasure-stability-of-alltop-gabor-frames--ede488cf192e
5. *Exact four-column spectra and extremal census for real Paley harmonic frames*, published mathematical result, November 8, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-four-column-spectra-and-extremal-census-for-real-paley-har--28714709e48e
6. *Five-column spectral dichotomy and exact multiplicities for skew-conference tight frames*, published mathematical result, November 2, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-five-column-spectral-dichotomy-and-exact-multiplicities-for-skew--86724d774ebb
7. H. Hasse, classical elliptic-curve point-count bound; and A. J. Hoffman, classical regular-graph independence bound, used only in their stated standard forms.
