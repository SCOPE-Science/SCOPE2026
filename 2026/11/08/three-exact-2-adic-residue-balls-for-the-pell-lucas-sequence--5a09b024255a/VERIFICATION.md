---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Let x_n=Q_n/2 for Q_{n+2}=2Q_{n+1}+Q_n and Q0=Q1=2. The norm identity in Z[sqrt2], v2(P_m)=v2(m), and addition law prove v2(x_{4t+r}−x_{4s+r})=3+v2(t−s) for r=1,3. These two branches are isometric onto 1+8Z2 and 7+8Z2. Even index m=odd gives x_{2m}=3+32(z+4z²), z=(x_m−1)/8, and z↦z+4z² is an exact 2-adic isometry; m even gives an already covered odd branch. Therefore the exact Q support is (2+16Z2)∪(14+16Z2)∪(6+64Z2), with finite-modulus classes 9·2^(k−6) for k≥6 and Haar measure 9/64. Independent complete recurrence-state cycle enumeration for k=1..12 confirmed every image class, not merely a sample of indices.

## originality

PASS

Best-of-knowledge new exact 2-adic value-image support and Haar measure of the Pell–Lucas trace Q_n. A published general negative-sign even-trace Lucas theorem treats X²−PX+1 with 4|P, whereas this sequence has X²−2X−1; the results are not equivalent by sign or parameter specialization. Pell companion cycle spectra classify pair-state periods, not which scalar residues the particular trace seed attains. Lang and Lang give residue-completeness conditions only, not the three disks or their 9/64 measure.

## value

PASS

The exact support, infinitely repeated residue-class characterization and Haar measure 9/64 solve a natural ramified-prime local-image problem for the classical Pell–Lucas companion. This is a complete all-power classification with a structural isometry explanation, not just a few numerical residues or a routine recurrence period.

The dated certificate retains the supplied scientific assessment, sources and limitations.
