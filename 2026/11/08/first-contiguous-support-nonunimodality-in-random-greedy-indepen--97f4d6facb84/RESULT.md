# First contiguous-support nonunimodality in random greedy independent sets on trees

## Finding

**Theorem.** For every integer \(1\le n\le5\) and every simple, unweighted tree \(T\) on \(n\) vertices, if the support of its random greedy maximal-independent-set cardinality \(X_T\) is an integer interval, then its probability mass function is unimodal. At \(n=6\), exactly one unlabelled tree violates this implication: the spider \(S(1,1,3)\), whose three arms have edge lengths \(1,1,3\). It has
\[
\Pr(X_T=2)=\frac{19}{72},\quad
\Pr(X_T=3)=\frac{16}{72},\quad
\Pr(X_T=4)=\frac{37}{72},
\qquad
\mathbb E[z^{X_T}]=\frac{z^2(19+16z+37z^2)}{72}.
\]
These are all its possible sizes, and \(19>16<37\) is a strict interior valley. Exactly \(360\) of the \(6^4=1296\) labeled six-vertex trees are exceptional.

## Assumptions and scope

All trees are finite, connected, simple, and unweighted. Independently of the graph, sample one of the \(n!\) permutations of its vertices uniformly. Inspect vertices in that order; accept a vertex precisely if none of its neighbors has previously been accepted. The terminal accepted set is a maximal independent set and \(X_T\) is its cardinality. We call its law *gap-free* if \(\{k:\Pr(X_T=k)>0\}\) is an interval of integers. A finite probability sequence on its support is *unimodal* if there exists a mode with all terms weakly increasing before it and weakly decreasing after it. We make no general unimodality claim for distributions whose support contains gaps: a star gives a trivial support-gap obstruction. Spider notation \(S(a,b,c)\) denotes one branching vertex joined to three leaves by internally disjoint paths of \(a,b,c\) edges.

## Proof

**Exact recursion.** Write \(F_G(z)=\mathbb E[z^{X_G}]\), with the greedy process defined on any forest and \(F_{\varnothing}(z)=1\). The first vertex in a uniform random permutation is uniform on \(V(G)\), and accepting it deletes its closed neighborhood. The remaining relative vertex order is uniform. Thus for every nonempty graph,
\[
F_G(z)=\frac{z}{|V(G)|}\sum_{v\in V(G)}F_{G-N[v]}(z).
\]
This is a finite exact rational recurrence, and when \(G\) is a disjoint union the output sizes of its components under the induced uniform relative orders are independent, giving a product of their generating polynomials.

**The six-vertex witness.** Label the central degree-three vertex \(c\), its two pendant neighbors \(a,b\), and its length-three arm \(c-d-e-f\). Conditioning on the first selected vertex yields these conditional size laws:

| First vertex | Conditional distribution of \(X_T\) |
|---|---|
| \(c\) | \(\Pr(X_T=2)=1\) |
| \(d\) | \(\Pr(X_T=4)=1\) |
| Either \(a\) or \(b\) | \(\Pr(X_T=3)=1/3\), \(\Pr(X_T=4)=2/3\) |
| \(e\) | \(\Pr(X_T=2)=1/3\), \(\Pr(X_T=3)=2/3\) |
| \(f\) | \(\Pr(X_T=2)=1/4\), \(\Pr(X_T=4)=3/4\) |

Each row follows immediately from the closed-neighborhood deletion recursion: the residual graph is a path, isolated vertices, or a star. Averaging the six equally likely first vertices gives the displayed distribution. Because all three probabilities are positive, the support is the full interval \(\{2,3,4\}\), so the strict interior valley disproves unimodality without relying on support gaps. It also violates log-concavity since \(16^2<19\cdot37\).

**Sharp lower bound and uniqueness.** The attached executable `check.py` is a complete finite enumeration certificate, not sampling. For each \(n\in\{1,\ldots,6\}\), it generates every labeled tree, using the Prüfer bijection for \(n\ge2\), and evaluates all \(n!\) vertex orderings by direct greedy simulation with integer bitmasks. For each probability mass vector it checks gap-free support and the defining mode inequalities. These are exhaustive integer computations, not floating-point or extrapolated checks. The exact outputs are:

| Number of vertices \(n\) | Labeled trees checked | Gap-free, nonunimodal trees |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 1 | 0 |
| 3 | 3 | 0 |
| 4 | 16 | 0 |
| 5 | 125 | 0 |
| 6 | 1296 | 360 |

For each of the \(360\) exceptions, the checker verifies both its arm-length shape \(S(1,1,3)\) and its exact unnormalized order counts \((190,160,370)\) at cardinalities \((2,3,4)\); it rejects any other exceptional shape. Conversely this spider has precisely two interchangeable one-edge arms, hence automorphism group order \(2\), and exactly \(6!/2=360\) labelings. The Prüfer bijection proves exhaustive coverage of all possible six-vertex trees; the complete permutation enumeration proves the reported probabilities exactly. This establishes both lower bound and uniqueness.

## Verification

Run `python3 check.py` using only the Python standard library. Its final line must be `CERTIFICATE PASSED`. The standalone checker generates every tree directly from Prüfer words and every vertex order directly from permutations. It tests the support and all possible unimodal modes, checks each exceptional six-vertex tree's exact shape and all \(720\) order outcomes, and checks the canonical witness separately. In particular its finite domain includes all \(1296\) labeled six-vertex trees and no graph database is required. A second calculation using the displayed first-vertex recurrence independently gives the same exact witness fractions. The certificate proves only the finite cutoff stated here.

## Relationship to prior work

Krivelevich, Mészáros, Michaeli, and Shikhelman (arXiv:1907.07216) define this same random-order greedy independent-set process and prove an extremal *expectation* theorem for trees; their inspected Sections 1, 8 and 9 do not state a fixed-tree support-unimodality classification. Contat (arXiv:2103.03800) finds the *unconditional law averaged over a uniformly random Cayley tree*, not the law conditional on one fixed six-vertex shape. Krapivsky (arXiv:2009.08609) studies occupation-number counting statistics on a *one-dimensional interval*, not the branched six-vertex tree. The ordinary independence polynomial counts all independent sets by size, not probability weights of terminal sets produced by greedy random permutations. Thus known independence-polynomial unimodality questions do not imply this result. Research-record searches for the exact shape, equivalent random sequential adsorption terminology, probability laws, and sharp unimodality cutoffs found no matching theorem; this does not certify historical priority.

## Limitations

The theorem classifies only trees of at most six vertices. It gives no claim for larger trees, general graphs, weighted arrival orders, or other adsorption models. It does not assert nonunimodality without the gap-free condition (which is essential to remove trivial support gaps). The originality assessment is conditional on the literature actually inspected; an unlocated earlier exact enumeration could overlap. Independent audit has not been performed.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216, first public 2019-07-16. https://arxiv.org/html/1907.07216v6
2. A. Contat, *Surprising identities for the greedy independent set on Cayley trees*, arXiv:2103.03800, first public 2021-03-05. https://arxiv.org/html/2103.03800v3
3. P. L. Krapivsky, *Large Deviations in One-Dimensional Random Sequential Adsorption*, arXiv:2009.08609, first public 2020-09-18. https://arxiv.org/html/2009.08609v2
