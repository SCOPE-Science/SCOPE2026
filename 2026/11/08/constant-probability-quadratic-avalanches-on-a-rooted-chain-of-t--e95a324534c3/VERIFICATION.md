---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

A chain of k triangles meeting at articulation vertices has 3^k recurrent states by the blockwise burning condition. The explicit maximal odometer U(v_i)=2i (i<k), U(v_k)=2k-1, U(w_i)=2i-1 satisfies reduced Laplacian L U=e_{v{k-1}}+e_{vk}+e_{wk}. Least action bounds every initial recurrent state, with equality precisely when the last two triangle blocks carry (1,1). This gives 3^(k-2) maximizers and stationary probability 1/9; the harmonic-potential solution gives E(total topplings)=(2k^2+k)/3. Independent direct stabilization over all 3^k codes for k=2,...,6 confirmed both the extremizer criterion and exact mean; finite evidence is not the all-k proof.

## originality

PASS

Ali and Dhar (1995) solve avalanche scaling on decorated one-dimensional chains with alternating double/single bonds or diamond cells, not the one-sink chain of triangular cycles or exact stationary maximal-toppling event. Other Resultary results concern different sandpile graphs, source/sink choices, and distributions. No inspected prior statement supplies the exact constant-probability event 1/9 independent of k, or the explicit maximizing terminal block condition. PASS qualified by potential transfer-matrix treatments of triangular cactus graphs not yet identified.

## value

PASS

The effect of a fixed distal drive on a natural cactus family yields a non-obvious nonvanishing probability 1/9 of an O(k^2) extreme avalanche, with a two-block local recurrence certificate and an exact stationary mean. This is a structural stationary-law phenomenon, not a trivial sandpile group-order computation or tiny enumeration, and distinguishes maximal avalanches from typical-size scaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
