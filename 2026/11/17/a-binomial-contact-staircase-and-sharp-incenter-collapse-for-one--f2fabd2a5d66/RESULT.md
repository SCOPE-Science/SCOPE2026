# A binomial contact staircase and sharp incenter collapse for one-cluster ultrametrics

## Finding
For each integer \(m\ge3\) and real \(0<t<1\), take a point \(o\) and an equilateral cluster \(a_1,\ldots,a_m\), with \(d(o,a_i)=1\) and \(d(a_i,a_j)=t\) whenever \(i\ne j\). Embed the real Lipschitz-free unit ball \(P_{m,t}\) canonically into the zero-sum hyperplane of \(\mathbb R^{m+1}\), equipped with its ordinary Euclidean norm. Put
\[
Q_{m,t}(k)=m(1-t)^2+k(2t-t^2)-\frac{[m(1-t)+kt]^2}{m+1},\qquad 1\le k\le m,
\]
and
\[
\alpha_{m,t}=\frac{m-1}{2}+\frac1t,\qquad
\mathcal K_{m,t}=\operatorname*{argmin}_{1\le k\le m,\ k\in\mathbb Z}|k-\alpha_{m,t}|.
\]
Then the globally largest Euclidean inscribed ball is attained at the origin and has **exact radius**
\[
\boxed{r_{m,t}=\left(\max_{1\le k\le m}Q_{m,t}(k)\right)^{-1/2}
       =\left(\max_{k\in\mathcal K_{m,t}}Q_{m,t}(k)\right)^{-1/2}.}
\]
The complete number of facets tangent to this origin-centered maximum ball is
\[
\boxed{T_{m,t}=2\sum_{k\in\mathcal K_{m,t}}\binom mk.}
\]
The affine dimension of the set of *all centers* of radius-\(r_{m,t}\) balls is
\[
\boxed{\dim_{\rm aff}\mathcal I_{m,t}=
\begin{cases}m-1,&0<t<2/m,\\0,&2/m\le t<1.\end{cases}}
\]
Thus a positive-dimensional family of incenters collapses to a **unique center exactly at \(t=2/m\)**. For \(0<t<2/m\) the simpler formulas \(r_{m,t}=\sqrt{(m+1)/m}\), \(T_{m,t}=2\) hold. At the transition \(t=2/m\), the contacts jump to \(T_{m,2/m}=2(m+1)\). Other precise two-level tie walls are \(t=2/(2k-m+2)\) for integers \(\lfloor m/2\rfloor<k<m-1\) whenever the right side lies in \((0,1)\); the preceding binomial formula covers all such walls.

## Assumptions and scope
The metric has \(m+1\) labeled points and is a two-level ultrametric for every \(0<t<1\). Use the real vector space
\[
H=\left\{\mu\in\mathbb R^{m+1}:\sum_{x\in M_{m,t}}\mu_x=0\right\}
\]
with the standard inherited Euclidean inner product. Its Lipschitz-free unit ball is the convex hull of the normalized molecules \((e_x-e_y)/d(x,y)\), over distinct points. Its polar in \(H\) consists of centered one-Lipschitz potential vectors \(v=f-(\sum_x f(x)/(m+1))\mathbf1\), where potentials are identified modulo constants. Fix \(f(o)=0\); then the bounded polytope of potentials is
\[
K_{m,t}=\left\{(f_1,\ldots,f_m)\in\mathbb R^m:\ |f_i|\le1,\quad |f_i-f_j|\le t\ \text{for all }i\ne j\right\}.
\]
A vertex of \(K_{m,t}\) gives a facet of \(P_{m,t}\); the normalization of each supporting inequality for the latter is \(\langle v,\mu\rangle\le1\). The Euclidean distance of that supporting hyperplane from the origin is \(1/\|v\|_2\). The incenter locus \(\mathcal I_{m,t}\subset H\) is the set of centers \(c\) satisfying \(c+r_{m,t} B_2^H\subseteq P_{m,t}\).

