# Scientific review

## Correctness — PASS
The source's household offspring formula specializes to two exact mean counts after applying the susceptibility-biased seed probabilities, which are \(1/(r+1)\) and \(r/(r+1)\), rather than \(1/2\). Their difference reduces to \(F_r(x)\). The derivative factors through a strictly convex function with exactly one interior zero, proving a unique interior crossing of \(F_r\). Both exact threshold witnesses were independently recomputed with rational arithmetic in `verification.py`; the analytical proof covers all real \(r>1\), not just finite tests.

## Originality — PASS, with literature-priority risk
Ball and Critcher (2026) provide the general formula and threshold; these are credited and not reasserted as original. The uniform-in-contrast unique household assortativity reversal is a further sign-classification theorem, not directly given by the source's multitype threshold formula. Discrete-time household epidemic theory (Ball et al., 2026) and household-size herd-immunity comparisons (Ball et al., 2023) address different objects. A 2026 published result on household matching, outbreak probability and household reproduction numbers was read in full. It fixes the four local transmission probabilities, assumes equal global susceptibility weights, and varies the proportion of mixed pairs, showing opposite monotonicity of reproduction number and major-outbreak probability. It does not address a common local-intensity parameter or the unique crossing in the present opposing-traits family. Earlier broad multitype-household literature could contain an unlocated comparison. No exhaustive historical priority certification is claimed.

## Value — PASS
The two extremal household mixing arrangements preserve all individual activity, susceptibility and contact-rate parameters. Their *ranking* changes at a unique, contrast-dependent within-household transmission intensity for every real contrast greater than one. Exact examples make the qualitative major-outbreak threshold change sign in either direction. The classification directly distinguishes the influence of grouping individuals from their fixed individual transmission traits, a motivated epidemiological quantity not captured by an undirected comparison of reproduction formulas alone.

## Scientific limitations
Only the many-household invasion threshold, not outbreak-size or outbreak-probability ordering, is proved. The equal-type, two-person, reciprocal-trait model and one-unit infectious periods are explicit restrictions. The related 2026 household-matching result was inspected in full; the older general Ball–Lyne (2001) text was not inspected in full. All assertions of analytical correctness and scope are provisional pending independent evaluation.

Self-review: passed. Independent audit: not yet performed.
