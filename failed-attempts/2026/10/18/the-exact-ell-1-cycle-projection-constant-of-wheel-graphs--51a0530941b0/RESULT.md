# The exact \(\ell_1\) cycle-projection constant of wheel graphs

## Finding
Let \(W_n=K_1*C_n\) be the simple unweighted wheel with \(n\ge4\) rim vertices and one hub, and let \(Z(W_n)\subset\ell_1(E(W_n);\mathbb R)\) be the real kernel of the oriented vertex-edge incidence map. Its *relative projection constant* is
\[
\lambda_n=\inf\{\|P\|_{1\to1}:P^2=P,\ \operatorname{ran}P=Z(W_n)\}
=\begin{cases}\frac53,&n=4,\\\frac74,&n=5,\\\frac95,&n\ge6.\end{cases}
\]
Thus the optimal norm stabilizes **exactly** at \(9/5\) once the rim has six vertices. Explicit optimal projections and finite dual witnesses valid at every size are given below. As a boundary consistency check, the analogous statement for \(n=3\) has value \(3/2\), already covered by the classical complete-graph instance \(W_3=K_4\).

## Assumptions and scope
All spaces and projections are real. Graph edges have unit weight, and all edge-vector norms are \(\ell_1\) norms. Write rim indices in \(\mathbb Z/n\mathbb Z\), orient rim edges \(r_i:i\to i+1\) and spokes \(s_i:o\to i\), where \(o\) is the hub. An edge vector has two blocks \((r,s)\in\mathbb R^n\oplus\mathbb R^n\). Let \((Dx)_i=x_i-x_{i-1}\), with indices modulo \(n\). The cycle subspace is precisely
\[
 Z(W_n)=\{(x,Dx):x\in\mathbb R^n\}.
\]
This follows from zero divergence at each rim vertex, which forces \(s_i=x_i-x_{i-1}\), and zero divergence at the hub, which then holds automatically.

## Proof
### Reduction to two cyclic kernels
The dihedral group of the rim acts on the edge \(\ell_1\) space by signed coordinate permutations and preserves the cycle space. Averaging any projection over this finite isometry group does not increase its norm or change its restriction to the cycle space. Consequently, a minimum-norm projection can be taken dihedrally equivariant.

Identify the range with its rim-flow coordinates \(x\). Rotational equivariance makes its rim response to unit rim edge \(r_j\) a translate of a vector \(a=(a_k)\), and its response to a unit spoke \(s_j\) a translate of \(b=(b_k)\). Reflection \(i\mapsto-i\) reverses rim orientation and preserves spoke orientation, so
\[
 b_k=-b_{n-1-k}.
\]
Being the identity on \((x,Dx)\) imposes
\[
 a_k+b_k-b_{k-1}=\mathbf1_{k=0},\qquad a=\delta_0-Db.
\]
Conversely, **every** such antisymmetric \(b\), with \(a=\delta_0-Db\), defines a projection onto the cycle subspace by cyclic convolution with these kernels. The \(\ell_1\) norm of any operator is its maximum absolute column sum. Therefore
\[
 \lambda_n=\min_{b_k=-b_{n-1-k}}\max\{R(a),S(b)\},\quad
 R(a)=\sum_k(|a_k|+|a_k-a_{k-1}|),\quad
 S(b)=\sum_k(|b_k|+|b_k-b_{k-1}|),\quad a=\delta_0-Db.
\tag{1}
\]
The minimum is attained because the corresponding finite-dimensional projection problem has a minimizer; the explicit construction below suffices for the upper bound.

### Explicit upper bounds
For \(n=4,5\), take
\[
 b_k=\frac{n-1-2k}{4(n-1)}\quad(0\le k<n),\qquad
 a_0=\frac12,\quad a_k=\frac1{2(n-1)}\ (1\le k<n).
\]
These vectors satisfy the symmetry and identity conditions. Direct summation gives \(R(a)=S(b)=2-1/(n-1)\), namely \(5/3\) and \(7/4\).

For every \(n\ge6\), choose \(b_0=3/10\), \(b_{n-1}=-3/10\) and all other \(b_k=0\). Then \(a_0=2/5\), \(a_1=a_{n-1}=3/10\), all other \(a_k=0\). The cyclic difference and absolute-value sums give
\[
 R(a)=\frac95=S(b).
\]
This proves the asserted upper bounds.

