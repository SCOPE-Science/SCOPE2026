# Odd-period rigidity and an interlaced bifurcation staircase for right-triangle farthest projections

## Finding

The farthest-orthogonal-projection map of a right triangle has a complete and unexpectedly rigid **nonconstant odd-period spectrum** once its leg aspect ratio is at least two. Every nonfixed odd cycle must pass through the right-angle vertex. Consequently there can be at most one such cycle, and its existence and exact least period admit a logarithmic formula. There are infinitely many isolated parameter values where the cycle disappears into a tie-fixed point, interlaced with the usual period-jump parameters.

Let \(h\ge2\), and define
\[
q=\sqrt{1+h^2},\qquad b=\frac{h^2}{1+h^2},\qquad
c=\frac{h}{h+1},\qquad d=\frac{q}{q+1},
\]
\[
\rho(h)=\frac{\log d}{\log b},\qquad
\sigma(h)=\frac{\log c}{\log b}.
\]
Then \(1<\rho(2)<\sigma(2)<2\), both functions are strictly increasing to infinity, and
\(0<\sigma(h)-\rho(h)<1\).

**Theorem.** Among all nonconstant periodic orbits with odd least period \(\ge3\), there are:

- No cycles if \(\rho(h)\in\mathbb Z\) or \(\sigma(h)\in\mathbb Z\).
- Otherwise exactly one cycle, with least period
\[
P(h)=2\lfloor\rho(h)\rfloor+3.
\]
It contains \(O=(0,0)\), and every point in some relatively open neighborhood of that cycle on the union of supporting lines is mapped **exactly onto the cycle in finitely many iterations**. As \(h\) varies, the realized least periods are precisely \(5,7,9,\ldots\); furthermore \(P(h)=2h+O(1)\) as \(h\to\infty\).

For each integer \(m\ge2\), let \(s_m,r_m\) be the unique solutions of
\[
\sigma(s_m)=m,\qquad\rho(r_m)=m.
\]
They satisfy
\[
2<s_2<r_2<s_3<r_3<\cdots,
\]
and are exactly the exceptional aspect ratios. At \(s_m\) the orbit of \(O\) reaches a fixed tie on the hypotenuse, while at \(r_m\) it reaches a fixed tie on the vertical leg. The first thresholds are \(s_2=2.2055694304\ldots\) (the unique root \(>2\) of \(h^3-2h^2-1=0\)) and \(r_2=2.3654204555\ldots\) (the unique root \(>2\) of \(h^8=(1+h^2)(1+2h^2)^2\)).

## Assumptions and scope

Work on the union of the **complete supporting lines**
\[
L_0=\{(x,0):x\in\mathbb R\},\quad
L_1=\{(0,y):y\in\mathbb R\},\quad
L_2=\{(x,y):hx+y=h\}
\]
of the right triangle \(O=(0,0)\), \(A=(1,0)\), \(B=(0,h)\), with \(h\ge2\). From a point on one line, project perpendicularly to whichever of the other two lines has the larger Euclidean distance. At equality, leave the point fixed. At a line intersection, the unique nonzero-distance projection is used; this is independent of which incident line represents the point. This is the original *unrestricted-line* version of the map, not the boundary-of-triangle variant.

A **nonconstant odd periodic orbit** is an orbit with primitive least period an odd integer \(\ge3\). Fixed points (least period one) are explicitly excluded. The theorem does not assert that all orbits converge to the odd cycle, nor does it classify even-period orbits, orbits converging to fixed points, or the full basin.

## Proof

**1. An odd-cycle rigidity lemma.** A nonfixed point on a unique line \(L_i\) is sent to a point on a different line, unless it is tie-fixed. Consider a periodic orbit avoiding all three vertices. Its cyclic line itinerary has no consecutive repeated labels. Without traversing the edge between \(L_0\) and \(L_1\), the itinerary lies in the bipartite graph with parts \(\{L_2\}\) and \(\{L_0,L_1\}\), and therefore has even length. Hence any odd itinerary traverses \(L_0\leftrightarrow L_1\). Those two lines are perpendicular: their mutual orthogonal projection is always \(O\). This contradicts vertex avoidance. If a periodic orbit contains either of the other vertices \(A\) or \(B\), its next image is \(O\): the only nonzero-distance projection from either vertex is onto the opposite leg. Thus **every nonconstant odd periodic orbit contains \(O\)**. In particular, there is at most one such orbit.

