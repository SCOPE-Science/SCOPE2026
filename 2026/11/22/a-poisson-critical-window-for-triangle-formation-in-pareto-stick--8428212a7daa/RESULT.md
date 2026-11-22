# A Poisson critical window for triangle formation in Pareto stick samples

## Finding

Let \(X_1,\ldots,X_n\), \(n\ge3\), be independent Pareto type-I lengths with scale one and common shape \(\alpha_n>0\): \(\Pr(X_j>x)=x^{-\alpha_n}\) for \(x\ge1\). Write their order statistics as \(X_{(1)}<\cdots<X_{(n)}\), almost surely, and define the local triangle-violation count and point measure
\[
Z_n=\sum_{i=1}^{n-2} I_{n,i},\qquad I_{n,i}=\mathbf1\{X_{(i)}+X_{(i+1)}>X_{(i+2)}\},\qquad\Xi_n=\sum_{i=1}^{n-2}I_{n,i}\delta_{i/n}.
\]
Every triple of sampled sticks fails to form a nondegenerate triangle if and only if \(Z_n=0\).

**Critical-window and spatial theorem.** If \(n^3\alpha_n^2\to\lambda\in[0,\infty)\), then \(\Xi_n\) converges weakly as a finite point process on \([0,1]\) to the inhomogeneous Poisson process with intensity
\[
\nu_\lambda(\mathrm dx)=\frac{\pi^2\lambda}{12}(1-x)^2\,\mathrm dx.
\]
In particular, \(Z_n\Rightarrow\operatorname{Pois}(\pi^2\lambda/36)\), and
\[
\Pr\{\text{none of the }n\text{ sticks form any triangle}\}\longrightarrow
\exp\!\left(-\frac{\pi^2\lambda}{36}\right).
\]
If instead \(n^3\alpha_n^2\to\infty\), the last probability tends to zero. Thus \(\alpha_n\asymp n^{-3/2}\) is the sharp nontrivial triangle-free crossover.

**Finite-parameter error.** An absolute constant \(K<\infty\) exists such that, for every \(n\ge3\), \(\alpha>0\), the total-variation distance between \(\mathcal L(Z_n)\) and \(\operatorname{Pois}(\mu_{n,\alpha})\), where
\[
\mu_{n,\alpha}=\frac{\pi^2\alpha^2}{36}n(n-1)(n-2),
\]
is at most \(K(n^4\alpha^3+n^5\alpha^4)\). The same error estimate applies to the point-process law when the approximating Poisson process has grid intensity \((\pi^2/12)\alpha^2\sum_{i=1}^{n-2}(n-i)(n-i-1)\delta_{i/n}\).

## Assumptions and scope

The observations are independent and have exactly the stated Pareto law; the shape parameter may depend on sample size and is not bounded away from zero. Equality in triangle inequalities occurs with probability zero. The point measure records violations among **consecutive sorted triples**, not the total number of triangular triples. This distinction matters: both counts vanish simultaneously, but their values need not agree. The convergence of point measures is ordinary weak convergence on the compact interval \([0,1]\). The large-shape/fixed-shape regime and distributions beyond Pareto are not covered by the Poisson approximation claim when its explicit bound is uninformative.

## Proof

**1. Exact local representation.** Since \(\log X_j\sim\operatorname{Exp}(\alpha)\), exponential order-statistic spacings give independent ratios
\[
R_i=\frac{X_{(i)}}{X_{(i+1)}}\sim\operatorname{Beta}(\beta_i,1),\qquad\beta_i=(n-i)\alpha,\qquad1\le i<n.
\]
A triple is a triangle exactly when \(R_{i+1}(1+R_i)>1\). Hence \(I_{n,i}\) depends only on \((R_i,R_{i+1})\), so indicators at nonadjacent indices are independent. For any sorted sample, no triangular triple is equivalent to each consecutive triple failing its triangle inequality: if \(a<b<c\) form a triangle, then the adjacent predecessors of \(X_{(c)}\) have sum at least \(X_{(a)}+X_{(b)}>X_{(c)}\).

