# A three-regime summatory law for generalized Dineva divisor weights

## Finding

For every fixed real \(t\), define the generalized Dineva divisor weight
\[
F_t(n)=\sum_{d\mid n}\frac{\mu(d)^2d^t}{\varphi(d)}
=\prod_{p\mid n}\left(1+\frac{p^t}{p-1}\right),
\qquad S_t(X)=\sum_{1\le n\le X}F_t(n).
\]
The finite Euler product is the identity of Pain (2026), with his parameter \(s=-t\). The new claim is the following complete asymptotic trichotomy, for each fixed real \(t\):
\[
S_t(X)\sim \begin{cases}
C_tX,&t<1,\\
X\log X,&t=1,\\
\zeta(t)X^t/t,&t>1,
\end{cases}
\qquad C_t=\prod_p\left(1+\frac{p^{t-1}}{p-1}\right).
\]
For \(t=1\), the stronger two-term formula is
\[
S_1(X)=X\log X+\left(2\gamma-1+\sum_p\frac{\log p}{p(p-1)}\right)X
+O_\varepsilon(X^{1/2+\varepsilon}).
\]
For each fixed \(t>1\), a power-saving form is
\[
S_t(X)=\frac{\zeta(t)}{t}X^t+
O_{t,\varepsilon}\left(X^{\max\{1,t-1/2\}+\varepsilon}\right).
\]
The Euler product defining \(C_t\) converges absolutely for \(t<1\); the displayed prime sum converges absolutely. All conclusions hold without unproved hypotheses.

## Assumptions and scope

Here \(\mu\) is the Möbius function, \(\varphi\) is Euler's totient, \(\zeta\) the Riemann zeta function in its real convergent domain, and \(\gamma\) Euler's constant. The real parameter \(t\) is held fixed as \(X\to\infty\). For each \(\varepsilon>0\), the constants implicit in big-O may depend on the displayed fixed parameters. The \(t<1\) assertion does not claim an error term uniform as \(t\uparrow1\), and the \(t>1\) assertion is not uniform as \(t\downarrow1\).

## Proof

**1. A single multiplicative correction kernel.** Put \(a(n)=\mu(n)^2n/\varphi(n)\). Let \(h\) be multiplicative, with
\[
h(1)=1,\quad h(p)=\frac1{p-1},\quad h(p^2)=-\frac{p}{p-1},\quad h(p^j)=0\ (j\ge3).
\]
A prime-power check shows \(a=\mathbf1*h\), where \(\mathbf1(n)=1\), and hence \(F_1=\mathbf1*a=\tau*h\), with \(\tau=\mathbf1*\mathbf1\). The Dirichlet series of \(h\) is
\[
H(z)=\prod_p\left(1+\frac{p^{-z}}{p-1}-\frac{p^{1-2z}}{p-1}\right).
\]
For every fixed \(\sigma>1/2\), \(\sum_{n\ge1}|h(n)|/n^\sigma<\infty\): its prime-local deviation from one is \(O(p^{-1-\sigma}+p^{-2\sigma})\). At \(z=1\), **each** local factor equals exactly one, so \(H(1)=1\). Termwise differentiation is permitted in a neighborhood of one. As each local factor is one at one,
\[
H'(1)=\sum_p\frac{\log p}{p(p-1)}.
\]
The sign of this derivative is positive: the derivative of the negative quadratic prime term contributes twice the magnitude of the derivative of the positive linear term.

**2. Mean of the basic squarefree coefficient.** The convolution and the absolute convergence above imply
\[
A(y):=\sum_{n\le y}a(n)
=\sum_{d\le y}h(d)\lfloor y/d\rfloor
=yH(1)+O_\varepsilon(y^{1/2+\varepsilon})
=y+O_\varepsilon(y^{1/2+\varepsilon}).
\]
Indeed, choose \(1/2<\sigma<\min(1,1/2+\varepsilon)\). The floor error is at most \(\sum_{d\le y}|h(d)|\le y^\sigma\sum_d|h(d)|/d^\sigma\), and the omitted tail \(y\sum_{d>y}|h(d)|/d\le y^\sigma\sum_d|h(d)|/d^\sigma\).

**3. Subcritical parameter.** Write \(a_t(d)=\mu(d)^2d^t/\varphi(d)=d^{t-1}a(d)\ge0\). Then \(F_t=\mathbf1*a_t\), so exactly
\[
S_t(X)=\sum_{d\le X}a_t(d)\lfloor X/d\rfloor.
\]
If \(t<1\), \(\sum_d a_t(d)/d=C_t<\infty\): the Euler factor is \(1+p^{t-1}/(p-1)\), and the prime sum converges by comparison with \(\sum_p p^{t-2}\). Divide the floor identity by \(X\); for each fixed \(d\), \(\lfloor X/d\rfloor/X\to1/d\), while \(0\le\lfloor X/d\rfloor/X\le1/d\). Dominated convergence for series gives \(S_t(X)/X\to C_t\).

