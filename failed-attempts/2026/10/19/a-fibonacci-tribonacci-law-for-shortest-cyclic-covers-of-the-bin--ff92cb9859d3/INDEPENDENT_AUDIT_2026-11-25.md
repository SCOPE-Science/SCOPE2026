# Independent mathematical audit

## correctness

PASS

A closed walk in the full de Bruijn graph minus one copy of each required arc has excess divergence +1 at precisely the vertices ending but not beginning in 11 (and -1 at the reversed type). An excess path from such a source cannot reach a vertex beginning in 11 before r shifts, where r is that source's first 11 index. For v=p11s the r-letter append p reversed reaches 11s reverse(p), stays legal, and is inverted by cutting at the last 11. This balances a strongly connected graph and yields an attaining Euler circuit. At k=3 both imbalance sets are empty. I recalculated P(z)=z(1+2z)/(1-z-z²)^2 and B(z)=1+z³+z^4 A(z) from the allowed prefix and suffix; multiplying by z³ gives the displayed excess. The zero-run recurrence is primitive (hence has a unique dominant simple pole), and at its pole rho, 1-rho-rho²=rho³ gives the asserted ratio. In a fresh finite replay I used BFS in both overlap graphs and a minimum assignment of source-to-target distances with matching dual certificate; the costs at k=3..10 were 0,1,4,9,21,45,93,188 in both graphs. This test corroborates the exact all-length proof.

## originality

FAIL

The earlier Resultary all-alphabet, all-run-length theorem gives the same rational law, all displayed numbers and the same reversed-prefix legal augmentation under a constrained-host definition. Its published dual certificate works on the full overlap graph without a new lemma: for a vertex of length L set phi to the first forbidden-prefix run a^(r-1) index, or L-(r-1)+1 if absent. In any full-graph left shift an existing occurrence can move left by at most one, and a newly created one can start only at L-(r-1); if a leftmost index zero disappears, the drop bound is automatic. Thus phi(u)-phi(v)≤1 on every edge, including forbidden windows. After removing required edges from a full-graph covering walk, the very same divergence identity sums these drops to the old sharp bound; the old legal augmentation attains it. The unrestricted-host assertion is therefore mechanically implied by the earlier certificate and construction, even though not explicitly stated there. The limit is also the corresponding pole ratio of the already given series. This is a prior-coverage finding, not an access-based rejection.

## value

FAIL

The natural all-length minimum and its overhead are useful invariants, but the record supplies no independently substantive increment over the earlier exact law and its published certificate. The apparent change of host domain only requires noticing that the same edge inequality never used legality; the new numerical limit is routine extraction from the same rational functions. No surviving valuable distinct claim was identified for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
