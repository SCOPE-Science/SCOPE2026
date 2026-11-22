# Affine-regular hexagons are the unique equality geometry for the three-vector \(3/2\) separation bound

## Finding
Let \(X\) be a real normed space, and let \(v_1,v_2,v_3\in X\setminus\{0\}\) be noncollinear with \(v_1+v_2+v_3=0\). For the opposite-pair separation profile
\[
R(v_1,v_2,v_3)=\max_{\{i,j,k\}=\{1,2,3\}}\frac{\|v_i-v_j\|}{\|v_k\|},
\]
we have \(R\ge3/2\). Equality holds **if and only if** the unit ball of the induced norm on \(Y=\operatorname{span}\{v_1,v_2\}\) is an affine-regular hexagon, with the normalized \(v_i\) at alternate edge midpoints. All equality triples have equal \(\|v_i\|\) and satisfy \(\|v_i-v_j\|=3\|v_k\|/2\). Conversely, every affine-regular hexagonal normed plane admits an equality triple. In particular, if \(X\) has no isometric affine-regular hexagonal two-dimensional subspace, then \(R>3/2\) for every admissible triple; this includes all strictly convex real spaces.

## Assumptions and scope
All spaces and scalars are real. The vectors are nonzero and their span has dimension exactly two. An *affine-regular hexagon* means an invertible linear image of the Euclidean regular centrally symmetric hexagon. Unit balls and supporting functionals below are taken **in the induced two-dimensional norm**; no ambient smoothness, reflexivity or completeness is assumed. This result classifies equality in the separation estimate used in the Fermat–Torricelli radial-rescaling argument, without claiming that the already-established critical fixed-ratio Fermat–Torricelli theorem is new.

## Proof
Put \(s_i=\|v_i\|>0\), \(d_i=\|v_j-v_k\|\), where \(\{i,j,k\}=\{1,2,3\}\), and \(S=s_1+s_2+s_3\), \(D=d_1+d_2+d_3\). Since \(v_i+v_j+v_k=0\),
\[
3v_i=(v_i-v_j)+(v_i-v_k),\qquad 3s_i\le d_j+d_k.
\]
Sum over \(i\) to obtain \(3S\le2D\). On the other hand \(D\le R S\). Thus \(R\ge3/2\).

Suppose \(R=3/2\). Both inequalities above are equalities, so each \(d_i=(3/2)s_i\) and each \(3s_i=d_j+d_k\). Therefore
\[
3s_i=\frac32(S-s_i),\qquad s_1=s_2=s_3=:s>0,
\]
and \(d_1=d_2=d_3=3s/2\). Write \(u_i=v_i/s\), and let
\[
p_1=\frac23(u_1-u_2),\quad p_2=\frac23(u_2-u_3),\quad p_3=\frac23(u_3-u_1).
\]
All \(p_i\), their negatives, and all \(u_i\) have norm one. The six distinct points \(\pm p_1,\pm p_2,\pm p_3\) are the vertices of an affine-regular hexagon \(H\). Indeed, in the linear coordinates \(u_1=(1,0)\), \(u_2=(0,1)\), \(u_3=(-1,-1)\), their ordered vertex coordinates are
\[
(2/3,-2/3),\ (4/3,2/3),\ (2/3,4/3),\ (-2/3,2/3),\ (-4/3,-2/3),\ (-2/3,-4/3).
\]
The vectors \(u_1,u_2,u_3\) are midpoints of three alternating edges (and their negatives are midpoints of the other three). For example, \(u_1=(p_1-p_3)/2\); the other two identities follow cyclically. As all vertices \(\pm p_i\) have norm one, \(H\subseteq B_Y\). At each midpoint \(\pm u_i\), which has norm one, choose a norm-one supporting functional of \(B_Y\). It also supports \(H\) at the interior of the corresponding edge and therefore supports the entire edge. The six resulting edge-supporting half-planes intersect in exactly \(H\). Thus \(B_Y\subseteq H\), proving \(B_Y=H\).

Conversely, in the plane with \(B_Y=\operatorname{conv}\{\pm(2/3,-2/3),\pm(2/3,4/3),\pm(-4/3,-2/3)\}\), choose \(u_1=(1,0)\), \(u_2=(0,1)\), \(u_3=(-1,-1)\). They are alternate edge midpoints, so \(\|u_i\|=1\); their opposite differences are \(3/2\) times unit vertices, so \(\|u_i-u_j\|=3/2\). This witnesses equality. Every affine-regular hexagon is linearly isometric to this norm after an appropriate coordinate choice and common scaling, giving the converse and the last assertion.

## Verification
The enclosed `checker.py` reconstructs the canonical hexagon with exact rational vertices, verifies the six unit vertices, three unit edge midpoints, and three opposite differences of norm \(3/2\) through exact signed support-function inequalities. The universal lower bound and equality implication are proved analytically above; finite checks are not substitutes for the proof. The midpoint-support argument does not invoke any computational extrapolation.

## Relationship to prior work
Fang and Liu, *The Fermat–Torricelli problem under isosceles orthogonality-type conditions* (arXiv:2611.13648v1, first posted 10 November 2026), prove the general \(3/2\) lower bound in Lemma 3 and a fixed-ratio characterization for parameters strictly above \(2/3\). The specific equality geometry of that lemma is not stated in the inspected full text. The critical endpoint characterization itself is already present in earlier mathematical findings and is **not** asserted here. The result characterizes exactly the planar configuration saturating the numerical bound, rather than extending the endpoint characterization. Related literature on affine-regular hexagonal normed planes treats other geometric constants, without implying this equality classification by statement alone.

## Limitations
The conclusion concerns **exact equality**, not a dimension-free quantitative closeness theorem for near-equality triples. No result is claimed about a Fermat–Torricelli endpoint not already settled elsewhere. The literature comparison is bounded by available texts; older geometric characterizations expressed in different terminology remain a residual originality risk. No independent mathematical audit has been performed.

## References
1. Z. Fang and Q. Liu, *The Fermat–Torricelli problem under isosceles orthogonality-type conditions*, arXiv:2611.13648v1 (10 November 2026), https://arxiv.org/html/2611.13648v1, especially Lemma 3.
2. H. Martini, K. J. Swanepoel and G. Weiß, *The Fermat–Torricelli problem in normed planes and spaces*, J. Optim. Theory Appl. 115 (2002), 283–314; arXiv:0707.2592.
3. T. Pakhrou, *Location problem and inner product spaces*, J. Funct. Anal. 285 (2023), 110078, https://doi.org/10.1016/j.jfa.2023.110078.