## Proof
**1. Exhaust all polar vertices.** If no \(|f_i|\) equals \(1\), both small uniform translations of all \(f_i\) remain feasible. Thus a vertex must have \(f_j=1\) or \(f_j=-1\) for some \(j\). In the positive case, every coordinate lies in the common interval \([1-t,1]\). If any other coordinate lies strictly between these endpoints, changing that one coordinate a sufficiently small amount in either direction preserves every constraint: all other coordinates remain in \([1-t,1]\), and the altered coordinate is still strictly less than \(t\) away from each of them. Therefore at a vertex every coordinate equals \(1\) or \(1-t\), and at least one equals \(1\). Conversely, fixing any nonempty subset \(S\subseteq\{1,\ldots,m\}\), the potential
\[
f_S(o)=0,\qquad f_S(a_i)=\begin{cases}1,&i\in S,\\1-t,&i\notin S\end{cases}
\]
is a vertex: the one or more saturated constraints \(f_i=1\) for \(i\in S\), together with the saturated differences \(f_i-f_j=t\) for \(i\in S\), \(j\notin S\), uniquely fix every coordinate. The negative potentials \(-f_S\) provide all the negative vertices; the positive and negative families are disjoint. Hence the polar has exactly \(2(2^m-1)\) vertices and the free unit ball has exactly this many facets. No limit, genericity, or rationality assumption on \(t\) was used.

**2. Compute every Euclidean facet shell.** Write \(k=|S|\). The uncentered potential vector has squared norm \(k+(m-k)(1-t)^2\) and coordinate sum \(k+(m-k)(1-t)\). Subtracting the mean over **all \(m+1\) points, including \(o\)** gives precisely
\[
\|v_S\|_2^2=Q_{m,t}(k).
\]
There are exactly \(2\binom mk\) polar vertices of this squared norm. Expanding \(Q\) gives a quadratic in \(k\) with negative leading coefficient \(-t^2/(m+1)\). Completing its square yields
\[
Q_{m,t}(k)=C_{m,t}-\frac{t^2}{m+1}(k-\alpha_{m,t})^2,
\quad \alpha_{m,t}=(m-1)/2+1/t,
\]
where \(C_{m,t}\) is independent of \(k\). Thus \(Q\) is maximized at precisely the integer(s) closest to \(\alpha_{m,t}\) in \([1,m]\), proving the exact maximizer set \(\mathcal K_{m,t}\). Ties can occur only between two consecutive integers; an equality of \(Q(k)\) and \(Q(k+1)\) is equivalent to \(t=2/(2k-m+2)\). This proves the radius and tangent-facet formulas, once global origin optimality is established.

**3. Global, not merely origin-centered, optimality.** The unit ball is centrally symmetric, and its complete facet inequalities come in opposed pairs \(|\langle v_S,\mu\rangle|\le1\). If a Euclidean ball of radius \(r\) centered at \(c\in H\) lies in that unit ball, then for each \(S\) both inequalities require
\[
r\|v_S\|_2+|\langle v_S,c\rangle|\le1.
\]
In particular \(r\le1/\max_S\|v_S\|_2\). The ball centered at \(c=0\) attains equality for all facet inequalities simultaneously; therefore this is the global Euclidean inradius.

**4. Sharp incenter collapse.** The maximizing set consists solely of \(k=m\) precisely when \(\alpha_{m,t}>m-1/2\), equivalently \(t<2/m\), using \(Q(m)-Q(m-1)=t(2-mt)/(m+1)\). At equality \(t=2/m\), the maximizing levels are \(m-1\) and \(m\). At every larger \(t\), the maximizing set includes at least one \(k\) in \(\{1,\ldots,m-1\}\). For every optimal center \(c\), its scalar products with **all** maximally long polar normals must vanish; this follows from the display in Step 3 at the optimal radius.

If \(k=m\) alone is maximizing, all contacts are the two opposite normals of the potential \((0,1,\ldots,1)\). Their span has dimension one in \(H\). All other facet inequalities have strictly positive slack at the origin, so sufficiently small shifts within the \((m-1)\)-dimensional orthogonal complement remain admissible centers. Therefore the full incenter locus has affine dimension \(m-1\).

