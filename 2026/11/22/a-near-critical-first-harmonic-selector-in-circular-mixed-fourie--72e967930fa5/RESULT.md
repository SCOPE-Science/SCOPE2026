# A near-critical first-harmonic selector in circular mixed Fourier extension

## Finding

For every fixed integer \(m\ge 0\) there exists \(\varepsilon_m>0\) such that, for every real \(4<p<4+\varepsilon_m\) and every integer \(k>m\),
\[
I_m(p)>I_k(p),\qquad I_j(p):=\int_0^\infty |J_j(r)|^p r\,dr.
\]
Here \(J_j\) is the ordinary Bessel function of the first kind. In particular, throughout a nonempty interval immediately above the critical exponent \(4\), the first angular harmonic is the **unique maximizing nonconstant degree** in the two-dimensional radial--angular mixed Fourier-extension problem. The sharp squared-norm stability coefficient on that interval is
\[
\Gamma_{2,p}=(2\pi)^2\bigl(I_0(p)^{2/p}-I_1(p)^{2/p}\bigr),
\qquad
\lim_{p\downarrow4}\frac{\Gamma_{2,p}}{\sqrt{p-4}}=\frac{4\pi}{\sqrt3}.
\]
The assertion is uniform over **all** higher integer degrees \(k\), not just over each fixed finite collection of degrees. The existence of the interval is proved; no explicit optimal endpoint is claimed.

## Assumptions and scope

Let \(\mathbb S^1\) carry unnormalized arc length \(d\sigma=d\theta\) and use
\[
\widehat{f\sigma}(x)=\int_{\mathbb S^1}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega).
\]
For \(p>4\) let
\[
\|F\|_{L^p_{\mathrm{rad}}L^2_{\mathrm{ang}}}=
\left(\int_0^\infty\bigl(\int_{\mathbb S^1}|F(r\omega)|^2\,d\sigma(\omega)\bigr)^{p/2}r\,dr\right)^{1/p}.
\]
Write \(P_0\) for the \(L^2(\mathbb S^1)\)-orthogonal projection onto constants. The stability inequality concerns every complex \(f\in L^2(\mathbb S^1,d\sigma)\), with \(C_{2,p}\) the sharp extension constant:
\[
C_{2,p}^2\|f\|_2^2-\|\widehat{f\sigma}\|_{L^p_{\mathrm{rad}}L^2_{\mathrm{ang}}}^2
\ge \Gamma_{2,p}\|f-P_0f\|_2^2.
\]
The near-critical interval can depend on the fixed lower degree \(m\); there is no asserted common interval for all pairs of degrees.

## Proof

**1. Exact critical adjacent-degree gap.** Bessel's adjacent-order recurrences
\[
J_n'(r)=\frac nrJ_n(r)-J_{n+1}(r),\qquad
J_{n+1}'(r)=J_n(r)-\frac{n+1}{r}J_{n+1}(r)
\]
give, for \(n\ge0\) and \(r>0\), the identity
\[
\frac{d}{dr}\left(\frac{r^2\bigl(J_n(r)^2+J_{n+1}(r)^2\bigr)^2}{4n+2}\right)
=r\bigl(J_n(r)^4-J_{n+1}(r)^4\bigr).
\]
The boundary contribution at zero vanishes. Fixed-order Hankel asymptotics give
\(J_n(r)^2+J_{n+1}(r)^2=2/(\pi r)+O_n(r^{-2})\) as \(r\to\infty\). Consequently, for every fixed \(0\le m<k\),
\[
\lim_{R\to\infty}\int_0^R r\bigl(J_m(r)^4-J_k(r)^4\bigr)\,dr
=\frac{2}{\pi^2}\sum_{j=m}^{k-1}\frac1{2j+1}>0.
\]
This fixed-degree identity is known in the nearby critical-moment literature; it is used here as an input, not presented as the novelty.

