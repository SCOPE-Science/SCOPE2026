# Sharp volume endpoints for odd-dimensional simplices with three coincident centers

## Finding

Let \(n\ge5\) be odd. Consider all nondegenerate Euclidean \(n\)-simplices whose centroid, incenter, and circumcenter coincide and whose circumradius is one and inradius is \(h\in(0,1/n]\). Set
\[
V_{\mathrm{reg}}=\frac{\sqrt{n+1}}{n!}\left(\frac{n+1}{n}\right)^{n/2},\qquad
D=\sqrt{\frac{h^{-2}-n^2}{n-1}},\qquad
 t=\frac{\sqrt{D^2+4}-D}{2}.
\]
Then \(0<t\le1\) and the exact sharp endpoint bounds are
\[
V_{\mathrm{reg}}t^{n-1}\left(\frac{n}{1+(n-1)t^2}\right)^{n/2}
\ \le\ \operatorname{Vol}_n(\Delta)\ \le\
V_{\mathrm{reg}}t\left(\frac{n}{n-1+t^2}\right)^{n/2}.
\]
For \(0<h<1/n\), each endpoint is realized by precisely one simplex congruence class. The lower endpoint has one exceptional *large* spectral axis, the upper endpoint one exceptional *small* spectral axis, each along a balanced sign vector. At \(h=1/n\), the only simplex is regular. Both endpoints therefore are attained in all odd dimensions \(n\ge5\), The result makes no assertion that every intermediate volume occurs.

As \(h\downarrow0\), the extremal volumes have different sharp powers:
\[
\frac{V_{\min}}{V_{\mathrm{reg}}}\sim n^{n/2}(n-1)^{(n-1)/2}h^{n-1},\qquad
\frac{V_{\max}}{V_{\mathrm{reg}}}\sim\left(\frac{n}{n-1}\right)^{n/2}\sqrt{n-1}\,h.
\]

## Assumptions and scope

All distances and volumes are Euclidean in the affine span. The simplex has \(n+1\) affinely independent vertices \(u_i\), with \(\sum_i u_i=0\), \(\|u_i\|=1\), and every facet supporting hyperplane at the same *positive* distance \(h\) from the origin. These conditions make the origin simultaneously the centroid, circumcenter, and incenter. No assumption is made that facets are congruent. The result is restricted to odd \(n\ge5\); it makes no assertion of sharpness of the displayed spectral bounds when \(n\) is even. The lower-dimensional tetrahedral problem was previously studied and is not asserted to be new here.

## Proof

**1. Matrix model.** Write \(m=n+1\), \(H=\{x\in\mathbb R^m:\sum_i x_i=0\}\), \(v_i=e_i-m^{-1}\mathbf1\). The \(v_i\) form a regular \(n\)-simplex, satisfy \(\sum_i v_i=0\), \(\sum_i v_iv_i^{\mathsf T}=I_H\), and \(\|v_i\|^2=n/m\). Every centered nondegenerate simplex is, after identifying its span with \(H\), the image of these vertices under an invertible \(T:H\to H\). Put \(Q=T^{\mathsf T}T\) and \(A=(n/m)Q\). Because \(\|Tv_i\|=1\) for every \(i\), the tight-frame identity gives \(\operatorname{tr}Q=m\) and \(\operatorname{tr}A=n\).

The facet opposite \(Tv_i\) has equation \(\langle x,-T^{-\mathsf T}v_i\rangle=1/m\): this follows since \(\langle v_j,v_i\rangle=-1/m\) for \(i\ne j\). Its distance from the origin is \(1/(m\|T^{-\mathsf T}v_i\|)\). Equal facet distances \(h\), together with the same tight-frame identity applied to \(T^{-\mathsf T}\), give \(\operatorname{tr}Q^{-1}=1/(mh^2)\) and hence \(\operatorname{tr}A^{-1}=1/(nh^2)\). Finally, \(\operatorname{Vol}_n(\Delta)/V_{\mathrm{reg}}=\sqrt{\det A}\). Thus we can bound volume by optimizing \(\det A\) over positive matrices satisfying these two trace constraints; only at equality do we need the additional equal-vertex and equal-facet diagonal conditions.

**2. Sharp spectral extrema.** If \(h=1/n\), Cauchy–Schwarz gives \(\operatorname{tr}A\operatorname{tr}A^{-1}\ge n^2\), with equality only for \(A=I_H\). Assume \(h<1/n\). Let the positive eigenvalues be \(\lambda_1,\ldots,\lambda_n\) with fixed sum \(n\) and reciprocal sum \(1/(nh^2)>n\). The feasible spectral set is compact and lies strictly in the positive orthant. At every extremum, the two constraint gradients are independent (because not all eigenvalues agree), and the Lagrange equation for \(\sum_i\log\lambda_i\) is
\[
\lambda^{-1}-\alpha+\beta\lambda^{-2}=0.
\]
It has at most two positive roots \(x>y>0\). Writing the stationarity multipliers in terms of the roots gives \(\alpha=1/(x+y)\) and \(\beta=-xy/(x+y)\). The diagonal Hessian of the constrained Lagrangian is
\[
L''(\lambda)=\frac{2xy/(x+y)-\lambda}{\lambda^3},
\]
which is **negative at** \(x\) and **positive at** \(y\). If the larger root occurred at least twice, varying two such coordinates in opposite directions would be tangent to both constraints but have negative second variation; it therefore cannot be a local minimum. Hence the *minimum* determinant has multiplicities \((1,n-1)\) for \((x,y)\). If the smaller root occurred at least twice, the analogous positive second variation would forbid a local maximum. Thus the *maximum* has multiplicities \((n-1,1)\). This argument includes all spectral critical points and fixes both global extrema.

