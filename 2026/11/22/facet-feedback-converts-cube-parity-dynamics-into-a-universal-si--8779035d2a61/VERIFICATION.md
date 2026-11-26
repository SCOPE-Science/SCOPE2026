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

For m=d-1 the coordinate flips commute and square to I. The normalized neighbor part N=A_m+(m mod 2)I squares to zero; its two-by-two block equations show that the kernel is the graph of an involution, so its rank is 2^(m-1) for m>=1. Writing F=C⊗I+I⊗N and p=t²+t+1 gives p(F)=I⊗N, F³+I=C²⊗N, F⁶=I and F²+I=C⊗I invertible. Thus exactly q^(2^(d-1)) states are fixed by F³, only zero is fixed by F², and all states outside Fix(F³) have least period six. Dividing the populations by their respective least periods counts labelled temporal orbits. For the compressed cyclicity step in RESULT.md line 65, p(F)≠0 alone is not enough if p splits, but the displayed tensor form gives the full argument: for a Jordan pair Ne₂=e₁ take u=(1,0) and w=u⊗e₂. The vectors w,Fw,p(F)w,Fp(F)w are independent, since the first two project to u,Cu in the e₂ quotient and the last two give u,Cu in the e₁ subspace. Thus each four-dimensional summand is cyclic over every stated field. For d=1 only C remains, of order three and with no nonzero fixed state. The unmodified parity law follows by squaring the sum of flips. Inspected verify_algebra.py, verify_direct.py and their recorded outputs, not executed: the former checks binary matrices through d=8, the latter exhausts the listed finite (d,q) cases. The general proof does not depend on these checks.

## originality

PASS

Prior characteristic-two cube perturbations include periods three and six and even the same four-dimensional polynomial. The supported distinction is coefficient-one diagonal self-input on an entire coordinate facet, with the whole state space reversible and composed solely of identical cyclic blocks in both parities, giving the stated counts. No inspected stronger statement covers that combination.

## value

PASS

A coordinate facet is a natural feedback geometry. The same modification converts the square-zero even-dimensional and involutive odd-dimensional regimes into a common reversible dynamics. The whole-space cyclic decomposition and exact configuration populations add predictive information beyond discovering that some six-cycles exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
