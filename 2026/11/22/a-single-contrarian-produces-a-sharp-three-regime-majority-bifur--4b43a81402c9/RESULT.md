# A single contrarian produces a sharp three-regime majority bifurcation on bicliques

## Finding

Let \(a,b\ge1\). On the labelled complete bipartite graph \(K_{a,b}\), distinguish one vertex in the shore of size \(a\). Every other vertex uses synchronous strict open-neighbour binary majority, retaining its own bit when the two opinions tie. The distinguished vertex adopts the *opposite* of a strict neighbour majority, likewise retaining its bit on ties. Let \(F\) be the resulting global map on \(\{0,1\}^{a+b}\). A state first becomes periodic at time \(t\) when \(F^t(x)\) is periodic and none of \(x,F(x),\ldots,F^{t-1}(x)\) is periodic.

Write
\[
H_r=\begin{cases}\binom{r}{r/2},&r\text{ even},\\0,&r\text{ odd},\end{cases}\qquad Z=2^{a+b}.
\]

**Theorem (complete attraction census).**

1. If \(a=1\), there is one primitive four-cycle and no other periodic orbit. Its basin contains all \(Z\) states, with \(4\) states initially periodic and \(Z-4\) entering after one update.

2. If \(a=2\), all attractors are fixed. Their number is \(2^b+H_b\). Two polar fixed states have individual basin size \(2^b+2\); exactly \(2^b-H_b-2\) additional fixed states have individual basin size \(2\); and exactly \(2H_b\) fixed states have singleton basins. The first-periodic-entry counts, at times \(0,1,2\), are respectively
\[
N_0=N_2=2^b+H_b,\qquad N_1=2^{b+1}-2H_b.
\]

3. If \(a\ge3\), there are precisely two polar fixed points, one primitive two-cycle, and \(H_aH_b\) additional fixed points with singleton basins. Define
\[
O_{a,b}=\frac{(2^a-H_a)(2^b-H_b)}2.
\]
The unique two-cycle attracts exactly \(O_{a,b}\) initial states. Each polar fixed point has individual basin size
\[
\frac{Z-O_{a,b}-H_aH_b}{2}.
\]
The first-periodic-entry census is
\[
\begin{aligned}
N_0&=4+H_aH_b,\\
N_2&=H_a(2^b-2-H_b)+H_b(2^a-2-H_a),\\
N_1&=Z-N_0-N_2.
\end{aligned}
\]
There are no states of greater entrance depth. A configuration enters the two-cycle **if and only if** both shores initially have strict majorities and those majorities disagree. This is exactly the same configuration-wise oscillation basin as for ordinary strict majority on \(K_{a,b}\), without a contrarian vertex.

In particular, the uniform-initialization oscillation probability for \(a\ge3\) equals
\[
\frac12\left(1-\frac{H_a}{2^a}\right)\left(1-\frac{H_b}{2^b}\right),
\]
which is exactly one half when both shores are odd and tends to one half as both shore sizes tend to infinity. The transitions \(a=1\) (certain period four), \(a=2\) (no oscillation), and \(a\ge3\) (one two-cycle with a positive basin) are sharp.

## Assumptions and scope

All graphs are simple, finite, complete bipartite and labelled. There is exactly one designated contrarian in the first shore; each bit is updated simultaneously from the *old* neighbouring bits, excluding self-neighbours. In an even-degree neighbourhood tie, the vertex preserves its old bit, including at the contrarian. The initial-state distribution is uniform only for the probability statement; every deterministic population count is for all \(Z\) labelled bit vectors.

For a state let \(c\in\{0,1\}\) denote the contrarian bit, \(x\) the number of ones among the other \(a-1\) vertices of its shore, and \(y\) the number of ones in the opposite shore. Write \(S=x+c\). Although \((x,c,y)\) loses positional information, the update acts compatibly on it and each signature has multiplicity \(\binom{a-1}{x}\binom{b}{y}\). This is not a claim that distinct labelled states are identical.

