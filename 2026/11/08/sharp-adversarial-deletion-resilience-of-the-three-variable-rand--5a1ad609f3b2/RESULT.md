# Sharp adversarial-deletion resilience of the three-variable random-graph theory in Kneser graphs

## Finding

Let \(r\ge2\), \(n\ge3r\), and let \(G=\mathrm{KG}(n,r)\) have the \(r\)-subsets of an \(n\)-set as vertices, adjacent exactly when disjoint. Write \(\binom{a}{b}=0\) if \(a<b\), and set
\[
J=\binom{n-2r}{r},\qquad M=\binom{n-r-1}{r-1},\qquad Z=\binom nr-2\binom{n-r}{r}+\binom{n-2r}{r},\qquad m=\min\{J,M,Z\}.
\]
For every set \(S\) of at most \(m-1\) vertices, the induced subgraph \(G-S\) is 2-existentially closed. In fact it satisfies **exactly the same counting-free first-order sentences using at most three reusable variables, at unrestricted quantifier depth**, as the countable random graph. This bound is sharp: there is a set of exactly \(m\) vertices whose deletion destroys 2-existential closure and separates the resulting graph by a three-variable sentence. Equivalently, the minimum number of vertices whose deletion destroys the 2-extension property is exactly \(m\).

The three candidates \(J,M,Z\) are genuine competing witness bottlenecks: common neighbors of disjoint vertices, asymmetric adjacency for maximally overlapping vertices, and common nonneighbors of disjoint vertices. In particular, for \(r=2\) the sharp deletion count is \(1\) at \(n=6\), \(3\) at \(n=7\), and \(4\) for every \(n\ge8\). For fixed \(r\), as \(n\to\infty\), the common-nonneighbor obstruction eventually wins and
\[
m\sim \frac{r^2}{(r-2)!}n^{r-2}.
\]

## Assumptions and scope

All graphs are undirected simple graphs in the pure adjacency/equality language, with no counting quantifiers. The base parameters satisfy \(r\ge2\) and \(n\ge3r\). Two-existential closure means: for every ordered pair of distinct vertices and every one of the four prescribed adjacency/nonadjacency patterns, a *third, distinct* vertex realizes the pattern. A deletion removes whole graph vertices, i.e., members of the family of \(r\)-subsets, not ground-set elements. The random graph is the countable graph with the finite extension property. For \(2r\le n<3r\), the undeleted Kneser graph itself fails the two-extension property because a disjoint pair has no common neighbor.

## Proof

**Exact four-pattern witness counts.** Fix distinct \(r\)-sets \(A,B\) and write \(s=|A\cap B|\), where \(0\le s\le r-1\). For a third distinct \(r\)-set \(X\), adjacency to \(A\) is disjointness from \(A\). The number \(N_{11}(s)\) adjacent to both is
\[
N_{11}(s)=\binom{n-2r+s}{r}.
\]
The number adjacent to \(A\) but not \(B\) is
\[
N_{10}(s)=\binom{n-r}{r}-\binom{n-2r+s}{r}-\mathbf{1}_{s=0}.
\]
The last subtraction removes \(X=B\) precisely when \(A,B\) are disjoint. By symmetry \(N_{01}(s)=N_{10}(s)\). Inclusion-exclusion gives the number adjacent to neither:
\[
N_{00}(s)=\binom nr-2\binom{n-r}{r}+\binom{n-2r+s}{r}-2\mathbf{1}_{s\ge1}.
\]
Here the final subtraction removes \(X=A\) and \(X=B\) precisely when \(A,B\) overlap.

**Optimization over intersection size.** The first expression is nondecreasing in \(s\), and attains minimum \(J\) at \(s=0\). For \(s\ge1\), the second is decreasing in \(s\), attaining \(M=\binom{n-r-1}{r-1}\) at \(s=r-1\). Its value at \(s=0\) exceeds or equals \(M\), since their difference is
\[
\binom{n-r-1}{r}-\binom{n-2r}{r}-1>0
\]
for \(n\ge3r\), \(r\ge2\). The fourth expression increases among \(s\ge1\). Its first value minus the value at \(s=0\) is \(\binom{n-2r}{r-1}-2\ge0\), because \(n-2r\ge r\ge2\). Thus the minimum of \(N_{00}\) is \(Z\) at \(s=0\). All three minimizing overlap configurations exist. Therefore the least witness count across all pairs and patterns is exactly \(m\).

**Positivity and exact resilience.** We have \(J\ge1\), \(M\ge1\), and \(Z>0\). For the last inequality choose one element of each disjoint anchor and supplement with \(r-2\) elements outside their union; the resulting \(r\)-set is distinct from either anchor and meets both. If fewer than \(m\) graph vertices are deleted, every remaining pair retains at least one witness for every pattern. Conversely, choose a pair and a pattern realizing the global minimum; deleting exactly its \(m\) witness vertices leaves the two anchors and eliminates that pattern. Hence \(m-1\) is the largest universal deletion radius.

