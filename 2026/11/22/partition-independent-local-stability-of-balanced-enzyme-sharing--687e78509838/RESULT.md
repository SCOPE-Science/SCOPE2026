# Partition-independent local stability of balanced enzyme-sharing cycles

## Finding
For any integer \(n\ge 3\), partition the reactions in the directed substrate ring \(X_0\to X_1\to\cdots\to X_{n-1}\to X_0\) into an arbitrary nonempty set of enzyme pools. Each reaction has a one-complex Henri–Michaelis–Menten mechanism, and every reaction has the same positive association, dissociation, and catalytic rate constants. In every positive conservation class admitting a *balanced equilibrium* (identical substrate and complex concentrations at all reactions and identical free-enzyme concentration in all pools), that equilibrium is locally exponentially asymptotically stable relative to its stoichiometric compatibility class. This holds for every enzyme-assignment partition, including highly uneven sharing. In particular, a Hopf bifurcation cannot occur at any of these balanced equilibria while the rates and conserved totals vary within this balanced family.

The conclusion concerns full mass-action dynamics with all complexes retained. It does not assert global convergence or exclude instability at unbalanced equilibria outside the stated family.

## Assumptions and scope
Let \(i\in\mathbb Z/n\mathbb Z\), let \(\pi\) map reaction indices onto \(q\ge 1\) enzyme pools, and write \(m_g=|\pi^{-1}(g)|\). Reaction \(i\) is
\[
X_i+E_{\pi(i)} \mathrel{\mathop{\rightleftarrows}^{k_+}_{k_-}} C_i
\xrightarrow{\,k_c\,}X_{i+1}+E_{\pi(i)},
\]
where \(k_+,k_-,k_c>0\) are common to all \(n\) reactions. The conserved substrate total is \(M=\sum_i(X_i+C_i)\); the conserved total of pool \(g\) is \(T_g=E_g+\sum_{\pi(i)=g}C_i\). All species concentrations are positive.

Fix any \(e,c>0\), put \(h=k_-+k_c\), and choose \(x=hc/(k_+e)>0\), \(M=n(x+c)\), and \(T_g=e+m_gc\). These totals define a positive compatibility class containing the balanced equilibrium \(X_i=x,\ C_i=c,\ E_g=e\). Conversely, every balanced equilibrium with common positive free enzyme, substrate and complex concentrations has this form. The dimension of the substrate-complex compatibility manifold is \(2n-1\) after enzyme conservation laws are eliminated.

## Proof
Set \(y_i=X_i+C_i\), \(z_i=C_i\), and eliminate free enzymes by \(E_g=T_g-\sum_{\pi(j)=g}z_j\). Direct mass-action bookkeeping gives
\[
\dot y_i=k_c(z_{i-1}-z_i),\qquad
\dot z_i=k_+\left(T_{\pi(i)}-\sum_{\pi(j)=\pi(i)}z_j\right)(y_i-z_i)-hz_i.
\]
Substituting the balanced state makes each reaction flux \(k_+ex=hc\), so it is an equilibrium.

Write \(\alpha=k_+e>0\), \(\beta=k_+x>0\), \(\kappa=k_c>0\). Let \(S\) be the backward cyclic permutation \((Sz)_i=z_{i-1}\), and let \(B_{ij}=1\) when \(\pi(i)=\pi(j)\), zero otherwise. Because \(B=GG^\top\), where \(G_{ig}=1\) precisely for \(\pi(i)=g\), the matrix \(B\) is positive semidefinite. Put \(H=(\alpha+h)I+\beta B\). In the \((y,z)\) coordinates, the full reduced Jacobian is
\[
J=\begin{pmatrix}0&\kappa(S-I)\\ \alpha I&-H\end{pmatrix}.
\]
Thus \(H\) is real symmetric and \(H\succeq(\alpha+h)I\).

Suppose \(\lambda\) is an eigenvalue with real part \(u\ge0\). For its nonzero complex eigenvector \((y,z)\), one has \(z\ne0\), since \(\alpha y=0\) would otherwise force \(y=0\). Eliminating \(y\) (including when \(\lambda=0\), by multiplying through) yields
\[
[\lambda^2I+\lambda H+\alpha\kappa(I-S)]z=0.
\]
The Hermitian inner product with \(z\), divided by \(\lVert z\rVert^2\), yields
\[
\lambda^2+\eta\lambda+\alpha\kappa\zeta=0,\qquad
\eta=\frac{\langle z,Hz\rangle}{\lVert z\rVert^2}\ge\alpha+h,
\quad
\zeta=1-\frac{\langle z,Sz\rangle}{\lVert z\rVert^2}.
\]
Since \(S\) is unitary, \(|1-\zeta|\le1\), hence \(\operatorname{Re}\zeta\ge0\) and \((\operatorname{Im}\zeta)^2\le2\operatorname{Re}\zeta\).

