# Unique Kemeny-optimal quadrilateral-book walks and strict separation from fastest mixing

## Finding
For each integer \(m\ge 2\), let \(B_m=K_{1,m}\mathbin{\square}K_2\), the graph consisting of \(m\) quadrilaterals with a common central edge. Among **all** irreducible symmetric, nonnegative, row-stochastic transition matrices supported on its edges and vertex holding loops, there is exactly one minimizing the *zero-target* Kemeny spectral sum
\[
\mathcal K(P)=\sum_{j=2}^{2m+2}\frac{1}{1-\lambda_j(P)}.
\]
The minimizer is invariant under page permutations and interchange of the two layers. Write \(x\) for each of the \(2m\) central-to-peripheral spoke probabilities, \(y\) for the central hub-to-hub probability, and \(z\) for each of the \(m\) outer page-rung probabilities.

For \(m=2\), let \(\eta\in(0,1)\) be the unique real root of
\[
15\eta^3+31\eta^2+21\eta-3=0,
\qquad\eta=0.12026393921747289\ldots.
\]
The unique minimizer is
\[
(x,y,z)=\left(\frac{1-\eta}{2},\eta,\frac{1+\eta}{2}\right),
\]
with exact minimum \(\mathcal K_*=(9\eta^3+21\eta^2-181\eta-105)/[6(\eta-1)(\eta+3)(3\eta+1)]\).

For **every** \(m\ge3\), the unique minimizer is instead
\[
\boxed{(x,y,z)=\left(\frac1m,0,1-\frac1m\right)},
\qquad
\boxed{\mathcal K_*=
\frac{4m^5-4m^4+6m^3-m^2-2m+1}{2(m-1)(m+1)(2m-1)}}.
\]
For the Kemeny objective, the change at **three pages** is exact: the common edge is used at \(m=2\) but assigned zero probability for every \(m\ge3\), even though the remaining support stays connected. This bridge-deletion page-count boundary is **not by itself new**: a prior fastest-mixing result on the identical graph identifies the same deletion boundary for a different objective. All optimal holding probabilities vanish. In particular, because \(B_m\) is bipartite, the Kemeny-optimal chain is irreducible but periodic with period two; it need not converge to its stationary law from a point mass. If aperiodicity is additionally demanded, the same value is an infimum approached by adding arbitrarily small holding, but it is not attained within this stricter class.

The two objectives nevertheless have **strictly disjoint global optimizer sets for every \(m\ge2\)**. A prior exact fastest-mixing analysis gives optimal SLEM \(2-\sqrt2\) at \(m=2\) and \(1-1/m\) for every \(m\ge3\). By contrast, the Kemeny-optimal chain has \(\operatorname{SLEM}(P_*)=1\) at all sizes because every optimal vertex has zero holding and the connected graph is bipartite. For \(m\ge3\), the previously recorded symmetry-invariant SLEM-optimal peripheral-rung interval is \(1/[2(m-1)]\le z\le(m-1)/m-1/[2(m-1)]\), whereas the new Kemeny optimum uniquely uses \(z=(m-1)/m\). Thus the shared hub-rung deletion transition does not identify a shared optimal walk; the Kemeny criterion selects a periodic endpoint strictly beyond the mixing-optimal range.

For the maximum-degree benchmark, assigning \(x=y=z=1/(m+1)\),
\[
\mathcal K_{\mathrm{md}}(m)=\frac{8m^3+27m^2+16m+9}{6(m+3)},\qquad
\lim_{m\to\infty}\frac{\mathcal K_{\mathrm{md}}(m)}{\mathcal K_*(m)}=\frac43.
\]

## Assumptions and scope
The vertex set consists of central hubs \(h_0,h_1\) and \(a_i,b_i\) for \(1\le i\le m\). There are edges \(h_0a_i\), \(h_1b_i\), \(a_ib_i\), and \(h_0h_1\), and no other non-loop edges. Every supported off-diagonal transition is nonnegative; all rows sum to one; \(P=P^{\mathsf T}\). Zero transition probabilities on graph edges are permitted; all vertex loops are permitted. The matrix must be irreducible; aperiodicity is **not** assumed. The stationary distribution is uniform. Eigenvalues are ordered \(1=\lambda_1>\lambda_2\ge\cdots\ge\lambda_{2m+2}\ge-1\); the zero-target convention omits the constant recurrence term of one.

For a symmetric invariant walk the stochasticity constraints are precisely \(x>0\), \(y,z\ge0\), \(mx+y\le1\), and \(x+z\le1\), with irreducibility also required. The two holding probabilities are \(u=1-mx-y\) at each hub and \(v=1-x-z\) at each outer vertex. Every stated minimizer satisfies both equalities and is connected.

