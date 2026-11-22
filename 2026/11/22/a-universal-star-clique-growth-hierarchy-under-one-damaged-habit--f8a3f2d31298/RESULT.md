# A universal star–clique growth hierarchy under one damaged habitat

## Finding

**Theorem (uniform topology and damage-location ordering).** For every integer \(n\ge3\), every emigration rate \(m>0\), every additional mortality rate \(\delta>0\), and every common local net growth rate \(r\in\mathbb R\), let \(\Lambda_{L}\), \(\Lambda_{K}\), and \(\Lambda_{H}\) be the principal linear population growth exponents when a single damaged patch is respectively a **leaf of the \(n\)-star**, an arbitrary vertex of the **complete \(n\)-patch network**, and the **hub of the \(n\)-star**. Every individual emigrates at total rate \(m\) and chooses uniformly among its current neighbors. The damaged patch has local rate \(r-\delta\), and every other patch has local rate \(r\).

Then the strict ordering

\[
\boxed{\Lambda_{L}>\Lambda_{K}>\Lambda_{H}}
\]

holds for all admissible parameters, with no migration-rate or mortality-severity crossover. Thus completing the star can lower or raise the linear growth exponent, depending on which patch is degraded. More explicitly, set \(q=\delta/m\), \(\alpha=(n-2)/(n-1)\) and \(\beta=1/(n-1)\). Write \(\Lambda_i=r+m(z_i-1)\), where each \(z_i\) is the largest real root of the corresponding equation:

\[
\begin{aligned}
&z_L^3+qz_L^2-z_L-\alpha q=0,\\
&(z_K+q)(z_K-\alpha)=\beta,\\
&z_H(z_H+q)=1.
\end{aligned}
\]

They satisfy \(\sqrt\alpha<z_L<1\), \(\alpha<z_K<1\), and \(0<z_H<1\).

For fixed \(n,m\), as \(\delta\downarrow0\),

\[
\begin{aligned}
\Lambda_L&=r-\frac{\delta}{2(n-1)}+O(\delta^2/m),\\
\Lambda_K&=r-\frac{\delta}{n}+O(\delta^2/m),\\
\Lambda_H&=r-\frac{\delta}{2}+O(\delta^2/m).
\end{aligned}
\]

For fixed \(n,m\), as \(\delta\to\infty\),

\[
(\Lambda_L,\Lambda_K,\Lambda_H)\longrightarrow
\bigl(r-m+m\sqrt\alpha,\;r-m+m\alpha,\;r-m\bigr).
\]

These asymptotics are part of the same classification, not assertions about nonlinear persistence probabilities.

## Assumptions and scope

Take a simple, connected, undirected habitat graph \(G\) on \(n\) patches, and let \(A_G\) be its adjacency matrix and \(D_G\) the diagonal degree matrix. The row-stochastic transition matrix for uniform-neighbor emigration is \(P_G=D_G^{-1}A_G\). If \(e_d\) marks the one damaged patch, the nonnegative population vector \(x(t)\) satisfies

\[
\frac{d}{dt}x(t)=B_Gx(t),\qquad
B_G=rI-\delta e_de_d^{\mathsf T}+m(P_G^{\mathsf T}-I).
\]

The quantity \(\Lambda_G\) is the spectral abscissa of \(B_G\), equivalently its real simple Perron eigenvalue because \(B_G\) is an irreducible Metzler matrix. It determines the asymptotic exponential growth rate of every strictly positive initial vector. It does not by itself determine total abundance at each finite time, nonlinear carrying-capacity equilibria, or extinction probabilities of a finite stochastic population. Graph comparisons hold at equal **total outgoing emigration per individual**, not equal emigration along each separate edge.

The three marked graph types are exactly a star with damaged leaf, a star with damaged hub, and a complete graph with one damaged vertex. For \(n=3\), these enumerate every connected three-patch simple network with one distinguished damaged patch. For \(n>3\), they compare two specified graph families, not every connected graph.

## Proof

**1. Positive reduced roots.** Subtract the scalar \((r-m)I\) and divide by \(m\). The shifted spectral parameter \(z=1+(\Lambda-r)/m\) is the Perron root of \(P_G^{\mathsf T}-q e_de_d^{\mathsf T}\), with \(q>0\). The transformed matrix is irreducible Metzler; a strictly positive Perron vector exists. Moreover the killing term forces its largest eigenvalue below \(1\). The positivity of the reduced roots follows from the explicit equations below.

For a damaged star leaf, let \(u\) denote the damaged-leaf eigenvector component, \(v\) any of the \(n-2\) healthy-leaf components and \(w\) the hub component. The eigen-equations are

\[
(z+q)u=\beta w,\quad zv=\beta w,\quad zw=u+(n-2)v.
\]

Eliminating \(u,v,w\) gives \(F_L(z)=z^3+qz^2-z-\alpha q=0\). Since \(F_L(\sqrt\alpha)=\sqrt\alpha(\alpha-1)<0\) and \(F_L(1)=q\beta>0\), the Perron root is \(z_L\in(\sqrt\alpha,1)\). The corresponding eigenvector components are all positive, identifying this root as the unique Perron root.

