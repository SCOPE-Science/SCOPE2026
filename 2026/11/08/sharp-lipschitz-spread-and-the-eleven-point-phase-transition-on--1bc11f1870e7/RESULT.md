# Sharp Lipschitz spread and the eleven-point phase transition on Kneser pair graphs

## Finding
Let \(G_n=KG(n,2)\), \(n\ge6\), have the two-subsets of \([n]\) as vertices, with unit edges exactly between disjoint two-subsets. Give the \(N=\binom n2\) vertices uniform probability. Define
\[
\mathcal S(G_n)=\max_{\operatorname{Lip}(f)\le1}\left(\frac1N\sum_v f(v)^2-\left(\frac1N\sum_v f(v)\right)^2\right).
\]
This is the squared norm of the canonical inclusion of the real graph-Lipschitz space modulo constants into centered \(L^2\). Put
\[
E_n=N(2n-3)-(2n-5)^2,\qquad B_n=\left\lfloor\frac{N^2}{4}\right\rfloor.
\]
Then
\[
\boxed{\mathcal S(G_6)=\frac{86}{225},\qquad
\mathcal S(G_n)=\frac{\max\{E_n,B_n\}}{N^2}\quad(n\ge7).}
\]
The exceptional pattern wins for \(7\le n\le10\); both patterns tie at \(n=11\); and the balanced binary pattern wins for all \(n\ge12\). In particular the sharp norm reaches the complete-graph benchmark precisely at \(n\ge11\), despite the missing intersecting-pair edges in the Kneser graph.

