# Two observation-horizon laws for perfectly grounded leaders on star networks

## Finding
Let \(G=K_{1,m}\) be the unit-conductance star with hub \(0\), \(m\ge 2\) leaves and exactly \(1\le k\le m\) perfectly pinned leaders \(S\). Write \(F=V(G)\setminus S\) and let \(L_{FF}(S)\) be the principal follower block of the **original** combinatorial graph Laplacian (retaining the diagonal contributions from edges to leaders). For every physical horizon \(T>0\), define
\[
Q_T(S)=\operatorname{tr}\!\left(e^{-2T L_{FF}(S)}\right),\qquad
E_T(S)=\int_0^T Q_s(S)\,ds.
\]
Here \(Q_T\) is the squared Frobenius norm of the follower propagator; \(E_T\) is the total covariance trace at horizon \(T\) for unit-isotropic white-noise forcing from zero initial covariance. For a chosen \(k\), there are precisely two symmetry types: \(\mathsf L\), with \(k\) leaves pinned and the hub unpinned, and \(\mathsf H\), with the hub and \(k-1\) leaves pinned.

For \(1\le k<m\), put
\[
\lambda_\pm=\frac{m+1\pm\sqrt{(m+1)^2-4k}}2,\quad
\alpha=1-\lambda_-\in(0,1),\quad \beta=\lambda_+-1>\alpha.
\]
There is exactly one positive \(T_Q(m,k)\) solving
\[
e^{2\alpha T_Q}+e^{-2\beta T_Q}=2.
\]
Every \(\mathsf L\) placement uniquely minimizes \(Q_T\) up to leaf relabeling for \(0<T<T_Q\), every \(\mathsf H\) placement does so for \(T>T_Q\), and the two types tie at \(T_Q\). The phrase *uniquely up to relabeling* refers to the optimal **type**; every choice of the indicated \(k\) leaves realizes that type.

For the integrated-noise objective \(E_T\), the classification is different. If \(2k<m+1\), there is exactly one \(T_E(m,k)>T_Q(m,k)\) solving
\[
\frac{1-e^{-2\lambda_-T_E}}{\lambda_-}
+\frac{1-e^{-2\lambda_+T_E}}{\lambda_+}
=2(1-e^{-2T_E}).
\]
The optimal type is \(\mathsf L\) for \(0<T<T_E\), both types at equality, and \(\mathsf H\) for \(T>T_E\). If \(2k\ge m+1\), **only** type \(\mathsf L\) minimizes \(E_T\) at every finite positive \(T\), including the exactly tied *infinite-horizon* case \(2k=m+1\). At \(k=m\), type \(\mathsf L\) strictly minimizes both objectives for every \(T>0\).

For each fixed positive integer \(k\), as \(m\to\infty\), the two transition times have different universal limits:
\[
T_Q(m,k)\longrightarrow\frac{\log 2}{2},\qquad
T_E(m,k)\longrightarrow\frac{\tau_0}{2},
\]
where \(\tau_0\approx 1.59362426004004\) is the unique positive solution of \(\tau=2(1-e^{-\tau})\). In particular, the instantaneous-error optimizer eventually selects the hub at every budget \(1\le k<m\), while the finite-horizon stochastic-error optimizer **never** selects the hub when \(2k\ge m+1\). Thus the two natural horizon-dependent performance measures can prescribe disjoint leader types for an open interval of times (indeed for all sufficiently large times in this budget regime).

## Assumptions and scope
All star edges have conductance one; the graph has \(m+1\) vertices. The leader count is exact, leaders are ideal zero-error pinned vertices, the hub is vertex \(0\), and the other vertices are interchangeable leaves. A follower next to a pinned leader still has its original Laplacian diagonal contribution. Both criteria sum over **followers only**. Time is continuous and positive. White-noise covariance interpretation uses the stochastic differential equation \(dx=-L_{FF}(S)x\,dt+dW\) with independent unit-intensity forcing on followers and deterministic initial state zero. This convention makes \(E_T\), without extra factor, the covariance trace. All eigenvalues used are strictly positive because \(k\ge1\).

