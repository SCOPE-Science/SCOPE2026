# Scientific review

## Correctness — PASS

The probabilistic model is defined by independent retention of each edge. On a tree, the unique path yields \(M_v(p)=1+\sum_j a_v(j)p^j\); this determines all coefficients. Difference polynomials vanish at both endpoints, and the cumulative-distance-profile expression proves the factorization by \(p(1-p)\). The finite proof enumerates all labelled trees of every size up to seven by Prüfer codes, deduplicates via rooted-tree canonical strings, and tests every unordered pair with exact rational Sturm chains, including one-sided endpoint signs and square-free reduction. It finds no interior roots for sizes two through six and exactly three representative source pairs, in two marked-edge orbits, at seven. Independent formulas for both witnesses and edge-pattern enumeration reproduce the differences and crossings. A separate NetworkX/SymPy census agrees on all reversal counts. The exact finite bound is not extrapolated to higher orders.

## Originality — PASS within inspected literature, with priority risk

The key literature is Gordon and Jager (2009/2010), whose Lemma 2.4 **already proves** that adjacent tree vertices may have *any prescribed integral endpoint-vanishing difference polynomial*. Therefore the qualitative existence of crossing roots and even arbitrarily many roots is known, not claimed as original. Their Proposition 2.5 also extends crossings to globally top-ranked nodes in substantially larger trees. The final claim concerns instead the *sharp minimum order seven* and the *complete classification of marked pairs at that minimum*. Neither statement follows numerically or structurally from their unspecified-size existence theorem or from Eisenstat–Gordon–Redlich (2008), which studies polynomial properties and reconstruction. The present seven-vertex census and two exact crossover laws supply the new finite answer. Searches for the minimum order, equivalent root-expected-reliability formulation and exact small-tree tables found no matching published statement in inspected material. Nonetheless an older relevant paper, Aivaliotis–Gordon–Graveman (2002), was not accessible in full; human priority review remains necessary. A failed search is not treated as proof of novelty.

## Value — PASS

Choosing a source/initial case and interpreting its expected affected population are natural tasks in an independent-transmission network. Transmissibility-independent source rankings are valid on trees of order at most six, but fail already on two distinct seven-node branching geometries. The minimum order and complete configurations distinguish local degree (weak transmission) from more distant reach (strong transmission), giving a sharp, interpretable limit to a common degree-based comparison. The exact two-class classification is a meaningful finite structural boundary, not an arbitrarily selected instance. It neither requires nor claims a larger theoretical framework.

## Closest literature and limits

Eisenstat–Gordon–Redlich (2008), DOI 10.1137/06065951X, gives the exact expected-rank setting and distance formula. Gordon–Jager (2009/2010), DOI 10.1002/net.20363, proves a much broader unrestricted existence theorem, but no exact minimal-order classification; that strong prior is directly incorporated into the novelty assessment. Bucur–Holme (2020), DOI 10.1371/journal.pcbi.1008052, studies epidemic influence at the source under a distinct continuous-time model. Aivaliotis–Gordon–Graveman (2002), DOI 10.1002/jgt.1004, is a plausible inaccessible priority risk. The computational census covers only trees of order at most seven; all mean comparisons are pairwise, not global source optimality.

Self-review: passed. Independent audit: not yet performed.
