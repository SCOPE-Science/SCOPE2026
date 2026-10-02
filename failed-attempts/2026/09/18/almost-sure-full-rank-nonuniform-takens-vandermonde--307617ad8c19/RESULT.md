# Almost-sure full rank for nonuniform Takens Vandermonde matrices

## Statement

Consider the generalized temporal Vandermonde matrix
\[
T(\tau,\theta)_{kp}=e^{i\tau_k\theta_p},
\qquad
1\le k\le \ell,\quad 1\le p\le m,
\]
where the delays \(\tau_k>0\) are pairwise distinct and the angles
\(\theta_p\in(-\pi,\pi]\) are pairwise distinct. This is the branch convention
\(z_p^{\tau_k}=e^{i\tau_k\theta_p}\) for \(z_p=e^{i\theta_p}\) used in
nonuniform delay-coordinate matrices. Let \(r=\min\{\ell,m\}\).

**Theorem.**

1. For every fixed admissible angle tuple \(\theta\), the set of delay tuples
   \(\tau\in(0,\infty)^\ell\) for which
   \[
   \operatorname{rank}T(\tau,\theta)<r
   \]
   has \(\ell\)-dimensional Lebesgue measure zero.

2. For every fixed admissible delay tuple \(\tau\), the set of angle tuples
   \(\theta\in(-\pi,\pi]^m\) for which
   \[
   \operatorname{rank}T(\tau,\theta)<r
   \]
   has \(m\)-dimensional Lebesgue measure zero.

3. In the admissible parameter set, full rank is an open dense condition.

Consequently, if the uneven delays have any joint probability law absolutely
continuous with respect to Lebesgue measure, then for every fixed set of
distinct frequencies,
\[
\Pr\!\left(\operatorname{rank}T=r\right)=1.
\]
The same statement holds with delays fixed and angles drawn from an absolutely
continuous joint law.

This resolves the probability-one rank conjecture used by Ng and Kutz for
non-uniformly sampled stable linear Takens embeddings, under the standard
probabilistic interpretation that the sampled continuous parameters have an
absolutely continuous law.

## Proof

The case \(r=1\) is immediate because every entry of \(T\) is nonzero. Assume
\(r\ge2\).

### A clustered exponential determinant

For pairwise distinct real numbers \(a_1,\ldots,a_r\) and
\(b_1,\ldots,b_r\), define
\[
N=\frac{r(r-1)}2,\qquad
V(a)=\prod_{1\le j<k\le r}(a_k-a_j),
\qquad
V(b)=\prod_{1\le p<q\le r}(b_q-b_p).
\]
Then, as \(\varepsilon\to0\),
\[
\det\!\left[e^{i\varepsilon a_jb_p}\right]_{j,p=1}^r
=
\frac{(i\varepsilon)^N}{\prod_{q=0}^{r-1}q!}
V(a)V(b)
+O(\varepsilon^{N+1}).
\tag{1}
\]

To see this, expand
\[
e^{i\varepsilon a_jb_p}
=
\sum_{n=0}^\infty
\frac{(i\varepsilon)^n}{n!}a_j^n b_p^n.
\]
Applying Cauchy--Binet to this factorization, the determinant is a sum over
strictly increasing exponent sets
\(0\le n_1<\cdots<n_r\). The smallest possible total degree is
\[
n_1+\cdots+n_r=0+1+\cdots+(r-1)=N,
\]
attained uniquely by \((n_1,\ldots,n_r)=(0,\ldots,r-1)\). Its coefficient is
exactly the product of the two ordinary Vandermonde determinants divided by
\(\prod_{q=0}^{r-1}q!\), proving (1). Since the \(a_j\) and \(b_p\) are
distinct, this leading coefficient is nonzero.

### Fixed angles, generic delays

Choose any \(r\) columns and \(r\) rows and denote their determinant by
\(D(\tau)\). It is a complex-valued real-analytic function of the selected
delays. We show that it is not identically zero.

Fix distinct real \(a_1,\ldots,a_r\), choose \(t_0>0\), and set
\[
\tau_j=t_0+\varepsilon a_j
\]
for sufficiently small positive \(\varepsilon\), so the selected delays remain
positive and distinct. Factoring \(e^{it_0\theta_p}\) from column \(p\),
\[
D(\tau)
=
e^{it_0\sum_{p=1}^r\theta_p}
\det\!\left[e^{i\varepsilon a_j\theta_p}\right]_{j,p=1}^r.
\]
Equation (1), with \(b_p=\theta_p\), shows that this determinant is nonzero for
all sufficiently small nonzero \(\varepsilon\). Hence \(D\) is not the zero
analytic function.

Now
\[
F(\tau)=|D(\tau)|^2
\]
is a nontrivial real-analytic function. The zero set of a nontrivial
real-analytic function has Lebesgue measure zero. Rank deficiency forces this
particular \(r\times r\) minor to vanish, so
\[
\{\tau:\operatorname{rank}T<r\}\subseteq\{\tau:F(\tau)=0\},
\]
which proves the first claim. If \(\ell>r\), the unused delay variables are
simply additional analytic variables; the same conclusion holds in the full
\(\ell\)-dimensional parameter space.

