---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The two rim families and two cross families form C_(2n)^2, counted once even at n=3. The side-triangle incidence bound in RESULT.md gives F>=n+(r_a+r_b)/2, with each rim defect count congruent to n modulo 2. An independent check uses bonds e_i=sigma_i sigma_(i+1) on the squared ring. If p is the number of + bonds and q the number of their cyclic runs in a nonconstant bond sequence, the energy in units J is 2p-4q, p is even, and q<=min(p,2n-p). The constant bond sequences cannot minimize. For even n, the minimum requires p=q=n, giving two alternating bond sequences and two spin orientations per sequence, each with M=0. For odd n, the minimum requires p=q=n-1: at p>=n+1 the bound gives energy at least -2n+6, and at p<=n-3 it gives at least -2n+6. The minimizing spin sequences have n+1 alternating-sign spin runs, exactly two of length 1 and all others length 2. To count labelled sequences, choose one of 2n start sites, a starting spin and the two short runs, and divide by n+1 possible choices of marked run. The two short runs on opposite signs give M=0 and count n(n+1); placing both on one sign gives n(n-1)/2 for each M=+2 and -2. Finite Gibbs fluctuation-response gives k_B T chi=Var(M), tending to the stated equal-weight ground variance at fixed n. A separate exhaustive squared-cycle enumeration for 3<=n<=9 reproduced the energy minima and each magnetization sector; it does not prove larger n. The uploaded checker was not executed.

## originality

FAIL

Resultary record 94f2eff70cbd, dated 2026-11-02 in the catalogue, explicitly gives the same Hamiltonian and size range, labelled ground energies and degeneracies, complete magnetization distribution and odd Curie coefficient, as part of a stronger exact result that includes the complete ground-state two-point functions. The even Curie limit is the immediate variance of its explicitly supported M=0 law. This is exact scientific coverage, not a title match or a conjectural connection to previous Ising methods.

## value

FAIL

The finite-size moment and commensurability distinction are mathematically meaningful, but the reviewed record repeats the exact invariants and response already given on the same natural object, with no surviving new quantity or structural result. The Laurent-polynomial presentation is a re-encoding of the exact earlier table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
