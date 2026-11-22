# Universal five-chamber two-field Potts ground energy on bipartite cubic triangle expansions

## Finding
Let \(G\) be any finite simple cubic bipartite graph, with \(m=|V(G)|\), and construct its triangle expansion \(T(G)\): each incidence \((v,e)\), with \(v\in e\), becomes a vertex; the three incidences at each \(v\) form a triangle, and the two incidences of every original edge are joined. Place one of three labeled colors \(0,1,2\) at each new vertex. The antiferromagnetic Hamiltonian, for \(J>0\) and \(h_0>h_1>h_2\), is
\[
\mathcal H(\sigma)=J\sum_{uv\in E(T(G))}\mathbf 1_{\sigma_u=\sigma_v}-\sum_{i=0}^2h_i n_i(\sigma).
\]
Write \(x=(h_0-h_1)/J>0\), \(y=(h_1-h_2)/J>0\). For all finite graphs \(G\) in this class and every \(x,y>0\), the exact zero-temperature ground energy is
\[
\boxed{\frac{E_0+3m h_2}{J}=-3my+m\min\left\{-x+y,\,\frac{1-3x+y}{2},\,1-\frac{3x}{2},\,\frac32-2x,\,\frac92-3x\right\}.}
\]
The five affine branches have nonempty open regions in the strictly ordered field quadrant. In their order above, their unique color populations \((n_0,n_1,n_2)\) and numbers \(e\) of monochromatic bonds are

| Region | Population \((n_0,n_1,n_2)\) | Monochromatic bonds |
|---|---|---|
| \(x+y<1\) | \((m,m,m)\) | \(0\) |
| \(1<x+y<2,\;y<1\) | \((3m/2,m,m/2)\) | \(m/2\) |
| \(x<1,\;y>1\) | \((3m/2,3m/2,0)\) | \(m\) |
| \(1<x<3,\;x+y>2\) | \((2m,m,0)\) | \(3m/2\) |
| \(x>3\) | \((3m,0,0)\) | \(9m/2\) |

At boundary points the displayed minimum formula remains exact; multiple configurations and, potentially, multiple populations can coexist. The open-region classification does not assert a finite-temperature or infinite-volume phase transition.

## Assumptions and scope
The base graph is finite, simple, undirected, cubic, and bipartite, possibly disconnected. Cubicity implies \(m\) is even, with exactly \(3m/2\) base edges. Each expanded vertex has degree three, and there are exactly \(3m\) new vertices, \(3m\) triangle edges and \(3m/2\) external matching edges. Colors are distinguished labels, not classes modulo permutation. The two field differences are strictly positive, but there is no bound on their size. The model has one uniform positive antiferromagnetic equality penalty \(J\) on every edge, and no further interactions. Set \(a=n_0\), \(b=n_1\), \(c=n_2\), so \(a+b+c=3m\). Denote the number of monochromatic expanded-graph edges by \(e\). Then
\[
\frac{\mathcal H+3mh_2}{J}=e-(x+y)a-yb=-3my+e-xa+yc.
\]
This identity specifies the correct field-independent energy normalization throughout the proof.

## Proof
**1. Six universal support inequalities.** Split \(e=e_{\triangle}+e_{\mathrm{ext}}\), for the original-vertex triangles and the external perfect matching. Let \(a_v,c_v\) count colors zero and two in the triangle indexed by \(v\). Every triangle contains at least \(a_v-1\) monochromatic edges, and has at least one monochromatic edge unless it contains a color-two spin. Thus
\[
e_{\triangle}\ge a-m,\qquad e_{\triangle}+c\ge m.
\]
There are \(3m/2\) external edges, each containing at most two zero spins; pigeonholing gives \(e_{\mathrm{ext}}\ge\max(0,a-3m/2)\). It follows that
\[
e-a\ge-m,\quad e-2a\ge-5m/2,\quad e+c\ge m,\quad e-a+c\ge-m/2.
\]
For the second inequality, add \(a-m\) and \(\max(0,a-3m/2)\) and compare separately on either side of \(a=3m/2\); the fourth is obtained analogously from \(m-c\). Trivially \(e\ge0\). Finally \(T(G)\) has degree three and \(9m/2\) edges. Turn each of the \(3m-a\) nonzero spins into zero; each change can increase the number of equal-color edges by at most three. Comparing with the resulting all-zero coloring proves
\[
e-3a\ge-9m/2.
\]
These six statements hold for **every** coloring of **every** graph in the stated class, not only for special configurations.

**2. Lower envelope in all field chambers.** Define \(Q=e-xa+yc\), so \((\mathcal H+3mh_2)/J=-3my+Q\). Write the six inequalities from Step 1 as \(e\ge0\), \(e-a\ge-m\), \(e-2a\ge-5m/2\), \(e-3a\ge-9m/2\), \(e+c\ge m\), \(e-a+c\ge-m/2\). Their nonnegative linear combinations give the five candidate lower bounds:

