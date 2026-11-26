---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Under u=|x|/a, inner states map by t(1−u), and outer by the increasing P(u)=s(u−1). Four successive outer states would require P³(u)>1 for some u≤t, whereas P³(t)=ρ<1. Hence the product in every regular four-window is at least Λ=ts³. The proposed u*=ρ/(1+Λ) is strictly inside (0,1); P³(t(1−u*))=u*>0 implies the three outer inputs are all >1 by working backward, and they are all <t because the first is <t and P strictly reduces a positive outer input. The magnitude orbit has one inner state per four and least period four. Precisely one sign reversal in four steps gives least signed period eight. For μ(B)=0, invariance removes the union of all forward boundary encounters (the union of the preimages of B), and expectation of each four-window gives inner mass ≥1/4. Equality makes the integer window count identically one almost surely and subtracting adjacent counts forces the repeated IOOO word up to shift. On that cylinder the four-step magnitude return is ρ−Λu; any displacement from its fixed point grows by Λ on each return and cannot stay in [0,t]. The lift is a single signed eight-cycle and invariance forces equal atom weights. This proves uniqueness of the minimizing measure, not uniqueness of all initial points with a limiting exponent equal to the floor. The rational sample cycle, all images and its multiplier 4096/625 were independently checked with `python3 /workspace/checks/exact_checks.py`; this is not the universal proof.

## originality

FAIL

A distinct Resultary result, 0e8f83f035e7, covers the floor and its sharp period-eight witness on a parameter chamber containing the entire frozen regime. Its proof supplies the precise symbolic restriction and expanding affine return that also give uniqueness of the minimizing invariant measure as a direct corollary. Thus the frozen mathematical claim is covered in the inspected corpus; this is not a judgment of chronological precedence, copying, or coverage by the 2021 paper. The matching record has a later catalogue path (2026/11/1 versus 2026/10/18).

## value

PASS

The invariant-measure minimum over an open chamber and the exact extremal measure address a natural expansion problem for a studied interval map with contracting branches. The analytical extremum adds information beyond typical numerical exponents and does not suggest cryptographic significance. This assesses the mathematical object and question, not distinctness from the covering result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
