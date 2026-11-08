# Four price phases in worst-pair resistance design on matching-priced \(K_{m,m}\)

## Finding

Fix an integer \(m\ge3\), a total budget \(B>0\), and a matching-edge price \(P>0\). Label the two parts of \(K_{m,m}\) by \(u_1,\ldots,u_m\) and \(v_1,\ldots,v_m\). Each matching edge \(u_i v_i\) costs \(P\) per unit conductance, and each other edge costs one. Optimize all nonnegative edge conductances independently, subject to connected positive support and total cost at most \(B\), to minimize the largest pairwise effective resistance (the resistance diameter).

Put
\[
\gamma=\frac{\sqrt{m(m-2)}-(m-2)}2,\quad
P_1=\frac{m-1}{m-2},\quad
P_2=\frac{m-1+\gamma^2}{(m-2)/2+\gamma^2},\quad
P_3=\frac{4m^2-11m+8}{(m-2)(2m-3)}.
\]
Then \(0<P_1<P_2<P_3\). Define \(t_*(P)\) by the four branches
\[
t_*(P)=
\begin{cases}
\frac12\left[\sqrt{\frac{m[2(m-1)-P(m-2)]}{P}}-(m-2)\right],&0<P\le P_1,\\[3pt]
\gamma,&P_1\le P\le P_2,\\[3pt]
\displaystyle\frac{(m-1)\sqrt{m-1-P(m-2)/2}-\frac{m-2}{2}\sqrt{P-1}}{\sqrt{P-1}-\sqrt{m-1-P(m-2)/2}},&P_2\le P\le P_3,\\[8pt]
0,&P\ge P_3.
\end{cases}
\]
At common endpoints these expressions agree. An optimal conductance allocation assigns
\[
y_* =\frac{B}{m[Pt_*(P)+m-1]}
\quad\text{to every nonmatching edge},\qquad
x_*=t_*(P)y_*
\quad\text{to every matching edge}.
\]
Among allocations invariant under simultaneous permutation of matched vertex pairs and interchange of the two parts, this optimizer is unique. The unrestricted global optimum has the same value, namely
\[
D_* = \frac{m}{B}[Pt_*+m-1]\max\!\left\{
\frac1m+\frac1{2t_*+m-2},\quad
\frac{2(m-1)}{m(2t_*+m-2)}+\frac1{m(t_*+m-1)}
\right\}.
\]
The worst pair is within one bipartition part for \(0<P<P_1\), both a same-part pair and a matched pair for \(P_1\le P\le P_2\), and a matched pair for \(P_2<P\). In the invariant optimum, all expensive matching edges disappear exactly for \(P\ge P_3\). The narrow positive-matching transition has width
\[
P_3-P_2=\frac1{2m^2}+O(m^{-3})\qquad(m\to\infty).
\]

## Assumptions and scope

An edge's conductance \(w\ge0\) contributes \(w(e_u-e_v)(e_u-e_v)^\mathsf T\) to the symmetric graph Laplacian \(L\). For a connected positive-support graph, resistance is \(R_{ij}=(e_i-e_j)^\mathsf T L^\dagger(e_i-e_j)\). The objective is \(\max_{i\ne j}R_{ij}\). Costs are linear in conductance. There are no fixed positive lower bounds on edges; zero matching-edge weight is allowed, since the remaining graph is connected for \(m\ge3\). This theorem gives one explicit unrestricted optimum and uniqueness only *within the invariant class*; it does not classify every potentially asymmetric optimal allocation.

## Proof

**1. Global symmetry reduction.** For fixed pair \(i,j\), the variational identity
\[
R_{ij}(w)=\sup_{v\perp\mathbf1}\left(2(e_i-e_j)^\mathsf T v-v^\mathsf T L(w)v\right)
\]
shows convexity in the edge conductances, including connected boundary designs. The maximum of these convex functions is convex. Averaging any feasible design over simultaneous permutations of matched index pairs and the exchange \(u_i\leftrightarrow v_i\) preserves its price budget, and cannot increase its resistance diameter. Its positive-support union remains connected. Positive scaling decreases every resistance, so any optimum spends the full budget. Therefore an unrestricted optimum exists among two-orbit designs with matching conductance \(x\ge0\) and nonmatching conductance \(y>0\), satisfying \(mPx+m(m-1)y=B\).

**2. Exact pair resistances.** Set \(d=x+(m-1)y\) and \(z=2x+(m-2)y\). The Laplacian is
\[
L=\begin{pmatrix}dI&-[(x-y)I+yJ]\\-[(x-y)I+yJ]&dI\end{pmatrix}.
\]
Its positive eigenvalues are \(my\) and \(z\), each with multiplicity \(m-1\), and \(2d\) with multiplicity one. Orthogonal decomposition of the three vertex-pair types gives
\[
R_{\rm same}=\frac1{my}+\frac1z,\qquad
R_{\rm match}=\frac{2(m-1)}{mz}+\frac1{md},
\]
\[
R_{\rm nonmatch}=\frac1{my}+\frac{m-2}{mz}+\frac1{md}.
\]
Here \(R_{\rm same}\) is a pair of distinct vertices in the same part, \(R_{\rm match}\) is \(u_i,v_i\), and \(R_{\rm nonmatch}\) is \(u_i,v_j\) with \(i\ne j\). Since
\[
R_{\rm same}-R_{\rm nonmatch}=\frac{y}{zd}>0,
\]
the maximum is determined by only the first two types.