**Unlimited-depth three-variable equivalence and sharp distinction.** In the usual three-pebble game, when Spoiler moves a pebble, at most two other pebbles remain. Duplicator matches equality when Spoiler reuses an occupied vertex, and otherwise invokes the two-extension property to choose a fresh vertex satisfying the requisite adjacency/nonadjacency requirements to these one or two occupied vertices. When fewer than two remain, introduce an arbitrary auxiliary anchor and use the two-extension property; all structures under discussion have ample vertices. Thus Duplicator wins indefinitely between any two 2-existentially closed graphs. The countable random graph has this property, so \(G-S\) agrees with it on all three-variable sentences. Conversely, loss of one two-point pattern falsifies a sentence
\[
\forall x\,\forall y\,\bigl(x\ne y\ \longrightarrow\ \exists z\,(z\ne x\land z\ne y\land \eta_1(z,x)\land\eta_2(z,y))\bigr),
\]
where each \(\eta_i\) is either adjacency or nonadjacency. This sentence has three variables and is true in every 2-existentially closed graph. Consequently the deletion threshold is also sharp for preserving this three-variable theory.

**Two structural consequences.** For \(r=2\), the candidate counts simplify to \(J=\binom{n-4}{2}\), \(M=n-3\), and \(Z=4\), giving the stated three-branch exact threshold. For fixed \(r\), the three counts have growth orders \(n^r\), \(n^{r-1}\), and \(n^{r-2}\), respectively. Counting \(r\)-sets meeting each of two disjoint \(r\)-sets first in one point gives \(Z\sim r^2n^{r-2}/(r-2)!\); hence \(Z\) eventually controls the minimum.

## Verification

A standalone exhaustive checker is included as `check.py`. It enumerates every pair of distinct Kneser vertices and all four extension patterns for \(r=2\), \(6\le n\le11\), and \(r=3\), \(9\le n\le11\). All nine exhaustive parameter cases agree with the three closed formulas; there are no discrepancies. It also checks formula positivity and asymptotic bottleneck domination for several finite test ranges. Run `python check.py`; the exact expected output is embedded in `check_output.txt`. Finite checks corroborate the theorem; the proof above establishes the full quantified statement.

## Relationship to prior work

Forbes, Grannell and Griggs (2005) investigate 2- and 3-existential closure for block-intersection graphs of Steiner triple systems. Their vertex sets consist of selected triple blocks, with adjacency **intersection**, not the full family of all \(r\)-subsets with adjacency **disjointness**. Their general existence results do not give the three competing minimum witness counts for Kneser graphs or this sharp universal vertex-deletion radius. McKay and Pike (2007) extend the intersection-graph inquiry to balanced incomplete block designs, again with different underlying vertex families. Grohe and Schweikardt (2005) provide finite-variable logical context, not this Kneser-specific resilience invariant. Related research on two-extension thresholds for stable Kneser subgraphs likewise does not imply the present formula: restricting the allowable subsets changes all four witness counts. The connection with three-variable equivalence uses the standard pebble-game argument; originality is claimed for the exact robust combinatorial classification, not for that general logical implication.

## Limitations

The result is specific to ordinary Kneser disjointness graphs, deletion of graph vertices, and the two-extension (hence counting-free three-variable) theory. It does not establish full first-order equivalence, counting-logic equivalence, robustness after ground-set deletions, or the corresponding formula for stable Kneser graphs. The exact formula is an elementary inclusion-exclusion classification, not a claimed solution to a wider open Kneser problem. A more general unpublished or unidentified witness-count theorem might subsume it; historical priority remains provisional.

## References

1. A. D. Forbes, M. J. Grannell and T. S. Griggs, *Steiner Triple Systems and Existentially Closed Graphs*, Electronic Journal of Combinatorics 12 (2005), R42; published 2005-08-30. DOI: https://doi.org/10.37236/1939.
2. B. D. McKay and D. A. Pike, *Existentially Closed BIBD Block-Intersection Graphs* (2007). Open PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v14i1r70/pdf/. (The accessible PDF was inspected in part.)
3. M. Grohe and N. Schweikardt, *The Succinctness of First-Order Logic on Linear Orders*, arXiv:cs/0502047, 2005-02-09. https://arxiv.org/abs/cs/0502047. Finite-variable background only.
4. A. C. Burgess, R. D. Luther and D. A. Pike, *Existential Closure in Line Graphs*, arXiv:2211.01168 (2022), https://arxiv.org/abs/2211.01168. Abstract inspected; this potentially relevant complementary line-graph direction was not resolved through full-text comparison.
