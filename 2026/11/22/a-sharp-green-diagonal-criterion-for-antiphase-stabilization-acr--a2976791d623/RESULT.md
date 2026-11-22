# A sharp Green-diagonal criterion for antiphase stabilization across a single network bridge

## Finding
For the finite mixed-interaction Kuramoto flow defined below, with identical natural frequencies, the balanced antipodal configuration on two equal connected communities joined by exactly one edge is exponentially orbitally attracting **if and only if**
\[
R<1,\qquad K_2>\frac{2K_1}{|E|(1-R)},\qquad R=(L_A^\dagger)_{aa}+(L_B^\dagger)_{bb}.
\]
At equality in the second inequality (only when \(R<1\)), its Jacobian gains a second zero eigenvalue in addition to global phase rotation; below the threshold, or for every finite \(K_2\ge0\) when \(R\ge1\), it has exactly one positive eigenvalue. Whenever the antipodal state is attracting, the fully synchronized state is attracting as well.

As a sharp topology contrast, on the path with \(2m\) vertices, only \(m=1,2\) can ever stabilize this antipodal state using nonnegative global triadic coupling. Two \(m\)-cliques joined by one bridge, by contrast, can stabilize it for every \(m\ge2\), with the exact threshold below.

## Assumptions and scope
Let \(G=(V,E)\) be a finite connected undirected simple graph, and let \(V=A\sqcup B\), with \(|A|=|B|=m\ge1\), each induced graph \(G_A,G_B\) connected. Assume the **only** edge between the two vertex sets is \(\{a,b\}\), with \(a\in A\), \(b\in B\). Let \(N=2m\), \(d=2|E|/N>0\), and let \(L_A,L_B\) denote unweighted combinatorial Laplacians. For a singleton component, set its Laplacian pseudoinverse to the zero matrix.

Choose \(K_1>0\), \(K_2\ge0\), and identical oscillator frequencies \(\omega_i=\omega\). In the uniformly rotating frame the equations, with ordered indices in the triadic sum including repetitions, are
\[
\dot\theta_i=\frac{K_1}{d}\sum_{j=1}^N A_{ij}\sin(\theta_j-\theta_i)
+\frac{K_2}{N^2}\sum_{j,l=1}^N\sin(2\theta_j-\theta_l-\theta_i),
\quad i=1,\ldots,N.
\]
The balanced antipodal family consists of \(\theta_i=\phi\) for \(i\in A\) and \(\theta_i=\phi+\pi\) for \(i\in B\), with \(\phi\in\mathbb R/(2\pi\mathbb Z)\). It is an equilibrium circle: each graph-edge sine is zero, and the triadic sum vanishes because the first order parameter is zero. *Exponentially orbitally attracting* means exponentially asymptotically stable on the quotient by common phase shifts, or equivalently that the Jacobian is strictly negative definite on the mean-zero subspace.

## Proof
**Linearization.** Put \(s_i=1\) on \(A\) and \(s_i=-1\) on \(B\). Then \(\sum_i s_i=0\), and \(e^{2i\theta_j}=1\) at the antipodal configuration. Differentiating the triadic sum for every ordered \((j,l)\) gives \(-K_2ss^\top/N\): the first-index derivatives vanish after summing over \(l\), and the last-index derivative vanishes since \(\sum_l s_l=0\). Each intra-community edge has cosine \(+1\) and the bridge has cosine \(-1\). Thus the real symmetric Jacobian is
\[
J=-\frac{K_1}{d}\bigl[(L_A\oplus L_B)-(e_a-e_b)(e_a-e_b)^\top\bigr]
-\frac{K_2}{N}ss^\top.
\]
Here \(e_a,e_b\) are embedded in the full vertex space. As expected \(J\mathbf1=0\).

