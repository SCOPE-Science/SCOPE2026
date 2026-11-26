# Sharp simultaneous tail-weight envelope for subnormal unilateral shifts

## Finding

Let \(W e_j=w_j e_{j+1}\) be a bounded subnormal unilateral weighted shift on complex \(\ell^2(\mathbb N_0)\), with every \(w_j>0\). Fix an index \(n\ge0\) and an a priori cap \(M\ge\|W\|>0\). Set
\[
u=\left(\frac{w_n}{M}\right)^2,\qquad
v=\left(\frac{w_{n+1}}{M}\right)^2.
\]
Then \(0<u\le v\le1\). If \(u<1\), define
\[
x=\frac{u(1-v)}{1-u},\qquad
p=\frac{u-x}{1-x},\qquad
R_k=\frac{p+(1-p)x^{k+1}}{p+(1-p)x^k}\quad(k\ge0).
\]
For every integer \(k\ge2\), simultaneously,
\[
\boxed{w_{n+k}^{\,2}\le M^2 R_k.}
\]
The expression also gives exactly \(w_n^2=M^2R_0\) and \(w_{n+1}^2=M^2R_1\). These are optimal *simultaneous* bounds: for every admissible \(0<u<v<1\) and every \(n\ge0\), a single subnormal weighted shift with \(\|W\|=M\) attains equality for all \(k\ge0\). For \(n=0\), the same holds when \(0<u<v=1\). If \(u=v<1\), the tail is necessarily constant \(w_{n+k}^2=M^2u\), and this is realizable with a cap \(M\). If \(u=1\), every tail weight equals \(M\).

In the nondegenerate regime \(0<u<v<1\), the sharp profile has the exact logistic representation
\[
R_k=x+\frac{1-x}{1+\frac{1-p}{p}x^k},
\quad
K=\frac{\log((1-p)/p)}{\log(1/x)}.
\]
In particular, fixing \(u\in(0,1)\) and writing \(v=u+\delta\) with \(\delta\downarrow0\),
\[
p\sim\frac{u\delta}{(1-u)^2},\qquad
K\sim\frac{\log(1/\delta)}{\log(1/u)}.
\]
Thus a small local increase can coexist with a sharp extremal tail that stays near its earlier plateau for a logarithmically long horizon before approaching the permitted norm cap. This quantifies the distinction between equality-based flatness propagation and near-equality.

## Assumptions and scope

All weights are strictly positive, scalar, and subnormal. The cap \(M\) is not required to equal the actual norm. The index \(n\) is arbitrary and fixed. All upper bounds concern squared weights and integers \(k\ge2\); no claim is made for non-subnormal or general operator-valued shifts. For a genuinely nondegenerate pair \(0<u<v<1\), one has \(0<x<u<1\), \(0<p<1\). In the boundary case \(u<v=1\), \(x=0\); the sharp construction uses \(n=0\). The equal pair \(u=v\) is treated separately.

## Proof

**Step 1: Berger reduction.** Subnormality gives a probability measure \(\mu\) on \([0,M^2]\) with moments \(\gamma_j=\prod_{i<j}w_i^2=\int t^j\,d\mu(t)\). Rescale its variable by \(M^2\), obtaining \(\widetilde\mu\) on \([0,1]\). The normalized \(n\)-tilt
\[
d\nu(t)=\frac{t^n\,d\widetilde\mu(t)}{\int t^n\,d\widetilde\mu(t)}
\]
is a probability measure. If \(m_j=\int t^j\,d\nu(t)\), then
\[
m_0=1,\quad m_1=u,\quad m_2=uv,\quad
\frac{w_{n+k}^2}{M^2}=\frac{m_{k+1}}{m_k}\quad(k\ge0).
\]
The denominator is positive since \(u>0\). Log-convexity of moment sequences gives \(u\le v\), and support in \([0,1]\) gives \(v\le1\).

**Step 2: Endpoint-two-atom comparison.** The unique probability measure of the form
\[
\nu_*=(1-p)\delta_x+p\delta_1
\]
with the first two moments \(u\) and \(uv\) has precisely the displayed \(x,p\). Indeed \(\int t\,d\nu_*=u\) and \(\int t^2\,d\nu_*=uv\). Its moments are \(m_j^*=p+(1-p)x^j\), and \(R_k=m_{k+1}^*/m_k^*\in(0,1]\).

**Step 3: An explicit quadratic upper certificate.** For every integer \(\ell\ge3\), write
\[
P_\ell(t,x)=\sum_{r=0}^{\ell-3}\sum_{j=0}^{r}(j+1)t^{r-j}x^j,
\qquad P_2(t,x)=0.
\]
Direct multiplication shows that
\[
Q_\ell(t)=t^\ell+(1-t)(t-x)^2P_\ell(t,x)
\]
is a polynomial of degree at most two; equivalently it is the quadratic Hermite interpolant of \(t^\ell\), matching its value and derivative at \(x\) and value at \(1\). The formula remains valid at \(x=0\). Since
\[
P_{\ell+1}(t,x)-P_\ell(t,x)
=\sum_{j=0}^{\ell-2}(j+1)t^{\ell-2-j}x^j\ge0,
\]
all \(P_\ell\) are nonnegative on \([0,1]^2\). For \(k\ge2\), put \(h(t)=t^{k+1}-R_kt^k\) and \(Q_h=Q_{k+1}-R_kQ_k\). As \(0<R_k\le1\),
\[
Q_h(t)-h(t)=(1-t)(t-x)^2\bigl(P_{k+1}(t,x)-R_kP_k(t,x)\bigr)\ge0
\]
for \(0\le t\le1\).

