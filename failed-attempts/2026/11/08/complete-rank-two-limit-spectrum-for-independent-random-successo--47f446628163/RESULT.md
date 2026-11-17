# Complete rank-two limit spectrum for independent random successor orders

## Finding

**Theorem.** Fix an integer \(r\ge1\). Independently and uniformly sample \(r\) linear orders of the same labelled \(n\)-point set. Retain only their directed immediate-successor relations \(S_1,\ldots,S_r\), and no order predicates, constants, or additional relations. For every \(i<j\), let \(X^+_{ij}\) count ordered pairs \((u,v)\) satisfying \(S_i(u,v)\land S_j(u,v)\), and let \(X^-_{ij}\) count pairs satisfying \(S_i(u,v)\land S_j(v,u)\). As \(n\to\infty\), all \(N=r(r-1)\) counts converge jointly to mutually independent Poisson random variables of mean one.

Write \(p=1-e^{-1}\), \(q=e^{-1}\), and \(N=r(r-1)\). Among *all* ordinary first-order sentences of quantifier rank at most two in this pure successor language, the set of limiting satisfaction probabilities is **exactly**
\[
\mathcal L_r=\left\{\sum_{k=0}^{N}a_k p^kq^{N-k}:\ a_k\in\{0,1,\ldots,\binom Nk\}\right\}.
\]
These probabilities are distinct for distinct integer coefficient vectors, so
\[
|\mathcal L_r|=\prod_{k=0}^{N}\left(1+\binom Nk\right).
\]
For one successor the only limits are zero and one; for two successors there are exactly twelve distinct limits, and for three successors exactly \(1{,}053{,}696\) limits.

## Assumptions and scope

Fix \(r\) before letting \(n\) tend to infinity; the orders are independently uniform on the \(n!\) total orders. The language is equality together with directed exact-successor predicates \(S_i\) only. The class of sentences includes arbitrary Boolean connectives and ordinary existential/universal quantification but neither counting quantifiers nor extra labels nor accessible underlying order relations. Quantifier rank means maximum nested quantifier depth, including negations and Boolean combinations. All domains are nonempty. The statement is asymptotic for each fixed \(r\); no uniform result for \(r\) growing with \(n\) is asserted.

For each \(i<j\), the sign \(+\) denotes the same orientation in the two paths and \(-\) denotes opposite orientations. Each indicator \(B^s_{ij}=1_{\{X^s_{ij}>0\}}\) is definable at rank two by
\[
\exists x\exists y\,[S_i(x,y)\land S_j(x,y)]\quad(s=+),\qquad
\exists x\exists y\,[S_i(x,y)\land S_j(y,x)]\quad(s=-).
\]

## Proof

**1. Exact probability for forced adjacencies.** Given \(d\) distinct directed arc constraints in one uniform linear order, they are simultaneously achievable precisely when they form a vertex-disjoint union of consistently oriented directed paths (isolated vertices allowed). Contract each required path to a block. The probability is then
\[
\frac{(n-d)!}{n!}=\frac1{(n)_d},
\]
where \((n)_d=n(n-1)\cdots(n-d+1)\). Every contradictory set (including branching or a directed cycle) has probability zero. For a fixed finite number of constraints, a compatible collection has probability \(O(n^{-d})\). Different orders have independent probabilities.

**2. Joint Poisson limit.** Fix nonnegative integers \(k_{ij,s}\), with total \(t=\sum k_{ij,s}\). Expand the mixed factorial moment \(\mathbb E\prod_{i<j,s}(X^s_{ij})_{k_{ij,s}}\) as a sum over \(t\) labelled overlap events. An event specifies one unordered pair of vertices and two colored oriented arc constraints. In the sum, the \(k\) instances in each factorial term must be distinct. If all \(t\) events use disjoint vertex pairs, there are \((n)_{2t}\) oriented choices, and their combined probability is \(\prod_i (n)_{d_i}^{-1}\), where \(\sum_i d_i=2t\). Thus their contribution tends to one.

For any other compatible configuration, let \(e\) be the number of different underlying unordered edges, \(v\) the number of vertices appearing, and \(a\) the number of distinct required colored oriented arcs. Every edge needs at least two colored arcs. If two event instances use the same unordered edge, their distinct event labels require at least three different colored arcs: two copies of the same labelled event cannot occur in one factorial term, and incompatible opposite directions in one color are impossible in a directed path. Thus either some underlying edges share a vertex, giving \(v\le2e-1\le a-1\), or an edge carries at least three colors, giving \(v\le2e\le a-1\). For each fixed intersection pattern there are \(O(n^v)\) assignments and probability \(O(n^{-a})\). There are finitely many patterns for fixed \(r,t\), so their total is \(O(n^{-1})\). All mixed factorial moments therefore converge to one, the mixed factorial moments of independent Poisson-one variables. Their joint moment-generating function exists near zero, so factorial-moment convergence implies joint distributional convergence.

**3. The clean high-probability regime.** The \(2r\) ordered path endpoints are distinct with probability tending to one. With probability tending to one, no vertex meets two different overlap edges, no overlap edge touches an endpoint, and no unordered edge is used by three or more successor relations. Each forbidden pattern has an \(O(n^{-1})\) expected count: distinct endpoint collisions cost one extra vertex identification; overlap edges meeting have \(v<a\) as in Step 2; an overlap edge at an endpoint similarly adds an independent endpoint restriction, and three-color edges cost a third arc constraint. The overlap counts remain tight by Step 2. Consequently with probability tending to one all overlap edges are isolated, disjoint from endpoints, and the remaining vertices include ordinary vertices. Furthermore every vertex has a nonneighbor for all colors once \(n>2r+2\), because at most \(2r\) other vertices meet its successor ports.

