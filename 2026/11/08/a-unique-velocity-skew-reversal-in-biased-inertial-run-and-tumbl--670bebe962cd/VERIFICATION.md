---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For b>0, q=alpha+beta>0 and delta=(beta-alpha)/q∈(-1,1), the oscillator drift is Hurwitz and independent Gaussian noise adds no centered cumulant of order three. Center Y=X-delta/b and telegraph S=sigma-delta. The algebraic two-state identity S²=(1-delta²)-2delta S and Markov generator produce the stated coupled linear recurrences for M_ij and N_ij. Reconstructed degree-one, degree-two and degree-three balance, and independently solved exact rational linear systems at b=2,q=1,delta=1/3,T=1/2; obtained (E Y³,E Y²V,E YV²,E V³)=(-19/297,0,-1/33,2/297), precisely the pinned formulas. Their positive denominator H and strictly positive factors imply position/mixed fixed signs and unique nonzero-bias velocity skew zero at 3b-2(q+1)=0; temperature never enters the third cumulant. Since 2(q+1)/3>2/3>1/4, the threshold is underdamped. Symmetric delta=0 is correctly excluded from a strict skew-sign reversal.

## originality

PASS

General dichotomous oscillator moment methods and symmetric inertial run-and-tumble harmonic-trap distributions precede this result. The assessed contribution is the exact biased stationary cubic tensor and the unique temperature/bias-independent velocity-skew sign threshold, not general generator techniques. A particularly relevant 1987 Pawula paper derives general output moments for dichotomous-noise-driven oscillators; its full text could not be inspected because authorized institutional access returned VPN disconnected. The publisher abstract does not settle whether it already includes this exact threshold. On accessible evidence the precise theorem survives best-of-knowledge comparison, with explicit significant priority risk.

## value

PASS

Biased telegraph propulsion generates nonzero stationary cubic moments even though symmetric propulsion cannot. The sharp stiffness that reverses *velocity* skew while position and mixed skew retain their signs provides a motivated structural boundary in the standard inertial harmonic swimmer and a robust noise-independent skew diagnostic, not a routine parameter rename or trivial normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
