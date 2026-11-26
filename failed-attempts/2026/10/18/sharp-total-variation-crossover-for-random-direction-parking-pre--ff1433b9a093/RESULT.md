# Sharp total-variation crossover for random-direction parking preferences

## Finding

Let \(Q_{n,p}\) be the law of the last car's *preferred location*, conditional on all \(n\) cars parking in the independent random-direction protocol defined below, and let \(U_n\) be uniform on \(\{1,\ldots,n\}\). For every real \(t\) and every sequence \(p_n\in[0,1]\) with \(\sqrt n(p_n-1/2)\to t\),

\[
\lim_{n\to\infty}n\,\|Q_{n,p_n}-U_n\|_{\mathrm{TV}}
=\frac{1+\sqrt{1+32t^2/\pi}}2.
\]

For each fixed \(p\in[0,1]\setminus\{1/2\}\),

\[
\lim_{n\to\infty}\sqrt n\,\|Q_{n,p}-U_n\|_{\mathrm{TV}}
=2\sqrt{\frac2\pi}\,|p-1/2|.
\]

In particular, \(n\|Q_{n,1/2}-U_n\|_{\mathrm{TV}}\to1\). The crossover has nontrivial curved profile and its critical directional bias is of order \(n^{-1/2}\), interpolating between the previously established but not sharply constant-evaluated orders \(n^{-1}\) and \(n^{-1/2}\).

## Assumptions and scope

Fix \(n\ge2\) parking spots in a line, labeled \(1,\ldots,n\), and \(n\) successively arriving cars with independent uniformly sampled preferred locations. A car parks immediately if its preferred location is free. If occupied, it independently chooses to search strictly to the right with probability \(p\), or strictly to the left with probability \(1-p\), using the first free spot in that direction; if none exists, it fails. Condition on all cars parking. The exact conditional probability distribution of the final car's **preferred** spot is \(Q_{n,p}\), not the location where it actually parks. The total variation convention is \(\|\mu-\nu\|_{\mathrm{TV}}=\tfrac12\sum_j|\mu(j)-\nu(j)|\). No assertions concern conditioned preference vectors under different parking rules, partial occupancy fractions, or multiple observed coordinates.

## Proof

**Exact Abel--Cayley reduction.** Define, for \(1\le j\le n\),

\[
b_{n,j}:=\frac{\binom{n-1}{j-1}j^{j-2}(n+1-j)^{n-j-1}}{(n+1)^{n-1}},\qquad
F_{n,j}:=\sum_{k<j}b_{n,k}-\sum_{k>j}b_{n,k}.
\]

At endpoints interpret \(1^{-1}=1\). Abel's binomial identity gives \(\sum_{j=1}^n b_{n,j}=2/(n+1)\); reflection gives \(b_{n,j}=b_{n,n+1-j}\). Rearranging the exact last-preference formula of Durmić, Han, Harris, Ribeiro and Yin (Theorem 3, 2022) yields the finite identity

\[
Q_{n,p}(j)-\frac1n
=\frac12b_{n,j}-\frac1{n(n+1)}-(p-\tfrac12)F_{n,j}.
\tag{1}
\]

It is also checked by direct, independently enumerated parking outcomes for all \(n\le4\), but equation (1) is an exact analytical identity, not an extrapolation from enumeration.

**Borel factorization and the two boundary atoms.** Set

\[
q_k:=e^{-k}\frac{k^{k-1}}{k!}\quad(k\ge1),\qquad
c_n:=\frac{(n-1)!e^{n+1}}{(n+1)^{n-1}}.
\]

The positive sequence \((q_k)_{k\ge1}\) is the total-progeny distribution of a critical Poisson(1) Galton--Watson process: its extinction probability is the unique solution of \(r=e^{r-1}\) in \([0,1]\), namely \(r=1\), hence \(\sum_{k\ge1}q_k=1\). Elementary cancellation in equation (1) gives the *exact* factorization