## Proof
**1. Symmetry and uniqueness globally.** Put \(N=2m+2\), \(J=\mathbf1\mathbf1^{\mathsf T}/N\), and \(L=I-P\). For any connected symmetric stochastic \(P\),
\[
\mathcal K(P)=\operatorname{tr}[(L+J)^{-1}]-1.
\]
The domain of connected admissible matrices is convex: averaging two positive connected supports preserves connectivity. On this domain, \(L+J\) is positive definite. For any nonzero symmetric perturbation \(H\) with \(H\mathbf1=0\), the second derivative of \(\operatorname{tr}[(L+tH+J)^{-1}]\) at any admissible point is
\[
2\operatorname{tr}\bigl[A^{-1}HA^{-1}HA^{-1}\bigr]>0,
\qquad A=L+tH+J.
\]
Indeed \(A^{-1/2}HA^{-1/2}\) has a nonzero square and \(A^{-1}\) is positive definite. Hence the objective is *strictly convex* on nontrivial edge-weight changes. Averaging over page permutations and layer interchange cannot worsen it and strictly improves it unless the weights are already invariant. Consequently any global minimizer must use the three orbit weights \(x,y,z\), and any minimizing invariant point is the unique global minimizer.

**2. Exact spectral reduction.** Split vectors into the symmetric and antisymmetric sectors under layer interchange. On the symmetric sector the weighted star Laplacian has nonzero eigenvalues \(x\), repeated \(m-1\), and \((m+1)x\). On the antisymmetric sector, \(x+2z\) occurs with multiplicity \(m-1\), and the remaining two eigenvalues are those of
\[
M=\begin{pmatrix}mx+2y&-\sqrt m\,x\\-\sqrt m\,x&x+2z\end{pmatrix}.
\]
Its determinant and trace are \(2mxz+2xy+4yz\) and \((m+1)x+2y+2z\), respectively. Summing inverse eigenvalues gives the exact formula
\[
\tag{1}
\mathcal K_m(x,y,z)=
\frac{m-1+1/(m+1)}x+
\frac{m-1}{x+2z}+
\frac{(m+1)x+2y+2z}{2mxz+2xy+4yz}.
\]
This expression remains valid at \(y=0\) when the walk is connected.

**3. The regime \(m\ge3\).** Use nonnegative coordinates \((u,v,y)\) with \(x=(1-u-y)/m\) and \(z=1-x-v\). At \((u,v,y)=(0,0,0)\), compute the following three partial derivatives of (1), holding the other coordinates fixed:
\[
\begin{aligned}
\partial_u\mathcal K_m&=\frac{U(m)}{2(m-1)^2(m+1)(2m-1)^2},\\
\partial_v\mathcal K_m&=\frac{mV(m)}{2(m-1)^2(2m-1)^2},\\
\partial_y\mathcal K_m&=\frac{4m^3Y(m)}{(m-1)^2(m+1)(2m-1)^2},
\end{aligned}
\]
where
\[
\begin{aligned}
U(m)&=8m^7-24m^6+32m^5-28m^4+13m^2-6m+1,\\
V(m)&=4m^4-8m^3+12m^2-7m+1,\\
Y(m)&=m^4-3m^3+2m^2-2m+1.
\end{aligned}
\]
All are strictly positive for integer \(m\ge3\): setting \(h=m-3\ge0\) yields
\[
\begin{aligned}
U(m)&=8h^7+144h^6+1112h^5+4772h^4+12264h^3+18805h^2+15840h+5608,\\
V(m)&=4h^4+40h^3+156h^2+281h+196,\\
Y(m)&=h^4+9h^3+29h^2+37h+13.
\end{aligned}
\]
Therefore the first-order supporting hyperplane at the corner is strictly increasing in every nonzero feasible direction, since any feasible point has \(u,v,y\ge0\). Convexity proves the stated corner is the global optimum; strict convexity proves uniqueness. Substitution into (1) yields its rational minimum.

**4. The two-page exception.** For \(m=2\), restrict first to the zero-holding curve \(u=v=0\), parameterized by \(y=w\in[0,1)\), \(x=(1-w)/2\), \(z=(1+w)/2\). Formula (1) becomes
\[
Q(w)=\frac{9w^3+21w^2-181w-105}{6(w-1)(w+3)(3w+1)},
\qquad
Q'(w)=\frac{32(15w^3+31w^2+21w-3)}{3(w-1)^2(w+3)^2(3w+1)^2}.
\]
The cubic in the numerator increases strictly on \([0,1]\), is negative at zero and positive at one, hence has exactly one minimizer \(\eta\in(0,1)\). Along the zero-holding curve, the two remaining feasible coordinate derivatives are
\[
\begin{aligned}
\partial_u\mathcal K_2&=\frac{9w^6+42w^5+39w^4+972w^3+1927w^2+1002w+105}{6(w-1)^2(w+3)^2(3w+1)^2},\\
\partial_v\mathcal K_2&=\frac{3w^4+20w^3+114w^2+84w+35}{(w+3)^2(3w+1)^2}.
\end{aligned}
\]
Both are positive for \(0<w<1\). Thus at the unique curve minimum \(w=\eta\), the three feasible coordinate derivatives are nonnegative (strict in the holding directions, zero along \(w\)). The convexity supporting-hyperplane inequality proves unrestricted global optimality; strict convexity gives uniqueness.

