---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For r C4 squares meeting only at a hub, directly derived local peripheral-sink enumerator T=3+10z+z² and hub-sink enumerator B=3+z from the 14 noncyclic square orientations. Blocks share no simple cycles, so gluing gives S_r=T^r+(z−1)B^r. For z≠−3 roots satisfy [T(z)/B(z)]^r=1−z. The rational R(z)=z+7−18/(z+3) has derivative 1+18/(z+3)²>1, and comparison with H_r(z)=(1−z)^{1/r} proves exactly two simple real roots when r odd and four when r even; r=1 gives S=2z(z+6), r=2 yields all four real, higher r have nonreal roots. Independent SymPy exact Sturm real-root counts r=1..10 and derivative at zero equal (3r+1)3^r corroborate, not prove, unrestricted classification.

## originality

PASS

The closest all-acyclic-sink real-root theorem of Alexandersson–Maia Leite has chordal/claw-free hypotheses that square bouquets violate (induced C4, and induced claw when r≥2); its all-orientation version is a distinct invariant. Crown-graph sink-set and clique-bouquet results concern other graphs. The sharp parity-dependent root classification remains best-of-knowledge original, with a specific risk from inaccessible complete Alexandersson–Maia Leite text.

## value

PASS

Acyclic sink polynomials have a live real-rootedness conjecture/theorem landscape. A transparent cactus family moves from two real-rooted cases to universally nonreal-rooted larger examples and has a complete parity-controlled real-zero census, a mathematically motivated structural boundary outside chordal-claw-free hypotheses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
