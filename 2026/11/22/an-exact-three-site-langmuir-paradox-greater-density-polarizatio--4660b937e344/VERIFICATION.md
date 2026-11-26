---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The w=0 chain already communicates: any configuration can be emptied by right hops and exits, and a target is reachable by placing particles from right to left. Particle-hole reflection commutes with the generator. Denote the unnormalized pair weights of RESULT.md by A for 000/111, B for 100/110, C for 010/101, and E for 001/011. Direct generator balances reduce to (a+w)A=aE+wC, (1+w)B=aA+aC+wB, (1+a+w)C=B+wA and (2a+w)E=C+wE. Choosing E=a+w gives the stated A,B,C, which satisfy all four balances; their sum with E is D. The contrast is (E-B)/D, the adjacent covariances are (A-C)/(4D), and the distal numerator over 4D^2 simplifies to (A+C)^2-4BE=a^2(2a+4w+1)(1-2a). Since 4D-(2a+4w+1)(2a+1)^2=2a-1, the distal derivative has the claimed opposite sign (2D-2a+1>0); the adjacent and contrast derivatives follow by differentiating in w. At a=1/2 all weights agree and the contrast is zero, not strictly monotone. The strong-exchange limits follow directly. The frozen checker was inspected, not executed; the four exact balances, reflection and these rational identities are a replayable analytic verification.

## originality

PASS

The model and generator method are prior; the same-day counting-noise record even gives the exact stationary vector along the full w-line at a=1. The supported distinct result is the two-parameter classification, especially the sign reversal across a=1/2 and the opposed strict responses for all a≠1/2. The closest general exact method determines a kernel but does not give a closed stationary law or a correlation theorem that specializes to these inequalities; the fixed-a vector cannot give the reversal or global classification.

## value

PASS

Three sites are the smallest chain with an interior exchange site and two directed bonds. The all-rate signs and strict divergence between density contrast and connected covariance strength distinguish two transport diagnostics that could otherwise be conflated. They provide a finite calibration case near the product law, not evidence of a bulk phase transition or a longer-chain rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
