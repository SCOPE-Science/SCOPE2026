# A sharp discontinuous migration-benefit threshold in a binary three-season habitat cycle

## Finding
Consider a population distributed over two habitat patches, with annual positive linear reproduction followed by symmetric exchange of a fixed fraction \(d\) of each patch population. Suppose exactly one of three recurring seasons favors patch 1 and the other two favor patch 2, and that the favorable-to-unfavorable reproduction ratio is the same \(r>1\) each season. Define the per-three-season population propagator \(P_r(d)\) below and its Perron growth factor \(G_r(d)=\rho(P_r(d))\). The sedentary baseline is \(G_r(0)=r^2\).

**Theorem (complete strict-improvement classification).** A migration fraction \(d\in[0,1]\) strictly increases the three-season asymptotic population growth factor over the sedentary baseline if and only if
\[
r>r_c:=2+\sqrt3,\qquad d_-(r)<d<d_+(r),
\]
where
\[
d_\pm(r)=\frac{r^2+6r-1\ \pm\sqrt{(r^2-4r+1)(r^2+4r+1)}}{2(r^2+4r-1)}.
\]
For \(1<r<r_c\), zero migration is the unique globally optimal fraction. At \(r=r_c\), exactly \(d=0\) and \(d=(3-\sqrt3)/2\) tie for the global maximum, and every other rate is worse. For \(r>r_c\), every global maximizer lies in the displayed open interval; as \(r\) decreases to \(r_c\) from above, every such maximizer approaches the nonzero value \((3-\sqrt3)/2\). Thus onset of migration benefit is discontinuous in the optimizing rate, not a perturbative improvement from zero. In fact, for every fixed \(r>1\), *all sufficiently small positive exchange fractions are worse than no exchange*, even when larger exchange fractions eventually help.

**The capped-dispersal contrast.** If exchange fractions are restricted to \(0\le d\le1/2\) (as in completely redistributing a fraction of the population to an equally likely destination), a strict benefit over no exchange is possible if and only if \(r>2+\sqrt5\). Consequently for
\[
2+\sqrt3<r\le2+\sqrt5
\]
advantage is possible with direct exchange, but no amount of exchange at or below one half beats remaining sedentary. At \(r=2+\sqrt5\), \(d=1/2\) ties, rather than strictly improves, the sedentary growth factor. This contrast concerns the onset of a *strict benefit*, not an asserted unique global optimizer in the capped class.

Up to exchanging the names of the patches and cyclically relabeling the seasons, these statements classify every nonconstant binary three-season calendar made from the two complementary fitness environments with fixed contrast \(r\). Constant calendars do not benefit from dispersal.

## Assumptions and scope
Use column population vectors and the two matrices
\[
M(d)=\begin{pmatrix}1-d&d\\d&1-d\end{pmatrix},\quad
H_r=\operatorname{diag}(r,1),\quad L_r=\operatorname{diag}(1,r).
\]
Here \(r>1\), \(0\le d\le1\), and migration is lossless, symmetric, independent of patch and season, and occurs after reproduction. The environment cycles through \(H_r,L_r,L_r\), giving
\[
P_r(d)=M(d)L_rM(d)L_rM(d)H_r,
\qquad G_r(d)=\rho(P_r(d)).
\]
The asymptotic per-season growth multiplier is \(G_r(d)^{1/3}\); maximizing it is equivalent to maximizing \(G_r(d)\). Absolute fecundity scales common to the seasons multiply all growth factors and do not alter the relative comparison, but are not included in this normalization. The claim is about deterministic linear asymptotic abundance, not an evolutionarily stable dispersal strategy or finite-population survival. Direct exchange \(d>1/2\) is permitted and is not equivalent to drawing each migrant's destination independently from a two-patch equal pool; the latter has effective exchange at most one half.

