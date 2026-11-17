---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Stationary Poisson-redraw direction has E u²=1/d, E u⁴=3/(d(d+2)); generator L gives six triangular stationary fourth moments and a six-variable forward two-time hierarchy. Subtraction of reverse-lag E[x0^3 xs] yields exactly the stated e^-4s exponential polynomial F_d(s)/[15d²(d+2)] at r=gamma/a=2. The independent thermal OU component adds identical Wick cross terms to both fourth moments, hence cancels for all D>=0. Direct symbolic differentiation gives F(0)=F’(0)=F’’(0)=0,F’’’(0)=-18(d+3). H_d=e^-s F’’’ is affine in d and negative for d=1,7 and thus all 1..7. For d>=8 H_d’ is upward quadratic in exp(s) with one crossing on s>=0; successive integrations from zero show exactly one positive zero of F and hence the sign diagram. The general-r short-lag cubic and r>1 long-lag e^-s coefficients were reconstructed from the same triangular generator. No claim of uniqueness for general r or of a zero-mode asymptotic was made. The supplied independent numerical RK4 checks are consistency tests only.

## originality

PASS

Existing trapped run-and-tumble work covers stationary distributions and generator/moment techniques, but the inspected primary analyses do not already state the single-coordinate fourth two-lag antisymmetry sign threshold d=7/8 with one unique crossing at gamma=2a. A general moment method is not itself a published classification of signs and zero counts.

## value

PASS

A sharp dimension transition in the sign of a genuine stationary time-order asymmetry is a motivated structural classification of a natural active-matter model, not merely a computed one-time moment. The unique crossing and exact thermal-noise insensitivity are nontrivial and reusable qualitative facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