**2. A complete explicit itinerary of \(O\).** Write \(b=h^2/(1+h^2)\) and \(q=\sqrt{1+h^2}\). The projection of \(O\) onto \(L_2\) is \((b,h(1-b))\). If a point \((x,h(1-x))\in L_2\) has \(0<x<1\), its vertical-leg projection is farther than its horizontal-leg projection exactly when \(x>c=h/(h+1)\); equality gives a fixed tie. If \((0,y)\in L_1\) has \(0<y<h\), its hypotenuse projection is farther than its horizontal-leg projection exactly when \(y<(h-y)/q\); equality gives a fixed tie.

As long as the latter choice continues, the iterates have the explicit form
\[
T_h^{2j-1}(O)=(b^j,h(1-b^j))\in L_2,\qquad
T_h^{2j}(O)=(0,h(1-b^j))\in L_1
\]
for the admissible indices \(j\ge1\). The second formula is followed by another hypotenuse visit if and only if \(b^j>d=q/(q+1)\). Because \(h\ge2\), we have \(b>d>c\): equivalently \(h^2>q\) gives the first inequality, while \(q>h\) gives the second. Thus \(j=1\) is certainly admissible.

Set
\[
k=\min\{j\ge2:b^j\le d\}.
\]
All earlier choices are strict, since for \(j<k\) we have \(b^j>d>c\). At time \(2k-1\) the orbit is at the hypotenuse point with horizontal coordinate \(b^k\). If \(b^k=c\), the two axis distances are equal, so the orbit becomes fixed there. If \(b^k=d\), then \(d>c\), so the next image is on \(L_1\) and is tie-fixed there. The two equalities are disjoint.

Otherwise \(b^k<d\) and \(b^k\ne c\). If \(b^k>c\), the hypotenuse point projects onto \(L_1\), and the next step projects onto \(L_0\), returning to \(O\) at time \(2k+1\). If \(b^k<c\), the hypotenuse point projects onto \(L_0\) at \((b^k,0)\). Since \(b^{k-1}>d\), we have \(b^k>bd\), and \(bd>8/15>1/2\) for \(h\ge2\). On \(L_0\) at \(x>1/2\), the distance to \(L_1\) is \(x\), exceeding the distance \(h(1-x)/q\) to \(L_2\); hence the next image is again \(O\), now on \(L_1\). This occurs at time \(2k+1\), with no earlier return and no tie. Thus the return is primitive.

Since \(0<b<1\), the inequality \(b^k\le d\) is equivalent to \(k\ge\rho(h)=\log d/\log b\). Away from equality, \(k=\lfloor\rho\rfloor+1\). The tie conditions \(b^k=d\) and \(b^k=c\) are precisely \(\rho\in\mathbb Z\) and \(\sigma\in\mathbb Z\), respectively: the latter uses \(\rho<\sigma<\rho+1\) proved in Step 3. For a strict return we obtain \(P=2k+1=2\lfloor\rho\rfloor+3\). Step 1 supplies the uniqueness and, when the vertex orbit becomes fixed, the absence of all nonconstant odd cycles.

