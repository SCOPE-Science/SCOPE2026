# A uniform Dirichlet stationary limit with nonuniform finite laws for multipartite zealot copying

## Finding
Fix integers \(r\ge3\) and \(n\ge2\). On the unweighted complete \(r\)-partite graph with \(n\) vertices in every part, fix one vertex of part \(j\) forever at opinion \(j\), for each \(j=1,\ldots,r\). All other vertices independently at rate one copy the opinion of a uniformly chosen neighbor. In its unique stationary law, let \(X_{j,a}^{(n)}\) be the fraction of vertices in part \(j\) holding opinion \(a\), including its fixed vertex; put \(P_a^{(n)}=r^{-1}\sum_j X_{j,a}^{(n)}\).

For **every finite** \(n\ge2\),
\[
\mathbb E X_{j,a}^{(n)}=\begin{cases}
 (n+r-2)/(rn-1),&j=a,\\
 (n-1)/(rn-1),&j\ne a,
\end{cases}\qquad
\mathbb E P_a^{(n)}=\frac1r.
\]
As \(n\to\infty\) at fixed \(r\), the entire \(r\times r\) matrix converges jointly in distribution,
\[
\big(X_{j,a}^{(n)}\big)_{j,a}
\ \Longrightarrow\ (P_a)_{j,a},\qquad
(P_1,\ldots,P_r)\sim\operatorname{Dirichlet}(1,\ldots,1).
\]
In particular, the limiting global opinion vector is **uniform on the probability simplex**, and every part's opinion vector synchronizes to this same random limit despite the complete absence of within-part edges. For nonnegative integers \(k_1,\ldots,k_r\), \(K=\sum_a k_a\),
\[
\lim_{n\to\infty}\mathbb E\prod_{a=1}^r(P_a^{(n)})^{k_a}
=\frac{(r-1)!\prod_{a=1}^r k_a!}{(K+r-1)!}.
\]
The result is **not** an exact finite-size Dirichlet-multinomial law. At the smallest nontrivial example, \(r=3,n=2\), define \(F_a\) as the number of **flexible** (nonzealot) vertices of opinion \(a\), so \(\sum_aF_a=3\). The stationary probability that \((F_1,F_2,F_3)\) has any specified composition \((3,0,0)\) up to permutation is \(46/405\), of any specified composition \((2,1,0)\) is \(13/135\), and of \((1,1,1)\) is \(11/135\): these are not equal, in contrast with the uniform finite composition law on the complete graph with one zealot per opinion.

## Assumptions and scope
The graph has \(r\) parts of size \(n\) (\(rn\) vertices). An edge joins exactly two vertices in different parts. There is exactly one non-updating, opinion-\(j\) zealot in each part \(j\); all other \(r(n-1)\) vertices update asynchronously with independent rate-one clocks. A neighbor is sampled uniformly over all \((r-1)n\) outside-part vertices, including other zealots. Opinions are exactly \(1,\ldots,r\). No spontaneous mutation, within-part copy, intrinsic conformity, or extra zealots are allowed. Limits hold with fixed \(r\) and \(n\to\infty\), not uniformly for growing \(r\). Stationary statements concern the unique stationary distribution of the full labelled finite continuous-time chain.

## Proof
**1. Uniqueness.** Consider the labelled configuration in which every flexible vertex in part \(j\) has opinion \(j+1\) cyclically, while the zealots keep their fixed opinions. From any configuration one may reach it by successively having each flexible vertex in part \(j\) copy the permanently fixed zealot in part \(j+1\). Every specified update has positive rate because these vertices lie in different parts, regardless of the other flexible vertices' opinions. Hence one state is accessible from every configuration. Every finite Markov chain with such an accessible state has exactly one closed communicating class and therefore one stationary probability law; transient states do not matter. The update rule is invariant under simultaneous permutations of part labels and opinion labels.

**2. Exact generator identities.** For a test function \(f\), write \(\mathcal L f\) for the sum of its changes weighted by actual jump rates. Set \(P_a=r^{-1}\sum_j X_{j,a}\) and \(Q_{j,a}=(rP_a-X_{j,a})/(r-1)\), the opinion-\(a\) fraction among all potential neighbors of part \(j\). The old opinion among all \(n\) vertices of part \(j\) has frequency \(X_{j,a}\), but only its \(n-1\) flexible vertices change. Direct counting, with \(\delta_{ja}\) denoting the Kronecker delta, gives the **pointwise**, not just stationary, identities
\[
\mathcal L X_{j,a}=\frac{n-1}{n}Q_{j,a}-X_{j,a}+\frac{\delta_{ja}}n
=-\frac r{r-1}(X_{j,a}-P_a)+\frac{\delta_{ja}-Q_{j,a}}n,
\qquad
\mathcal L P_a=\frac{1-rP_a}{rn}.
\tag{1}
\]
Simultaneous permutation symmetry of the unique stationary distribution makes \(\mathbb E P_a=1/r\). Stationarity of \(X_{j,a}\) in (1) and \(\sum_j\mathbb E X_{j,a}=1\) give
\[
0=\frac{n-1}{n(r-1)}(1-\mathbb E X_{j,a})-\mathbb E X_{j,a}+\frac{\delta_{ja}}n.
\]
Solving gives exactly the finite means stated above (and all denominators are positive for \(r,n\) in scope).

