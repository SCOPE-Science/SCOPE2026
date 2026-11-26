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

Independent-set enumeration on the stated 30-edge graph gives (1,12,36,20) by excitation number and parity sizes 37/32. An allowed single flip reverses excitation parity, so the Hermitian Hamiltonian has off-diagonal block B(t) and kernel dimensions 37−rank B and 32−rank B. The separate exact replay /workspace/branches/6b9550e8-81ba-4479-87d4-d4f79216bb25/icosahedron_check.py reconstructs the graph and block, matches every Gram characteristic coefficient at t=1 by integer traces and Newton identities, and symbolically reproduces the ordered maximal minor 2(t²−1)^6. The Gram polynomial has a zero of order six and all the displayed remaining factors have nonzero constant terms, giving rank 26 and nullities 11 plus 6. The identity det(xI−H)=x⁵ det(x²I−BᵀB) yields the entire stated homogeneous polynomial. The minor forces rank 32 at every real t other than ±1, including t=0. Multiplication of each basis state containing vertex 0 by −1 conjugates t to −t, so the homogeneous rank returns at −1. The five-mode lower bound applies to arbitrary real amplitudes by parity dimensions; the full sharp classification holds only for this single-site profile and ideal projected zero-detuning dynamics. Frozen scripts were read, not executed; the uniform rank and all-real-t classification do not depend on modular sampling.

## originality

PASS

The known graph combinatorics and standard chiral parity bound cover the baseline five modes. The distinct supported result is the full homogeneous spectrum and the sharp all-real single-defect rank classification, including the twelve extra modes present only at homogeneous drive magnitude.

## value

PASS

The icosahedron is a canonical Platonic interaction graph and a local drive defect is a meaningful perturbation of the homogeneous constrained Hamiltonian. The exact polynomial and all-real defect classification separate parity-protected multiplicity from twelve fine-tuned zero modes, rather than just reproducing the known independent-set count or a floating-point gap. These data are useful benchmarks for symmetry and sensitivity in constrained finite dynamics and do not assert physical zero modes away from perfect blockade and zero detuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
