# Review of negative-run normal form for interval membership

**Correctness — PASS.** The positive-observation version spaces are independent left- and right-endpoint thresholds, including boundary cases. Negative-only observations separate all admissible intervals into distinct unqueried runs, and querying one point splits precisely one run. The exact rank recurrence follows by induction on remaining sites; zero-capacity and singleton cases use the stated sentinel convention. The dyadic equality has matching lower and upper proofs. Independent explicit-concept computations agree through ten sites.

**Originality — PASS within inspected sources.** The closest checked works are Manurangsi–Rubinstein (2017) for general exact Ldim computation, Ghazi–Golowich–Kumar–Manurangsi (2021) for aggregation bounds, and Haghtalab–Roughgarden–Shetty (2021 preprint/2024 journal) for threshold-product lower bounds and interval VC dimension. None of the inspected relevant sections asserts the all-history interval-state decomposition and exact run-partition rank recursion. Earlier theorems on fixed-width translated intervals or two-row order ideals have different queries, so their mathematical implications do not state this result. Priority under alternative terminology remains an explicit risk.

**Value — PASS.** The central contribution is a complete structural classification of conditional online ranks for an important small-VC concept class, not merely a numerical table. The integer-partition normal form gives a direct exact recurrence, and the unrestricted theorem yields an infinite sharp entropy-bound family and an unbounded static/adaptive separation. The stated state-count bound is not represented as improving the best generic algorithm.

**Limitations.** There is no elementary closed formula for every input length; finite checks cannot replace the proof. Some ingredients (threshold rank, product additivity, information bound) are standard, and the dyadic special case alone is not claimed as an independent general technique. Independent mathematical review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
