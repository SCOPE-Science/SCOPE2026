# A sharp three-stage variation threshold for Euclidean projection onto cyclic TV balls

## Finding

For integer \(n\ge3\), real vectors \(x=(x_0,\dots,x_{n-1})\), and cyclic indices define
\[
V_n(x)=\sum_{i=0}^{n-1}|x_{i+1}-x_i|,
\qquad
P_{n,\tau}(x)=\mathop{\mathrm{argmin}}_{z:V_n(z)\le\tau}\frac12\sum_{i=0}^{n-1}(z_i-x_i)^2.
\]
For every \(\tau>0\), the exact two-input variation-Lipschitz norm is
\[
\boxed{
\sup_{V_n(x-y)>0}\frac{V_n(P_{n,\tau}x-P_{n,\tau}y)}{V_n(x-y)}
=\begin{cases}
1,&n=3,4,\\
3/2,&n=5,\\
2,&n\ge6.
\end{cases}}
\]
Each supremum is attained by some finite pair \(x,y\). The radius does not affect the answer.

## Assumptions and scope

All coordinates and projections are real and Euclidean, every cycle edge has unit variation weight, and \(n\) is an integer at least three. The variation is the *cyclic* adjacent-edge seminorm, not path variation, and no mean anchoring is imposed. The map preserves additive constants, so its variation-Lipschitz factor is well defined on the quotient by constants. For \(\tau=0\) projection is the constant-mean map and the factor is zero, hence the assumption \(\tau>0\) is essential.

## Proof

**1. Reduction to face Jacobians.** The ball \(B_\tau=\{V_n\le\tau\}\) is a polyhedron invariant under constants. Euclidean projection onto it is continuous and piecewise affine. On an open projection cell where the projected point lies in the relative interior of a fixed face \(F\), the linear part is orthogonal projection \(J_F\) onto the parallel space of \(F\). A segment joining arbitrary input vectors crosses finitely many such cells (or can be approximated by generic segments), hence a uniform bound \(V_n(J_Fv)\le K V_n(v)\) for all faces implies the global two-input bound.

Let \(E\) be the nonempty set of edges of a projected boundary point where differences are nonzero. Its zero-difference edges identify consecutive cyclic blocks \(B_1,\ldots,B_r\); \(r=|E|\ge2\). Let \(Q\) be Euclidean averaging within each block. Denote by \(s_e\in\{-1,1\}\) the sign of the nonzero difference on edge \(e\in E\), and put \(s_e=0\) off \(E\). Define the incidence map \((Dv)_e=v_{e+1}-v_e\) and \(g=QD^Ts\). Because a closed cycle's nonzero signed differences sum to zero, both signs occur. The face-parallel space is exactly the block-constant vectors orthogonal to \(g\), and therefore
\[
J_F=Q-\frac{gg^T}{\|g\|_2^2}.
\]
Here \(g\ne0\). For a point in the interior of \(B_\tau\), \(J_F=I\). All proper boundary face types are covered by the formula.

**2. Universal factor-two bound.** First, consecutive cyclic block averaging is variation diminishing:
\[
V_n(Qv)\le V_n(v).
\]
Indeed, select one vertex uniformly and independently in each block. The selected vertices occur in cyclic order. For each selection, the sum of successive absolute value differences cannot exceed \(V_n(v)\), since the paths joining successive selected vertices partition the original cyclic edges. Jensen's inequality gives the stated bound for the block averages.

Write \(\gamma_j\) for the constant value of \(g\) on block \(B_j\) of length \(\ell_j\). If the incident boundary-edge signs before and after that block are \(a_j,b_j\in\{\pm1\}\), then
\[
\gamma_j=(a_j-b_j)/\ell_j\in\{0,\pm2/\ell_j\}.
\]
Consequently, using \(V_n(g)=\sum_j|\gamma_{j+1}-\gamma_j|\),
\[
V_n(g)\le2\sum_j|\gamma_j|=\sum_j\ell_j\gamma_j^2=\|g\|_2^2.
\]
Also, for any \(v\),
\[
|g^Tv|=|s^TDQv|\le V_n(Qv)\le V_n(v).
\]
Thus the rank-one operator \(R=gg^T/\|g\|_2^2\) satisfies \(V_n(Rv)\le V_n(v)\). The triangle inequality in \(J_F=Q-R\) proves the universal \(V_n(J_Fv)\le2V_n(v)\) and hence the global bound two for all \(n\ge3\).

**3. Exact finite small-cycle bound.** The extreme points of the cyclic variation unit ball modulo constants are precisely the positive and negative normalized arc indicators. To prove this, apply the cyclic difference map: its image is the hyperplane \(\sum_e d_e=0\), with variation \(\sum_e|d_e|\). Intersecting the \(\ell^1\) cross-polytope with that hyperplane has vertices \((e_i-e_j)/2\) for all distinct edges \(i,j\); each pulls back to a half-scaled arc indicator. Therefore, for each fixed \(J_F\), maximizing \(V_n(J_Fv)/V_n(v)\) reduces to the \(n(n-1)/2\) arcs, up to sign and constants.

All face types are exhaustively described by choosing a set \(E\) of \(r\ge2\) nonzero boundary edges and choosing their signs with both signs present, modulo simultaneous reversal. Every such choice is feasible because one can choose strictly positive edge-difference magnitudes of each sign summing to the same amount, and therefore corresponds to a genuine exposed face. The exact rational standalone verifier `verify_cycle_tv.py` enumerates every such face, constructs \(Q,g,J_F\) over rational numbers and computes the maximum over all arc vertices. Its complete small-cycle table is:

