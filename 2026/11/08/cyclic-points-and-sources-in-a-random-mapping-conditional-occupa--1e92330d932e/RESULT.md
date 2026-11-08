# Cyclic points and sources in a random mapping: conditional occupancy and independent limits

## Finding
Let \(F_n:[n]\to[n]\) be a uniformly random map, meaning that its \(n\) images are independent and uniform on \([n]\). Write \(C_n\) for the number of vertices belonging to directed cycles of its functional digraph, and \(Z_n\) for the number of vertices with in-degree zero. For every \(n\ge2\), \(1\le k<n\), and \(0\le r\le n-k\),
\[
\mathbb E\!\left[\binom{Z_n}{r}\mid C_n=k\right]
=\binom{n-k}{r}\left(1-\frac r n\right)^{n-k-1}.
\]
Consequently, conditional on \(C_n=k\), \(Z_n\) is distributed as the number of empty boxes among \(n-k\) designated boxes after \(n-k-1\) independent uniform throws into \(n\) boxes. If \(k=n\), then \(Z_n=0\) surely. In particular,
\[
\mathbb E[Z_n\mid C_n=k]=(n-k)\left(1-\frac1n\right)^{n-k-1}
\quad(1\le k<n),
\]
which decreases strictly with \(k\), including the final value zero. Thus \(\operatorname{Cov}(Z_n,g(C_n))<0\) for every nonconstant nondecreasing real function \(g\) on \(\{1,\ldots,n\}\).

Despite this strict finite-size negative regression, the two fluctuations have independent limits:
\[
\left(\frac{C_n}{\sqrt n},\frac{Z_n-n/e}{\sqrt n}\right)
\xrightarrow{\ d\ }(R,N),
\]
where \(\Pr\{R>x\}=\exp(-x^2/2)\) for \(x\ge0\), \(N\) is centered normal with variance \(e^{-1}-2e^{-2}\), and \(R,N\) are independent. These are assertions about one common mapping, not independently sampled marginal statistics.

## Assumptions and scope
Self-loops and directed cycles of every positive length are allowed. Each of the \(n^n\) mappings has probability \(n^{-n}\). A cyclic vertex belongs to a periodic orbit; a zero-in-degree vertex has no preimage. All conditional laws refer to the exact event \(C_n=k\), which has positive probability for each \(1\le k\le n\). The finite formula is exact for all integer parameters within the stated ranges; the limit holds as \(n\to\infty\) through positive integers. In the limit notation \(R\) has the Rayleigh distribution with unit scale.

## Proof
**1. Deletion identity.** Let \(S\) be any fixed \(r\)-subset of \([n]\). The event \(S\subseteq\{v:\deg^-(v)=0\}\) means that all images of \(F_n\) avoid \(S\); its probability is \(((n-r)/n)^n\). Conditioned on this event, the images of vertices in \([n]\setminus S\) are independent uniform on the remaining \(n-r\) vertices. They therefore define an ordinary uniform mapping on that complement. The images of the deleted vertices also land in the complement and cannot belong to a cycle, while the original cycles inside the complement are unchanged. For any bounded function \(f\), with \(0\le r<n\),
\[
\mathbb E\!\left[\binom{Z_n}{r}f(C_n)\right]
=\binom nr\left(\frac{n-r}{n}\right)^n\mathbb E[f(C_{n-r})].\tag{1}
\]
Here the last expectation is under a separately defined uniform mapping on \(n-r\) points. The case \(r=n\) gives zero on the left because every finite mapping has at least one vertex with positive indegree.