\[
b_{n,j}=c_nq_jq_{n+1-j}.
\tag{2}
\]

Stirling's formula yields \(c_n\sim\sqrt{2\pi n}\), \(q_k\sim(2\pi)^{-1/2}k^{-3/2}\). For each fixed positive \(j\), we therefore have \(nb_{n,j}\to q_j\), with an identical contribution at the reflected endpoint. More quantitatively, there exists an absolute finite \(C\) such that for \(1\le j\le(n+1)/2\),

\[
0\le b_{n,j}\le\frac{C}{n j^{3/2}},\qquad
|F_{n,j}|\le\frac{C}{n\sqrt j},
\tag{3}
\]

and symmetric bounds hold at the other endpoint. The first inequality follows from (2), the uniform bounds \(c_n\le C\sqrt n\) and \(q_k\le Ck^{-3/2}\), and \(n+1-j\ge(n+1)/2\); the second follows from reflection, the exact identity \(F_{n,j}=-\sum_{k=j+1}^{n+1-j}b_{n,k}\) for the left half, and the bound obtained by summing the reflected halves; the telescoping relation is \(F_{n,j+1}-F_{n,j}=b_{n,j}+b_{n,j+1}\). These bounds provide a summable majorant for the endpoint mass and an integrable majorant for the bias term.

For any fixed \(0<\varepsilon<1/2\), dominated convergence in the endpoint series and (3) show

\[
\lim_{n\to\infty}\sum_{j\le\varepsilon n}n b_{n,j}=1,
\qquad
\lim_{n\to\infty}\sum_{j\ge(1-\varepsilon)n}n b_{n,j}=1.
\tag{4}
\]

Thus the positive term \(nb_{n,j}/2\) in \(n\) times (1) has a half-unit boundary mass at each end; its interior contribution vanishes. In particular, the total limiting positive boundary mass is one.

**Interior profile.** Uniformly over every closed subinterval of \((0,1)\), equation (2) and Stirling give

\[
n^{5/2}b_{n,\lfloor nx\rfloor}\longrightarrow
h(x):=\frac1{\sqrt{2\pi}[x(1-x)]^{3/2}}.
\tag{5}
\]

By symmetry, \(F_{n,j}\) is zero or of order \(n^{-5/2}\) at the central index. Its exact finite difference is \(F_{n,j+1}-F_{n,j}=b_{n,j}+b_{n,j+1}\). The corresponding Riemann sums, anchored at the center, imply compact-uniform convergence

\[
n^{3/2}F_{n,\lfloor nx\rfloor}\longrightarrow
f(x):=\frac4{\sqrt{2\pi}}\frac{2x-1}{\sqrt{x(1-x)}}.
\tag{6}
\]

