# Exact two-cycle census and a universal expanding Floquet multiplier for quadratic-delay maps

## Finding

A quadratic delay recurrence has a complete real primitive-two-cycle classification, with a universal expanding direction at **every** nontrivial two-cycle. For all real parameters \(a,u,v,d\) with \(u\ne0\), define
\[
G(r,s)=(ar+f(s),r),\qquad f(t)=ut^2+vt+d.
\]
Set
\[
S=\frac{1+a-v}{u},\quad
\Delta=\frac{(v-1)^2+2a(v-1)-3a^2-4ud}{u^2},\quad K=u^2\Delta,\quad H=2[1+(1+a)^2].
\]
There is exactly one (unordered) real primitive two-cycle if \(\Delta>0\), consisting of \((p,q)\) and \((q,p)\) where
\[
p=\frac{S+\sqrt\Delta}{2},\qquad q=\frac{S-\sqrt\Delta}{2}.
\]
If \(\Delta\le0\), no primitive two-cycle exists. At an existing two-cycle, the two-step Floquet characteristic polynomial is exactly
\[
\chi(\lambda)=(\lambda-1)(\lambda-(1+a)^2)-K.
\]
Thus both multipliers are real and distinct, with \(\mu_-<1<\mu_+\) (indeed \(\mu_+>\max\{1,(1+a)^2\}\)). The orbit is a hyperbolic saddle for \(0<K<H\), nonhyperbolic but unstable for \(K=H\), and a hyperbolic repeller for \(K>H\). It is never locally asymptotically attracting.

For the Liu--Zhong two-parameter system [1]
\[
F_{a,b}(x,y)=\left(ax+\frac32 y,\,b(x-x^2)\right),\qquad ab\ne0,
\]
write \(c=3b/2\), \(h=c-(1-a)\), and \(Q=6a^2+4a+4>0\). There is exactly one real primitive two-cycle if and only if \(|h|>2|a|\). Its exact classification is:

- \(2|a|<|h|<\sqrt Q\): hyperbolic saddle;
- \(|h|=\sqrt Q\): nonhyperbolic, with one multiplier \(-1\) and another greater than \(1\);
- \(|h|>\sqrt Q\): hyperbolic repeller.

At parameters outside those regions there is no primitive real two-cycle. The bounds are strict and exhaustive, including negative \(a,b\) and parameter degeneracies other than the excluded \(ab=0\). The orbit points of \(F\) are
\[
\left(p,\frac23(q-ap)\right),\quad
\left(q,\frac23(p-aq)\right),
\]
where \(p,q=S/2\pm\sqrt\Delta/2\) with \(u=-c,v=c,d=0\). No primitive real two-cycle of the published map is attracting.

A rational witness is \(a=-1/5\), \(b=79/150\) (thus \(c=79/100\)). The alternating scalar coordinates are \(p=4/79\), \(q=-5/79\), and the full-plane two-step Floquet multipliers are
\[
\mu_\pm=\frac{82\pm9\sqrt5}{100},\qquad \mu_+>1.
\]
This example lies strictly below \(b=\frac23(1+a)=8/15\), the flip threshold in [1], yet the primitive period-two orbit is a saddle, not an attracting cycle.

## Assumptions and scope

All states and parameters are real. A primitive two-cycle means two distinct points mapped to one another and not fixed; two points of the same orbit are counted as one cycle. Floquet multipliers refer to the full two-dimensional derivative of the second iterate, **not** an arbitrarily restricted invariant curve. We require \(u\ne0\) for the general classification; the specialization to [1] assumes its published restriction \(a,b\ne0\).

## Proof

1. **Reduction and census.** If \((p,q)\leftrightarrow(q,p)\) is a primitive cycle of \(G\), then
\[
p=aq+f(p),\qquad q=ap+f(q).
\]
Subtracting these equations and dividing by \(p-q\ne0\) gives
\[
1+a=\frac{f(p)-f(q)}{p-q}=u(p+q)+v,
\]
so \(p+q=S\). Adding gives \((1-a)S=u(S^2-2pq)+vS+2d\), hence
\[
pq=\frac{uS^2+(v+a-1)S+2d}{2u}.
\]
The discriminant \((p-q)^2=S^2-4pq\) simplifies to exactly \(\Delta\). Conversely any two distinct real roots of this sum/product pair satisfy the summed and subtracted equations, hence both original equations. Therefore \(\Delta>0\) is necessary and sufficient and yields precisely one cycle; \(\Delta=0\) is a fixed point, not a primitive cycle.

