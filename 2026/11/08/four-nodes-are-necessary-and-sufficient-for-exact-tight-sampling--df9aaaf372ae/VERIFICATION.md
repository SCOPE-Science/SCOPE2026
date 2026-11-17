---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For f=a0+a1 z+a2 z²/√2, the proposed 0 node weight 1/2 and three radius √2 cube-root nodes weight 1/6 yield Gram diagonals 1/2+1/2, (3/6)·2=1, (3/6)·(4/2)=1; the angular sums vanish for exponents ±1,±2. A positive exactly-three-node tight frame in dimension 3 would give a square unitary evaluation matrix and pairwise orthogonal weighted rows, forcing K2(z_i,z_j)=1+t+t²/2=0 for every pair. Roots -1±i impose all node magnitudes 2^(1/4) and oriented angular differences ±3π/4. Three such differences cannot sum to 0 modulo 2π. Thus 3 impossible and 4 achievable, including repeated/smaller counts by rank. I checked exact diagonal rational moments and all eight ± phase sums; source CHECK.py was inspected. Gaussian coherent weight conversion is w_j=v_j exp(|z_j|²), positive. Does not claim exact integration of arbitrary bivariate quartic polynomials.

## originality

PASS

Finite exact minimal-node positive Parseval sampling in degree-two one-variable Fock polynomial space is not established by general infinite-dimensional near-tight discretization or one-circle conditioning theorems. Construction corresponds to a restricted complex Gaussian cubature; older cubature literature remains a genuine priority risk.

## value

PASS

Minimal positive exact point sampling is intrinsic to a finite-dimensional reproducing-kernel Hilbert space. The four-node constructive optimum and universal three-node obstruction give a sharp natural design threshold, though intentionally small and without a general-degree extension; exact finite natural invariants can be useful independently.

The dated certificate retains the supplied scientific assessment, sources and limitations.