**3. Unique pair-type crossing.** Put \(t=x/y\ge0\), so \(y=B/[m(Pt+m-1)]\). The difference between the unscaled same-part and matched resistances has numerator
\[
2t^2+2(m-2)t-(m-2).
\]
It has exactly one nonnegative root \(\gamma\), and changes from negative to positive there. Consequently, for \(t\le\gamma\), matched pairs govern, whereas for \(t\ge\gamma\), same-part pairs govern. The diameter, divided by \(m/B\), equals \(\Phi_M(t)\) on \([0,\gamma]\) and \(\Phi_S(t)\) on \([\gamma,\infty)\), with
\[
\Phi_S(t)=(Pt+m-1)\left(\frac1m+\frac1{2t+m-2}\right),
\]
\[
\Phi_M(t)=(Pt+m-1)\left(\frac{2(m-1)}{m(2t+m-2)}+\frac1{m(t+m-1)}\right).
\]

**4. Exact four-phase minimization.** Differentiation yields
\[
\Phi_S'(t)=\frac Pm+\frac{P(m-2)-2(m-1)}{(2t+m-2)^2},
\]
\[
\Phi_M'(t)=\frac{m-1}{m}\left[\frac{P(m-2)/2-(m-1)}{(t+(m-2)/2)^2}+\frac{P-1}{(t+m-1)^2}\right].
\]
The first derivative vanishes at the stated \(t_*\) on the same-part branch exactly when \(P\le P_1\); at \(\gamma\), it has the sign of \(P-P_1\). The second displayed first-derivative expression has at most one zero with a negative-to-positive sign change, because the ratio \((t+m-1)/(t+(m-2)/2)\) decreases strictly in \(t\). Its derivative vanishes at \(\gamma\) precisely for \(P=P_2\), and at zero precisely for \(P=P_3\). Solving \(\Phi_M'(t)=0\) gives the stated square-root expression on \(P_2<P<P_3\).

For completeness, the price thresholds are strictly ordered: at \(P=P_1\), \(\Phi_S'(\gamma)=0\), whereas \(\Phi_M'(\gamma)<0\), since the difference \(\Phi_S-\Phi_M\) has strictly positive derivative at its crossing; hence \(P_2>P_1\). At \(P=P_3\), \(\Phi_M'(0)=0\), and \(P_3=2(m-1)/(m-2)-1/(2m-3)\) implies \(\Phi_M'(t)>0\) for \(t>0\); hence \(P_3>P_2\). The two branch minima and their common crossing establish every case, with no other local or global minimizers inside the invariant class.

**5. Structural comparison and asymptotics.** For the same invariant designs, the Laplacian spectral gap equals \(\min\{my,z\}\). Under the same budget its optimizer changes from \(t=1\) to \(t=0\) only at \(P_{\rm gap}=2(m-1)/(m-2)\). Therefore \(P_{\rm gap}-P_3=1/(2m-3)\): throughout \(P_3<P<P_{\rm gap}\), optimizing worst-pair resistance eliminates the matching even though a spectral-gap-optimal invariant design retains it. Finally, binomial expansion of \(\sqrt{m(m-2)}\) gives the asserted \(m^{-2}\) width; this follows from exact radical formulas, not from finite numerical fitting.

## Verification

The accompanying standalone `verify.py` independently constructs and inverts grounded graph Laplacians over the rational numbers for \(3\le m\le6\), with varied zero and positive matching weights. It checks all three shell formulas directly and tests the four-phase optimum against independent scalar numerical minimization and competitor values, with derivative identities checked symbolically. Execute `python verify.py` with Python, SymPy and SciPy. A successful run reports 144 exact grounded-Laplacian shell checks, 108 optimization/phase checks, and three symbolic derivative identities. These finite checks supplement, but do not replace, the all-parameter proof above.

## Relationship to prior work

Ghosh, Boyd and Saberi's 2006 conference paper established convexity of effective-resistance allocation and explicitly proposed *minimizing the maximum effective resistance* as a general semidefinite program (section VII). Its 2008 full version retained that extension (section 8). These papers supply the foundational setup, but do not state the matching-priced bipartite four-phase formula, its pair-type crossover, or its \(m^{-2}\) transition window. Classical unweighted complete-bipartite resistance formulas address the uniform graph rather than this independently priced network design. Optimization of algebraic connectivity and optimization of total effective resistance are different functionals and neither determines the worst-pair optimum here. A previously studied matching-priced complete graph is not equivalent to the present bipartite domain, since its same-part edges are available while here they are prohibited.

## Limitations

The result concerns finite balanced complete bipartite networks with one distinguished matching and positive linear prices; it does not cover arbitrary bipartite graphs, nonlinear conductance costs, directed circuits, or an all-optimizer classification beyond the invariant class. Global attainment follows from convexity and symmetry; the theorem does not assert that *every* unrestricted optimizer has the displayed support. The first dated conference version is associated with July 24–28, 2006; an earlier public manuscript date has not been independently established. Priority relative to specialist literature not found in the searches remains subject to independent expert assessment.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, July 24–28, 2006, pp. 1185–1196. https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
2. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, https://doi.org/10.1137/050645452 (published online February 1, 2008).
3. S. Gervacio, *Resistance distance in complete n-partite graphs*, The Mindanawan Journal of Mathematics 3 (2012), 1–19. https://journals.msuiit.edu.ph/tmjm/article/view/26
