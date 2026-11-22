# A golden-ratio obstruction for variance-normalized discrete Stein factors

## Finding
Let \(p=(p_j)_{j\ge0}\) be a strictly positive log-concave probability mass function on the nonnegative integers, and let \(w>0\) be a constant birth rate. Put \(d(0)=0\) and \(d(j)=w p_{j-1}/p_j\) for \(j\ge1\), and let \(\Gamma(p,w)\) be the optimal supremum norm of the Stein solution for indicator test functions under the operator \(\mathcal Ag(j)=w g(j+1)-d(j)g(j)\). Define the best, possibly infinite, universal normalized factor by
\[
C_*:=\sup_p\frac{w\Gamma(p,w)}{\max\{1,\sqrt{\operatorname{Var}_p(X)}\}}.
\]
The supremum is over all such full-support log-concave laws with finite variance. Then
\[
C_*\ge\varphi:=\frac{1+\sqrt5}{2}=1.6180339887\ldots.
\]
More precisely, there is an explicit one-parameter family of full-support log-concave laws whose limiting normalized factors form the curve
\[
c(q)=\min\left\{\frac1{1-q},\frac1{\sqrt q}\right\},\qquad 0<q<1.
\]
Its unique maximum over \(q\in(0,1)\) is \(\varphi\), occurring at \(q_*=(3-\sqrt5)/2\). This is a **necessary lower bound** for the constant in the proposed universal log-concave uniform Stein-factor inequality, not a solution to that upper-bound conjecture.

## Assumptions and scope
Fix \(q\in(0,1)\), and integers \(N\ge1\). Let \(\varepsilon_N=2^{-N}\) and define positive unnormalized weights
\[
a_{N,j}=\begin{cases}q^{N-j},&0\le j\le N,\\ \varepsilon_N^{j-N},&j>N.\end{cases}
\]
Put \(Z_N=\sum_{j=0}^{\infty}a_{N,j}=(1-q^{N+1})/(1-q)+\varepsilon_N/(1-\varepsilon_N)\) and \(p_{N,j}=a_{N,j}/Z_N\). The successive ratios are \(1/q\) up to \(N\) and then \(\varepsilon_N\), so they are nonincreasing; thus every \(p_N\) has **full support**, is log-concave, and has all moments finite. It is a stationary law for the constant-birth operator above with nondecreasing death rates \(d(j)=wq\) for \(1\le j\le N\) and \(d(j)=w/\varepsilon_N\) for \(j>N\).

## Proof
For any positive law \(p\) and \(F(j)=\sum_{i\le j}p_i\), \(G(j+1)=\sum_{i>j}p_i\), the indicator Stein equation has the solution
\[
g_A(j+1)=\frac{\sum_{i=0}^{j}p_i(\mathbf1_A(i)-p(A))}{w p_j}.
\]
For fixed \(j\), the signed measure in the numerator has positive total mass \(F(j)G(j+1)\) on \(\{0,\ldots,j\}\) and equal negative total mass on its complement. Therefore taking the supremum over indicator sets gives the **exact identity**
\[
w\Gamma(p,w)=\sup_{j\ge0}\frac{F(j)G(j+1)}{p_j}.
\]
For the constructed \(p_N\), put \(B_N=\varepsilon_N/(1-\varepsilon_N)\). For \(0\le j\le N\), geometric sums yield
\[
\frac{F_N(j)G_N(j+1)}{p_{N,j}}=
\frac{1-q^{j+1}}{1-q}\frac{(1-q^{N-j})/(1-q)+B_N}{Z_N}.
\]
In particular \(F_N(j)/p_{N,j}=(1-q^{j+1})/(1-q)\le1/(1-q)\), so these values are at most \(1/(1-q)\). For \(j>N\), direct summation gives \(G_N(j+1)/p_{N,j}=\varepsilon_N/(1-\varepsilon_N)\), so the values are at most \(B_N\). Taking \(j=\lfloor N/2\rfloor\) in the displayed exact expression, both powers \(q^{j+1}\) and \(q^{N-j}\) vanish as \(N\to\infty\), while \(B_N\to0\) and \(Z_N\to(1-q)^{-1}\). The lower and upper estimates combine to give
\[
\lim_{N\to\infty}w\Gamma(p_N,w)=\frac1{1-q}.
\]
Let \(K_N=N-X_N\). Its weights for \(K_N\in\{0,\ldots,N\}\) are proportional to \(q^{K_N}\), and its negative tail has total probability \(B_N/Z_N=O(2^{-N})\) and uniformly vanishing second moment. By dominated convergence for the geometrically bounded positive part, \(K_N\) converges in its first two moments to a geometric variable \(K\) with \(\Pr(K=k)=(1-q)q^k\). Shifting by \(N\) does not affect variance. Consequently
\[
\lim_{N\to\infty}\operatorname{Var}(X_N)=\operatorname{Var}(K)=\frac{q}{(1-q)^2}.
\]
Combining the two limits proves \(c(q)=(1-q)^{-1}/\max\{1,\sqrt q/(1-q)\}=\min\{(1-q)^{-1},q^{-1/2}\}\). The first branch strictly increases and the second strictly decreases. They cross only when \(\sqrt q=1-q\), namely at \(q_*=(3-\sqrt5)/2\); their common value is \(\varphi\). For every universal constant \(C\) valid for all positive log-concave targets, every \(N\) obeys \(w\Gamma(p_N,w)\le C\max\{1,\sigma_N\}\), hence its limit forces \(C\ge\varphi\). This completes the proof.

