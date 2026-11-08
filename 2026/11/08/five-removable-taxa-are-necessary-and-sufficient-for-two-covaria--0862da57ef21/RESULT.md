# Five removable taxa are necessary and sufficient for two covariance reversals in a rooted food web

## Finding

Consider a finite rooted directed acyclic food web with an undeletable external-energy root, two undeletable focal consumers \(X,Y\), and \(n\) other taxa subject to primary removals. A focal consumer persists exactly when a directed path from the root to it remains after the removals. Choose the surviving set \(S\) uniformly among all \(k\)-element subsets of the \(n\) removable taxa; let \(F_X(S),F_Y(S)\in\{0,1\}\) be the resulting focal persistence indicators. Write
\[
C_k=\operatorname{Cov}(F_X(S),F_Y(S)),\qquad k=0,\ldots,n.
\]
A *strict sign reversal* is a change between positive and negative entries in the sequence of nonzero \(C_k\), in increasing \(k\) order.

**Theorem.** For every such web with \(n\le4\), the covariance sequence has at most one strict sign reversal. A rooted acyclic food web with \(n=5\) has exactly two strict sign reversals, with
\[
(C_0,C_1,C_2,C_3,C_4,C_5)=\left(0,-\frac1{25},\frac1{20},-\frac1{100},0,0\right).
\]
Thus five removable taxa, excluding the root and two monitored consumers, is the smallest possible number for two reversals. The lower bound holds more generally for every pair of coordinatewise increasing Boolean persistence functions, not just food-web reachability functions.

## Assumptions and scope

A directed arc \(u\to v\) means that \(u\) can supply an energy path to \(v\). The undeletable root \(o\) is always present. The two focal consumers \(X,Y\) are evaluated for secondary extinction and are not in the uniform primary-removal pool. No energy fluxes, population abundances, recovery, prey switching, or top-down feedback are modeled. All removable taxa that remain in \(S\) retain their original arcs; a deleted taxon and incident arcs disappear. Path reachability is recomputed after each deletion set. The choice of \(S\) is uniform conditional on its cardinality, not independent Bernoulli removal. Neither focal consumer needs to have a surviving path in the empty set; in the exhibited web both do not.

The count \(n\) is the number of *removable* taxa. Consequently the exhibited directed food web contains seven taxa (five removable, two focal), plus the abstract external root. The theorem does not assert anything about a minimal number of arcs, about nonuniform deletion probabilities, or about real ecological systems.

## Proof

**1. Increasing-function reduction.** Each focal-persistence function \(F(S)\) is coordinatewise increasing: retaining additional taxa cannot destroy an already existing root-to-consumer directed path. Therefore, proving a bound for all increasing Boolean functions on \(n\) coordinates implies the bound for rooted food webs.

For \(n\le3\), only \(n-1\le2\) interior cardinality levels may have nonzero covariance, since the levels \(k=0,n\) are deterministic. Two strict reversals are impossible.

For \(n=4\), a complete finite certificate covers **all** increasing Boolean functions, not a sample of graphs. Encode any function by the 16-bit truth table \(b\in\{0,1\}^{16}\), one bit for every survivor subset of \(\{0,1,2,3\}\). Such a function is increasing exactly when
\[
F(S)\le F(S\cup\{i\})\quad\text{for every }S\subseteq\{0,1,2,3\}\text{ and }i\notin S.
\]
There are exactly 32 such cover relations. Testing all \(2^{16}\) tables yields exactly 168 increasing functions, including both constants. For every ordered pair of these 168 functions, each of the three interior covariance signs is computed by the exact integer numerator
\[
D_k=\binom4k\sum_{|S|=k}F(S)G(S)
-\left(\sum_{|S|=k}F(S)\right)
 \left(\sum_{|S|=k}G(S)\right),\quad k=1,2,3,
\]
with \(C_k=D_k/\binom4k^2\). Exhausting all \(168^2=28{,}224\) ordered pairs finds no three nonzero signs alternating \(+,-,+\) or \(-,+,-\). Because only three interior levels exist, two strict reversals are impossible. The included standalone `check.py` implements this enumeration from first principles, without a precomputed list or an external package; its terminating, exhaustive finite search is the certificate for the four-coordinate case.

