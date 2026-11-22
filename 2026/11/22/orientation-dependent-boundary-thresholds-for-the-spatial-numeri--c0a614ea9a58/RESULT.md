# Orientation-dependent boundary thresholds for the spatial numerical radius on \(\ell_p\)

## Finding
Let \(1<p<\infty\), let \(q=p/(p-1)\), and let \(X=\ell_p(\mathbb N_0;\mathbb C)\). Define the right and left unilateral shifts by \(Re_j=e_{j+1}\) and \((Lx)_j=x_{j+1}\), and the rank-one coordinate projection by \(P_0x=x_0e_0\). For every real \(t\ge0\), set \(F_t=R+tP_0\) and \(B_t=L+tP_0\). Write \(v_p(T)\) for the spatial numerical radius, calculated with the unique normalized \(\ell_p\)-duality functional.

The two radii admit the **complete exact formulas**
\[
 v_p(F_t)=\begin{cases}
 1,&0\le t\le (p-1)/p,\\
 t+\frac1p\left(\frac{p-1}{pt}\right)^{p-1},&t>(p-1)/p,
 \end{cases}
\]
\[
 v_p(B_t)=\begin{cases}
 1,&0\le t\le 1/p,\\
 t+\frac{p-1}{p}\left(\frac1{pt}\right)^{1/(p-1)},&t>1/p.
 \end{cases}
\]
In the region of radius one neither operator attains its numerical radius. Above its respective threshold, **every unit norming vector** is a common-phase multiple of the unique positive geometric vector
\[
 x_j=(1-r^p)^{1/p}r^j,\qquad j\ge0,
\]
with \(r=(p-1)/(pt)\) for \(F_t\), and \(r=(pt)^{-1/(p-1)}\) for \(B_t\). In particular the critical boundary strengths differ except at \(p=2\); their order reverses as \(p\) crosses two.

There is nevertheless one **orientation-independent sharp quadratic onset coefficient**. For either orientation, with its own threshold \(t_c\),
\[
 v_p(T_{t_c+\delta})=1+\frac{p^2}{2(p-1)}\delta^2+O_p(\delta^3)
 \qquad(\delta\downarrow0).
\]
The ordinary numerical-radius transition occurs while the essential numerical range remains the closed unit disk in both orientations for every \(t\ge0\).

## Assumptions and scope
The scalar field is complex; the same numerical-radius formulas and positive-vector equality statements hold over real \(\ell_p\). The exponent is strictly between one and infinity and the defect strength is real and nonnegative. The index starts at zero, and the shifts are the *forward* and *backward* operators defined above, not shifts with a modified first edge weight. For \(\|x\|_p=1\), the norming functional is
\[
 J_p(x)(y)=\sum_{j\ge0}|x_j|^{p-2}\overline{x_j}y_j,
 \qquad v_p(T)=\sup_{\|x\|_p=1}|J_p(x)(Tx)|.
\]
At a zero coordinate, the expression \(|x_j|^{p-2}\overline{x_j}\) is defined as zero. This theorem determines scalar spatial numerical radii, not full Banach numerical-range geometry or any higher-rank matrix numerical range.

## Proof
**1. Reduction to a nonnegative variational problem.** For any unit \(x\), writing \(u_j=|x_j|\), Hölder's inequality ensures convergence and the triangle inequality gives
\[
 |J_p(x)(F_tx)|\le t u_0^p+\sum_{j\ge0}u_j u_{j+1}^{p-1}=:G_F(u),
\]
\[
 |J_p(x)(B_tx)|\le t u_0^p+\sum_{j\ge0}u_j^{p-1}u_{j+1}=:G_B(u).
\]
Equality holds for positive real sequences. Thus the two suprema reduce exactly to maximizing \(G_F\) and \(G_B\) over nonnegative unit \(\ell_p\) sequences.

