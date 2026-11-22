# Sharp sparse-branching transient law for diagonally dominant triangular Jacobi solves

## Finding

**Theorem (exact finite-dimensional worst-case residual law).** Fix integers \(n\ge2\), \(d\ge1\), \(1\le k<n\), and a real dominance bound \(0<\tau<1\). Let \(\mathcal G(n,d,\tau)\) consist of real strictly lower-triangular \(n\times n\) matrices \(G\) satisfying
\[
\sum_{j<i}|G_{ij}|\le\tau\quad(1\le i\le n),\qquad
\#\{i:G_{ij}\ne0\}\le d\quad(1\le j\le n).
\]
Set
\[
S_{d,k}(m)=\sum_{j=0}^{k}\left\lceil\frac{m}{d^j}\right\rceil,\qquad
M_{n,d,k}=\max\{m\in\{1,\ldots,d^k\}:S_{d,k}(m)\le n\}.
\]
The maximum defining \(M_{n,d,k}\) is nonempty because \(n\ge k+1\). Because \(S_{d,k}(m)\) is increasing, the exact value of \(M_{n,d,k}\) is computable by integer binary search; no graph enumeration is required. If \(T=I-G\) and the zero-start Jacobi approximation for \(Tx=b\) is
\[
x^{(k)}=\sum_{j=0}^{k-1}G^jb,
\]
then
\[
\boxed{\max_{G\in\mathcal G(n,d,\tau)}\sup_{b\ne0}
\frac{\|b-Tx^{(k)}\|_2}{\|b\|_2}
=\tau^k\sqrt{M_{n,d,k}}.}
\]
The extremum is attained by a nonnegative, one-parent-per-row rooted forest. In particular, the worst-case \(k\)-sweep residual grows above the initial Euclidean residual precisely when \(\tau^{2k}M_{n,d,k}>1\). At fixed \(d,\tau,k\), the smallest dimension with this behavior is
\[
n_{\min}=\sum_{j=0}^{k}\left\lceil\frac{m_*}{d^j}\right\rceil,
\qquad m_*=\lfloor\tau^{-2k}\rfloor+1,
\]
provided \(m_*\le d^k\); otherwise no dimension permits amplification at that sweep count. Across all dimensions and sweep counts, universal Euclidean residual nonexpansion holds exactly when \(\tau\sqrt d\le1\).

For example, let \(d=2\), \(\tau=3/4\), \(k=2\), and \(n=7\). Put \(G_{2,1}=G_{3,1}=G_{4,2}=G_{5,2}=G_{6,3}=G_{7,3}=3/4\), all other entries zero, and let \(b=e_1\). Then the row dominance ratios are at most \(3/4\), each column contains at most two nonzeros, but the exact two-sweep residual satisfies
\[
\frac{\|b-(I-G)x^{(2)}\|_2}{\|b\|_2}
=\|G^2e_1\|_2=\frac98>1.
\]
After at most \(n\) sweeps the residual is exactly zero, because \(G\) is nilpotent.

## Assumptions and scope

The result concerns finite-dimensional **real** triangular systems with a unit diagonal, zero Jacobi initial iterate, a bound on *absolute row sums*, and a maximum of \(d\) off-diagonal entries in every **column**. The column bound is distinct from row sparsity. There is no assumption of symmetry, positive definiteness, random right-hand sides, or positivity of the matrix entries. Arithmetic and residuals are exact. The upper dominance bound is inclusive; \(0<\tau<1\) makes every \(T=I-G\) strictly row-diagonally dominant and invertible.

## Proof

**1. Exact residual.** Multiplying the finite Neumann sum by \(I-G\) gives
\[
(I-G)\sum_{j=0}^{k-1}G^j=I-G^k.
\]
Therefore \(b-Tx^{(k)}=G^kb\), and the worst-right-hand-side amplification is \(\|G^k\|_2\).

**2. Reduction to nonnegative one-parent matrices.** Given a permissible \(G\), put \(H=|G|\) entrywise. As \(|G^k|\le H^k\) entrywise, for every real vector \(z\),
\[
\|G^kz\|_2\le\|H^k|z|\|_2\le\|H^k\|_2\|z\|_2.
\]
It is therefore enough to maximize over nonnegative \(H\). Each row of such an \(H\), when its original support is fixed, lies in a simplex of nonnegative weights with total at most \(\tau\).

Fix all other rows, and vary a single row \(i\). Every directed path from column to row in a strictly lower-triangular matrix has strictly increasing vertex indices; it visits vertex \(i\) at most once. In the path expansion of \(H^k\), each monomial consequently uses at most one entry from row \(i\). Thus \(H^k\) is **affine** in that row while the other rows are held fixed. Since the spectral norm of an affine matrix-valued function is convex, its maximum on the row simplex occurs at a vertex. Such a vertex is the zero row or a row containing just one weight \(\tau\), supported in one of the original permitted columns. Replacing the rows successively by maximizing simplex vertices never decreases \(\|H^k\|_2\), never introduces a new nonzero position, and therefore never breaches the original maximum-column-sparsity constraint. Thus a nonnegative matrix \(P\), with at most one nonzero per row and every nonzero equal to \(\tau\), attains at least as large a power norm as \(G\).

