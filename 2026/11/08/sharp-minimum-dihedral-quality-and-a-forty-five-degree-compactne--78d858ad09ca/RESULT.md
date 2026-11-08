# Sharp minimum-dihedral quality and a forty-five-degree compactness transition for path tetrahedra

## Finding

For positive real numbers \(a,b,c\), let
\[
T(a,b,c)=\operatorname{conv}\{(0,0,0),(a,0,0),(a,b,0),(a,b,c)\}\subset\mathbb R^3.
\]
Define \(\delta(T)\) to be the smallest *interior dihedral angle* among its six edges. Put
\[
\varphi=\frac{1+\sqrt5}{2},\qquad
\theta_*=\arccos(\varphi^{-1})=0.9045568943023814\ldots\quad\text{radians}.
\]
Then the sharp upper bound over all nondegenerate path tetrahedra is
\[
\max_{a,b,c>0}\delta(T(a,b,c))=\theta_*,
\]
with equality exactly when \(a:c:b=\sqrt\varphi:\sqrt\varphi:1\). Thus this is a unique similarity class, up to reversing the orthogonal edge path.

More precisely, let \(t\in(0,\theta_*]\), and normalize the consecutive perpendicular edge lengths by \(x=a/b\), \(y=c/b\). Then \(\delta(T)\ge t\) if and only if
\[
 x\ge\tan t,\qquad y\ge\tan t,\qquad
 \frac{xy}{\sqrt{(1+x^2)(1+y^2)}}\le\cos t. \tag{1}
\]
For \(t>\pi/4\), the allowed shape parameters in (1) satisfy the *sharp individual bounds*
\[
 \tan t\le x,y\le U(t):=\frac{\cos t}{\sqrt{\sin^2t-\cos^2t}}. \tag{2}
\]
Each upper bound is attained for some tetrahedron with \(\delta(T)=t\). In contrast, for every \(0<t\le\pi/4\), the feasible set (1) is unbounded in each coordinate. Consequently the nonempty normalized shape superlevel sets undergo an exact noncompact-to-compact transition at \(t=\pi/4\) and collapse to one point at \(t=\theta_*\). For \(t>\theta_*\), the superlevel set is empty.

## Assumptions and scope

The tetrahedra are Euclidean and nondegenerate, with three consecutive *mutually perpendicular* edges of positive lengths. Their shape is determined up to similarity by the positive ratios \(x=a/b\) and \(y=c/b\). The dihedral quality \(\delta\) is an **angle**, not a vertex solid angle or sum of dihedral angles. Dihedral angles lie in \((0,\pi)\) and are measured internally. No constraint on volume, circumradius, or total edge length is imposed.

## Proof

**1. Exact six angles.** The outward-normal calculation for the four triangular faces, or direct use of the scalar products of their normals, yields three right dihedrals and the three remaining angles
\[
 \alpha=\arctan x,\qquad \gamma=\arctan y,\qquad
 \beta=\arccos\frac{xy}{\sqrt{(1+x^2)(1+y^2)}}
      =\arccos(\sin\alpha\sin\gamma).\tag{3}
\]
For completeness, with vertices \(O=(0,0,0)\), \(A=(a,0,0)\), \(B=(a,b,0)\), \(C=(a,b,c)\), the dihedrals at \(OA\), \(BC\), \(OC\) are \(\arctan y\), \(\arctan x\), and \(\beta\), respectively. The other three are \(\pi/2\). Since each of \(\alpha,\beta,\gamma\) is in \((0,\pi/2)\),
\[
\delta(T)=\min\{\alpha,\gamma,\beta\}.\tag{4}
\]

**2. Exact feasible shapes.** For any \(t\in(0,\pi/2)\), (4) is at least \(t\) exactly when \(\alpha,\gamma\ge t\) and \(\beta\ge t\). Monotonicity of tangent, sine, and cosine on the indicated angular ranges makes these conditions equivalent to (1).

**3. Sharp global maximum and rigidity.** If \(\delta(T)\ge t\), then \(\alpha,\gamma\ge t\), and hence \(\sin\alpha\sin\gamma\ge\sin^2t\). Simultaneously \(\beta\ge t\), so by (3) \(\sin\alpha\sin\gamma\le\cos t\). Thus \(\sin^2t\le\cos t\). Letting \(u=\cos t\in(0,1)\), this is \(1-u^2\le u\), i.e. \(u^2+u-1\ge0\). Hence \(u\ge\varphi^{-1}\), or \(t\le\theta_*\). Equality forces \(\alpha=\gamma=\theta_*\): strict monotonicity of sine rules out either angle being larger. The identity \(\sin^2\theta_*=\cos\theta_*\) gives \(\beta=\theta_*\), so the bound is attained. Finally,
\[
 \tan^2\theta_*=\frac{\sin^2\theta_*}{\cos^2\theta_*}
 =\frac{1}{\cos\theta_*}=\varphi,
\]
so the only maximizing normalized shape is \(x=y=\sqrt\varphi\), proving unique optimal similarity class.

