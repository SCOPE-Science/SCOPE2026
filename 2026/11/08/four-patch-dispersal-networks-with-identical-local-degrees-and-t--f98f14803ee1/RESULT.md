# Four-patch dispersal networks with identical local degrees and three distinct invasion thresholds

## Finding

For directed, loopless, unweighted, strongly connected patch networks, the least number of patches permitting two networks with the **same in-degree and out-degree at each corresponding patch** but different adjacency Perron roots is four. Four patches and five directed dispersal routes are simultaneously sufficient and, among strongly connected four-patch networks, the smallest possible route budget for such a discrepancy.

More precisely, fix patch labels \(0,1,2,3\) and the ordered local profiles \((d_i^-,d_i^+)=(1,2),(2,1),(1,1),(1,1)\), respectively. Exactly five strongly connected graphs satisfy these profiles, and their spectral radii take **exactly three** distinct values:
\[
\alpha,\quad 2^{1/3},\quad \sqrt{\frac{1+\sqrt5}{2}},
\]
where \(\alpha>1\) is the unique positive root of \(t^4-t-1=0\). These values are strictly increasing. Their characteristic polynomials are respectively \(t^4-t-1\), \(t(t^3-2)\), and \(t^4-t^2-1\), attained by two, one, and two labeled realizations with this fixed profile.

Crucially, the lowest and middle cases both have **no reciprocated dispersal routes**. Thus even the full patchwise in/out-degree information *together with zero reciprocity* does not determine the linear colonization threshold. For the concrete extinction-to-colonization ratio \(\mu/\lambda=5/4\), the lowest-root network has a linearly stable all-vacant state while the middle-root network, despite also having zero reciprocal arcs, has an unstable one.

## Assumptions and scope

All graphs here are finite simple digraphs: no loops or parallel routes; a directed arc \(i\to j\) represents colonization from patch \(i\) to patch \(j\). A graph is strongly connected when every ordered pair is joined by a directed path. Its adjacency matrix is \(A_{ij}=1\) when \(i\to j\), and zero otherwise. Write \(\rho(A)\) for its spectral radius.

For the continuous-time homogeneous patch-occupancy mean-field model, let \(x_i\in[0,1]\), local extinction rate \(\mu>0\), and per-arc colonization coefficient \(\lambda>0\):
\[
\dot x_i=-\mu x_i+\lambda(1-x_i)\sum_{j:j\to i}x_j.
\]
This is a deterministic mean-field model, not an assertion about almost-sure indefinite survival of a finite-state stochastic process. The all-vacant equilibrium has Jacobian \(J=-\mu I+\lambda A^\mathsf T\). Since \(A\) is irreducible and nonnegative, this equilibrium is linearly asymptotically stable for \(\lambda\rho(A)<\mu\), and linearly unstable for \(\lambda\rho(A)>\mu\). The equality case is intentionally excluded.

## Proof

**1. The complete five-route class.** Fix the stated ordered degrees. A direct finite classification of loopless five-arc sets, by requiring one incoming and two outgoing arcs at patch \(0\), two incoming and one outgoing at patch \(1\), and one of each at patches \(2,3\), yields seven edge sets. Two are not strongly connected. The five strongly connected sets are, with \(ij\) abbreviating \(i\to j\):

| Arcs | Characteristic polynomial |
| --- | --- |
| \(01,02,10,23,31\) | \(t^4-t^2-1\) |
| \(01,02,13,21,30\) | \(t^4-t-1\) |
| \(01,03,10,21,32\) | \(t^4-t^2-1\) |
| \(01,03,12,20,31\) | \(t^4-t-1\) |
| \(02,03,10,21,31\) | \(t(t^3-2)\) |

The list is exhaustive: the attached program iterates all \(\binom{12}{5}=792\) subsets of possible loopless directed arcs and applies the explicit ordered in/out constraints and a reachability test. The five displayed polynomials also follow directly from \(\det(tI-A)\); the program computes each twice, by the Leibniz determinant and by Newton's trace identities, using exact integer/rational arithmetic. The two graphs with polynomial \(t^4-t-1\) and the unique graph with polynomial \(t(t^3-2)\) have no pair of oppositely directed arcs, as may be checked in the displayed lists.

**2. Ordering of the Perron roots.** Strong connectivity makes each adjacency matrix irreducible; its Perron eigenvalue is the positive spectral radius. The polynomial \(t^4-t-1\) is strictly increasing for \(t\ge1\), negative at \(1\), and positive at \(2^{1/3}\), because \((2^{1/3})^4-2^{1/3}-1=2^{1/3}-1>0\). Hence \(\alpha<2^{1/3}\). Let \(\varphi=(1+\sqrt5)/2\). Then \(\varphi^3=2+\sqrt5>4\), so \(\sqrt\varphi>2^{1/3}\). This establishes three strict thresholds.

