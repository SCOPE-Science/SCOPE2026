# Star rigidity and a four-vertex sign reversal for graph-pattern sparse approximate inverses

## Finding

Let \(T=(V,E)\) be a finite tree, let \(w_e>0\) be edge conductances, and let \(\mu>0\). Put \(A=\mu I+L_w\), with \((L_w)_{ii}=\sum_{k\sim i}w_{ik}\), and \((L_w)_{ij}=-w_{ij}\) on edges. Let \(B\) uniquely minimize \(\|AB-I\|_F^2\) over all real matrices supported on the diagonal and the edges of \(T\). Symmetry is *not* imposed on \(B\).

**Complete topology classification.** The optimal \(B\) is entrywise nonnegative for *every* choice of \(\mu>0\) and all positive edge weights if and only if \(T\) is a star (including the one-vertex tree). Regardless of topology, when all edge weights equal one, every allowed entry of \(B\) is strictly positive, for every \(\mu>0\). Thus weight heterogeneity is essential for sign loss, and four vertices are the minimum tree order exhibiting it.

**Exact computable local sign criterion.** For each column \(j\), put \(d_v=\mu+\sum_{k\sim v}w_{vk}\) and, for every neighbor \(i\sim j\), define
\[
s_i=\sum_{k\sim i,\ k\ne j}w_{ik}^{2},\qquad r_i=d_i^2+s_i,\qquad
V_j=\sum_{i\sim j}\frac{w_{ij}^2}{r_i},
\]
\[
D_j=d_j-\sum_{i\sim j}\frac{w_{ij}^2d_i}{r_i},\quad
E_j=\sum_{i\sim j}\frac{w_{ij}^2s_i}{r_i},\quad
\Delta_j=D_j^2+(1+V_j)E_j.
\]
Then \(D_j>0\), \(\Delta_j>0\), and
\[
B_{jj}=\frac{D_j}{\Delta_j},\qquad
B_{ij}=\frac{w_{ij}(d_iD_j-E_j)}{r_i\Delta_j}\quad(i\sim j),\qquad
B_{ij}=0\quad(i\not\sim j,\ i\ne j).
\]
Consequently, for any weighted tree the sign of each permitted offdiagonal entry is exactly the sign of \(d_iD_j-E_j\), without forming the optimal matrix or solving any dense inverse problem.

**Sharp four-vertex witness.** On the path \(1-2-3-4\), take \(\mu=1\), and successive conductances \((1,t,t)\), with \(t>0\). Then
\[
B_{1,2}=\frac{-t^4+6t^3+21t^2+14t+3}{13t^4+44t^3+85t^2+48t+9}.
\]
This coefficient crosses zero at exactly one positive \(t\), approximately \(8.6269993073\); at \(t=9\) it equals \(-7/2445\). Every nonstar tree contains an induced four-vertex path, and the negative sign survives when its remaining edges are given sufficiently small positive conductances. Therefore the topology classification is sharp.

## Assumptions and scope

All trees are finite, undirected, simple and connected; \(w_e\) and \(\mu\) are strictly positive real numbers. The support constraint allows \(B_{ij}\) only when \(i=j\) or \(\{i,j\}\in E\). The objective is the **right** Frobenius residual \(\|AB-I\|_F\), not a factorized approximate inverse, nonnegative-constrained least squares, a spectral-condition optimizer, or a symmetric-constrained optimizer. Since \(A\) is symmetric positive definite, the columnwise least-squares minimizers exist and are unique. No restriction is imposed on the number of tree vertices.

## Proof

**1. Exact columnwise solution.** Fix \(j\), write \(x_0=B_{jj}\), \(x_i=B_{ij}\) for \(i\sim j\), and set
\[
z=1-d_jx_0+\sum_{i\sim j}w_{ij}x_i.
\]
The absence of cycles means distinct neighbors of \(j\) have disjoint descendant sets at distance two. Thus the complete squared column residual is exactly
\[
\|AB_{\cdot j}-e_j\|_2^2=z^2+\sum_{i\sim j}\bigl[(w_{ij}x_0-d_ix_i)^2+s_ix_i^2\bigr].
\]
The normal equations for \(x_i\) give \(r_ix_i=w_{ij}(d_ix_0-z)\). Substituting this identity into the defining equation for \(z\) gives \((1+V_j)z=1-D_jx_0\). The remaining normal equation gives \(E_jx_0=D_jz\). Solving the last two equations yields \(x_0=D_j/\Delta_j\) and \(z=E_j/\Delta_j\), whence the stated formula for every \(x_i\).

Each \(d_i>w_{ij}\) and \(r_i\ge d_i^2\), so
\[
\sum_{i\sim j}\frac{w_{ij}^2d_i}{r_i}\le\sum_{i\sim j}\frac{w_{ij}^2}{d_i}<\sum_{i\sim j}w_{ij}<d_j.
\]
Hence \(D_j>0\); also \(E_j\ge0\), so \(\Delta_j>0\). The least-squares Hessian is positive definite because the restricted columns of invertible \(A\) are independent; the displayed critical point is therefore the unique global minimizer.