**4. Compactness transition and sharp coordinate bounds.** Suppose \(\delta(T)\ge t\) and \(t>\pi/4\). Since \(\sin\gamma\ge\sin t\), (3) and \(\beta\ge t\) imply \(\sin\alpha\le\cot t<1\), and similarly \(\sin\gamma\le\cot t\). Because \(\alpha,\gamma\in(0,\pi/2)\), converting the sine bound into a tangent bound gives precisely the two right-hand inequalities in (2). The left-hand inequalities are (1). Both coordinate upper bounds are sharp: choose \(\gamma=t\) and \(\alpha=\arcsin(\cot t)\). The latter satisfies \(\alpha\ge t\) for \(t\le\theta_*\), because \(\sin^2t\le\cos t\), while (3) gives \(\beta=t\). Swapping \(\alpha,\gamma\) proves sharpness for the other coordinate. The allowed region is closed in the positive \((x,y)\)-plane, and (2) makes it bounded, hence compact.

When instead \(0<t\le\pi/4\), choose \(\gamma=t\) and take \(\alpha\to\pi/2\), i.e. \(x\to+\infty\). Then \(\sin\alpha\sin\gamma\le\sin t\le\cos t\), so \(\beta\ge t\) and \(\delta(T)\ge t\). The same argument with the roles reversed makes \(y\) arbitrarily large. At the endpoint \(\theta_*\), (2) gives \(U(\theta_*)=\tan\theta_*=\sqrt\varphi\), so the feasible region collapses to the unique optimizing shape. This proves all assertions.

## Verification

Run `python3 check_path_tetra.py` with Python 3 and no third-party packages. The independent computation uses outward unit face normals, not just the derivation (3), and checks agreement of all six dihedrals on \(2500\) deterministic pseudorandom tetrahedra. It also tests the feasibility predicate, the sharp maximum and equality configuration, and \(1000\) near- and post-transition boundary constructions. Its expected output is `PATH_TETRA_DIHEDRAL_CHECKS_OK 9506`. These finite checks supplement the proof; they do not certify universal quantifiers. The proof above is self-contained once elementary trigonometry and Euclidean face normals are accepted.

## Relationship to prior work

Korotov and Křížek (2026), Section 2, define the same path tetrahedra, calculate their dihedral angles, and establish optimal bounds for the **sum** of dihedral angles. Formula (3) is their established geometric ingredient. This result instead maximizes the **minimum** angle and completely describes its shape superlevel sets, including the sharp compactness threshold. These conclusions are not stated in their inspected Section 2. Brandts, Korotov, and Křížek (2020) treat path tetrahedra as elements of nonobtuse simplicial partitions. Numerical mesh-quality studies use minimum dihedral angle as a distinct quality criterion. The published minimum-**solid**-angle optimization of the same orthoscheme family concerns spherical vertex angles, not dihedral angles, and its optimizer has different edge ratios; no conclusion here is obtained by converting a solid-angle theorem.

## Limitations

This result applies only to path tetrahedra. It does not maximize the minimum dihedral angle among all tetrahedra, does not assess global mesh conformity or shape-regularity under subdivision, and does not establish a mesh convergence theorem. The maximizing shape is one local quality criterion rather than a universal preferred tetrahedral element. Priority remains subject to older specialist FEM and orthoscheme geometry literature; source access was not exhaustive. No independent mathematical audit has been performed.

## References

1. S. Korotov and M. Křížek, *Two-sided bounds for dihedral angle sums of path and 4-ball tetrahedra*, arXiv:2601.08304v1, first posted 2026-01-13; https://arxiv.org/html/2601.08304v1 (especially Section 2).
2. J. Brandts, S. Korotov, and M. Křížek, *Simplicial Partitions with Applications to the Finite Element Method*, Springer, 2020; DOI: 10.1007/978-3-030-55677-8.
3. *An efficient method to improve the quality of tetrahedron mesh with MFRC*, *Scientific Reports* 11 (2021), DOI: 10.1038/s41598-021-02187-1; a contemporary example treating minimum dihedral angle as a mesh-quality metric.
