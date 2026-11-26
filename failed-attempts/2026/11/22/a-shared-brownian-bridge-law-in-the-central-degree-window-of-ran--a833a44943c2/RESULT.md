# A shared Brownian-bridge law in the central degree window of random permutation graphs

## Finding

Let \(\pi_n\) be uniform on the permutations of \(\{1,\ldots,n\}\), and form its inversion graph: distinct \(i,j\) are adjacent when \((i-j)(\pi_n(i)-\pi_n(j))<0\). Write \(d_n(i)\) for vertex degree. Fix \(r\ge2\) and distinct real numbers \(t_1,\ldots,t_r\). For all sufficiently large \(n\) define distinct indices
\[
i_{n,a}=\left\lfloor\frac n2+t_a\sqrt n\right\rfloor\quad(1\le a\le r).
\]
Let \(B\) be one *standard Brownian bridge* on \([0,1]\), with covariance \(\mathbb E[B(u)B(v)]=\min(u,v)-uv\), and let \(U_1,\ldots,U_r\) be independent \(\operatorname{Unif}[0,1]\) variables, independent of \(B\). Then
\[
\boxed{\left(\frac{d_n(i_{n,a})-(n-1)/2}{\sqrt n}\right)_{a=1}^r
\ \xrightarrow{\mathrm d}\
\left(t_a(1-2U_a)+B(U_a)\right)_{a=1}^r.}
\tag{1}
\]
In particular, the limiting coordinates are **not independent**: for \(a\ne b\),
\[
\boxed{\operatorname{Cov}(Z_a,Z_b)=\frac1{12},\qquad
\operatorname{Var}(Z_a)=\frac16+\frac{t_a^2}{3}.}
\tag{2}
\]
The dependence is caused by one shared Brownian bridge, evaluated at independently selected uniform arguments. The one-point zero-offset law is the previously established normal-scale mixture \(B(U)\); the joint window law and shared-bridge representation are the claim here.

## Assumptions and scope

The permutation is exactly uniform; no limit is asserted for nonuniform permutation measures. The number \(r\) of designated vertices is fixed as \(n\to\infty\), and the offsets are fixed and pairwise distinct. Convergence is finite-dimensional weak convergence in \(\mathbb R^r\). Distinct offsets ensure distinct integer indices for all large \(n\); no claim is made about a growing number of marked vertices or tightness of a degree process indexed by every window position.

## Proof

**1. A score representation and exact degree identity.** Let \(X_1,\ldots,X_n\) be iid \(\operatorname{Unif}[0,1]\); their ranks generate a uniform permutation and preserve all inversion comparisons. Put \(m=\lfloor n/2\rfloor\), and for \(0\le u\le1\), define
\[
A_n(u)=\sum_{j\le m}{\bf1}\{X_j<u\},\qquad
R_n(u)=\sum_{j>m}{\bf1}\{X_j<u\}.
\]
For \(u=X_i\) and \(P_{i-1}(u)=\sum_{j<i}{\bf1}\{X_j<u\}\), direct counting of inversions gives the *pathwise* identity
\[
d_n(i)=(i-1)+A_n(u)+R_n(u)-2P_{i-1}(u).\tag{3}
\]
The strict sign matters only at the marked point itself; ties occur with probability zero.

**2. The common empirical bridge.** Define
\[
H_n(u)=\frac{R_n(u)-(n-m)u-A_n(u)+mu}{\sqrt n}.
\tag{4}
\]
The two blocks comprise independent iid samples. The classical empirical-process central limit theorem, applied to the two blocks, gives
\[
H_n\ \xrightarrow{\mathrm d}\ B\quad\text{in }D[0,1]
\]
with a continuous limit, because the two independent standard bridges are combined with coefficients tending to \(1/\sqrt2\) and \(-1/\sqrt2\). Indeed the limit covariance is \(\min(u,v)-uv\). This step can alternatively be checked via the multinomial central limit theorem and fourth-moment tightness for interval counts.

For each fixed \(r\), the marks \(X_{i_{n,1}},\ldots,X_{i_{n,r}}\) are independent uniforms. Delete the at most \(r\) marked observations from both empirical sums and replace their deterministic centering terms by their respective expectations. The resulting process differs from \(H_n\) in sup norm by at most \(2r/\sqrt n\), and is independent of all the deleted marks. Thus the joint limit consists of \(B\) independent of \((U_1,\ldots,U_r)\), and the continuous evaluation map yields
\[
\bigl(H_n(X_{i_{n,a}})\bigr)_{a=1}^r
\ \xrightarrow{\mathrm d}\
\bigl(B(U_a)\bigr)_{a=1}^r.\tag{5}
\]

**3. Controlling the short positional block.** Uniformly for each of the finitely many marked positions \(i=i_{n,a}\),
\[
P_{i-1}(X_i)=A_n(X_i)+(i-1-m)X_i+o_{\mathbb P}(\sqrt n).\tag{6}
\]
To see this, the difference on the left consists of a signed sum of at most \(|i-m|+1=O(\sqrt n)\) independent Bernoulli indicators with success probability \(X_i\), except for the marked observation itself (whose contribution is deterministic zero). Conditional on \(X_i\), its centered variance is at most \(|i-m|+1\), and its conditional mean deviates from \((i-1-m)X_i\) by at most one. Chebyshev's inequality therefore gives an \(O_{\mathbb P}(n^{1/4})\) error, which is \(o_{\mathbb P}(\sqrt n)\). A finite union bound covers all marks.

