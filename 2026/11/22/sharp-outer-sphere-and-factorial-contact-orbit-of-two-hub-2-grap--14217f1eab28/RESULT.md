# Sharp outer sphere and factorial contact orbit of two-hub 2-graph polytopes

## Finding

For each integer \(q\ge2\), let \(K_{2,q}\) have two distinguished hub vertices and \(q\) leaf vertices. In the canonical standard-coordinate realization of Pešović and Stojadinović, define the **2-graph polytope**
\[
P_q=Q_{K_{2,q},2}=\sum_{\substack{\varnothing\ne S\subseteq V(K_{2,q})\\|S|\le3,\ K_{2,q}[S]\text{ connected}}}\operatorname{conv}\{e_i:i\in S\}\subset\mathbb R^{q+2}.
\]
Here every eligible subset appears once, with coefficient one; in particular all singletons are included. All points of \(P_q\) have coordinate sum \(T_q=(q+1)(q+2)\). Its unique minimum enclosing Euclidean ball has center
\[
c_q=(x_q,x_q,\underbrace{y_q,\ldots,y_q}_{q\text{ leaves}}),\qquad
x_q=\frac{(q^2+3q+8)(3q^2+7q+6)}{12(q+2)^2},\qquad
y_q=\frac{3q^3+26q^2+57q+46}{6(q+2)^2},
\]
and squared radius
\[
R_q^2=\frac{q(q+1)(9q^5+111q^4+523q^3+1145q^2+1256q+484)}{72(q+2)^3}.
\]
The complete contact set consists of two, and only two, vertex families:

- **Leaf-order family:** hub coordinates \((1,1)\), and leaf coordinates any permutation of \((4,6,\ldots,2q+2)\). There are \(q!\) distinct points.
- **Hub-order family:** all leaf coordinates equal to \(1\), and hub coordinates the two permutations of \(\bigl(1+q(q+1)/2,\ 1+q(q+3)/2\bigr)\). There are exactly two distinct points.

Thus exactly \(q!+2\) vertices touch the outer sphere. The full vertex count is
\[
 f_0(P_q)=q!\left(2\sum_{s=0}^q\frac{q-s+1}{s!}-1\right),
\]
so the contacting fraction is asymptotic to \(1/(2e q)\). The result is about the specified Euclidean realization, not an arbitrary affine model or a different member of the graph-polytope interpolation.

## Assumptions and scope

The parameter is any integer \(q\ge2\). Give the two hubs indices \(0,1\), and give leaves indices \(2,\ldots,q+1\). Distances are ordinary ambient \(\ell_2\) distances; equivalently, intrinsic distances in the affine hyperplane of coordinate sum \(T_q\). All distinct vertices are counted once. The minimum enclosing ball is the least-radius closed Euclidean ball containing the entire convex polytope, not an inscribed ball or a minimum-volume ellipsoid.

## Proof

**1. Exhaustive parametrization of vertices.** Every supporting functional with a strict ordering of the \(q+2\) coordinate weights uniquely maximizes each simplex summand at its largest-weight coordinate. Every polytope vertex is exposed by a functional that can be perturbed to such an ordering. Place the first hub before the second, and let \(s\) leaves precede the first hub and \(k\) leaves precede the second, where \(0\le s\le k\le q\). List leaves in their relative order \(j=0,\ldots,q-1\). Directly counting eligible connected subsets of sizes one, two and three gives
\[
 a_s=1+\frac{s(s+1)}2,\qquad b_k=1+\frac{k(k+3)}2,
\]
and leaf-coordinate sequence
\[
 L_j(s,k)=\begin{cases}1&0\le j<s,\\2+j&s\le j<k,\\4+2j&k\le j<q.\end{cases}
\]
The opposite hub ordering swaps the first two coordinates. The corresponding points are all vertices because each is a unique maximizer of its strict-weight functional, and this construction exhausts all vertices. The coordinates sum to \(T_q\), as required by the number of simplex summands.

**2. Radius and exhaustive outer inequality.** A candidate center fixed by the hub and leaf permutation groups lies in the sum hyperplane, so write it as \((x,x,y,\ldots,y)\) with \(2x+qy=T_q\). Choose \(x=x_q\), \(y=y_q\) as in the finding. At both endpoint patterns \((s,k)=(0,0)\) and \((q,q)\), direct substitution gives the same squared distance \(R_q^2\). Moreover,
\[
2(x_q-y_q)=\frac{(q-2)(3q^2+10q+11)}{6(q+2)}.
\]
To certify all other vertices, write \(H=a_s+b_k\), \(V=a_s^2+b_k^2+\sum_jL_j(s,k)^2\). The finite-sum identity
\[
12V=3k^4+6k^3-15k^2-42k+3s^4+2s^3-3s^2-2s+16q^3+72q^2+104q+24
\]
shows, after cancellation of the common quadratic center term, that
\[
12(q+2)\bigl(R_q^2-\|v(s,k)-c_q\|_2^2\bigr)=N(q,s,k),
\]
where
\[
\begin{aligned}
N(q,s,k)={}&(q+2)(-3k^4-6k^3+15k^2+42k-3s^4-2s^3+3s^2+2s)\\
&+(q-2)(3q^2+10q+11)(k^2+3k+s^2+s).
\end{aligned}
\]
This is a globally nonnegative polynomial on all required integer parameters. For an explicit **all-dimensions algebraic certificate**, substitute \(u=s\), \(v=k-s\), \(w=q-k\). All are nonnegative. Direct polynomial expansion gives
\[
N=P_0(u,w)+vP_1(u,w)+v^2P_2(u,w)+v^3P_3(u,w)+v^4P_4(u,w),
\]
where
\[
\begin{aligned}
P_0={}&2uw(6u^3+9u^2w+22u^2+3uw^2+22uw+16u+6w^2+8w+4),\\
P_1={}&6u^4+42u^3w+19u^3+36u^2w^2+113u^2w+20u^2+6uw^3+71uw^2+68uw+39u+9w^3+12w^2+15w+18,\\
P_2={}&9u^3+45u^2w+19u^2+27uw^2+96uw+22u+3w^3+31w^2+30w+23,\\
P_3={}&3u^2+24uw+7u+9w^2+29w+6,\\
P_4={}&6w+1.
\end{aligned}
\]
Every displayed coefficient is positive. The full expansion has 41 nonzero monomials, and the identity is verified independently by the exact integer polynomial checker in `verify_graph2.py`. Equality holds exactly if \(v=0\) and \(uw=0\), which means \((s,k)=(0,0)\) or \((q,q)\). Strict convexity of squared distance implies no nonvertex point of the polytope can touch this sphere: a nontrivial convex combination of distinct vertices lies strictly inside. The two specified vertex families therefore comprise the complete contact set.

