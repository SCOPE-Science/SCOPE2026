# Frozen-coordinate order barriers for graph diffusion: a sharp spectral-variance classification

## Finding

Let \(G\) be a finite connected undirected graph with \(n\ge2\) vertices and strictly positive symmetric edge conductances. Its weighted combinatorial Laplacian is \(L\). Fix a uniform killing rate \(\kappa\ge0\), put \(Q=L+\kappa I\), and consider the positive linear flow
\[
\dot u=-Qu,\qquad u(t)=e^{-tQ}u(0).
\]
Consider **any** finite-valued, one-evaluation, coordinatewise residual-scaled step
\[
\mathcal F_h(u)_i=u_i-\psi_i(h,u)(Qu)_i,\qquad h>0,
\]
where the multipliers may depend nonlinearly on the entire state and on the timestep. In particular, this includes finite positive denominator steps \(\psi_i=\phi_i/(1+\tau_i\phi_i)\). No boundedness assumption on the multipliers as \(h\to0\) is needed for the obstruction.

For each vertex \(i\), define the **local spectral-variance obstruction**
\[
\Delta_i(Q)^2=(Q^4)_{ii}-\frac{((Q^3)_{ii})^2}{(Q^2)_{ii}}\ge0.
\]
The denominator is positive. Every starting state on the coordinate nullcline \((Qu)_i=0\) is frozen at that coordinate by every such step, while the exact flow generally moves by a term of order \(h^2\). The obstruction is sharp: if \(u_0\) is strictly positive and \((Qu_0)_i=0\), and \(0<\varepsilon<\min_j(u_0)_j\), then
\[
\lim_{h\downarrow0}\frac1{h^2}
\sup_{\substack{z\perp Qe_i\\\|z\|_2\le1}}
\left|[\mathcal F_h(u_0+\varepsilon z)-e^{-hQ}(u_0+\varepsilon z)]_i\right|
=\frac{|(Q^2u_0)_i|+\varepsilon\Delta_i(Q)}2.
\]
This value is independent of the choice of finite multipliers. In particular, a positive obstruction forces a genuine local error of order \(h^2\), incompatible with second-order local consistency at every strictly positive state.

There is a complete graph-theoretic classification:

1. **Killing:** if \(\kappa>0\), then \(\Delta_i(Q)>0\) at *every* vertex of *every* connected weighted graph with \(n\ge2\). Consequently no finite coordinatewise residual-scaled step can have second-order local consistency on the entire strictly positive cone. Such killed graph flows have a unique hyperbolic equilibrium and satisfy standard positivity assumptions for dynamical systems.
2. **Conservative diffusion:** if \(\kappa=0\), all the obstructions vanish exactly when \(G\) is a complete graph having one common conductance \(w>0\) on every edge. For this exceptional family, \(L=nw(I-\mathbf1\mathbf1^\top/n)\), and the scalar multiplier \(\psi_i(h,u)=(1-e^{-nwh})/(nw)\) reproduces the exact, positive heat flow for every state and every timestep.
3. **Vertex classification without weights:** if \(\kappa=0\) and every existing edge has conductance one, then \(\Delta_i(L)=0\) **if and only if** vertex \(i\) is universal (adjacent to all other vertices). Thus a star's center has no coordinate-freeze obstruction, but its noncentral leaves do.

The obstruction survives arbitrarily weak killing even on the exceptional complete graph. Writing \(c=nw\) on that graph, the exact formula is
\[
\Delta_i(L+\kappa I)^2=\frac{c^2\kappa^2(c+\kappa)^2(n-1)}{n\bigl(\kappa^2+(n-1)(c+\kappa)^2\bigr)},\qquad
\Delta_i(L+\kappa I)\sim\frac{c\kappa}{\sqrt n}
\quad(\kappa\downarrow0).
\]

## Assumptions and scope

The graph is finite, connected, undirected, loopless, with strictly positive conductances on all its edges; zero conductances mean absent edges. The state space in the order statement is the full strictly positive orthant \((0,\infty)^n\), and \(n\ge2\). The map is evaluated once at the old state and has no extra additive stage or nonlocal correction. Each \(\psi_i(h,u)\) must be a finite real number for the state and positive step in question. For conventional first-order consistency one may additionally require \(\psi_i(h,u)=h+O(h^2)\) at fixed states, but this is **not used** in the impossibility proof. Second-order *local* consistency means \(\mathcal F_h(u)-e^{-hQ}u=O(h^3)\) as \(h\downarrow0\) for every fixed strictly positive \(u\). There is no claim about global convergence orders under weaker, state-dependent definitions.

When \(\kappa>0\), the vector field \(f(u)=-Qu\) satisfies \(f_i(u)+(\deg_w(i)+\kappa)u_i=\sum_jw_{ij}u_j\ge0\) for nonnegative \(u\), and its sole equilibrium \(u=0\) is hyperbolic and attracting. Thus the no-go branch is not caused by a failure of these common positivity and hyperbolicity assumptions.