Insert (6) into (3). With \(u=X_i\),
\[
\frac{d_n(i)-(n-1)/2}{\sqrt n}
=\frac{i-(n+1)/2}{\sqrt n}
+\frac{n-2i+2}{\sqrt n}u+H_n(u)+o_{\mathbb P}(1).\tag{7}
\]
For \(i=i_{n,a}\), the first two coefficients converge respectively to \(t_a\) and \(-2t_a\). Joint convergence (5) and Slutsky's theorem prove (1).

**4. Covariance and compatibility with exact finite moments.** For independent uniform \(U,V\),
\[
\mathbb E[B(U)^2]=\int_0^1 u(1-u)\,du=\frac16,
\quad
\mathbb E[B(U)B(V)]=\int_0^1\!\int_0^1(\min(u,v)-uv)\,du\,dv=\frac1{12}.
\]
All other mixed terms between distinct coordinates vanish because their uniform marks are independent and the bridge is centered. Since \(\operatorname{Var}(1-2U)=1/3\), this proves (2).

As an independent finite check, the exact degree covariances are
\[
\operatorname{Cov}(d_n(i),d_n(j))=\frac{n+1}{12}\quad(i\ne j),\qquad
\operatorname{Var}(d_n(i))=\frac{n-1}{6}+\frac{(2i-n-1)^2}{12}.
\tag{8}
\]
For the first identity, expand the two degrees into inversion indicators. Disjoint comparison pairs are independent. Their shared edge contributes \(1/4\); each of the other \(n-2\) vertices supplies three overlapping comparisons with net covariance \(1/12\), by the \(1/3\) and \(1/6\) probabilities for three-point orders. For the second, among two inversion comparisons incident to \(i\), equal-side neighbors contribute \(+1/12\) and opposite-side neighbors \(-1/12\); summing gives (8). The variance formula was also recorded in later literature and is not separately claimed as new. Substituting the critical-window indices into (8) agrees with (2).

## Verification

The standalone \`verify_mesoscopic.py\` exhaustively checks the exact means and covariance matrix against all permutations for \(2\le n\le7\), verifies the two bridge integrals exactly as rational numbers, and checks the convergence of the finite second moments along three growing sample sizes. It passed 186 assertions. An independent simulation at \(n=1001\) with 4,000 replicates and offsets \((-1,0,1)\) gave empirical off-diagonal covariances near \(0.08\), consistent with \(1/12\); simulation is diagnostic only. The actual proof of (1) is the empirical-process argument above, not the finite tests.

Reproduce exact checks with \`python3 verify_mesoscopic.py\` from the same directory as this document (Python standard library only).

## Relationship to prior work

Bhattacharya and Mukherjee (arXiv:1503.03582, first submitted 2015-03-12) establish the independent macroscopic label-degree limits at scale \(n\), and the one-point mid-vertex normal-mixture limit at scale \(\sqrt n\) (their Corollary 3.3 and Theorem 3.4). Their full preprint and hypergeometric proof of the latter were inspected. Neither assertion determines simultaneous \(\sqrt n\)-scale dependence among several labels approaching the middle at the critical rate. Here the shared bridge captures that dependence and its offset-dependent drifts. The one-point result is acknowledged as prior work, not rebranded as new.

Gürerk, Işlak and Yıldız (arXiv:1901.06678, first submitted 2019-01-20, later version 2021) provide another proof of the one-point mid-vertex limit and the exact individual degree variance; their relevant sections were inspected. These statements also do not give the marked joint law.

An independently available incidence-matrix covariance theorem for all inversion indicators (published-finding corpus record \`2026/10/4/SCOPE-incidence-precision-law-for-all-inversion-indicators-of-a-random--f6af0a8c3805\`) covers the pairwise inversion-indicator covariance geometry; its full result was inspected. By aggregation, this prior theory can imply (8). It gives no limiting *joint distribution* for fluctuating critical-window degrees, so (8) is evidence and not the new claim.

## Limitations

The result concerns fixed finitely many marked positions and does not give a functional limit for all indices in a growing window, a nonuniform-permutation analogue, or a rate of convergence. The use of the standard empirical-process central limit theorem is explicit; the finite checker cannot certify that infinite-dimensional input theorem. The literature comparison excludes specific closely related results but does not establish historical priority against every possible differently named local-permutation limit theorem. Independent mathematical review has not occurred.

## References

1. B. B. Bhattacharya and S. Mukherjee, *Degree Sequence of Random Permutation Graphs*, arXiv:1503.03582, version 1 of 2015-03-12, https://arxiv.org/abs/1503.03582.
2. O. Gürerk, Ü. Işlak and M. A. Yıldız, *A study on random permutation graphs*, arXiv:1901.06678, first submitted 2019-01-20, https://arxiv.org/abs/1901.06678.
3. J.-F. Marckert, *One more approach to the convergence of the empirical process to the Brownian bridge*, arXiv:0710.3296, first submitted 2007-10-17, https://arxiv.org/abs/0710.3296 (standard empirical-process background, not a permutation-graph result).
4. *Incidence precision law for all inversion indicators of a random permutation*, published-finding corpus finding 2026/10/4/SCOPE-incidence-precision-law-for-all-inversion-indicators-of-a-random--f6af0a8c3805, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-incidence-precision-law-for-all-inversion-indicators-of-a-random--f6af0a8c3805.
