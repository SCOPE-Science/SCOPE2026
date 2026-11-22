---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The synchronous 3-neighbor majority rule on C_n square K_2 has a direct 4-bit space-time transfer with 256 state-pairs for F^2-fixed configurations and a 2-bit/16-state transfer for F-fixed states. Frozen verify_transfer.py explicitly defines all triple-letter majority constraints, computes 400/20 allowed directed edges, cyclic strongly connected components 16,8,8,2,1,1 and 4,1,1, and exact integer characteristic polynomials via Newton identities; the characteristic power sums determine traces for ALL n, not just checked n. Independent implementation of microscopic neighbor majority from adjacency arrays enumerated ALL 2^(2n) labelled configurations at n=3..9 and reproduced (H_n,P_n)=(4,22),(8,64),(14,124),(22,484),(32,844),(48,2304),(76,5782). Exact direct comparison to Nov 1 published formulas f_P=R_n+2, q_P=(R_n+2)^2 for even n and R_{2n}+2 for odd n verifies equivalence via R_n=L_n+2cos(npi/3) and standard Lucas L_{2n}=L_n^2-2(-1)^n. The formula and orbit quotient are mathematically correct for labelled n>=3; the finite enumeration verifies the certificate inputs rather than establishing universal n alone.

## originality

FAIL

Decisive exact prior coverage. The complete fixed-state count, two-step recurrent count and primitive two-cycle count for the IDENTICAL prism graph, majority rule and labelled convention were published on November 1, 2026. The assigned six residue-class Lucas table is only the prior closed formulas expanded modulo six, and its leading asymptotic is the same. There is no distinct surviving new claim in the frozen RESULT.md.

## value

FAIL

The exact prism periodic orbit census is a natural worthwhile invariant IN GENERAL, but for this assigned claim it was already completely evaluated in the November 1 publication with an even broader prism/Möbius theorem. Re-expressing published formulas using residues and repeating an exact transfer certificate has no independent new mathematical value. This is a rejection of the unchanged combined claim, not a rejection of majority dynamics or of exact finite enumeration as such.

The dated certificate retains the supplied scientific assessment, sources and limitations.
