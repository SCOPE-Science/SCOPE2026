# Exact fastest symmetric mixing through a partial matching between two cliques

## Finding
Let \(m,k\) be integers with \(2\le k\le m/2\). Form a connected graph \(G_{m,k}\) from two disjoint copies of \(K_m\) by adding a matching of exactly \(k\) inter-clique edges. Among all real symmetric entrywise-nonnegative row-stochastic matrices \(P\) whose nonzero off-diagonal entries are supported on \(G_{m,k}\), with self-loops permitted, the minimum centered spectral norm (second-largest eigenvalue modulus) is
\[
\rho_*(m,k)=\frac{m-4k+2\sqrt 2\,k}{m+2k-2\sqrt 2\,k}
=1-\frac{(6-4\sqrt2)k}{m+(2-2\sqrt2)k}.
\]
An explicit globally optimal kernel is specified below. In particular, the exact optimal spectral gap depends only on the bridge-density ratio \(k/m\), and is asymptotic to \((6-4\sqrt2)k/m\) whenever \(k=o(m)\). The result concerns spectral-norm mixing of symmetric chains, not arbitrary nonreversible chains or total-variation mixing times.

## Assumptions and scope
The two cliques each contain \(m\) vertices. Within each clique, designate \(k\) *gateway* vertices, each incident to exactly one matching edge, and \(r=m-k\) *peripheral* vertices, incident to no inter-clique edge. The matching pairs gateways on opposing sides. Define
\[
H=(1+\sqrt2)m-2k,\qquad
b=\frac{\sqrt2}{H},\qquad
c=1-rb,\qquad
d=\frac{1-kb}{r}.
\]
For the claimed kernel, assign probability \(c\) on each matching edge, \(b\) on every gateway–peripheral edge within each clique, \(d\) on every distinct peripheral–peripheral edge within each clique, and zero on every distinct gateway–gateway edge. Choose diagonal holding probabilities to make each row sum to one. In particular, gateway holding probabilities are zero and peripheral holding probabilities equal \(d\). Since \(m\ge2k\), one has \(H>0\), \(0<mb\le1\), \(rb\ge1/2\), \(0<c\le1/2\), and \(d>0\). Thus this is a valid symmetric stochastic matrix. Graph edges may legitimately receive zero probability.

For any admissible \(P\), set \(\rho(P)=\lVert P-\mathbf1\mathbf1^{\mathsf T}/(2m)\rVert_2\). We minimize over all such \(P\), including those with no symmetry in the assigned probabilities.

## Proof
**1. Symmetry reduction.** The permutation group permuting the \(k\) matched gateway pairs simultaneously, permuting the peripheral vertices independently within each clique, and exchanging the two cliques acts by graph automorphisms. The feasible set is convex and invariant under this action. The map \(P\mapsto\lVert P-\mathbf1\mathbf1^{\mathsf T}/(2m)\rVert_2\) is convex and invariant under conjugation by permutations. Averaging any feasible matrix over this finite group therefore cannot increase its objective. Hence a global optimizer exists with constant gateway–peripheral probability \(x\) and matching-edge probability \(y\). Row nonnegativity forces
\[x\ge0,\quad y\ge0,\quad rx+y\le1,\quad kx\le1.\]
The unneeded other orbit weights need not be fixed when deriving a lower bound.

**2. A four-dimensional invariant subspace and the lower bound.** Consider vectors constant on the gateway and peripheral classes separately on each side. The subspace odd under exchange of cliques is two-dimensional; in the orthonormal class-indicator basis, its restriction is
\[
B_-(x,y)=\begin{pmatrix}1-rx-2y&\sqrt{kr}\,x\\\sqrt{kr}\,x&1-kx\end{pmatrix}.
\]
This block is orthogonal to the constant vector, so \(\rho(P)\) is at least its larger eigenvalue, \(\lambda_+(x,y)\). Increasing \(y\) decreases \(B_-\) in the positive-semidefinite order, hence cannot increase \(\lambda_+\). Thus, writing \(A=m^2+4mk-4k^2\),
\[
\rho(P)\ge\lambda_+(x,y)\ge\lambda_+(x,1-rx)
=f(x):=\frac{(m-2k)x+\sqrt{4-4mx+Ax^2}}2
\]
for \(0\le x\le1/r\); the condition \(kx\le1\) is automatically satisfied because \(r\ge k\).