**4. Supercritical parameter.** For \(t>1\), Abel summation of Step 2 gives
\[
A_t(y):=\sum_{d\le y}a_t(d)=\frac{y^t}{t}+
O_{t,\varepsilon}(y^{t-1/2+\varepsilon})
\qquad(y\ge2).
\]
The estimate also remains true after enlarging its implicit constant for \(1\le y<2\). Reverse the exact divisor summation:
\[
S_t(X)=\sum_{m\le X}A_t(X/m)
=\frac{X^t}{t}\sum_{m\le X}m^{-t}+
O_{t,\varepsilon}\left(X^{t-1/2+\varepsilon}\sum_{m\le X}m^{-t+1/2-\varepsilon}\right).
\]
Completing the convergent zeta tail costs \(O_t(X)\). The remaining sum is bounded by a power, a logarithm at its boundary, or a constant, yielding \(O_{t,\varepsilon}(X^{\max\{1,t-1/2\}+\varepsilon})\). This is \(o(X^t)\) for fixed \(t>1\).

**5. Critical parameter and second term.** Let \(D(y)=\sum_{n\le y}\tau(n)\). Dirichlet's hyperbola method gives the classical elementary bound
\[
D(y)=y\log y+(2\gamma-1)y+O(\sqrt y).
\]
Use \(F_1=\tau*h\) and the absolute convergence in Step 1:
\[
S_1(X)=\sum_{d\le X}h(d)D(X/d)
=X\log X\sum_{d\le X}\frac{h(d)}{d}
-X\sum_{d\le X}\frac{h(d)\log d}{d}
+(2\gamma-1)X\sum_{d\le X}\frac{h(d)}{d}+
O\left(\sqrt X\sum_{d\le X}\frac{|h(d)|}{\sqrt d}\right).
\]
For any small \(\varepsilon>0\), absolute convergence at \(1/2+\varepsilon/4\) bounds the error and the tails of both \(h(d)/d\) and \(h(d)\log d/d\) by \(O_\varepsilon(X^{1/2+\varepsilon})\) after multiplication by \(X\). Substituting \(H(1)=1\), \(-\sum_d h(d)\log d/d=H'(1)\), and the value of \(H'(1)\) from Step 1 yields the asserted two-term formula.

## Verification

The included standalone program `verification/check.py` checks the prime-power decomposition and all finite divisor/Euler identities exactly with rational arithmetic for integer parameters \(t=0,1,2\) and \(1\le n\le120\), and independently checks the critical convolution \(a=\mathbf1*h\). It also generates finite summatory ratios for \(t=0,1/2,1,3/2,2\). The exact values from its last run are recorded in `verification/output.txt`. The asymptotic statements and their error bounds are established by the proof above, not by the finite numerical tests.

## Relationship to prior work

Pain, *Generalized relations between arithmetic functions* (first arXiv posting 20 January 2026), Theorem 1, already gives the finite formula \(F_t(n)=\prod_{p\mid n}(1+p^t/(p-1))\) for all real parameters (his sign convention is \(s=-t\)). Its Sections 3–4 and Appendix A discuss multiplicative identities, finite/partial Euler products and sieve context, not the present full summatory trichotomy, the critical second constant or the sharp first-order coefficient \(\zeta(t)/t\). The classical divisor summatory estimate is not claimed as new. Kaltenböck–Kiuchi–Saad Eddin–Ueda (2021) establish other GCD-weighted summatory expressions using the divisor problem; their objects \(M_r(x;f)\) and formulas do not imply this particular divisor-weight phase transition by substitution. The new observation is the common kernel whose local values at its critical pole are all one, producing a universal supercritical constant and a nontrivial critical derivative.

## Limitations

This theorem describes each fixed real parameter, not a uniform double-scaling window around \(t=1\); it does not establish an optimal remainder for fixed \(t\), and gives no explicit power-saving remainder in the subcritical regime. Literature indexing is incomplete, so the priority assessment is qualified: unindexed earlier work on related Dirichlet series might contain an equivalent assertion. The result is a derivation using classical convolution and divisor-summatory methods, not an independent proof of those classical tools.

## References

1. J.-C. Pain, *Generalized relations between arithmetic functions*, arXiv:2601.14521 (first version 20 January 2026), https://arxiv.org/abs/2601.14521, especially Theorem 1 and Appendix A.
2. L. Kaltenböck, I. Kiuchi, S. Saad Eddin, M. Ueda, *Sums of Averages of GCD-Sum Functions II*, Results in Mathematics 76 (2021), article 43, https://doi.org/10.1007/s00025-021-01357-x.
3. Classical Dirichlet hyperbola formula for the summatory divisor function; see the preceding article, equation (5), for a stated version.
