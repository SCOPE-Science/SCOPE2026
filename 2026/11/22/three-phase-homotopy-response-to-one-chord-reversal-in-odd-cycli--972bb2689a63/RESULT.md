# Three-phase homotopy response to one chord reversal in odd cyclic tournaments

## Finding

For every integer \(m\ge2\), orient a tournament \(R_{2m+1}\) on \(\{0,\ldots,2m\}\), with an arc \(i\to i+j\pmod{2m+1}\) whenever \(1\le j\le m\). Let \(T_{m,d}\) reverse precisely the arc \(0\to d\), where \(1\le d\le m\), and put \(X_{m,d}=\operatorname{dFl}(T_{m,d})\), the simplicial complex of vertex sets inducing transitive tournaments. Then

\[X_{m,d}\simeq\begin{cases}S^1,&d=m,\\S^2,&m\ge3\text{ and }d=m-1,\\\ast,&\text{otherwise}.\end{cases}\]

Thus the penultimate chord reversal, unlike any shorter chord reversal, produces a two-sphere, while the longest reversal preserves one circle. The first case where the two-sphere occurs is the seven-vertex tournament.

## Assumptions and scope

Only finite odd regular cyclic tournaments of order at least five and exactly one reversed arc are included. Distance \(d\) means the clockwise arc length before reversal; cyclic rotations carry every arc of a fixed distance to the selected arc. The directed flag complex is a simplicial complex rather than a tournaplex: each transitive subtournament contributes a unique simplex because every tournament has at most one topological ordering compatible with all arcs. Homotopy equivalences, hence homology with every coefficient ring, are asserted; no equivariant equivalence is asserted.

## Proof

**A link-collapse criterion.** Suppose a vertex \(v\) of a simplicial complex has a collapsible link. The cone over the link, namely the closed star of \(v\), collapses relative to the link, so the whole complex collapses onto its induced deletion of \(v\). For the tournament links used below, the incoming and outgoing vertex classes each induce a transitive tournament. The link is therefore the clique complex of a graph with two complete vertex classes: a cross pair is present exactly when its two vertices and \(v\) form a transitive triple. If \(N[u]\subseteq N[w]\) in this graph, deletion of \(u\) is an elementary strong collapse. All the following dismantling steps satisfy this *closed-neighborhood* inclusion, verified using the displayed cross-pair inequalities.

**Inductive reduction for \(m\ge4\) and \(2\le d\le m\).** First delete tournament vertex \(1\). Its link graph has complete classes \(A=\{0,m+2,\ldots,2m\}\) and \(B=\{2,\ldots,m+1\}\). The cross edges are exactly

- \((0,b)\) for \(2\le b\le m\) except \(b=d\);
- \((a,b)\) for \(m+2\le a\le2m\), \(2\le b\le a-m-1\).

If \(d\ge3\), fold each \(b=3,\ldots,m+1\) into vertex \(2\), fold \(0\) into \(m+3\), then fold \(2\) and \(m+2\) into \(m+3\). The remaining vertices \(m+3,\ldots,2m\) form one simplex. If \(d=2\), first fold each \(b=4,\ldots,m+1\) into \(3\), then fold \(0\) into \(m+4\), \(3\) into \(2\), and \(2,m+2\) into \(m+3\); again a simplex remains. The existence of vertex \(m+4\) requires \(m\ge4\), explaining the exceptional seven-vertex base below.

After deleting vertex \(1\), delete \(m+1\). Its link graph has complete classes \(A=\{2,\ldots,m\}\) and \(B=\{0,m+2,\ldots,2m\}\). Its cross edges are \((d,0)\) together with all \((a,b)\) satisfying \(2\le a\le m\), \(m+2\le b\le m+a\). Fold \(0\) into \(m+2\), fold successive vertices \(2\to3\to\cdots\to m\), and fold \(m\) into \(m+2\); the remaining class \(B\setminus\{0\}\) is a simplex. Thus both links are collapsible.

Removing these two tournament vertices, then relabeling the survivors in increasing order, yields *exactly* \(T_{m-1,d-1}\); checking the arcs amounts to the two inequalities \(1\le(j-i)\pmod{2m+1}\le m\) and \(1\le(j'-i')\pmod{2m-1}\le m-1\). Hence \(X_{m,d}\searrow X_{m-1,d-1}\) for all stated parameters. The same fold proof works for the boundary \(m=3,d=3\).