**2. Cyclic-point distribution and conditional law.** Exactly \(\binom nk k!\,k n^{n-k-1}\) mappings have \(k\) cyclic vertices: choose the cyclic labels, permute their cycle edges, and choose a directed forest with those \(k\) prescribed roots using the classical rooted-forest count \(k n^{n-k-1}\). Thus
\[
\Pr(C_n=k)=\frac{k(n)_k}{n^{k+1}},\qquad 1\le k\le n,
\tag{2}
\]
where \((n)_k=n(n-1)\cdots(n-k+1)\). The forest count also holds at \(k=n\) by interpretation as one empty forest. Apply (1) with \(f=\mathbf1_{\{k\}}\), then divide by (2):
\[
\frac{\binom nr ((n-r)/n)^n\Pr(C_{n-r}=k)}{\Pr(C_n=k)}
=\binom{n-k}{r}\left(\frac{n-r}{n}\right)^{n-k-1}.
\tag{3}
\]
This formula includes \(r=0\). It equals the \(r\)-th binomial moment of the number of empty designated boxes after \(n-k-1\) independent uniform allocations among all \(n\) boxes, since any prescribed \(r\) designated boxes are jointly empty with probability \((1-r/n)^{n-k-1}\). Since both variables are supported on \(\{0,\ldots,n-k\}\), equality of their binomial moments establishes equality of distributions. An explicit probability formula is
\[
\Pr(Z_n=z\mid C_n=k)=\binom{n-k}{z}
\sum_{j=0}^{n-k-z}(-1)^j\binom{n-k-z}{j}
\left(1-\frac{z+j}{n}\right)^{n-k-1},\tag{4}
\]
for \(0\le z\le n-k\), \(k<n\).

**3. Strict negative regression.** Put \(q=1-1/n\). Conditional means from (3) equal \(h(t)=tq^{t-1}\) at \(t=n-k\in\{1,\ldots,n-1\}\), with \(h(0)=0\). For every \(1\le t<n-1\),
\[
\frac{h(t+1)}{h(t)}=\frac{t+1}{t}\frac{n-1}{n}>1.
\]
Also \(h(1)>h(0)\). Hence \(\mathbb E[Z_n\mid C_n=k]\) strictly decreases in \(k\). Every \(C_n=k\) has positive probability, so the covariance of this strictly decreasing function with any nonconstant nondecreasing \(g(C_n)\) is strictly negative, by the independent-copy identity \(2\operatorname{Cov}(A,B)=\mathbb E[(A-A')(B-B')]\).

**4. Rayleigh marginal.** From (2), or from its telescoping representation,
\[
\Pr(C_n\ge r)=\frac{(n)_r}{n^r}
=\prod_{j=0}^{r-1}\left(1-\frac jn\right).
\tag{5}
\]
For \(r=\lfloor x\sqrt n\rfloor+1\), the logarithm tends to \(-x^2/2\). Therefore \(C_n/\sqrt n\Rightarrow R\), with the stated Rayleigh tail.

**5. Normal marginal and uniform conditional coupling.** Let \(Y_n\) be the number of empty boxes after \(n\) independent uniform throws into \(n\) boxes. The classical occupancy central limit theorem yields
\[
\frac{Y_n-n/e}{\sqrt n}\Rightarrow N(0,e^{-1}-2e^{-2}).\tag{6}
\]
One can also obtain (6) by Poissonizing the bin occupancies and conditioning on their total: for independent Poisson(1) counts, the covariance of the emptiness indicator and the count is \(-e^{-1}\), so the conditional Gaussian variance is \(e^{-1}(1-e^{-1})-e^{-2}=e^{-1}-2e^{-2}\). The standard lattice local central limit theorem justifies conditioning; alternatively, invoke the classical occupancy CLT cited below.

Fix \(M<\infty\). For \(1\le k\le M\sqrt n\), set \(m=n-k-1\) and \(r=k+1\). On a common sequence of \(n\) independent uniform throws, let \(X_{n,k}\) count the empty boxes among the first \(n-k\) boxes after the first \(m\) throws; let \(Y_n\) count all empty boxes after all \(n\) throws. By (3), \(X_{n,k}\) has the conditional distribution of \(Z_n\) given \(C_n=k\). Let \(A\) count empty boxes among the *last* \(k\) boxes after the first \(m\) throws, and let \(B\) count formerly empty boxes (among all \(n\)) first occupied during the last \(r\) throws. Then \(X_{n,k}-Y_n=B-A\).

