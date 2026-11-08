# A sharp power-cutoff hub transition in uniform recursive trees

## Finding

Fix \(0<\gamma<1\). At time \(m+1\), attach the new vertex independently and uniformly to the existing labels
\[
\{\lfloor m^\gamma\rfloor,\lfloor m^\gamma\rfloor+1,\ldots,m\}.
\]
Let \(D_v(n)\) be the number of children of vertex \(v\) in the resulting tree on \(\{1,\ldots,n\}\), let \(\Delta_n=\max_v D_v(n)\), and choose the smallest maximizing label \(V_n\).

Set
\[
\gamma_* =1-\frac{1}{2\log2},\qquad t_0=\frac1{\log2}.
\]
For \(0<\gamma\le\gamma_*\), put \(t_\gamma=t_0\). For \(\gamma_*<\gamma<1\), let \(t_\gamma\) be the unique solution with \(t>2(1-\gamma)\) of
\[
t\log\frac{t}{1-\gamma}-t+1-2\gamma=0.
\]
Then
\[
\frac{\Delta_n}{\log n}\xrightarrow[n\to\infty]{\mathrm{a.s.}}t_\gamma,
\qquad
\frac{\log V_n}{\log n}\xrightarrow[n\to\infty]{\mathbb P}\max\{\gamma,\gamma_*\}.
\]
The same maximum-degree coefficient holds when degrees are undirected, since each degree differs from its child count by at most one. In particular \(t_{1/2}=e/2\), while \(\gamma_*=0.278652479555\ldots\). The two limiting quantities are the same as in the unrestricted uniform recursive tree up to \(\gamma_*\); beyond this threshold, the maximum-degree coefficient decreases and the hub-label exponent equals the power cutoff.

## Assumptions and scope

All parent choices at distinct arrival times are independent. The restriction applies to the exact floor cutoff, not to a random window or degree-weighted attachment. The parameter \(\gamma\) is fixed in \((0,1)\) while \(n\to\infty\). Convergence of normalized maximum degree is almost sure on the natural common infinite probability space; convergence of the maximizing label exponent is in probability. The vertex label is the arrival index. Neither second-order fluctuations nor a limiting distribution of the argmax is asserted.

## Proof

**1. Uniform degree-mean profile.** For each \(m\ge v\), set
\[
p_{m,v}=\frac{\mathbf1\{\lfloor m^\gamma\rfloor\le v\}}{m-\lfloor m^\gamma\rfloor+1},\qquad
D_v(n)=\sum_{m=v}^{n-1}\mathbf1\{\text{parent}(m+1)=v\}.
\]
For every \(m\), the denominator reciprocal differs from \(1/m\) by \(O_\gamma(m^{\gamma-2})\); its error series is absolutely summable. Also \(\lfloor m^\gamma\rfloor\le v\) is equivalent to \(m^\gamma<v+1\). The harmonic-sum comparison therefore gives, uniformly for all \(1\le v\le n\),
\[
\mathbb ED_v(n)=\bigg[\log\!\left(\frac{\min\{n,v^{1/\gamma}\}}{v}\right)\bigg]_++O_\gamma(1).
\]
Writing \(a=\log v/\log n\), define
\[
c_\gamma(a)=\min\{1,a/\gamma\}-a\qquad(0\le a\le1).
\]
Thus \(\mathbb ED_v(n)=c_\gamma(a)\log n+O_\gamma(1)\), including the label boundaries. For fixed \(0<a<1\) and \(v\in[n^a,2n^a]\), the mean equals \(c_\gamma(a)\log n+O_\gamma(1)\) and the maximal single-arrival success probability is \(O(n^{-a})\).

**2. A uniform upper bound and a local sharp lower bound.** Define, for \(t>c>0\),
\[
I(t;c)=t\log(t/c)-t+c,
\quad I(t;0)=+\infty.
\]
Every child count is a sum of independent Bernoulli variables. The exponential Markov bound, using \(\log(1+p(e^s-1))\le p(e^s-1)\), shows for \(k\ge\mu_v\) that
\[
\Pr\{D_v(n)\ge k\}\le\exp\{-k\log(k/\mu_v)+k-\mu_v\}.
\]
Consequently, on compact positive label-exponent intervals with \(t>c_\gamma(a)\), the upper logarithmic tail exponent is \(-I(t;c_\gamma(a))\).