**3. Forest norm.** Interpret each nonzero \(P_{ij}=\tau\), where \(j<i\), as a directed parent relation from parent \(j\) to child \(i\). Each vertex has at most one parent and at most \(d\) children, so the directed graph is a rooted forest with increasing labels away from its roots. The entry \((P^k)_{ij}\) is exactly \(\tau^k\) when \(j\) is the \(k\)-th ancestor of \(i\), and zero otherwise. Each row of \(P^k\) has at most one nonzero, hence distinct columns are orthogonal. If \(m_j\) counts the vertices at exact distance \(k\) below \(j\), then
\[
(P^k)^{\mathsf T}P^k=\tau^{2k}\operatorname{diag}(m_1,\ldots,m_n),
\quad \|P^k\|_2=\tau^k\sqrt{\max_jm_j}.
\]

**4. Exact depth budget.** A vertex with \(m\) descendants at distance exactly \(k\) needs at least \(\lceil m/d\rceil\) parents of these descendants, at least \(\lceil m/d^2\rceil\) vertices two levels up, and so forth, in addition to its \(m\) descendants. Because distinct tree levels are disjoint, it requires at least \(S_{d,k}(m)\) vertices. Further \(m\le d^k\). It follows that \(m\le M_{n,d,k}\).

Conversely, for any positive \(m\le d^k\) with \(S_{d,k}(m)\le n\), construct a tree with exactly \(\lceil m/d^j\rceil\) vertices in generation \(k-j\) for each \(0\le j\le k\). For every adjacent pair of generations, assign each child to a parent in consecutive groups of size at most \(d\). The ceiling identity ensures enough parent capacity, and each non-root parent can be given a child. Number vertices by increasing generation and then append isolated vertices to reach dimension \(n\). The resulting parent matrix lies in \(\mathcal G(n,d,\tau)\) and has \(m\) descendants at distance \(k\) from its root. Taking \(m=M_{n,d,k}\) proves attainment and the sharp norm formula.

**5. Thresholds.** The integer \(m_*\) is the smallest descendant count satisfying \(\tau^{2k}m>1\). Monotonicity of \(S_{d,k}\) gives the minimal dimension above. Since \(M_{n,d,k}\le d^k\), \(\tau^k\sqrt{M_{n,d,k}}\le(\tau\sqrt d)^k\). A complete \(d\)-ary depth-\(k\) parent tree has \(m=d^k\) and attains the upper envelope in dimension \(\sum_{j=0}^kd^j\). Thus, if \(\tau\sqrt d>1\), even one sweep can amplify the residual for a sufficiently large tree, while if \(\tau\sqrt d\le1\), no sweep does.

## Verification

The accompanying `verify.py` is a standalone standard-library Python script. It enumerates every parent forest permitted by the chronological lower-triangular ordering for a finite range of small dimensions, independently computes all depth counts from parent chains, and checks the predicted optimum against the exact ceiling formula. It also verifies the exact rational seven-vertex, two-sweep example and the minimal-dimension arithmetic. These finite checks are supplementary; the proof above establishes the unrestricted result for all admissible \(n,d,k,\tau\).

To reproduce: `python verify.py` with Python 3.9 or later. No external data or libraries are required.

## Relationship to prior work

Dargaville and Pain [1] describe Jacobi/Neumann approximation to ILU triangular solves in their Section 4, including the exact identity for a truncated Neumann polynomial and the possibility of large transient norms despite nilpotency. Their Section 6.2 introduces a diagonal-dominance-controlled splitting, using an absolute off-diagonal row-sum ratio. They do not derive the present sharp finite-dimensional joint dependence on column branching, row dominance, and sweep count. The standard proof of diagonal-dominance Jacobi convergence bounds the maximum norm, not the sharp Euclidean norm of individual powers; see [2]. Saad [3] is a general reference for iterative sparse linear systems.

This result neither asserts that the paper's methods are incorrect nor establishes its graph degree cap for every ILU factor. The cap on column support is an explicit additional hypothesis to be checked for a concrete factor or subblock.

## Limitations

The theorem characterizes the worst-case **Euclidean inner residual after a fixed number of Jacobi sweeps**, not the exact error relative to \(T^{-1}b\), convergence of an outer Krylov solver, average-case residuals, or the running time on a GPU. The extremal matrices are artificial but admissible strictly diagonally dominant sparse triangular factors; no claim is made that they arise from a particular PDE ILU factorization. The exact spectrum of every such \(G\) is zero and the residual vanishes after at most \(n\) sweeps. An independent mathematical audit has not been performed.

## References

[1] S. Dargaville and C. C. Pain, *A comparison of parallel iterative methods for ILU triangular solves*, arXiv:2611.00552v1 (first public version, 2026-10-31), https://arxiv.org/abs/2611.00552 ; full text https://arxiv.cnoctave.top/pdf/2611.00552 .

[2] *Jacobi method*, traditional row-diagonal-dominance convergence theorem; overview https://en.wikipedia.org/wiki/Jacobi_method .

[3] Y. Saad, *Iterative Methods for Sparse Linear Systems*, 2nd ed., SIAM, 2003, cited by [1]; bibliographic reference only, not asserted to have been inspected in full.
