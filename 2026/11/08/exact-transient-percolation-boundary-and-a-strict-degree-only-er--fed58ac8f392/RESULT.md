# Exact transient percolation boundary and a strict degree-only error in a resetting network

## Finding
Consider the node-resetting, edge-creation network of Artime [1], observed a fixed positive time after an initially edgeless state. Put \(u=rt>0\) and \(c=\alpha/r>0\). Let
\[
\mu_u(dx)=e^{-x}\mathbf 1_{(0,u)}(x)\,dx+e^{-u}\delta_u(dx),
\qquad
(K_uf)(x)=\int_{(0,u]}\min(x,y)f(y)\,\mu_u(dy).
\]
Here \(\delta_u\) is a point mass at the right endpoint. Let \(\lambda_u=\|K_u\|_{L^2(\mu_u)\to L^2(\mu_u)}\). In the limit of infinitely many vertices, a giant component is present with high probability precisely when
\[
c>c_*(u):=\lambda_u^{-1};
\]
when \(c\le c_*(u)\), the largest component occupies a vanishing fraction of the graph.

For every \(u>0\), the published degree-only critical line [1, Eq. (16)] is **strictly too high**:
\[
\boxed{\quad c_*(u)<c_{\mathrm{degree}}(u)
=\frac{3(1+e^{-u})}{2(1+e^{-u}-2e^{-2u})}.\quad}
\]
Consequently every \(u>0\) has a nonempty interval of connection strengths where a giant component exists despite the degree-only calculation predicting none. Moreover \(c_*(u)\) decreases strictly with \(u\), tends to infinity as \(u\downarrow0\), and
\[
\boxed{\quad \lim_{u\to\infty}c_*(u)=\frac{j_{0,1}^2}{4}
=1.445796490736\ldots<\frac32.\quad}
\]
Here \(j_{0,1}\) is the first positive zero of the ordinary Bessel function \(J_0\). This stationary Bessel spectral value is known for an equivalent limiting kernel in a different model [2, Section 16.5]; the contribution here is the **finite-time phase boundary for the node-resetting process and the strict comparison at every positive time**.

The finite-time threshold is explicitly characterized by a Sturm--Liouville problem. Its principal eigenvalue is the unique value \(\lambda>0\) admitting a strictly positive solution of
\[
\lambda f''(x)=-e^{-x}f(x)\quad(0<x<u),\qquad
f(0)=0,\qquad \lambda f'(u)=e^{-u}f(u).
\]
Equivalently, with \(q=2/\sqrt\lambda\) and \(v=qe^{-u/2}\), the principal branch satisfies
\[
Y_0(q)[2J_1(v)-vJ_0(v)]-J_0(q)[2Y_1(v)-vY_0(v)]=0.
\]
For example, \(c_*(1)=1.843805774139\ldots\), whereas \(c_{\mathrm{degree}}(1)=1.870035149252\ldots\). As \(u\downarrow0\), \(c_*(u)\sim u^{-1}\).

## Assumptions and scope
For each integer \(N\ge2\), begin from the empty undirected graph on \(N\) labelled vertices. Independently, at rate \(\alpha N/2\), attempt an edge between one uniformly chosen unordered distinct pair; repeated attempts do not affect simple-graph connectivity. At rate \(rN\), uniformly choose a vertex and delete all its incident edges, leaving the same vertex isolated. Here \(r,\alpha>0\) are fixed, and \(t>0\) is fixed before taking \(N\to\infty\). Equivalently each vertex resets independently at rate \(r\), and each pair receives independent edge attempts at rate \(\alpha/(N-1)\). The statement concerns the simple-graph projection if multiple edge attempts are recorded.

The giant-component assertion is the usual large-\(N\) statement: \(C_1/N\to0\) in probability below and at criticality, and \(C_1/N\) converges to a strictly positive deterministic limit in probability above criticality. No claim is made about a finite-size critical window.

## Proof
**Conditional graph law.** Independent Poisson splitting turns the global clocks into independent vertex-reset clocks and pair-attempt clocks. At time \(t\), the time since the last reset of vertex \(i\), or since initialization if no reset occurred, is \(A_i=\min(E_i,t)\), where \(E_i\) are independent exponentials of rate \(r\). Hence the scaled ages \(X_i=rA_i\) have independent common law \(\mu_u\). A potential edge \(ij\) is present exactly when its pair clock rang after both vertices' last resets; conditionally on all ages, distinct edges are independent, and
\[
\mathbb P(ij\in E\mid X_1,\ldots,X_N)
=1-\exp\left[-\frac{c\min(X_i,X_j)}{N-1}\right].
\]
This is an inhomogeneous random graph with limiting type distribution \(\mu_u\) and kernel \(c\min(x,y)\), including the genuine endpoint atom. It is irreducible on \((0,u]\) up to null sets, and its kernel is bounded at each fixed \(u\). The giant-component theorem for inhomogeneous random graphs [2, Theorem 3.1] therefore gives the exact threshold \(c\lambda_u=1\), including the absence of an extensive component at equality.