**2. Every weighted star is positive.** If \(j\) is the hub, then each neighbor is a leaf, so all \(s_i=0\), \(E_j=0\), and \(d_iD_j-E_j>0\). If \(j\) is a leaf, it has a single neighbor \(i\) joined by weight \(w\). Direct substitution yields
\[
d_iD_j-E_j=d_id_j-w^2>0,
\]
since both \(d_i\) and \(d_j\) exceed \(w\). The one-vertex case has \(B=\mu^{-1}\).

**3. Every unweighted tree is positive.** For unit conductances, \(d_i=\deg(i)+\mu\), \(s_i=\deg(i)-1\), \(r_i=d_i^2+s_i\). Because \(d_i\ge1+\mu\),
\[
(1+\mu)r_i-[(1+\mu)d_i+s_i]
=(1+\mu)d_i(d_i-1)+\mu s_i>0.
\]
Therefore, writing \(k=\deg(j)\),
\[
(1+\mu)D_j-E_j>(1+\mu)(k+\mu)-k=\mu(k+1+\mu)>0.
\]
Since \(d_i\ge1+\mu\) and \(D_j>0\), also \(d_iD_j-E_j>0\). The isolated-vertex case follows separately.

**4. Every nonstar tree admits sign loss.** A connected tree is a star if and only if its diameter is at most two. Any nonstar has a simple four-vertex path. Put conductances \((1,9,9)\) on that path and assign a common value \(\varepsilon>0\) to all remaining edges; choose \(\mu=1\). At \(\varepsilon=0\), the graph splits into the specified four-vertex path and isolated or smaller components. The full column least-squares normal-equation matrix is invertible even at this limit, as \(A\) remains positive definite, so each optimal coefficient depends continuously on \(\varepsilon\). The negative coefficient \(B_{1,2}=-7/2445\) persists for sufficiently small positive \(\varepsilon\). The rational expression for this coefficient follows by the formulas in Step 1. Its numerator has exactly one positive zero by Descartes' rule of signs applied to \(t^4-6t^3-21t^2-14t-3\), and changes from positive to negative. No tree of fewer than four vertices is a nonstar.

## Verification

The standalone file `verify_spai.py` evaluates the exact local formula using rational arithmetic and independently solves each sparse normal-equation problem by Gaussian elimination. It checks every labelled unweighted tree up to five vertices at three positive shifts, randomly generated positive weighted stars up to eight vertices, the four-vertex rational witness, and positive weighted extensions. It reports 13,257 successful exact-rational assertion groups. These finite checks verify the displayed algebra in tested instances; Steps 1–4 constitute the proof for all finite trees and positive real weights.

Run with `python3 verify_spai.py`. The only dependency is the Python standard library.

## Relationship to prior work

Classical sparse approximate inverse (SPAI) methods minimize a Frobenius residual using independent columnwise least-squares problems [1,2,3]. The present sign theorem concerns the optimizer with a fixed *graph-neighborhood* sparsity pattern, not the construction or convergence properties of adaptive SPAI/RSAI. Wang, Lawlor and Kale [4, Section 3.3, Theorem 3.7] prove a nonsingularity implication for a strictly diagonally dominant \(M\)-matrix **conditional on the resulting sparse approximate inverse being nonnegative**. That condition is not automatic: the four-vertex example here violates it despite strict diagonal dominance. The present star rigidity classification and local sign formula are not consequences of their conditional theorem. An additional static-pattern source [5] describes the columnwise minimization but does not furnish this sign classification.

## Limitations

The result does not state that a nonnegative approximate inverse is the most accurate *constrained nonnegative* preconditioner, nor that the sparse inverse is symmetric or optimizes spectral condition number. It does not classify graphs with cycles or characterize arbitrary nonsymmetric \(M\)-matrices. The exact rational crossing is for the stated one-parameter path family. Historical equivalent statements in unindexed or inaccessible publications cannot be excluded; priority should be checked independently before formal publication. The finite checker is not a general automated proof.

## References

1. N. I. M. Gould and J. A. Scott, *Sparse approximate-inverse preconditioners using norm-minimization techniques*, SIAM Journal on Scientific Computing, 1998. Full-text source: https://www.numerical.rl.ac.uk/media/people/nick-gould/GoulScot98_sisc.pdf
2. Z. Jia and W. Kang, *A residual based sparse approximate inverse preconditioning procedure for large sparse linear systems*, arXiv:1503.04500, first submitted 16 March 2015. https://arxiv.org/abs/1503.04500
3. R. M. Holland, A. J. Wathen and G. J. Shaw, *Sparse approximate inverses and target matrices*, SIAM Journal on Scientific Computing 26 (2005), published online 25 July 2006. https://doi.org/10.1137/030601132
4. K. Wang, O. Lawlor and L. V. Kale, *The nonsingularity of sparse approximate inverse preconditioning and its performance based on processor virtualization*, Section 3.3. https://charm.cs.illinois.edu/newPapers/05-21/sai.pdf
5. *Smoothing and regularization with modified sparse approximate inverses*, 2010. https://onlinelibrary.wiley.com/doi/10.1155/2010/930218
