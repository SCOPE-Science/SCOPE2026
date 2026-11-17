# Optimal dedicated control of affine-plane incidence graphs with a stalled zero-forcing placement

## Finding

**Theorem.** Let \(\mathcal A\) be any *existing* finite affine plane of order \(q\ge2\), and let \(G\) be its unweighted, undirected point--line incidence graph. Its vertices consist of \(q^2\) points and \(q(q+1)\) lines. Let \(L\) be the combinatorial Laplacian. For a vertex set \(S\), let \(B_S\) have the distinct standard coordinate vectors \(e_v\), \(v\in S\), as its columns. Then

\[
\min\bigl\{|S|:(-L,B_S)\ \text{is controllable}\bigr\}=q^2-1.
\]

Any controllable \(S\) contains at least \(q\) line vertices. Both bounds are attained by the following field-free construction: choose a line \(\ell\) and a point \(P\notin\ell\); actuate every point except those on \(\ell\) and \(P\), and actuate all \(q\) lines through \(P\) which meet \(\ell\). This optimum is **not** a zero-forcing set (its forcing process stalls immediately).

## Assumptions and scope

A finite affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines, exactly \(q\) points per line and \(q+1\) lines through each point. Any two distinct points determine a unique line. The lines are partitioned into \(q+1\) parallel classes, each comprising \(q\) lines; one member of each class goes through any point. The graph has one edge for each point--line incidence, with weight exactly one. Inputs are independent real signals, each coupled to exactly one vertex; no free changes to edge weights, feedback law, or other actuator patterns are permitted. Controllability means ordinary finite-dimensional Kalman controllability of the stated continuous-time, fixed-Laplacian system.

No claim is made for an order at which no affine plane exists. In particular, no prime-power or coordinatization assumption is made in the theorem.

## Proof

**1. Incidence identity and complete Laplacian spectrum.** Write \(v=q^2\), \(b=q(q+1)\), and let \(M\in\{0,1\}^{v\times b}\) be the point--line incidence matrix (points index rows). Unique joining lines and point degree \(q+1\) imply

\[
MM^{\mathsf T}=qI_v+J_v.
\]

This matrix is positive definite, so \(\operatorname{rank}M=v\) and \(\dim\ker M=b-v=q\). With point vertices first, the Laplacian is

\[
L=\begin{pmatrix}(q+1)I_v&-M\\-M^{\mathsf T}&qI_b\end{pmatrix}.
\]

For the two-dimensional constant-on-each-part space its eigenvalues are \(0\) and \(2q+1\), each simple. For every point vector \(x\perp\mathbf1_v\), the two eigenvalues obey

\[
(q+1-\lambda)(q-\lambda)=q,
\qquad
\lambda_{\pm}=\frac{2q+1\pm\sqrt{4q+1}}2,
\]

and have multiplicity \(v-1=q^2-1\) each: the corresponding line component is \(y=(q-\lambda)^{-1}M^{\mathsf T}x\). The remaining line-only eigenspace is \(\{(0,y):My=0\}\), of dimension \(q\) and eigenvalue \(q\). These five eigenvalues are distinct when \(q\ge2\), with total multiplicities \(1+(v-1)+q+(v-1)+1=v+b\).

For a real symmetric system matrix, the PBH test says that the coordinate inputs on \(S\) yield controllability precisely when no nonzero eigenvector vanishes on all vertices of \(S\). An eigenspace of dimension \(v-1\) thus forces \(|S|\ge v-1=q^2-1\). Also, vectors in the eigenvalue-\(q\) space have zero point component, so rank \(q\) on that space requires at least \(q\) *line*-vertex inputs in every controllable set.

**2. Attaining both lower bounds.** Fix \(\ell\) and \(P\notin\ell\). Let \(\mathcal Q\) be the \(q\) points on \(\ell\). Every line through \(P\) other than the unique line parallel to \(\ell\) meets \(\ell\) once; these \(q\) lines meet it at the distinct points \(Q\in\mathcal Q\). Select all \(v-(q+1)=q^2-q-1\) point vertices in the complement of \(\mathcal Q\cup\{P\}\), and those \(q\) line vertices. Hence \(|S|=v-1\), with exactly \(q\) line inputs.

For eigenvalues \(0\) and \(2q+1\), both eigenspaces are one-dimensional with nonzero constant point and line components. As the selected set is nonempty, neither space contains a nonzero vector vanishing on \(S\).