**2. Sharp one-point intensities.** Put \(q_i=\Pr(I_{n,i}=1)\), \(a=\beta_i\), \(b=\beta_{i+1}\). Conditioning on \(R_i=x\) gives the exact integral
\[
q_i=a\int_0^1 x^{a-1}\left[1-(1+x)^{-b}\right]\,\mathrm dx.
\]
The constant
\[
C=\int_0^1\frac{\log(1+x)}x\,\mathrm dx=\frac{\pi^2}{12}
\]
comes from the alternating dilogarithm series. For all \(a,b>0\), \(q_i\le Cab\). Moreover, using \(0\le t-(1-e^{-t})\le t^2/2\), \(0\le1-x^a\le a|\log x|\), and \(\log^2(1+x)\le(\log2)\log(1+x)\), one obtains
\[
\left|q_i-Cab\right|\le Dab\,a+\frac{C\log2}{2}ab^2,\qquad
D=\int_0^1\frac{|\log x|\log(1+x)}x\,\mathrm dx=\frac34\zeta(3).
\]
Thus \(\sum_i q_i=\mu_{n,\alpha}+O(n^4\alpha^3)\), since \(\sum_{i=1}^{n-2}(n-i)(n-i-1)=n(n-1)(n-2)/3\).

**3. Adjacent-event control and Poisson approximation.** For \(1\le i\le n-3\), the event at index \(i+1\), conditional on \(R_i,R_{i+1}\), has probability at most \(\beta_{i+2}\log2\). Therefore
\[
\Pr(I_{n,i}=I_{n,i+1}=1)
\le (\log2)\beta_{i+2}q_i
\le C(\log2)\beta_i\beta_{i+1}\beta_{i+2}.
\]
Use dependency neighborhoods \(\{i-1,i,i+1\}\). In the standard local-dependence Chen--Stein Poisson **point-process** approximation, the nonlocal-dependence term vanishes identically, while the remaining two sums satisfy
\[
b_1=\sum_i\sum_{|j-i|\le1}q_iq_j=O(n^5\alpha^4),\quad
b_2=\sum_i\sum_{0<|j-i|\le1}\Pr(I_{n,i}=I_{n,j}=1)=O(n^4\alpha^3).
\]
The process approximation theorem of Arratia, Goldstein and Gordon (1990, Theorems 2--3) bounds the total variation error by an absolute multiple of \(b_1+b_2\). Replacing the true grid intensity by \(Cab\) costs no more than \(\sum_i|q_i-C\beta_i\beta_{i+1}|=O(n^4\alpha^3)\), by a Poisson coupling. This proves the stated quantitative estimate for both the process and its total count. The bound is nonasymptotic; its right-hand side may exceed one outside the sparse regime.

**4. Critical point-process limit.** For every continuous \(f\) on \([0,1]\), if \(n^3\alpha_n^2\to\lambda<\infty\),
\[
C\alpha_n^2\sum_{i=1}^{n-2}(n-i)(n-i-1)f(i/n)
\longrightarrow C\lambda\int_0^1(1-x)^2f(x)\,\mathrm dx
\]
by Riemann sums. The two error terms \(n^4\alpha_n^3\) and \(n^5\alpha_n^4\) vanish: from bounded \(n^3\alpha_n^2\) we have \(n\alpha_n\to0\) and \(n^2\alpha_n^2\to0\). Poisson point processes with the grid intensities consequently converge to the displayed continuum Poisson point process. Evaluating its total mass gives \(C\lambda/3=\pi^2\lambda/36\), and the probability of no points is its exponential negative.

