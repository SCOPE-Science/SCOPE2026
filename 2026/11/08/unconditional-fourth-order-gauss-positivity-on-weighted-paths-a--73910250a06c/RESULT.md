# Unconditional fourth-order Gauss positivity on weighted paths: a four-vertex cutoff

## Finding

**Theorem.** Let \(n\ge2\) be an integer and let \(w_1,\ldots,w_{n-1}\) be arbitrary strictly positive real conductances on the successive edges of the undirected path \(P_n\). Its combinatorial weighted Laplacian \(L\) has entries \(L_{ii}=w_i+w_{i+1}\) with missing boundary weights interpreted as zero, and \(L_{i,i+1}=L_{i+1,i}=-w_{i+1}\) for zero-based indices \(i=0,\ldots,n-2\). The completed two-stage, fourth-order Gauss--Legendre Runge--Kutta end-step for graph heat flow is
\[
T(h)=F(hL),\qquad F(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad h\ge0.
\]
The following conditions are equivalent:

1. \(T(h)\) is entrywise nonnegative for every \(h\ge0\).
2. One of these mutually exclusive possibilities holds:
   - \(n=2\), with any positive conductance;
   - \(n=3\), with \(\frac12\le w_2/w_1\le2\);
   - \(n=4\), with \((w_1,w_2,w_3)=a(1,2,1)\) for some \(a>0\).

In each permitted case every entry of \(T(h)\) is strictly positive for every \(h>0\). For any other positive path conductances, at least one adjacent off-diagonal entry is strictly negative for all sufficiently large \(h\).

## Assumptions and scope

The path is finite and connected, conductances are symmetric and strictly positive, the state evolves by \(u'=-Lu\), and the question concerns the *completed* Runge--Kutta end-step, not positivity of intermediate stages. No normalization of total edge weight is imposed: scaling every conductance merely rescales \(h\). There are no restrictions on the positive timestep. The assertion covers real weights, not only rational ones.

## Proof

**Step 1: the large-step obstruction.** Let \(\mathbf1\) be the all-ones vector and \(J=\mathbf1\mathbf1^\mathsf{T}/n\). Since the spectrum of \(L\) consists of zero and strictly positive real eigenvalues, \(K=L^+\), its Moore--Penrose inverse, satisfies
\[
T(h)=I-\frac{12}{h}K+O(h^{-2})\quad(h\to\infty).
\]
This follows by applying \(F(h\lambda)=1-12/(h\lambda)+O(h^{-2})\) separately to every positive eigenvalue and observing \(F(0)=1\). Consequently, if \(K_{ij}>0\) for distinct vertices, then \(T(h)_{ij}<0\) for all sufficiently large \(h\). Universal positivity therefore requires \(K_{ij}\le0\) for all distinct vertices.

**Step 2: exact adjacent Green-function signs.** Put \(r_k=1/w_k>0\), where edge \(k\) connects vertices \(k-1\) and \(k\), \(1\le k\le n-1\). In a weighted tree the resistance distance is \(R_{ab}=\sum_{a<k\le b}r_k\) for \(a<b\). Writing \(H=I-J\), the familiar identity \(K=-HRH/2\) follows immediately from \(R_{ab}=K_{aa}+K_{bb}-2K_{ab}\) and \(K\mathbf1=0\). For adjacent vertices this gives the explicit formula
\[
n^2K_{k-1,k}=\sum_{j<k}j^2r_j+\sum_{j>k}(n-j)^2r_j-k(n-k)r_k.
\tag{1}
\]
Thus necessary adjacent sign constraints are
\[
t_k\ge\sum_{j<k}\frac{j}{n-j}t_j+\sum_{j>k}\frac{n-j}{j}t_j,\qquad t_j=j(n-j)r_j>0.
\tag{2}
\]

**Step 3: the four-vertex cutoff.** For \(n\ge4\), retain inequalities (2) at \(k=1,2,3\), discarding all other nonnegative summands. Then \(t=(t_1,t_2,t_3)^\mathsf{T}>0\) satisfies \(t\ge B_nt\), where \((B_n)_{ii}=0\), \((B_n)_{ij}=(n-j)/j\) for \(i<j\), and \((B_n)_{ij}=j/(n-j)\) for \(i>j\). Here indices \(i,j\) run through \(1,2,3\). This positive-off-diagonal matrix is diagonally similar to the symmetric matrix \(S_n\) whose off-diagonal entries are
\[
(S_n)_{ij}=\sqrt{\frac{i(n-j)}{j(n-i)}}\qquad(i<j).
\tag{3}
\]
For \(n=4\), direct multiplication shows \(B_4(3,2,3)^\mathsf{T}=(3,2,3)^\mathsf{T}\). Perron--Frobenius therefore gives \(\rho(S_4)=1\). For any \(n>4\), every upper-triangular entry in (3) increases strictly, because \((n-j)/(n-i)\) is strictly increasing in \(n\) when \(i<j\). By strict spectral-radius monotonicity for positive irreducible matrices, \(\rho(S_n)>1\). But \(t>0\) and \(t\ge B_nt\) would force \(\rho(B_n)\le1\) by multiplying by a positive left Perron vector. Hence no \(n\ge5\) is admissible.

For \(n=4\), equality in the Perron inequality forces \(t\) proportional to \((3,2,3)\), and therefore \((r_1,r_2,r_3)\) proportional to \((1,1/2,1)\), equivalently \((w_1,w_2,w_3)=a(1,2,1)\). For \(n=3\), the two conditions in (2) reduce to \(2r_1\ge r_2\) and \(2r_2\ge r_1\), which are equivalent to \(1/2\le w_2/w_1\le2\). For \(n=2\) there is no adjacent sign restriction. In every excluded case, at least one adjacent \(K_{k-1,k}>0\), so Step 1 proves the claimed eventual negative transition.

**Step 4: sufficiency for every positive timestep.** All denominators displayed below have strictly positive coefficients for positive variables. Let \(x=hw_1>0\).

For \(n=2\), \(T(h)\) has diagonal entries \((1+F(2x))/2\) and off-diagonal entries \((1-F(2x))/2\). For \(z>0\), \(0<F(z)<1\): the numerator of \(F\) is \((z-3)^2+3\), its denominator is positive, and their difference is \(12z\). Thus every entry is positive.

For \(n=3\), set \(v=w_2/w_1\). Define the strictly positive polynomial
\[
D_3=3x^4v^2+12x^3v^2+12x^3v+16x^2v^2+44x^2v+16x^2+48xv+48x+48.
\]
Direct exact rational matrix evaluation yields the three distinct off-diagonal entries
\[
\begin{aligned}
(T(h))_{0,1}&=\frac{4x\bigl((2v^2-v)x^2+6vx+12\bigr)}{D_3},\\
(T(h))_{1,2}&=\frac{4xv\bigl((2-v)x^2+6x+12\bigr)}{D_3},\\
(T(h))_{0,2}&=\frac{8x^2v\bigl((v+1)x+3\bigr)}{D_3}.
\end{aligned}
\tag{4}
\]
All are strictly positive for \(x>0\) if \(1/2\le v\le2\), including both endpoints.

For \(n=4\), scale the weights to \((1,2,1)\), put
\[
D_4=(x^2+3x+3)(x^4+9x^3+30x^2+27x+9)>0,
\]
and evaluate the four reflection classes:
\[
\begin{aligned}
(T(h))_{0,1}=(T(h))_{2,3}&=\frac{9x(x^3+5x^2+6x+3)}{D_4},\\
(T(h))_{0,2}=(T(h))_{1,3}&=\frac{3x^2(x^3+6x^2+15x+9)}{D_4},\\
(T(h))_{0,3}&=\frac{3x^3(2x^2+6x+3)}{D_4},\\
(T(h))_{1,2}&=\frac{9x(x^2+6x+6)}{D_4}.
\end{aligned}
\tag{5}
\]
These are strictly positive for \(x>0\). Finally, for all \(n\), the symmetric matrix \(T(h)\) is positive definite because \(F(z)>0\) for every \(z\ge0\); therefore every diagonal entry is strictly positive. Equations (4) and (5), together with the \(n=2\) formula, establish sufficiency. At \(h=0\), \(T(0)=I\) is nonnegative.

## Verification

The standalone file `verify.py` uses exact SymPy arithmetic to reconstruct the rational matrix function and verify the two-, three- and four-vertex formulas, symmetry and conservation; it also checks the adjacent resistance identity on several rationally weighted paths. Run `python verify.py` with Python 3 and SymPy installed; its expected final output is `VERIFY_OK`. The infinite-order cutoff and all-real-weight assertions are proved analytically above rather than inferred from the finite checks. Every polynomial appearing in (4) and (5) has its stated nonnegative coefficients, giving a human-checkable certificate.

## Relationship to prior work

Absolute monotonicity and positivity of rational Runge--Kutta methods are analyzed by Lóczi and Ketcheson (2013), but their rational-function threshold setting does not provide the all-timestep classification for weighted path Laplacians. The *necessary* inverse-Laplacian sign restriction in Steps 1--3 has substantial prior coverage: Chen, Kirkland and Neumann (1995) treated path/Jacobi group inverses, Kirkland, Neumann and Shader (1997) gave weighted-tree group-inverse formulas and a four-vertex weighted-path example, and Kirkland and Neumann (1998) characterized the weighted-tree group-inverse M-matrix problem. This theorem does **not** claim that earlier inverse-sign classification as new. Its distinct claim identifies precisely when the fourth-order Gauss rational end-step stays positive at **all positive timesteps** and provides explicit rational certificates of the sufficient cases. Earlier results on unweighted complete multipartite graphs imply positivity for the equal-weight three-vertex path and the two-vertex case, and already document failure for the unweighted four-vertex path. These special cases are acknowledged as covered. The present weighted-path classification, especially the full three-vertex weight interval, the unique four-vertex positive ray, and the all-weight exclusion at higher orders, is not implied by those unweighted statements. Related cycle and Cartesian-product graph results also concern different parameter domains.

## Limitations

This is a theorem only for symmetric positive conductances on finite paths and the specified completed two-stage Gauss end-step. It does not assert positivity at intermediate Runge--Kutta stages or for directed generators, arbitrary trees, or higher-stage methods. The inverse-Laplacian sign condition is not asserted to be sufficient on general graphs. Publication priority remains subject to specialist literature not available in full text, especially the 1995 and 1998 group-inverse papers; the present proof directly establishes every statement without relying on inaccessible results.

## References

- L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1 (first public March 26, 2013), https://arxiv.org/abs/1303.6651.
- S. J. Kirkland, M. Neumann and B. L. Shader, *Distances in Weighted Trees and Group Inverse of Laplacian Matrices*, SIAM J. Matrix Anal. Appl. 18 (1997), 827--841, https://doi.org/10.1137/S0895479896298713; lawful author/repository copy: https://pdfs.semanticscholar.org/6c13/6f0da4d44678c5251fe9b5a461f6ddbe1164.pdf.
- S. J. Kirkland and M. Neumann, *The M-Matrix Group Generalized Inverse Problem for Weighted Trees*, SIAM J. Matrix Anal. Appl. 19 (1998), 226--234, https://doi.org/10.1137/S0895479896304927.
- H. Chen, S. Kirkland and M. Neumann, work on group inverses of Jacobi matrices (1995), https://doi.org/10.1080/03081089508818406. The cited weighted-path findings are discussed in Kirkland--Neumann--Shader (1997).
