# Sharp Fourier sampling spectrum and critical mass crossover for rooted cycle forests

## Finding

For every integer \(n\ge3\) and activity \(q>0\), sample a **rooted spanning forest** on the labelled cycle \(C_n\): a proper edge subset \(F\subsetneq E(C_n)\) has probability proportional to
\[
q^{k(F)}\prod_{T\in\mathcal C(F)}|V(T)|,
\]
where \(k(F)\) is its number of components. Let \(X_j=\mathbf1_{\{e_j\in F\}}\) be the \(n\) edge indicators and \(C_{n,q}=\operatorname{Cov}(X)\), normalized as a probability covariance (without an additional factor of \(1/n\)). Let \(\sigma_j\) be its Fourier eigenvalue at frequency \(2\pi j/n\). Define
\[
t=\frac{q+2-\sqrt{q(q+4)}}2\in(0,1),\quad
b=\frac{1-t}{1+t},\quad H_n=\frac{1+t^n}{1-t^n}.
\]
Then \(C_{n,q}\) is positive definite and its **complete** spectrum is
\[
\boxed{\sigma_0=\frac{2tbH_n}{(1+t)^2}-\frac{2nb^2t^n}{(1-t^n)^2}},
\]
\[
\boxed{\sigma_j=bH_n\left(1-\frac{b(1-t^4)}{1-2t^2\cos(2\pi j/n)+t^4}\right)},\qquad 1\le j<n.
\]
The unique minimum is \(\sigma_0\). The maximum is precisely at the alternating Fourier mode \(j=n/2\) for even \(n\), or at the two conjugate near-alternating modes \(j=(n\pm1)/2\) for odd \(n\). The nonzero-frequency eigenvalues are strictly increasing with angular frequency from \(2\pi/n\) to the frequency closest to \(\pi\). In particular the exact squared-energy Riesz condition ratio is \(\kappa_{n,q}=\sigma_{\lfloor n/2\rfloor}/\sigma_0\), with both terms given above.

The ratio has a **sharp mass-scale crossover**. For every fixed \(q>0\),
\[
\boxed{\lim_{n\to\infty}\kappa_{n,q}=\frac{(1+t)^2}{1+t^2}\in(1,2).}
\]
For any sequence \(q_n>0\), if \(n^2q_n\to c\in(0,\infty)\),
\[
\boxed{\lim_{n\to\infty}\kappa_{n,q_n}
=\frac{2\sinh\sqrt c}{\sinh\sqrt c-\sqrt c}.}
\]
This function is strictly decreasing from \(+\infty\) to \(2\) as \(c\) grows. If \(n^2q_n\to0\), then \(\kappa_{n,q_n}\sim12/(n^2q_n)\). If \(q_n\to0\) while \(n^2q_n\to\infty\), then \(\kappa_{n,q_n}\to2\). The small-mass and large-cycle limits therefore do not commute.

## Assumptions and scope

The cycle is simple with at least three labelled vertices, one unit-conductance edge between successive vertices, and independent strictly positive root activity \(q\) per rooted component. Every component is a tree; each has exactly one chosen root. The weight above is the marginal weight of the unrooted edge set after summing its root choices. The complete cycle is excluded because it is not a forest. Frequencies are the characters \(j\mapsto e^{2\pi i sj/n}\). All eigenvalues use probability covariance rather than a convention with extra sample-count scaling. The condition ratio is the ratio of largest to smallest eigenvalues of this positive definite real symmetric matrix. In the fixed-\(q\) limit the activity does not depend on \(n\); in the critical window \(q_n\) depends on \(n\).

## Proof

**1. Determinantal edge covariance.** Give an additional hub and join it to every vertex of \(C_n\) by a spoke of conductance \(q\). Removing the hub from a weighted spanning tree selects a rooted forest with the required law. Let \(L=2I-S-S^{-1}\) be the cycle Laplacian and \(D=I-S\) a consistently oriented edge-to-vertex incidence matrix. The matrix-tree determinant identity and differentiation with respect to individual rim conductances give the transfer-current kernel
\[
K=D(qI+L)^{-1}D^*=L(qI+L)^{-1}=I-qG,
\qquad G=(qI+L)^{-1}.
\]
For distinct edges \(i\ne j\), the determinantal pair-inclusion identity gives \(\operatorname{Cov}(X_i,X_j)=-K_{ij}^2\), and \(\operatorname{Var}(X_i)=K_{ii}(1-K_{ii})\). Thus, writing \(a=K_{00}=1-qG_0\),
\[
C_{ij}=a\mathbf1_{i=j}-K_{ij}^2.
\]
The identity also follows directly by differentiating the logarithm of the weighted spanning-tree determinant twice. No independence approximation is used.