## Proof

**1. Coordinate freezing and exact local error.** Put \(r_i=e_i^\top Q\) and \(s_i=e_i^\top Q^2\). Whenever \(r_i u=0\), the proposed numerical step has \(\mathcal F_h(u)_i=u_i\), identically for every finite multiplier. The matrix exponential gives, uniformly for bounded \(u\),
\[
(e^{-hQ}u)_i=u_i-h r_i u+\frac{h^2}{2}s_i u+O(h^3\|u\|_2).
\]
On the nullcline, the difference is \(-h^2s_i u/2+O(h^3\|u\|_2)\). The orthogonal projection of \(s_i\) onto \(r_i^\perp\) has squared length
\[
\|s_i\|_2^2-\frac{(s_i r_i^\top)^2}{\|r_i\|_2^2}=(Q^4)_{ii}-\frac{((Q^3)_{ii})^2}{(Q^2)_{ii}}.
\]
Since \(u_0+\varepsilon z\) is positive for every \(\|z\|_2\le1\) under the stated bound on \(\varepsilon\), and the suprema of \(s_i z\) over the unit ball in \(r_i^\perp\) are \(\pm\Delta_i(Q)\), the displayed sharp supremum formula follows. The exponential remainder is uniform over this compact ball. Moreover, \(\Delta_i(Q)=0\) precisely when \(r_iQ\) is a scalar multiple of \(r_i\), equivalently \(Qe_i\) is a \(Q\)-eigenvector.

**2. The nullcline meets the positive cone.** Every vertex has positive weighted degree \(d_i\) because the graph is connected and nontrivial. Set \((u_0)_j=1\) for \(j\ne i\) and \((u_0)_i=d_i/(d_i+\kappa)\). This is strictly positive, and \((Qu_0)_i=(d_i+\kappa)(u_0)_i-d_i=0\). If \(\Delta_i(Q)>0\), the positive nullcline contains an open relative neighborhood of \(u_0\), and some such state has \(s_i u\ne0\); this also follows directly from the sharp supremum formula. Hence second-order local consistency on the entire positive cone requires every \(\Delta_i(Q)\) to vanish.

**3. Killing gives a universal obstruction.** Suppose \(\kappa>0\). Connectedness gives \(L\mathbf1=0\) with a simple zero eigenvalue and strictly positive remaining eigenvalues. Accordingly \(Q\) has eigenvalue \(\kappa\) on the constant vectors and eigenvalues greater than \(\kappa\) on their orthogonal complement. For each \(i\), \(e_i\) has a nonzero projection onto each of these two invariant subspaces. Multiplication by invertible \(Q\) preserves both nonzero spectral projections. Thus \(Qe_i\) has nonzero spectral components at distinct eigenvalues and cannot itself be an eigenvector. Therefore \(\Delta_i(Q)>0\) for every \(i\), and Step 2 supplies strictly positive nullcline states with second-order defects.

**4. Zero-killing global classification.** Suppose \(\kappa=0\) and every \(\Delta_i(L)=0\). Then for each vertex there is a real scalar \(c_i\) such that the \(i\)-th row of \(L^2\) is \(c_i\) times the \(i\)-th row of \(L\). Equivalently \(L^2=CL\) with \(C=\operatorname{diag}(c_i)\). Symmetry of \(L^2\) implies \(CL=LC\). On each positive-conductance edge \(i\!\sim\!j\), the off-diagonal \(L_{ij}\ne0\) forces \(c_i=c_j\). By connectedness all \(c_i\) agree, say \(c>0\), so \(L^2=cL\). The spectral theorem and connectedness show that \(0\) has multiplicity one and every other eigenvalue is \(c\). Therefore
\[
L=c\left(I-\frac{\mathbf1\mathbf1^\top}{n}\right),
\]
which is exactly a complete graph with every edge conductance \(c/n\). Conversely this formula satisfies \(L^2=cL\), so every obstruction vanishes. Also \(e^{-hL}=I-(1-e^{-ch})L/c\), establishing the claimed exact scalar multiplier and positivity for all steps.

**5. Individual vertices of unweighted graphs.** If vertex \(i\) is universal, then \(Le_i=ne_i-\mathbf1\) and \(L^2e_i=nLe_i\), so \(\Delta_i(L)=0\). Otherwise, connectedness ensures a vertex \(j\) at graph distance exactly two from \(i\); then \(L_{ij}=0\) but \((L^2)_{ij}\) equals the positive number of common neighbors of \(i,j\). Thus row \(i\) of \(L^2\) cannot be proportional to row \(i\) of \(L\), proving \(\Delta_i(L)>0\).

