---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each connected finite simple cactus and every finite abelian palette H of order q>=3, simultaneous colour translation forces unbalanced Fourier frequencies to zero. At a one-vertex block amalgamation balanced frequencies factor uniquely and W_G=q^{-1}W_{G1}W_{G2}; induction over the block-cut tree gives one global q factor and independent bridge/cycle lists. A bridge has normalized multiplier list (q−1,−1,...,−1). Fourier expansion of unequal-colour indicators on a cycle gives the pinned-potential list ((−1)^ell/q)sum_a(1−q)^{m_a}, integer by mod q. A zero satisfies sum_{a=1}^q(−(q−1))^{m_a}=0; divide by its minimum exponent and reduce modulo q−1>=2: precisely q−1 terms attain the minimum and the one other must be exactly one exponent higher. Thus length ell=qt+1, t>=1, with exactly ell!/[(t+1)!(t!)^(q−1)] pinned zeros. The rank product q^e∏(q^(ell_j−1)−Z_q(ell_j)) follows. Independently enumerated all Fourier transforms of q3 C3/C4, q4 C4/C5, q5 C6: extra balanced zeros 12,60,360 and ranks 15,196,2765, matching theorem. Finite tests do not replace the block and occupancy proofs.

## originality

PASS

Published separate ternary cycle and Klein-four cycle Walsh nullity classifications are explicit q=3 and q=4 special cases, correctly treated as *already covered* pieces. Goodall's graphical Fourier/Potts expansions and Babson–Beck graph-colouring results explain the edge transform but do not in inspected primary texts assert the full signed coefficient multiset independent of the abelian group structure for *every* cactus, nor the all-q exact zero/rank criterion. The new contribution is the simultaneous palette-agnostic all-cycle all-cactus extension and sharp block product, not the known special cases.

## value

PASS

An exact signed Fourier spectrum and recovery rank for every connected cactus and every finite abelian palette is a natural full classification; the resonance boundary ell≡1 mod q characterizes exactly when spectral information is lost. The block law gives reusable closed-form ranks under cactus gluings instead of a finite table of small graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