## Proof
**1. Exhaustive symmetry reduction.** A set of exactly \(k\) leaders either contains the hub or not. The automorphism group of \(K_{1,m}\) is transitive within both types. If the hub is pinned, the remaining \(m-k+1\) followers are isolated from each other and each retains diagonal degree one. Thus the follower spectrum of type \(\mathsf H\) is \(1\) with multiplicity \(m-k+1\).

If \(k<m\) leaves alone are pinned, the follower block (hub first) is
\[
\begin{pmatrix}m&-\mathbf 1^{\mathsf T}\\-\mathbf 1&I_{m-k}\end{pmatrix}.
\]
The subspace of leaf vectors summing to zero supplies eigenvalue \(1\) with multiplicity \(m-k-1\). The remaining two-dimensional quotient has characteristic polynomial \(z^2-(m+1)z+k\), giving \(0<\lambda_-<1<\lambda_+\). If \(k=m\) leaves are pinned, only the hub remains and its eigenvalue is \(m\). These cases exhaust every feasible leader set.

**2. The unique instantaneous switch.** When \(1\le k<m\), subtraction cancels the common \(m-k-1\) unit eigenvalues and yields
\[
Q_T(\mathsf L)-Q_T(\mathsf H)
=e^{-2\lambda_-T}+e^{-2\lambda_+T}-2e^{-2T}
=e^{-2T}\big(e^{2\alpha T}+e^{-2\beta T}-2\big).
\]
The parenthesized function has value zero at \(T=0\), initial derivative \(2(\alpha-\beta)=2(1-m)<0\), strictly positive second derivative for all \(T\ge0\), and tends to infinity. A strictly convex function with those properties has exactly one additional zero, is strictly negative before it and strictly positive after it. Hence the asserted exhaustive optimizer classification for \(Q_T\).

