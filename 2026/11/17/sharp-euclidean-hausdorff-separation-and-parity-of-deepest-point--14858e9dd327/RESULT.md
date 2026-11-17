# Sharp Euclidean Hausdorff separation and parity of deepest points for Catalan matroid polytopes

## Finding

For every integer \(n\ge 2\), define the standard hypersimplex and the Catalan matroid base polytope by
\[
\Delta_{n,2n}=\{x\in[0,1]^{2n}:\sum_{i=1}^{2n}x_i=n\},\qquad
P_n=\operatorname{conv}\{\mathbf1_B:B\subseteq[2n],\ |B|=n,\ 2|B\cap[j]|\ge j\text{ for all }1\le j\le 2n\}.
\]
Both use the ordinary inherited Euclidean metric in \(\mathbb R^{2n}\), **not** a rescaled or affine-equivalent realization. Then
\[
\boxed{d_H(\Delta_{n,2n},P_n)^2=\left\lfloor\frac{n+3}{2}\right\rfloor.}
\]
For **odd** \(n\), the unique point of the entire hypersimplex attaining this distance is the binary vertex \((0^n,1^n)\). For **even** \(n\), the complete farthest-point locus is the **closed edge** connecting this vertex to the vertex obtained by interchanging its two middle coordinates, which are initially \((0,1)\). In particular, for even \(n\), every interior point of that edge also attains the Hausdorff distance; there are no other maximizers.

All farthest-point projections are explicit. Put
\[
C_n=\{y:y_1=1,\ y_{2n}=0,\ y_{2j}+y_{2j+1}=1\ (1\le j<n),\ 0\le y_i\le1\}.
\]
This is an exposed \((n-1)\)-cube face of \(P_n\). At a farthest vertex, its unique closest point in \(P_n\) is obtained by setting the first and last coordinates to \(1,0\), replacing each middle pair \((0,0)\) or \((1,1)\) by \((1/2,1/2)\), and retaining a mixed middle pair, if one exists. For even \(n\), these two closest points move affinely along an edge of \(C_n\), and their displacement vector from the respective farthest points remains constant.

As a scale comparison, \(\operatorname{diam}(\Delta_{n,2n})=\sqrt{2n}\), so the Hausdorff gap is asymptotically one half of the hypersimplex diameter. This is a statement about an extrinsic gap, not an inradius or a facet-distance invariant.

## Assumptions and scope

A Dyck word consists of \(n\) up-steps, encoded by \(1\), and \(n\) down-steps, encoded by \(0\), with nonnegative cumulative height \(2\sum_{i\le j}x_i-j\) at every prefix. The Catalan matroid, introduced by Ardila, has precisely these up-step sets as bases. The coordinate hyperplane \(x_1=1\) and \(x_{2n}=0\) holds identically on \(P_n\) but not on the containing hypersimplex. Distances and projections here are computed in the full common ambient coordinate space. The directed distance from \(P_n\) to \(\Delta_{n,2n}\) is zero because \(P_n\subseteq\Delta_{n,2n}\).

The claim covers all integers \(n\ge2\) and all points of the continuous hypersimplex; it does not claim a full nearest-point formula for arbitrary points away from the farthest locus.

## Proof

**1. A canonical exposed cube.** Every Dyck word begins with \(1\) and ends with \(0\), and satisfies \(\sum_{i=1}^{2j+1}y_i\ge j+1\) for \(0\le j<n\). Simultaneously imposing equality at these odd-prefix support hyperplanes gives exactly \(C_n\): after the initial \(1\), each pair \((2j,2j+1)\) sums to one, and the final coordinate is zero. Conversely, every binary word satisfying those equalities is Dyck: after an odd prefix it has height one, and the intervening even prefix has height either zero or two. Thus the indicated cube is the convex hull of \(2^{n-1}\) actual Dyck bases, and is an exposed face (an intersection of supporting faces) of \(P_n\).