**3. Optimality and uniqueness.** Average all \(q!\) points in the leaf-order family to obtain \(A=(1,1,q+3,\ldots,q+3)\), and average the two hub-order points to obtain \(B=(1+q(q+2)/2,1+q(q+2)/2,1,\ldots,1)\). Set
\[
\lambda_q=\frac{(q+1)(3q^2+13q+26)}{6(q+2)^3}.
\]
Then \(0<\lambda_q<1\), since the denominator minus numerator is \(3q^3+20q^2+33q+22>0\), and \(c_q=(1-\lambda_q)A+\lambda_q B\). Thus \(c_q\) is a convex combination of contact points. For any alternative center \(z\), averaging squared distances to those points with these strictly positive orbit weights yields exactly \(R_q^2+\|z-c_q\|_2^2\). Any enclosing radius is at least this average squared distance, hence is at least \(R_q\), and equality forces \(z=c_q\). This proves both global minimality and uniqueness.

**4. Vertex and contact counts.** At \((0,0)\), both hub coordinates are \(1\), while all \(q\) leaf values are distinct, giving \(q!\) vertices. For any other \((s,k)\), the unequal hub values identify the pair \((s,k)\) up to hub exchange, and exactly \(s\) leaf coordinates equal \(1\), while all others are distinct. Thus there are \(2q!/s!\) distinct vertices for each of the other pairs. Summing over \(s\le k\le q\) gives the displayed \(f_0(P_q)\). Only the two endpoint patterns touch, giving \(q!+2\). The asymptotic contact fraction follows from \(\sum_{s=0}^q(q-s+1)/s!=eq+O(1)\).

## Verification

The standalone `verify_graph2.py` uses only the Python standard library and exact integer and rational arithmetic. It (i) expands both sides of the polynomial nonnegativity certificate as formal polynomials in three variables, verifies equality, all 41 positive coefficients, and the necessary vanishing structure, and (ii) independently reconstructs vertices from all strict total orders of the original simplex-sum definition for \(2\le q\le6\), then checks the exact radius, vertex count and complete contact set. Recorded result: `POSITIVE_POLYNOMIAL_CERTIFICATE_PASS monomials=41`; exhaustive vertex counts \(20,92,498,3142,22766\), with respective contact counts \(4,8,26,122,722\); final `TWO_HUB_2_GRAPH_SPHERE_PASS`. The formal polynomial certificate, not the finite enumeration, supplies the all-dimensional inequality.

## Relationship to prior work

Pešović and Stojadinović introduced the \(m\)-graph polytopes, with \(Q_{\Gamma,1}\) a graphical zonotope and larger \(m\) interpolating to a graph-associahedron. Their full preprint defines the particular unit simplex-sum realization used here and studies weighted quasisymmetric enumerators, normal-fan stabilization and related posets. The present statement additionally determines an extrinsic Euclidean Chebyshev center, a sharp equality certificate and every contacting vertex in the distinct \(K_{2,q}\), \(m=2\) case. Related published results on graphical-zonotope spheres apply to \(m=1\) and those on star graph-polytopes concern different graphs or inscribed balls, so their displayed claims do not imply this result. Historical priority against unindexed work is not established by an unsuccessful search alone.

## Limitations

The theorem is proved only for \(m=2\), the graph \(K_{2,q}\) and the stated unit-coordinate realization, with \(q\ge2\). It does not assert the same formula for weighted tubes, \(m\ge3\), other complete bipartite graphs, or affine-invariant extremal ellipsoids. Computational enumeration stops at \(q=6\), while the formal proof covers all integers \(q\ge2\). The checked literature is not an exhaustive priority guarantee; related indexed results whose full text could not be fetched are described in the review.

## References

1. M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053v1 (first public 2022-09-24), especially Definition 2.1 and Sections 3–4, https://arxiv.org/html/2209.12053v1 .
2. M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, Turkish Journal of Mathematics 47 (2023), 1362–1373, https://doi.org/10.55730/1300-0098.3434 .