**4. Two-round logical normal form.** For distinct points \(x,y\), define the *mask* \(M(x,y)\) as the subset of \(\{1^+,1^-,\ldots,r^+,r^-\}\) marking exactly which \(S_i(x,y)\) and \(S_i(y,x)\) hold. The diagonal \(y=x\) is always its own fixed quantifier-free type: all successor relations are irreflexive. Thus the quantifier-rank-one type of \(x\) is completely determined by the set \(T(x)=\{M(x,y):y\ne x\}\), not the multiplicities of these masks. Indeed each rank-one unary formula is a Boolean combination of quantifier-free unary facts and statements \(\exists y\,\psi(x,y)\) with \(\psi\) quantifier-free. Consequently any closed rank-at-most-two formula is determined by the *set* of realized sets \(T(x)\), because it is a Boolean combination of existence assertions about rank-one unary types.

In the clean regime the possibilities for \(T(x)\) can be read off completely. A generic vertex has the empty mask and all \(2r\) singleton masks. The first or last point of a color is missing exactly that color's predecessor or successor singleton mask, and otherwise has every singleton and the empty mask. An endpoint of an overlap edge of type \((i,j,+)\) has one doubleton mask \(\{i^+,j^+\}\) or \(\{i^-,j^-\}\) in place of those two singletons; type \((i,j,-)\) gives \(\{i^+,j^-\}\) or \(\{i^-,j^+\}\). All other singleton masks and the empty mask occur. Each one of these local types is present exactly when its corresponding overlap type occurs, apart from the generic and endpoint types, which occur with probability tending to one.

Hence, on a probability-one-asymptotic event, the rank-two theory of the whole structure depends **only** on the \(N\) support bits \(B^s_{ij}\). Step 2 shows that these bits converge jointly to independent Bernoulli variables with success probability \(p=1-e^{-1}\).

**5. Exact spectrum and sharp distinctness.** Every Boolean function of the support bits is the truth function of a rank-two sentence: take Boolean combinations of the explicit rank-two witnesses in the assumptions. Conversely Step 4 shows that every rank-two sentence agrees with one of these Boolean functions with probability tending to one. A Boolean function that selects exactly \(a_k\) of the \(\binom Nk\) bit vectors containing \(k\) successes has limiting probability \(\sum_k a_k p^kq^{N-k}\). This proves that the displayed set is exact, including attainability.

Finally, \(q=e^{-1}\) is transcendental and the degree-\(N\) Bernstein polynomials \((1-q)^kq^{N-k}\) for \(k=0,\ldots,N\) are linearly independent over \(\mathbb Q\). Thus no two different integer coefficient vectors evaluate to the same real number. Counting coefficient choices gives the claimed product formula.

## Verification

`checker.py` exhaustively fixes the first of two orders as the identity and enumerates every second order on labelled sets of sizes three through seven. It constructs directed-adjacency masks, the sets of realized unary rank-one types, the positive and negative overlap counts, and the support bits. On clean instances it checks that identical support bits imply identical rank-two signatures. It checks the exact two-color expectation identity \(\mathbb E X^+=\mathbb E X^-=(n-1)/n\). The checker is a finite diagnostic; the infinite theorem follows from Steps 1–5. Reproduce with `python3 checker.py`.

## Relationship to prior work

Michaliszyn and Witkowski (2026), and Jeż, Michaliszyn and Witkowski (2026), study satisfiability for multiple exact successor predicates, including the significance of overlapping and oppositely directed edges, but do not provide the uniform-random-model rank-two probability spectrum. Bender and Canfield (1999) prove Poisson behavior for sparse graph intersections. Diaconis, Evans and Graham (2013) give an exact fixed-point-law correspondence for a **single same-direction adjacency count** of two random orders, directly subsuming that one marginal. Xu, Alain and Sankoff (2008) study Poisson shared-adjacency counts in genome comparisons. None of these inspected results states the full all-pairs, both-orientations independent limit together with the rank-two logical-spectrum classification. The coincidence-count part is related to existing Poisson approximation theory and is not independently claimed as a wholly new phenomenon.

## Limitations

The claim is restricted to fixed \(r\), ordinary quantifier rank at most two, pure directed successor predicates, and independently uniform full linear orders. It says nothing about quantifier rank three or higher, logic with counting or additional predicates, visible linear orders, nonuniform order laws, growing \(r\), or quantitative total-variation bounds. The cited primary literature is not an exhaustive historical-priority audit: an equivalent general sparse-motif or restricted-logic formulation might exist. The proof and finite checker are self-reviewed; independent validation has not been performed.

## References

1. Jakub Michaliszyn and Piotr Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758v1 (public October 7, 2026), https://arxiv.org/abs/2610.09758.
2. Artur Jeż, Jakub Michaliszyn and Piotr Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943v1 (public October 14, 2026), https://arxiv.org/abs/2610.19943.
3. Edward A. Bender and E. Rodney Canfield, *Intersections of Randomly Embedded Sparse Graphs are Poisson*, 1999, https://doi.org/10.37236/1468.
4. Persi Diaconis, Steven N. Evans and Ron Graham, *Unseparated Pairs and Fixed Points in Random Permutations*, Berkeley Technical Report 822 (2013), https://statistics.berkeley.edu/tech-reports/822.
5. Y. Xu, A. Alain and D. Sankoff, *Poisson adjacency distributions in genome comparison*, *Bioinformatics* (2008), https://doi.org/10.1093/bioinformatics/btn295.
