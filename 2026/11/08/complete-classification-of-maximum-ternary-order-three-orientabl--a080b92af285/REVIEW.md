# Scientific review: maximum ternary orientable cycles

## Correctness — PASS

The exact domain and equivalences are stated in RESULT.md. An orientable cyclic word cannot contain a palindrome or more than one triple from the same reversal class, so its length is at most nine. The nine reversal pairs are explicitly listed. An exhaustive enumeration of the \(512\) possible orientations yields ten balanced masks; only two are strongly connected. For each, direct integer determinant calculation gives four rooted in-arborescences, and the directed BEST formula gives four cyclic Euler circuits. Thus exactly eight cycles exist. An independent brute-force scan of every length-nine ternary word confirms the exact eight representatives and the two symmetry class sizes. The full proof concerns only the specified finite domain.

## Originality — PASS with historical risk

The earliest relevant date-verifiable preprint checked (Rampersad–Shallit, 2003-11-07) establishes infinite-word reversal avoidance, not this finite cyclic enumeration. Burris–Motta–Shipman (2016) cover palindromes as part of a different unoriented de Bruijn problem. Alhakim et al. (2024), Example 5.1, give one maximal ternary cycle; Gabrić–Sawada (2024) state the known length-nine optimum and one example. Mitchell–Wild (2026) develops general bounds and existence constructions. Exact eight-cycle classification and two nonisomorphic types are not contained in the inspected passages and results. The surviving risk is an earlier unpublished or unindexed full census, particularly in the early orientable-sequence tradition. Priority is not independently certified.

## Value — PASS

The smallest nonbinary three-window setting is the first natural finite test case for bidirectional position-and-direction labels with the full nine reverse-distinguishable windows. A full optimal-design classification answers how many labeled cyclic designs exist and whether they are unique up to obvious symmetries. The two nonisomorphic optimum families expose a genuine structural choice not supplied by a single construction or upper bound. The result is a natural complete classification, not a claim of coding performance or a general formula.

## Boundaries

The maximum nine is known; this work counts/classifies its equality cases. Both enumerations are exhaustive finite proofs with exact integer arithmetic. The source-priority comparison is best-knowledge only, and no external independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
