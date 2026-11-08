# Independent mathematical audit

## correctness

FAIL

A binary length-n even-parity arc is the unique mandatory outgoing and incoming arc at every (n−1)-bit de Bruijn state, so the required subdigraph is a union of permutation cycles. Every circular cover is a connected Eulerian arc multiset; subtract the mandatory arcs to obtain balanced augmentation decomposable into simple cycles. The mandatory-component incidence hypergraph must be connected, and any chosen connected family yields an Euler cover. Given a witness augmentation of cost B_n, no optimum simple augmentation cycle has length >B_n. Canonical simple-cycle enumeration by least vertex and a strictly expanding bitmask recurrence therefore prove exhaustive lower bounds for each n=2..7; explicit 2^{n−1}+B_n witness words supply upper bounds. Outputs (4,7,16,24,46,82); odd-only restricted augmentation costs lead to 26 and 85 at n=5,7 versus 24 and 82. No n≥8 claim. SCIENTIFIC COUNTEREXAMPLE TO A SEPARATE EXPLICIT FINDING SENTENCE: The original RESULT.md asserts that an order-four optimal cover "requires all 16 possible windows," and REVIEW.md/AUDIT.json say it must be a complete de Bruijn cycle. This is false. The length-16 indexed circle s=1111001101010000 contains every even-parity binary 4-gram 0000,0011,0101,0110,1001,1010,1100,1111, but its 16 cyclic windows contain only 14 DISTINCT four-grams, omitting 0010 and 1011. Independent exhaustive enumeration of all 65536 binary indexed circles of length16 found 384 valid parity covers, of which 128 are NOT length-four de Bruijn cycles, and the least distinct-window count is 14. Thus the exact length L_4=16 remains correct, as do the verified finite length minima, but the additional asserted necessity of every binary word is false. Original final claim C=FAIL unless complete scientific files are repaired; no audit disclaimer is a repair.

## originality

PASS

Best-of-knowledge originality is a statement/implication comparison, not a title-match test. The exact established object, parameters, finite tables and known stronger results were cross-checked against published Resultary findings and primary literature; no decisive prior coverage of the final claim was established. Highly plausible inaccessible sources and indirect possible corollaries are disclosed in residual_risks. Searches alone are not novel proof.

## value

PASS

Even-parity n-grams are a natural disconnected spanning permutation of a de Bruijn graph. The first six exact cyclic covering minima, notably the n=5 and n=7 mixed-parity advantage and n=4 full de Bruijn boundary, provide meaningful small-order exact data and a reusable complete augmentation reduction, not an arbitrary window slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