**2. The five-taxon witness.** Label the removable taxa \(0,1,2,3,4\). Give the root arcs
\[
o\to0,\quad o\to1,\quad o\to2,
\]
and use precisely the eight further arcs
\[
0\to4,\quad0\to Y,\quad1\to3,\quad2\to4,\quad2\to X,
\quad3\to4,\quad4\to X,\quad4\to Y.
\]
This is an acyclic directed graph in which every removable taxon influences the persistence of at least one focal consumer. If \(s_i=\mathbf1\{i\in S\}\), inspecting all root-to-consumer paths gives the exact Boolean identities
\[
F_X=s_2\lor\bigl(s_4\land(s_0\lor(s_1\land s_3))\bigr),
\qquad
F_Y=s_0\lor\bigl(s_4\land(s_2\lor(s_1\land s_3))\bigr).
\]
The code independently evaluates graph reachability and these formulas on all 32 survivor subsets.

For each survivor count \(k\), let \(N_k=\binom5k\), let \(a_k\) and \(b_k\) count subsets on which \(X\) and \(Y\), respectively, persist, and let \(j_k\) count subsets on which both persist. Complete enumeration gives:

| \(k\) | \(N_k\) | \(a_k\) | \(b_k\) | \(j_k\) | \(N_kj_k-a_kb_k\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 0 | 0 |
| 1 | 5 | 1 | 1 | 0 | -1 |
| 2 | 10 | 5 | 5 | 3 | 5 |
| 3 | 10 | 9 | 9 | 8 | -1 |
| 4 | 5 | 5 | 5 | 5 | 0 |
| 5 | 1 | 1 | 1 | 1 | 0 |

Since \(C_k=(N_kj_k-a_kb_k)/N_k^2\), the claimed covariance values and two sign reversals follow. This completes the proof.

## Verification

Run `python3 check.py` with a standard Python 3 interpreter. The program verifies every graph state against the independently written Boolean formulas; checks the entire exact witness table; constructs all increasing four-variable truth tables by verifying the 32 cover relations; and exhausts every ordered pair of those functions on all three interior cardinality layers. All arithmetic is integer arithmetic. There is no random sampling, numerical approximation, third-party dependency, network call, or unexamined time cutoff.

## Relationship to prior work

Allesina and Bodini (2004) use directed paths from an external root, dominator trees, and single-species removal to understand structural coextinction. The graph and reachability interpretation here follow their model, but the present object is the **conditional covariance of two focal survival indicators as the uniform primary-removal count varies**. Their individual-node influence and dominator statistics do not, as stated, determine the all-count covariance sign sequence.

Allesina and Pascual (2009) analyze ranked sequential removals and total extinction area, not this finite-size all-pairs covariance threshold. In a different, direct bipartite partner-survival setting, the covariance has a one-switch law; the exhibited directed, multi-step web genuinely lies outside that class, because its focal persistence functions contain conjunctions of intermediate species. Generic independent-coordinate positive-correlation inequalities likewise do not imply a sign restriction under fixed-cardinality sampling.

## Limitations

This is a precise finite structural statement, not a population-dynamics model or an empirical ecological prediction. It assumes an undeletable energy root and two undeletable focal species. The four-variable nonexistence result is established by exhaustive transparent computation rather than a short closed-form classification. The construction is not claimed to minimize the number of links or to bound the number of sign reversals in larger webs. Historical priority is provisional: although relevant full-text ecology papers and mathematical searches were compared, analogous fixed-slice monotone-reliability examples could exist elsewhere.

## References

- Allesina, S. and Bodini, A. (2004). “Who dominates whom in the ecosystem? Energy flow bottlenecks and cascading extinctions.” *Journal of Theoretical Biology* 230, 351–358. First publicly available online 17 July 2004. DOI: https://doi.org/10.1016/j.jtbi.2004.05.009 . Author-accessible article: https://www.sccs.swarthmore.edu/users/08/bblonder/phys120/docs/allesina.pdf .
- Allesina, S. and Pascual, M. (2009). “Googling Food Webs: Can an Eigenvector Measure Species' Importance for Coextinctions?” *PLoS Computational Biology* 5, e1000494. https://doi.org/10.1371/journal.pcbi.1000494 . Full text: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000494 .
- Allesina, S., Bodini, A., and Pascual, M. (2009). “Functional links and robustness in food webs.” *Philosophical Transactions of the Royal Society B* 364, 1701–1709. https://doi.org/10.1098/rstb.2008.0214 .
- Colwell, R. K., Dunn, R. R., and Harris, N. C. (2012). “Coextinction and Persistence of Dependent Species in a Changing World.” *Annual Review of Ecology, Evolution, and Systematics* 43, 183–203. https://doi.org/10.1146/annurev-ecolsys-110411-160304 .
