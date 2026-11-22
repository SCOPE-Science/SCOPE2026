# Exact weighted variation sensitivity and anisotropy rigidity of finite greatest convex minorants

## Finding

Let \(n\ge2\) be an integer and \(x_1<\cdots<x_n\) arbitrary distinct real knots. Given real data \(y=(y_1,\ldots,y_n)\), let \(g_y\) be the **greatest convex minorant** of the polygonal interpolant through \((x_i,y_i)\) on \([x_1,x_n]\), and put \(G_x(y)=(g_y(x_1),\ldots,g_y(x_n))\). For positive edge weights \(w_i\), define
\[
V_w(h)=\sum_{i=1}^{n-1}w_i|h_{i+1}-h_i|.
\]
The exact two-input sensitivity is
\[
\boxed{\mathcal K(x,w)=\sup_{V_w(y-z)>0}\frac{V_w(G_x(y)-G_x(z))}{V_w(y-z)}
=\max_{1\le a<b\le n}\frac{\sum_{i=a}^{b-1}w_i(x_{i+1}-x_i)}{(x_b-x_a)\min_{a\le j<b}w_j}.}
\]
Every term in the finite maximum is attainable by arbitrarily close pairs. In particular \(\mathcal K(x,w)=1\) **if and only if** all edge weights are equal (for \(n=2\) this is automatic). This classification does not require uniform knots. For the knots \((0,1,3,4)\) and weights \((1,7,1)\) the sharp coefficient is \(5\), attained on a minorant having one chord spanning the first two edges.

## Assumptions and scope

The data, knots and weights are real; the knots increase strictly and the weights are strictly positive. The greatest convex minorant is the pointwise largest convex function bounded above by the polygonal interpolant of the data on its closed knot interval. In one dimension its graph is exactly the **lower convex hull** of the finitely many nodal points, joined by straight segments; both endpoints are contacts. The seminorm \(V_w\) sums unnormalized **nodal** jumps of a signal weighted by \(w_i\). It is not the variation of a derivative and is unrelated to the least-squares metric used in isotonic or convex regression. Since \(G_x(y+c\mathbf1)=G_x(y)+c\mathbf1\), pairs with zero input seminorm also have zero output seminorm. The displayed supremum excludes a zero denominator.

## Proof

**1. A linear map for each lower-hull contact partition.** At a generic data vector the lower hull has a uniquely determined set of contact indices \(1=c_0<c_1<\cdots<c_m=n\), and all noncontact data lie *strictly above* the relevant chords. On a sufficiently small open neighborhood with these same contacts, \(G_x\) agrees with a linear chord-interpolation map \(Q_c\): on each interval \([a,b]=[c_j,c_{j+1}]\),
\[
(Q_ch)_i=\frac{x_b-x_i}{x_b-x_a}h_a+\frac{x_i-x_a}{x_b-x_a}h_b,\qquad a\le i\le b.
\]
Its consecutive increments are \((x_{i+1}-x_i)(h_b-h_a)/(x_b-x_a)\). Set the positive face-average edge weight
\[
\overline w_{ab}=\frac{\sum_{i=a}^{b-1}w_i(x_{i+1}-x_i)}{x_b-x_a}.
\]
For each disjoint lower-hull face,
\[
\sum_{i=a}^{b-1}w_i|(Q_ch)_{i+1}-(Q_ch)_i|
=\overline w_{ab}|h_b-h_a|
\le\frac{\overline w_{ab}}{\min_{a\le k<b}w_k}\sum_{k=a}^{b-1}w_k|h_{k+1}-h_k|.
\]
Summing over faces (which partition all input edges) proves \(V_w(Q_ch)\le\mathcal K(x,w)V_w(h)\) for every contact partition.

**2. No tie assumptions are needed.** Each nodal value of the convex minorant is the minimum among finitely many possible affine two-contact chord values whose endpoints bracket that node (including the trivial singleton contact). Therefore \(G_x\) is continuous and piecewise affine as a function of \(y\). Along any segment \(z+t(y-z)\), its restriction consists of finitely many affine pieces. On the interior of each generic piece its derivative is a chord-interpolation map from Step 1; at a degenerate piece where some data lie exactly on the same chord, that derivative agrees with a neighboring generic chord-selection map, by continuity. Integrating the derivative in this finite-dimensional vector space gives
\[
V_w(G_x(y)-G_x(z))\le\int_0^1V_w(Q_{c(t)}(y-z))\,dt\le\mathcal K(x,w)V_w(y-z).
\]
This extends the upper bound globally, including nonunique contact descriptions and ties.