Writing \(y=t^2x\), either multiplicity pattern yields
\[
h^{-2}=n^2+(n-1)(t^{-1}-t)^2,
\]
with the unique \(t\in(0,1)\) defined in the finding. For the minimum, \(x=n/(1+(n-1)t^2)\) and \(\det A=x^nt^{2(n-1)}\). For the maximum, \(x=n/(n-1+t^2)\) and \(\det A=x^nt^2\). Taking positive square roots proves both inequalities.

**3. Exact attainment and equality rigidity.** Since \(m=n+1\) is even, choose \(q\in H\) with \(m/2\) coordinates \(+1/\sqrt m\) and \(m/2\) coordinates \(-1/\sqrt m\). Let \(P=qq^{\mathsf T}\). The explicit lower-extremizer vertices are
\[
u_i^{\min}=\frac{[P+t(I_H-P)]v_i}{\sqrt{[1+(n-1)t^2]/m}},
\]
and the upper-extremizer vertices are
\[
u_i^{\max}=\frac{[(I_H-P)+tP]v_i}{\sqrt{[n-1+t^2]/m}}.
\]
Because \(\langle q,v_i\rangle=q_i\) and \(q_i^2=1/m\), every vertex in each construction has unit norm; every opposite facet has equal distance from the origin by the inverse-operator version of the same identity. The above spectral calculations give exactly the prescribed \(h\) and the endpoint volumes. In any equality case the exceptional eigenspace is one-dimensional, spanned by some unit \(q\in H\). Equal vertex lengths force the quantities \(|\langle q,v_i\rangle|^2=|q_i|^2\) to be constant. Thus all coordinates are equal in magnitude, and since they sum to zero, exactly half are positive and half negative. All such choices are equivalent under permutations of the regular-simplex vertices, so each endpoint has precisely one congruence class. At \(t=1\), both become regular.

## Verification

The analytic proof handles all odd \(n\ge5\), all \(0<h\le 1/n\), both endpoints and equality cases. For independent finite checking, run `python3 centered_simplex_checker.py`: it uses exact rational matrices and Gaussian elimination to check eighteen construction instances across dimensions \(5,7,9\), deformation parameters \(1/2,2/3,3/4\), and both extrema. Each checks unit vertex norms, equal facet distances, the predicted inradius and the exact Gram-determinant volume. The finite checker is corroboration, not the infinite proof. No computer-assisted exhaustive search is claimed.

## Relationship to prior work

Nour's 2026 construction uses simplices with coincident circumcenter and incenter to prove sharp ball-union obstructions, and constructs an explicit rank-two Fourier-mode degeneration in all dimensions. Its full manuscript does not give the sharp fixed-inradius volume envelope or the two rank-one balanced equality classes. Edmonds–Hajja–Martini (2005) studies coincident simplex centers, especially four-dimensional examples and Gram matrices, but not the stated odd-dimensional sharp volume law. A published three-dimensional result gives a full volume interval for concentric bicentric tetrahedra, so dimension three is excluded from the novelty claim. The volume law here is a geometric counterpart to Nour's sharp local covering-radius formula, not a new proof of the union-of-balls conjecture.

## Limitations

The result imposes coincidence of **all three** centers, not only incenter and circumcenter. It does not characterize the volume envelope in even dimensions; the balanced rank-one equality construction exists only when \(n+1\) is even. It does not claim that the simplex-volume law improves the universal covering radius. Priority searches cannot rule out unindexed determinant or simplex-geometry results. An independent mathematical audit has not been performed.

## References

1. C. Nour, *A counterexample to the strong version of the union of uniform closed balls conjecture in dimensions three and higher*, arXiv:2611.14181v1 (first posted 10 November 2026), https://arxiv.org/abs/2611.14181; sections 2–3.
2. A. L. Edmonds, M. Hajja and H. Martini, *Coincidences of Simplex Centers and Related Facial Structures*, Contributions to Algebra and Geometry **46** (2005), 491–512, https://eudml.org/serve/126304/accessibleLayeredPdf/0; especially section 4.
3. *Sharp volume interval for concentric bicentric tetrahedra*, published-finding corpus published research record (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-volume-interval-for-concentric-bicentric-tetrahedra--3c21c1faa6d8. Its public summary describes the three-dimensional interval, not a higher-dimensional formula.