**6. Exact killed-clique constant.** In the exceptional conservative clique, \(Q\) has eigenvalues \(\kappa\) on constants and \(c+\kappa\) on their orthogonal complement. The squared norm of the constant spectral part of \(Qe_i\) is \(a=\kappa^2/n\), and that of the nonconstant part is \(b=(n-1)(c+\kappa)^2/n\). The squared projection distance of \(Q^2e_i\) from the span of \(Qe_i\) is \(ab c^2/(a+b)\), giving the formula and its small-\(\kappa\) asymptotics.

## Verification

The standalone \(\texttt{verify.py}\) uses exact rational matrix arithmetic. It checks every connected simple graph on two through five vertices: the vertexwise universal-vertex criterion, positivity of the killed obstruction at every vertex, and the all-vertex complete-graph criterion. It additionally checks weighted complete graphs with different conductances, the closed-form killed-clique obstruction for multiple sizes and parameters, and exact two- and three-vertex witnesses. It performs 12,445 assertions/diagnostic checks in the supplied version and prints \(\texttt{VERIFY_OK}\) if successful. These finite checks are not substitutes for Steps 1–6.

Two exact illustrative witnesses are:

* For the unit three-vertex path, take \(u=(1,1,2)^\top\). At its first endpoint, \((Lu)_1=0\), \((L^2u)_1=1\), and \(\Delta_1(L)^2=3/2\), so that component's one-step error is \(-h^2/2+O(h^3)\), irrespective of multiplier.
* For the two-vertex unit edge with \(\kappa=1\), \(Q=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\) and \(u=(1,2)^\top\). Here \((Qu)_1=0\) and \((Q^2u)_1=-3\), giving error \(+3h^2/2+O(h^3)\). This positive system has a unique attracting hyperbolic equilibrium.

Execute \(\texttt{python3 verify.py}\) with Python 3 and no third-party dependencies.

## Relationship to prior work

Hoang's 2026 nonstandard-denominator scheme (1.4), equivalently (2.3), uses the coordinatewise old-state residual form analyzed here [1]. Its Theorem 2.3 derives a second-order denominator condition using a quotient with \(f_i(u)\) and states that condition at states where \(f_i(u)\ne0\). Our sharp theorem instead analyzes the excluded zero-residual hypersurfaces, where finite scalar multipliers cannot change a coordinate even though the exact second derivative may be nonzero. This distinguishes the logical domains: the obstruction does not assert that the published nonzero-residual Taylor identity is invalid, but establishes that an unqualified whole-positive-cone second-order claim cannot follow from such an identity.

The earlier modified explicit-Euler method of Alalhareth, Gupta, Kojouharov and Roy [2, Theorem 1, equations (3) and its proof] belongs to the same coordinatewise class and states a second-order conclusion for general differentiable systems; its zero-component case explicitly identifies the unchanged numerical coordinate with the exact evolution. The graph witnesses here directly distinguish an instantaneously vanishing component derivative from a constant component trajectory. Its two-stage Runge–Kutta construction is not in the one-evaluation class. In contrast, Anguelov and Lubuma's 2022 symmetric second-order construction [3, Eq. (6)] uses nonlocal evaluations of both endpoint states and is not excluded. The graph Laplacian and finite-dimensional spectral identities used here are classical; the assessed new statement is the quantitative sharp graph-nullcline obstruction with exact weighted graph classification and its killed complete-graph asymptotics. This is a domain-specific implication comparison, not a claim of exhaustive historical priority.

## Limitations

The result is limited to a single initial-state residual evaluation multiplied coordinatewise by finite scalars. A stage method, an implicit/nonlocal right-hand-side evaluation, an additive higher-derivative correction, or an update with potentially singular undefined factors is outside the domain. No theorem is claimed for general nonlinear systems, directed graphs, disconnected graphs, or global second-order convergence at fixed final time. The graph classifications rely on symmetry; a different statement may be necessary for directed Markov generators. The local order obstruction does not prohibit positivity-preserving second-order methods from other families.

## References

1. Manh Tuan Hoang, *A simple second-order nonstandard numerical method for a general class of dynamical systems and its applications*, arXiv:2608.09141, version 1, first submitted 2026-08-10. https://arxiv.org/abs/2608.09141
2. Fawaz K. Alalhareth, Madhu Gupta, Hristo V. Kojouharov and Souvik Roy, *Second-Order Modified Nonstandard Explicit Euler and Explicit Runge–Kutta Methods for n-Dimensional Autonomous Differential Equations*, Computation **12** (2024), 183, published 2024-09-09. https://doi.org/10.3390/computation12090183
3. Roumen Anguelov and Jean M.-S. Lubuma, *Second-order nonstandard finite difference schemes for a class of models in bioscience*, arXiv:2207.11618, version 1, 2022-07-23. https://arxiv.org/abs/2207.11618
4. Standard finite graph Laplacian and spectral-theorem identities, recalled and proved as needed above.
