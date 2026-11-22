---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS: from r=x^2-1 and G=x(1-ar), r'=r q_a(r), q_a(r)=1-2a+(a^2-2a)r+a^2 r^2. q(-1)=q(2/a)=1; vertex r*=(2-a)/(2a) has q=-b, b=a+a^2/4. Since q<=1, H=q^2 exceeds t>=1 iff q<-sqrt(t), giving r_pm=[2-a±sqrt(a^2+4a-4sqrt(t))]/(2a). For X uniform on (-sqrt(1+2/a),sqrt(1+2/a)), calculate probability [sqrt(1+r_+)-sqrt(1+r_-)]/sqrt(1+2/a)=sqrt(1-2sqrt(1+sqrt(t))/(a+2)), supported 1<=t<b^2 when a>2sqrt(2)-2. For Z=a(X^2-1) independently uniform on (-a,2), interval width produces sqrt(max(a^2+4a-4sqrt(t),0))/(a+2). Essential sup b^2; derivatives give asserted endpoint and onset constants. For sign flip r>1/a, whereas amplification r<r_+(1)<1/a (a<1), so events disjoint. The probability 1-sqrt((a+1)/(a+2)) follows from |x|>sqrt(1+1/a). No trajectory-wide result follows.

## originality

PASS

PASS (best knowledge): earlier papers specify the identical cubic residual map, catapult onset and bounded domain, but their examined statements do not give the arbitrary severity threshold probabilities under two distinct continuous initialization measures or the event disjointness. The exact one-step superlevel measure is new relative to checked implications, not a new dynamical map or threshold. Inaccessible full Hofmann text is a real priority risk; no negative whole-document claim is made.

## value

PASS

PASS: the question of the distribution of a transient first-step loss spike is physically intrinsic to the exact quartic gradient dynamics; both initializations used in the literature lead to markedly different severity distributions, despite identical deterministic thresholds. Sharp onset, endpoint and sign-switch separation are diagnostic refinements beyond a binary stable/unstable classification, not a parameter renaming or gratuitous tiny instance. This is restricted one-step analysis, not a full catapult trajectory law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