### Fixed delays, generic angles

Fix an admissible delay tuple and choose an \(r\times r\) minor. Select
pairwise distinct real \(b_1,\ldots,b_r\) and put
\[
\theta_p=\varepsilon b_p.
\]
For sufficiently small nonzero \(\varepsilon\), all selected angles are
distinct and lie in \((-\pi,\pi)\). Equation (1), now with
\(a_j=\tau_j\), shows that the minor is nonzero for sufficiently small
\(\varepsilon\). Thus the minor is not identically zero as a real-analytic
function of the angles. The same zero-set theorem gives measure zero for its
zero locus, and hence for the rank-deficient set. The boundary faces involving
the endpoint \(\theta=\pi\) themselves have Lebesgue measure zero, so the
half-open angular convention does not alter the conclusion.

### Openness and density

Full rank is open because at least one \(r\times r\) minor remains nonzero
under sufficiently small perturbations. The rank-deficient set is contained
in the zero set of a nontrivial real-analytic minor; such a zero set has empty
interior. Therefore the full-rank set is dense.

This completes the proof.

## Consequence for nonuniform stable linear Takens embeddings

Ng and Kutz factor the delay-coordinate matrix in their linear setting into a
temporal generalized Vandermonde factor and an observability factor. For a
class-\(A(d)\) system, the temporal factor has \(m=2d\) columns corresponding
to distinct oscillatory nodes \(e^{\pm i\theta_j}\). If \(\ell\ge2d\) and
the joint law of the uneven delays is absolutely continuous, the theorem above
gives full column rank of the temporal factor almost surely for the fixed
system frequencies.

Therefore the generalized-Vandermonde rank conjecture is not an additional
assumption for the paper's probability-one existence statement for stable
nonuniform delay embeddings: under its remaining observability assumptions,
the required temporal rank holds almost surely. Any separate hypotheses used
for asymptotic conditioning or convergence of embedding quality remain
necessary.

The result also strengthens the probabilistic interpretation by conditioning
on the dynamical system: the frequencies need not themselves be randomized.

## Rank is not conditioning

The proof simultaneously shows why the rank result does not solve the
finite-sample conditioning problem. For clustered delays
\[
\tau_j=t_0+\varepsilon a_j,
\]
the same selected square minor satisfies
\[
|D(\tau)|
=
\frac{|\varepsilon|^N}{\prod_{q=0}^{r-1}q!}
|V(a)V(\theta)|
+O(|\varepsilon|^{N+1}).
\tag{2}
\]
As \(\varepsilon\to0\), the rows coalesce and the matrix tends to rank one,
so its smallest singular value tends to zero even though every sufficiently
small generic nonzero \(\varepsilon\) gives full rank. Thus probability-one
injectivity and robust embedding are genuinely different questions. Equation
(2) also rules out any uniform positive lower bound on the smallest singular
value over all distinct uneven-delay configurations.

Recent work on generalized Vandermonde matrices in nonuniform array processing
derives deterministic minimum-singular-value bounds for structured segmented
sampling geometries. Those quantitative results are complementary: they do
not remove the need to distinguish generic full rank from uniform conditioning
over arbitrary delay configurations.

## Limitations

- The theorem is a rank/genericity statement. It gives no useful positive
  finite-sample lower bound on \(\sigma_{\min}(T)\).
- Absolute continuity matters. A discrete or singular sampling law can be
  supported on an aliasing set of measure zero and need not have full rank
  almost surely.
- Distinct angular nodes are essential. Frequency collisions modulo the chosen
  \(2\pi\) branch, including degenerate conjugate pairs at special angles, are
  outside the theorem.
- The consequence concerns the linear stable-Takens framework of the cited
  source; it is not a nonlinear Takens theorem.
- The proof resolves the source-specific probability-one rank conjecture.
  The analytic zero-set theorem, Cauchy--Binet expansion, and ordinary
  Vandermonde determinant used in the proof are standard tools and are not
  claimed as new.

## References

1. F. Ng and J. N. Kutz, *Stable Takens' Embedding Theorem for
   Non-Uniformly-Sampled Linear Systems*, arXiv:2608.14001 (2026).
   https://arxiv.org/abs/2608.14001
2. B. S. Mityagin, *The Zero Set of a Real Analytic Function*,
   Mathematical Notes 107 (2020), 529--530.
   https://doi.org/10.1134/S0001434620030189
3. W. Huang, K. Li, and P. Liu, *Generalized Hankel/Toeplitz matrix for
   array signal processing*, arXiv:2609.03325 (2026).
   https://arxiv.org/abs/2609.03325
4. H. L. Yap and C. J. Rozell, *Stable Takens' Embeddings for Linear
   Dynamical Systems*, IEEE Transactions on Signal Processing 59 (2011),
   4781--4794. https://doi.org/10.1109/TSP.2011.2160629