Empty-box indicators for multinomial allocations have nonpositive pairwise covariances, so \(\operatorname{Var}(A)\le k\). Conditional on the first \(m\) throws, \(B\) changes by at most one under resampling any of its \(r\) independent later throws; Efron--Stein therefore gives \(\mathbb E[\operatorname{Var}(B\mid\text{first }m)]\le r/2\). If \(H_m\) is the number of empty boxes after those first \(m\) throws, then
\[
\mathbb E[B\mid\text{first }m]
=H_m\left(1-(1-1/n)^r\right).
\]
Again \(\operatorname{Var}(H_m)\le n\), and \(1-(1-1/n)^r\le r/n\), so \(\operatorname{Var}(B)\le r/2+r^2/n\). Finally,
\[
\mathbb E X_{n,k}=(n-k)(1-1/n)^{n-k-1},
\quad\mathbb E Y_n=n(1-1/n)^n,
\]
and their difference is bounded uniformly for \(k\le M\sqrt n\), by expanding the logarithm of their ratio, or directly from \((1-k/n)(1-1/n)^{-k-1}=1+O_M(1/n)\). Therefore
\[
\sup_{1\le k\le M\sqrt n}
\frac{\mathbb E[(X_{n,k}-Y_n)^2]}n\longrightarrow0.\tag{7}
\]
By coupling and (6), the conditional centered-and-scaled law of \(Z_n\) converges to the same normal law **uniformly** in this range in bounded-Lipschitz distance. The Rayleigh tightness of \(C_n/\sqrt n\), together with the tower property, then implies that for any bounded continuous test functions \(u,v\),
\[
\lim_{n\to\infty}\mathbb E\left[u(C_n/\sqrt n)
 v((Z_n-n/e)/\sqrt n)\right]
=\mathbb E[u(R)]\,\mathbb E[v(N)].\tag{8}
\]
This proves the stated joint convergence to independent marginals. The finite negative covariance does not contradict asymptotic independence, because its normalized contribution vanishes.

## Verification
The standalone Python file `check_mapping.py` enumerates every mapping of \([n]\) for \(2\le n\le7\) (up to \(7^7=823543\) maps), computes both observables directly, checks the exact cyclic-point probabilities, verifies the conditional distribution through the inclusion--exclusion formula (4) and every conditional binomial moment (3), and checks strict negative regression. It additionally verifies the conditional monotonicity identity for sizes up to \(100\). Running `python check_mapping.py` yields `VERIFY_OK 464 exact assertions`. This finite computation is a reproducibility cross-check, not a substitute for the proof for all sizes or the asymptotic argument.

## Relationship to prior work
The classical random-mapping decomposition into directed cycles carrying rooted forests and the marginal Rayleigh law are established facts; no novelty is asserted for them. Finch (2022) analyzes cyclic points, components and cycle sizes, not the two-observable conditional distribution stated here. Hansen and Jaworski (2007, 2010) develop exchangeable-in-degree and prescribed-cyclic-point forest decompositions, which are closely related and can imply some of the counting steps. The exact distributional equivalence (3)--(4), its strict monotone-regression consequence, and the joint independent Rayleigh--Gaussian limit constitute the scoped claim. Standard empty-box Gaussian asymptotics are also prior knowledge, not part of the novelty claim.

## Limitations
The theorem concerns uniform mappings with unrestricted indegrees. It does not claim independence at any finite order, an optimal convergence rate, a generalization to nonuniform images, or an independently audited result. The conditional representation can potentially be recovered from classical random-forest enumeration or older mixed generating functions, and priority of its full combination with the joint limit requires broader historical scrutiny. An accessible 2010 paper on prescribed cyclic-point counts was inspected at its abstract, introduction and component-size theorem; these pages do not settle all possible implicit derivations in its other sections. The asymptotic normal limit invokes a standard occupancy CLT rather than deriving that theorem from first principles.

## References
- S. R. Finch, *Components and Cycles of Random Mappings* (first public version 2022-05-11), https://arxiv.org/abs/2205.05579v1 .
- J. C. Hansen and J. Jaworski, *Random mappings with exchangeable in-degrees*, Random Structures & Algorithms 33 (2008), 105--126, first available 2007, https://doi.org/10.1002/rsa.20187 .
- J. C. Hansen and J. Jaworski, *Random mappings with a given number of cyclical points*, Ars Combinatoria 94 (2010), 341--359, https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/ .
- V. E. Stepanov, *Limiting distributions of certain characteristics of random mappings*, Theory of Probability & Its Applications 14 (1969), 612--626, https://doi.org/10.1137/1114078 .
- B. A. Sevast'yanov and V. P. Chistyakov, *Asymptotic Normality in the Classical Ball Problem*, Theory of Probability & Its Applications 9 (1964), https://doi.org/10.1137/1109034 .
