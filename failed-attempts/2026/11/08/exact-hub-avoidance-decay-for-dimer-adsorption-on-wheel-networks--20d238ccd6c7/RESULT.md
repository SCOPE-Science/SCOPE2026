# Exact hub-avoidance decay for dimer adsorption on wheel networks

## Finding

For each integer \(m\ge2\), let \(W_{2m}=K_1\vee C_{2m}\) be the wheel with a central hub and \(2m\) rim vertices. Each edge has an independent unit-rate exponential first-attempt clock; its dimer is deposited if both endpoints are vacant, and occupied vertices stay unavailable. The eventual hub-vacancy probability \(P_{2m}\) has the exact representation
\[
P_{2m}=2\int_{[0,\infty)^m}\exp\!\left(-3\sum_{j=1}^m t_j-\sum_{j=1}^m\min(t_j,t_{j+1})\right)\,dt_1\cdots dt_m,
\qquad t_{m+1}=t_1.
\]
Equivalently, define the self-adjoint integral operator \(K\) on \(L^2(0,\infty)\) by
\[
(Kf)(t)=\int_0^\infty \exp\!\left[-\frac32(t+s)-\min(t,s)\right]f(s)\,ds.
\]
Then \(K\) is trace-class, has one simple strictly positive eigenvalue \(\lambda_*\), and every other eigenvalue has modulus strictly smaller than \(\lambda_*\). In particular,
\[
P_{2m}=2\operatorname{tr}(K^m),\qquad
P_{2m}=2\lambda_*^m\bigl(1+O(\vartheta^m)\bigr)
\quad\text{for some }0<\vartheta<1.
\]
The constant has a special-function characterization:
\[
\lambda_* =\frac{1}{4z_*^2}=0.287730645241419\ldots,
\qquad 2z_* I_{3/4}(z_*)=I_{-1/4}(z_*),
\qquad z_*=0.932130984806627\ldots,
\]
where \(I_\nu\) is the modified Bessel function and \(z_*\) is the unique positive root of the displayed equation. For a wheel with an odd number of rim vertices, the hub-vacancy probability is exactly zero. Thus the even-rim probability is a rare event with a precisely characterized exponential decay rate, whereas odd-rim hub avoidance is impossible.

## Assumptions and scope

The graph is the simple wheel obtained from the cycle on \(n\ge3\) distinct rim vertices by adding a hub joined to each rim vertex. The primary theorem concerns even \(n=2m\ge4\), with no edge weights or additional adsorption channels. Edge first-attempt clocks are independent with the same continuous distribution; exponential clocks of rate one are used for the integrals. Replacing them by any common continuous law leaves the final occupation distribution unchanged, because only the relative order matters. Repeated attempts after the first rejection cannot change outcomes, since occupied vertices never become vacant. Every edge contributes a single possible dimer and two vertices are covered on success. Probability is with respect to all independent edge arrival clocks.

## Proof

**1. The perfect-rim event.** At terminal time, an unoccupied hub cannot have a vacant rim neighbor, because the connecting spoke would then remain available. Therefore hub vacancy forces every rim vertex to be covered by successful rim dimers. An odd rim cannot be perfectly matched. The cycle \(C_{2m}\) has exactly two perfect matchings (the two alternating edge sets); their successful-deposition events are disjoint.

**2. Exact clock inequalities.** Fix one alternating perfect matching. Let \(E_j\) be the arrival clock of its \(j\)-th edge, \(F_j\) the intervening rim edge joining matching edges \(j\) and \(j+1\), and \(S_{j,1},S_{j,2}\) the two spokes at the endpoints of matching edge \(j\). That alternating matching is exactly the accepted final set if and only if
\[
S_{j,1}>E_j,\quad S_{j,2}>E_j,\quad
F_j>\min(E_j,E_{j+1})\qquad (1\le j\le m),
\]
with cyclic indices. Necessity follows because an earlier spoke would capture its free endpoint and an earlier intervening edge would capture both of its as-yet-free endpoints. For sufficiency, inspect the matching-edge arrivals in chronological order: every preceding nonmatching edge is already blocked by an earlier matching-edge arrival, and every spoke is later than its incident matching edge. Thus each matching edge succeeds. Conditional on \(E_j=t_j\), the independent spoke inequalities have probability \(\exp(-2\sum_jt_j)\), while the intervening-edge inequalities contribute \(\exp(-\sum_j\min(t_j,t_{j+1}))\). Multiplying by the matching-clock density \(\exp(-\sum_jt_j)\) and by the two alternating choices proves the displayed exact integral. For \(m=2\), the two distinct intervening rim edges both join the same pair of matching edges; the cyclic sum correctly counts both.

**3. Trace-class transfer operator.** Put \(w(t)=e^{-3t/2}\) and \(w_u(t)=w(t)\mathbf1_{\{t\ge u\}}\). The kernel identity
\[
e^{-\min(t,s)}=1-\int_0^\infty e^{-u}\mathbf1_{\{t\ge u\}}\mathbf1_{\{s\ge u\}}\,du
\]
gives the trace-norm decomposition
\[
K=w\otimes w-\int_0^\infty e^{-u}(w_u\otimes w_u)\,du.
\]
Indeed, \(\|w\|_2^2=1/3\) and \(\int_0^\infty e^{-u}\|w_u\|_2^2du=1/12\), so \(K\) is trace-class. The standard cyclic kernel formula for traces of products of Hilbert–Schmidt integral operators, first for bounded cutoffs and then by dominated convergence, gives exactly \(P_{2m}=2\operatorname{tr}(K^m)\) for \(m\ge2\).