**2. Weighted Young inequalities and exact upper envelopes.** For any \(a,b\ge0\) and \(r>0\), Young's inequality, with its equality case, gives
\[
 ab^{p-1}\le\frac{r^{p-1}}p a^p+\frac{p-1}{pr}b^p,
 \qquad
 a^{p-1}b\le\frac{p-1}{p}r a^p+\frac1{pr^{p-1}}b^p.
\]
In either inequality equality holds exactly when \(b=ra\) (including the joint-zero case). Summing across the half-line, and using \(\sum_{j\ge0}u_{j+1}^p=1-u_0^p\), yields
\[
 G_F(u)\le \frac{r^{p-1}}p+\frac{p-1}{pr}+\left(t-\frac{p-1}{pr}\right)u_0^p,
\]
\[
 G_B(u)\le \frac{p-1}p r+\frac1{pr^{p-1}}+\left(t-\frac1{pr^{p-1}}\right)u_0^p.
\]
If \(t>(p-1)/p\), choose \(r=(p-1)/(pt)<1\). The coefficient of \(u_0^p\) vanishes in the first bound and its value is precisely the claimed supercritical \(v_p(F_t)\). If \(t>1/p\), choose \(r=(pt)^{-1/(p-1)}<1\) in the second bound to obtain precisely the claimed supercritical \(v_p(B_t)\).

**3. Sharpness, existence, and rigidity of supercritical vectors.** With the chosen \(0<r<1\), set \(u_j=(1-r^p)^{1/p}r^j\). Then \(\|u\|_p=1\), every pair of consecutive coordinates satisfies the equality condition for weighted Young, and both upper bounds in step 2 are equalities, separately in their corresponding orientation. Thus they are the exact numerical radii. Conversely equality in the sum of nonnegative Young deficits forces \(u_{j+1}=ru_j\) for every \(j\), hence the stated unique normalized positive sequence. For a complex vector to attain the radius, the complex triangle inequality must also be sharp. Its positive diagonal term \(t|x_0|^p\) and every nonzero shift term must have the same complex argument. Since \(t>0\), adjacent coordinates must have equal phases, hence only a single global phase is free. This proves both attainment and the equality classification.

**4. The plateau and nonattainment.** In step 2 take \(r=1\). The first bound simplifies to \(G_F(u)\le1+(t-(p-1)/p)u_0^p\), and the second to \(G_B(u)\le1+(t-1/p)u_0^p\). Hence the respective radius cannot exceed one below or at its threshold. On the other hand, unit vectors constant on a long finite block supported after coordinate zero give numerical values \((N-1)/N\to1\) in either orientation, independent of the diagonal defect; both radii therefore equal one. Equality in the upper bound for a nonzero unit vector would require equality in every unweighted Young summand, so \(u_{j+1}=u_j\) for all \(j\); a nonzero constant sequence is not in \(\ell_p\). Thus numerical-radius attainment is impossible at and below the thresholds.

**5. Sharp critical onset and geometric localization.** On each supercritical side the exact formula is analytic in \(t\). Differentiating at \(t_c=(p-1)/p\) for the forward family, or at \(t_c=1/p\) for the backward family, gives value \(1\), right derivative \(0\), and right second derivative \(p^2/(p-1)\). Taylor's theorem gives the stated quadratic asymptotic, with an \(O_p(\delta^3)\) remainder. In both families the maximizing decay ratio \(r\uparrow1\) as \(t\downarrow t_c\); the associated normalized geometric vectors spread over a diverging number of coordinates and weakly approach zero. This also explains the nonattainment at criticality.

**6. Essential numerical range.** The unperturbed forward and backward shifts have the closed unit disk as essential numerical range: their norm is one and normalized long blocks translated to infinity supply the unit-circle limits, whence convexity gives the entire disk. The rank-one term \(tP_0\) is compact; compact-perturbation invariance of the essential numerical range on \(\ell_p\) then preserves that disk. No assertion about the *whole ordinary numerical range* of the perturbed operators is needed for the radius formulas.