## Proof
**1. Exact characteristic polynomial.** Multiplication gives
\[
\begin{aligned}
T_r(d)&:=\operatorname{tr}P_r(d)
=(r+1)(1-d)\bigl[r-2rd+(r+1)^2d^2\bigr],\\
D_r(d)&:=\det P_r(d)=r^3(1-2d)^3.
\end{aligned}
\]
The two real eigenvalues \(\lambda_+(d)\ge\lambda_-(d)\) exist because \(P_r(d)\) is a nonnegative \(2\)-by-\(2\) matrix and its eigenvalue discriminant is \((P_{11}-P_{22})^2+4P_{12}P_{21}\ge0\). The larger eigenvalue equals the spectral radius: for \(0<d<1\) the matrix is strictly positive; at either endpoint direct multiplication gives the same conclusion. At \(d=0\), \(P_r(0)=\operatorname{diag}(r,r^2)\), so \(G_r(0)=r^2\).

**2. The characteristic-polynomial sign detects advantage.** If \(0\le d\le1/2\), then \(D_r(d)\ge0\) and both eigenvalues are nonnegative. Because their product is at most \(r^3\), the smaller eigenvalue satisfies \(0\le\lambda_-(d)\le\sqrt{D_r(d)}\le r^{3/2}<r^2\). If \(1/2<d\le1\), then \(D_r(d)<0\), so \(\lambda_-(d)<0<r^2\). Therefore, for every allowed \(d\), \(r^2-\lambda_-(d)>0\). In particular
\[
\begin{aligned}
(r^2-\lambda_+)(r^2-\lambda_-)
&=r^4-r^2T_r(d)+D_r(d)\\
&=r^2d(r-1)Q_r(d),\\
Q_r(d)&=(r^2+4r-1)d^2-(r^2+6r-1)d+3r.
\end{aligned}
\]
For \(d>0\), the sign of \(G_r(d)-r^2\) is exactly the *opposite* of the sign of \(Q_r(d)\). At \(d=0\) equality always holds.

**3. Sharp quadratic discriminant and boundaries.** The leading coefficient of \(Q_r\) is positive for \(r>1\), and its discriminant factors as
\[
\Delta_r=(r^2-4r+1)(r^2+4r+1).
\]
Its vertex is
\[
d_v(r)=\frac{r^2+6r-1}{2(r^2+4r-1)}
=\frac12+\frac{r}{r^2+4r-1}\in(1/2,1).
\]
Also \(Q_r(0)=3r>0\) and \(Q_r(1)=r>0\). Since \(r>1\), the unique discriminant threshold is \(r_c=2+\sqrt3\). When \(r<r_c\) the quadratic is strictly positive; when \(r=r_c\), it is nonnegative with one double root \(d_c=d_v(r_c)=(3-\sqrt3)/2\); when \(r>r_c\), it is strictly negative precisely between its two distinct roots \(d_\pm(r)\), both in \((0,1)\). The sign identity proves every strict-improvement assertion.

At the threshold, only zero migration and \(d_c\) attain \(r^2\), so they are exactly the two global optimizers. Above the threshold, continuity of the spectral radius on the compact interval ensures global maximizers exist; all must lie inside \((d_-,d_+)\), because this interval is the only region above the sedentary baseline. The endpoints of this interval both converge to \(d_c>0\) as \(r\downarrow r_c\), proving the discontinuous onset. Below the threshold zero migration is uniquely optimal.

**4. Capped exchange.** The quadratic \(Q_r\) decreases strictly on \([0,1/2]\), since its vertex is larger than one half. Its minimum on that interval is
\[
Q_r(1/2)=\frac{-r^2+4r+1}{4}.
\]
This is negative exactly when \(r>2+\sqrt5\). When negative, the admissible fraction \(d=1/2\) strictly improves growth; when nonnegative, no fraction in \((0,1/2]\) strictly improves. This proves the second threshold and its equality case.

**5. Binary-calendar completeness.** Any nonconstant three-season word in \(H_r,L_r\) has either one occurrence of one symbol or two. Exchanging patches conjugates \(H_r\) and \(L_r\) by the swap matrix, and commutes with \(M(d)\). Cyclic permutations of square matrix products preserve characteristic polynomials, including when \(M(1/2)\) is singular. Therefore all nonconstant binary three-season words have the same spectral radius as \(H_r,L_r,L_r\). For a constant word \(H_r,H_r,H_r\) (or its conjugate), the propagator is \((M(d)H_r)^3\), with \(\rho(M(d)H_r)\le\|M(d)H_r\|_1=r\); therefore dispersal cannot outperform the sedentary baseline \(r^3\). No other binary three-season configurations exist.

