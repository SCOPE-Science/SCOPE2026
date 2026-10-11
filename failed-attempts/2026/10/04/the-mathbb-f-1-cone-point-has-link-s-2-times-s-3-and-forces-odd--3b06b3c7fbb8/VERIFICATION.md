---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Wuebben's current primary source supplies the two nonstandard geometric inputs: \(X_C\) has one singularity analytically equal to the anticanonical cone over \(\mathbb F_1\), and its smooth crepant resolution has \((h^{1,1},h^{2,1})=(4,108)\). The cone link is the unit circle bundle of \(K_{\mathbb F_1}\). With \(K=-2S-3F\), fresh intersection arithmetic gives \(K\cdot S=-1\) and \(K\cdot F=-2\), so the Euler class is primitive, the circle bundle is simply connected, and its Gysin sequence has \(H^2\cong H^3\cong\mathbb Z\) with no torsion. Because \(w_2(\mathbb F_1)\equiv -K\pmod2\) pulls back to zero, the link is spin; Smale--Barden then gives \(S^2\times S^3\). The resolution Euler characteristic is \(2(4-108)=-208\), and replacing the exceptional \(\mathbb F_1\), of Euler characteristic four, by a point gives \(-211\). Odd Euler characteristic excludes rational Poincaré duality in formal dimension six.

## originality

FAIL

The current full primary source already states that the unique germ is the anticanonical cone over \(\mathbb F_1\) and gives the smooth crepant resolution Hodge numbers \((4,108)\). From those exact inputs, the assigned conclusions are formal standard-topology consequences: the link of a line-bundle cone is its unit circle bundle, the primitive Euler class and Gysin sequence determine the homology, Smale--Barden identifies the simply connected spin five-manifold, and Euler additivity gives \(-211\). The primary source does not print the final numbers or link type, but under implication-based originality those unstated textbook consequences are covered.

## value

FAIL

The link and odd Euler characteristic are clean descriptive invariants, but after the source fixes the local cone and resolution Hodge pair, the calculation is a standard Gysin/Smale--Barden exercise plus one-line Euler additivity. Under the common value bar this is useful exposition of a known object rather than an independently motivated new structural gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
