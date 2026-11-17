# Almost-independent phase defects and vanishing immediate excitation waves on Boolean cubes

## Finding

Let \(Q_d\) be the \(d\)-dimensional Boolean cube, \(d\ge1\), with independent uniformly random initial colors in \(\{0,1,2\}\). Under synchronous threshold-one, three-state Greenberg–Hastings updating, let \(X_d\) be the number of vertices that **lack** a neighbor in the next cyclic color. Write
\[
N=2^d,\qquad p=(2/3)^d,\qquad \mu=Np=(4/3)^d,
\]
and \(M_d=1+d+\binom d2\), \(B_d=1+\tfrac74d+\tfrac{17}{8}\binom d2\). Then:

1. The initial configuration lies on a primitive temporal three-cycle if and only if \(X_d=0\). In particular its probability tends to zero, even though the probability of a phase defect at any *specified* vertex tends to zero.
2. The exact first two moments are
\[
\mathbb E X_d=\mu,\qquad
\operatorname{Var}(X_d)=\mu+\frac{Np^2}{16}(d^2-5d-16).
\]
3. The variance is strictly *below* the Poisson reference mean for \(1\le d\le7\), and strictly *above* it for every \(d\ge8\), exhibiting an exact dimension-eight fluctuation crossover. For all \(d\ge1\), using the usual supremum-over-events total-variation distance,
\[
d_{\mathrm{TV}}\!\left(\mathcal L(X_d),\operatorname{Poisson}(\mu)\right)
\le p B_d(1-e^{-\mu})\le pB_d.
\]
More strongly, if \(Y=(Y_v)_{v\in Q_d}\) records all defect locations and \(Y'\) is a vector of **independent** Bernoulli\((p)\) indicators on the same vertex set, then
\[
d_{\mathrm{TV}}\!\left(\mathcal L(Y),\mathcal L(Y')\right)
\le 2Np^2(B_d+1)=2(8/9)^d(B_d+1)\longrightarrow0.
\]
4. For the event of an immediate primitive temporal three-cycle,
\[
\Pr(X_d=0)\le(1-p)^{\lceil N/M_d\rceil}
\le\exp\!\left[-\frac{(4/3)^d}{M_d}\right]\longrightarrow0.
\]
Thus the **complete random spatial pattern of defects** becomes asymptotically indistinguishable in total variation from independent site defects, despite a growing mean number of defects and nonzero short-distance correlations. The last bound controls the unusually rare all-defect-free event without attempting to extract a relative approximation from total variation.

## Assumptions and scope

The vertices of \(Q_d\) are length-\(d\) binary words. An edge joins words differing in exactly one coordinate; all vertices are labelled. The update map \(F\) replaces color \(1\) by \(2\), color \(2\) by \(0\), and color \(0\) by \(1\) precisely when an adjacent vertex currently has color \(1\); otherwise color \(0\) remains \(0\). Updates are simultaneous. The initial colors \((C_v)\) are independent and uniform on \(\{0,1,2\}\), independent of no other randomness (the graph is fixed).

A configuration has primitive temporal period three if \(F^3(C)=C\), while \(F(C)\ne C\). For each vertex, define
\[
Y_v={\bf1}\{\text{no neighbor of }v\text{ has color }C_v+1\pmod3\},
\qquad X_d=\sum_vY_v.
\]
Here \(d_{\mathrm{TV}}(P,Q)=\sup_A|P(A)-Q(A)|\). The Poisson approximation concerns a distribution whose parameter \(\mu=(4/3)^d\) itself diverges; it does not assert convergence to a fixed Poisson distribution.

## Proof

**A. Three-period recurrence criterion.** If \(F^3(C)=C\), a site visiting color \(1\) traverses \(1,2,0\) and must return to \(1\) at the next update; a site visiting color \(2\) similarly rotates. A site that starts in color \(0\) either remains zero throughout or rotates through all three colors. Therefore every vertex is either constantly zero or rotates through \(0,1,2\). If a constantly zero vertex is adjacent to a rotating one, it has an excited neighbor at one of the three update times and cannot remain zero. Since \(Q_d\) is connected, the only nonrotating three-periodic state is the all-zero fixed point. A rotating configuration has the required transition at every vertex exactly when each vertex sees a successor-colored neighbor at time zero; the same contact condition persists under uniform cyclic advancement of colors. Consequently a primitive period-three state is equivalent to \(Y_v=0\) for every vertex.

**B. Single and joint defect probabilities.** Given \(C_v\), its \(d\) neighbors have independent colors, each avoiding the forbidden successor with probability \(2/3\). Thus \(\Pr(Y_v=1)=p\). The joint defect probability depends only on Hamming distance \(r\) between \(v,w\):
\[
\Pr(Y_v=Y_w=1)=
\begin{cases}
\frac34p^2,&r=1,\\
\frac98p^2,&r=2,\\
p^2,&r\ge3.
\end{cases}
\]
At distance one, adjacent centers must carry the same color (probability \(1/3\)); otherwise at least one center supplies the other's prohibited successor. The remaining \(2d-2\) neighbors are distinct, giving \(\frac13(2/3)^{2d-2}=\frac34p^2\). At distance two, centers share exactly two neighbors. With equal center colors (probability \(1/3\)), each shared neighbor avoids one forbidden color; with different center colors (probability \(2/3\)), each avoids two forbidden colors. The other \(2d-4\) neighbor colors are independent, so
\[
\Pr(Y_v=Y_w=1)=(2/3)^{2d-4}
\left[\frac13(2/3)^2+\frac23(1/3)^2\right]=\frac98p^2.
\]
For distance at least three, the two closed one-neighborhoods are disjoint, so the events are independent. Each vertex has \(d\) neighbors at distance one and \(\binom d2\) at distance two. Expanding the variance by ordered vertex pairs yields
\[
\operatorname{Var}(X_d)=Np(1-p)+Np^2\left[-\tfrac14d+\tfrac18\binom d2\right]
=\mu+\tfrac{Np^2}{16}(d^2-5d-16).
\]

**C. Full-process decoupling.** Let the dependency neighborhood for \(Y_v\) be all vertices at Hamming distance at most two from \(v\). Its size is \(M_d\). The corresponding Arratia–Goldstein–Gordon (1989) quantities are, exactly,
\[
b_1=N M_dp^2,\qquad
b_2=Np^2\left(\frac34d+\frac98\binom d2\right),\qquad b_3=0,
\]
so \(b_1+b_2=Np^2B_d\). The equality \(b_3=0\) follows from independence of the entire disjoint family of initial colors outside the closed two-neighborhood. Their Theorem 1, after dividing their norm by two to match our convention, gives the stated Poisson total-variation bound. Their Theorem 3 similarly gives the independent-indicator vector bound
\[
d_{\mathrm{TV}}\le 2(b_1+b_2)+2Np^2
=2Np^2(B_d+1).
\]
Since \(Np^2=(8/9)^d\) and \(B_d\) is quadratic in \(d\), this bound tends to zero. The mean itself tends to infinity, so this is a growing-intensity, full-pattern decoupling statement.

**D. Impossibility of a typical immediate three-cycle.** Greedy selection of disjoint closed neighborhoods in \(Q_d\) produces a set \(S\) of at least \(\lceil N/M_d\rceil\) vertices at mutual distances at least three: each selected vertex removes at most \(M_d\) candidates. The indicators \((Y_v)_{v\in S}\) depend on disjoint families of independent initial colors, and hence are mutually independent. The event \(X_d=0\) implies \(Y_v=0\) for all \(v\in S\). This proves
\[
\Pr(X_d=0)\le (1-p)^{|S|}\le(1-p)^{\lceil N/M_d\rceil}
\le e^{-Np/M_d}.
\]
Finally \((4/3)^d/M_d\to\infty\), proving the final claim. These bounds hold at all \(d\ge1\); asymptotic conclusions require \(d\to\infty\).

## Verification

The standalone Python-standard-library checker `tools/defect_check.py` exhaustively enumerates the \(9\), \(81\), and \(6561\) initial configurations for \(d=1,2,3\). Independently of the local defect criterion, it updates every configuration three times and checks exact equivalence to initial least temporal period three. It also verifies the exact expectation, variance, and all available distance-one/two pair probabilities using rational arithmetic. The \(d=3\) enumeration finds \(252\) primitive-period-three configurations, or \(84\) orbits, agreeing with the separately published finite-cube census. The captured program output is `data/defect_check_output.txt`.

Reproduce with `python3 tools/defect_check.py`. The checker also evaluates the exact formulas for the approximation prefactors and the packing bound at a set of larger dimensions; those numerical evaluations are diagnostics only, not proofs of the all-dimensional statements. The all-dimensional proof is the explicit neighborhood calculation and the cited dependency-graph theorem.

## Relationship to prior work

The Greenberg–Hastings excitation rule originates with Greenberg and Hastings (1978), while Durrett and Steif (1991) establish general probabilistic behavior on lattice systems and finite periodic boxes. Gravner, Lyu and Sivakoff (2016) study long-time activity and excitation on arbitrary graphs, including random graphs, rather than the present initial defect-location law on fixed, growing-dimensional Boolean cubes.

A published analysis, *A rarest-color Poisson threshold for immediate three-cycles in random excitable networks* (2026), gives a Poisson window for the initial three-cycle event on **random-edge Erdős–Rényi graphs**, where the expected number of defects approaches a constant. The new statement here is for a **fixed hypercube**, where defect probabilities, pair correlations, spatial dependence, and the exponentially increasing mean are different; its full-vector decoupling and exact moment formula do not follow from that random-edge result.

The powerful, general Chen–Stein bounds (Arratia, Goldstein and Gordon, 1989) are not claimed as new. Indeed, their Example 1 already treats rare edge-orientation events on hypercubes, a distinct stochastic field. The contribution here is the all-dimensional calculation of the *color-induced excitation defects* (including opposite-sign correlations at distances one and two), the sharp form of its total variation consequences, and the dynamical conclusion that immediate global three-cycles are atypical.

## Limitations

The claim concerns **periodic behavior starting at time zero**, not eventual-period statistics or absorption basins. The exponential upper bound for the probability of no defects does not give a matching lower bound or an exact logarithmic asymptotic; total-variation convergence by itself is too coarse for a relative asymptotic of such a rare event. Dimensions one through three are exhaustively checked, but the infinite-family statements rely on their proofs and the correctly normalized published Chen–Stein inequalities. A fully independent mathematical audit has not been performed, and unindexed equivalent treatments of this special random coloring remain a historical-priority risk. An older founding article has a verified May 1978 publication month but no verified exact public day; bibliographic dates are not used as mathematical evidence.

## References

1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics **34** (1978), 515–523. DOI `10.1137/0134040` (published May 1978; exact day unverified).
2. R. Durrett and J. E. Steif, *Some Rigorous Results for the Greenberg–Hastings Model*, Journal of Theoretical Probability **4** (1991), 669–690. DOI `10.1007/BF01259549` (publication dated October 1, 1991).
3. R. Arratia, L. Goldstein and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, Annals of Probability **17** (1989), 9–25. https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/AGG-1.pdf. Theorems 1 and 3, pages 11–12.
4. J. Gravner, H. Lyu and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, arXiv:1610.07320v1, publicly posted October 24, 2016. https://arxiv.org/abs/1610.07320.
5. *Primitive excitation periods on the four-cube: an exact finite-state census* (2026), publicly available scientific result: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-primitive-excitation-periods-on-the-four-cube-an-exact-finite-st--d99b448f2f7e.
6. *A rarest-color Poisson threshold for immediate three-cycles in random excitable networks* (2026), publicly available scientific result: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-rarest-color-poisson-threshold-for-immediate-three-cycles-in-r--1d35b531b603.
