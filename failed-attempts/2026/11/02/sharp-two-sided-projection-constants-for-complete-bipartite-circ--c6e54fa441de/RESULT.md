# Sharp two-sided projection constants for complete-bipartite circulation spaces

## Finding

Let \(m,n\ge 2\) be integers and identify the oriented real edge-flow space of the complete bipartite graph \(K_{m,n}\) with \(\mathbb R^{m\times n}\), equipped with its entrywise \(\ell_p\) norm. The circulation (cycle) subspace is
\[
 Z_{m,n}=\left\{X:\ \sum_{j=1}^n X_{ij}=0\ (1\le i\le m),\quad \sum_{i=1}^m X_{ij}=0\ (1\le j\le n)\right\}.
\]
For \(s\ge2\) let \(C_s=I_s-s^{-1}J_s\), and let \(Q_{m,n}(X)=C_mXC_n\). For **every** \(p\in[1,\infty]\), this one projection simultaneously minimizes the projection norm and the complementary projection norm among all linear projections \(P\) onto \(Z_{m,n}\):
\[
\boxed{\min_{P^2=P,\ \operatorname{range}P=Z_{m,n}}\|P\|_{p\to p}
=\|Q_{m,n}\|_{p\to p}=\|C_m\|_{p\to p}\|C_n\|_{p\to p},}
\]
\[
\boxed{\min_{P^2=P,\ \operatorname{range}P=Z_{m,n}}\|I-P\|_{p\to p}
=\|I-Q_{m,n}\|_{p\to p}.}
\]
In particular, for **both endpoints** \(p=1\) and \(p=\infty\), both independently sharp constants are explicit:
\[
\boxed{\|Q_{m,n}\|_{1\to1}=\|Q_{m,n}\|_{\infty\to\infty}=\frac{4(m-1)(n-1)}{mn},}\qquad
\boxed{\|I-Q_{m,n}\|_{1\to1}=\|I-Q_{m,n}\|_{\infty\to\infty}=1+\frac{2(m-1)(n-1)}{mn}.}
\]
At \(p=2\), both optimal norms are \(1\). At either endpoint, the difference between the two optimal costs is
\[
 \boxed{\frac{(m-2)(n-2)-2}{mn}.}
\]
Their values coincide exactly at the two parameter pairs \((m,n)=(3,4),(4,3)\). On larger bicliques the optimal circulation projection costs more than its complementary projection; on \(K_{2,n}\) and \(K_{3,3}\) it costs less. As both parts tend to infinity, the respective exact endpoint constants approach \(4\) and \(3\).

## Assumptions and scope

All graph edges are unweighted, and each edge is oriented from the first vertex part to the second. Edge flows have the **entrywise** real \(\ell_p\) norm \(\|X\|_p=(\sum_{ij}|X_{ij}|^p)^{1/p}\) for finite \(p\), with the largest absolute entry norm at \(p=\infty\). The incidence boundary operator records row sums at the first part and negative column sums at the second, so its kernel is exactly \(Z_{m,n}\). This space has dimension \((m-1)(n-1)\), with a basis formed by the \((m-1)(n-1)\) four-cycle flows \(E_{ij}-E_{in}-E_{mj}+E_{mn}\), for \(i<m,j<n\). Here \(E_{ij}\) denotes a coordinate edge matrix. A projection means a real-linear map \(P\) from the entire edge-flow space onto this fixed kernel, satisfying \(P(z)=z\) for \(z\in Z_{m,n}\), not a coordinate deletion on the transportation quotient and not a metric nearest-point map. No uniqueness over all norm-minimizing projections is asserted.

## Proof

**1. Double centering is a projection.** Since \(C_s^2=C_s\), the map \(Q(X)=C_mXC_n\) is idempotent. Every output has zero row and column sums. For every \(X\in Z_{m,n}\), its row and column means vanish, so \(QX=X\). Thus \(Q\) is a projection onto \(Z_{m,n}\). Its coefficients, with input cell \((k,l)\) and output cell \((i,j)\), are
\[
 Q_{(i,j),(k,l)}=(\mathbf 1_{i=k}-1/m)(\mathbf 1_{j=l}-1/n).
\]

**2. Symmetrization minimizes both norms.** The group \(S_m\times S_n\) acts by independently permuting rows and columns, preserving the kernel and acting by isometries for every entrywise \(\ell_p\) norm, including both endpoints. Given any projection \(P\) onto \(Z_{m,n}\), average its conjugates over this finite group to obtain \(\overline P\). Every conjugate has range in \(Z_{m,n}\) and fixes \(Z_{m,n}\), so the same is true of their average: it is again a projection onto the kernel. The triangle inequality gives simultaneously
\[
 \|\overline P\|_{p\to p}\le\|P\|_{p\to p},\qquad
 \|I-\overline P\|_{p\to p}\le\|I-P\|_{p\to p}.
\]
It suffices to prove that \(Q\) is the **only** projection onto the kernel commuting with all row and column permutations.

