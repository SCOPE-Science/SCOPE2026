# Review of cyclic Rule-254 constrained inverse fibers

## Correctness — PASS

Every finite one-run is covered by input-one positions beginning one cell inside its left boundary and ending one inside its right boundary. The independent-source constraint and absence of holes enforce spacing precisely two or three, yielding the complete product formula. The classical all-one Perrin exception is separated from nonconstant runs. Rooted cyclic run-pairs yield the two logarithmic derivatives after explicit constant-word corrections, including the one-site ring. Dominant simple roots follow from nonnegative primitive renewal series. `verify.py` independently checks the claimed fibers, reachability test and both counting series through length 18. Finite checks do not establish the theorem beyond this range; the proof does.

## Originality — PASS, qualified

Full text: V. Salo, arXiv:2209.13373, §1 and §§5–6 (2022) concerns von Neumann regularity, golden-mean shifts for Rule 28 and SFT image questions, rather than the exact restricted Rule-254 run-product and logarithmic-derivative counts. Full text: Bisdorff and Marichal (2008), introduction and Perrin/bijection discussion, establishes the maximal-independent-set count, which subsumes the all-one case but does not give the variable-output product formula. Structured result searches for Rule 254, golden-mean restricted images, three-point dilation, forbidden one-runs, individual preimage fibers, and finite-type image counts returned nearby, but different-rule or different-domain results. In particular Rule 232 majority on hard-core input has distinct local logic and distinct run-gap fibers, and unrestricted Rule 110 has a Perrin maximum but not the present image spectrum. No exact equivalent table or broader theorem with these parameters was identified. Remaining risk: equivalent independent-set dilation or covering enumeration may exist under different terms.

## Value — PASS

This classifies, for every length and every possible observed output, both reachability and reconstruction ambiguity under a canonical constrained local readout. The three forbidden run lengths give a finite-type output description; the two rational series and their distinct growth rates quantify the exact loss of distinguishability and uniquely recoverable observations. It is not just the known Perrin homogeneous case or finite enumeration, and it does not claim error correction in noisy channels.

## Limits

This is a self-review with a documented residual historical-priority risk, not independent mathematical validation. The 2008 Perrin identity is acknowledged as prior. Every displayed formula applies to indexed cyclic words with the explicit size-one exception; no generalization to all source shifts is asserted.

Self-review: passed. Independent audit: not yet performed.
