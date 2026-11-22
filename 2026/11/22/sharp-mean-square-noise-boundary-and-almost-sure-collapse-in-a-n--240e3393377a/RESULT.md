# Sharp mean-square noise boundary and almost-sure collapse in a nonexpansive reflection iteration

## Finding

Consider stochastic Krasnoselskii–Mann iteration
\[
x_{k+1}=x_k+\beta_k\bigl(F(x_k)-x_k+M_{k+1}\bigr),\qquad F(u,v)=(u,-v),
\]
with \(x_0=(1,0)\) and conditionally unbiased noise
\[
M_{k+1}=\frac{\sigma u_k}{\sqrt2}(\xi_{k+1},\zeta_{k+1}),
\]
where all \(\xi_j,\zeta_j\) are independent symmetric signs. This is the reflection example of Tamizholi, Chandak and Singh [1]. Its conditional noise variance is exactly \(\sigma^2 u_k^2\), so it obeys their iterate-dependent noise condition.

Set \(c=\sigma^2/2\), \(U_k=\mathbb E[u_k^2]\), \(V_k=\mathbb E[v_k^2]\), and \(r_k=4V_k\). For the polynomial step sizes in the scope below, the complete asymptotic law is
\[
\boxed{\frac{V_k}{U_k}\sim\frac{c\beta_k}4,\qquad r_k\sim c\beta_k\prod_{j=0}^{k-1}(1+c\beta_j^2).}
\]
In the critical step-size case \(b=1/2\), put \(p=cB^2=\sigma^2B^2/2\). Then
\[
\boxed{r_k\sim\frac{cB\Gamma(K)}{\Gamma(K+p)}k^{p-1/2}.}
\]
The **exact mean-square threshold** is \(\sigma B=1\): mean-square residuals tend to zero below it, to the explicit strictly positive constant \(cB\Gamma(K)/\Gamma(K+1/2)\) at equality, and diverge above it. For \(0<b<1/2\), mean-square residuals diverge for every \(\sigma>0\), with
\[
\lim_{k\to\infty}\frac{\log r_k}{k^{1-2b}}=\frac{cB^2}{1-2b}.
\]

Yet **for all these parameters the iterates converge almost surely to the origin**, including in the mean-square-divergent regimes. At nonresonant noise parameters (no finite \(j\) with \(\sigma\beta_j/\sqrt2=1\)), they have the sharp almost-sure logarithmic rate
\[
\boxed{\lim_{k\to\infty}\frac{\log\|x_k\|_2}{c\sum_{j<k}\beta_j^2}=-\frac12\quad\hbox{almost surely}.}
\]
Thus the same algorithm may converge at an explicit pathwise rate while its expected squared fixed-point residual tends to infinity.

## Assumptions and scope

Quantifiers: choose any \(0<b\le1/2\), real \(B>0\), \(K\ge1\) and \(\sigma>0\) such that \(\beta_0=BK^{-b}\le1/2\), and use \(\beta_k=B(k+K)^{-b}\) for every integer \(k\ge0\). Choose the two symmetric signs independently at each update, and make sign pairs independent across updates. The operator and the update are exactly those displayed above. Expectations refer to these signs, with exact real arithmetic. The almost-sure convergence statement includes resonant \(\sigma\beta_j/\sqrt2=1\); only the sharp logarithmic path rate excludes them. No assertion is made about arbitrary nonexpansive maps or other noise laws.

## Proof

**1. Exact moment recurrences.** Write \(a_k=\sigma\beta_k/\sqrt2\). The coordinate updates are
\[
u_{k+1}=(1+a_k\xi_{k+1})u_k,\qquad
v_{k+1}=(1-2\beta_k)v_k+a_k\zeta_{k+1}u_k.
\]
Independence and centering give, with \(U_0=1\) and \(V_0=0\),
\[
U_{k+1}=(1+c\beta_k^2)U_k,\qquad
V_{k+1}=(1-2\beta_k)^2V_k+c\beta_k^2U_k.
\]
In particular \(U_k=\prod_{j<k}(1+c\beta_j^2)>0\) even at a resonance. The ratio \(q_k=V_k/U_k\) satisfies
\[
q_{k+1}=\frac{(1-2\beta_k)^2q_k+c\beta_k^2}{1+c\beta_k^2}.
\]

**2. Sharp transverse variance transfer.** For \(y_k=q_k/\beta_k\), the preceding identity reads \(y_{k+1}=A_k y_k+D_k\), where
\[
A_k=\frac{\beta_k}{\beta_{k+1}}\frac{(1-2\beta_k)^2}{1+c\beta_k^2},\qquad
D_k=\frac{c\beta_k^2}{\beta_{k+1}(1+c\beta_k^2)}.
\]
Since \(b<1\), \(\beta_k/\beta_{k+1}=1+O(k^{-1})=1+o(\beta_k)\). Therefore \(A_k=1-4\beta_k+o(\beta_k)\) and \(D_k=c\beta_k+o(\beta_k)\). For large \(k\), \(0\le A_k\le1-2\beta_k\), \(0\le D_k\le2c\beta_k\), so \(y_k\) is bounded. Subtracting \(c/4\) yields \(y_{k+1}-c/4=A_k(y_k-c/4)+o(\beta_k)\). For every fixed \(\varepsilon>0\), after a sufficiently large index the error satisfies \(\lvert y_{k+1}-c/4\rvert\le(1-2\beta_k)\lvert y_k-c/4\rvert+\varepsilon\beta_k\). Iterating, and using \(\sum_k\beta_k=\infty\), proves \(y_k\to c/4\), establishing \(V_k/U_k\sim c\beta_k/4\) and \(r_k\sim c\beta_k U_k\).

