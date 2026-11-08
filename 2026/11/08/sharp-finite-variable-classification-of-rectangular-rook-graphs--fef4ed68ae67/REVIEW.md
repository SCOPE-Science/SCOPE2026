# Scientific review: rectangular rook graphs

## Correctness

**PASS.** The defining objects and language are fixed: finite simple rook graphs on boards with both sides at least two, counting-free adjacency logic, unrestricted quantifier depth. A permanent coordinatewise partial-bijection strategy works when truncated side sizes agree: after one pebble is removed at most \(k-1\) coordinate values remain used, so a fresh value is always available if the source value is fresh. This preserves equalities and adjacency indefinitely. Conversely, cliques and independent sets have exact maxima \(\max(a,b)\) and \(\min(a,b)\), and sentences asserting the existence of \(r\) such vertices use exactly \(r\) variables. Two pebbles cannot detect cardinalities when every vertex has a neighbor and a distinct nonneighbor. Theory counts and defining widths follow from these two directions. Two independent finite programs provide corroboration, not an infinite proof.

## Originality

**PASS with residual historical-priority risk.** Primary literature inspected includes Pikhurko--Verbitsky on general graph logical complexity and Ehrenfeucht games, Berkholz--Krebs--Verbitsky on finite-variable alternation, Gray--Macpherson on connected-homogeneous graphs including rook structures, and Adler--Benediktsson--Macpherson on VC invariants of related Hamming and Johnson graphs. None of these inspected results gives the exact unlimited-depth \(\mathrm{FO}^{k}\) classification for all rectangular rook graphs. Semantic searches of published mathematical records found related complete-multipartite logical-width results but not a matching rook-graph statement. The latter search findings are not a complete proof of novelty; an uninspected general product or interpretation theorem may subsume the result. Direct transformation from the complete-bipartite classification does not preserve the number of variables without separate proof.

## Mathematical value

**PASS.** The family is a standard two-factor Hamming-type construction and a line-graph family appearing naturally in graph homogeneity and model-theoretic investigations. A complete exact classification for every fixed variable width, a sharp collapse at width two, an exact quadratic theory count, minimum representatives, and a strict hierarchy are structural results about this motivated natural family. They are not merely a finite enumeration or an arbitrary parameter slice. General products with more factors offer a possible further direction, but no such theorem is claimed.

## Closest literature and limits

The 2010 Gray--Macpherson paper establishes a very different structural classification of connected-homogeneous graphs. The 2010 Pikhurko--Verbitsky survey supplies general game methods but no matching rook-graph invariant in the sections inspected. The 2012 Berkholz--Krebs--Verbitsky work targets quantifier alternation. The 2020 Adler--Benediktsson--Macpherson paper concerns VC dimension/density rather than equivalence under all bounded-variable sentences. The theorem is restricted to pure adjacency without counting and to two-factor rook graphs; exact novelty priority is provisional. The self-contained proof covers all positive parameter values in the stated domain, while code tests only finitely many small cases.

Self-review: passed. Independent audit: not yet performed.