If a level \(1\le k<m\) is maximizing, take all \(k\)-subsets \(S\). Differences between the centered vectors \(v_S\) and \(v_T\) are \(t(\mathbf1_S-\mathbf1_T)\) on the cluster and zero at \(o\); as \(S,T\) vary, these span the entire \((m-1)\)-dimensional zero-sum cluster subspace. Their average has a nonzero component in the remaining radial direction, since the average uncentered potential equals \(1-t+kt/m>0\) at each cluster point and zero at \(o\). Consequently all contacting normals span \(H\), forcing \(c=0\). This proves uniqueness for all \(t\ge2/m\) and completes the proof.

## Verification
A standalone exact-rational Python program `check_cluster_inball.py` reconstructs polar vertices independently from **all oriented spanning-tree tight-constraint systems** for fifteen configurations with cluster sizes \(m=3,4,5\), totaling 450 recovered distinct vertices across the tests. It checks the explicit vertex classification, all squared Euclidean norms, maximizing multiplicities, nearest-integer law, and exact ranks of contacting normals. Further exact-rational checks cover cluster sizes \(3\le m\le8\) and both sides of the first threshold and later tie walls. Run `python3 check_cluster_inball.py` with Python's standard library. The concluding message is `SINGLE_CLUSTER_ULTRAMETRIC_INBALL_ALL_CHECKS_PASS`. Finite enumeration serves only as a check of the full proof and does not establish the all-parameter theorem by itself.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2018) prove finite-ultrametric \(\ell_1\)-isomorphism bounds, not Euclidean inradii in the canonical zero-sum embedding. Alexander, Fradelizi, García-Lirola and Zvavitch (2019) study general finite-dimensional Lipschitz-free polytopes and their volume-product geometry; that framework supplies the natural duality but does not provide this radius/contact/center classification. Cúth and Doucha (2014) study Banach-space structure of Lipschitz-free spaces over ultrametrics, not their exact Euclidean inspheres.

A separate all-dimensional equiradial-star Hilbert-distortion calculation assumes the normalized hub-to-leaf distance is at most the leaf-to-leaf distance; our hub-to-leaf distance is strictly larger, and we study the canonical Euclidean inball rather than optimal ellipsoid distortion. A prior exact Hilbert Banach--Mazur distortion calculation treats the same **four-point metric** (\(m=3\)) and already lists its fourteen dual vertices; its facet enumeration in that special case is not claimed as new. Banach--Mazur distance, optimized over arbitrary Euclidean inner products, does not determine the present fixed-embedding Euclidean inradius or the center-collapse threshold. Prior sharp projection constants for clustered metrics similarly optimize a different operator norm. The new claim is the all-\(m\), all-\(t\) Euclidean facet-shell and incenter characterization and the resulting binomial staircase, not a rediscovery of general duality or the four-point vertex list.

## Limitations
The metric has one nonsingleton equilateral cluster and a single remote point, all scalars are real, and the Euclidean embedding is the stated canonical one. The endpoints \(t=0\) (metric collapse) and \(t=1\) (equilateral degeneration of the facet structure) are excluded. The theorem does not calculate Banach--Mazur distances or higher-depth ultrametrics. An equivalent older formulation in the literature on Lipschitz variance or symmetric metric polytopes cannot be entirely excluded without independent historical review. No independent mathematical validation has been performed.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814, first public 10 July 2018 (relevant finite-ultrametric discussion).
2. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first public 24 November 2019.
3. M. Cúth and M. Doucha, *Lipschitz-free spaces over ultrametric spaces*, arXiv:1411.2434, first public 10 November 2014.
4. *Exact Hilbert distortion of a four-point ultrametric with an equilateral cluster*, 2026 research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-hilbert-distortion-of-a-four-point-ultrametric-with-an-equ--aeb3c22792bd.
5. *Sharp optimal projection constants for clustered finite metric free spaces*, 2026 research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-optimal-projection-constants-for-clustered-finite-metric-f--bd13acd51aa3.
6. *Exact Euclidean distortion for equiradial star Lipschitz-free spaces*, 2026 research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-euclidean-distortion-for-equiradial-star-lipschitz-free-sp--e536fc6e91f9.
