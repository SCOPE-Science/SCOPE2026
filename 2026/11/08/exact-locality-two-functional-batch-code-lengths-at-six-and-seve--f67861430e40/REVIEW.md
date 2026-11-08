# Scientific review: exact dimension-three locality-two batch lengths

## Correctness (C): PASS

The theorem has one precisely delimited claim, \(L_2(3,6)=12\) and \(L_2(3,7)=13\). The seven nonzero types and each size-one/two recovery have been modeled exhaustively. The identical-request upper capacity \(M_a\) is exact because its three relevant unordered type pairs are mutually disjoint. Summation of these capacities gives the exact pairwise discrepancy identity. Balancing integer multiplicities proves that lengths 11 and 12 respectively fail the necessary capacity inequality; monotonic padding excludes shorter codes. Actual encoded witnesses for all 924 and 1716 request multisets of the displayed 12- and 13-column generators have been independently replayed by `verify.py`, checking every XOR, distinct coordinate and size bound. A separate check enumerates the entire weak-composition domains for both obstruction thresholds. No solver optimality flag or partial numerical enumeration is used as a substitute for the infinite-domain balancing proof.

## Originality (O): PASS, subject to historical priority risk

Relevant primary full texts inspected: Oksner et al. (arXiv:2601.12302), which treats restricted retrieval and compares general bounds and the known 14-column 8-request code; Yohananov–Yaakobi (arXiv:2101.06722), whose double-simplex construction is explicitly excluded from the claim; and Kılıç–Ravagnani–Salizzoni (arXiv:2508.02586), which treats unrestricted sizes. The available full text on simplex batch properties (arXiv:2110.07421) and the accessible abstract of Lember–Riet (arXiv:2405.02107) were also compared. An exact earlier five-request locality-two result is not part of this claim. Neither broad bounds nor the eight-request construction by themselves prove these mixed-request optima for the two punctured generators, while the present lower bounds are instance-sharp. Searches covering synonyms, punctuation, query counts and neighboring parameters did not identify an indexed result giving the same pair of exact values. The residual risk is an equivalent unindexed table or a general puncturing theorem that implies both cases; definitive priority cannot be guaranteed without a broader historical audit.

## Value (V): PASS

The original research problem asks how much storage is needed for simultaneous arbitrary linear-form retrieval with small recovery sets. The two adjacent exact thresholds close a concrete finite, locality-constrained gap in its smallest interesting dimension. At six requests the restriction costs one column compared with the unrestricted length 11, whereas seven requests are possible at unrestricted length 13 with size-two retrievals. The distinction is supported by sharp lower bounds and mixed-request certificates, not by a superficial numerical example. Both lengths are natural adjacent instances of the contemporary small-recovery code-length problem, and the constructions serve as verifiable design benchmarks.

## Limits

No general all-request-length formula, classification of all optimizers, or efficient constructive decoder is asserted. The finite proof relies on provided recovery certificates, and independent scientific assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
