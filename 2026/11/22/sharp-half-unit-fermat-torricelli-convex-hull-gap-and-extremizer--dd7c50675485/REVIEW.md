# Review of sharp median-to-hull gap and equality geometry

## Correctness — PASS
The median is coordinatewise. Two explicit admissible hull points establish the upper bound; equality forces coordinate sign agreement, and derivatives along two edges force equal common blocks and disjoint residual supports. Conversely the three-block construction has exactly constant triangle distance, and direct dual functionals prove both orthogonality directions. Complete quantifiers and limits are in `RESULT.md`. Reproducibility script passes 4,510 finite exact checks; it does not certify all inputs.

## Originality — PASS (with risk)
The closest original source is Fang–Qi–Liu, arXiv:2611.09226v1 (6 November 2026): a **qualitative** Birkhoff–James-orthogonal convex-hull characterization, not an exact l1-distance optimum. The coordinatewise median formula is known from Dragomir–Comănescu–Kikianty (2013, Theorem 6.3). Martini–Swanepoel–Weiss (2002; arXiv:0707.2592) address general loci and planar convex-hull inclusion; Paul–Roy–Sain–Sohel (2025) cover general optimization duality. Dedicated equivalent-formulation, broader-coverage, database and claim-implication searches found no stronger claim subsuming the sharp quantitative bound **and all equality configurations**. An equivalent unindexed result remains possible. See `AUDIT.json` for actual searches, comparisons and material inspections.

## Mathematical value — PASS
The result calculates the size of a natural failure mode in the qualitative Hilbert-space characterization, and rigidity identifies exactly which geometry maximizes that failure. A sharp universal constant and complete support-pattern classification hold in all dimensions at least three, with only one signed-permutation orbit at minimal dimension.

## Limitations
Only real finite-dimensional coordinate l1, two unit inputs and three equally weighted sites. Neither a general Banach-space stability theorem nor independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