2. **Exact two-step spectrum.** At state \((r,s)\) the derivative is
\[
DG(r,s)=\begin{pmatrix}a&f'(s)\\1&0\end{pmatrix}.
\]
Over one primitive cycle, the product of the two alternating derivative matrices has trace \(a^2+f'(p)+f'(q)=a^2+2v+2uS=1+(1+a)^2\), and determinant \(f'(p)f'(q)=(1+a)^2-u^2(p-q)^2\). These equalities give the polynomial \(\chi\) above. Because \(K>0\), \(\chi(1)=-K<0\), while \(\chi(\lambda)\to+\infty\) as \(\lambda\to\pm\infty\); therefore its two real roots straddle \(1\). Moreover evaluating at \((1+a)^2\) is also negative, so the larger root is greater than both base roots. At \(-1\),
\[
\chi(-1)=2[1+(1+a)^2]-K=H-K.
\]
Since the larger multiplier is \(>1\), the smaller lies above, at, or below \(-1\) exactly when \(K<H\), \(K=H\), or \(K>H\). This proves each full-state stability classification and excludes attraction, including the nonhyperbolic boundary where the larger multiplier still expands.

3. **Specialization.** The scalar first-coordinate recurrence for [1] is \(x_{n+2}=a x_{n+1}+c x_n(1-x_n)\), which is conjugate to \(G\) by the global invertible linear change \((x,y)\mapsto(ax+3y/2,x)\). Substituting \(u=-c,v=c,d=0\) yields
\[
K=(c-1-a)(c-1+3a)=[c-(1-a)]^2-4a^2=h^2-4a^2.
\]
Consequently \(K>0\iff |h|>2|a|\). The saddle criterion \(K<H\) is equivalent to \(h^2<4a^2+2[1+(1+a)^2]=6a^2+4a+4=Q\). Here \(Q-4a^2=2[(a+1)^2+1]>0\), so the regions are well ordered and nonempty whenever the corresponding value of \(c\ne0\) is admissible. The conjugacy gives the stated orbit points and preserves Floquet spectra. Substitution of \(a=-1/5,c=79/100\) verifies the rational witness and polynomial \(\chi(\lambda)=\lambda^2-41\lambda/25+6319/10000\), whose roots are the stated radicals.

## Verification

Run the included self-contained source file `check.py` with Python 3 and SymPy:

```sh
python check.py
```

It verifies symbolic discriminant and Jacobian-product identities, the exact specialized discriminant, and the rational witness. It additionally verifies the claimed exact Floquet polynomial against 129 deterministic quadratic parameter samples admitting real primitive cycles. The analytic proof above—not these finite tests—establishes all quantified statements.

## Relationship to prior work

Liu and Zhong [1] introduce the exact map, derive equilibrium bifurcation conditions, and in their Theorem 5 describe the period-two branch as stable for negative \(a\) to the left of the flip threshold. The complete two-cycle census and full-state return spectrum above instead give a genuinely expanding multiplier at every nontrivial cycle. The explicit rational parameter witness lies in that indicated region. This comparison addresses precisely the stated full-plane stability of primitive two-cycles; it does not deny the occurrence of an equilibrium multiplier crossing \(-1\) or any separate one-dimensional restricted dynamics.

Bektešević, Kulenović and Pilav [2] classify dynamics of a general quadratic second-order equation **with nonnegative coefficients and nonnegative initial states**. That regime includes earlier saddle results for certain positive-cone period-two states but does not cover the signed quadratic term \(-cx_n^2\) paired with \(+cx_n\) here. Their subsequent cubic study [3] extends positive-coefficient methods and similarly does not furnish an all-real signed-quadratic Floquet classification. The structural calculation is elementary but its universal signed-parameter and explicit two-parameter consequences go beyond these inspected assertions.

## Limitations

No global orbit or basin classification is claimed beyond the exact primitive period-two census. The nonhyperbolic boundary does not determine higher-order local normal forms, although the separate expanding multiplier already excludes attraction. Priority remains provisional: unindexed classical results on quadratic delay recurrences may contain an equivalent theorem. Independent verification by another party has not been carried out.

## References

[1] L. Liu and X. Zhong, *Research on Stability and Bifurcation for Two-Dimensional Two-Parameter Squared Discrete Dynamical Systems*, Mathematics **12** (2024), 2423. https://doi.org/10.3390/math12152423 (first publicly dated 4 August 2024).

[2] J. Bektešević, M. R. S. Kulenović and E. Pilav, *Global dynamics of quadratic second order difference equation in the first quadrant*, Applied Mathematics and Computation **227** (2014), 50–65. https://doi.org/10.1016/j.amc.2013.10.048.

[3] J. Bektešević, M. R. S. Kulenović and E. Pilav, *Global dynamics of cubic second order difference equation in the first quadrant*, Advances in Difference Equations **2015**, 176. https://doi.org/10.1186/s13662-015-0503-x.
