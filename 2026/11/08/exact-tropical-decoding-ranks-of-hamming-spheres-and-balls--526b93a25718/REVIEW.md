# Scientific review

## Correctness (C): PASS

The distance-to-sphere and distance-to-ball identities follow from the exact number of coordinate changes needed to attain the target weight. The only critical rank step is covered twice: an explicit finite min-plus factorization indexed by the weight interval \([a,b]\), and a tropical minor of that same order with entries \(|i-j|\) or \(\max\{0,i-j\}\). Both have a unique zero-cost identity permutation. The standard crossing argument establishes that tropical rank cannot exceed min-plus factor rank. All boundary cases \(\ell=0\), \(t=0\), \(r=0\), and \(r=m\) are included. The independent finite checker reports 432 parameter/function cases, 6,762 factorization-entry comparisons, 4,902 witness-permutation checks, 252 independent tropical-rank computations and 3,258 direct decoding comparisons. The proof, not finite enumeration, supplies the unrestricted quantifiers.

## Originality (O): PASS with residual historical-priority risk

The closest published source is Sheshadri, *Trellis State Complexity as an Exact Tropical Factorization Rank*, arXiv:2607.23471 (2026-07-26). Its accessible full text proves the exact power-of-two rank for binary **linear** codes. The present all-alphabet sphere/ball rank three at \(m=4,\ell=t=r=2\) is outside those hypotheses. The general tropical-rank framework of Develin–Santos–Sturmfels, arXiv:math/0312114, was compared in full experimental arXiv HTML, and Gaubert–Niv's tropical Monge/staircase paper was also inspected in full accessible HTML. Actual searches included clipped Hankel matrices, constant-weight decoder tables, Hamming-ball distance ranks, and broader tropical matrix-rank formulas. No matching full-parameter claim was found, but an implicit earlier derivation from general Monge theory or an uninspected paper remains possible. Search absence is not certified novelty.

## Value (V): PASS

Exact minimum factorization width is a useful representational invariant of conditional Hamming decoding. This result is an all-radius, all-cut and all-alphabet classification for two standard nonlinear radial families; it explains equality of their rank profiles and why nonlinear examples depart from power-of-two linear-code behavior. It does not pretend to solve general nonlinear trellis complexity or computational hardness.

## Limitations and closest literature

The theorem does not cover arbitrary nonlinear codes, non-Hamming error penalties, approximate tropical rank, or independent validation. The relevant 2026 article was inspected in its available full-text rendering, alongside the full accessible older foundational and Monge papers; unlocated alternative treatments still require historical-priority caution.

Self-review: passed. Independent audit: not yet performed.
