# The sharp first-force threshold in projective-plane incidence graphs

## Finding

Let \(H\) be the point–line incidence graph of a finite projective plane of order \(q\ge 2\), and set \(v=q^2+q+1\). In standard power domination with sensor set \(S\), the initial observation is \(O=N_H[S]\). An **initial force** is available from \(x\in O\) when exactly one neighbor of \(x\) is outside \(O\).

The smallest number of sensors that permits an initial force is exactly \(q\), for every such plane. The placements of that size allowing a force admit the following exact description, including a count by forcing vertex. For a point \(x\) to force initially, omit one of the \(q+1\) lines through \(x\). On each of the other \(q\) lines choose exactly one sensor, either the line vertex itself or one of its \(q\) points other than \(x\). At least one choice must be a line vertex. For a line \(x\), use the point–line dual rule. These rules generate exactly the pairs \((S,x)\) with \(|S|=q\) in which \(x\) can force initially; the omitted vertex is the forced neighbor.

Consequently the total number of such pairs is
\[
  2v(q+1)\bigl((q+1)^q-q^q\bigr).
\]
This counts a placement once for each vertex eligible to make an initial force from it, not once per placement. More finely, for a fixed point \(x\) the number with exactly \(s\) line sensors is \((q+1)\binom{q}{s}q^{q-s}\) for \(1\le s\le q\); the dual count interchanges points and lines.

It follows that the power-domination number satisfies \(\gamma_P(H)\ge q\). In particular, a placement of at most two sensors can power dominate a plane incidence graph of order \(q\ge2\) only at \(q=2\); it can do so there by the known Fano-plane antiflag construction. No formula for \(\gamma_P(H)\) at higher orders is asserted.

## Proof

The graph is bipartite with \(v\) vertices on each side and degree \(q+1\). Any two distinct points determine one line and any two distinct lines meet in one point. No coordinate model is needed.

Sensors themselves have no unobserved neighbor. Consider an observed point \(x\notin S\). Each selected line contributes at most one observed line through \(x\), namely itself if it contains \(x\): the other vertices newly observed by a line sensor are points. Each selected point \(y\) contributes exactly one observed line through \(x\), the line joining \(x\) to \(y\); \(x\notin S\) ensures \(y\ne x\). Every observed neighbor of \(x\) is furnished by one of these contributions. Thus at most \(|S|\) of the \(q+1\) incident lines are observed. The same argument by duality applies to an observed line outside \(S\). No first force is possible with \(|S|\le q-1\). The initial observation at that size contains at most \((q-1)(q+2)<2v\) vertices, so it is not already complete either.

If \(|S|=q\) and \(x\) is a forcing point, exactly \(q\) lines through \(x\) must be observed. The preceding bound is an equality: every sensor contributes and all its contributed lines are different. The omitted line is unique. Hence all selected lines contain \(x\), and each selected point is on a different contributing line that is not itself selected. At least one of those lines must be selected because that is the only way to observe the unselected point \(x\) initially. Conversely, the stated selection rule observes \(x\) and covers exactly the \(q\) chosen lines through it. The omitted line remains unobserved, since it was not selected and none of the selected points lies on it. Thus \(x\) forces it. Choosing all \(q\) contributing line vertices gives such a placement, proving sharpness. Interchange the two vertex types for a forcing line.

For a fixed point \(x\), there are \(q+1\) ways to omit one line. After this choice each remaining line independently offers \(q+1\) options: itself or one of its \(q\) other points. The points offered on distinct contributing lines are disjoint. Subtract the \(q^q\) selections without a line sensor; equivalently, for a fixed line-sensor count \(s\), choose those \(s\) lines and then one of \(q\) points on each remaining line. Each pair \((S,x)\) has unique choices in this description. The graph has \(v\) point vertices and \(v\) line vertices, and the dual count equals the first, establishing the formula.

For the order-two endpoint, a nonincident point \(P\) and line \(\ell\) form a power-dominating pair. Each of the three lines through \(P\) initially sees \(P\) and its intersection with \(\ell\), so it forces its third point. All seven points are then observed. The points on \(\ell\) each observe \(\ell\) and their line to \(P\), and force their third line, completing observation. This endpoint is included for the cutoff and is not claimed as a new Heawood classification.

## Relationship to prior work and scope

The distinction here is between *being able to start propagation* and *being able to finish it*. Failure to start excludes small placements uniformly, including in non-Desarguesian planes. The equality description identifies the placements that must be examined first when searching for power domination at the lower bound, and counts the possible initial forcing sources. This count says nothing about later forces; different sources can force the same target.

The ordinary power-domination rule is standard; see T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi and M. A. Henning, *Domination in Graphs Applied to Electric Power Networks*, DOI [10.1137/S0895480100375831](https://doi.org/10.1137/S0895480100375831). The work *Exact power-domination obstruction complex of the Heawood graph* gives a stronger classification of **complete** observation on the order-two plane, including all 28 optimal antiflags and their jump graph. *Optimal power-domination mobility in the quaternary projective plane* determines the optimum for order four rather than the initial-force configurations of size four. The general results on the propagation radius in [arXiv:2510.02211v2](https://arxiv.org/abs/2510.02211v2) concern time to full observation from power-dominating sets, not the equality case for eligibility of a first force. The all-order theorem above uses only projective incidence and does not claim historical priority over unindexed results.

## Verification

The proof gives a direct finite counting bijection at every order. As a check at prime orders two and three, construct points and lines from nonzero triples over \(\mathbb F_q\) normalized to have first nonzero coordinate one, with incidence given by zero dot product. Enumerate all sensor sets of size at most \(q\), form \(N_H[S]\), and count vertices in that set with exactly one neighbor outside it. Sizes below \(q\) give none; the totals of pairs \((S,x)\) at size \(q\) are 210 and 3,848 respectively. These finite checks do not replace the proof or assert that those placements all power dominate.
