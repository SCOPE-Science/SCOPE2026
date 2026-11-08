# Minimum finite-model dimension for maximal near-invariance defect

## Finding
For every integer \(r\geq1\), the **smallest possible dimension** of a finite-dimensional scalar Hardy model space \(K_\theta\) containing the kernel of a rank-\(r\) perturbation of a truncated Toeplitz operator whose least nearly backward-shift-invariance defect is \(2r+1\) equals
\[
\boxed{N_{\min}(r)=4r+2.}
\]
This holds when minimizing over all finite Blaschke products \(\theta\), all bounded symbols \(g\), and all perturbations of rank exactly \(r\). It is attained by an explicit two-monomial symbol on \(K_{z^{4r+2}}\) and a sum of \(r\) orthogonal coordinate rank-one maps. In every dimension-minimal realization, the kernel \(M\) must have dimension \(2r+1\), every element of \(M\) vanishes at the origin, and the model space splits algebraically as \(K_\theta=M\oplus S^*M\).

## Assumptions and scope
Work over the complex Hardy space \(H^2(\mathbb D)\). For a finite Blaschke product \(\theta\) of degree \(N\), set \(K_\theta=H^2\ominus\theta H^2\), a complex Hilbert space of dimension \(N\). For \(g\in L^\infty(\mathbb T)\), the truncated Toeplitz operator is \(A_g^\theta f=P_{K_\theta}(gf)\). The backward shift \(S^*f=(f-f(0))/z\) preserves \(K_\theta\).

For a subspace \(M\subseteq K_\theta\), put \(M_0=\{f\in M:f(0)=0\}\). Its *least nearly backward-shift-invariance defect* \(d(M)\) is the smallest dimension of a subspace \(F\subseteq K_\theta\) such that \(S^*M_0\subseteq M+F\); equivalently,
\[
d(M)=\dim\big((M+S^*M_0)/M\big).
\]
The definition is independent of the choice of correction subspace; the correction may be chosen orthogonal to \(M\). All ranks and dimensions here are complex-linear.

## Proof
**Universal finite-dimensional obstruction.** Set \(m=\dim M\). Since \(M_0\subseteq M\) and \(S^*M_0\subseteq K_\theta\),
\[
d(M)\leq\dim M_0\leq m,\qquad d(M)\leq N-m.
\]
Thus \(N\geq 2d(M)\). In particular, \(d(M)=2r+1\) forces \(N\geq4r+2\), irrespective of the operator that produced \(M\).

If equality \(N=2d(M)\) holds, then \(m=\dim M_0=d(M)\). Thus \(M=M_0\) (every function in \(M\) vanishes at zero), the induced map \(S^*M\to K_\theta/M\) is injective, and its image is the entire quotient. Equivalently, \(K_\theta=M\oplus S^*M\). This proves the asserted necessary structure of every dimension-minimal realization.

**A matching rank-\(r\) truncated Toeplitz construction.** Fix \(r\geq1\), put \(N=4r+2\) and \(k=2r+2\), and take \(\theta(z)=z^N\). Let \(e_j=z^j\), for \(0\leq j<N\), be the monomial orthonormal basis of \(K_\theta\), and write \(J=S^*|_{K_\theta}\). Consider the two-monomial truncated Toeplitz symbol
\[
g(z)=\overline z^{\,k}+z^{N-1},\qquad A=A_g^\theta=J^k+(J^*)^{N-1}.
\]
Here the rank-one convention is \((u\otimes v)f=\langle f,v\rangle u\). Define the rank-\(r\) operator
\[
P=\sum_{j=0}^{r-1}e_{2j+1}\otimes e_{2j+2},\qquad B=A-P.
\]
The source vectors and output vectors in this sum are each orthonormal, so \(\operatorname{rank}P=r\) exactly.

