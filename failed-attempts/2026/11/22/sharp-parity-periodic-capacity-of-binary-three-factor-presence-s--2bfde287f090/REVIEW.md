# Independent mathematical audit

## correctness

PASS

The suffix and seen-mask are sufficient: appending a bit creates exactly one possible new triple and retains the other triples. Independent replay in branches/bf210e71-76b5-4902-beff-b025063e40e3/independent_check.py reproduced R_3 through R_11 = 8,15,27,48,72,94,100,103,101, the full equality E_11=E_17 with 196 states, parity-wise equality of the six support sets and P(E_10)=P(E_12), and odd support contained in even support with difference 46 and 116. Direct enumeration reproduced the support sets for lengths 3–15. Equality of full states, not equal counts, propagates by determinism; inspecting the six phase sets proves the infinite assertion. For the first exceptional profile the only complete walks use one forced entry, a positive number of two-cycle traversals, and one forced exit, giving word length 4+2t; complementation handles the second. One word per profile is exactly the zero-error optimum. The frozen source scripts were inspected, not run.

## originality

FAIL

The all-length formula was not found stated verbatim in the earlier record. Nevertheless the earlier exact inverse-fiber DP computes the entire suffix-by-mask count array and uses the identical fixed transition. Its positivity patterns at lengths 11 and 17 are obtained by keeping the Boolean snapshots of the already computed arrays and comparing them; then projection, differencing and deterministic induction give the whole finding, not merely a few coincidences in the profile counts. This is mechanical coverage by the prior exact computational result, not an inference from unavailable literature or from the modal-fiber threshold by itself.

## value

FAIL

Known-length profile capacity is naturally motivated and the two persistent parity obstructions are useful facts to display. Here the complete exact invariant and the certificate reduce to routine zero/nonzero readout and comparison of a prior exact computation on the same object and already covered lengths. No separate surviving classification or new inference beyond that readout is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