The derivative \(f'(x)=2h(x)\) fixes both the coefficient and sign. Bound (3) also gives an integrable tail envelope: the contribution to \(n^{1/2}\sum_j|F_{n,j}|\) from indices within \(\varepsilon n\) of either endpoint is \(O(\sqrt\varepsilon)\), uniformly in \(n\).

**Critical window.** Let \(\delta_n=p_n-1/2\), with \(\sqrt n\delta_n\to t\). Combining equations (1), (5), and (6), for \(j=\lfloor nx\rfloor\) with \(x\) in a compact subset of \((0,1)\), gives

\[
n^2\left(Q_{n,p_n}(j)-\frac1n\right)
\longrightarrow-1-tf(x).
\tag{7}
\]

Partition the TV sum into two strips of width \(\varepsilon n\) and the intervening compact interval. In the strips the baseline terms total \(O(\varepsilon)\) after multiplying TV by \(n\), while the total bias contribution is \(O((1+|t|)\sqrt\varepsilon)\) by (3). Equation (4) supplies one unit of limiting boundary absolute mass, and the compact interval uses (7). First let \(n\to\infty\), then \(\varepsilon\downarrow0\). It follows that

\[
\lim_{n\to\infty}n\,\|Q_{n,p_n}-U_n\|_{\mathrm{TV}}
=\frac12\left(1+\int_0^1|1+t f(x)|\,dx\right).
\tag{8}
\]

In the substitution \(z=2x-1\), one has \(f(x)=(8/\sqrt{2\pi})z/\sqrt{1-z^2}\) and \(dx=dz/2\). Directly splitting at the unique zero of the integrand gives

\[
\int_0^1|1+t f(x)|\,dx=\sqrt{1+\frac{32t^2}{\pi}}.
\tag{9}
\]

This proves the window theorem, including \(t=0\) and any convergent real sequence of rescaled biases.

**Fixed directional bias.** For fixed \(p\ne1/2\), the centered law's baseline and \(b\)-terms in (1) have total absolute mass \(O(n^{-1})\); their contribution vanishes under \(\sqrt n\) scaling. Equations (3) and (6) give convergence of the bias-term norm:

\[
\lim_{n\to\infty}\sqrt n\sum_{j=1}^n|F_{n,j}|
=\int_0^1|f(x)|\,dx=\frac8{\sqrt{2\pi}}.
\]

The triangle inequality and the definition of total variation prove the second displayed theorem, including \(p=0\) and \(p=1\).

## Verification

The standalone `verify.py` uses exact rational Abel--Cayley weights, direct independent enumeration of all preference vectors and successful directional-coin outcomes for \(n=2,3,4\), probability normalization, reflection and symmetry identities, and numerical asymptotic probes at larger \(n\). Its execution reports 704 passed assertions. The exhaustive finite checks corroborate (1); the all-size limits depend on Stirling, dominance, compact-uniform Riemann convergence and explicit integration, not finite enumeration.

## Relationship to prior work

Diaconis and Hicks (2016) introduced probabilistic methods for uniform classical parking functions. Bellin (2021) established multivariate uniformity and bounds for classical parking functions. Tian and Treviño (2021/2022) considered the random-direction parking protocol. Durmić, Han, Harris, Ribeiro and Yin (arXiv:2211.00536, 2022) gave the exact conditional last-preference law (their Theorem 3) and the two rates \(\Theta(n^{-1})\) and \(\Theta(n^{-1/2})\) (their Theorems 5 and 6). Harris, Ribeiro and Yin (2025) generalized the model to fewer cars than spaces. Those formulas and rate results are treated as prior results, not rediscovered contributions. The asserted addition is the critical-window limit profile together with the sharp constants for its endpoints and fixed-bias regime. The inspected source discussions do not state this simultaneous result.

## Limitations

This theorem is specific to the single last *preferred* location, conditioned on successful parking of all spots, in the random-direction protocol. It does not provide rates of convergence to the limiting crossover, a limit for multiple conditional preferences, or the regime of fewer cars than spaces. The new theorem has been reviewed against identified primary sources, but there is no independent mathematical audit or exhaustive guarantee of historical priority; hidden equivalent consequences of earlier generating-function identities remain a residual originality risk.

## References

- P. Diaconis and A. Hicks, *Probabilizing Parking Functions*, first public preprint 29 November 2016, https://arxiv.org/abs/1611.09821 .
- E. Bellin, *Asymptotic behaviour of the first positions of uniform parking functions*, first public preprint 19 August 2021, https://arxiv.org/abs/2108.08661 .
- I. Durmić, A. Han, P. E. Harris, R. Ribeiro and M. Yin, *Probabilistic Parking Functions*, first public preprint 1 November 2022, https://arxiv.org/abs/2211.00536 .
- P. E. Harris, R. Ribeiro and M. Yin, *Probabilistic (m,n)-Parking Functions*, first public preprint 1 February 2025, https://arxiv.org/abs/2502.00269 .
- C. Tian and E. Treviño, *Generalizing Parking Functions with Randomness*, manuscript dated 2021, subsequently cited as 2022; related protocol, not used for date anchoring.