**2. Continuity of fixed-degree differences at the critical exponent.** For each fixed order \(j\), the standard expansion, with \(\phi_j=j\pi/2+\pi/4\), is
\[
J_j(r)=\sqrt{\frac{2}{\pi r}}\bigl(\cos(r-\phi_j)+O_j(r^{-1})\bigr).
\]
Uniformly for \(4\le p\le5\), replacing \(r|J_j(r)|^p\) by \((2/\pi)^{p/2}r^{1-p/2}|\cos(r-\phi_j)|^p\) introduces an integrable \(O_j(r^{-2})\) tail. Since the periodic profiles for distinct integer orders have the same average
\[
M(p)=\frac1\pi\int_0^\pi|\cos u|^p\,du
=\frac{\Gamma((p+1)/2)}{\sqrt\pi\,\Gamma((p+2)/2)},
\]
their difference has a periodic primitive bounded uniformly for \(p\in[4,5]\). Integration by parts against \(r^{1-p/2}\) bounds its tail by \(O_{m,k}(R^{-1})\), uniformly in \(p\in[4,5]\). Therefore
\[
\lim_{p\downarrow4}(I_m(p)-I_k(p))
=\frac{2}{\pi^2}\sum_{j=m}^{k-1}\frac1{2j+1}>0.
\]
For any **finite** family of indices \(k>m\), the desired strict inequality follows on a common interval. The remaining issue is an infinite tail of orders.

**3. Published uniform high-order estimate.** The uniform transition/tail estimates in Section 3.2 of Xu (2026), specifically the bounds corresponding to (3.70), the transition contribution following it, and (3.77), imply the following explicit statement. For every integer \(k\ge4\), every \(0<t\le1\), and
\[
A(p):=2\left(\frac2\pi\right)^{p/2}M(p),\qquad
v_k:=\frac75 k^{2/3},\qquad p=4+t,
\]
one has
\[
I_k(4+t)\le\frac{A(4+t)}t\,v_k^{-t/2}+\frac{578}{1375}.
\tag{1}
\]
Indeed the three additive estimates are respectively bounded by \(3/125\), \(13/55\), and \(4/25\) for \(0<t\le1\); their sum is \(578/1375<1\). The crucial feature of (1) is that its additive error is **uniform in both \(k\) and \(t\)**. This proof invokes Xu's published technical Bessel estimates and does not rederive their long uniform-order asymptotic analysis.

**4. Matching fixed-order lower estimate.** Fix \(m\ge0\) and a sufficiently large fixed \(R>1\). The fixed-order Hankel expansion from Step 2, together with the uniform bound on the primitive of \(|\cos u|^p-M(p)\), shows that there exists a finite constant \(B_m=B_m(R)\), independent of \(0<t\le1\), for which
\[
I_m(4+t)\ge\frac{A(4+t)}tR^{-t/2}-B_m.
\tag{2}
\]
To verify (2), integrate only over \([R,\infty)\). The mean periodic contribution integrates exactly to \(A(4+t)R^{-t/2}/t\). The integrated Hankel error is bounded uniformly by \(C_m\int_R^\infty r^{-2}\,dr\); the centered periodic contribution is bounded by integration by parts against the decreasing weight \(r^{-1-t/2}\), whose endpoint and derivative have uniformly bounded total variation. All estimates are uniform for \(0<t\le1\).

**5. Infinite-order cutoff, then finite comparisons.** Choose an integer \(K>\max\{m+1,4\}\) so large that \(v_K>R\) and
\[
\frac{A(4)}2\log\frac{v_K}{R}>B_m+\frac{578}{1375}+1.
\]
Such \(K\) exists because \(v_K=(7/5)K^{2/3}\to\infty\) and \(A(4)=3/\pi^2>0\). Combining (1) and (2), for all \(k\ge K\),
\[
I_m(4+t)-I_k(4+t)\ge
A(4+t)\frac{R^{-t/2}-v_K^{-t/2}}t
-B_m-\frac{578}{1375}.
\]
The right side extends continuously to \(t=0\) with the strictly positive value prescribed in the choice of \(K\). Hence it is positive uniformly for all \(k\ge K\) whenever \(0<t<\delta_m\) for some \(\delta_m>0\). The remaining finite set \(m<k<K\) is handled by Step 2. Taking the minimum of finitely many positive neighborhoods proves the first assertion, with \(\varepsilon_m>0\).

