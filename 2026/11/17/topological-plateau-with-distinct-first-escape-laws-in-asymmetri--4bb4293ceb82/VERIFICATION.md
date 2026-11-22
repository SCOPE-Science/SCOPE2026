---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The negative doubling two affine branches have equal-length inverse cylinders, hence Lebesgue branch codes are IID fair bits. The left hole (1/4,1/2) is forbidden 00; the right dyadic cylinder is B_l=11 0 1 0... of length l=2k+1 or 2k+2. Since B_l contains no 00, first forbidden start is determined by first completion of either unequal-length word. Proper suffix-prefix overlaps yield two renewal equations, with an odd B-to-00 one-symbol overlap and an even B-to-B one-symbol overlap; elimination gives both displayed rational PGFs with denominator 1-t-t²+t^(2k+1). Differentiation at z=1 gives means (4^(k+1)-1-6k)/(4^k+2) and (4^(k+1)-1-3k)/(4^k+2). Because B_(2k+2)=B_(2k+1)1 and avoiding 00 forces a 1 after B_(2k+1), the infinite survivor languages agree; the Perron root comes from 1-sum_{j=0}^{k-1} t^(2j+1). Independent exhaustive enumeration of 2^(h+l+1) fair-bit words for k=1,2,3, both hole parities and h=0..5 reproduced the coefficients of each rational PGF exactly, using Fraction arithmetic. These finite cases corroborate; renewal and symbolic inclusion prove every k and horizon.

## originality

PASS

Best-of-knowledge originality: the exact claim is not mechanically implied by inspected primary or published related theorems. Equal survivor language entails equal entropy/dimension and exponential escape exponent but does NOT imply equal first-hit probabilities: the direct hole masses already differ at time zero, P(tau_w=0)=1/4+2^-(2k+1) versus P(tau_n=0)=1/4+2^-(2k+2). Prior symmetric formula cannot be transformed into these with a single parameter m, and generic prefix automata do not supply the compact explicit mean gap without further calculation. See explicit access and indexing risks; unsuccessful search is not proof of priority.

## value

PASS

Finite-time Lebesgue escape statistics inside a rigorously identical topological survivor plateau are a natural dynamical invariant not determined by entropy. The two close geometric hole widths have the same infinite symbolic trajectories yet explicit unequal all-time PGFs and a strictly positive k-dependent mean gap, isolating transient sensitivity that a topological invariant cannot detect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