**5. Baseline and periodicity.** Substituting the maximum-degree walk into (1) gives the stated benchmark. Division of its leading \((4/3)m^2\) term by the optimum's leading \(m^2\) term gives \(4/3\). Since \(u=v=0\) and every \(B_m\) is connected bipartite, each optimum has eigenvalue \(-1\) and period two, although every \(1-\lambda_j\) for \(j\ge2\) is positive and the Kemeny objective is finite.

## Verification
The included standalone `verify.py` uses SymPy to reconstruct formula (1), all three corner gradients, the positive-coefficient certificates, the two-page cubic derivative and holding-direction inequalities, and the exact maximum-degree ratio. Independently, it constructs full weighted Laplacians and checks the direct inverse trace against formula (1) over 28 exact rational test cases, including connected \(y=0\) boundary cases. Run `python verify.py` with SymPy installed. These finite tests corroborate but do not replace the analytical proof above.

## Relationship to prior work
The closest same-graph previous result is *Sharp compulsory central-rung deletion in quadrilateral-book fastest mixing*, a recorded October 2026 theorem for exactly \(B_m=K_{1,m}\mathbin{\square}K_2\) and unrestricted symmetric stochastic kernels. It establishes that the common edge is necessarily deleted in fastest mixing for every \(m\ge3\), with the same page-count boundary as the present Kemeny optimum; **that boundary is previously known, not a new consequence in isolation**. However its objective is the second-largest eigenvalue modulus, with optimal values \(2-\sqrt2\) for \(m=2\) and \(1-1/m\) thereafter. The recorded symmetry-invariant fastest-mixing optimum for \(m\ge3\) requires \(x=1/m\), \(y=0\), and \(z\le(m-1)/m-1/[2(m-1)]\), whereas the new Kemeny-optimal result uniquely uses \(z=(m-1)/m\), hence lies strictly outside that range, has SLEM one, and is periodic. The two global optimization criteria cannot have a common minimizer: the fastest-mixing optimum has SLEM strictly smaller than one, and the Kemeny minimizer is unique. This is the new direct cross-objective separation and exact Kemeny allocation not implied by the previous SLEM minimax result. Only the recoverable earlier claim was consulted for this comparison; its full manuscript was not inspected.

Boyd, Diaconis and Xiao study the general symmetric-graph-constrained SLEM problem; Hunter's 2012 work describes Kemeny's constant and its normalization; Patel, Agharkar and Bullo establish a convex/semidefinite framework for general Kemeny optimization. Those mathematical frameworks do not supply the new all-size optimal Kemeny probabilities on \(B_m\). A separate book-graph result concerns choosing two pinned leader vertices, not optimizing stochastic transitions. A generalized-quadrilateral paper examines different constructions and fixed-walk spectra. The exact new claim is the unrestricted unique Kemeny optimum, its zero-holding periodicity, and its separation from fastest-mixing and maximum-degree baselines; no priority claim is made for the shared edge-deletion page-count boundary alone. Residual risk from unindexed equivalent Kemeny work remains.

## Limitations
This is a theorem about uniform-stationary symmetric discrete-time chains, with arbitrary holding allowed and graph edges permitted to carry zero weight. It does not optimize reversible chains with nonuniform stationary distribution, directed chains, fastest-mixing SLEM, or restricted positive lower bounds on all edges. At the exact optimum the chain has period two, so it is unsuitable when total-variation convergence from a point source is required without adding laziness. Publication priority beyond the inspected records remains uncertain, and no independent proof audit has occurred.

## References
- Jeffrey J. Hunter, *The Role of Kemeny's Constant in Properties of Markov Chains*, first arXiv version 2012-08-23, https://arxiv.org/abs/1208.4716.
- Stephen Boyd, Persi Diaconis, and Lin Xiao, *Fastest Mixing Markov Chain on a Graph*, *SIAM Review* **46** (2004), 667–689, https://stanford.edu/~boyd/papers/pdf/fmmc.pdf.
- Rushabh Patel, Pushkarini Agharkar, and Francesco Bullo, *Robotic Surveillance and Markov Chains with Minimal Weighted Kemeny Constant*, accessible full text https://motion.me.ucsb.edu/pdf/2014b-pab.pdf.
- Qi Ma and Huaping Wang, *The (normalized) Laplacian spectrum and related indexes of generalized quadrilateral graphs*, *J. Math. Comput. Sci.* **11** (2021), https://doi.org/10.28919/jmcs/5253. (Different graph construction and fixed-walk invariants.)
- *Sharp compulsory central-rung deletion in quadrilateral-book fastest mixing*, recorded October 13, 2026 research theorem, item ca9ef0ce-4718-416f-8bab-e6d27f6de957 (retrieved exact prior claim from historical mathematical record; full manuscript not inspected).
- *A three-stage two-leader transition on quadrilateral book graphs*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-three-stage-two-leader-transition-on-quadrilateral-book-graphs--3b37aec41c1b. (Different optimization problem; full record not accessible in the current inspection.)
