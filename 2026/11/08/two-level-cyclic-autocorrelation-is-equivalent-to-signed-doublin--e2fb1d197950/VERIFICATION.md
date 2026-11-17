---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The subset generating polynomial gives B(t)=prod_a(1+zeta^(ta))^m(a); the DFT of periodic autocorrelation H(s) is |B(t)|², yielding the exact two-level constant by character inversion. Since 1+z=(1-z²)/(1-z), log|B(t)| becomes sum delta(a)log|1-zeta^(ta)| for delta=m(2^-1 a)-m(a). Invariance of c makes delta antisymmetric and kills all these log sums. Conversely for any even nonprincipal character psi of the unit group, isolate its primitive even conductor d|n using t=(n/d)u; the weighted log-sine transform equals -tau(chi)L(1,conjugate chi), nonzero by Gauss sums and Dirichlet nonvanishing. Vanishing all even-character coefficients, plus principal zero, forces delta(a)+delta(-a)=0. Empty set and composite-modulus examples fit. Independent exhaustive binary-multiplicity tests for n=3,5,7,9 and direct n=9,65 nonuniform profiles agreed; finite cases are not the all-odd proof.

## originality

PASS

Gaitanas 2023 treats completely uniform nonempty subset sums and signed doubling progressions with modulus restrictions; Ciprietti–Glaudo treat equality/reconstruction of full subset-sum multisets. Crucially Glaudo–Kravitz 2024 Theorems 1.5/1.6 already use precisely the space V of signed-doubling-invariant multiplicity differences to characterize equality of two whole subset-sum multisets up to shift. That is a very close algebraic formulation, but does not explicitly assert that a *single* multiset has all nonprincipal Fourier magnitudes equal one, or a two-level autocorrelation, and direct specialization from profile equality would require an additional suitable comparison multiset/phase argument. The current complete Fourier-flatness iff on arbitrary odd moduli is best-of-knowledge distinct, subject to high priority risk of an implicit corollary.

## value

PASS

It completely characterizes a natural two-level cyclic autocorrelation invariant of subset-sum counts over all odd moduli, separating constant Fourier magnitude from the stronger full equidistribution of nonempty subsets. The nontrivial primitive-character inversion and composite counterexamples show structure beyond prime-power progressions or finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