**3. Uniqueness of the equivariant projection.** Let \(R\) be an equivariant projection, and inspect \(Y=R(E_{11})\). The stabilizer \(S_{m-1}\times S_{n-1}\) of the input edge forces \(Y\) to take a constant value \(a\) at \((1,1)\), a constant \(b\) in the rest of row one, a constant \(c\) in the rest of column one, and a constant \(d\) in all remaining positions. As \(Y\in Z_{m,n}\), its row and column sums vanish:
\[
 b=-\frac{a}{n-1},\qquad c=-\frac{a}{m-1},\qquad
 d=\frac{a}{(m-1)(n-1)}.
\]
The entry pattern therefore equals a scalar multiple of \(Q(E_{11})\). Transitivity of the group on all input edges implies \(R=\gamma Q\) on the full coordinate basis, for some scalar \(\gamma\). Because \(R\) and \(Q\) both fix the nonzero subspace \(Z_{m,n}\), \(\gamma=1\). Hence \(\overline P=Q\) for every original projection \(P\). The two simultaneous norm inequalities in step 2 now prove **both** global minimality claims, for all \(p\in[1,\infty]\).

**4. Tensor factorization at every exponent.** Left multiplication by \(C_m\) acts on each of the \(n\) column vectors and has operator norm exactly \(\|C_m\|_{p\to p}\), by the definition of entrywise norms; similarly right multiplication by \(C_n\) has norm \(\|C_n\|_{p\to p}\) on the rows. Their composition is \(Q\), proving the product upper bound. For vectors \(u\in\mathbb R^m\) and \(v\in\mathbb R^n\), the rank-one matrix \(X=uv^\top\) satisfies \(QX=(C_mu)(C_nv)^\top\) and \(\|X\|_p=\|u\|_p\|v\|_p\) at every exponent, including infinity. Taking independent norm-maximizing unit vectors (which exist in finite dimensions) proves the reverse inequality, hence the exact product formula.

**5. Exact endpoints and crossing.** Put \(\alpha=(m-1)(n-1)/(mn)\). In each column of the matrix of \(Q\), the diagonal entry is \(\alpha\). The absolute contributions from the remaining cells in the same row, from the remaining cells in the same column, and from cells in neither are each **exactly** \(\alpha\), by the coefficient formula in step 1. Consequently each absolute column sum of \(Q\) is \(4\alpha\). For \(I-Q\) the diagonal entry is \(1-\alpha>0\), while the sum of off-diagonal absolute entries is \(3\alpha\). Thus every column has absolute sum \(1+2\alpha\). Both matrices are symmetric, so their \(\ell_\infty\) row-sum norms equal their \(\ell_1\) column-sum norms. Step 3 proves these are the least possible norms, not merely upper bounds. The difference \(2\alpha-1\) simplifies to \(((m-2)(n-2)-2)/(mn)\); since \(m,n\ge2\) are integers, the only equality cases are \((3,4)\) and \((4,3)\), and the sign gives all other cases. Taking \(m,n\to\infty\) yields \(4\) and \(3\).

**6. Hilbert endpoint.** The operator \(Q\) is symmetric and idempotent under the standard Euclidean inner product. It is therefore the orthogonal projection onto \(Z_{m,n}\); \(I-Q\) is the orthogonal projection onto its nonzero orthogonal complement. As \(m,n\ge2\), both subspaces are nonzero, so both Euclidean operator norms equal \(1\). Their minimality follows from step 3 (or directly from the nonzero idempotent lower bound).

## Verification

The standalone file `verify_projection.py` uses only the Python standard library with exact rational arithmetic. Running `python verify_projection.py` prints `CHECK_OK 71 exact full-matrix cases including idempotence, cycles, row/column constraints, symmetry, and endpoint norms`. It constructs the entire operator matrix rather than assuming the target norm values, and checks the asserted identities and cycle-space invariance over 71 parameter pairs. These finite computations are consistency tests; all parameter ranges and all real \(\ell_p\) exponents follow from the analytical symmetry, matrix-coefficient, and rank-one arguments above.

## Relationship to prior work

The graph-flow / Lipschitz-free viewpoint and averaging over finite automorphism groups are established in Dilworth, Kutzarova and Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1 (2018); its Section 5.1 explicitly treats a two-vertex bipartition, so that **boundary case is not claimed as novel**. The same authors' *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (2023), treats minimal cycle-space projections and representation methods, focusing particularly on discrete tori and Hamming graphs. Their inspected theorems do not state the **simultaneous** sharp projection and complementary norms for all complete-bipartite graphs of arbitrary two-part sizes. Published exact results about Euclidean Banach–Mazur distances for complete-bipartite **transportation quotients** concern a different Banach-space invariant; likewise, suppression projections on cactus-graph quotient bases act on a different target. The distinctive claims here are the uniform two-sided minimization, the exact endpoint pair, and the arithmetic crossover for \(m,n\ge3\), together with all-exponent tensor factorization.

## Limitations

The result applies to the canonical **unweighted** complete-bipartite edge space with entrywise real \(\ell_p\) norms and the oriented circulation kernel. It does not classify weighted edge norms, arbitrary bipartite graphs, or all individual optimal projections. The exponents are \(1\le p\le\infty\); no quasi-Banach range is claimed. For intermediate \(p\), the projection norm is factored into two exact one-coordinate centering norms, while no elementary closed formula for the complementary norm is asserted. Earlier, differently worded computations for matrices with zero row and column sums may exist; an independent bibliographic review has not been completed.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1, first public 2018-07-10, https://arxiv.org/abs/1807.03814.
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, first public 2023-05-21, https://arxiv.org/abs/2305.12582.
