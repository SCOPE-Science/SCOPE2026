---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The frozen proof counts i+α selected X′ points at the zero-branch endpoint t=m, although the queried trace is empty. This is a real counting error in the proof, not a counterexample to the theorem. The replacement proves that the one possible completion has exactly α=2u−i selected X′ points, even by the zero branch's choice of i. I checked the full corrected argument: complement pairs halve the slice and make the all-zero and all-one traces incompatible for a support of size m. After querying x₀, the two branches choose opposite parities of i from {u−1,u}; both exterior blocks are nonempty. For 0<t<m the lower endpoint max(0,t−β) is strictly smaller than both α and t, so the needed parity is always attainable. At the other endpoint t=0 in the one branch, the full support has the required odd count. This yields a complete depth-m tree and a static support of size m−1. No complete tree can exceed m because an all-positive path cannot repeat queries or use more than m positives. If a=1 the singleton is absent; if b=1 its label is fixed by m. Each residual class is a full k-of-(2m−1) layer with both dimensions min(k,2m−1−k)=m−1, including m=1. The unrestricted slice has both dimensions m by the same uniform-layer argument.

## originality

PASS

The exact simultaneous dimension classification, in particular preservation of depth m by different static supports after the first answer, survives the local proof correction unchanged. No materially compared source gives that implication. This is a qualified originality judgment, not priority certification.

## value

PASS

The model is a natural constant-weight class with one parity check. The sharp result distinguishes fixed from adaptive coordinate access at every size and explains why the gap disappears at a singleton block. The adaptive certificate consists of two explicit branchwise static supports. The value is this structural mechanism and complete boundary, not a numerical gap at a selected size or the standard uniform-layer formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
