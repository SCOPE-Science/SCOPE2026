# A sharp three-phase nonlinear Poincaré law for spoke-weighted Petersen graphs

## Finding
Let \(G\) be the Petersen graph in its canonical outer-pentagon/inner-pentagram presentation. Give each of the ten rim edges conductance \(1\), and give each of the five spokes conductance \(t>0\). For all maps \(f\) from its ten vertices to **any** metric space \((M,d)\), define the best constant \(\Gamma(t)\) by
\[
\frac1{100}\sum_{u,v\in V(G)}d(f(u),f(v))\le
\frac{\Gamma(t)}{5(2+t)}\sum_{\{u,v\}\in E(G)}c_{uv}(t)d(f(u),f(v)).
\]
Then the exact, attained universal metric constant is
\[
\boxed{\Gamma(t)=
\begin{cases}
\dfrac{2+t}{2t},&0<t\le1,\\[3pt]
\dfrac{5(2+t)}{2(4+t)},&1\le t\le\dfrac94,\\[3pt]
\dfrac{2(2+t)}5,&t\ge\dfrac94.
\end{cases}}
\]
The two transitions are exactly \(t=1\) and \(t=9/4\). The first regime has a two-value extremizer that collapses each pentagonal rim. The middle regime is attained by the intrinsic shortest-path metric with both rim-edge lengths \(2\) and spoke lengths \(1\). The third regime is attained by collapsing corresponding inner and outer vertices to the same point of a unit five-cycle. For \(1<t<9/4\), every extremizing metric has dihedrally averaged rim lengths equal to twice its averaged spoke length. At \(t=1\), \(\Gamma(1)=3/2\).

## Assumptions and scope
Indices are taken modulo \(5\). The vertices are \(o_i,v_i\), \(0\le i<5\); edges are \(o_io_{i+1}\), \(v_iv_{i+2}\), and \(o_iv_i\). Only the last type has conductance \(t\). Metric-valued maps need not be injective, so distinct graph vertices may have identical images. All distances enter to the first power, not squared. The edge sum is unordered and the all-pairs sum is ordered, with diagonal zero. The total conductance is \(5(2+t)\). No assumption of linearity, completeness, or Banach structure is made about the target.

Write
\[
S(f)=\sum_{\{u,v\}\subset V(G)}d(f(u),f(v)),\qquad
D_t(f)=\sum_{\{u,v\}\in E(G)}c_{uv}(t)d(f(u),f(v)).
\]
For every nonconstant map, \(D_t(f)>0\) since \(G\) is connected. Consequently \(\Gamma(t)=(2+t)\sup_f S(f)/(10D_t(f))\).

## Proof
**Symmetry reduction.** The dihedral group of order ten acts by simultaneously rotating and reflecting the two five-vertex layers; it preserves each edge type. Averaging a metric-valued map's pullback pseudometric over this group preserves \(S\) and \(D_t\), preserves all triangle inequalities, and gives three constant edge lengths: \(x\ge0\) for outer edges, \(y\ge0\) for inner edges and \(z\ge0\) for spokes. Thus \(D_t=5(x+y+tz)\). The averaged pseudometric need not itself be represented inside the original target, but it suffices for an upper bound.

**Two all-pairs path certificates.** There are seven unordered pair orbits. The table gives each orbit's multiplicity and two explicit upper bounds derived from graph paths, measured using edge lengths \(x,y,z\). Here \(i=0\) suffices by dihedral symmetry.

| Pair representative | Multiplicity | Route A bound | Route B bound |
|---|---:|---|---|
| \(o_0,o_1\) | 5 | \(x\) | \(x\) |
| \(v_0,o_0\) | 5 | \(z\) | \(z\) |
| \(v_0,o_2\) | 10 | \(y+z\) | \(y+z\) |
| \(o_0,o_2\) | 5 | \(2x\) | \(y+2z\) |
| \(v_0,o_1\) | 10 | \(x+z\) | \(x+z\) |
| \(v_0,v_2\) | 5 | \(y\) | \(y\) |
| \(v_0,v_1\) | 5 | \(2y\) | \(x+2z\) |

For example, the competing paths from \(o_0\) to \(o_2\) are the outer two-step path and the path through \(v_0,v_2\); the competing paths from \(v_0\) to \(v_1\) are the inner two-step path and the path through \(o_0,o_1\). Summing the complete table yields both global inequalities
\[
S\le25(x+y+z),\qquad S\le20(x+y)+45z. \tag{1}
\]
They are statements for **all** pseudometrics on the ten graph vertices, not just shortest-path metrics.

