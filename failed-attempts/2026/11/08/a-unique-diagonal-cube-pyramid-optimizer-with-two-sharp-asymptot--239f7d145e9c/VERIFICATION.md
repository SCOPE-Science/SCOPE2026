---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Coarea gives V(s)=sf_n(s)/n. Log-concavity of f_n and strict concavity of log s prove one optimizer; central derivative is positive. Differentiated sinc Fourier expansion produces f_n(n/2+x)/sqrt(6/(pi n))=1-(6x²+3/20)/n+(18x⁴+9x²/2-13/1120)/n²+O(n^-3) uniformly on bounded x; solving the first derivative gives x=1/6+2/(45n), and substitution yields 1+1/(6n)+7/(120n²) and absolute 73/3360. The two earlier published full proofs independently establish the same results.

## originality

FAIL

FAIL: an October 18 published Resultary RESULT.md gives the exact same theorem for every n>=3, including uniqueness, maximizer offset, normalized gain, absolute volume, and dimension-three boundary. An October 25 source repeats the same theorem and adds an n=4 benchmark. The assigned finding is mathematically identical under the centralization x=s-n/2; later wording does not restore originality.

## value

FAIL

FAIL: all principal independent conclusions, including two sharp asymptotic corrections and the absolute coefficient, are explicitly proved in the earlier October 18 source; the submission adds no material mathematical invariant beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