### Exact lower bounds: finite dual certificates
For any positive integers \(p,q\), and any four real sequences \(u,v,w,z\) satisfying
\[
 |u_k|,|v_k|\le p,\qquad |w_k|,|z_k|\le q,
\]
we have \(pR(a)+qS(b)\ge u\cdot a+v\cdot Da+w\cdot b+z\cdot Db\). Define the adjoint cyclic difference \((D^*y)_k=y_k-y_{k+1}\). Substituting \(a=\delta_0-Db\) yields
\[
 u\cdot a+v\cdot Da+w\cdot b+z\cdot Db
 =c+t\cdot b,\quad
 c=(u+D^*v)_0,\quad t=-D^*(u+D^*v)+w+D^*z.
\tag{2}
\]
If \(t_k=t_{n-1-k}\) for all \(k\), its pairing with the antisymmetric \(b\) vanishes. In that event every such projection obeys
\[
 \max\{R(a),S(b)\}\ge\frac{c}{p+q}.
\tag{3}
\]
The following table supplies complete certificates for the exceptional small rim sizes. Entries are indexed from \(0\), in the displayed order; \(t\) is included so the reflection symmetry can be checked directly.

| \(n\) | \((p,q;c)\) | \(u\) | \(v\) | \(w\) | \(z\) | \(t\) |
|---|---|---|---|---|---|---|
| 4 | (5,4;15) | (5,5,5,5) | (5,-5,-5,1) | (4,4,-4,-4) | (4,-4,-4,-4) | (2,-2,-2,2) |
| 5 | (7,5;21) | (7,7,7,7,7) | (7,-7,-5,0,7) | (5,5,0,-5,-5) | (5,-5,-5,-5,-5) | (-1,2,-2,2,-1) |
| 6 | (3,2;9) | (3,3,3,3,3,3) | (3,-3,-3,-2,0,3) | (2,2,0,0,-2,-2) | (2,-2,-2,-2,-2,-2) | (0,1,-1,-1,1,0) |
| 7 | (3,2;9) | (3,3,3,3,3,3,3) | (3,-3,-3,-2,0,0,3) | (2,2,2,0,0,-2,-2) | (2,-2,-2,0,0,-2,-2) | (0,1,-1,2,-1,1,0) |

For **every** \(n\ge8\), let \((p,q)=(3,2)\). Define \(u,v,w,z\) by the following nonzero coefficients (all unspecified coefficients are zero):
\[
\begin{aligned}
&u_0=u_1=u_2=u_3=u_{n-2}=u_{n-1}=3,\quad u_{n-3}=1;\\
&(v_0,v_1,v_2,v_3,v_{n-1})=(3,-3,-3,-2,3);\\
&w_0=w_1=w_2=w_3=2,\quad w_{n-3}=w_{n-2}=w_{n-1}=-2;\\
&(z_0,z_1,z_2,z_{n-2},z_{n-1})=(2,-2,-2,-2,-2).
\end{aligned}
\]
Direct use of \((D^*y)_k=y_k-y_{k+1}\) gives \(c=9\) and
\[
 t=(0,1,-1,1,\underbrace{0,\ldots,0}_{n-8},1,-1,1,0),
\]
which is reflection-symmetric. All coefficient bounds hold. Equation (3) gives \(9/5\) for every \(n\ge8\), and the finite rows supply the same bound for \(n=6,7\), as well as \(5/3\) and \(7/4\) for \(n=4,5\). Together with the constructions this proves the theorem. \(\square\)

## Verification
The self-contained standard-library program `verify.py` reconstructs the coefficients as exact rational numbers, checks all coordinate bounds, all adjoint-difference identities and reflection equalities, and both upper-bound column norms. Running `python verify.py` checks sizes \(3\) through \(60\), including the finite cases and a range of the uniform template. This computation is corroboration, not an infinite proof: the algebraic support formula for \(n\ge8\) in the preceding paragraph supplies the infinite argument. Independent numerical linear programs for all projections on wheels with \(3\le n\le11\) also agreed with the stated exact numbers; numerical optimization is not used in the proof.

## Relationship to prior work
Dilworth, Kutzarova, and Ostrovskii (first publicly available 21 May 2023, arXiv:2305.12582) establish the general framework for minimizing projections from \(\ell_1(E)\) onto graph cycle spaces, including finite-group averaging, and study tori, Hamming graphs, and earlier recursive graph families. Their paper does not state the above wheel-family constants, nor the stabilization threshold. Its averaging principle is used here as known background, not claimed as new. For \(n=3\), the wheel is the complete graph \(K_4\), whose minimal cycle-projection norm is already encompassed by the complete-graph formula; this known boundary value is excluded from the new theorem. General transportation-cost formulas do not themselves calculate minimum norms of linear projections onto these kernels.

## Limitations
The result is for real \(\ell_1\) edge spaces with equal edge lengths and wheel graphs with \(n\ge4\). It does not claim complex projections, arbitrary edge weights, other graph families, or uniqueness of the minimizer. An equivalent projection-constant result under different terminology in literature not indexed by the checked sources remains possible.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (first submitted 21 May 2023), especially Sections 1.1, 1.4(C), 2.1. https://arxiv.org/abs/2305.12582
2. G. Skandalis, A. Valette, *On the transportation cost norm on finite metric graphs*, arXiv:2601.16859 (2026), for the quotient-norm setting; this later note is contextual rather than a chronological source for the present direction. https://arxiv.org/abs/2601.16859