For eigenvalue \(q\), the kernel \(\ker M\) has the following explicit basis. Let \(h_d\) be the indicator of all \(q\) lines in the \(d\)-th parallel class, for \(d=0,\ldots,q\). Since \(Mh_d=\mathbf1_v\), the \(q\) vectors \(h_d-h_0\), for \(d=1,\ldots,q\), belong to \(\ker M\), are independent, and span it by dimension. The selected \(q\) lines belong to \(q\) different parallel classes (all except the class of \(\ell\)). If a vector in this kernel vanishes on these selected lines, its coefficients in those \(q\) classes vanish; the sum-zero condition forces the remaining coefficient to vanish too. Thus the eigenvalue-\(q\) space is observed injectively.

Finally, consider either \(\lambda_+\) or \(\lambda_-\). Its eigenvectors have a point component \(x\perp\mathbf1_v\) and line component \(y=(q-\lambda)^{-1}M^{\mathsf T}x\), where \(q-\lambda\ne0\). If the eigenvector vanishes at all selected points, \(x\) is supported on \(\mathcal Q\cup\{P\}\). Vanishing at the selected line \(PQ\), for each \(Q\in\mathcal Q\), gives

\[
0=y_{PQ}=\frac{x_P+x_Q}{q-\lambda},
\quad\text{so}\quad x_Q=-x_P.
\]

Since \(\sum x=0\), it follows that \((1-q)x_P=0\). As \(q\ge2\), all components of \(x\) vanish, and hence those of \(y\) vanish. PBH therefore holds for every eigenvalue. Both asserted minima are attained.

**3. The optimal placement is stalled under zero forcing.** Color just the selected vertices black. Each selected line \(PQ\) has precisely two white point neighbors, namely \(P\) and \(Q\); all its other point neighbors are black. Each selected point lies on at most one selected line because all selected lines pass through \(P\), so its \(q+1\) line neighbors include at least \(q\ge2\) white lines. Every black vertex has at least two white neighbors. Hence there is no legal initial zero-forcing move, and the entire graph has not been colored: \(S\) is not zero forcing.

## Verification

Run `python3 verify_affine.py` using standard Python. The program constructs affine planes over the prime fields of orders \(2,3,5,7,11\) and independently checks the exact incidence-Gram identity, the full-rank point-component observation constraints modulo \(1000003\), the independent observation of the line-kernel space, both actuator counts, and the absence of any initial zero-forcing move. It prints `VERIFY_OK` upon success. The modular rank test supplies exact full-rank witnesses for those instances, not a proof of the theorem for all orders; that follows from the plane-axiom argument above. The symbolic spectrum and PBH reasoning apply equally to non-Desarguesian affine planes.

## Relationship to prior work

Burgarth et al. (2011) establish zero forcing as a sufficient, not necessary, condition for controllability of network systems with standard coordinate controls. The placement here is a natural infinite, explicitly optimal, **stalled** family illustrating the insufficiency of that criterion for *necessary* leader selection. Yuan et al. (2013) prove a general geometric-multiplicity formula for the minimum number of freely configured independent input channels and describe driver identification. Their general lower bound is consistent with \(q^2-1\) but supplies neither the incidence-specific, field-free coordinate placement nor simultaneous attainment of the sharp minimum number of line actuators. Monshizadeh, Zhang and Camlibel (2014) characterize robust controllability over a family of graph-compatible matrices using zero forcing; this is different from the fixed, unit-weight Laplacian here. The affine-plane-specific construction is the added result.

## Limitations

This theorem concerns exact controllability, not actuator energy, conditioning, resilience under vertex failure, generic edge weights, input restrictions, or minimum time to control. It does not claim that *every* optimal placement is stalled or that \(q^2-1\) is the zero-forcing number. Existence of a plane of an arbitrary order is not assumed; numerical checks only cover prime orders listed in the verification section. Broader literature could contain an equivalent specialized formulation not indexed by the searches described in the accompanying review.

## References

1. D. Burgarth, D. D'Alessandro, L. Hogben, S. Severini, and M. Young, *Zero forcing, linear and quantum controllability for systems evolving on networks*, arXiv:1111.1475v1 (public November 7, 2011), https://arxiv.org/abs/1111.1475.
2. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang, and Y.-C. Lai, *Exact controllability of complex networks*, Nature Communications **4**, 2447 (September 12, 2013), https://doi.org/10.1038/ncomms3447.
3. N. Monshizadeh, S. Zhang, and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868v1 (March 19, 2014), https://arxiv.org/abs/1403.4868.
