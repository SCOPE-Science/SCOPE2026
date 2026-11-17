---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For P=pq, candidates m+Pk with m mod P avoiding residues 0,1 at p and q have exactly (r−1)/2+1_{m odd} odd lifts for 0<=k<r. Deleting two distinct excluded residues modulo r yields 2T(Pr)−S(Pr)=|G_P|+2O_P−2B_r. When r>P, the CRT digit u given by ur ≡ m−c (mod P) ensures parity of removed lift remains fixed for r modulo 2P. Exact finite certificates are (|G|,O,B)=(63,30,68) for p5 q23 r349 and (75,38,70) for p7 q17 r269, giving −13,+11. Dirichlet supplies infinitely many primes in the coprime progressions. Finite counts are not used to establish prime infinitude.

## originality

FAIL

Decisive exact prior coverage: Resultary published 2026-10-18 “Two-sided sharpness and residue spectra for the three-prime totient discrepancy” proves D(65r)=−6 for primes r≡24(mod65) and D(119r)=+6 for primes r≡31(mod119), where D=T−(S−1)/2. Algebraically D=−6 and +6 are exactly the assigned bounds T=(S−13)/2 and T=(S+11)/2. Its exhaustive residue table even includes P=115 with D=−6. Thus two-sided infinite sharpness, the entire assigned final claim, and stronger residue distributions were already proved; changing to P=115 for the negative example does not establish originality.

## value

FAIL

Sharp attainment of both constants is intrinsically meaningful, but that exact result, stronger infinite progressions, and finite residue spectra are already established in the October 18 theorem. The remaining different prime support and witness arithmetic is a routine already-tabulated specialization and does not supply an independently valuable new classification or unknown invariant. The rejection does not question correctness or the mathematical value of the prior theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