**3. The integrated horizon law, including its boundary.** Let
\[
D(T)=E_T(\mathsf L)-E_T(\mathsf H)
=\frac12\left[
\frac{1-e^{-2\lambda_-T}}{\lambda_-}
+\frac{1-e^{-2\lambda_+T}}{\lambda_+}
-2(1-e^{-2T})\right].
\]
Then \(D(0)=0\) and \(D'(T)=Q_T(\mathsf L)-Q_T(\mathsf H)\), whose sign by step 2 is negative until \(T_Q\), then positive. Thus \(D\) strictly decreases to a negative minimum at \(T_Q\), then strictly increases. As \(T\to\infty\), using \(\lambda_-\lambda_+=k\) and \(\lambda_-+\lambda_+=m+1\),
\[
\lim_{T\to\infty}D(T)
=\frac12\left(\frac{m+1}{k}-2\right)
=\frac{m+1-2k}{2k}.
\]
If this is positive, strict monotonicity after \(T_Q\) gives one finite positive crossing \(T_E>T_Q\), with the signs claimed. If the limit is zero or negative, the function remains strictly negative at every finite positive time (in the zero case it approaches zero strictly from below). This establishes the exact strict boundary \(2k=m+1\) without treating an infinite-time tie as a finite-time tie.

For \(k=m\), the two follower spectra are \(\{m\}\) for type \(\mathsf L\) and \(\{1\}\) for type \(\mathsf H\); since \(m>1\), the former has strictly lower instantaneous trace and strictly lower integral for every \(T>0\).

**4. Fixed-budget large-star limit.** Fix \(k\) and let \(m\to\infty\). The quadratic roots obey \(\lambda_-=k/(m+1)+O(m^{-2})\) and \(\lambda_+=m+1+O(m^{-1})\), so \(\alpha\to1\) and \(\beta\to\infty\). On compact positive-time intervals the instantaneous crossing equation tends uniformly to \(e^{2T}=2\). The sign pattern and uniqueness from step 2 force \(T_Q\to(\log2)/2\). Similarly the integrated comparison converges uniformly on compact positive-time intervals to
\[
\frac12\big(2T-2(1-e^{-2T})\big).
\]
This limiting function is initially negative, is strictly convex for positive time and has one positive zero \(T=\tau_0/2\), where \(\tau_0=2(1-e^{-\tau_0})\). The finite positive crossings exist for all sufficiently large \(m\) (since fixed \(k\) satisfies \(2k<m+1\)) and converge to that unique zero. No inference about infinite \(m\) relies on numerical samples.

## Verification
The standalone `verify.py` uses Python 3 and NumPy. It constructs the full grounded combinatorial Laplacian independently for every \(2\le m\le32\) and every \(1\le k\le m\), checks both leader types against the claimed eigenvalues, and compares instantaneous and integrated traces at multiple horizons. It also brackets positive instantaneous roots, checks strict signs before and after them, verifies the existence and later position of integrated roots when \(2k<m+1\), checks persistent preference otherwise, and verifies stationary trace differences through \(m=59\). Run `python3 verify.py`; the expected final message is `VERIFIED 21043 matrix, transient, and stationary comparisons`. All general sign and uniqueness arguments are analytic, not experimental.

For a concrete example, \(m=5,k=2\) gives \(T_Q\approx0.53398252319\) and \(T_E\approx1.25029565747\). With \(m=5,k=4\), the instantaneous type switches at \(T_Q\approx1.46810508855\), but type \(\mathsf L\) remains the strictly better finite-horizon stochastic choice for every \(T>0\).

## Relationship to prior work
Clark, Bushnell and Poovendran (2012, arXiv:1208.0946), and Clark, Alomair, Bushnell and Poovendran (2013, arXiv:1306.4949), develop supermodular leader-selection methods for steady-state network error and for bounded finite-time convergence errors, respectively. The latter result treats upper bounds defined by matrix-row probabilities rather than exact grounded heat-trace or finite-horizon white-noise covariance objectives; it does not classify optimal hub/leaf sets by time or budget.

The published result *Optimal noise-free leaders on an arbitrarily weighted star: two candidate sets and a re-entrant hub* (published-finding corpus public research record, 2026-11-08) gives a stronger **steady-state inverse-trace** classification for arbitrary weighted stars; setting all weights equal recovers the \(2k=m+1\) stationary comparison above. That prior result therefore covers the infinite-time comparison and is not asserted to be novel here. It does not give the two **finite-time** crossing laws, the always-leaf finite-horizon regime, or the distinct fixed-budget limiting times. Earlier network coherence work (Lin, Fardad and Jovanović, arXiv:1302.0450) supplies the standard grounded-Laplacian objective but not this time-resolved optimizer classification. A published fixed-two-leader complete-bipartite heat-trace result has different graphs and parameter ranges; its statement does not imply the present all-budget star theorem.

## Limitations
This is an exact theorem on unweighted stars, not a theorem for arbitrary graphs or positive nonuniform spoke conductances. It assumes ideal grounded leaders and spatially isotropic follower noise with no initial covariance; arbitrary nonuniform noise, finite feedback gains or nonzero initial covariance can change the criteria and minimizers. The universal limits are proved only for fixed leader budget as \(m\) grows. The stationary all-budget threshold is existing work, used solely for comparison. The inspections below do not exclude every unpublished or unindexed equivalent finite-horizon classification. An independent mathematical audit has not been performed.

## References
1. A. Clark, L. Bushnell and R. Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems*, first public arXiv posting 2012-08-04, https://arxiv.org/abs/1208.0946.
2. A. Clark, B. Alomair, L. Bushnell and R. Poovendran, *Minimizing Convergence Error in Multi-Agent Systems via Leader Selection: A Supermodular Optimization Approach*, first public arXiv posting 2013-06-20, https://arxiv.org/abs/1306.4949.
3. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, first public arXiv posting 2013-02-03, https://arxiv.org/abs/1302.0450.
4. *Optimal noise-free leaders on an arbitrarily weighted star: two candidate sets and a re-entrant hub*, public research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-optimal-noise-free-leaders-on-an-arbitrarily-weighted-star-two-c--58eb0fc2195a.
