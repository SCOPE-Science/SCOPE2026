---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Reconstructed the all-prime proof on the marked smooth finite coefficient base. Simultaneous vanishing of the partial derivatives implies all projective coordinates are nonzero and λ⁴=1, and at λ⁴=1 such a singular point exists (choose coordinates 1/λ,1,1,1). The coefficient extraction gives H_p=λ^(p-1) times the degree-m truncation at z=λ^(-4), m=floor((p-1)/4); from Wilson or the factorial multiplication formula the ratio in the j-th multinomial coefficient is (1/4)_j(1/2)_j(3/4)_j/(j!)³ modulo p. The chosen Clausen or Euler-transformed Gauss series terminates at k modulo p through degree m because one upper parameter is -k; denominators through that degree are invertible and the alternative squared polynomial with its possible factor 1-z has degree at most 2k+δ=m. Thus reduction of the formal identity yields the asserted polynomial identity, including λ=0 by extension. For the Gauss equation at a putative multiple root z0 outside {0,1}, the lowest nonzero Taylor term of order l≥2 would give a nonzero term of order l-2 multiplied by z0(1-z0)l(l-1), since l≤k<p. Also P(0)=1 and Vandermonde gives P(1)=(1-β)_k/k!, nonzero: the four starting representatives 3k+1,3k+2,3k+2,3k+3 and the next k-1 factors do not reach p. No leading coefficient vanishes (both parameters have no zero factor before k), so the lowest λ exponent d-4k is 0 or 1, as required at the Fermat point. The map λ↦λ^(-4) is étale off λ=0, yielding simple nonzero roots and excluding λ⁴=1. The monic polynomial has degree d, including the constant p=5 case. A smooth residue parameter lifts via an unramified characteristic-zero lift with good reduction. Rank at least 19 on the characteristic-zero pencil specializes injectively, and ρ≤22-2h excludes finite heights h≥2. Thus the Hasse vanishing locus is exactly the infinite-height locus. Read the supplied verifier but did not execute it. In a separate bounded modular replay at p=5,7,11,13,17,41,47,53,59,101,103,109,113,251,257, formed H from the multinomial, divided by the proposed boundary factor, solved top-down for a monic square root by matching the coefficient at λ^(d+j) (subtract the known higher-index products, then divide by 2), checked by squaring, and compared every predicted Gauss coefficient. The all-prime proof, not this replay, establishes squarefreeness and the height conclusion.

## originality

PASS

The coefficient Hasse test, the hypergeometric periods, the square-of-period structure after a Legendre change of variable, and the characteristic-zero Picard rank are prior. Credit is limited to the explicit monic characteristic-p square root with its boundary factor, the reduced support in the original marked coefficient coordinate including the capped-off Fermat point, and the all-prime geometric support count. No inspected source is a dominating theorem for that full divisor calculation. This is not a priority certification.

## value

PASS

The ordinary/nonordinary test does not answer how its divisor sits in the marked K3 pencil. The explicit all-prime factorization separates the singular boundary, settles multiplicity on the smooth base and gives a reduced defining polynomial and a geometric coefficient count, including the ramified Fermat point. These are useful exact invariants for this standard pencil, independent of any unsupported claim to count isomorphism classes or describe singular fibres.

The dated certificate retains the supplied scientific assessment, sources and limitations.
