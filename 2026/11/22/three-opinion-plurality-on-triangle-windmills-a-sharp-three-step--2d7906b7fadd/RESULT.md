# Three-opinion plurality on triangle windmills: a sharp three-step clock and a square-root equilibrium law

## Finding

Let \(F_m=K_1\vee(mK_2)\) denote the labelled friendship graph consisting of \(m\ge1\) triangles sharing exactly one hub. Each vertex carries one of three colors \(\{0,1,2\}\). Under synchronous *open-neighborhood plurality with incumbent retention*, a vertex copies the unique most frequent color among its neighbors; if there is no unique most frequent color, it retains its current color, even if that color is not a plurality winner. Let \(\Phi_m\) be this global map and let \(T(x)=\min\{t\ge0:\Phi_m^{t+1}(x)=\Phi_m^t(x)\}\).

**Uniform fixation and sharp boundary.** For every \(m\ge1\),
\[
\Phi_m^4=\Phi_m^3.
\]
There are no nonconstant recurrent orbits. The sharp maximal fixation times are \(1\) for \(m=1\), \(2\) for \(2\le m\le4\), and \(3\) for every \(m\ge5\).

**Exact equilibrium census.** Write \(E_m=\#\{x:\Phi_m(x)=x\}\). Then
\[
E_m=3\sum_{\substack{k+a+b+t=m\\ k,a,b,t\ge0}}
\frac{m!\,2^t}{k!a!b!t!}\,\mathbf1\!\left\{a=b\ \text{or}\ (2k\ge2a+t\ \text{and}\ 2k\ge2b+t)\right\}.
\]
In particular,
\[
E_m\sim 3\cdot5^m\sqrt{\frac5{4\pi m}}.
\]

**Typical first fixation times.** If all \(2m+1\) initial colors are independent uniform draws from \(\{0,1,2\}\), then
\[
\Pr(T=1)\longrightarrow\frac13,\qquad
\Pr(T=2)\longrightarrow\frac23,\qquad
\Pr(T=3)\le2e^{-2m/81}.
\]
The final hub color equals its initial color with probability at least \(1-2e^{-2m/81}\). Moreover,
\[
\Pr(T=0)=\frac{E_m}{3^{2m+1}}\sim
\left(\frac59\right)^m\sqrt{\frac5{4\pi m}}.
\]
The bound for \(\Pr(T=3)\) holds for every \(m\ge1\); the two limits refer to \(m\to\infty\).

## Assumptions and scope

All graphs are simple, with the hub incident to both ends of each of \(m\) disjoint peripheral edges, and no inter-petal edges. Three genuinely distinct colors are available; three-color ties are resolved by retaining the incumbent, not by a prescribed favorite color or randomization. Updates are synchronous. The hub has degree \(2m\), each peripheral vertex has degree two, and the vertex being updated is not one of its own neighbors. All states and counts are *labelled*, including both endpoints of each peripheral edge. No probabilistic assumption is needed for the deterministic results.

A peripheral edge has an unordered type among \(00,01,02,11,12,22\); the three mixed types admit two independently labelled orientations. Permuting peripheral edges never changes the fixation time. Consequently exhaustive enumeration of the six unordered edge types with their exact orientation/multinomial multiplicities covers the entire state space, not a sample.

## Proof

**Local locking rule.** Fix a hub color \(h\) and peripheral edge colors \(u,v\). If \(u=v\), both peripheral vertices retain their color forever: each sees one neighbor of its own color and one other neighbor, so it either sees a tie or its own color twice. If \(u\ne v\) and \(h\in\{u,v\}\), the vertex opposite \(h\) sees \(h\) twice and changes to \(h\); the other retains \(h\). The pair becomes monochromatic and remains so. If \(h\notin\{u,v\}\), each sees two distinct colors and retains its current color. Thus every update either freezes some mixed petals or leaves them untouched; a monochromatic petal never thaws.

**Three-step universal cutoff.** Write the hub colors at times zero and one as \(a,b\). At the first update every mixed petal containing \(a\) becomes monochromatic. If \(b\ne a\), every remaining mixed petal must contain \(b\), because there are exactly three available colors. Hence all petals are monochromatic at time two. With the peripheral configuration frozen, the hub is governed by the idempotent map "choose the unique peripheral plurality, if one exists, otherwise retain the present color." The time-three state is therefore fixed.

If instead \(b=a\), then at time one no remaining mixed petal contains the hub color \(a\), so the peripheral configuration does not change in the next update. If the hub stays at \(a\) again, the time-one state is fixed. Otherwise at time two the hub changes to a color \(c\ne a\), which must be the **unique** plurality of the (unchanged) petals. At time three the remaining mixed petals, all containing \(c\), become monochromatic of color \(c\); the hub remains \(c\), because its current peripheral neighbors still have the same unique plurality as in the preceding update. Locking these petals can only increase the number of \(c\)-colored peripheral neighbors and decrease the competing counts, so \(c\) remains the unique plurality thereafter. Hence time three is fixed in this case as well. This proves \(\Phi_m^4=\Phi_m^3\) for every \(m\).

**Sharpness.** The six-type finite enumeration described below gives the complete exact first-fixation counts for \(m=1,2,3,4\): respectively \((9,18,0,0)\), \((45,126,72,0)\), \((153,1062,972,0)\), and \((789,10926,7968,0)\), with coordinates for times \(0,1,2,3\). The checker exhausts every pair-type multiset with every possible hub color, weighting each by all labelled realizations; this is a complete finite verification for these four exceptional sizes.

For \(m=5\), an explicit time-three witness has hub color \(0\) and peripheral pairs \(00,01,12,12,12\); its hub trajectory is \(0,1,0,1\). For \(m=6\), take hub color \(2\) and pairs \(00,00,01,11,12,12\), with hub trajectory \(2,2,0,0\). For \(m=7\), take hub color \(2\) and pairs \(00,00,01,01,11,12,12\), again with hub trajectory \(2,2,0,0\). In the latter two examples, the final peripheral change is at time three. Appending one monochromatic petal of **each** color to a configuration adds two neighbors of each color to the hub at every update and never changes any old petal's evolution. Therefore this operation preserves the complete time-to-fix, extending the three witnesses to every \(m\ge5\) in their three residue classes modulo three.

**Equilibrium census.** By color symmetry fix the hub at zero. A fixed petal must be among \(00,11,22,12,21\); mixed petals involving zero would change. Suppose there are \(k\) petals of type \(00\), \(a\) of type \(11\), \(b\) of type \(22\), and \(t\) mixed petals of unordered type \(12\). The hub sees the three color counts
\[
(2k,\ 2a+t,\ 2b+t).
\]
It remains zero exactly if the other two colors tie (\(a=b\)), or if zero is tied for or has the largest count (\(2k\ge2a+t\) and \(2k\ge2b+t\)). For each tuple, there are \(m!/(k!a!b!t!)\) allocations of labelled petals and \(2^t\) orientations. Multiplying by the three hub choices proves the exact formula.

The contribution from \(a=b\) has the coefficient representation
\[
Q_m=[z^0](3+z+z^{-1})^m
=\frac{5^m}{2\pi}\int_{-\pi}^{\pi}
\left(\frac{3+2\cos\theta}{5}\right)^m\!d\theta.
\]
Since the integrand has its unique modulus-one point at zero and equals \(\exp(-m\theta^2/5+O(m\theta^4))\) there, elementary Laplace asymptotics give
\[
Q_m\sim5^m\sqrt{\frac5{4\pi m}}.
\]
All remaining fixed states can only arise from the event that color zero beats both opponents under an independent uniform distribution over the five admissible ordered petal types. For one such random petal the difference \(N_0-N_1\) is bounded between \(-2\) and \(2\) and has expectation \(-2/5\). Hoeffding's inequality therefore bounds the number of such states by \(5^m e^{-m/50}\). This is exponentially smaller than \(Q_m\). Multiplication by three proves the stated asymptotic for \(E_m\).

**Random fixation-time law.** Conditional on the hub initially being color zero, let \(A\) count peripheral petals containing zero, let \(B\) count type \(11\), let \(C\) count type \(22\), and let \(D\) count types \(12\) and \(21\). These mutually exclusive counts satisfy \(A+B+C+D=m\), with independent petal-category probabilities \((5,1,1,2)/9\). Following the first update, the peripheral color counts are exactly \((2A,2B+D,2C+D)\). Define the event
\[
\mathcal G=\{A>B+D\ \text{and}\ A>C+D\}.
\]
For each petal, the difference between its indicator for \(A\) and its indicator for \(B+D\) is in \([-1,1]\) with mean \(2/9\), and likewise for \(C+D\). Hoeffding plus a union bound gives \(\Pr(\mathcal G^c)\le2e^{-2m/81}\). On \(\mathcal G\), the initial hub color zero is the unique plurality at time one. If the first hub update kept zero, the state is already fixed at time one. Otherwise the hub returns to zero at time two while all remaining mixed petals become monochromatic, and their conversion can only favor the color they acquire over the third; the inequalities defining \(\mathcal G\) ensure zero remains strictly dominant. Thus every state on \(\mathcal G\) fixes no later than time two, with final hub color zero. By rotational symmetry the same holds for any initial hub color.

For independent uniform initial colors, the initial neighbor plurality is unique with probability \(1-O(m^{-1/2})\): equality of any two of the three neighbor counts is a sum of independent, aperiodic, nondegenerate integer-valued increments, for which the elementary local central limit bound is \(O(m^{-1/2})\). Its winning color is asymptotically uniformly distributed among the three colors. On \(\mathcal G\), an initial hub color which is initially a winning color yields \(T\le1\), while one which loses the first comparison yields \(T=2\). Finally the fraction of initially fixed states is \(E_m/3^{2m+1}\to0\). These facts imply the limits \(\Pr(T=1)\to1/3\) and \(\Pr(T=2)\to2/3\), and the explicit tail and final-hub bounds follow from \(\mathcal G\).

## Verification

The standalone Python-standard-library program `verify.py` implements a hub/petal update from the rule above and an independent update on every labelled vertex from the actual graph adjacency. It exhaustively checks every labelled initial coloring for all three-opinion graphs with \(1\le m\le5\), tests the resulting first-fixation census against a separately implemented six-type weighted census, verifies the equilibrium multinomial formula for \(1\le m\le10\), checks the complete exceptional-size boundary \(m\le4\), and tests explicit time-three witnesses. The complete weighted enumerations for \(m\le10\) cover all \(3^{2m+1}\) labelled configurations at each size via exact orientation and factorial weights. Results are recorded in `verification_counts.txt`; no simulation is used as an infinite-size proof. Run `python3 verify.py` to reproduce the finite checks. The preceding symbolic argument establishes the universal statements.

## Relationship to prior work

Plurality dynamics with more than two alternatives is studied by Mossel, Neeman and Tamuz (2012); their explicit multicolor periodicity proposition assumes a weighted graph with **no tied neighbor votes** and establishes only eventual period at most two. It does not address the present tie-retaining rule on unweighted friendship graphs, its sharp transient time, or its exact equilibrium and fixation-time laws. Binary majority dynamics on arbitrary graphs is also well studied, including Tamuz and Tessler's 2013 public preprint. The published binary majority census on friendship graphs proves a two-round bound and a different equilibrium/basin formula; it does not cover three distinct colors, where both a new third-round transient and square-root-corrected equilibrium entropy arise. A published three-color, threshold-two cyclic-successor result on the same friendship graphs permits primitive three-cycles, whereas this rule always freezes; the transition and attractor mechanisms are different, not special cases of one another. Becchetti and collaborators consider randomized three-sample many-opinion dynamics on complete graphs rather than deterministic all-neighbor tie-retaining plurality on a friendship graph. The more recent three-opinion deterministic models of Di Ianni use different update conditions and graph-wide complexity objectives, not this local hub/petal theorem. The existence of general period-at-most-two theorems for binary majority does not imply the universal three-state three-step cutoff or the equilibrium and first-entry laws here.

## Limitations

The result is specific to exactly three opinions, the open-neighbor plurality rule with *incumbent retention on every tie*, fully synchronous updates, and friendship graphs. It does not determine individual fixed-point basin sizes or arbitrary nonuniform initial-color laws, and it makes no statement about larger palettes, arbitrary triangle cacti, stochastic ties, or asynchronous updates. The exponential bound on time-three probability is not claimed sharp. Absolute historical uniqueness cannot be inferred from indexed searches alone; an unindexed equivalent formulation may exist. Independent external validation has not been performed.

## References

1. E. Mossel, J. Neeman, and O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, arXiv:1207.0893v1, public July 4, 2012, Section 6.2, https://arxiv.org/html/1207.0893v1 .
2. O. Tamuz and R. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035v1, public July 15, 2013, https://arxiv.org/abs/1307.4035 .
3. L. Becchetti, A. Clementi, E. Natale, F. Pasquale, and L. Trevisan, *Stabilizing Consensus with Many Opinions*, arXiv:1508.06782v1, public August 27, 2015, https://arxiv.org/abs/1508.06782 .
4. M. Di Ianni, *Three Majority-Based Deterministic Dynamics for Three Opinions*, AppliedMath 5(4), 147 (2025), DOI:10.3390/appliedmath5040147, https://www.mdpi.com/2673-9909/5/4/147 .
5. *Exact attraction basins and rapid stabilization of majority dynamics on friendship graphs*, published mathematical record 6882fd08f78e, published-finding corpus (2026), https://github.com/published-finding corpus/2026 .
6. *Three-step collapse and the exact oscillation basin of threshold-two cyclic dynamics on friendship graphs*, published mathematical record 6dd9f02f5859, published-finding corpus (2026), https://github.com/published-finding corpus/2026 .
