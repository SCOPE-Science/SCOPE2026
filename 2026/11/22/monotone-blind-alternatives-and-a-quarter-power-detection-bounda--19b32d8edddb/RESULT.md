# Monotone blind alternatives and a quarter-power detection boundary for a uniformity U-statistic

## Finding

Consider the complete-data scalar uniformity statistic of Kattumannil and Sreedevi, defined for independent observations in \([0,1]\) by
\[
U_n=\binom{n}{2}^{-1}\sum_{1\le i<j\le n}h(X_i,X_j),\qquad
h(x,y)=\max\{x,y\}-x-y+\tfrac12(x^2+y^2).
\]
Its population target is \(\Delta(F)=\mathbb E_F h(X_1,X_2)\). The statistic is centered at zero under the uniform null, but a one-parameter family of **strictly increasing, everywhere-positive polynomial densities** has exactly the same zero target. Moreover, along linear density perturbations of the null, its sharp detection scale is \(n^{-1/4}\), rather than the conventional \(n^{-1/2}\).

Precisely, for \(0<r<1/3\), define
\[
\begin{aligned}
c_r&=\frac{14r}{7+r^2}, & d_r&=\frac{14r^2}{7+r^2},\\
f_r(x)&=1+c_r(2x-1)+d_r(6x^2-6x+1),&0\le x\le1.
\end{aligned}
\]
Then \(f_r\) is a strictly positive, strictly increasing probability density, its CDF satisfies \(F_r(x)<x\) for every \(0<x<1\), and \(\Delta(F_r)=0\). In particular, \(r=1/4\) gives the exact example
\[
f_{1/4}(x)=\frac{84x^2+28x+71}{113},\qquad
F_{1/4}(x)=\frac{28x^3+14x^2+71x}{113}.
\]
For every such fixed alternative, \(\sqrt n U_n\Rightarrow N(0,V(r))\) with
\[
V(r)=\frac{56595+80311r^4-6282r^6}{7425(7+r^2)^3}
\quad\text{and}\quad 0<V(r)<\frac1{45}.
\]
Therefore the published two-sided normal-calibrated level-\(\alpha\) test has limiting rejection probability
\[
2\Phi\!\left(-\frac{z_{1-\alpha/2}}{\sqrt{45V(r)}}\right)<\alpha<1
\quad (0<\alpha<1),
\]
not power one. At \(r=1/4\), \(V=233091814/10713510225\), and the limiting rejection probability at nominal \(5\%\) is approximately \(0.04761\).

For the alternative densities \(f_c(x)=1+c(2x-1)\), \(|c|\le1\), the target is \(\Delta(F_c)=-c^2/30\) exactly. If \(c_n=h n^{-\gamma}\), where \(h\ne0\) is fixed and \(\gamma>0\), the normal-calibrated two-sided test has limiting rejection probability \(\alpha\) when \(\gamma>1/4\), strictly between \(\alpha\) and \(1\) when \(\gamma=1/4\), and \(1\) when \(0<\gamma<1/4\). At the critical scale,
\[
\sqrt{45n}\,U_n\Rightarrow N\!\left(-\frac{h^2}{2\sqrt5},1\right).
\]
These properties refer specifically to this scalar \(U\)-statistic and its usual asymptotic normal critical value, not to integrated-squared characterization tests or to censoring-adjusted statistics.

## Assumptions and scope

For every integer \(n\ge2\), samples are independent and identically distributed, real, and supported on \([0,1]\). The null is the fully specified \(\operatorname{Uniform}(0,1)\) law. In the fixed-alternative result, \(r\in(0,1/3)\) is held constant as \(n\to\infty\). In the local-alternative result, \(c_n=h n^{-\gamma}\) and the corresponding row-wise independent samples follow \(f_{c_n}\), which is a valid density for all sufficiently large \(n\). The rejection rule is \(\sqrt{45n}\,|U_n|>z_{1-\alpha/2}\), where \(z_p\) denotes the standard normal \(p\)-quantile and \(0<\alpha<1\).

## Proof

**1. Exact population target.** For two independent observations with CDF \(F\),
\[
\mathbb E\max(X_1,X_2)=1-\int_0^1F(x)^2\,dx.
\]
For the two-parameter polynomial density
\[
f_{c,d}(x)=1+c(2x-1)+d(6x^2-6x+1)
\]
whenever it is nonnegative, its CDF is
\[
F_{c,d}(x)=x+c(x^2-x)+d(2x^3-3x^2+x).
\]
Direct polynomial integration gives
\[
\begin{aligned}
\mathbb EX&=\tfrac12+\tfrac c6,&
\mathbb EX^2&=\tfrac13+\tfrac c6+\tfrac d{30},\\
\int_0^1F_{c,d}(x)^2dx
&=\tfrac13-\tfrac c6+\tfrac{c^2}{30}-\tfrac d{30}+\tfrac{d^2}{210}.
\end{aligned}
\]
Thus, using \(\Delta(F)=\mathbb E\max(X_1,X_2)-2\mathbb EX+\mathbb EX^2\),
\[
\boxed{\Delta(F_{c,d})=\frac d{15}-\frac{c^2}{30}-\frac{d^2}{210}.}
\]
The zero equation is exactly \(14d=7c^2+d^2\). The stated rational parametrization \(d=rc\), \(c=14r/(7+r^2)\) solves it.

