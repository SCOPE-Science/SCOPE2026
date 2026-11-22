# Review of the interior Eulerian-row gcd theorem

## Correctness — PASS

Euler's generating identity reduces modulo two to \(E_n(t)=(1+t)^{n-1}\) in the prime field, giving the full parity criterion by Lucas's theorem. For an odd prime dividing every interior Eulerian coefficient, evaluation at one forces that prime to exceed the row index. The second- and fourth-cumulant identities, derived from the Eulerian generating function as rational formal series, then force the prime to be \(11\) and the index to be \(4\pmod{11}\), incompatible with indices at least five and below the prime. The two initial rows are evaluated directly. All denominators are invertible under the prime bound; no finite experiment is used as the infinite proof.

The standalone program checks 1,462 assertions on direct gcds, independent inclusion-exclusion coefficients, and exact rational moments. The computation is a diagnostic cross-check.

## Originality — PASS, with residual historical-priority risk

Nymann–Sáenz (1999) prove that every Eulerian coefficient in a prime-indexed row is one modulo that prime, not a classification for arbitrary indices or other prime divisors. Cao–Pan's accessible full text proves valuation bounds for sums over residue classes of Eulerian coefficients, not the gcd of all nonendpoint entries. The accessible Eulerian polynomial-congruence literature addresses polynomial identities near \(t=1\), which does not imply an integer-content classification. The `RowGcd` digital table gives compatible finite entries without a statement/proof for every index. Similar published gcd classifications for Narayana and generalized binomial rows have different coefficient objects and no identified implication to Eulerian rows. Semantic database searches for the exact claim and its equivalent coefficient-content formulation did not recover a dominating theorem; search absence alone is not treated as novelty proof. Possible older unindexed equivalent results remain a priority risk.

## Mathematical value — PASS

The gcd of the entire nonendpoint row is a canonical divisibility invariant of a central counting triangle. A complete answer for every row is a natural classification, not an arbitrary finite slice: it distinguishes a unique odd-prime obstruction, a dyadic infinite family, and all remaining rows. The fourth-cumulant exclusion explains why elementary parity evidence is exhaustive, and the all-index theorem goes beyond a computed table.

## Limits and provenance

Only the full interior row is classified. No valuation profile for individual entries or proper subcollections is implied. The proof and diagnostic code are included for reproducibility, and historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