For \(x=\sum_{i=0}^{N-1}x_ie_i\), the only possibly nonzero coordinates of \(Bx\) are
\[
(Bx)_{2j}=x_{k+2j},\qquad
(Bx)_{2j+1}=x_{k+2j+1}-x_{2j+2}
\quad(0\leq j<r),\qquad
(Bx)_{N-1}=x_0.
\]
It follows without any matrix-rank approximation that \(M=\ker B\) has the following basis of \(2r+1\) vectors:
\[
u_0=e_1,\qquad
u_{2j+1}=e_{2j+2}+e_{k+2j+1},\qquad
u_{2j+2}=e_{2j+3}\quad(0\leq j<r).
\]
These basis vectors exhaust the freely specifiable coordinates \(x_1,\ldots,x_{2r+1}\); the remaining coordinates are determined by the displayed equations. In particular, \(M_0=M\).

Since \(Je_i=e_{i-1}\) for \(i\geq1\) and \(Je_0=0\), direct substitution into the *same* operator \(B\) yields
\[
BJu_0=e_{N-1},\qquad
BJu_{2j+1}=e_{2j},\qquad
BJu_{2j+2}=-e_{2j+1}
\quad(0\leq j<r).
\]
The \(2r+1\) images form, up to signs and order, the linearly independent set \(\{e_{N-1},e_0,e_1,\ldots,e_{2r-1}\}\). As \(\ker B=M\), the quotient map \(K_\theta\to K_\theta/M\) factors injectively through \(B\) on its range. Hence
\[
d(M)=\dim B(JM)=2r+1.
\]
Because \(\dim M=2r+1\) and \(N=4r+2\), the same independence gives \(M\cap JM=\{0\}\) and \(K_\theta=M\oplus JM\). This achieves the universal lower bound on model-space dimension, proving the theorem for **every** integer \(r\geq1\).

## Verification
The accompanying standalone standard-library checker `check.py` creates the integral matrices of the displayed model for \(1\leq r\leq13\), verifies the kernel basis and each stated image of the backward shift, confirms the perturbation rank and kernel rank, and checks complementarity using prime-field elimination. Run `python3 check.py` in a directory containing the file. All thirteen cases passed. The proof above establishes the unbounded parameter range; finite checks are diagnostics and do not replace its symbolic argument.

## Relationship to prior work
Chattopadhyay and Khan (arXiv:2610.40295v1, Theorem 5.4) proved the upper bound \(d(\ker(A_g^\theta-P))\leq2r+1\) for rank-at-most-\(r\) perturbations of truncated Toeplitz operators. All-rank sharpness with larger finite models had also been demonstrated previously. Neither an upper bound nor an example in a larger model implies the exact **minimum** possible model-space dimension. The present contribution is the size-optimal realization \(N=4r+2\), together with its forced balanced and transverse kernel geometry. It does not claim first discovery of all-rank sharpness.

Liang and Partington (2020) studied nearly backward-shift-invariant kernels of perturbed Toeplitz operators on the full Hardy space. That setting does not determine a finite-dimensional lower cutoff for compressed, truncated Toeplitz perturbations.

## Limitations
The minimality statement concerns finite-dimensional **scalar** Hardy model spaces, not infinite inner functions or multiband constructions. No uniqueness or classification of all size-minimizing symbols and perturbations is asserted. The theorem determines an exact finite dimension and necessary subspace geometry; it is not a new bound on the defect itself. No independent mathematical audit or definitive publication-priority determination is claimed.

## References
1. A. Chattopadhyay and A. Khan, *Perturbations of Truncated Toeplitz operators*, arXiv:2610.40295v1, first public 2026-10-29, Theorem 5.4; https://arxiv.org/html/2610.40295v1 . The revised v3, https://arxiv.org/html/2610.40295v3 , retains the same defect upper bound.
2. Y. Liang and J. R. Partington, *Representing Kernels of Perturbations of Toeplitz Operators by Backward Shift-Invariant Subspaces*, Integral Equations and Operator Theory 92 (2020), 35; https://doi.org/10.1007/s00020-020-02592-7 ; author manuscript https://eprints.whiterose.ac.uk/162175/1/perturbations-of-Toeplitz-operators28.pdf .
