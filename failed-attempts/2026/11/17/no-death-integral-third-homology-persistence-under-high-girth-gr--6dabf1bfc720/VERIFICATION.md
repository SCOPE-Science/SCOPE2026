---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The asserted link-pair description for a valid insertion ab at distance >=6 is sound: L0 is complete bipartite K_{N(a),N(b)}, L1 is F-{a,b} together with that bipartite graph. Connectedness forces every component of the complement Q to meet the old link, so the relative incidence map C1(L1,L0;Z)->C0(L1,L0;Z) is integrally surjective and has saturated free kernel rank m-n+2=b(F)+1. The relative star-of-edge chain shift by 2 gives only relative H3=Z^{b+1}, and the H2(K)=0 inductively gives split injections with free cokernels. Independent small long-chord-cycle relative rank checks agreed. This is logically valid but is already contained in earlier published higher-generality argument.

## originality

FAIL

DECISIVE PRIOR COVERAGE: Full published 2026-10-18 Resultary theorem "Cycle-rank homology of total three-cut complexes of high-girth graphs" assumes only girth >=6 and has the same bounded-independence dual Γ(F)=BI3(F). Its PROOF §3 explicitly constructs a relative acyclic Morse matching after EACH edge insertion Γ(H)⊂Γ(H+e), states that this inclusion attaches exactly b(H)+1 three-cells and NO cells in other dimensions, and PROOF §4 says all these new S² attaching maps are nullhomotopic. The relative CW pair therefore has H3=Z^{b(H)+1} and other relative groups zero, and inclusion on H3 is primitive split mono with no deaths (by LES). Thus the entire alleged new persistence conclusion follows directly, even though the earlier title/boxed theorem emphasizes absolute ranks. The earlier theorem applies to girth >=6, strictly broader than current >=7. Cannot PASS by phrasing as new or adding explanatory certificate.

## value

FAIL

The natural filtration question is intrinsically motivated, but the precise claimed no-death integral groups and ranks are immediate, already-proved consequences of the explicit older relative-attachment construction. The new exposition offers a complementary incidence calculation, not a materially unknown structural fact or improved boundary. Correctness and reproducibility cannot make a covered statement newly valuable under this audit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
