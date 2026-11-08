---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification evidence

The analytic certificate is the combination of (i) the exact arc-span identity \(\beta=(\pi-u)/m\), (ii) polygon-plus-sector area decomposition, and (iii) strict concavity of \(f(z)=z\cot z\) on \([0,\pi/2]\), which yields \(f(a)+f(b)>1+f(a+b)\) for all positive \(a,b\) with \(a+b\le\pi/2\). This directly proves strict order for all integer arc counts and all perimeters in scope. Taylor expansions derive the sharp asymptotic rates.

The included `verify.py` uses independent midpoint integration of the radial intersection function and checks finite examples and rates. It has no nonstandard Python dependencies. Execution command: `python verify.py`; successful execution prints `DISK_HIERARCHY_CHECKS_OK` and a count. Its finite assertions are not an infinite proof, nor are floating-point inequalities an exact certification. The proof in `RESULT.md` provides the universal justification.

Historical priority against inaccessible older source text remains provisional. No independent audit was requested or performed.