For a damaged complete graph, denote the damaged component by \(u\) and a common healthy component by \(v\). Then \((z+q)u=v\) and \((z-\alpha)v=\beta u\), giving \(F_K(z)=(z+q)(z-\alpha)-\beta=0\). Its positive Perron root lies strictly in \((\alpha,1)\). For a damaged star hub, the corresponding two equations yield \(F_H(z)=z(z+q)-1=0\), whose positive Perron root lies in \((0,1)\).

**2. Parameter-uniform strict ordering.** Put \(z=z_K\). The clique equation gives the exact substitution

\[
q=\frac{(1-z)(z+\beta)}{z-\alpha},\qquad \alpha<z<1.
\]

Direct substitution (no approximation) yields the two factorization identities

\[
F_L(z)=\frac{\alpha\beta(z-1)}{z-\alpha}<0,
\qquad F_H(z)=\frac{\alpha(1-z)}{z-\alpha}>0.
\]

Because \(F_L(1)>0\), it has a positive root above \(z_K\). Such a root is necessarily at most the Perron root \(z_L\), and hence \(z_L>z_K\). Since \(F_H\) is strictly increasing on \((0,\infty)\) and vanishes at \(z_H\), the positive value \(F_H(z_K)>0\) implies \(z_K>z_H\). The map \(z\mapsto r+m(z-1)\) is strictly increasing. This establishes the displayed ordering for every \(n\ge3\), \(q>0\), and \(m>0\).

**3. Boundary laws.** At \(q=0\), all reduced Perron roots equal \(1\). Implicit differentiation at \((z,q)=(1,0)\) gives, respectively, \(dz_L/dq=-\beta/2\), \(dz_K/dq=-1/n\), and \(dz_H/dq=-1/2\), proving the small-\(\delta\) expansions. The limit \(q\to\infty\) in the displayed reduced equations yields \(z_L\to\sqrt\alpha\), \(z_K\to\alpha\), and \(z_H\to0\). The limits are unique in the established positive-root intervals; substituting back into \(\Lambda_i=r+m(z_i-1)\) proves the remaining formulas.

## Verification

Run `python3 check.py` from this directory with Python 3 and NumPy installed. The checker independently constructs the full migration-growth matrices for selected graph orders and mortality ratios and compares their numerical spectral abscissas to the reduced equations. It also checks the two key factorization identities using exact rational arithmetic, evaluates strict orders over a grid, and checks both asymptotic regimes. Its computations are supplementary; the universal quantifiers follow from the analytic proof, not the finite grid.

For the reproducible example \(n=5\), \(r=0\), \(m=\delta=1\), the reduced roots are approximately \(z_L=0.933099131255\), \(z_K=0.882782218537\), and \(z_H=0.618033988750\). The corresponding growth exponents are approximately \(-0.066900868745\), \(-0.117217781463\), and \(-0.381966011250\).

## Relationship to prior work

Suzuki and Economo (2024) use degree-normalized dispersal and compare the influence of metacommunity network topology, but their main response is biomass variability in a stochastic multispecies competition model, rather than this single-damaged-patch Perron eigenvalue. Nakagiri and colleagues (2024) explicitly investigate a three-patch hub effect and report that extra corridors can harm population outcomes; the qualitative three-patch corridor warning is **not claimed as new**. The present statement provides a strict, parameter-uniform comparison for every star size \(n\ge3\), both damaged-star placements and the complete graph, together with explicit weak- and strong-damage limits. Aldous and Fill describe stationary distributions, transition behavior and hitting times for star and complete-graph walks; those classical facts explain the weak-damage slopes but do not, on their own, state the finite-damage comparison established here.

## Limitations

Priority has been assessed only against inspected published material and accessible indexed statements, not the entire literature. The complete text of the especially relevant 2024 three-patch metapopulation article was unavailable; its public abstract and section excerpts were inspected. The proof concerns deterministic low-density linear growth under equal per-capita emigration. It does not establish a corresponding inequality for nonlinear equilibria, finite-time total biomass, stochastic extinction risk or graphs outside the two graph families. Equality arises at the excluded no-damage boundary \(\delta=0\); the theorem does not include that boundary in its strict claim.

## References

1. Suzuki, Y. and Economo, E. P., “The Stability of Competitive Metacommunities Is Insensitive to Dispersal Connectivity in a Fluctuating Environment,” *The American Naturalist* 203 (2024), https://doi.org/10.1086/729601. First published online 12 April 2024. In particular, the network-normalized emigration model in the Methods.
2. Nakagiri, N., Yokoi, H., Morishita, A. and Tainaka, K., “Three-lattice metapopulation model: Connecting corridor between patches may be harmful due to ‘hub effect’,” *Ecological Complexity* 59 (2024), 101090, https://doi.org/10.1016/j.ecocom.2024.101090. Public preview provides abstract and section excerpts; full text not inspected.
3. Aldous, D. and Fill, J. A., *Reversible Markov Chains and Random Walks on Graphs*, chapter 5.2, “Special graphs,” online draft, https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch5.S2.html. Background on complete-graph and star random walks and their stationary measures.