## Verification
The standalone `checker.py` verifies the exact formula against 28,860 deterministic finite nonnegative vector inequalities and equality-vector checks across several exponents, orientations and strengths; it also verifies the local critical coefficients numerically. Run `python checker.py` using Python and NumPy; the expected last line is `BOUNDARY_NUMERICAL_RADIUS_DIAGNOSTIC_OK 28860`. Finite tests establish no infinite-dimensional conclusion. The proof above independently supplies all bounds, equality conditions, existence, nonattainment and asymptotics. In the checker the geometric equality is evaluated using the exact infinite geometric sum, not a truncated extrapolation.

## Relationship to prior work
Müller and Tomilov, *Numerical and essential numerical ranges on* \(\ell_p\) (arXiv:2606.22693v1, 21 June 2026), establish the complex \(\ell_p\)-norming functional and the disk picture for the unperturbed unilateral shift in their Proposition 4.14, as well as general essential-range results. Their full text does not state the two oriented rank-one *diagonal* numerical-radius formulas or the non-Hilbert critical strengths.

A published Hilbert-space result, *A Robin critical window for numerical ranges of boundary-perturbed unilateral shifts* (2026), already treats exactly \(R+tP_0\) on \(\ell_2\), proves \(v_2=1\) below \(t=1/2\) and \(v_2=t+1/(4t)\) above it, and gives considerably more detailed finite-compression and numerical-range geometry. The specialization \(p=2\) of the present formula is **credited as previously known**; the new assertion concerns all non-Hilbert exponents, the resulting forward/backward asymmetry, unique extremizers and the common critical curvature.

The published *Sharp numerical-radius and attainment thresholds for one-edge perturbations of* \(\ell_p\) *shifts* (2026) treats the distinct operators with an **off-diagonal** exceptional first shift weight. It obtains the thresholds \(p^{1/p}\) and \(q^{1/q}\) for those operators but does not determine the present diagonal boundary family, nor an exact supercritical radius for these operators. These two problems are not interchanged by a mere change of notation: one alters a transition coefficient, the other adds a point potential to the diagonal.

Ko and Lee, *On rank one perturbations of the unilateral shift* (2011), study Hilbert-space point spectrum and hyponormality for general rank-one perturbations; their available author-supplied full text does not present a spatial \(\ell_p\) numerical-radius formula. Earlier Hilbert weighted-shift numerical-radius work concerns off-diagonal shift coefficients. The sharp weighted Young inequality is classical and is used as a proof tool; it is not claimed as a novel result.

## Limitations
Only scalar nonnegative perturbations at the first coordinate and the range \(1<p<\infty\) are covered. No claim is made for complex perturbation parameters, arbitrary diagonal potentials, other coefficient profiles or exact full ordinary numerical-range shapes. The result's mathematical novelty is not a statement about the weighted Young inequality, the known Hilbert specialization or the unperturbed disk; those antecedents are explicitly credited. An equivalent non-Hilbert formula could be present in older general sequence-space variational literature under different terminology; this remains a bibliographic risk despite targeted comparisons. Independent external mathematical audit has not been performed.

## References
1. V. Müller and Y. Tomilov, *Numerical and essential numerical ranges on* \(\ell_p\), arXiv:2606.22693v1, first posted 2026-06-21, https://arxiv.org/abs/2606.22693.
2. *A Robin critical window for numerical ranges of boundary-perturbed unilateral shifts*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-robin-critical-window-for-numerical-ranges-of-boundary-perturb--17bf045f66f8.
3. *Sharp numerical-radius and attainment thresholds for one-edge perturbations of* \(\ell_p\) *shifts*, published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-numerical-radius-and-attainment-thresholds-for-one-edge-pe--6d4363552adb.
4. E. Ko and J. E. Lee, *On rank one perturbations of the unilateral shift*, *Commun. Korean Math. Soc.* 26 (2011), 79–88, https://doi.org/10.4134/CKMS.2011.26.1.079.
5. M. Martín, J. Merí and M. Popov, *On the numerical radius of operators in Lebesgue spaces*, arXiv:1011.4785, https://arxiv.org/abs/1011.4785.