**Step 4: Integral comparison.** Because \(Q_h\) has degree at most two and \(\nu\), \(\nu_*\) have equal moments to degree two,
\[
\int h\,d\nu\le\int Q_h\,d\nu
=\int Q_h\,d\nu_*=\int h\,d\nu_*=0.
\]
The last equality holds because \(R_k=m_{k+1}^*/m_k^*\), and the middle equality with \(h\) holds because the certificate vanishes at the support points \(x,1\). Division by \(m_k>0\) proves \(m_{k+1}/m_k\le R_k\), hence the bound for every \(k\ge2\). For \(0<x<1\), the positive factor in the certificate is strictly positive off \(\{x,1\}\) for \(k\ge2\), so equality at any one such \(k\) forces \(\nu\) to be exactly the two-atom measure \(\nu_*\).

**Step 5: Sharpness at any index.** At \(n=0\), take \(\widetilde\mu=\nu_*\); its strictly positive moments define a subnormal weighted shift with the claimed initial pair and equality at all later indices. If \(n>0\) and \(x>0\), choose instead
\[
d\widetilde\mu(t)=\frac{t^{-n}\,d\nu_*(t)}{\int t^{-n}\,d\nu_*(t)}.
\]
Its \(n\)-tilt is \(\nu_*\), giving simultaneous equality and actual norm \(M\) because \(p>0\) puts positive mass at the cap. If \(u=v<1\), the variance \(uv-u^2\) of \(\nu\) vanishes, so \(\nu=\delta_u\), forcing constant tail; a constant-weight shift realizes it. The case \(u=1\) follows from support bounded by one.

**Step 6: Boundary layer.** With \(v=u+\delta\), one has \(x=u-u\delta/(1-u)\) exactly and \(p=u\delta/((1-u)^2+u\delta)\). Consequently \(p\sim u\delta/(1-u)^2\), while \(\log(1/x)\to\log(1/u)>0\), yielding the formula for \(K\) and the exact logistic profile.

## Verification

Run `python verify.py` with Python 3. The standalone checker uses exact rational arithmetic to verify the Hermite certificate polynomial cancellations and constraints for 70 symbolic parameter-degree cases; it also tests the moment-envelope inequality on 400 seeded finite atomic measures for 11 future indices and checks equality for the corresponding two-atom laws. It reports 8,870 exact checks. Those finite checks corroborate, but do not replace, the universal proof above.

## Relationship to prior work

Curto, Ech-charyfy, El Azhar and Zerouali (2025) give qualitative equality-propagation and structural decomposition theorems for weighted shifts, including matrix-valued extensions. The present result instead solves a cap-conditioned extremal problem for **arbitrary fixed two adjacent scalar weights**, providing a single sharp profile for all later indices and an explicit near-flatness delay. This uses the classical Berger-measure representation, not a new representation theorem. Lee and Yoon (2016) discuss two-atomic type-abc completions and multivariable recursion, which motivates checking the two-atom extremizer but does not establish the stated universal bound in the material available. Benhida, Curto and Exner (2025) study signed representing charges rather than sharp ratios under fixed first two positive moments. The possibility of an equivalent result in older truncated Hausdorff moment optimization literature is not eliminated.

## Limitations

The scalar subnormality assumption and fixed cap are essential to the argument. Only the sharp **upper** profile is obtained; no optimal lower profile or extension to finite-order hyponormality is asserted. The endpoint \(x=0\) cannot be realized by inverse tilting at a positive index. No assertion of independent peer review or proof certification is made. Literature-search noncoverage alone does not establish publication priority, and the complete 2016 article was not accessible.

## References

1. R. E. Curto, A. Ech-charyfy, H. El Azhar, and E. H. Zerouali, *Propagation Phenomena for Operator-Valued Weighted Shifts*, Results in Mathematics 81, 16 (2026), first public 13 December 2025, https://doi.org/10.1007/s00025-025-02572-6.
2. C. Benhida, R. E. Curto, and G. R. Exner, *Signed Representing Measures (Berger-Type Charges) in Subnormality and Related Properties of Weighted Shifts*, Results in Mathematics 81, 17 (2026), https://doi.org/10.1007/s00025-025-02574-4.
3. S. H. Lee and J. Yoon, *Recursiveness and propagation for 2-variable weighted shifts*, Linear Algebra and Its Applications 504 (2016), 228–247, https://doi.org/10.1016/j.laa.2016.04.006.