| \(n\) | \(r=2\) | \(r=3\) | \(r=4\) | \(r=5\) | Interior included |
|---|---:|---:|---:|---:|---:|
| 3 | 0 | 1 | — | — | 1 |
| 4 | 0 | 1 | 1 | — | 1 |
| 5 | 0 | 1 | \(4/3\) | \(3/2\) | \(3/2\) |

The face counts, respectively, are \((3,3)\), \((6,12,7)\), and \((10,30,35,15)\) by increasing \(r\); the verifier checks every sign choice, boundary subset and arc without floating-point rounding. The enumerated maxima plus the interior identity map give the claimed upper bounds for \(n=3,4,5\).

**4. Attainment and the threshold.** For \(n=3,4\), any two nearby distinct vectors already inside the variation ball have projection equal to themselves, giving ratio one. For \(n\ge5\), fix indices \(p=1\) and \(q=4\), using zero-based indexing, and let \(v\) equal one at vertices \(0,1,2\) and zero elsewhere. Choose a full-support difference-sign pattern with positive signs on the cyclic edge run from \(q\) to \(p\), and negative signs on the complementary run, so that \(D^Ts=2(e_p-e_q)\). A point \(z\) on the corresponding facet can be constructed by assigning each positive edge a positive increment summing to one, each negative edge a negative increment summing to minus one, and integrating around the cycle; thus \(V_n(z)=2\). More explicitly, take each positive edge increment to be \(1/N_+\), and each negative edge increment to be \(-1/N_-\), where \(N_+\) and \(N_-\) are the positive and negative sign counts, so that the increments sum to zero. Let \(g=D^Ts=2(e_p-e_q)\), \(\varepsilon=1/(10n)\), \(\delta=1/(100n)\), \(x=z+\varepsilon g\), and \(y=x+\delta v\). Then \(P_{n,2}(x)=z\), while \(P_{n,2}(y)=z+\delta Jv\): the latter point remains on the same facet because each original nonzero edge increment has magnitude at least \(1/n\) and each perturbation edge increment has magnitude at most \(\delta\); moreover the positive normal residual is \(y-(z+\delta Jv)=(\varepsilon+\delta/4)g\). Its local linear map is
\[
Jv=v-\frac{v_p-v_q}{2}(e_p-e_q).
\]
The variation of \(v\) equals two, while \(V_5(Jv)=3\) and \(V_n(Jv)=4\) for all \(n\ge6\). Therefore taking two sufficiently close inputs in this projection cell gives the finite-pair ratios \(3/2\) and \(2\). Scaling the data and the radius from two to arbitrary \(\tau>0\) preserves the ratios, completing the proof.

## Verification

Run `python3 verify_cycle_tv.py` with the standard Python library. It uses exact rational arithmetic and exhaustively checks all faces and all arc vertices for \(n=3,4,5\). The exact output is:

```
n= 3 face_counts= {2: 3, 3: 3} face_maxima= {2: '0', 3: '1'} with_interior= 1
n= 4 face_counts= {2: 6, 3: 12, 4: 7} face_maxima= {2: '0', 3: '1', 4: '1'} with_interior= 1
n= 5 face_counts= {2: 10, 3: 30, 4: 35, 5: 15} face_maxima= {2: '0', 3: '1', 4: '4/3', 5: '3/2'} with_interior= 3/2
EXACT_COMPLETE_SMALL_CYCLE_FACE_CERTIFICATE_PASS
```

The all-length factor-two bound and sharpness are analytical; the finite certificate is exhaustive only for the expressly listed small dimensions. The code computes proof-relevant face matrices and not a numerical sample of input pairs.

## Relationship to prior work

Fadili–Peyré, *Total Variation Projection with First Order Schemes*, studies the total-variation-ball projector and first-order algorithms. Couprie and collaborators, *Dual Constrained TV-based Regularization on Graphs*, develop incidence-based TV frameworks and proximal algorithms. Their inspected arguments do not give the sharp two-input norm in *cyclic variation* or its five-site intermediate regime. The published path-TV-ball result titled *Sharp bounded-variation stability transition for projection onto a discrete total-variation ball* proves the analogous path constants \(1\) (two and three sites) and \(2\) (four or more); the path theorem explicitly excludes the cyclic case, whose added edge changes both the ball and the perturbation seminorm. The present theorem is not a numerical specialization of that path claim. Exact equality with other historical formulations has not been independently excluded.

## Limitations

The result does not classify nonuniform edge weights, graph topologies beyond simple cycles, non-Euclidean metric projections, the zero-radius case as a positive-radius limit, or the full family of equality pairs. The finite certificate supplements but does not replace the analytical proof. Full-text access to all possibly relevant historical priority sources was not established; original-source priority remains subject to further checking.

## References

1. J. M. Fadili and G. Peyré, *Total Variation Projection with First Order Schemes*, IEEE Transactions on Image Processing 20 (2011), 657–669, DOI: 10.1109/TIP.2010.2072512; accessible manuscript: https://fadili.users.greyc.fr/Pub/bibtex/manuscript/manuscrit504.pdf.
2. C. Couprie, L. Grady, L. Najman, J.-C. Pesquet and H. Talbot, *Dual Constrained TV-based Regularization on Graphs*, SIAM Journal on Imaging Sciences 6 (2013), 1246–1273, DOI: 10.1137/120895068; open manuscript: https://files01.core.ac.uk/download/pdf/48332369.pdf.
3. *Sharp bounded-variation stability transition for projection onto a discrete total-variation ball* (published finite-path result), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-bounded-variation-stability-transition-for-projection-onto--43b65933e518.
