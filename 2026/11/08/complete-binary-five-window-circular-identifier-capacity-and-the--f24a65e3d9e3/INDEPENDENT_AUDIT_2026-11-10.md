# Independent mathematical audit

## correctness

PASS

Each length-k binary cyclic identifier consumes k distinct 5-bit windows from a 32-word universe, giving floor(32/k) bound and automatic zero above k=32. The frozen witnesses.json provides full candidate optimal families for k=5..32 excluding seven; source verifier independently tests their window disjointness. At k=7 all 20 rotation classes are known from 2^7 strings; 2 constant and 6 with repeated 5-windows leave exactly 12 valid primitive cycles. Their explicitly listed partition into 3 internally intersecting classes (sizes 5,5,2) bounds an admissible family by 3, and three published disjoint 7-cycles attain. Independent direct 2^7 string/7-cycle intersection enumeration reproduces exactly 12 and no disjoint quadruple, yielding the unique deficit E(2,7,5)=3. This is an exhaustive finite certificate.

## originality

PASS

Grubman–Şekercioğlu–Wood define E(q,k,l), bound and de Bruijn packing equivalence with some constructions including k=8, but their main theorems do not assert the exact full fixed q=2,l=5,k range or k=7 obstruction. Cameron–Gündoğan–Sawada construct a single cut-down de Bruijn sequence, not simultaneous disjoint identifiers; Álvarez et al. count cycles without every cycle sharing the same length. Targeted database search found no dominating exact fixed-seven packing table.

## value

PASS

The five-window binary eBug invariant is a naturally motivated and explicitly defined noiseless circular robot identifier capacity. A complete all-k profile supplies sharp constructive capacities and isolates a nontrivial seven-position deficit in an otherwise tight counting bound. The obstruction is a meaningful finite combinatorial classification of de Bruijn equal-length disjoint cycles, not arbitrary numerology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