Write \(\lambda=u+iv\). If \(v\ne0\), comparison of real and imaginary parts and the disk inequality gives
\[
\frac{v^2(2u+\eta)^2}{\alpha^2\kappa^2}
\le\frac{2(v^2-u(u+\eta))}{\alpha\kappa}
\le\frac{2v^2}{\alpha\kappa},
\]
so \((2u+\eta)^2\le2\alpha\kappa\). But \(\eta\ge\alpha+h\), and since \(h=k_-+\kappa>\kappa\), the arithmetic–geometric mean inequality gives \((\alpha+h)^2\ge4\alpha h>4\alpha\kappa>2\alpha\kappa\). This is impossible.

If \(v=0\), then \(\operatorname{Re}\zeta=-u(u+\eta)/(\alpha\kappa)\) forces \(u=0\). Thus the only possible eigenvalue in the closed right half-plane is zero. At \(\lambda=0\), the first block equation gives \((I-S)z=0\), so \(z=t\boldsymbol 1\). The second block equation gives \(y=Hz/\alpha\). Consequently
\[
\sum_i y_i=\frac{t}{\alpha}
\left(n(\alpha+h)+\beta\sum_gm_g^2\right).
\]
The conservation tangent space requires \(\sum_i y_i=0\), so \(t=0\); zero is not an eigenvalue restricted to that tangent space. All eigenvalues of the restricted Jacobian have strictly negative real parts. Standard smooth finite-dimensional linearization gives local exponential attraction within the positive compatibility class, completing the proof.

## Verification
The standalone standard-library script `checker.py` independently reconstructs the mass-action vector field from the conserved totals and compares its exact rational central-difference Jacobian to the stated block matrix at \(126\) balanced cases: \(n=3,\ldots,9\); distinct, pooled, periodic and uneven pool assignments; and three different positive rational rate sets. Its \(20{,}160\) matrix-entry comparisons are exact. This numerically finite consistency check does not establish stability; the spectral argument above proves the statement for every \(n\), partition, and positive rate set in scope.

Run: `python checker.py`.

## Relationship to prior work
Joshi and Nguyen, *Substrate hypergraph cycles: unique steady states and persistence for every enzyme assignment; oscillations enabled by enzyme sharing* (arXiv:2611.02523v1, first public 2026-11-02), prove existence, uniqueness, and persistence for arbitrary HMM substrate cycles, global convergence without enzyme sharing, and Hopf oscillations for certain shared-enzyme assignments. Their Theorems 1.1–1.3 do not provide a uniform-rate balanced local-stability criterion across every partition. The present statement supplies this parameter-and-conservation restriction and does not contradict their instability examples at other kinetic or total-enzyme parameters.

Donnell and Banaji, *Local and Global Stability of Equilibria for a Class of Chemical Reaction Networks* (arXiv:1211.2153), give a structural global-stability approach under special stoichiometric factorization assumptions. Joshi and Nguyen explicitly note that the factorization does not generally hold under enzyme sharing, so that older theorem does not by itself imply the all-partition result here. General symmetry or circulant diagonalization alone does not handle nonuniform enzyme-sharing partitions; the positive-semidefinite incidence Gram matrix is the key extra structural ingredient.

## Limitations
Only one-intermediate, one-substrate-per-step closed cycles are considered, with identical association, dissociation, and catalytic rates and with free enzymes equal at the balanced equilibrium. Enzyme totals may differ according to pool size, as specified. No global convergence, absence of other recurrent dynamics, quantitative uniform spectral gap, or robustness under arbitrary rate heterogeneity is claimed. The calculation does not address enzyme-free reactions, multireactant hyperedges, or chains of intermediates. Historical priority of an equivalent all-partition Gram-matrix criterion is a residual literature risk.

## References
1. B. Joshi and T. D. Nguyen, *Substrate hypergraph cycles: unique steady states and persistence for every enzyme assignment; oscillations enabled by enzyme sharing*, arXiv:2611.02523v1 (2026-11-02). https://arxiv.org/html/2611.02523v1
2. P. Donnell and M. Banaji, *Local and Global Stability of Equilibria for a Class of Chemical Reaction Networks*, arXiv:1211.2153v2 (2013). https://arxiv.org/abs/1211.2153
