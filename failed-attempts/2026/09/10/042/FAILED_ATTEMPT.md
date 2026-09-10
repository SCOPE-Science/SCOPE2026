# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Tagged-skein versus upper-cluster sharp boundary for the quantum once-punctured torus
- **Round:** 2026-09-07-first-light-01
- **Lane:** 603
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Cluster Algebras
- **Method:** scattering-diagram wall-consistency with broken-line theta-basis expansion and skein multicurve comparison

## Problem

Decide the quantum tagged-skein versus upper-cluster boundary for the once-punctured torus S_{1,1}, the minimal case excluded by Li p>=2 and the Mandel-Qin caveat: either prove Sk^{ta}_q(S_{1,1}) = U_q(S_{1,1}) via finite MCG-orbit generator certificates, or exhibit one explicit theta element in U with no tagged-multicurve representative as a sharpness witness.

## Attempted claim

For Sigma = once-punctured torus S_{1,1} with frozen tagged triangulation T0 of Markov type B(T0) = [[0,2,-2],[-2,0,2],[2,-2,0]] (two plain arcs plus one notched arc at the puncture), the quantum tagged skein algebra equals the quantum upper cluster algebra, Sk^{ta}_q(S_{1,1}) = U_q(S_{1,1}), certified by explicit Laurent-expansion logs showing every MCG-orbit generator of each algebra lies in the other.

## Research outcome

Disproved the target: Sk^{ta}_q(S_{1,1})=U_q(S_{1,1}) is false. Classical separator W with auditable Laurent-invariance log plus three-part quantum impossibility (singular seed admits no BZ form; quantum notched-torus generator excluded; specialization contradiction). Replay: python3 output/artifacts/verify_target.py -> VERIFY_OK.

## Why this attempt failed

Failed axes: originality, value.

originality: Final headline (classical Sk^ta(S1,1)!=U via W + quantum impossibility (i)-(iii)) is substantively implied by prior published theorems; it is a corollary/repackaging, not a new decision. Li Sec7 states for Sigma_{g,1} that Sk^ta subset U is strict via the potential (same Markov W up to notation) and proves tilde-A codim-2 with Sk=Gamma(tilde-A) not Gamma(A)=U; Remark 7.2 cites Zhou Thm 1.4 for S1,1 equality Sk=Gamma(tilde-A). Zhou SIGMA 2020 Thms 1.1-1.4/Sec5 proves can=mid != Gamma=U for S1,1 with W extra generator. Mandel-Qin Thms 1.1/9.4/9.6/App B proves bracelets=theta except notched once-punctured torus, classical factor 4^k and extra wall D'=D+{(H,f_H)}, and Sec7.4 expressly excludes quantum notched-torus bracelets (genus>=2 via DT only). Quantum (i) det=0 forbids BZ Lambda is textbook linear algebra (product invertible => B invertible), not a new theorem; (ii) restates Mandel-Qin scope; (iii) conditional specialization is generic. No new scattering-consistency log, broken-line count, or skein non-membership computation beyond known identification is offered. Timestamp/failed search does not establish priority; substantive implication suffices to FAIL. value: Correct disproof assembled from known strictness results has no independent retrieval value beyond restating Li/Zhou/Mandel-Qin boundary. Classical W-in-U Laurent identities and seed/tag checks are already-published generator/invariance facts (Matherne-Muller/Zhou) re-verified mechanically; PH/lambda numerics are trivial evaluations of published formulas. Quantum (i)-(iii) are textbook incompatibility + scope restatement + conditional specialization with no new quantisation, census, criterion, or downstream theorem. Falls under textbook restatement / recomputation / certificate / corollary / repackaging of known stronger facts. Does not meet exact-invariant exception because object and value were known and mechanically implied via cited identifications.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The W-notin-Sk direction relies on the cited theorems of Zhou (can<U with W as extra generator), Mandel-Qin (can=Sk up to scalars for S_{1,1}), and Li (Sk<U strict, Sk=Gamma(tilde-A)); our script verifies W-in-U Laurent invariance, the seed/tagged-triangulation obstruction, and the lambda/PH numerics, not an independent skein-basis non-membership computation. The quantum no-go uses the BZ compatibility criterion and Mandel-Qin Sec 7.4 scope plus a specialization argument, not a full classificat…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
