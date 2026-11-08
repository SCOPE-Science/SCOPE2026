# Mathematical review

## Correctness — PASS

A fort avoiding the hub is exactly a rim set complementary to an independent set; it is inclusion-minimal precisely when that independent set is maximal. A fort containing the hub corresponds to a minimal dominating rim set, except the two alternating sets on even rims. The cyclic-gap description of a minimal dominating set uses gap values zero, one and two, with exactly the six allowed adjacent gap pairs stated in the result. The trace-log transfer matrix has determinant \(1-zx^2-zx^3-z^2x^4+z^3x^6\), and the two correction terms remove artificial order-two contributions and forbidden alternating sets. Independent graph-level enumeration over all proper nonempty subsets agrees for every rim size three through twelve, and exact polynomial recurrences agree through order 160. The fractional LP proof uses all automorphisms of the rim and exact minimum-size witnesses, not an unchecked solver optimum. The asymptotic proof uses primitive transfer-matrix spectral theory and identifies the leading pole coefficient as one.

## Originality — PASS (provisional priority)

Cameron, Hogben, Kenter, Mojallal and Schuerger, arXiv:2310.17904, develop the fort hypergraph, fractional-transversal parameter, and values for several graph families. The inspected parameter table does not contain the wheel. These definitions and general principles are not claimed as new.

Becker, Cameron, Hanely, Ong and Previte, arXiv:2404.05963, Section 5.1, Proposition 20 and Corollary 21, provide a join construction, a wheel lower bound and the first thirteen hub-containing counts. The paper explicitly states that it does not know a formula for that sequence. Its existing characterization of maximal failed zero-forcing sets is consistent with the present structural split. The complete bivariate wheel minimal-fort census, closed recurrence for that sequence, exact fractional LP optimum and growth constant go beyond the implication of the inspected statements. A later paper on the hypercube fort numbers (arXiv:2507.10826) concerns a different graph family and is not evidence of wheel coverage. No prior indexed equivalent was found in targeted literature and mathematical-record searches. Searches do not prove priority; unindexed or later work remains a risk.

## Mathematical value — PASS

This solves the explicit wheel-enumeration question identified by the closest primary source, including every cardinality rather than a scalar count. It also gives a closed fractional zero-forcing optimum for a classical graph family absent from the available parameter table, quantifies its persistent gap from fort packing, and establishes a precise exponential growth rate. These are independently motivated natural graph invariants, not a reparameterized known calculation.

## Reproducibility and limits

Run `python3 verify_wheel_forts.py` with the Python 3 standard library. The program tests every nonempty vertex subset for rim orders three through twelve, and all proper nonempty subsets for minimality; it confirms exact polynomial coefficients and the published hub-containing sequence, with further formal-series recurrence comparisons through rim order 160. Numerical linear-program checks using a separate solver were also run for rim orders three through twelve, but the symbolic LP proof is the basis for the unrestricted statement. Verification is finite and does not constitute independent audit or establish publication priority.

Self-review: passed. Independent audit: not yet performed.