**2. Monotonicity and separation from uniformity.** If \(0<r<1/3\), then \(c_r>0\), \(d_r=rc_r>0\), and
\[
f'_r(x)=2c_r-6d_r+12d_rx\ge2c_r(1-3r)>0.
\]
The minimal density value is \(f_r(0)=1-c_r+d_r=(7-14r+15r^2)/(7+r^2)>0\), since the numerator is positive for all real \(r\). Moreover,
\[
F_r(x)-x=-x(1-x)[c_r+d_r(2x-1)]<0
\quad(0<x<1),
\]
since \(c_r>d_r\). Therefore every member is nonuniform and is strictly shifted to the right of the uniform law in first-order stochastic order, despite the exact zero target. The displayed rational example is obtained by substituting \(r=1/4\).

**3. Fixed-alternative limiting variance and rejection probability.** For continuous strictly positive \(f\), let
\[
L_F(x)=2xF(x)+2\int_x^1yf(y)\,dy-2x+x^2.
\]
The standard first Hoeffding projection of the bounded kernel \(h\) is half of \(L_F(x)\), up to an additive constant. Hence the nondegenerate \(U\)-statistic central limit theorem gives
\[
\sqrt n(U_n-\Delta(F))\Rightarrow
N(0,\operatorname{Var}_F(L_F(X))).
\]
Here nondegeneracy follows from \(L'_F(x)=2[F(x)+x-1]\), which is not identically zero on \([0,1]\) for a strictly positive density. Substituting \(f_r\), integrating the polynomial \(L_F(x)^2f_r(x)\), and subtracting its squared mean yields the stated rational \(V(r)\). Its derivative is
\[
V'(r)=\frac{-14r(30319r^4-160622r^2+24255)}{7425(7+r^2)^4}<0
\quad(0<r<1/3),
\]
because the bracket exceeds \(24255-160622/9>0\) on that interval. Since \(V(0)=1/45\), \(0<V(r)<1/45\). With \(\Delta(F_r)=0\), applying the continuous mapping theorem to the usual null-normal critical value proves the limiting rejection probability. In particular the test is not consistent against any of these fixed monotone alternatives.

**4. Sharp local detection scale.** Setting \(d=0\) in the exact target gives \(\Delta(F_c)=-c^2/30\). For a triangular array from \(f_{c_n}\), Hoeffding's decomposition writes
\[
U_n-\Delta(F_{c_n})=\frac2n\sum_{i=1}^n
\bigl(\mathbb E[h(X_i,Y)\mid X_i]-\Delta(F_{c_n})\bigr)+R_n,
\]
where \(\mathbb E R_n^2=O(n^{-2})\) uniformly in \(|c_n|\le1\), since \(h\) is uniformly bounded. Its row-wise independent, bounded, centered first projections converge uniformly to the uniform-null projection. Lindeberg's triangular-array theorem therefore implies
\[
\sqrt n\bigl(U_n-\Delta(F_{c_n})\bigr)
\Rightarrow N(0,1/45).
\]
The deterministic drift is \(\sqrt{45n}\,\Delta(F_{c_n})=-h^2n^{1/2-2\gamma}/(2\sqrt5)\). This proves the three regimes and the critical shifted normal law. The critical two-sided rejection probability is
\[
\Pr\left(\left|Z-\frac{h^2}{2\sqrt5}\right|>z_{1-\alpha/2}\right)
\quad\text{for }Z\sim N(0,1),
\]
which lies strictly between \(\alpha\) and \(1\) when \(h\ne0\).

## Verification

The standalone `VERIFY_CODE.py` uses exact rational-polynomial arithmetic in SymPy to test the population target in two independent ways (the CDF squared-integral and direct two-dimensional kernel integration), the polynomial blind family and example, the Hoeffding projection variance including its derivative, and equivalence to the published order-statistic formula on deterministic rational samples. It passed 18 exact-arithmetic assertions. These algebraic checks are supplementary to the proof of the uniform bounds and limiting theorems; no finite computation is represented as a proof of convergence.

Reproduce with `python VERIFY_CODE.py` after installing SymPy. No random-number seed or simulation is needed.

## Relationship to prior work

Kattumannil and Sreedevi (arXiv preprint publicly posted 2021-06-11; subsequent 2023 journal article) define and asymptotically calibrate this complete-data \(U\)-statistic, and also formulate a censored-data counterpart. The cited scalar statistic has a zero mean at uniformity. The new result proves that this zero is **not unique**, even among strictly positive, strictly increasing smooth densities, and quantifies the resulting fixed- and local-alternative power behavior.

Ebner and Liebenberg's earlier beta-characterization method uses an integrated squared function of the threshold, rather than this single scalar \(U\)-statistic. Its positive integrated discrepancy is not annihilated by the scalar cancellation constructed here. More general non-identification of scalar contrasts does not by itself supply the explicit monotone polynomial family, sharp quarter-power detection threshold or exact power constants. This is not a general failure claim about every characterization-based test.

## Limitations

The finding does not analyze the censoring-corrected version, estimation of an unknown uniform endpoint, exact finite-sample quantiles, or the consistency of other uniformity tests. The fixed-alternative rejection probabilities assume the usual null-normal calibration rather than a differently selected adaptive threshold. Independent verification of scientific novelty has not been performed. Generic asymptotic theory for \(U\)-statistics is used as a standard ingredient, not claimed as new.

## References

1. S. K. Kattumannil and E. P. Sreedevi, *A new goodness of fit test for uniform distribution with censored observations*, arXiv:2106.06368 (first public version 2021-06-11), https://arxiv.org/abs/2106.06368.
2. E. P. Sreedevi and S. K. Kattumannil, *Goodness of fit test for uniform distribution with censored observation*, Journal of the Korean Statistical Society 52 (2023), 382–394, https://doi.org/10.1007/s42952-023-00205-8.
3. B. Ebner and S. C. Liebenberg, *On a new test of fit to the beta distribution*, Stat 10 (2021), e341, first published 2020-12-02, https://doi.org/10.1002/sta4.341.
