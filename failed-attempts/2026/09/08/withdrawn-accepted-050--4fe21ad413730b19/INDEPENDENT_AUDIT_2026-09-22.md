# Independent audit — 2026-09-22 campaign

**Record:** `SCOPE-20260908-050` / `2026/09/08/050`  
**Reviewed UTC date:** 2026-09-24  
**Audited public commit:** `f1bee63e7115a5c2a8df4210f09faab70a83c26b`  
**Source tree:** `4b90f5bf37742c00a06929441ab49539bfd5cd0d`  
**RESULT.md blob:** `b6071a69f09a219b20e9ef97cc22c642304bc2df`

## Claim audited

The record presents two explicit 200000-bit binary 2-abelian-cube-free words and a deterministic search/checking package. Its scientific framing says that binary 2-abelian-cube avoidability is still a live open boundary, that the only prior computational benchmark is length 100000, and that the new words therefore double the published benchmark without resolving the open problem.

## Correctness — FAIL

The literature-status statements that motivate the result are false.

Michaël Rao's paper *On some generalizations of abelian power avoidability* explicitly states in its abstract: "We prove that 2-abelian-cubes are avoidable over a binary alphabet." The introduction further says the constructed morphisms give 2-abelian-cube-free binary words and answer the prior question. This is an infinite construction, not merely a longer finite search witness. I inspected the openly available author PDF:
https://perso.ens-lyon.fr/michael.rao/publi/kab.pdf
and the published article is Theoretical Computer Science 601 (2015), DOI 10.1016/j.tcs.2015.07.026.

Thus the record's statements that the binary case is a "live open boundary", that a length-200000 word "pressures but does not resolve the open 2-vs-3-letter threshold", and that the scientific benchmark is still the 2011 length-100000 computation are materially incorrect.

The existence of the filed finite words may still be computationally true. I inspected the constructor/checker logic and the archived record reports full checking, but a complete independent 6.66-billion-candidate replay was not needed to decide the record after the decisive literature contradiction. This audit does not claim the words are invalid.

## Originality — FAIL

The finite existence claim is subsumed by a 2015 infinite binary 2-abelian-cube-free construction. Any prefix of sufficient length of such an infinite word yields a 200000-bit witness. Therefore a 200000-bit existence witness is not a new frontier result in 2026, regardless of whether this particular bit string or its search obstruction histogram is new.

The record cites a different 2015 Rao/Rosenfeld paper but omits Rao's directly decisive 2015 avoidability theorem.

## Scientific value — FAIL

Once infinite binary avoidance is known, extending a 2011 finite search witness from 100000 to 200000 does not advance the avoidability threshold. The obstruction histogram is specific to one greedy search and the record itself disclaims intrinsic significance for it. The package can remain useful as a stress-test fixture for checkers, but not as the claimed scientific benchmark advance.

## Final disposition

**FAILED.** The decisive reason is prior full-text literature proving infinite binary 2-abelian-cube avoidance, which invalidates the record's open-problem framing, novelty claim, and scientific-value rationale. This is not an access or infrastructure failure.
