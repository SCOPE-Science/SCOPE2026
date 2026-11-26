---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The state transition M(x,y,z)=(y,z,x+z) has eighth power I+3B with the stated integer B. For T=M^8, cubing inductively gives T^(3^j)=I+3^(j+1)(B+3C_j) with integral C_j. Raising to a positive 3-adic unit u preserves uB as the leading coefficient modulo 3. The starting block shift T^s is the identity modulo 3, so the first scalar coefficient at branch r is (a_(r+8)−a_r)/3, giving (3,4,6,9,13,19,28,41). Its five units give the claimed valuation for all distinct s,t, with swapping resolving negative t−s. The modulo-three word has unique 2, hence least period eight. The lift gives period 8·3^(k−1), and an arbitrary period 8d must return the branch-1 value, which requires 3^(k−1)|d. Each unit branch injects onto a whole mod-3 residue class within that period, by matching cardinalities. Only branch 4 is over 2, while 5 and 7 are over 0 and 1 and 6 are over 1. This proves the multiplicities and infinite recurrence, including when k=1.

## originality

FAIL

A distinct indexed record, e37859da9078, covers the entire frozen claim with the same initial conditions and period normalization. Its Proof explicitly states the same five-branch two-point valuation law (and extends it to 3-adic arguments), plus the per-branch residue-bijection consequence; its Finding supplies the same least period and strictly stronger full multiplicities. The overlap is established directly from the text, not from a title or date. The shared date does not establish historical priority in either direction. No separate mathematical conclusion survives beyond the stronger statement; a shorter elementary derivation here does not make the frozen theorem distinct.

## value

FAIL

The theorem is intrinsically a meaningful structural result about a classical recurrence. As a distinct finding, however, it adds neither an unknown exact invariant nor a new boundary: the stronger exact-fibre record explicitly gives all five isometries and the same least-period fibre contrast, with a complete census beyond it. The binomial version is a useful elementary exposition, but the frozen claim does not establish a separate reusable theorem or a scientific gain beyond that covered result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
