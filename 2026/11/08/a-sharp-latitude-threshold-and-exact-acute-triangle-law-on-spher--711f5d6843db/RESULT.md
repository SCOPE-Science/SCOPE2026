# A sharp latitude threshold and exact acute-triangle law on spherical small circles

## Finding

Let \(0<\theta<\pi\), let \(C_\theta=\{(\sin\theta\cos t,\sin\theta\sin t,\cos\theta):0\le t<2\pi\}\subset S^2\), and sample three points independently and uniformly in arclength on \(C_\theta\). Join them by the shorter great-circle arcs. Define \(p(\theta)\) as the probability that **all three intrinsic spherical interior angles** are strictly less than \(\pi/2\). Put \(\lambda=\cos^2\theta\).

**Theorem.** The probability vanishes identically when \(\lambda\le1/3\); it is strictly positive and strictly increasing in \(\lambda\) on \((1/3,1)\), and its range there is \((0,1/4)\). An exact one-dimensional integral for every \(1/3<\lambda<1\) is as follows. Set
\[
K=\frac{1+\lambda}{1-\lambda},\quad r=2\arcsin(K^{-1}),\quad
q_0=\begin{cases}
2\arcsin\sqrt{(3-K)/4},&2<K<3,\\
0,&K\ge3.
\end{cases}
\]
Then
\[
\boxed{p(\theta)=\frac3{\pi^2}\left\{\frac\pi2\left(\frac\pi3-q_0\right)
-\frac34\left(\frac{\pi^2}9-q_0^2\right)
-\int_{q_0}^{r}\arccos\left(K\sin\frac q2\right)\,dq\right\}.}
\]
In particular \(p(\theta)=0\) precisely in the closed latitude belt \(|\cos\theta|\le1/\sqrt3\). The probability has the sharp quadratic onset
\[
\boxed{p(\theta)=\frac{243}{16\pi^2}\left(\cos^2\theta-\frac13\right)^2
+o\!\left(\left(\cos^2\theta-\frac13\right)^2\right)}
\]
as \(\cos^2\theta\downarrow1/3\). Moreover \(p(\theta)\to1/4\) as \(\theta\to0\) or \(\theta\to\pi\). Thus a **positive** acute-triangle probability determines \(|\cos\theta|\) uniquely; zero probability does not determine a latitude inside the belt.

## Assumptions and scope

The sphere has unit radius and the small circle is a fixed parallel of colatitude \(\theta\), not a spherical cap and not the whole sphere. Sampling is independent with uniform angular longitude (equivalently arclength along that small circle). Interior angles are formed by the *shorter spherical geodesics*; they are not the Euclidean angles of the chord triangle in ambient three-space. The endpoints \(\theta=0,\pi\) are excluded because their circles collapse to a point. Boundary configurations and longitude ties have probability zero.

## Proof

**1. From tangent vectors to circular gaps.** By rotation invariance, take a vertex at longitude zero and neighbors at longitudes \(-a\) and \(b\), where \(a,b\in(0,\pi)\). Write \(z=\cos\theta\), so \(\lambda=z^2\), and let \(X,Y,Z\) denote these three points. The signs of the intrinsic angle at \(X\) and of
\[
(Y-X(X\cdot Y))\cdot(Z-X(X\cdot Z))=(Y\cdot Z)-(X\cdot Y)(X\cdot Z)
\]
coincide. Elementary expansion of the dot products gives
\[
(Y\cdot Z)-(X\cdot Y)(X\cdot Z)
=(1-\lambda)\big[\lambda(1-\cos a)(1-\cos b)-\sin a\sin b\big].
\]
Since \(a,b\in(0,\pi)\), the angle is acute precisely when
\[
\lambda\tan(a/2)\tan(b/2)>1. \tag{1}
\]
Order the three random longitudes cyclically and let \(g_1,g_2,g_3>0\) be the successive clockwise gaps, with \(g_1+g_2+g_3=2\pi\). If a gap is at least \(\pi\), the other two gaps \(a,b\) are less than \(\pi\) and satisfy \(a+b\le\pi\); their tangents have product at most one, contradicting (1) because \(\lambda<1\). Hence all-acute implies \(0<g_i<\pi\) for every \(i\). Conversely, within that region, the condition (1) at each of the three vertices is necessary and sufficient.

Put \(q_i=\pi-g_i\in(0,\pi)\), so \(q_1+q_2+q_3=\pi\), and \(w_i=\tan(q_i/2)>0\). The identity \(\cos((q_1+q_2+q_3)/2)=0\) gives
\[
 w_1w_2+w_2w_3+w_3w_1=1.\tag{2}
\]
Since \(\tan(g_i/2)=1/w_i\), all three angles are acute if and only if
\[
\max\{w_1w_2,w_2w_3,w_3w_1\}<\lambda.\tag{3}
\]
By (2), the maximum is at least \(1/3\), with equality only when \(q_1=q_2=q_3=\pi/3\). This proves vanishing at and below the threshold and positivity above it.

