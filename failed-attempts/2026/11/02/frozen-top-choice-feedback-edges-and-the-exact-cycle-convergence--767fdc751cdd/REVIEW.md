# Independent mathematical audit

## correctness

PASS

The departures proof is sound: to return to a strictly worse former partner in a periodic orbit, a vertex must first be passively abandoned by some better partner. Iterating those departures gives a nonbacktracking walk, impossible in a finite forest. An initially occupied or newly formed mutual first-choice edge is permanent. In each stage without a new such feedback-edge formation, deleting frozen endpoints and disregarding all unformed feedback edges makes the observed moves legal forest moves. The cited forest bound of n³/8 gives the stated integer bound, including n=1,2, with at most f+1 stages and f transitions. For C_n, every nonconstant cyclic sign word has a plus-to-minus transition giving a mutual first-choice edge, and a coherent profile gives an n-step orbit of singleton matchings; the move also works for n=3. This yields exactly two bad profiles and the claimed independent-uniform probability. The even coherent cycles have stable alternating perfect matchings; on an odd coherent cycle any unmatched vertex blocks together with the neighbor that ranks it first. The small-cycle checker and recorded finite output were inspected, not executed and not used as the proof.

## originality

FAIL

The 2007 literature on acyclic preference systems covers the principal qualitative claim through a stronger theorem with exactly the same move at quota one. Every simple preference cycle is a graph cycle around which each vertex prefers its successor to its predecessor. A mutual first-choice edge cannot lie on it: in either orientation one endpoint would have to prefer the cycle's other adjacent edge to the mutual first choice. Hence the frozen feedback hypothesis eliminates every preference cycle and the old theorem applies. On C_n, the only possible simple preference cycles are the two coherent orientations. Conversely any such orientation gives the immediate singleton-blocking sequence, so the claimed dichotomy and prevalence are elementary consequences of the earlier framework. The exact numerical stage bound was not found verbatim; it is a direct application of the known n³/8 move bound per forest stage and permanence of mutual-first edges, not an independently supported new main result.

## value

FAIL

Universal matching convergence is a meaningful question, but the narrower characterization here follows immediately from established preference-cycle convergence and a singleton witness. The surviving stage-count arithmetic uses the existing forest maximum unchanged once per phase, ignoring the shrinking active instance; no sharpness, improved bound in a consequential regime, or new obstruction is established. There is no independently valuable remainder to repair into an accepted finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