**3. Monotonicity, exceptional parameters, and asymptotics.** Both \(\rho\) and \(\sigma\) increase strictly for \(h\ge2\). For \(\sigma\), differentiation of the quotient of negative logarithms reduces positivity of the derivative to
\[
2(h+1)\log(1+1/h)>(h^2+1)\log(1+1/h^2).
\]
The left side is \(>2\) by \(\log(1+t)>t/(1+t)\), while the right side is \(<1+h^{-2}\le5/4\). For \(\rho\), the analogous sufficient and necessary inequality is
\[
2(q+1)\log(1+1/q)>h^2\log(1+1/h^2),
\]
where the left side exceeds \(2\) and the right side is below \(1\). Also \(q>h\) implies \(c>d\) is false; in fact \(c<d\), so \(\rho<\sigma\). Finally
\[
\frac cd=\frac{h(q+1)}{q(h+1)}>\frac{h^2}{q^2}=b
\]
because \(q(q+1)>h(h+1)\); taking logarithms, with \(\log b<0\), gives \(\sigma-\rho<1\). At \(h=2\), both are strictly between one and two, and both tend to infinity. Therefore each integer level \(m\ge2\) has a unique root on each curve, and \(s_m<r_m<s_{m+1}\) by the strict sandwich \(\rho<\sigma<\rho+1\). The first equations reduce to the stated integer polynomials.

For any \(h\to\infty\), elementary logarithmic expansions give \(\rho(h)=h-1/2+O(1/h)\). Hence \(P(h)=2h+O(1)\) at nonexceptional parameters. The ordered crossings show that \(\lfloor\rho\rfloor\) takes every integer \(\ge1\) on a nonempty open parameter interval with only one isolated \(\sigma\)-tie in it. Thus each odd integer \(\ge5\) occurs.

**4. Finite-time attraction.** At a nonexceptional parameter every branch choice along the periodic orbit is strict except at the vertex \(O\), where the hypotenuse is uniquely at positive distance. The final transition is between perpendicular legs, so it is a constant projection to \(O\) on a relatively open interval around the incoming point. Continuity of all intermediate orthogonal projections within their strict-choice regions produces a relative open neighborhood of the entire cycle whose orbits fall exactly onto that cycle after finitely many steps. This proves the asserted local finite-time capture, which is stronger than geometric convergence.

## Verification

The accompanying `CHECK.py` uses exact rational coordinates and squared-distance comparisons; it makes no floating-point choices. It tests \(4001\) rational values of \(h\) between \(2\) and \(50\), independently computes the first exit from the alternating itinerary and simulates the actual projection map, and checks period and line-itinerary invariants. It passes **20,009** exact-rational assertions; the largest tested primitive period is \(101\). These are supporting finite checks only. Every universal and exceptional-parameter statement above is proved analytically; rational-grid testing is not substituted for uncountable-real verification.

## Relationship to prior work

Samuel Everett introduced this farthest-orthogonal-projection map and established general asymptotic periodicity / convergence to fixed points. The source's detailed bifurcation discussion treats isosceles triangles, not the exact complete odd-period census of right triangles with aspect ratio \(h\ge2\). The preprint `arXiv:2408.16019` is a later open-access version of the article published online January 7, 2021; the latter, not the later arXiv posting, determines the source date.

A published 2026 classification of primitive period-three cycles for arbitrary triangles covers that shorter period and is not claimed to be improved or rediscovered here. Its statement does not determine the higher odd periods \(5,7,9,\ldots\) or the two interlaced high-aspect parameter sequences. A separate exact computation for the right-isosceles case \(h=1\) counts period-four cycles, outside the present parameter range and parity class. The new point is the **complete odd-cycle rigidity and explicit period staircase, including its exact exceptional tie parameters and finite-time capture**, not the known global convergence theorem or any existing period-three count.

## Limitations

The parameter restriction \(h\ge2\) is essential to this elementary itinerary proof; no claim is made for \(0<h<2\). The theorem does not count fixed points, even primitive cycles, global basins, or all nonperiodic orbit behavior. The dynamics at exceptional parameters may have other even cycles; only odd cycles are ruled out. No independently performed mathematical audit is asserted. A logically equivalent formula in unindexed literature cannot be excluded solely by record searches.

## References

- S. Everett, *A Piecewise Contractive Map on Triangles*, Journal of Dynamical Systems and Geometric Theories 18(2), 183–192 (2020 volume), first published online 2021-01-07. DOI: `10.1080/1726037X.2020.1847765`. Full preprint `arXiv:2408.16019` (posted 2024-08-26).
- *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, published mathematical research record, 2026-10-11, identifier `2026/10/11/SCOPE-exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8`.
