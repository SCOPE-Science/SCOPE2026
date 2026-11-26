# Independent mathematical audit

## correctness

PASS

Idempotence makes each component a fixed root with leaves. An isomorphism preserves root colour and the multiset of leaf colours. For k copies of a type with leaf multiplicities m_i the automorphism factor is k! times (product m_i!)^k. Order two thus comes only from one doubled leaf colour in one component, or one doubled rigid component type; all other leaf and component multiplicities must be at most one. This gives the two nonnegative terms in the polynomial. A sorted list of rigid weights contains every size 1 through q+1; at each step the next weight is at most one plus the preceding sum, so subset sums contain the entire interval through N_q. The internal defect can add every size from 3 through q+2; the external defect supplies size 2 and adds at most q+1 to the maximum rigid inventory. At the top size, all rigid types are present and precisely two independent colours (root and repeated leaf) specify the defect. The empty and one-point models are rigid. Orbit–stabilizer gives n!/2 labelled copies per class. Direct polynomial arithmetic gives the stated q=1 coefficients and the q=2 total 256(8+4)=3072. See RESULT.md lines 28–48 and checker.py lines 30–52, 80–125 for the frozen polynomial construction and finite diagnostic; the checker was inspected, not executed, and the all-q derivation does not require it.

## originality

FAIL

The univariate numbers for unrestricted nested equivalences differ, but the prior rooted-multiset order-two result is stated for any rooted hierarchy and its polynomial construction applies to any inventory of admissible child types. A coloured rooted star is a chosen root colour plus the prior height-one leaf multiset, now allowing it to be empty and adding one counted vertex for the root. Substituting those two child polynomials gives the entire proposed F_q, not just an analogy, and its support and extremal multiplicity follow directly from the resulting positive products and the already-known gap-free rigid inventory. This is demonstrated prior implication, not failure to locate an exact displayed formula or to obtain a paper.

## value

FAIL

The cutoff is natural and the explicit census is convenient, but it repackages the prior generic two-defect rule with the directly shifted height-one inventories. The endpoints and top count are immediate degree and interval consequences of the same substitution. No independently unknown exact invariant or further obstruction survives this overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