**2. Exact probability integral.** Fix one sampled vertex as cyclic origin and sort the other two relative longitudes. The first two clockwise gaps are uniform on the open two-dimensional simplex \(g_i>0,\sum g_i=2\pi\) with joint density \(1/(2\pi^2)\) in coordinates \((g_1,g_2)\). The same constant density holds for \((q_1,q_2)\). By sixfold symmetry restrict to \(0<q_1\le q_2\le q_3\) and write
\[
q_2=\frac{\pi-q_1}{2}-d,\qquad q_3=\frac{\pi-q_1}{2}+d,
\qquad 0\le d\le \frac{\pi-3q_1}{2},\quad 0<q_1\le\pi/3.
\]
This change of coordinates has absolute Jacobian one. As \(w_1\le w_2\le w_3\), condition (3) reduces to \(w_2w_3<\lambda\). Writing \(K=(1+\lambda)/(1-\lambda)\), the tangent product identity yields
\[
 w_2w_3=\frac{\cos d-\sin(q_1/2)}{\cos d+\sin(q_1/2)},
\quad\text{so}\quad
 w_2w_3<\lambda\iff \cos d<K\sin(q_1/2).\tag{4}
\]
For fixed \(q_1\), the admissible \(d\)-interval starts at \(\arccos(K\sin(q_1/2))\) when the arccosine argument lies in \((0,1)\), and at zero once that argument reaches one. The former interval is nonempty precisely when
\[
K\sin(q_1/2)>\sin(3q_1/2).
\]
Using \(\sin3x=3\sin x-4\sin^3x\), this is equivalent to \(q_1>q_0\) for \(2<K<3\); for \(K\ge3\) it holds for all positive \(q_1\). The cutoff at which the arccosine becomes zero is \(r=2\arcsin(1/K)\). Integrating the allowed interval lengths with density \(6/(2\pi^2)=3/\pi^2\) gives exactly the displayed formula. Its integral is real-valued since \(0\le K\sin(q/2)\le1\) on \([q_0,r]\).

**3. Strict monotonicity and inverse information.** Increasing \(\lambda\) strictly enlarges the event (3). The maximum in (3) attains every value in \((1/3,1)\): take \(q_1=q_2=t\) and \(q_3=\pi-2t\), with \(\pi/3<t<\pi/2\). Then \(\max(w_iw_j)=\tan^2(t/2)\), which moves continuously from \(1/3\) to one. Nearby configurations have positive area. Thus the probability increases strictly. As \(\lambda\uparrow1\), (3) holds for every \(q_i>0\) summing to \(\pi\); that simplex occupies probability \(1/4\), as is also seen by the integral limit. Hence the range and inverse statement follow.

**4. Exact critical coefficient.** Let \(\delta=\lambda-1/3>0\) and put \(q_i=\pi/3+x_i\), where \(x_1+x_2+x_3=0\). A Taylor expansion at the unique threshold configuration gives, uniformly near the origin,
\[
w_iw_j=\frac13-\frac{2}{3\sqrt3}x_k+O(\|x\|^2),\qquad \{i,j,k\}=\{1,2,3\}.
\]
Consequently the small feasible region, rescaled by \(\delta^{-1}\), converges to the triangle \(x_k>-(3\sqrt3/2)\delta\) for all \(k\). Its \((x_1,x_2)\)-area is \(243\delta^2/8\). Compactness away from the symmetric configuration and (2) exclude other near-threshold regions. Multiplying by the simplex density \(1/(2\pi^2)\) proves the stated coefficient \(243/(16\pi^2)\).

## Verification

The accompanying `latitude_acute_verify.py` numerically evaluates the one-dimensional integral at nine parameter values, then independently samples 300,000 triples and tests the *three projected tangent-vector dot products directly*, without using the gap criterion (3). The calculation also compares the quadratic-onset ratio at five positive perturbations. The program prints `LATITUDE_ACUTE_CHECK_OK` on success. The computation is supplementary: the algebraic gap reduction, exact integral and asymptotic expansion above are the proof.

## Relationship to prior work

Finch and Jones (2010) study spherical triangles from **full-sphere uniform** vertices, chiefly area and perimeter distributions; their sample space is different. Maeda (2008) classifies spherical-triangle types for full-sphere uniform sampling. Kim and Walsh (2015) prove that all edges of a spherical triangle with acute interior angles are shorter than \(\pi/2\) (their Corollary 4.2), which supplies a useful general necessary condition but not the probability law or quadratic onset for boundary-circle sampling. Le (1989) provides shape densities for vertices sampled from the **interior of a spherical cap**, again not the fixed boundary small circle. Edelman and Strang (2015) study Euclidean random triangle shape models, not intrinsic angles between sphere geodesics. In particular, the classical probability \(1/4\) for an acute triangle inscribed in a Euclidean circle is the **degenerate small-circle limit** here, not the threshold or the positive-latitude law.

The new aspect is the exact one-parameter spherical-small-circle law together with its forbidden-latitude belt, strict inverse statement and sharp quadratic onset. Historical priority is provisional; the full text of Le (1989) was not accessible in this check. Its cap-interior sampling does not by itself state or imply the fixed-boundary calculation.

## Limitations

No claim is made for Euclidean chord angles in \(\mathbb R^3\), for uniform points in a spherical cap, or for arbitrary nonuniform longitude sampling. The exact expression is a convergent **one-dimensional definite integral**, not an asserted elementary closed form. The asymptotic coefficient applies only as \(\lambda\downarrow1/3\) from above. An observed zero probability is compatible with every latitude in the forbidden belt. External priority verification remains open.

## References

1. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, originally posted 2010-09-27. https://arxiv.org/abs/1009.5329
2. Y. Maeda, *Seven Types of Random Spherical Triangle in S\(^{n}\) and Their Probabilities*, in *Computational Geometry and Graph Theory*, Lecture Notes in Computer Science 4535 (2008), 119–126. https://doi.org/10.1007/978-3-540-89550-3_13
3. H. Le, *Random spherical triangles II: Shape densities*, *Advances in Applied Probability* 21 (1989), 581–594. https://doi.org/10.1017/S0001867800018826
4. S.-h. Kim and G. S. Walsh, *Coxeter groups, hyperbolic cubes and acute triangulations*, *Journal of Topology* 9 (2016), 117–142; first published 2015-12-14. https://doi.org/10.1112/jtopol/jtv038
5. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053, originally posted 2015-01-09. https://arxiv.org/abs/1501.03053