**Exact reduction of the quadratic form.** Every vector in \(\mathbf1^\perp\) has a unique representation
\[
x_A=c\mathbf1_m+u,\qquad x_B=-c\mathbf1_m+v,\qquad
\mathbf1_m^\top u=\mathbf1_m^\top v=0.
\]
Write \(\delta=u_a-v_b\), \(E_0=u^\top L_Au+v^\top L_Bv\), and \(\gamma=K_2d/K_1\). A direct computation shows
\[
\frac{d}{K_1}x^\top(-J)x=E_0-(2c+\delta)^2+\gamma N c^2.
\tag{1}
\]
For \(m\ge2\), the Laplacian quadratic forms are positive definite on each block's mean-zero space. The sharp Rayleigh duality identity for the linear functional \((u,v)\mapsto u_a-v_b\) is
\[
\sup_{E_0>0}\frac{\delta^2}{E_0}
=(L_A^\dagger)_{aa}+(L_B^\dagger)_{bb}=R>0.
\]
Indeed Cauchy--Schwarz in the block Laplacian energy inner product gives the upper bound, with equality for the pseudoinverse representers. For each chosen \(\delta\), the minimum \(E_0\) therefore equals \(\delta^2/R\); the remaining block-internal directions carry strictly positive energy. The reduced quadratic form is
\[
\left(\frac1R-1\right)\delta^2-4c\delta+(\gamma N-4)c^2.
\tag{2}
\]
It is positive definite precisely if \(R<1\) and its Schur complement is positive:
\[
\gamma N-4-\frac{4}{1/R-1}>0
\iff\gamma N>\frac4{1-R}
\iff\ K_2>\frac{4K_1}{Nd(1-R)}
=\frac{2K_1}{|E|(1-R)}.
\]
For \(m=1\), there are no nonzero internal perturbations and \(R=0\); formula (1) reduces to \((\gamma N-4)c^2\), yielding the same condition. At the finite threshold with \(R<1\), exactly one extra zero direction appears. If \(R\ge1\), form (2) is negative somewhere at every finite \(\gamma\) (for \(R=1\), take nonzero \(\delta\) and a sufficiently small \(c\) of the same sign); hence no coupling can stabilize it. In all non-attracting regimes away from threshold, there is exactly one unstable direction: \(-J\) is a positive-semidefinite block-Laplacian-plus-rank-one form minus a single bridge square, so it has at most one negative direction, while the displayed test yields at least one. This proves the sharp stability classification.

**Coexisting synchrony.** At the all-equal phase state, direct differentiation gives
\[
J_{\rm sync}=-\frac{K_1}{d}L_G-K_2\bigl(I-\mathbf1\mathbf1^\top/N\bigr).
\]
Connectedness and \(K_1>0\) make this strictly negative on \(\mathbf1^\perp\), independently of \(K_2\). Hence whenever the antipodal state is stable there are two distinct locally attracting equilibrium circles, one all-equal and one antipodal.

**Exact graph families.** For the path \(P_{2m}\) cut at its central edge, the well-known endpoint Green diagonal can be computed directly from the one-dimensional inverse Laplacian or from pairwise distances:
\[
(L_{P_m}^\dagger)_{\text{end},\text{end}}
=\frac{(m-1)(2m-1)}{6m}.
\]
One derivation uses the pseudoinverse resistance identity \((L^\dagger)_{aa}=(1/m)\sum_v d(a,v)-(1/(2m^2))\sum_{u,v}d(u,v)\), since unit path resistance equals graph distance. Therefore
\[
R_{P_{2m}}=\frac{(m-1)(2m-1)}{3m}.
\]
It is below one exactly at \(m=1,2\). The exact coupling thresholds are \(K_2>2K_1\) for \(P_2\), and \(K_2>4K_1/3\) for \(P_4\); paths on at least six vertices remain unstable at any finite \(K_2\).

For the graph obtained by joining two complete graphs \(K_m\) at one bridge, \(m\ge2\), the formula \(L_{K_m}^\dagger=m^{-1}(I-\mathbf1\mathbf1^\top/m)\) gives \(R=2(m-1)/m^2<1\). There are \(|E|=m(m-1)+1\) edges, giving the exact threshold
\[
K_2>\frac{2K_1}{[m(m-1)+1][1-2(m-1)/m^2]}
\sim\frac{2K_1}{m^2}\quad (m\to\infty).
\]
This completes the proof.