**6. Sharp stability and its critical scale.** Xu's harmonic decomposition and global stability reduction give the exact coefficient in terms of \(\max_{k\ge1}I_k(p)\). Step 5 with \(m=1\) makes the maximizing nonzero index uniquely \(1\) for \(4<p<4+\varepsilon_1\), yielding the stated formula. It is sharp on pure first harmonics. For \(t=p-4\downarrow0\), the common leading Hankel tail and Step 2 give
\[
I_0(4+t)\sim\frac3{\pi^2t},\qquad I_0(4+t)-I_1(4+t)\longrightarrow\frac2{\pi^2}.
\]
The mean-value theorem applied to \(x\mapsto x^{2/p}\) therefore gives
\[
\lim_{t\downarrow0}\frac{(2\pi)^2\bigl(I_0(4+t)^{2/(4+t)}-I_1(4+t)^{2/(4+t)}\bigr)}{\sqrt t}
=\frac{4\pi}{\sqrt3}.
\]
This completes the proof.

## Verification

The supplied `verify_identity.py` checks symbolically, for formal order and formal Bessel values, the differential identity in Step 1 under the adjacent Bessel recurrences. It also checks the exact rational error sum and critical coefficient normalization. The script was run successfully with SymPy. The uniform-order analytic estimate in Step 3 is an explicitly cited literature input; symbolic and finite numerical checks do not replace its proof. The remaining steps are analytic and do not depend on numerical experiments.

## Relationship to prior work

Xu (2026) proves \(I_0(p)>I_k(p)\) for all nonzero modes at every finite admissible exponent, and full adjacent-order monotonicity in dimensions at least three. In dimension two, Remark 3 identifies the maximizing nonconstant degree as unresolved in general. The present theorem determines that degree on a nonempty **open interval abutting \(p=4\)**. It does not determine the entire remaining range.

The publicly recorded result *Exact critical fourth-moment gaps in circular Fourier extension* establishes Step 1's critical fixed-index differences and associated fixed-index squared gaps. Those results alone do not allow the higher index to depend on \(p\), so they do not imply the all-degrees quantifier in Step 5. Public results identifying the first harmonic at \(p=6\) and for all \(p\ge9\) concern disjoint exponent regimes and likewise do not imply the present near-critical interval. No assertion is made that the classical Bessel recurrence itself is new.

## Limitations

The positive widths \(\varepsilon_m\) are nonconstructive and no optimal thresholds are determined. The theorem does not establish full strict order for every pair of modes simultaneously at one fixed exponent, and it does not settle the intermediate interval between the near-critical range and other established regimes. The proof relies on the uniform high-order bound from Xu's October 2026 preprint, which remains an external analytical premise rather than an independently re-proved lemma here. A different equivalent older uniform-order result could affect the literature novelty assessment; independent mathematical audit has not been performed.

## References

- Z. Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648v1, first posted 2026-10-14; especially Section 3.2 and Remark 3. https://arxiv.org/html/2610.19648
- E. Carneiro, D. Oliveira e Silva, M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365, first posted 2017-10-28, Advances in Mathematics 341 (2019), 583--608. https://arxiv.org/abs/1710.10365
- V. Ciccone, M. Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, arXiv:2312.07309, first posted 2023-12-12; Journal of Fourier Analysis and Applications 31 (2025), article 70. https://arxiv.org/abs/2312.07309
- *Exact critical fourth-moment gaps in circular Fourier extension*, public research result, 2026-11-16. https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-critical-fourth-moment-gaps-in-circular-fourier-extension--4d8d086fa937
- *First-harmonic sharp circular mixed-Fourier stability for every real exponent \(q\ge9\)*, public research result, 2026-11-16. https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-first-harmonic-sharp-circular-mixed-fourier-stability-for-every--f07ac5a86b30
- *First-harmonic sharp sixth-power stability for circular mixed Fourier extension*, public research result, 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-first-harmonic-sharp-sixth-power-stability-for-circular-mixed-fo--02fc40e0dcf1