**3. Strict one-dimensional minimization.** The quadratic inside the square root is positive for all real \(x\), since \(A-m^2=4k(m-k)>0\). Direct differentiation gives
\[
f'(x)=\frac{m-2k}{2}+\frac{Ax-2m}{2\sqrt{4-4mx+Ax^2}},\qquad
f''(x)=\frac{2(A-m^2)}{(4-4mx+Ax^2)^{3/2}}>0.
\]
The point \(b=\sqrt2/[(1+\sqrt2)m-2k]\) lies in \((0,1/r)\), and substitution shows
\[
4-4mb+Ab^2=2,\qquad Ab-2m=-\sqrt2(m-2k).
\]
Therefore \(f'(b)=0\), and strict convexity makes \(b\) the unique minimizer of \(f\). Its minimum is
\[
f(b)=\frac{(m-2k)b+\sqrt2}{2}=\frac{m-4k+2\sqrt2\,k}{m+2k-2\sqrt2\,k}=:\rho_*.
\]
This establishes a universal lower bound for all admissible matrices.

**4. Attainment and all other eigenmodes.** At the specified kernel, the gateway-local zero-sum subspaces have eigenvalues \(+c\) and \(-c\), each of multiplicity \(k-1\); the peripheral-local zero-sum subspaces have eigenvalue zero with total multiplicity \(2(r-1)\). The even class-constant subspace has eigenvalues \(1\) and \(1-mb\). The odd class-constant subspace has eigenvalues
\[
\mu_{\pm}=\frac{(m-2k)b\pm\sqrt2}{2}.
\]
These multiplicities total \(2m\). Since \(m\ge2k\), their sum \(\mu_++\mu_-=(m-2k)b\ge0\), whence \(|\mu_-|\le\mu_+=\rho_*\). The inequalities \(rb\ge1/2\), \(mb\le1\), and \(mb\ge rb\) give \(0<c\le1/2\) and \(0\le1-mb\le1/2\). Finally, \(\rho_*\ge1/\sqrt2>1/2\) (because \(\mu_+=((m-2k)b+\sqrt2)/2\)). Thus every nonconstant eigenvalue is in \([-\rho_*,\rho_*]\), with \(\mu_+=\rho_*\), attaining the lower bound. This proves global optimality.

## Verification
Run `python verify.py` with Python 3. The standalone program constructs the claimed matrices, separately diagonalizes them using a Jacobi algorithm, checks the complete predicted spectrum for 67 integer pairs, checks stochasticity and nonnegativity, and checks the scalar lower bound over 8,405 feasible grid points. It also checks parameter identities for 437 integer pairs. Its printed success marker is `VERIFY_OK`. These finite checks support but do not substitute for the infinite-family proof above.

## Relationship to prior work
Boyd, Diaconis and Xiao formulated fastest symmetric mixing as a convex semidefinite program; Boyd, Diaconis, Parrilo and Xiao developed general group-symmetry reductions. Those results supply the framework but not the explicit partial-matching formula above. Allison and Shader analyzed unions of overlapping cliques, not the graph here with two disjoint cliques and \(k\ge2\) independent matching bridges. Olesker-Taylor and Zanetti discuss complete cliques joined by a *full* matching (the case \(k=m\), outside our domain), obtaining mixing-order results, not this partial-matching exact optimum. Jafarizadeh treats clique-lifts including barbells with a single linking edge; our graph has at least two independently paired linking edges and does not reduce by that one-bridge formula. No inspected source supplies a stronger formula implying the displayed one. This is an originality assessment based on consulted material, not proof of publication priority.

## Limitations
The proof covers only \(2\le k\le m/2\), symmetric stochastic kernels with unrestricted holding and possible zero weights on allowed edges. It does not classify all optimizing kernels, does not cover \(k>m/2\), and does not optimize nonreversible or nonuniform-stationary chains. Publication-priority uncertainty remains from unindexed literature and an inaccessible full text by Allison and Shader (2011). Independent validation has not been performed.

## References
- S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, https://doi.org/10.1137/S0036144503423264.
- S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (public September 6, 2007), https://arxiv.org/abs/0709.0955; SIAM J. Optim. 20 (2009), 792–819.
- M. Allison, B. L. Shader, *Fastest mixing Markov chain problem for the union of two cliques*, Linear and Multilinear Algebra 59 (2011), 801–823, https://doi.org/10.1080/03081087.2010.538690.
- S. Olesker-Taylor, L. Zanetti, *Geometric bounds on the fastest mixing Markov chain*, Probab. Theory Relat. Fields 188 (2024), 1017–1062, https://doi.org/10.1007/s00440-023-01257-x.
- S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, arXiv:2501.02421 (2025), https://arxiv.org/abs/2501.02421.