**3. Sharpness in patch count and route budget.** A strongly connected, loopless graph on \(n\) patches has at least \(n\) arcs. If it has exactly \(n\) arcs, each patch has in-degree and out-degree one, and strong connectivity forces a directed \(n\)-cycle; its Perron root is one. In particular four patches and at most four arcs cannot exhibit a discrepancy. For \(n=1\), there is only one loopless graph and hence no possible pair. For \(n=2\) the only strongly connected graph is the reciprocal pair. For \(n=3\), classification by the sorted multiset of \((d_i^-,d_i^+)\) gives the following exhaustive possibilities and characteristic polynomials:

| Degree multiset | Characteristic polynomial |
| --- | --- |
| \((1,1),(1,1),(1,1)\) | \(t^3-1\) |
| \((1,1),(1,1),(2,2)\) | \(t(t^2-2)\) |
| \((1,1),(1,2),(2,1)\) | \(t^3-t-1\) |
| \((1,2),(2,1),(2,2)\) | \((t+1)(t^2-t-1)\) |
| \((2,2),(2,2),(2,2)\) | \((t-2)(t+1)^2\) |

All five rows are forced by the degree multiset; an exhaustive exact check independently visits all \(2^6=64\) possible three-patch digraphs, of which 18 are strongly connected. Therefore no two smaller strongly connected networks with the same patchwise bidegrees have different Perron roots.

**4. Ecological interpretation.** The displayed local-occupancy system has extinction Jacobian \(-\mu I+\lambda A^\mathsf T\), and the Perron eigenvalue of \(A\) is real and dominates the real parts of all other adjacency eigenvalues. Its stability boundary is therefore \(\lambda/\mu=1/\rho(A)\). The three five-route realizations admit three distinct such boundaries, with the low and middle cases indistinguishable by patchwise degrees or reciprocity alone. For the rational parameter \(\mu/\lambda=5/4\), \(\alpha<5/4<2^{1/3}\): indeed \((5/4)^4-(5/4)-1=49/256>0\) and \((5/4)^3=125/64<2\). Thus the lowest-root graph has stable extinction and the no-reciprocity middle-root graph has unstable extinction at the very same demographic parameters.

## Verification

Run `python3 check.py` using a standard Python 3 installation. The program enumerates all simple directed graphs on two and three vertices, all five-route four-vertex graphs with the stated labeled degrees, and checks their characteristic polynomials via two finite exact constructions. The expected final line is `CHECK_OK`. No numerical root finding is used for the theorem or strict ordering. The finite classification is exhaustive over the precisely stated finite search space, not over larger patch networks.

## Relationship to prior work

Shtilerman and Stone (2015) develop a directed dispersal model with a spectral-radius criterion and examine in/out-degree correlation and reciprocal-link symmetry, primarily as predictors in large networks. The present result does not dispute their statistical findings or general spectral criterion. It supplies the sharp small-network boundary and full five-arc realization classification showing that the degree information and reciprocity they study do not make that threshold an exact graph invariant. Their paper's available indexed scientific passages concerning its models, simulation designs, and asymptotic approximation were inspected; whole-document textual comparison was limited by access restrictions.

Kwapisz (1996) studies general degree-based bounds on the spectral radius of a directed graph, rather than the present finite exact threshold classification. Bıyıkoğlu and Leydold (2008) study largest spectral radii under degree constraints for *undirected* connected graphs, which does not imply the directed fixed-bidegree result here. These are methodological precedents, not claims of a proof of historical uniqueness.

## Limitations

The claim concerns uniform unweighted directed arcs and the local stability of the deterministic extinction equilibrium, not random outbreak sizes, exact finite-state extinction times, global stability, empirical ecosystem prognosis, or heterogeneous dispersal rates. The count of five and the three polynomial classes is restricted to the specified labeled four-patch bidegree profile; no classification is asserted for all larger digraphs. The historical-priority search was bounded, and inaccessible complete texts or unindexed small-graph tables could contain an earlier equivalent classification. Independent scientific validation has not been performed.

## References

1. E. Shtilerman and L. Stone, *The effects of connectivity on metapopulation persistence: network symmetry and degree correlations*, Proceedings of the Royal Society B 282 (2015), 20150203. DOI: https://doi.org/10.1098/rspb.2015.0203. First public journal date 2015-05-07.
2. J. Kwapisz, *On the spectral radius of a directed graph*, Journal of Graph Theory 23 (1996), 405–411. DOI: https://doi.org/10.1002/(SICI)1097-0118(199612)23:4%3C405::AID-JGT9%3E3.0.CO;2-V.
3. T. Bıyıkoğlu and J. Leydold, *Graphs with Given Degree Sequence and Maximal Spectral Radius*, Electronic Journal of Combinatorics 15 (2008), R119. https://doi.org/10.37236/843.