## Verification
`check.py` (Python 3 and SymPy) constructs the signed Jacobian quadratic form over an exact rational basis of the mean-zero subspace, independently computes the Green diagonal by the identity \(L^\dagger=(L+\mathbf1\mathbf1^\top/m)^{-1}-\mathbf1\mathbf1^\top/m\), and applies Sylvester's criterion using exact rational determinants. It tests every connected labelled block graph among selected sizes up to four nodes per block, along with paths, cliques, and values on either side of and exactly at the predicted threshold. The test output is included in `VERIFICATION.md`. This is finite corroboration; the unrestricted theorem follows from the proof above, not from enumeration.

## Relationship to prior work
Sharma et al. (2026) introduce the same mixed pairwise-network/global-triad phase equation and numerically examine synchronization thresholds on Erdős--Rényi graphs with heterogeneous frequencies; no exact bridge antiphase Hessian or Green-diagonal criterion is given there. The present result is for identical frequencies and deterministic two-community graphs, so it is not a general formula for their random-graph transition statistics.

Zelazo and Bürger (2014) develop general signed-Laplacian effective-resistance definiteness theory. The use of Laplacian energies and pseudoinverses here is an application of established linear-algebraic technology, not a new general theorem on signed matrices. The distinguishing result is the model-specific global-triad rank-one linearization, its necessary-and-sufficient stabilization threshold for all single-bridge partitions, and the sharp path-versus-barbell contrast.

Kachhvah and Jalan (2022) obtain antiphase clustering for **adaptive** dyadic/triadic weights, and Bick, Böhle and Kuehn (2023) analyze twisted states for nonlocal higher-order interactions in ring graphon limits. Neither supplies the present finite, static, one-bridge criterion. Menara et al. (2018) study sparse Kuramoto cluster manifolds without this global three-body term and require an external equitable condition for invariant cluster manifolds, whereas our antipodal **single equilibrium** exists even when the two-block partition is not externally equitable.

## Limitations
This is a local, deterministic theorem. It assumes simple unweighted graph edges, connected equal-sized blocks separated by exactly one bridge, identical frequencies, positive pairwise coupling, nonnegative global triadic coupling, and the ordered-index triad sum as specified. It neither proves global attraction nor describes basin volumes, heterogeneous frequencies, general multi-bridge graphs, random-network synchronization transitions, or nonlinear dynamics at the nonhyperbolic equality threshold. Prior generic signed-Laplacian theory covers part of the proof strategy; the model-specific result may also have appeared under different terminology, which a finite literature search cannot rule out.

## References
- A. Sharma, A. Suman, M. Anvari, M. D. Shrimali, C. I. del Genio and S. Jalan, *Synchronization transitions in Kuramoto oscillators with mixed interactions*, arXiv:2611.09564v1 (first publicly posted 2026-11-06), https://arxiv.org/html/2611.09564v1.
- D. Zelazo and M. Bürger, *On the Definiteness of the Weighted Laplacian and its Connection to Effective Resistance*, arXiv:1408.2187v1 (2014), https://arxiv.org/html/1408.2187v1.
- A. D. Kachhvah and S. Jalan, *First-order route to antiphase clustering in adaptive simplicial complexes*, arXiv:2203.16254v3 (2022), https://arxiv.org/html/2203.16254v3.
- C. Bick, T. Böhle and C. Kuehn, *Phase Oscillator Networks with Nonlocal Higher-Order Interactions: Twisted States, Stability, and Bifurcations*, SIAM J. Applied Dynamical Systems (2023), DOI:10.1137/22M1500940, https://epubs.siam.org/doi/10.1137/22M1500940.
- T. Menara, G. Baggio, D. S. Bassett and F. Pasqualetti, *Stability Conditions for Cluster Synchronization in Networks of Heterogeneous Kuramoto Oscillators*, arXiv:1806.06083 (2018), https://arxiv.org/abs/1806.06083.