**Why the degree-only threshold is always incorrect.** For \(0<x\le u\), direct tail integration gives
\[
(K_u\mathbf1)(x)=\int_0^x\mu_u([s,u])\,ds=1-e^{-x}=:g(x).
\]
Consequently
\[
m_1:=\langle\mathbf1,K_u\mathbf1\rangle
=\frac{1-e^{-2u}}2,
\qquad
m_2:=\langle\mathbf1,K_u^2\mathbf1\rangle
=\frac{1-3e^{-2u}+2e^{-3u}}3.
\]
Conditionally on its age, a vertex has asymptotic Poisson degree of mean \(cg(x)\). Thus the degree-only Molloy--Reed closure places criticality at \(c=m_1/m_2\), algebraically the displayed \(c_{\mathrm{degree}}(u)\), exactly the line printed in [1]. But \(K_u\) is positive semidefinite, since for every real \(h\in L^2(\mu_u)\),
\[
\langle h,K_uh\rangle
=\int_0^u\left(\int_{[s,u]}h(x)\,\mu_u(dx)\right)^2ds\ge0.
\]
It is compact, injective, and has a simple positive leading eigenfunction. The spectral inequality \(K_u^2\preceq\lambda_u K_u\) implies \(m_2\le\lambda_um_1\). Equality would force \(\mathbf1\) into the top eigenspace (injectivity removes a possible nullspace component), contradicting \(K_u\mathbf1=1-e^{-x}\), which is nonconstant. Thus \(m_2<\lambda_um_1\), proving \(c_*(u)<m_1/m_2\) for every \(u>0\). The same argument applies to the stationary infinite-interval operator.

**Eigenvalue equation.** Differentiating the eigen-equation for \(K_uf=\lambda f\) on \((0,u)\) yields \(\lambda f''=-e^{-x}f\); the minimum kernel forces \(f(0)=0\). Its right derivative satisfies \(\lambda f'(u-)=e^{-u}f(u)\), because the endpoint atom contributes mass \(e^{-u}\). Under \(z=2e^{-x/2}/\sqrt\lambda\), the ODE is the Bessel equation of order zero. The solution vanishing at \(x=0\) is proportional to
\[
F(z)=Y_0(q)J_0(z)-J_0(q)Y_0(z).
\]
The right boundary reads \(-2F'(v)=vF(v)\), yielding the displayed finite-time Bessel determinant. Positivity of the principal eigenfunction and the compact positive integral operator select the principal root without ambiguity.

**Time dependence and stationary boundary.** Couple all horizons by a single independent pair of unit-rate exponentials \(E,E'\). The kernel becomes \(\min(E,E',u)\) on a common probability space. For \(0<u<v\), this kernel increases pointwise and strictly on a positive-probability set, so positivity of the principal eigenfunction implies \(\lambda_v>\lambda_u\). As \(u\downarrow0\), its ratio to \(u\) converges to the rank-one constant kernel in Hilbert--Schmidt norm, hence \(\lambda_u/u\to1\). As \(u\to\infty\), the kernels converge in Hilbert--Schmidt norm to \(\min(E,E')\). On the infinite half-line the boundary becomes \(f'(\infty)=0\), excluding the divergent \(Y_0\) solution. Therefore \(J_0(2/\sqrt{\lambda_\infty})=0\), and the positive principal eigenfunction selects \(\lambda_\infty=4/j_{0,1}^2\). At stationarity \(m_1=1/2\), \(m_2=1/3\), yielding the degree-only value \(3/2\) and the strict limiting discrepancy.

## Verification
Run `python verify.py` with Python, NumPy, SciPy and SymPy. It checks the endpoint-atom moment identities symbolically, independently evaluates the principal eigenvalue through a quadrature matrix and a Robin-boundary ODE, tests the Bessel determinant, and checks the strict ordering and asymptotic limit. A completed run gave 42 passed assertions, including \(c_*(1)=1.843805774139\ldots\). These finite numerical tests supplement the analytic operator argument and are not offered as a proof of a universal inequality.

## Relationship to prior work
Artime [1, Sections 2--4, especially Eq. (16)] defines exactly the edge-creation/vertex-resetting dynamics and computes the degree distribution, but uses the uncorrelated degree-based branching closure for the giant component. The conditional age representation shows why that closure loses relevant two-endpoint correlations. Bollobás--Janson--Riordan [2, Theorem 3.1] provide the general inhomogeneous-random-graph giant criterion; their Section 16.5 already evaluates the **same limiting stationary minimum-age kernel** in Turova's different vertex-growth/edge-death model. That stationary Bessel constant is prior art, not asserted as novel independently. Crane--Ráth--Yeo [3, Section 2.2] develop age-driven inhomogeneous random graphs in a forest-fire model with component-dependent resets, but do not supply the independent-reset truncated-exponential age law or its exact positive-time phase boundary. The asserted contribution is the application to [1], the atom-sensitive finite-time eigenboundary, and the strict full-time discrepancy from [1, Eq. (16)].

## Limitations
The theorem is at fixed positive time followed by \(N\to\infty\), for homogeneous independent Poisson vertex resets and uniformly attempted edges from the empty initial graph. It does not quantify finite-size scaling, finite-system giant-component probabilities, non-Poisson reset distributions, or other initial conditions. The known stationary spectral constant from [2] is not a claim of independent novelty; published work might contain an implicit equivalent time-dependent calculation beyond the inspected sources. No independent scientific validation has been performed.

## References
[1] O. Artime, *Stochastic resetting in a networked multiparticle system with correlated transitions*, arXiv:2211.01869 (first public version 2022-11-03), https://arxiv.org/abs/2211.01869 .

[2] B. Bollobás, S. Janson, O. Riordan, *The phase transition in inhomogeneous random graphs*, arXiv:math/0504589 (2005), especially Theorem 3.1 and Sections 16.5--16.6, https://arxiv.org/abs/math/0504589 .

[3] E. Crane, B. Ráth, D. Yeo, *Age evolution in the mean field forest fire model via multitype branching processes*, arXiv:1811.07981 (2018), Section 2.2, https://arxiv.org/abs/1811.07981 .
