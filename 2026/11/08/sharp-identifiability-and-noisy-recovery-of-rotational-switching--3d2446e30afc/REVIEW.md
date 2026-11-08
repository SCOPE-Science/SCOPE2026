# Scientific review: rotational switching-itinerary identifiability

## Correctness — PASS

The claim has four logically separate ingredients. The circular interval-overlap identity (5) gives the exact switch count; the two exclusive maximum-correlation lags yield the necklace equivalence \(m\sim -m\); the prime-period arithmetic gives all ambiguity classes; and the independent resampling-plus-bit-flip model gives the observation probability and matching information-theoretic upper and lower sample bounds. Every use of a statistical inequality states its distribution and range. The converse bound concerns only independent two-symbol disagreement samples, not general access to the original word. The universal proof is mathematical, while the exact checker provides limited finite corroboration.

## Originality — PASS within the inspected evidence

The nearest primary source is Simpson, arXiv:2312.03887v1 (2023), which defines precisely the rotational switching words and relates them to invariant-circle dynamics. Its Section 3 and border-collision results do not assert the occupancy-sensitive single-switch-statistic identification criterion or its noise-limited inverse problem. Frid–Jamet, arXiv:1302.3722 (2013), enumerates binary rotation words of arbitrary intervals; Berstel–Vuillon, arXiv:math/0106217 (2001), studies their Sturmian recoding. Neither inspected full text establishes the stated phase-blind switch ambiguity and sharp noisy recovery law. Published research-record searches surfaced generic binary adjacent-pair multispectrum enumeration and full-cycle reconstruction by much richer signatures, but these do not directly imply the specialized theorem. Their full documents were not accessible during this comparison; possible equivalent or stronger older formulations remain a priority risk. There is no claim that circle-overlap identities, elementary concentration, or binary hypothesis-testing inequalities are themselves new.

## Mathematical value — PASS

Rotational words are the admissible symbolic class for a natural mode-locking mechanism. Recovering the rotation class from only the fraction of adjacent symbol changes is a well-posed minimal-observation inverse problem: the theorem determines precisely which occupancies allow it and how many distinct dynamical necklaces are indistinguishable otherwise. It also quantifies the sharp quadratic-in-period and fourth-power-in-noise-contrast experimental cost when only fresh noisy adjacent disagreements are observable. This is a structural identifiability boundary with an explicit information-theoretic obstruction, not a renamed word count or a numerical curiosity.

## Limits and risk

The statements do not cover nonrotational sequences, correlated sequential samples, unknown error probability, or recovery of the orientation \(m\) versus \(p-m\). A broad and possibly fragmented literature on cyclic interval sequences, phase retrieval, and Sturmian codings could contain equivalent formulas. Search absence is not proof of global priority.

Self-review: passed. Independent audit: not yet performed.