**Sharp upper envelope.** Put \(a=x+y\) and \(Q=a+tz>0\). If \(0<t\le1\), (1) gives \(S\le25(a+z)\le(25/t)Q\). If \(t\ge9/4\), it gives \(S\le20a+45z\le20Q\). For \(1\le t\le9/4\) set
\[
\theta=\frac{9-4t}{4+t}\in[0,1].
\]
Take \(\theta\) times the first inequality in (1) plus \(1-\theta\) times the second. Coefficient comparison gives
\[
S\le\frac{125}{4+t}(a+tz)=\frac{125}{4+t}Q.
\]
Dividing by \(D_t=5Q\) proves the claimed three-piece upper bound for \(S/D_t\). The definition of \(\Gamma\) gives the displayed formula.

**Attainment.** In the first regime map all outer vertices to one point and all inner vertices to a second point at distance \(1\). Then \(S=25\), \(D_t=5t\), attaining \(S/D_t=5/t\).

In the middle regime take the ten-point shortest-path pseudometric with edge *lengths* \(2\) on both rims and \(1\) on every spoke. Each of these fifteen edge lengths is geodesically realized. Directly from the seven orbits, \(S=125\), while \(D_t=5(4+t)\), attaining \(S/D_t=25/(4+t)\).

In the last regime map \(o_i\) and \(v_i\) to the same vertex \(i\) in a five-cycle endowed with its shortest-path metric. Then every outer edge has distance \(1\), every inner edge has distance \(2\), and each spoke has distance zero. The ten distinct index pairs of the five-cycle have total distance \(15\), each represented four times among the original vertices; therefore \(S=60\), \(D_t=15\) and \(S/D_t=4\).

**Interior equality restriction.** For \(1<t<9/4\) the convex combination above has two strictly positive coefficients. Equality forces both route inequalities in (1) to be equalities. In the table this requires simultaneously \(2x\le y+2z\) and \(y+2z\le2x\), as well as \(2y\le x+2z\) and \(x+2z\le2y\). Hence \(2x=y+2z\), \(2y=x+2z\), and \(x=y=2z\). Nonconstancy gives \(z>0\). This concerns the averaged orbit lengths; it does not assert uniqueness of the original target-space map.

## Verification
The stand-alone standard-library script `verify_petersen.py` verifies with exact rational arithmetic: the seven pair-orbit multiplicities, the existence of graph walks for both advertised route types, the total edge-type loads \((25,25,25)\) and \((20,20,45)\), metric triangle inequalities for the three explicit extremal families, and exact sharpness at nine parameter values including both transitions. These finite checks supplement the symbolic path-routing proof and do not independently prove the all-parameter statement.

Run from the same directory: `python3 verify_petersen.py`.

## Relationship to prior work
Polavarapu (arXiv:2611.05649, first submitted 3 November 2026) provides cotype-dependent upper bounds for nonlinear spectral gaps of regular graphs into specified Banach spaces. Its theorem is neither an exact, arbitrary-metric gap formula nor a conductance-dependent Petersen computation. Altschuler, Dodos, Tikhomirov and Tyros (arXiv:2509.25489, first submitted 29 September 2025) study metric Poincaré extrapolation and sharp asymptotics for random regular graphs; their stated results do not calculate this three-regime ten-vertex invariant. Published research on spectral-gap design for generalized Petersen networks concerns the scalar quadratic Laplacian rather than the metric first-power inequality; an \(L^1\)-distortion computation for the Petersen shortest-path metric likewise does not determine this weighted first-power gap. No claim of a globally exhaustive literature search is made.

## Limitations
This is a complete exact result for the stated Petersen graph, with identical conductances on both rim types and a single independently variable spoke conductance. It makes no assertion for arbitrary edge conductances, other generalized Petersen graphs, power \(p>1\), or Hilbert-space squared-distance spectral gaps. The equality restriction established here concerns averaged edge lengths, not a full classification of individual metric extremizers. Publication priority remains subject to independent literature audit; relevant indexed research summaries and some external full texts were not independently inspected.

## References
1. A. R. Polavarapu, *Linear Cotype Bounds for Nonlinear Spectral Gaps of Scalar Expanders*, arXiv:2611.05649 (submitted 2026-11-03), https://arxiv.org/abs/2611.05649.
2. D. J. Altschuler, P. Dodos, K. Tikhomirov and K. Tyros, *Metric Poincaré inequalities for graphs*, arXiv:2509.25489 (submitted 2025-09-29), https://arxiv.org/abs/2509.25489.
3. M. Krnc and R. J. Wilson, *Recognizing generalized Petersen graphs in linear time*, arXiv:1701.05806 (submitted 2017-01-20); *Discrete Applied Mathematics* 283 (2020), 756–761, https://doi.org/10.1016/j.dam.2020.03.007 (graph nomenclature).