## Verification
The standalone Python 3 script `checker.py` checks finite exact-rational geometric-sum identities for 49 combinations of \(q\) and \(N\), computes the complete supremum including the infinite geometric tail, verifies exact first and second moments, and tests limits for large \(N\). Run `python checker.py`. The observed output was `PASS 1479 exact identities and finite-limit checks; optimal limiting normalized factor = 1.618033988749895`. The infinite limit and optimization are established analytically above; finite checks alone do not establish them.

## Relationship to prior work
DeSalvo (2026), Theorem 2.5 and Open Problem 8.2, gives the indicator factor identity in the Bessel case and proposes a universal bound \(\Gamma\le C\max\{1,\sigma\}/w\) for arbitrary log-concave targets, with an explicit near-deterministic example showing why the maximum with one is necessary. The present statement does **not** claim the identity or the qualitative conjecture as new. Its content is the sharp \(\varphi\) lower obstruction within a geometrically truncated but full-support family with variance tending to one; the obstruction is quantitatively stronger than the earlier example's asymptotic normalized value one. The published numerical scan value \(1.14\) in DeSalvo is an observation for selected models, not a conjectured optimal constant. Other known discrete Stein-factor papers provide general envelopes or affine-birth special cases, but no equivalent \(\varphi\) constraint was identified in accessible inspected material. This last assertion is conditional on the scope of literature access, not a uniqueness certificate.

## Limitations
This proves only a lower bound on an unknown universal constant, not finiteness, an upper bound, or a universal extremizer. The family is log-concave but not strictly log-concave in the interior; strict positivity is satisfied at every site. At the threshold, the variance approaches one; this does not imply a finite-\(N\) law has variance exactly one. Priority remains uncertain, especially because the full text of a plausible 2026 preprint on Mills-ratio Stein factors was not accessible through attempted channels.

## References
1. S. DeSalvo, *Two moments suffice for Bessel approximation: conditioned differences, contingency tables, and probabilistic divide-and-conquer*, arXiv:2611.00263, version 1 submitted 2026-10-30, version 2 dated 2026-11-14. https://arxiv.org/html/2611.00263v2, Theorem 2.5, Open Problem 8.2, Remarks 9.1–9.2.
2. P. Eichelsbacher, *Stein Solution Factors via Mills Ratios: Affine Birth Rates and Symmetric Potential Distributions*, arXiv:2609.25380 (2026-09-21). https://arxiv.org/abs/2609.25380 (abstract accessible; full text could not be inspected).
3. T. C. Brown and A. Xia, *Stein's method and birth–death processes*, Annals of Probability 29 (2001), 1373–1403. Cited for background general Stein-factor theory, not asserted to exclude an equivalent lower bound.