**Adjacent reversal reduction.** For \(d=1\), \(m\ge3\), remove vertices \(2\) and \(m+2\) successively. The first link graph has complete classes \(A=\{0,1,m+3,\ldots,2m\}\), \(B=\{3,\ldots,m+2\}\). Cross edges are exactly \((0,b)\) for \(3\le b\le m\), \((1,b)\) for \(3\le b\le m+1\), and \((a,b)\) for \(m+3\le a\le2m\), \(3\le b\le a-m-1\). Fold \(B\setminus\{3\}\) into \(3\), all of \(A\setminus\{0\}\) into \(0\), then \(3\) into \(0\).

The second link, after deleting \(2\), has complete classes \(A=\{3,\ldots,m+1\}\), \(B=\{0,1,m+3,\ldots,2m\}\). Its cross edges are \((m+1,0)\) and \((a,b)\) for \(3\le a\le m+1\), \(m+3\le b\le m+a\). Fold \(1\) into \(0\), \(0\) into \(m+3\), \(3\to4\to\cdots\to m+1\), then \(m+1\) into \(m+3\); the remaining vertices form a simplex. The survivor tournament is exactly \(T_{m-1,1}\), hence \(X_{m,1}\searrow X_{m-1,1}\). These steps independently establish the previously known adjacent-reversal result.

**Three finite bases.** At \((m,d)=(2,1)\), the twenty-one nonempty faces collapse in ten free-face pairs to a vertex. At \((2,2)\), twenty-two faces collapse in eight pairs to a three-edge circle. At \((3,2)\), fifty-six faces collapse in eight pairs to a connected two-complex with face vector \((7,19,14)\). Choosing a spanning tree of its one-skeleton gives thirteen free fundamental-group generators. Its fourteen triangle relators eliminate all thirteen by legitimate unit-occurrence Tietze substitutions, leaving the trivial group; the remaining relators reduce to the identity. The resulting simply connected, two-dimensional complex has Euler characteristic \(7-19+14=2\), hence integral second homology \(\mathbb Z\) and no other reduced homology. The degree-one Hurewicz isomorphism in dimension two and Whitehead's theorem give a homotopy equivalence with \(S^2\). The accompanying program reconstructs every free-face pair and every Tietze substitution without external dependencies.

Now for \(d=m\), repeatedly reduce to \((2,2)\); for \(d=m-1\) with \(m\ge3\), repeatedly reduce to \((3,2)\); for \(2\le d\le m-2\), repeatedly reduce to some adjacent case, then to \((2,1)\). This exhausts all allowed parameters.

## Verification

The standalone `verify.py` constructs the transitive-subtournament faces from directed 3-cycle avoidance, checks all elementary collapses for the three bases, checks the thirteen-generator group elimination, compares each proposed link cross-edge formula with actual tournament triples, and checks each displayed graph-fold sequence as a closed-neighborhood containment. Finite checks were replayed successfully for every \(3\le m\le33\) and all applicable chord distances, plus complete face computations through \(m=7\). The infinite proof is the explicit interval-inequality argument above, not an extrapolation from these checks.

## Relationship to prior work

Govc's 2020 work gives the general directed flag-complex method and a finite classification of tournament homotopy types through ten vertices; that finite census covers the small bases as abstract cases but does not state or entail this unbounded chord-distance theorem. Govc, Levi and Smith (2021) develop the broader tournaplex filtration, of which the directed flag complex is a subcomplex. Previously published work on a single adjacent reversal establishes the contractible \(d=1\) case, and on two disjoint adjacent reversals establishes a different two-fault phenomenon; these are credited rather than claimed. The new content is the uniform long-chord trichotomy for all odd orders, established with the two-vertex collapse.

## Limitations

The theorem does not classify multi-arc reversals, noncyclic tournaments, dihedral actions, or persistence maps under further reversals. A finite tournament homotopy census can contain all small instances without proving the asserted unbounded pattern. Search coverage cannot rule out unindexed equivalent work.

## References

- D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333 (first public version June 9, 2020), especially Section 3 on finite tournament classifications, https://arxiv.org/abs/2006.05333.
- D. Govc, R. Levi and J. P. Smith, *Complexes of tournaments, directionality filtrations and persistent homology*, Journal of Applied and Computational Topology 5 (2021), 313–337, https://doi.org/10.1007/s41468-021-00068-0.
- *A single adjacent reversal contracts the cyclic tournament flag complex*, published published-finding corpus finding, October 4, 2026, identifier `published-finding corpus adjacent-reversal finding (October 4, 2026)` (contextual comparison; the adjacent reduction is proved again here).
