# The complete affine-shift covariance spectrum of squarefree monic cubics

## Finding

For every prime power \(q\), let \(\mathcal M_3\) be the monic cubics over \(\mathbb F_q\). Write \(\operatorname{sf}(f)=1\) when \(f\) is squarefree, and \(0\) otherwise. For every nonzero affine shift \(h(T)=uT+v\), define
\[
 C_q(u,v)=\sum_{f\in\mathcal M_3}\operatorname{sf}(f)\operatorname{sf}(f+h),\qquad
 \Delta_q(u,v)=C_q(u,v)-q(q-1)^2.
\]
The quantity \(\Delta_q/q^3\) is the covariance of the two squarefree indicators under uniformly random monic cubics. Define \(R_q(z)=\#\{d\in\mathbb F_q^\times:d^3=z\}\) for nonzero \(z\).

If \(q\) is odd, then
\[
 \Delta_q(u,v)=\begin{cases}
 -1,&u\ne0,\\
 q(R_q(2v)-1),&u=0,\ v\ne0.
 \end{cases}
\]
If \(q\) is even, then
\[
 \Delta_q(u,v)=\begin{cases}0,&u\ne0,\\-q,&u=0,\ v\ne0.\end{cases}
\]
These formulae yield every frequency in the full covariance spectrum. In odd characteristic, \(q(q-1)\) shifts have covariance \(-1\). If \(3\nmid q-1\), the other \(q-1\) shifts have covariance \(0\). If \(3\mid q-1\), among these constant shifts exactly \((q-1)/3\) have covariance \(2q\) and exactly \(2(q-1)/3\) have covariance \(-q\). In even characteristic, \(q(q-1)\) shifts have covariance \(0\), and \(q-1\) have covariance \(-q\). Frequencies count shifts \((u,v)\), not underlying cubics.

## Assumptions and scope

The field \(\mathbb F_q\) is arbitrary, including nonprime and characteristic-two fields. All cubics are monic of degree exactly three; \(h\) has degree at most one and must be nonzero. There are \(q^3\) monic cubics, each squarefree with probability \(1-1/q\). The baseline \(q(q-1)^2\) is thus the product-of-marginals benchmark, not an asymptotic truncation. No claim concerns higher-degree polynomials or quadratic shifts.

## Proof

**1. A repeated-root parametrization.** A non-squarefree cubic must have a repeated linear factor over \(\mathbb F_q\): a repeated irreducible factor of degree at least two would already have degree at least four. That repeated root is unique, even for a triple root. Hence there is a bijection
\[
 (r,t)\in\mathbb F_q^2\longmapsto (T-r)^2(T-t)
\]
onto non-squarefree monic cubics. Precisely \(q^2\) cubics are not squarefree. Let \(I_q(u,v)\) count cubics such that both \(f\) and \(f+h\) are not squarefree. Inclusion--exclusion gives
\[
 C_q(u,v)=q^3-2q^2+I_q(u,v),\qquad \Delta_q(u,v)=I_q(u,v)-q.
\]

**2. Odd characteristic.** Write a cubic with repeated root \(r\) as
\[
 f(T)=(T-r)^2(T+a+2r)
 =T^3+aT^2+(-2ar-3r^2)T+(ar^2+2r^3).
\]
If \(f+h\) has repeated root \(s\), then \(s\ne r\): a common repeated root would imply \(h(r)=h'(r)=0\), which for a nonzero polynomial of degree at most one is impossible. Put \(d=s-r\ne0\) and \(t=s+r\). Comparing the linear and constant coefficients of the two repeated-root expansions gives
\[
 u=-d(2a+3t),\qquad
 v=d\bigl(at+2(s^2+sr+r^2)\bigr).
\]
Since \(s^2+sr+r^2=(3t^2+d^2)/4\), elimination of \(a\) yields the single equation
\[
 d^3=ut+2v.
\]
Conversely, each solution \((d,t)\in\mathbb F_q^\times\times\mathbb F_q\) determines uniquely
\[
 r=(t-d)/2,\quad s=(t+d)/2,\quad
 a=-(u/d+3t)/2,
\]
so it determines a unique cubic counted by \(I_q(u,v)\). This inverse construction works in characteristic three as well. For \(u\ne0\), each of the \(q-1\) nonzero values \(d\) determines exactly one \(t\), so \(I_q=q-1\). For \(u=0\) and \(v\ne0\), there are \(R_q(2v)\) permitted choices of \(d\), each with \(q\) choices of \(t\); hence \(I_q=qR_q(2v)\). Substitution into \(\Delta=I_q-q\) proves both odd-characteristic cases.

**3. Characteristic two.** A cubic with repeated root \(r\) has the unique form
\[
 (T-r)^2(T+a)=T^3+aT^2+r^2T+ar^2.
\]
For the shifted cubic to have a repeated root \(s\), its coefficient equations are
\[
 s^2-r^2=u,\qquad a(s^2-r^2)=v.
\]
The squaring map of every finite field of characteristic two is bijective. If \(u\ne0\), for each \(r\) there is a unique \(s\), and \(a=v/u\); thus \(I_q=q\). If \(u=0\) and \(v\ne0\), the equations are inconsistent and \(I_q=0\). Therefore the even-characteristic formula follows.

**4. Frequencies.** On \(\mathbb F_q^\times\), the cube map has kernel of size \(g=\gcd(3,q-1)\), so \(R_q(z)\) is \(g\) on its image and zero otherwise. When \(q\) is odd, multiplication by \(2\) permutes the nonzero field elements. Counting its cube values gives the stated multiplicity spectrum. There are \(q(q-1)\) shifts with \(u\ne0\) and \(q-1\) remaining nonzero constant shifts. No unexamined cases remain.

## Verification

The included self-contained Python 3 file `verify.py` implements arithmetic in finite fields and tests squarefreeness via polynomial gcd with the formal derivative, independently of the repeated-root counting proof. It compares direct enumeration against the asserted formula for all nonzero affine shifts over fields of orders \(2,3,4,5,7,8,9\) and selected shifts over \(11,13,16,25\). Its tested outcome is `VERIFY_OK finite_fields=11 cases=293 tested_cubics=413477`. Run `python3 verify.py` to reproduce. This finite check corroborates but does not establish the theorem for untested fields; the preceding argument is the proof for all prime powers.

## Relationship to prior work

Carmon and Rudnick [1] study correlations of polynomial Möbius *signs*, prove large-field results, and discuss simultaneous discriminant vanishing. Their full text addresses general-degree critical-point collisions but does not give the present exact degree-three squarefree-indicator covariance spectrum. Keating and Rudnick [2] explicitly study the squarefree-indicator pair sum for \(f\) and \(f+J\) in Appendix A; their formula is an asymptotic in polynomial degree with a singular series and an error term. An asymptotic does not yield the exact characteristic-sensitive fixed-degree-three formula here. Carmon [3] treats Möbius signs in characteristic two. Bary-Soroker and Stix [4] count **simultaneously irreducible** cubic pairs for particular shifts, a different property from being squarefree. None of the inspected statements immediately implies the displayed complete affine-shift spectrum; possible implicit equivalences in broader literature remain unexcluded.

## Limitations

Only monic cubics and nonzero affine shifts are classified. The result does not determine higher-degree correlations, distinguish irreducibility within squarefree cubics, or resolve sign correlations. The originality assessment is best-knowledge and does not establish uniqueness against all historical literature. Computational cases are finite. No independent audit has been performed.

## References

[1] M. Carmon and Z. Rudnick, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field*, arXiv:1205.1599 (first public version, 2012-05-08), https://arxiv.org/abs/1205.1599.

[2] J. P. Keating and Z. Rudnick, *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions*, arXiv:1504.03444 (first public version, 2015-04-14), https://arxiv.org/abs/1504.03444; especially Appendix A.

[3] M. Carmon, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field in characteristic 2*, arXiv:1409.3694 (2014), https://arxiv.org/abs/1409.3694.

[4] L. Bary-Soroker and J. Stix, *Cubic twin prime polynomials are counted by a modular form* (2017); analysis of irreducible cubic pairs, not simultaneous squarefreeness.
