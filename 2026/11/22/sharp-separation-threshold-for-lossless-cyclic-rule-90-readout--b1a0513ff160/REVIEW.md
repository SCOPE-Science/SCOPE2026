# Self-review

## Correctness — PASS

The proof states the domain of indexed binary cyclic words, the lower bound \(n\ge2r+3\), the observation rule, and the exact inverse-fiber quantifiers. First, an exact cyclic gap-composition bijection counts all admissible inputs, including the all-zero word. Second, any output collision has a difference in the complete kernel of Rule 90: a constant mask on odd rings, or an even-site, odd-site, or full-site mask on even rings. Third, the simultaneous forbidden-adjacency constraints exclude the full-site mask except for alternating inputs at \(r=1\), and force a pair of parity-complement patterns at spacing \(r=2,3\) and \(4\mid n\). The full-site exception and both parity cases are merged without double-counting. This proves the complete nonzero fiber spectrum and the exact source/image formulas for all permitted parameters. The actual standalone `verify.py` was executed from its package directory and passed exhaustive direct checks on 57 parameter pairs up to length 20. Enumeration is corroboration; all-size validity rests on the proof, not the checks.

## Originality — PASS, with historical-priority risk

Actual semantic published-finding corpus searches for Rule 90 under hard-core, sparse and run-length-limited aliases returned the unconstrained Rule 90 necklace predecessor classification, a hard-core-shift endomorphism rigidity result, and a temporal-sensor observability result as closest comparisons. Their complete public scientific `RESULT.md` texts were inspected. The necklace result uses the rotation quotient and unrestricted inputs; the rigidity result requires the map to preserve the source shift, whereas this observation generally does not; the sensor result uses multiple times and unrestricted sources. Salo's 2022 open-access article studies CA regularity and finite-type images, including Rule 28 on the golden-mean shift, but not this constrained Rule 90 input/output fiber census. Neither the compared statements nor their stronger general frameworks directly subsume the exclusion-dependent three-phase result. A possible equivalent prior theorem in constrained coding, linear CA, or inverse-word enumeration remains a specific priority risk; absence from search results is not proof of novelty.

## Mathematical value — PASS

The exact injectivity threshold in a natural separated-input observation problem is structurally sharp and persists at all stable ring lengths. Below the threshold the theorem distinguishes two isolated ambiguity outputs at \(r=2,3\), versus exponentially many double fibers and one triple fiber at \(r=1\), with complete multiplicities and explicit worst-case inputs. This supplies a precise input-spacing criterion for lossless deterministic local reconstruction, rather than an arbitrary finite census or a restatement of the classical linear kernel. No broad coding-capacity or error-correction claim is inferred.

## Closest literature and limitations

Salo, *On von Neumann regularity of cellular automata* (arXiv:2209.13373, first public 2022-09-27); *The four-valued predecessor law for cyclic Rule 90 necklaces*; *Radius-two rigidity across binary hard-core shifts, with sharp forbidden-block horizons*; and *Exact rank deficits and optimal static sensors for cyclic Rule 90*. See the full bibliographic links and exact logical distinctions in `RESULT.md`. The proof applies only to indexed binary rings of length \(n\ge2r+3\), noiseless one-step Rule 90, with unrestricted output words. The scope does not include small degenerate rings, temporal inversion, or independent priority certification.

Self-review: passed. Independent audit: not yet performed.
