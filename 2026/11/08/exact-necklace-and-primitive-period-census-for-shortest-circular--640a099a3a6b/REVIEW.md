# Self-review

## Correctness — PASS
The complete claim covers all labeled alphabets of size \(q\ge2\) and positive indices \(k\), only at the minimal length \(qk\). The greedy-arch characterization proves exactly when a shortest linear word is a concatenation of permutations. A circular phase is a cut residue modulo \(q\), and for any selected phase set the common-prefix-set argument identifies intersections with fixed blocks. Its ordered alphabet partitions give \(q!\bigl(\prod_i g_i!\bigr)^{k-1}\) possibilities. Inclusion–exclusion with a rooted-composition multiplicity \(q/t\) produces the marked-word formula. Equal symbol counts force periods divisible by \(q\); Burnside and Möbius yield orbit counts and primitive orbits. The complete derivation does not depend on finite checking. Actual standalone checks verify 19 explicit cases and 35 extra formula identities, as detailed in VERIFICATION.md.

## Originality — PASS, qualified
Barker et al. (2020) introduces precisely the circular universality object, but its section 4 treats repetition and index, not rotation-orbit enumeration. Fleischmann, Germann and Nowotka (2021) similarly study remainder/repetition. Adamson (2023) computes the linear enumeration; Adamson et al. (2023) offer broader automatic-language counting. Related public results give linear binary counts. The formulas here count the overlaps between circular permutation cuts and distinguish primitive periods, neither provided as a covering statement in the inspected sources. Existing ordinary necklace formulas alone do not select circularly universal words. Searches are best-knowledge evidence rather than proof against every possible equivalent, and an unindexed equivalent remains a risk.

## Value — PASS
The theorem is a uniform exact classification of a natural circular variant of scattered-subsequence universality at its sharp length bound. It determines labeled counts, full necklaces, primitive necklaces, the constrained period spectrum, the binary and ternary specializations, and exponential asymptotics. Cut-overlap inclusion–exclusion is structurally required rather than a routine relabeling of a previously counted object.

## Limitations and literature
The family counts minimum-length words only; it does not count longer strings or all circular witnessing phases per necklace. Independent validation has not been performed. Closest inspected original sources: arXiv:2003.04629v1, 2104.09063v1, 2304.04583v1 and 2311.10658v1. Finite verification cannot substitute for the proof, and the publication search is nonexhaustive.

Self-review: passed. Independent audit: not yet performed.
