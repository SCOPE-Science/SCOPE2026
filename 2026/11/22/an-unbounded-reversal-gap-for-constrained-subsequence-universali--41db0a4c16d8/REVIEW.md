# Mathematical review: an unbounded reversal gap

## Correctness — PASS

The statement concerns the two entire binary language families for all \(d\ge2,k\ge1\). An arch-count lemma translates subsequence universality to reaching \(k\) complete two-letter arches. The factor monitor distinguishes an arbitrary terminal zero run for forbidden \(0^d1\) from an arbitrary initial zero run for forbidden \(10^d\). The proof enumerates all reachable right-quotient candidates, coalesces exactly the hopeless configurations, and supplies explicit shortest-completion and forbidden-run distinguishing suffixes. This proves both state counts for every allowed parameter. The standard-library `verify.py` independently minimized 384 constructed automata and compared 196,584 direct finite word cases. These calculations corroborate but do not replace the proof.

## Originality — PASS, with residual priority risk

Barker et al. (2020), *Scattered Factor-Universality of Words*, provides arch-based universality results but no exact automaton-state formula for these constrained languages. Adamson et al. (2023), *\(k\)-Universality of Regular Languages*, supplies general decision and counting methods for universal words intersected with regular languages, not a minimized-state equality classification of these two explicit regular intersections. An indexed result on Wheeler/prefix-sorted automata for the sole forbidden factor \(0^d1\) does not include the subsequence-universality condition, and an indexed run-cap result forbids an entire long run instead of the distinct pattern ending with a one. A general construction or algorithm is not itself a closed formula for the number of inequivalent residuals. No equivalent or stronger statement was identified in the checked material. The relevant indexed-record full text could not be inspected; unindexed equivalent literature remains possible.

## Value — PASS

The theorem identifies an exact **unbounded directional memory gap** inside a canonical, two-parameter intersection of the subsequence-universality language with a one-pattern avoidance language. Reversal preserves every lengthwise count but changes the number of required deterministic states by \(d-1\). This is a motivated structural classification, not a single small numerical instance or an automatic consequence of a product-state bound.

## Closest literature and limitations

The two closely related primary papers are Barker et al., arXiv:2003.04629v1 (2020-03-10), and Adamson et al., arXiv:2311.10658v1 (2023-11-17). Factor avoidance and scattered-subsequence universality are different constraints; the formulas apply only to the exact languages defined in the result. Independence and formal certification are not claimed.

Self-review: passed. Independent audit: not yet performed.