## Verification
Run `python checker.py` with Python 3 and SymPy installed in the directory containing the checker. The program regenerates `verification_certificate.json`, asserts ten exact symbolic equalities (trace, determinant, factorization, discriminant, critical double root, and endpoint relations), and checks 707 rational parameter pairs using independently computed matrix eigenvalues and the sign criterion. Four further exact-sign checks cover the contrast between exchange rates. The expected total is 721 assertions. These finite checks are diagnostic; the universal classification is established by the analytic argument above. All necessary checker source and the deterministic certificate are supplied.

At \(r=4\), direct substitution gives \(G_r(0)=16\), \(G_r(1/2)=125/8=15.625\), and \(G_r((3-\sqrt3)/2)\approx16.5024\): direct exchange helps, while complete pooling does not. At \(r=5\), \(G_r(0)=25\) and \(G_r(1/2)=27\), consistent with the higher capped-exchange threshold.

## Relationship to prior work
Classical patch ecology establishes that dispersal may change growth when habitat quality varies across space and time; the novelty asserted here is neither the existence of dispersal-induced growth nor the general use of Perron eigenvalues. Schreiber and Li (2010, first arXiv version) analyze unconditional dispersal and evolutionary strategies in periodic environments. A published mathematical treatment titled *Two-season endpoint optimality and the first interior dispersal optimum* gives a universal two-season endpoint comparison and a *different* three-season witness involving a neutral season and opposite single-patch favored seasons; its witness does not give the present binary-calendar all-parameter thresholds. Another published treatment, *Four seasons are necessary and sufficient for interior-optimal dispersal in a two-patch periodic model*, concerns **equal-pool dispersal** with exchange probability bounded above by one half, and does not allow the direct-exchange rates that first become beneficial at \(2+\sqrt3\). Its general three-season endpoint theorem is compatible with the capped boundary \(2+\sqrt5\); it does not give the current sharp contrast thresholds. Katriel (2021 preprint, 2022 journal) analyzes a continuous-time periodic-migration differential equation and general dispersal-induced growth, rather than this discrete three-step binary calendar. The inspected evidence did not state or imply the complete result as an already published corollary. Priority remains provisional: differently indexed positive-matrix and ecological literature could contain equivalent factorizations.

## Limitations
The proof prescribes patch fertility rather than deriving it from climate or a coupled ecological model, and assumes equal time steps, lossless symmetric exchange, a common fitness contrast, and zero density dependence. Only binary three-season calendars are classified, with the two patch rates exactly reciprocal across the seasons. The result establishes improvement over the sedentary baseline and the discontinuous onset; it does **not** prove uniqueness of the global maximizing fraction when \(r>r_c\), a demographic-stochastic persistence probability, or an evolutionarily stable dispersal strategy. Distinguishing direct exchange from equal-pool redistribution is essential. Literature inspection is not an independent novelty certificate.

## References
1. S. J. Schreiber and C.-K. Li, *Evolution of unconditional dispersal in periodic environments*, arXiv:1007.5267v1, first publicly posted 2010-07-29. https://arxiv.org/abs/1007.5267
2. M. A. McPeek and R. D. Holt, *The evolution of dispersal in spatially and temporally varying environments*, *The American Naturalist* 140 (1992), DOI: 10.1086/285453. https://doi.org/10.1086/285453
3. G. Katriel, *Dispersal-induced growth in a time-periodic environment*, arXiv:2104.01589, first posted 2021-04-04; *Journal of Mathematical Biology* 85 (2022), article 24. https://arxiv.org/html/2104.01589v4
4. *Two-season endpoint optimality and the first interior dispersal optimum*, publicly indexed mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-season-endpoint-optimality-and-the-first-interior-dispersal--4bf78d70bf53
5. *Four seasons are necessary and sufficient for interior-optimal dispersal in a two-patch periodic model*, publicly indexed mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-four-seasons-are-necessary-and-sufficient-for-interior-optimal-d--277a84601303