**4. Simple dominant eigenvalue.** The kernel is strictly positive at every pair of nonnegative arguments. The compact self-adjoint operator therefore admits a positive top eigenvalue, with a strictly positive eigenfunction. The inequalities
\[
|\langle f,Kf\rangle|\le\langle |f|,K|f|\rangle\le\lambda_*\|f\|_2^2
\]
are strict in the first step whenever a real eigenfunction changes sign on sets of positive measure. This proves simplicity of the positive leading eigenvalue and rules out an eigenvalue of opposite sign with the same modulus. Alternatively, the rank-one-minus-positive decomposition proves there is at most one positive eigenvalue; positivity of \(\langle w,Kw\rangle\) guarantees its existence. Since the remaining eigenvalues are discrete and tend to zero, their moduli have a supremum strictly below \(\lambda_*\). The trace-class spectral expansion and a geometric remainder bound imply the claimed relative asymptotic.

**5. Bessel boundary problem.** Let \(f>0\) be the leading eigenfunction and set \(u(t)=e^{3t/2}f(t)\). The eigen-equation becomes
\[
\lambda_*u(t)=\int_0^\infty e^{-3s-\min(t,s)}u(s)\,ds.
\]
The right side makes \(u\) bounded. Differentiation yields
\[
\lambda_*u'(t)=-e^{-t}\int_t^\infty e^{-3s}u(s)\,ds,
\qquad u''(t)+u'(t)-\lambda_*^{-1}e^{-4t}u(t)=0.
\]
It follows that \(u'(0)=-u(0)\) and \(u'(t)=O(e^{-4t})\) as \(t\to\infty\). With \(z=e^{-2t}/(2\sqrt{\lambda_*})\), the differential equation has basis \(z^{1/4}I_{-1/4}(z)\), \(z^{1/4}I_{1/4}(z)\). The second solution has a nonzero \(e^{-t}\) derivative at infinity and is excluded. The identity
\[
\frac{d}{dz}\left[z^{1/4}I_{-1/4}(z)\right]=z^{1/4}I_{3/4}(z)
\]
turns the boundary condition at zero into \(2z_*I_{3/4}(z_*)=I_{-1/4}(z_*)\). Conversely, any positive root gives a bounded positive solution satisfying the integral eigen-equation, by integrating its differential identity and using the boundary condition. The simplicity and strict positivity of the leading eigenfunction imply that this positive root is unique. Hence \(\lambda_*=1/(4z_*^2)\) as claimed.

## Verification

The standalone Python file `verify_wheel.py` implements three independent finite-size checks: a recursion over uncovered rim subsets, direct integration over all chronological orders of the matching-edge clocks using exact rational arithmetic, and enumeration of all eight-edge arrival orders for the four-rim wheel. The first two approaches agree exactly for rim lengths \(4,6,8,10,12,14,16\), giving
\[
\begin{array}{c|rrrrrrr}
 n&4&6&8&10&12&14&16\\\hline
 P_n&1/6&1/21&19/1386&41/10395&523/460845&890/2725569&5323909/56664579510
\end{array}
\]
The checker also verifies odd-rim impossibility for \(n=5\), computes the Bessel constant using its convergent power series, and verifies its root equation numerically. Run with `python3 verify_wheel.py`; the successful terminal line is `ALL_CHECKS_PASS`. These finite checks are not relied upon as proof of the infinite-size asymptotic, which follows from the trace-class spectral argument.

## Relationship to prior work

Penrose and Sudbury (2005) provide the general finite-graph edge-clock definition of dimer random sequential adsorption, vacancy equations, and exact analysis for regular trees; the edge-clock process and its order invariance are prior machinery. Pippenger (1989) studies random sequential adsorption on graphs, including an edge-packing variant. Miller and Pritikin (1997) analyze the expected size and performance bounds for random greedy matchings, which share the same accepted-edge dynamics; Gamarnik and Goldberg (2009) develop regular-graph large-girth matching estimates. The present statement concerns a different observable: the rare event that the hub stays unoccupied on a specific family of high-degree wheels, its exact cyclic transfer trace, and the explicit Bessel-root exponential constant. The comparison does not claim the underlying RSA process, perfect-matching reduction, or generic edge-greedy equivalence to be novel.

## Limitations

The theorem gives the probability of hub vacancy under equal edge rates, not the full distribution of terminal matching size, finite-time occupancy, or effects of nonuniform edge rates. The decay constant is characterized implicitly, not by an elementary closed form. Its historical priority is provisional because the complete text of some older broad graph-adsorption and greedy-matching articles was not accessible for statement-by-statement comparison. No assertion of independent external validation is made.

## References

1. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, arXiv:math/0503519v1 (public 24 March 2005), https://arxiv.org/abs/math/0503519.
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401, https://doi.org/10.1137/0402034.
3. Z. Miller and D. Pritikin, *On randomized greedy matchings*, Random Structures & Algorithms 10 (1997), 353–383, https://doi.org/10.1002/(SICI)1098-2418(199705)10:3%3C353::AID-RSA5%3E3.0.CO;2-V.
4. D. Gamarnik and D. A. Goldberg, *Randomized Greedy Algorithms for Independent Sets and Matchings in Regular Graphs: Exact Results and Finite Girth Corrections*, Combin. Probab. Comput. 19 (2010), 61–81, https://dspace.mit.edu/entities/publication/36eae796-81ba-4fbd-980d-4455c69cd9f2.