## Proof

**Exact one-step reduction.** When \(2y>b\), every conformist of the first shore becomes one and the contrarian becomes zero; when \(2y<b\), every conformist becomes zero and the contrarian becomes one; when \(2y=b\), that whole shore remains unchanged. Independently, the opposite shore becomes all one for \(2S>a\), all zero for \(2S<a\), and remains unchanged for \(2S=a\). Thus the signature transition is
\[
(x,c,y)\longmapsto (x',c',y'),
\]
with
\[
(x',c')=\begin{cases}(a-1,0),&2y>b,\\ (0,1),&2y<b,\\ (x,c),&2y=b,\end{cases}
\qquad
y'=\begin{cases}b,&2S>a,\\0,&2S<a,\\y,&2S=a.\end{cases}
\]
These formulas also preserve the labelled bits on tied shores; hence they determine every labelled orbit.

**The case \(a=1\).** The opposite shore becomes uniform with the old contrarian bit after one step. Once that shore is uniform, the contrarian flips against it and the shore follows the old contrarian bit. The four configurations having uniform opposite shore form one primitive four-cycle. Every initial state enters it by time one; only those four configurations are initially periodic.

**The case \(a=2\).** A strict majority in the opposite shore sends the two-vertex shore to one of \((c,x)=(1,0)\) and \((0,1)\). Both have \(S=1\), exactly tied for the opposite-shore update, so the opposite shore subsequently freezes. If initially \(S=1\), that opposite shore already freezes, and the first shore reaches its corresponding stationary pattern in at most one update. If initially \(S\) is zero or two, the opposite shore becomes unanimous in one update and both shores are fixed by the second. Fixed points have \(S=1\), with the contrarian one when the opposite shore has strictly fewer than half ones, conformists one when it has strictly more than half, and either pattern when tied. This gives \(2^b+H_b\) fixed states.

To count individual basins, an initial first shore with \(S=0\) inevitably ends at the polar fixed state with opposite shore all zero, whatever its opposite-shore starting pattern; similarly \(S=2\) ends at the all-one opposite-shore polar state. Initial \(S=1\) keeps the opposite shore unchanged. Therefore the two polar fixed points each have \(2^b+2\) predecessors in their full basins; every nonunanimous, nontied opposite-shore pattern has one fixed first-shore pattern with basin two (both initial \(S=1\) patterns); and every tied opposite-shore pattern has two isolated fixed states. The stated basin multiplicities follow. Entrance time two occurs exactly from initial \(S=0\) with opposite-shore strict majority one or a tie, or initial \(S=2\) with opposite-shore strict majority zero or a tie. Each collection contributes \(2^{b-1}+H_b/2\) states; hence \(N_2=2^b+H_b\). As \(N_0\) equals the fixed-point count, subtraction from \(Z\) yields \(N_1\).

**The case \(a\ge3\).** Define the two canonical first-shore patterns \(P=(c=0,x=a-1)\) and \(Q=(c=1,x=0)\). Their shore totals \(a-1\) and \(1\) have respectively strict positive and negative majorities *precisely because* \(a\ge3\). If both initial shore majorities are strict, one update sends each shore to its canonical pattern corresponding to the *other* shore's initial majority. Equal initial signs give one of the polar fixed points \((P,1^b)\), \((Q,0^b)\); opposite signs give the two configurations \((P,0^b)\), \((Q,1^b)\) of a single two-cycle. If exactly one shore is initially tied, it holds its old pattern for one step; the other shore becomes canonical, and after one further update both settle into a polar fixed point. If both shores are tied, every bit is fixed at once. Because canonical patterns have strict signs and unanimity is strict in any nonempty shore, this exhausts all eventual behavior.

The number of labelled configurations with a tied shore of size \(r\) is \(H_r\). By global bit complementation, the two strict majority signs each occur in exactly \((2^r-H_r)/2\) configurations. Hence opposite strict signs occur in exactly \(2\cdot(2^a-H_a)/2\cdot(2^b-H_b)/2=O_{a,b}\) initial states. The states tied on both shores number \(H_aH_b\), and none has a transient predecessor: a nontied shore becomes canonical or unanimous and cannot subsequently become tied. These are singleton-basin fixed points. The remaining configurations split equally by complementation between the two polar fixed points. This proves the individual basin sizes and configuration-wise invariance relative to ordinary majority, which has the same strict-sign criterion.

The immediately recurrent states are the two polar fixed points, the two phases of the unique two-cycle, and the \(H_aH_b\) doubly tied states. For entrance time two, there are two disjoint possibilities: the first shore is initially tied and the second is neither unanimous nor tied; or the second is initially tied and the first is neither canonical nor tied. Their labelled counts are \(H_a(2^b-2-H_b)\) and \(H_b(2^a-2-H_a)\), respectively. All other transient states enter after one update, proving the time census.

## Verification

The accompanying scripts provide independent exact tests of the reduction and the formulas. `check_direct.py` exhaustively follows 260,100 labelled initial states for all 64 parameter pairs with \(1\le a,b\le8\), checking entrance depths, eventual periods, and counts. `check_quotient.py` separately constructs the weighted three-coordinate transition and verifies exact binomial-weighted counts for all 1,600 pairs with \(1\le a,b\le40\). `check_basins.py` enumerates individual attractor basin sizes independently for the 64 smaller pairs. `check_invariance.py` checks, configuration by configuration on 257,040 states with \(3\le a\le8\), \(1\le b\le8\), that the oscillation basin is unchanged relative to ordinary majority. Each script is standalone apart from the documented local import of `check_direct.py` by `check_invariance.py`; run all in the same directory with Python 3.9 or later.

The infinite-parameter statements are proved by the three-coordinate recurrence and combinatorial identities, not by finite experimental extrapolation. The scripts check implementation and boundary cases; they do not independently certify historical originality.

## Relationship to prior work

Haslegrave and Cannings, arXiv:1606.05496v1 (2016), study a single nonconforming vertex on general graphs and prove a broad period-set restriction, including periods one, two and four for a triangle-free simple graph. That theorem does not determine this complete-bipartite family's *absence* of periods four when \(a\ge2\), the sharp two-step relaxation, the exact individual basins, or their configuration-wise invariance under changing one agent's rule. Cannings (2009) studies mixed majority/minority games on complete networks, hypercubes, and cubic examples; its available abstract does not settle the present biclique census. Bagnoli and Rechtman (2015) consider a stochastic reasonable-contrarian model and associated mean-field bifurcations with different local rules. The present result is a deterministic, exact, all-parameter local-defect classification; it makes no claim of novelty for the general period restrictions.

## Limitations

The theorem applies to one designated minority-rule vertex, the specified tie-retaining convention, and complete bipartite graphs. It does not address arbitrary graphs, additional contrarians, stochastic updates, or other tie policies. Its equality of oscillation basins with the unperturbed process holds only when the contrarian's shore has at least three vertices. Historical priority could be affected by unindexed literature, particularly earlier work on mixed majority/minority games whose full text was not available during this comparison. Independent external mathematical audit has not been performed.

## References

1. J. Haslegrave and C. Cannings, *Majority dynamics with one nonconformist*, arXiv:1606.05496v1, first submitted 2016-06-17, https://arxiv.org/abs/1606.05496.
2. C. Cannings, *The majority and minority models on regular and random graphs*, GameNets (2009), DOI:10.1109/GAMENETS.2009.5137464, https://eudl.eu/doi/10.1109/gamenets.2009.5137464.
3. F. Bagnoli and R. Rechtman, *Bifurcations in models of a society of reasonable contrarians and conformists*, arXiv:1503.01016, first submitted 2015-03-03, https://arxiv.org/abs/1503.01016.
4. E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications*, Discrete Applied Mathematics 3 (1981), 93–105; general threshold-network background.