**2. Exact distance to this cube.** Given \(x\in\Delta_{n,2n}\), its unique Euclidean projection \(c(x)\) to \(C_n\) fixes the first and last coordinates at \(1,0\) and independently projects each middle pair \((x_{2j},x_{2j+1})\) onto the segment of coordinate sum one. The projected pair is
\[
\left(\frac{1+x_{2j}-x_{2j+1}}2,\frac{1-x_{2j}+x_{2j+1}}2\right);
\]
these entries lie in \([0,1]\), so no clipping is required. Consequently
\[
\operatorname{dist}_2(x,C_n)^2=(1-x_1)^2+x_{2n}^2+
\frac12\sum_{j=1}^{n-1}(x_{2j}+x_{2j+1}-1)^2.\tag{1}
\]
As \(C_n\subseteq P_n\), the squared distance to \(P_n\) is at most (1).

**3. Sharp upper bound at all hypersimplex vertices.** Let \(x\) now be binary with precisely \(n\) ones, and put \(u=x_1\), \(v=x_{2n}\). Among its \(n-1\) middle pairs let \(a,b,c\) count the types \(00,11,\text{mixed}\), respectively. Counting all ones yields
\[
a+b+c=n-1,\qquad b-a=1-u-v.\tag{2}
\]
Equation (1) becomes
\[
\operatorname{dist}_2(x,C_n)^2=(1-u)+v+\frac{n-1-c}{2}.\tag{3}
\]
If \((u,v)\ne(0,1)\), this is at most \(1+(n-1)/2\), strictly smaller than \(R_n^2=\lfloor(n+3)/2\rfloor\). If \((u,v)=(0,1)\), equation (2) forces \(a=b\), so \(c\equiv n-1\pmod2\). Thus \(c\ge0\) for odd \(n\), or \(c\ge1\) for even \(n\). It follows that (3) is at most \(R_n^2\), with equality only if the first and last bits are \(0,1\) and the middle pairs have equally many \(00\) and \(11\), together with no mixed pair (odd \(n\)) or precisely one mixed pair (even \(n\)). Since squared distance to a nonempty closed convex set is convex, the vertex upper bound extends to every point of the hypersimplex.

**4. Only correctly ordered candidate vertices can be farthest.** For an equality candidate from step 3, let \(y=c(x)\), and write \(w=x-y\). Its first and last entries are \(-1,+1\); its two entries in each middle pair are equal to a scalar \(t_j\in\{-1/2,0,+1/2\}\), with values \(-1/2,0,+1/2\) corresponding respectively to pair types \(00,\text{mixed},11\).

Suppose some earlier pair \(j\) has \(t_j>t_k\) for a later pair \(k\). Choose a Dyck vertex \(z\in P_n\) with first and last entries \(1,0\), pair \(j\) equal to \(11\), pair \(k\) equal to \(00\), and all other middle pairs summing to one. This is Dyck: its odd-prefix heights are one except for the intervening block, where they are three; the even-prefix heights remain nonnegative. Since every pair of \(y\) sums to one,
\[
w\cdot(z-y)=t_j-t_k>0.
\]
Hence \(y\) is *not* the projection of \(x\) onto \(P_n\), and \(\operatorname{dist}_2(x,P_n)^2<\operatorname{dist}_2(x,C_n)^2\). Therefore the pair types must be ordered as all \(00\), then the optional single mixed pair, then all \(11\). For odd \(n\), this forces the unique reversed word \((0^n,1^n)\). For even \(n\), the only freedom is the orientation of the single central mixed pair, giving exactly the two vertices stated.

**5. The two or one candidates really attain the bound.** Let \(x\) be one of these ordered candidates, \(y=c(x)\), and retain \(w=x-y\) and the now nondecreasing scalars \(t_1\le\cdots\le t_{n-1}\). For any \(z\in P_n\), set
\[
\delta_j=z_{2j}+z_{2j+1}-1,\qquad S_k=\sum_{j=1}^k\delta_j.
\]
The odd-prefix Dyck inequalities, together with \(z_1=1\), imply \(S_k\ge0\). The sum condition and \(z_{2n}=0\) imply \(S_{n-1}=0\). Accordingly, discrete summation by parts gives
\[
w\cdot(z-y)=\sum_{j=1}^{n-1}t_j\delta_j
=-\sum_{j=1}^{n-2}(t_{j+1}-t_j)S_j\le0.\tag{4}
\]
The fixed endpoints make no contribution to the first equality. The variational characterization of orthogonal projection onto a closed convex set now proves that \(y\) is the **unique** closest point of \(P_n\) to \(x\). Equation (3) gives \(\|x-y\|_2^2=R_n^2\).

