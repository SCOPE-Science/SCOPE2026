# Scientific review

## Correctness — PASS

The two input strings each have exactly one run change but in opposite order. For a deletion-minimal common supersequence, every position is essential to at least one input; this bounds the zeros and ones by twice their required counts. An embedding-order contradiction forces one bound to be attained, and a second essentiality contradiction forbids both. In the full-zero case, the shared central ones are pinned between consecutive zeros, and deletion essentiality forces the exact outside-block boundary letters. The full-one case is symmetrical. Conversely every classified word makes all positions essential. Two independent generation routes in the standalone verifier agree with the analytic binomial-square multiplicities for tested pairs. Infinite correctness follows from the supplied symbolic proof, not the finite checks.

Risk: Proof relies on the precise indexing of essential outside ones. The explicit inequalities and several small asymmetric boundaries are provided for manual replay.

## Originality — PASS, with residual priority risk

The theorem is a complete **unequal-run** classification, not a claim to a previously considered equal-run subcase. Primary full-text examination of Sopp et al. (2026), Sun–Ge (2026), Lin (2026) and the 2022 arXiv Alon et al. version found general algorithms, primitive-layer decompositions or bounds rather than this explicit two-parameter binomial-square spectrum and branch transition. The older Fraser–Irving and Fraser–Irving–Middendorf records were identified, but full text could not be inspected. No identical or logically dominating published formula was identified in the checked accessible sources; the inaccessible paper is a real residual risk.

The Alon et al. 2022 arXiv statement of a total-count inequality, read literally, conflicts with the verified example \((a,b)=(2,3)\). This is not treated as a proof of new priority and is not used to justify the claim. Any corrected published version remains to be compared.

## Value — PASS

Minimal common supersequences model inclusion-minimal sequence merging, a problem specifically targeted by new enumeration algorithms in 2026. For a natural, unbounded, two-parameter input class, the theorem supplies all attainable lengths, exact multiplicities, and a qualitative transition absent in the equal-run slice: a unique shortest minimal supersequence with different central-run families appearing on opposite sides of a sharp threshold. This classification supplies explicit output-size instances and is not a numeric table or a renaming of the symmetric case.

## Scientific limitations

Binary inputs must each have one transition and unequal positive run lengths. No statement covers general inputs or additional strings. Historical priority and independent mathematical validation are unresolved.

Self-review: passed. Independent audit: not yet performed.