For the corresponding lower bound choose \(v\in[n^a,2n^a]\), with \(0<a<1\), \(c=c_\gamma(a)>0\), and \(k=\lceil t\log n\rceil\), where \(t>c\). Put \(p_i=p_{m,v}\), \(\mu=\sum p_i\), and let \(e_k(p)\) be the degree-\(k\) elementary symmetric polynomial. Since \(\sum p_i^2=o(1)\),
\[
\Pr\{D_v(n)=k\}=\prod_i(1-p_i)e_k\left(\frac{p_i}{1-p_i}\right)
\ge e^{-\mu+o(1)}e_k(p).
\]
Expand \(\mu^k\) into ordered \(k\)-tuples of indices. By the union bound, the chance of any repeated index when drawing each index proportionally to \(p_i\) is at most \(\binom{k}{2}(\max p_i)/\mu=o(1)\). Hence \(e_k(p)\ge(1-o(1))\mu^k/k!\). Stirling's formula and the mean profile prove the sharp, uniform-in-that-interval estimate
\[
\Pr\{D_v(n)\ge\lceil t\log n\rceil\}
=n^{-I(t;c_\gamma(a))+o(1)}.
\]
This estimate is used only when \(t>c_\gamma(a)>0\).

**3. The variational threshold.** Since labels in a fixed exponent strip near \(a\) number \(n^{a+o(1)}\), the relevant exponent is
\[
F_{\gamma,t}(a)=a-I(t;c_\gamma(a)),\qquad
M_\gamma(t)=\sup_{0<a<1}F_{\gamma,t}(a).
\]
Take \(t>1-\gamma=\max_a c_\gamma(a)\). On \(0<a\le\gamma\), direct differentiation gives
\[
F'_{\gamma,t}(a)=1-\frac{1-\gamma}{\gamma}+\frac ta>0.
\]
On \(\gamma\le a<1\), it gives \(F'_{\gamma,t}(a)=2-t/(1-a)\). Therefore the unique maximizer of \(F\) is \(a=1-t/2\) when \(t\le2(1-\gamma)\), and \(a=\gamma\) otherwise. Substituting yields the exact optimization
\[
M_\gamma(t)=
\begin{cases}
1-t\log2,&1-\gamma<t\le2(1-\gamma),\\
2\gamma-1+t-t\log\dfrac{t}{1-\gamma},&t\ge2(1-\gamma).
\end{cases}
\]
These expressions agree at the junction, and \(M_\gamma\) decreases strictly from a positive value to a negative value, so there is one zero. The zero is \(t_0\) when \(\gamma\le 1-1/(2\log2)\), and otherwise is the solution specified in the finding. At this zero the unique maximizing label exponent is \(a_\gamma=\max\{\gamma,\gamma_*\}\).

**4. Upper and lower bounds for the maximum.** For each \(t>t_\gamma\), \(M_\gamma(t)<0\). Divide the label range into finitely many small strips according to \(\log v/\log n\), bounding all means within each strip by the maximum of \(c_\gamma\) there plus \(O(1/\log n)\). A union bound over \(n^{a+o(1)}\) labels and the Chernoff estimate gives, for some \(\eta>0\),
\[
\Pr\{\Delta_n\ge t\log n\}\le n^{-\eta}
\]
for all sufficiently large \(n\). The strips near endpoints where \(c_\gamma\) vanishes are treated by their arbitrarily small upper mean, which only strengthens the bound.

For \(1-\gamma<t<t_\gamma\), there exists \(0<a<1\) such that \(F_{\gamma,t}(a)>0\). In \([n^a,2n^a]\) let \(Z\) count labels with \(D_v(n)\ge\lceil t\log n\rceil\). The sharp lower tail in step 2 implies \(\mathbb EZ\ge n^\eta\) for some \(\eta>0\). For two distinct labels \(u,v\), their child counts are coordinatewise sums of independent one-hot categorical trials. They are negatively quadrant dependent: for one trial the conditional covariance of increasing functions is \(-p_up_v\,\Delta f\,\Delta g\le0\); after adding the trial, the conditional mean functions remain increasing, so induction and the total-covariance identity preserve this inequality. Thus the high-degree indicators for distinct labels have nonpositive covariance, \(\operatorname{Var}(Z)\le\mathbb EZ\), and
\[
\Pr\{\Delta_n<t\log n\}\le\Pr\{Z=0\}\le n^{-\eta}.
\]
Arbitrarily choosing \(t<t_\gamma\) but above \(1-\gamma\), and \(t'>t_\gamma\), yields convergence in probability of \(\Delta_n/\log n\). On the dyadic subsequence \(n=2^j\), both errors are summable; Borel--Cantelli, monotonicity of \(\Delta_n\), and \(\log(2^{j+1})/\log(2^j)\to1\) upgrade this to almost-sure convergence for all \(n\).

**5. Location of the maximizing hub.** The maximizer \(a_\gamma\) of \(F_{\gamma,t_\gamma}\) is unique. For any fixed \(\varepsilon>0\), compactness gives \(F_{\gamma,t_\gamma}(a)\le-\eta\) uniformly outside \((a_\gamma-\varepsilon,a_\gamma+\varepsilon)\). Choose \(t<t_\gamma\), sufficiently close to \(t_\gamma\) and still above \(1-\gamma\), so the same strict negative margin persists for \(F_{\gamma,t}\) outside that interval. Repeating the upper-tail union bound over the excluded strips shows that the chance any excluded label reaches \(t\log n\) tends to zero. Meanwhile step 4 shows \(\Delta_n\ge t\log n\) with probability tending to one. Every maximizing label therefore satisfies \(n^{a_\gamma-\varepsilon}<V_n<n^{a_\gamma+\varepsilon}\) with probability tending to one. This is precisely the claimed convergence in probability.

## Verification

Run `python3 verify.py` from the directory containing the accompanying standalone script. It enumerates all independent parent-choice vectors for sizes \(2\le n\le8\) at three cutoff powers; checks degree expectations, negative-quadrant inequalities for every pair of vertices and all relevant integer thresholds using exact rational arithmetic; and checks the piecewise variational equations at nine cutoff powers. It reports `CHECKS_PASSED 19519` and the values \(t_{1/2}=e/2\), \(\gamma_*=0.278652479555518\ldots\). These are finite diagnostics, not a substitute for the analytic proof of asymptotics.

## Relationship to prior work

Angel, Bhamidi, Donderwinkel, Maitra and Sakanaveeti introduce the cutoff recursive-tree family and study macroscopic \(j(m)=\lfloor\theta m\rfloor\) and mesoscopic \(j(m)=m-\lfloor m^\beta\rfloor\) cases; Remark 1.1 explicitly mentions \(j(m)=\lfloor m^\beta\rfloor\) as an unexplored power-cutoff regime. Their results on local limits, height and components do not state the maximum-degree coefficient or exponent of the maximizing label for this regime. Lodewijks and Ortgiese investigate maximum degree in trees with fixed, positive vertex weights, rather than a label's deterministic disappearance from eligibility as time advances. Classical uniform-recursive-tree maximum-degree results provide the baseline \(1/\log2\), but not the restricted-age phase boundary. The present theorem treats one natural new regime, and does not assert absolute bibliographic uniqueness.

## Limitations

The parameter is fixed \(0<\gamma<1\); no uniform limit in \(\gamma\), second-order maximum fluctuations, almost-sure convergence of the hub exponent, or dynamics of the winning label are established. Numerical and finite exact tests do not prove infinite limits. Historical priority outside the inspected literature remains uncertain. The theorem assumes independent uniform selections at different arrival times; changing this selection rule may change the result.

## References

1. O. Angel, S. Bhamidi, S. Donderwinkel, N. Maitra and A. Sakanaveeti, *Evolution of recursive trees with limited memory*, arXiv:2510.18856v1 (first posted 2025-10-21), especially Remark 1.1 and Sections 1--2, https://arxiv.org/abs/2510.18856.
2. B. Lodewijks and M. Ortgiese, *The maximal degree in random recursive graphs with random weights*, arXiv:2007.05438 (first posted 2020-07-10), Sections 1--2, https://arxiv.org/abs/2007.05438.
3. L. Devroye and J. Lu, *The strong convergence of maximal degrees in uniform random recursive trees and dags*, Random Structures & Algorithms (1995), classical unweighted benchmark.
4. W. Goh and E. Schmutz, *Limit distribution for the maximum degree of a random recursive tree*, Journal of Computational and Applied Mathematics 142 (2002), 61--82, https://doi.org/10.1016/S0377-0427(01)00460-5.