**6. Every continuous maximizer.** For any convex decomposition \(x=\sum_h\lambda_h v_h\) into hypersimplex vertices, convexity of squared distance gives
\[
\operatorname{dist}_2(x,P_n)^2\le\sum_h\lambda_h\operatorname{dist}_2(v_h,P_n)^2\le R_n^2.
\]
Equality requires each positively weighted vertex to be one of those found in steps 4–5. For odd \(n\), their convex hull is a single vertex. For even \(n\), it is the edge between the two candidates. Their projection points differ only within the central mixed pair, while their residual vector \(w\) is identical. The projection inequality (4) remains valid for every affine interpolation of those two points, so every point of that edge has squared distance exactly \(R_n^2\). No other continuous maximizer exists.

Finally, two disjoint complementary \(n\)-sets give hypersimplex diameter \(\sqrt{2n}\), proving the comparison in the Finding section.

## Verification

The standalone `check_catalan_distance.py` independently constructs the Catalan feasible set as a bounded quadratic program using fixed endpoints, the remaining coordinate-sum equality, coordinate bounds, and odd-prefix ballot inequalities. For every \(n=2,3,4,5,6\), it enumerates **all** \(\binom{2n}{n}\) binary hypersimplex vertices, solves their Euclidean projection problems numerically, checks the maximum and its parity-sensitive maximizing vertices, and verifies exact support-vector inequalities against every Dyck vertex. It additionally tests interior points of the even-rank deepest edge and checks the symbolic normal order and squared residual through \(n=40\). Run with Python, NumPy, and SciPy:

```bash
python check_catalan_distance.py
```

A successful finite check is not a substitute for the unrestricted proof above; the numerical optimizer is subject to floating-point tolerance.

## Relationship to prior work

Ardila's original Catalan-matroid paper establishes the Dyck-path basis structure. Bidkhori and An–Jung–Kim study lattice-path matroid polytopes and their faces. Benedetti–Knauer–Valencia-Porras study alcoved triangulations, snake subdivisions, Gorenstein properties, and Ehrhart-related invariants. An independently published exact Euclidean **inradius/incenter** result for Catalan matroid polytopes addresses a different metric optimization problem in the affine hull. None of these cited results, in the portions inspected, supplies the present extrinsic Hausdorff gap or classifies all deepest points of the hypersimplex. Inradius formulas, face descriptions and triangulations do not by themselves imply the distances to a larger hypersimplex. The exposed cube is described directly here; any known combinatorial identification of such a face is not claimed as original by itself.

## Limitations

The novelty assessment concerns the particular exact Euclidean Hausdorff distance, parity-dependent farthest-point locus, and their explicit projections, not the existence of Catalan matroids, their inequality model, or the standard convexity/projection lemmas. This does **not** give nearest-point projections for all hypersimplex points. No independent review has been performed. An equivalent earlier result under ballot-path, matroid proximity, or quadratic projection terminology remains a bibliographic risk.

## References

1. Federico Ardila, *The Catalan matroid*, arXiv:math/0209354v1 (25 September 2002), especially Section 2; DOI: 10.1016/S0097-3165(03)00121-3.
2. Hoda Bidkhori, *Lattice Path Matroid Polytopes*, arXiv:1212.5705v1 (22 December 2012), especially Sections 2–4.
3. Suhyung An, JiYoon Jung, Sangwook Kim, *Facial structures of lattice path matroid polytopes*, arXiv:1701.00362v1 (2 January 2017), especially Sections 3–5.
4. Carolina Benedetti, Kolja Knauer, Jerónimo Valencia-Porras, *On lattice path matroid polytopes: alcoved triangulations and snake decompositions*, arXiv:2303.10458v1 (18 March 2023), especially Sections 1–4.
5. *A dimension-stable inball and codimension-four incenter family for Catalan matroid polytopes*, published research record, 2026, published-finding corpus identifier `2026/11/8/SCOPE-a-dimension-stable-inball-and-codimension-four-incenter-family-f--f5bcefc8b90a` (a distinct inradius result).