**2. Exact cyclic Green function.** The smaller root \(t\in(0,1)\) of \(t+t^{-1}=q+2\) has \(q=(1-t)^2/t\) and \(\sqrt{q(q+4)}=(1-t^2)/t\). Periodizing the infinite-line Green kernel \(t^{|d|}/\sqrt{q(q+4)}\) gives, for \(0\le d<n\),
\[
G_d=\frac{t^d+t^{n-d}}{\sqrt{q(q+4)}(1-t^n)}.
\]
This solves \((q+2)G_d-G_{d-1}-G_{d+1}=\mathbf1_{d=0}\) with periodic boundary, and uniqueness follows from positive definiteness of \(qI+L\). Hence \(qG_0=bH_n\).

**3. Squared-Green Fourier sum.** For each \(j\), Fourier transforming the circulant covariance gives
\[
\sigma_j=qG_0-q^2\sum_{d=0}^{n-1}G_d^2e^{-2\pi i jd/n}.
\]
For \(r=t^2\) and \(\theta=2\pi j/n\), expand \((t^d+t^{n-d})^2\). The two geometric series for \(t^{2d}\) and \(t^{2n-2d}\) combine into
\[
(1-t^{2n})\frac{1-t^4}{1-2t^2\cos\theta+t^4},
\]
while their cross term \(2t^n\) contributes \(2nt^n\mathbf1_{j=0}\). Dividing by the squared Green denominator, using \(q/\sqrt{q(q+4)}=b\), gives for all \(j\)
\[
q^2\sum_dG_d^2e^{-2\pi i jd/n}
=b^2H_n\frac{1-t^4}{1-2t^2\cos\theta+t^4}
+\frac{2nb^2t^n}{(1-t^n)^2}\mathbf1_{j=0}.
\]
At \(j=0\), \(b(1+t^2)/(1-t^2)=(1+t^2)/(1+t)^2\), yielding the stated zero-mode expression. At nonzero \(j\), the rational expression gives the claimed complete spectrum.

**4. Exact global extremizers and positivity.** Since \(t\in(0,1)\), the denominator \(1-2t^2\cos\theta+t^4\) is strictly increasing in angular distance from zero up to \(\pi\). Thus the nonzero-frequency eigenvalues strictly increase in this distance, with the indicated parity-dependent maximizers. For every \(j\ne0\), the denominator is strictly larger than \((1-t^2)^2\); the zero-frequency Fourier sum has in addition the strictly positive cross term \(2nb^2t^n/(1-t^n)^2\). Consequently \(\sigma_j>\sigma_0\). Every proper subset of cycle edges, including the empty set and each singleton, has strictly positive forest probability. If a linear score \(\sum_jv_jX_j\) were almost surely constant, evaluation first at the empty set and then at each singleton would force all \(v_j=0\). Hence the covariance is positive definite, in particular \(\sigma_0>0\).

**5. Fixed-mass thermodynamic limit.** At fixed positive \(q\), \(t<1\) is fixed, \(H_n\to1\), and \(nt^n\to0\). The angular argument of \(\sigma_{\lfloor n/2\rfloor}\) converges to \(\pi\). Therefore
\[
\sigma_0\to\frac{2tb}{(1+t)^2},\qquad
\sigma_{\lfloor n/2\rfloor}\to\frac{2tb}{1+t^2}.
\]
Division yields \((1+t)^2/(1+t^2)\), strictly between 1 and 2.

**6. Critical window and its two sides.** Suppose \(n^2q_n\to c>0\), let \(u=\sqrt c\). From \(t+t^{-1}=2+q_n\), \(n(1-t)\to u\), \(t^n\to e^{-u}\), \(nb\to u/2\), and \(H_n\to\coth(u/2)\). The two exact extreme formulas give
\[
 n\sigma_{\lfloor n/2\rfloor}\to\frac u2\coth(u/2),
\quad n\sigma_0\to\frac u4\coth(u/2)-\frac{u^2}{8\sinh^2(u/2)}.
\]
Their ratio simplifies to \(2\sinh u/(\sinh u-u)\). Its derivative has the sign of \(\sinh u-u\cosh u<0\), proving strict decrease; the endpoint limits follow from the Taylor series and exponential growth of \(\sinh u\). If \(n^2q_n\to\infty\) and \(q_n\to0\), then \(t^n\to0\), \(t\to1\), and the formulas in step 5 remain valid with varying \(t\) after using \(n(1-t)\to\infty\); the ratio tends to 2.