**3. Synchronization in stationary mean square.** Define \(Y_{j,a}=X_{j,a}-P_a\), and \(V=\sum_{j,a}Y_{j,a}^2\). Subtracting the identities in (1) yields
\[
\mathcal L Y_{j,a}=-\frac r{r-1}Y_{j,a}+R_{j,a},
\quad
R_{j,a}=\frac{\delta_{ja}-Q_{j,a}}n-\frac{1-rP_a}{rn}.
\]
Since all displayed fractions are in \([0,1]\), \(|R_{j,a}|\le2/n\). Each flexible update changes any \(Y_{j,a}\) by at most \(2/n\), and the sum of all flexible update rates is at most \(r(n-1)\). Therefore, for each coordinate, its jump carré du champ obeys \(\mathcal L(Y_{j,a}^2)-2Y_{j,a}\mathcal L Y_{j,a}\le4r/n\). The exact product rule gives
\[
\mathcal L V\le-\frac{2r}{r-1}V+
\frac4n\sum_{j,a}|Y_{j,a}|+\frac{4r^3}{n}.
\]
Every \(|Y_{j,a}|\le1\), so the error on the right is bounded by a constant \(C_r/n\), uniformly in all configurations. Stationarity then implies \(\mathbb E V\le C'_r/n\). Thus, for fixed \(r\), every part's entire opinion vector differs from the global vector by \(o_{L^2}(1)\).

**4. Limiting generator and its covariance normalization.** Let \(f\) be a polynomial on the simplex and define \(\partial_a=\partial/\partial p_a\), using any polynomial extension to a neighborhood. A flexible update in part \(j\) changes the global opinion vector by \((e_b-e_c)/(rn)\) when old opinion \(c\) is replaced by sampled opinion \(b\). Its total rate is bounded by \(rn\). The exact drift from (1), multiplied by \(rn\), is \(1-rP_a\). On the same accelerated scale the jump quadratic covariation satisfies
\[
rn\sum_{\mathrm{jumps}}\!\mathrm{rate}\,(\Delta P_a)(\Delta P_b)
\ \xrightarrow{L^1}\ 2(P_a\delta_{ab}-P_aP_b),
\tag{2}
\]
where the right side is evaluated at the current global opinion vector, and \(L^1\) refers to the stationary law. To justify (2) without an independence assumption, condition on the current configuration: the old-opinion empirical law among free sites of part \(j\) is \((nX_{j,\cdot}-e_j)/(n-1)\), and the sampled outside-part law is \(Q_{j,\cdot}\). The conditional expectation of \((e_b-e_c)^{\otimes2}\) is the sum of their respective diagonal covariance terms and the two cross terms. These are bounded polynomials of these two empirical laws. By Step 3 both laws differ from \(P\) in stationary \(L^1\) by \(o(1)\), uniformly across the finitely many parts. The usual independent-draw expression at identical law \(P\) is \(2(\operatorname{diag}P-PP^\mathsf T)\). Each fixed part carries \(n-1\) update clocks, which makes the normalizing factor converge to one. This proves (2). Taylor's third-order remainder after multiplication by \(rn\) is bounded by \(O_{f,r}(n^{-1})\), since jump size is at most \(2/(rn)\). Consequently,
\[
rn\mathcal L f(P)-\mathcal Gf(P)\xrightarrow{L^1}0,\qquad
\mathcal Gf(p)=\sum_a(1-rp_a)\partial_a f(p)
+\sum_{a,b}p_a(\delta_{ab}-p_b)\partial_{ab}f(p).
\tag{3}
\]
The factor of two in (2) cancels the one-half in the second-order Taylor term; the coefficient in (3) is thus exactly one, not one-half.

**5. Moment identification and convergence.** Because the global vector is supported on the compact simplex, each subsequence has a further weakly convergent stationary subsequence. Let \(\mu\) denote any such limit. Stationarity of \(f(P)\), boundedness, and (3) imply \(\int\mathcal Gf\,d\mu=0\) for every polynomial \(f\). For \(f(p)=\prod_a p_a^{k_a}\) with \(K=\sum k_a\ge1\), expand each derivative in (3) to obtain
\[
K(K+r-1)m_k=\sum_{a=1}^r k_a^2m_{k-e_a},\qquad
m_k=\int\prod_a p_a^{k_a}\,\mu(dp),
\tag{4}
\]
where terms with \(k_a=0\) are omitted and \(m_0=1\). The coefficient on the left is strictly positive. The recursion determines **all** moments by induction on \(K\), and its unique solution is
\[
m_k=\frac{(r-1)!\prod_a k_a!}{(K+r-1)!}.
\]
These are exactly the moments of uniform measure on the simplex, or \(\operatorname{Dirichlet}(1,\ldots,1)\). Polynomials are dense in continuous functions on the compact simplex, so the moments determine the probability measure. Every subsequence has the same weak limit; hence the full stationary global vectors converge, and Step 3 plus Slutsky gives joint convergence of all part vectors. This is an infinite-family proof, not an extrapolation from finite calculations.

**6. Exact finite obstruction.** When \(r=3,n=2\), there are only three flexible vertices and 27 labelled configurations. In lexicographic order of their opinions \(0,1,2\) (an equivalent zero-based encoding), the exact nonnegative integer stationary weights in `FINITE_CERTIFICATE.json` sum to 8100. Multiplying these weights by the actual \(27\)-state generator gives zero in every column. Their aggregates over total flexible opinion counts are exactly the three values stated in the Finding, with respective multiplicities three, six, and one. This is a finite result supported by a complete exact certificate, not an assumption about the limiting law.

## Verification
Run `python verify.py` from the directory containing `verify.py` and `FINITE_CERTIFICATE.json` using Python 3 standard libraries only. It exhaustively constructs every labelled state and actual off-diagonal transition for \((r,n)=(3,2),(3,3),(4,2)\), totaling 1012 configurations, and checks the two identities in (1) exactly with rational arithmetic for all parts and opinions. It separately checks all 27 stationary balance equations using the embedded 8100-normalized integer certificate, derives the three composition probabilities, and checks the exact means. The successful output is `MULTIPARTITE_VOTER_EXACT_CHECKS_PASSED 1012 local configurations and 27 state stationarity balances`. These finite computations corroborate the derivation; Steps 3–5 are the proof for arbitrary \(n\).

## Relationship to prior work
Palombi and Toti (arXiv:1309.0396, September 2013) study multi-opinion copying with candidates on networks constructed from cliques with within-part interactions and randomly linked communities. Their model and limiting degree regime differ: in the present graph **every within-part edge is absent**, but every cross-part edge is present, and each zealot occupies a distinct part. Their calculations do not directly give the uniform Dirichlet conclusion for this graph.

Ramírez, San Miguel, and Galla (arXiv:2207.05465, 2022) derive the exact flat finite composition distribution for a complete, well-mixed network with one zealot per opinion and discuss more general graphs. Their complete-graph identity does not apply to a complete multipartite graph lacking whole classes of edges; Step 6 supplies a concrete nonflat counterexample while Steps 3–5 prove an asymptotically flat limit. The special well-mixed Dirichlet mechanism is **prior work**, not claimed new.

Khalil and Galla (arXiv:2007.07535, 2020) treat multiple opinion states with intrinsic noise on complete interaction graphs, which differs in both graph topology and mutation mechanism. Related published research results on two-opinion complete-bipartite zealot copying and a conditional rare-coexistence Dirichlet law for an opinion-compatibility star have been compared at the level of hypotheses and conclusions: the former has only two parties/opinions and a one-dimensional Beta limit, while the latter has no frozen vertex and studies an absorbing event on a different communication network. Neither implies the present \(r\ge3\) stationary simplex theorem. Standard generator, carré-du-champ and polynomial moment methods are not claimed novel.

## Limitations
No assertion of exact finite Dirichlet-multinomial stationarity: already \(r=3,n=2\) disproves it. The theorem assumes equal part sizes, fixed \(r\), one zealot per part with matching opinion, uniform cross-part copying, and no mutation; it does not establish the same limit for unequal part sizes, general dense regular graphs, growing \(r\), synchronous updates, transient mixing times, or trajectories at a fixed nonstationary time. Independent scientific review has not been performed. Historical originality is assessed only against accessible primary material and targeted public-record searches; a more general result elsewhere may imply the theorem.

## References
1. F. Palombi and S. Toti, *Stochastic Dynamics of the Multi-State Voter Model over a Network based on Interacting Cliques and Zealot Candidates*, arXiv:1309.0396v1, first public 2 September 2013. https://arxiv.org/abs/1309.0396
2. L. S. Ramírez, M. San Miguel and T. Galla, *Local and global ordering dynamics in multi-state voter models*, arXiv:2207.05465, 2022. https://arxiv.org/abs/2207.05465
3. N. Khalil and T. Galla, *Zealots in multi-state noisy voter models*, arXiv:2007.07535, 2020. https://arxiv.org/abs/2007.07535
4. D. Braha and M. A. M. de Aguiar, *A voter-model representation of the multi-allelic Moran process: Exact stationary distributions and diversity thresholds from well-mixed populations to complex networks*, Journal of Theoretical Biology, 2026, https://doi.org/10.1016/j.jtbi.2026.112517