**5. Supercritical absence of triangle-free samples.** First suppose \(n\alpha_n\to0\) and \(n^3\alpha_n^2\to\infty\). Step 2 gives \(\mathbb EZ_n\sim Cn^3\alpha_n^2/3\to\infty\). Independence beyond distance one and Step 3 give
\[
\operatorname{Var}(Z_n)\le\mathbb EZ_n+O(n^4\alpha_n^3),\qquad
\frac{\operatorname{Var}(Z_n)}{(\mathbb EZ_n)^2}
=O\!\left(\frac1{n^3\alpha_n^2}+\frac1{n^2\alpha_n}\right)\to0.
\]
Chebyshev's inequality yields \(\Pr(Z_n=0)\to0\). For general \(\alpha_n\) with \(n^3\alpha_n^2\to\infty\), set \(\widetilde\alpha_n=\min(\alpha_n,n^{-4/3})\). Then \(n\widetilde\alpha_n\to0\) but \(n^3\widetilde\alpha_n^2\to\infty\). Couple the models using fixed uniforms via \(R_i(\alpha)=U_i^{1/((n-i)\alpha)}\); every \(R_i\), and therefore every violation indicator, is nondecreasing in \(\alpha\). Hence \(\Pr_{\alpha_n}(Z_n=0)\le\Pr_{\widetilde\alpha_n}(Z_n=0)\to0\). The subcritical case follows directly from \(\Pr(Z_n>0)\le\mathbb EZ_n\le Cn^3\alpha_n^2/3\).

## Verification

`CHECK.py` uses direct numerical integration of the exact Beta-ratio probability, tests the nonasymptotic upper and remainder bounds over several parameter families, checks adjacent-event bounds, verifies the triangle-free equivalence over finite nondecreasing integer samples, and runs a deterministic-seed Monte Carlo diagnostic of the critical regime. Running `python CHECK.py` with NumPy and SciPy yielded `PASS 13315 deterministic/seeded checks`. The computer diagnostics do not prove the Poisson-process theorem, which follows from the analytic local-dependence estimates and the cited standard approximation theorem.

## Relationship to prior work

Barczy and Lovas (2026, arXiv:2611.04436v1) establish exact integral formulas for the finite-sample Pareto triangle-free probability and the independent order-ratio representation. Brennan, Callow and Lin (2026, arXiv:2604.27573v2, §3.3) provide a general integral representation for unbounded stick laws; Sudbury et al. (2025, arXiv:2504.19911) treat uniform sticks. These results supply underlying identities but do not establish a Poisson critical window with a spatial intensity. The independently published *Sharp quadratic decay for triangle-free Pareto stick samples* (2026) proves a \(\Theta(n^2)\) logarithmic decay for **fixed** positive \(\alpha\), without a uniform moving-index limit. The fixed-sample \(\alpha\downarrow0\) expansion likewise does not imply a growing-sample law, as its error constant depends on sample size. Here the new statement is the complete moving-parameter threshold, the inhomogeneous point-process limit and quantitative Poisson approximation. In particular, the fixed-\(\alpha\) large-sample asymptotic cannot be inserted into this nonuniform critical regime.

## Limitations

The points in \(\Xi_n\) count adjacent sorted-triple violations only, rather than every triangular subset; only the zero events coincide. The Poisson process is asserted for the exact i.i.d. Pareto family; arbitrary regularly varying tails are not covered. The finite-n error bound may be vacuous when \(n\alpha\) is not small. The argument does not furnish a universal moderate-deviation expansion outside the critical window or an exact finite-n triangle-free probability beyond existing integrals. Priority remains conditional on the literature searched and awaits independent evaluation.

## References

1. M. Barczy and R. Lovas, *Pick-up sticks problems for exponential and Pareto distributions*, arXiv:2611.04436v1, first public November 3, 2026. https://arxiv.org/html/2611.04436v1
2. M. Brennan, N. Callow and T. C. Lin, *Fibonacci numbers and the probability of polygon formation using random length sticks*, arXiv:2604.27573v2, §3.3 (2026). https://arxiv.org/html/2604.27573v2
3. A. Sudbury, A. Sun, D. Treeby and E. Wang, *Pick-up Sticks and the Fibonacci Factorial*, arXiv:2504.19911v4 (2026; first public 2025). https://arxiv.org/html/2504.19911v4
4. *Sharp quadratic decay for triangle-free Pareto stick samples*, public mathematical record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-quadratic-decay-for-triangle-free-pareto-stick-samples--8d0ac1d44459
5. R. Arratia, L. Goldstein and L. Gordon, *Poisson approximation and the Chen--Stein method*, Statistical Science 5 (1990), 403--434. https://doi.org/10.1214/ss/1177012015
