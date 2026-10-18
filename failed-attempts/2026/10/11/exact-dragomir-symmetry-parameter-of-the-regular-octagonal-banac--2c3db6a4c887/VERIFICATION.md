---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The deterministic exhaustive geometric proof was checked against the actual unit-ball vertices (±1,±r),(±r,±1), r=sqrt(2)-1. Quotient duality gives dist(y,Rx)=|det(x,y)|/max_{z in B}|det(x,z)|. Dihedral isometries reduce x to edge x=(1,t), |t|<r with unique supporting functional s, so unit y=(0,±1) and reverse distance 1/(1+r|t|)>=1/(1+r²). For vertex x=(1,r), the entire normal cone yields directions y=(q,-1)/N(q,-1), 0<=q<=1. Here det denominator 1+r², N(q,-1)=1 for q<=r or (1+q)/sqrt2 for q>=r, and expression (1+rq)/[(1+r²)N(q,-1)] is >=1/(1+r²) because sqrt2(1+rq)-(1+q)=r(1-q)>=0. Equality at q=0 and q=1. Therefore d0=(2+sqrt2)/4 and sqrt(1-d0²)=sqrt((5-2sqrt2)/8) for all Birkhoff pairs, not mere sampled pairs. Independently checked the radical, vertex-branch algebra using SymPy, as well as the exact source `verify.py`; its finite sampling is supplemental.

## originality

FAIL

Decisive **exact published overlap**: distinct published Resultary record SCOPE-20261011-54cfddcd9eed has precisely the same norm, Birkhoff/Dragomir definitions, exact radical sqrt((5-2sqrt2)/8), equivalent reverse distance (2+sqrt2)/4, and same extremizing x=(1,sqrt2-1), y=(0,-1). Read its actual full RESULT.md; its proof independently analyzes both edges and vertices. This is theorem equivalence, not a matching title or notation only. The present record is a duplicate, so no best-of-knowledge novelty PASS.

## value

FAIL

As currently submitted, the record repeats a complete already-published sharp evaluation on the identical norm with the identical extremizer and edge/vertex argument; it supplies no new structural lemma, classification, motivated cutoff, or unknown exact invariant beyond that covered result. Although the invariant itself is mathematically natural and the proof correct, the duplicate claim is known-table recomputation rather than a new valuable scientific finding under the specified bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