**3. Exact threshold and constants.** For \(0<b<1/2\), \(\log U_k=\sum_{j<k}\log(1+cB^2(j+K)^{-2b})\sim cB^2 k^{1-2b}/(1-2b)\). This follows from \(\log(1+z)=z+O(z^2)\) and summation, since the sum of squared \(z\)-terms is lower order. Since \(\log\beta_k=O(\log k)\), this proves the logarithmic mean-square law. For \(b=1/2\), the gamma-product identity gives exactly
\[
U_k=\prod_{j=0}^{k-1}\left(1+\frac{p}{j+K}\right)
=\frac{\Gamma(K)\Gamma(k+K+p)}{\Gamma(K+p)\Gamma(k+K)}
\sim\frac{\Gamma(K)}{\Gamma(K+p)}k^p.
\]
Substituting into Step 2 proves the asymptotic residual constant and its sharp three-way phase classification.

**4. Almost-sure norm decay.** Assume first that no \(a_j=1\), and let \(S_k=\sum_{j<k}a_j^2\to\infty\). The product for \(u_k\) is nonzero. For all sufficiently large \(j\), \(a_j<1/2\). For \(Y_j=\log|1+a_j\xi_{j+1}|\),
\[
\mathbb E Y_j=\tfrac12\log(1-a_j^2)=-a_j^2/2+O(a_j^4),\qquad
\operatorname{Var}(Y_j)=a_j^2+O(a_j^4).
\]
Because \(\sum a_j^2/S_{j+1}^2<\infty\), the centered martingale series with denominators \(S_{j+1}\) converges almost surely; Kronecker's lemma gives \(\sum_{j<k}(Y_j-\mathbb EY_j)=o(S_k)\). Also \(\sum_{j<k}a_j^4=o(S_k)\), hence \(\log|u_k|/S_k\to-1/2\) almost surely.

For \(\delta>0\), on this probability-one event, eventually \(|u_k|\le C\exp[-(1/2-\delta)S_k]\). Set \(h=1/2-2\delta>0\). Since \(a_k=O(\beta_k)\), \(a_k^2=o(\beta_k)\) and \(S_k\to\infty\), a sufficiently large random constant \(C'\) makes \(C'e^{-hS_k}\) a supersolution of
\[
|v_{k+1}|\le(1-2\beta_k)|v_k|+a_k|u_k|.
\]
Indeed, after a large index \((1-2\beta_k)+(C/C')a_ke^{-\delta S_k}\le1-\beta_k\le e^{-h a_k^2}\). Therefore \(\limsup\log|v_k|/S_k\le-h\); letting \(\delta\downarrow0\) and using \(\|x_k\|\ge|u_k|\) gives \(\log\|x_k\|/S_k\to-1/2\). At an exceptional finite resonance \(a_j=1\), either the product remains nonzero and this same argument works after that index, or it becomes exactly zero; then the \(u\)-coordinate stays zero and \(v\) contracts deterministically since \(\prod_{\ell\ge j}(1-2\beta_\ell)=0\) in the infinite-limit sense. Thus \(x_k\to0\) almost surely in every case.

## Verification

The accompanying `verify.py` executes exact-fraction finite-state enumeration of the four independent sign choices over four updates and compares both second moments against the exact recurrences. It also checks the stated gamma-product constant and variance-transfer ratio numerically for several decaying schedules. Run `python3 verify.py` using only Python's standard library. Finite checks support the formulas but cannot prove the infinite asymptotics or almost-sure statements; those follow from Steps 2–4.

## Relationship to prior work

Tamizholi, Chandak and Singh [1, Section 4.3 and Appendix B.3] introduce precisely this two-dimensional reflection construction and show mean-square residual divergence for \(b<1/2\) and, at \(b=1/2\), under the sufficient condition \(p>1\). Their proof retains only the latest forcing term. The new statement instead estimates the full accumulated transverse variance, proving the exact boundary \(p=1/2\), an explicit nonzero critical limit and simultaneous almost-sure convergence with sharp decay rate. It does not claim novelty for the stochastic reflection construction or the basic moment recurrence. The general stochastic fixed-point analyses of Bravo–Cominetti [2] and Cortild–Cartis [3] concern broader almost-sure convergence under hypotheses such as moment summability or samplewise nonexpansive oracle maps, rather than the exact phase diagram of [1]'s iterate-dependent-noise example.

## Limitations

This is an exact-arithmetic theorem for one explicit two-dimensional family of nonexpansive stochastic approximation problems. Mean-square divergence is not pathwise divergence. The logarithmic almost-sure rate needs the stated nonresonance, though almost-sure convergence does not. The theorem does not imply a universal square-summability threshold for arbitrary operators, noise structures or finite-precision simulations. Independent mathematical validation is not claimed.

## References

1. R. Tamizholi, S. Chandak and R. Singh, *Optimal Last-Iterate Bounds for Nonexpansive Stochastic Approximation*, arXiv:2611.13846v1 (first posted 2026-11-10), Sections 4.3 and B.3. https://arxiv.org/html/2611.13846v1
2. M. Bravo and R. Cominetti, *Stochastic fixed-point iterations for nonexpansive maps: Convergence and error bounds*, arXiv:2208.04193, later SIAM Journal on Control and Optimization 62 (2024), 191–219. https://arxiv.org/abs/2208.04193
3. D. Cortild and C. Cartis, *Stochastic Krasnoselskii–Mann Iterations: Convergence without Uniformly Bounded Variance*, arXiv:2604.22581 (first posted 2026-04-24). https://arxiv.org/abs/2604.22581