**3. Every face and every cheapest edge are exactly realizable.** Fix \(a<b\) and an edge \(j\in\{a,\ldots,b-1\}\) minimizing \(w_j\) over that interval. Take the strictly convex baseline values \(q_i=x_i^2\) and let \(\ell\) denote the chord joining \((x_a,q_a)\) and \((x_b,q_b)\). Choose a sufficiently large positive \(M\) and put \(Y_i=q_i\) outside the open index interval \((a,b)\) and \(Y_i=\ell(x_i)+M\) inside it. Its lower hull has every index outside \((a,b)\) as a strict contact and one strictly exposed chord \([a,b]\). Convexity of the baseline follows from strict increase of the slopes \(x_i+x_{i+1}\), including the slopes into and out of this new chord; outside nodal values are strictly above its extended line. (The case \(b=a+1\) needs no interior elevation.)

Put \(h_i=0\) when \(i\le j\) and \(h_i=1\) when \(i>j\). Because all relevant hull inequalities are strict, \(Y+\varepsilon h\) has the same contact partition for every sufficiently small \(\varepsilon>0\). Thus
\[
V_w((Y+\varepsilon h)-Y)=\varepsilon w_j,
\qquad
V_w(G_x(Y+\varepsilon h)-G_x(Y))=\varepsilon\overline w_{ab}.
\]
The attained ratio is \(\overline w_{ab}/w_j\), exactly the corresponding term of the maximum. The separation \(\varepsilon\) can be arbitrarily small. Choosing a maximizing face proves equality.

**4. Rigidity of the contraction boundary.** Each \(\overline w_{ab}\) is a convex combination of the strictly positive edge weights on \([a,b]\), so the ratio of Step 3 is at least \(1\) and is exactly \(1\) for every interval when the weights are uniform. Conversely, if some weights differ, choose \([a,b]=[1,n]\): its strictly positive weighted average exceeds the global minimum edge weight. The formula then gives \(\mathcal K(x,w)>1\). This proves both directions, including the automatic two-knot case.

## Verification

The self-contained Python 3 program `verify.py` uses only standard-library exact rational arithmetic. Running `python verify.py` checks 900 randomized strictly increasing rational meshes and positive weight vectors, with an exact sharpness witness for the formula in each case. It also tests 900 independent pairs of random rational signals against the predicted inequality and checks the explicit amplification-five example. These computations validate finite instances of the formula and the witness construction; the all-size result follows from the preceding proof, not the experiments.

## Relationship to prior work

Kearsley's 2006 full-text study of isotonic regression describes the greatest convex minorant construction for cumulative sum diagrams, whereas the present map takes the lower convex envelope **directly of arbitrary nodal signal values**. Its perturbation seminorm is the weighted first variation of those output nodal values; neither this exact sharp formula nor the uniform-weight rigidity follows from the paper's statements about least-squares order fitting. Anevski and Hössjer (2006) study asymptotic stochastic distributions of greatest convex minorants, not deterministic finite-dimensional two-input weighted variation sensitivity. Gorokhovik (2011) characterizes piecewise-affine maps abstractly, but does not derive the exact weighted hull-face norm. The later Yang–Barber result (2017) gives a contraction criterion for **isotonic Euclidean projection** in arbitrary seminorms; its map is an average over pooled coordinate blocks, not the direct lower-convex-envelope chord map, and it does not imply the sharp formula here without additional reduction that is not in that work. Nearby published records treat variation under sliding min/max morphology and variation of isotonic least-squares regression on cycle-shaped orders, with different operators and implications. A search for equivalent graph, chord-selection, convexification and weighted-BV formulations yielded no covering result; unindexed historical treatments remain a priority risk.

## Limitations

The theorem covers finite scalar data on one real interval with strict knots, positive edge weights and nodal first-order total variation. It does not address higher-dimensional convex envelopes, continuous perturbations between nodes, higher differences, or stability in the derivative variation seminorm. The mathematical proof is an analytical finite-dimensional argument, not a claim of historical priority certification; older inaccessible or unindexed works could contain an equivalent operator-norm statement. Related stochastic-convex-minorant articles were not all available in full text.

## References

- A. J. Kearsley, *Projections Onto Order Simplexes and Isotonic Regression*, Journal of Research of the National Institute of Standards and Technology 111 (2006), 121–125, DOI 10.6028/jres.111.011; full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC4662501/ .
- D. Anevski and O. Hössjer, *A general asymptotic scheme for inference under order restrictions*, arXiv:math/0611270v1, submitted November 9, 2006, https://arxiv.org/abs/math/0611270 .
- V. V. Gorokhovik, *Geometrical and analytical characteristic properties of piecewise affine mappings*, arXiv:1111.1389v1, submitted November 6, 2011, https://arxiv.org/html/1111.1389 .
- F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852v1, 2017; compared as later contextual literature, https://arxiv.org/html/1706.01852v3 .