- When \(x+y\le1\), use \(Q=(1-x-y)e+x(e-a)+y(e+c)\ge m(-x+y)\).
- When \(1\le x+y\le2\) and \(y\le1\), the region is the convex quadrilateral with corners \((0,1),(1,0),(1,1),(2,0)\). At those corners, respectively, the bounds \(e+c\ge m\), \(e-a\ge-m\), \(e-a+c\ge-m/2\), \(e-2a\ge-5m/2\) give \(Q\ge m(1-3x+y)/2\). For each coloring, its difference from this affine lower bound is affine in \((x,y)\), hence nonnegative throughout the quadrilateral.
- When \(x\le1\) and \(y\ge1\), use \(Q\ge(1-x)(e+c)+x(e-a+c)\ge m(1-3x/2)\), since the omitted term \((y-1)c\) is nonnegative.
- When \(1\le x\le2\) and \(x+y\ge2\), use \(Q\ge(2-x)(e-a+c)+(x-1)(e-2a)\ge m(3/2-2x)\). When \(2\le x\le3\), instead use \(Q\ge(3-x)(e-2a)+(x-2)(e-3a)\ge m(3/2-2x)\), discarding \(yc\ge0\).
- When \(x\ge3\), use \(Q\ge(e-3a)-(x-3)a\ge-9m/2-3m(x-3)=m(9/2-3x)\), since \(a\le3m\).

The interiors of these five regions partition the positive quadrant except the stated phase boundaries. Thus every coloring is bounded below by the appropriate affine candidate in every region; on boundaries the same conclusion follows by continuity. This is a **global** lower bound, with no use of finite enumeration.

**3. Universal simultaneous attainability.** A finite cubic bipartite graph has a proper three-edge-coloring, obtainable by decomposing its edges into three perfect matchings. Fix such a coloring with edge labels \(k=0,1,2\) and choose a bipartition \(L\sqcup R\) (both parts contain \(m/2\) vertices). At an incidence \((v,e)\), put the entry numbered \(k(e)\) from the triple prescribed for the side of \(v\):

| Branch | Triple on \(L\) | Triple on \(R\) |
|---|---|---|
| First | \((0,1,2)\) | \((1,2,0)\) |
| Second | \((0,0,1)\) | \((1,2,0)\) |
| Third | \((0,0,1)\) | \((1,1,0)\) |
| Fourth | \((0,0,1)\) | \((1,0,0)\) |
| Fifth | \((0,0,0)\) | \((0,0,0)\) |

Directly count the local equal pairs on each triangle and the equal pairs across every base edge. The results are exactly \((e,a,b,c)=(0,m,m,m)\), \((m/2,3m/2,m,m/2)\), \((m,3m/2,3m/2,0)\), \((3m/2,2m,m,0)\), and \((9m/2,3m,0,0)\). In particular each of the five lower bounds of Step 2 is *attained* for every admissible base graph. Combining the lower and upper bounds proves the energy formula globally.

**4. Exhaustiveness and uniqueness of open population sectors.** All five regions are nonempty, for example take \((x,y)=(1/4,1/4),(5/4,1/4),(1/4,7/4),(7/4,5/4),(4,1/4)\). In each region its branch is strictly below the other four. If any other coloring attains the energy at an interior point, the difference between its own affine energy and the active branch is a nonnegative affine function throughout a neighborhood that vanishes at an interior point. Such a function is identically zero. Its \(x\)- and \(y\)-coefficients therefore agree, forcing \(a\) and \(c\), and hence \(b\), and its constant coefficient forces \(e\). Thus every ground configuration in an open chamber has exactly the stated population and bond count. No additional open chamber is possible.

## Verification
Run `python3 verify_universal.py` with Python 3.10 or newer from this extracted package. The verifier independently constructs the triangle expansions of \(K_{3,3}\) and the three-dimensional cube, counts all their edges, checks all five explicit witness configurations using exact integers, and confirms that each is the unique active branch at a rational point of its predicted region. It also performs 1,500 pseudorandom spin checks on each graph of all six support inequalities and of the rational energy lower envelope. It prints `TWO_FIELD_POTTS_UNIVERSAL_CHECKS_PASSED 3010` after success. The complete all-graph result comes from the analytic inequalities and bipartite edge-coloring argument above; the random tests are not a substitute for the proof.

## Relationship to prior work
The field-dependent Potts partition-function formalism of Shrock and Xu [1] treats a generalized field favoring a subset of colors with **one shared** field value, and derives graph-dependent partition identities and bounds; it does not evaluate the present three distinct chemical potentials on the triangle expansions of all cubic bipartite graphs. The multivariate-field V-polynomial framework of Dasu and Marcolli [2] can encode the present Hamiltonian, but a general graph-polynomial representation does not yield this evaluated universal five-chamber ground-state law or its sharp realizations. Earlier exact **one-field** Potts classifications on the truncated tetrahedron and cubic line graphs use respectively a single graph and a different graph transformation. In particular the line graph of a cubic base is not its triangle expansion: the latter is the line graph of the once-subdivided base and has intertriangle edges. One-field results cannot establish the two independently tunable chemical-potential inequalities and the five regions here. This comparison is about scientific implications, not mere title differences.

## Limitations
Cubicity and bipartiteness are essential to the stated constructive proof. For a cubic graph without a proper three-edge-coloring, the sharp zero-frustration branches can fail. The result concerns exactly three labeled Potts colors, equally weighted positive antiferromagnetic bonds, two strictly ordered fields, and finite zero-temperature systems. It does not count open-chamber degeneracies beyond exhibiting a ground configuration in each, resolve coexistence multiplicities on the boundaries, establish positive-temperature phase transitions, or cover a non-bipartite base. The literature comparison cannot exclude all unindexed equivalent calculations.

## References
1. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182v1, first public 2010-09-07, https://arxiv.org/abs/1009.1182.
2. S. Dasu and M. Marcolli, *Potts models with magnetic field: arithmetic, geometry, and computation*, arXiv:1412.7925v1, first public 2014-12-26, https://arxiv.org/abs/1412.7925.