For \(n^2q_n\to0\), let \(A_{n,k}\) count hub-spoke configurations with exactly \(k\) spokes. The cyclic cut/spoke count gives \(A_{n,k}=\frac nk\binom{n+k-1}{2k-1}\); in particular \(A_{n,1}=n^2\), \(A_{n,2}=n^2(n^2-1)/12\). The ratio of total weight of \(k=2\) to \(k=1\) is \((n^2-1)q_n/12\), and the weight of \(k\ge3\) is \(O((n^2q_n)^2)\) relative to \(k=1\), uniformly in \(n\), by the factorial bound on \(A_{n,k}\). Thus \(\operatorname{Var}(k)\sim(n^2-1)q_n/12\). Because exactly \(k\) rim edges are deleted, the zero-mode eigenvalue is \(\sigma_0=\operatorname{Var}(k)/n\), giving \(n\sigma_0\sim(n^2-1)q_n/12\). The nonzero-mode exact formula also gives \(n\sigma_{\lfloor n/2\rfloor}\to1\) uniformly in this regime. Division proves \(\kappa_{n,q_n}\sim12/(n^2q_n)\).

## Verification

Run `python3 verify_cycle_forest.py` with Python 3; only the standard library is required. Its finite independent enumeration covers all proper edge subsets for \(3\le n\le10\) at three rational activities and calculates weighted moments directly, before Fourier transformation. These are compared with the closed eigenvalue formulas and predicted extreme modes. Additional numerical checks cover fixed mass, the critical mass-scale crossover, and the vanishing-mass asymptotic; the current script prints the actual total of assertions. All-size conclusions, uniform low-mass estimates, and strict monotonicity follow from the proof, not from these finite computations.

## Relationship to prior work

The weighted rooted-forest measure, determinant partition function, and transfer-current determinantal identity are classical and not claimed as new. Grunwald and Mednykh's circulant-forest work gives partition-function enumerations; it does not state the edge-indicator Fourier covariance spectrum. Avena and collaborators describe the general rooted-forest model and applications to multiresolution graph analysis. D'Achille, Enriquez and Melotti supply the general determinant and edge-inclusion kernel in a 2026 open-access article, whose main results concern complete graphs.

A publicly available wheel spanning-tree result gives the **full** finite spoke/cut composition law for every conductance and the even-Poisson critical component-count limit. That stronger distributional knowledge yields the zero-frequency variance by marginalization, so no novelty is claimed for the component-count distribution or its mean/variance alone. The present result is a new **Fourier spectral optimization and condition-ratio statement**: exact ordering of every spatial mode for every finite \(n,q\), the sharp location of both extreme eigenspaces, and their simultaneous critical-scale ratio. It requires separate analysis of nonzero spatial modes, absent from the prior distributional statement. A previously worked-out equivalent edge-structure-factor specialization may exist; historical priority is not independently certified.

## Limitations

The classification concerns homogeneous positive root activity and the edge-coordinate Fourier Gram only on a simple cycle. It does not treat unrooted equal-weight forests, inhomogeneous vertex masses, full wheel spoke-plus-rim covariance, more general circulant graphs, or an independent external audit. General determinantal and distributional results already contain strong ingredients, and novelty should be read as a new sharp spectral specialization rather than discovery of the underlying law.

## References

- L. Avena, F. Castell, A. Gaudillière and C. Mélot, *Random Forests and Networks Analysis*, arXiv:1711.01635 (first public 2017-11-05), https://arxiv.org/abs/1711.01635.
- L. A. Grunwald and I. A. Mednykh, *The number of rooted forests in circulant graphs*, arXiv:1907.02635 (first public 2019-07-04), https://arxiv.org/abs/1907.02635; *Ars Math. Contemp.* 22 (2022), doi:10.26493/1855-3974.2029.01d.
- M. D'Achille, N. Enriquez and P. Melotti, *Massive Spanning Forests on the Complete Graph: Exact Distribution and Local Limit*, *Random Structures & Algorithms* (2026), https://doi.org/10.1002/rsa.70048, especially Section 2.
- *Exact spoke–cut compositions in weighted wheel spanning trees and their critical spatial limit*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-spoke-cut-compositions-in-weighted-wheel-spanning-trees-an--c4b024089d31.
- *Quadratic vertex-covariance anisotropy of wheel spanning-tree polytopes*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-quadratic-vertex-covariance-anisotropy-of-wheel-spanning-tree-po--20c51f1ae988.