All equality cases are explicit. For \(7\le n\le10\), choose one two-set \(e\), assign it value \(0\), every other two-set intersecting \(e\) value \(2\), and every two-set disjoint from \(e\) value \(1\); also allow value reflection and addition of a common constant. At \(n=11\), add every balanced binary labeling of the \(N\) graph vertices. At \(n\ge12\), precisely these balanced binary labelings (up to additive constants) maximize. For \(n=6\), two further kinds maximize: choose two distinct two-sets \(e,e'\), either intersecting or disjoint, give both value \(0\), give all other two-sets intersecting both value \(2\), and give the rest value \(1\), together with reflections and translations. The resulting size profiles are \((1,8)\) and \((2,4)\), and their reflections. The \(n=5\) Petersen instance is omitted from the novelty claim: its corresponding inradius is already recorded in earlier work.

## Assumptions and scope
The graph is simple, unweighted and connected; \(n\ge6\), the probability law is uniform on vertices, functions are real, and \(\operatorname{Lip}(f)\le1\) means \(|f(e)-f(e')|\le1\) for every graph edge. Constant shifts do not affect the variance. All classifications are exact, including ties. The theorem does not address general \(KG(n,k)\), nonuniform vertex weights, or non-Hilbert target norms.

## Proof
**1. Reduction to integer potentials.** The graph is connected with diameter two for \(n\ge5\): if two two-sets intersect, a third two-set disjoint from both exists. Anchor the value at one vertex to \(0\). The inequalities \(\pm(f(u)-f(v))\le1\) have a totally unimodular node-edge incidence matrix, so every vertex of the anchored Lipschitz polytope is integral. The centered-variance quadratic form is strictly convex on this anchored space. Thus **every** global maximizer is a polytope vertex and hence integral. After translating the minimum to zero, every maximizing potential takes values in \(\{0,1,2\}\).

**2. Two cross-intersecting families.** Let \(\mathcal A\) be the vertices assigned \(0\), let \(\mathcal B\) be those assigned \(2\), and put \(a=|\mathcal A|\), \(b=|\mathcal B|\). They are disjoint, and every two-set in \(\mathcal A\) intersects every two-set in \(\mathcal B\), since disjoint two-sets are adjacent and cannot differ by two. Conversely this cross-intersection condition suffices for a feasible three-level potential. Centering at the intermediate level gives the exact objective
\[
N^2\operatorname{Var}(f)=N(a+b)-(a-b)^2.\tag{1}
\]
When either family is empty, the function is binary-valued; the largest possible numerator is \(B_n\), attained precisely by balanced counts of zeros and ones.

**3. A sharp two-edge cross-intersection bound.** Suppose \(a,b\ge2\). Then
\[
\boxed{a+b\le\max\{n,6\}.}\tag{2}
\]
Indeed, fix \(\mathcal B\). If it contains exactly two incident edges \(\{x,y\},\{x,z\}\), every member of \(\mathcal A\) must either contain \(x\) or equal \(\{y,z\}\). Excluding the two chosen members of \(\mathcal B\) gives \(a\le n-2\) and hence \(a+b\le n\) in the case \(b=2\). If it consists of two disjoint edges, every \(\mathcal A\)-edge must be one of the four cross pairs, hence \(a+b\le6\) for \(b=2\).

If \(b\ge3\) and \(\mathcal B\) contains three edges at a common vertex \(x\), every \(\mathcal A\)-edge must contain \(x\). Since \(a\ge2\), all \(\mathcal B\)-edges also contain \(x\), with at most one exception: when \(\mathcal A\) consists of two \(x\)-edges, their other endpoints may themselves form one extra \(\mathcal B\)-edge. Therefore \(a+b\le n\). If \(\mathcal B\) is pairwise intersecting but contains no three-edge star, it is a triangle; every two-set meeting all three of its edges is one of those triangle edges, forbidden because \(\mathcal A\cap\mathcal B=\varnothing\). Otherwise \(\mathcal B\) contains two disjoint edges. A third edge of \(\mathcal B\) reduces the four possible cross pairs available to \(\mathcal A\) to at most two, so \(a=2\). If the two \(\mathcal A\)-edges intersect, switch the family roles to obtain \(b\le n-2\); if they are disjoint, obtain \(b\le4\). This proves (2). Moreover, \((a,b)=(3,3)\) is impossible when \(a+b=6\): a three-edge star permits total size at most \(n-1\) when both families have three edges, and a nonstar three-edge family permits at most two edges in the other family.

**4. Singleton regime and the small exceptional order.** If \(a=1\), say \(\mathcal A=\{e\}\), then \(\mathcal B\) contains at most the other \(2n-4\) two-sets meeting \(e\). The expression \(N(1+b)-(b-1)^2\) increases strictly for integers \(1\le b<2n-4\), because its forward difference is \(N-2b+1>0\) for \(n\ge5\). Its maximum is exactly \(E_n\), attained only when all these \(2n-4\) neighbors are used. The case \(b=1\) is symmetric.

For \(n=6\), inequality (2) gives \(a+b\le6\) for both family sizes at least two. Equality with sizes \((3,3)\) is impossible as shown; the best remaining profile is \((2,4)\) or \((4,2)\), giving \(6\cdot15-4=86\). These profiles are realized both by two incident two-sets and by two disjoint two-sets, with the other family consisting of all permitted cross-intersecting two-sets. The singleton profile also gives \(E_6=86\). Any smaller total size gives numerator at most \(5\cdot15=75\), and binary labelings give at most \(B_6=56\). This proves the exact exceptional case and all its equality patterns.

For every \(n\ge7\), (2) gives numerator at most \(nN\) when both family sizes are at least two. But
\[
E_n-nN=\frac{n^3-12n^2+43n-50}{2}>0\qquad(n\ge7).
\]
The inequality holds at \(n=7\), where the right-hand side is \(3\), and its derivative as a polynomial is positive thereafter. Thus no two-nonsingleton configuration can maximize, and the only candidates are the singleton pattern of value \(E_n/N^2\) and balanced binary patterns of value \(B_n/N^2\).

**5. Sharp phase switch.** Let \(Q_n=4E_n-N^2\). Direct algebra gives
\[
Q_{n+1}-Q_n=-(n-8)(n^2-4n+8),\qquad Q_{11}=-1.
\]
The differences are strictly negative for \(n\ge9\); direct substitution checks \(Q_n>0\) for \(7\le n\le10\). Since \(B_n=\lfloor N^2/4\rfloor\), one has \(E_{11}=B_{11}\) (both numerator values are \(756\)); for \(n\ge12\), \(E_n<B_n\), while \(7\le n\le10\) has \(E_n>B_n\). This proves the formulas and, by the strict case distinctions and the integrality of every maximizer, the complete equality classification.

## Verification
Run `python3 verify.py` with Python 3. The standalone standard-library program independently enumerates all disjoint cross-intersecting zero/two families for \(n=5,6,7\), optimizing over every possible size of the second family. It checks sharp integer numerators and all equality size profiles, then checks the explicit formulas and phase inequalities for \(7\le n\le999\). These finite checks corroborate, but do not replace, the all-order proof above. The Petersen case \(n=5\) is included only as a known-boundary control and is not claimed as original.

## Relationship to prior work
Addario-Berry, Janson and McDiarmid (first public preprint February 6, 2009) define graph spread, review the integral extremizer principle, determine the complete-graph baseline, and study random graph models; their inspected treatment does not state the Kneser pair-graph formulas or the switch at \(n=11\). Borg (first preprint February 3, 2011) studies sum/product extremal problems for cross-intersecting families, not the disjoint-family, variance-penalized functional in (1). The earlier Petersen symmetric-edge inradius result exactly covers the \(n=5\) special case under Euclidean polarity: this is intentionally excluded from the new theorem. A separate Kneser pair-eigenpolytope ellipsoid calculation concerns a different polytope from the graph symmetric-edge polar. The distinction between titles and actual implication is essential; no unindexed-literature uniqueness is claimed.

## Limitations
The proof uses specific intersections of two-subsets, diameter two, uniform vertex weights and real centered quadratic variance. The theorem does not address general higher-uniformity Kneser graphs, weighted laws or other Lipschitz exponents. A logically equivalent formula may exist in literature not found by the targeted comparisons. Independent external mathematical validation has not been performed.

## References
1. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156 (first version February 6, 2009), https://arxiv.org/abs/0902.1156 .
2. P. Borg, *The maximum sum and maximum product of sizes of cross-intersecting families*, arXiv:1102.0667 (first version February 3, 2011), https://arxiv.org/abs/1102.0667 .
3. *Exact inradius and contact-facet rigidity of the Petersen symmetric edge polytope* (2026), indexed research result; this prior result covers the \(n=5\) instance by polarity.
4. *Parity-controlled John and Löwner ellipsoids of Kneser pair-eigenpolytopes* (2026), indexed research result; different realization and optimization.
