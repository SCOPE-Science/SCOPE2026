---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The proof correctly normalizes Haar measure and uses |gamma|=1. For ord χ>=7 or infinite, the seven frequency differences -3..3 are pairwise distinct, yielding s²+2Σ|R_h|² by Parseval. The outer and inner RMS pair estimates follow directly by Cauchy–Schwarz and AM–GM: |R1|≤2AB+B², |R2|≤2AB, |R3|≤A²; all can be sharp simultaneously. Writing t=A/B gives H(t) and H’(t)=−2(3t³+3t²−3t−1)/(1+t²)³. The cubic decreases only up to t=1/3, then strictly rises, has exactly one positive root rho≈0.7925172139743403 and gives global K≈2.808840165474397; both A=0 and B=0 give ratio at most 3/2. Equality demands a0=a3=A,a1=a2=B and common adjacent phase differences, giving precisely λ(rho,e^{iφ},e^{2iφ},rho e^{3iφ}). Direct exact cyclic-correlation enumeration at orders 4,5,6 with all coefficients one gives ratios 4,13/4,23/8>K. An independently written checker verified both derivative factorizations, the reciprocal parameterization of the earlier source, 1610 finite-group comparisons/sharp extremizers (largest direct-vs-correlation deviation 4.27e-14), and the exact small-grid witnesses. The finite checks corroborate, rather than replace, the universal algebraic proof.

## originality

FAIL

An original public SCOPE record, Exact fourth moment and all extremizers for four consecutive Fourier characters, with earlier Git commit timestamp 2026-10-11T12:57:45Z, proves the identical unrestricted complex-coefficient four-mode sharp L2-to-L4 fourth-power constant and equality family; the current audited source commit is 2026-10-11T12:59:37Z. The first theorem uses t=1/rho; its cubic t^3+3t^2-3t-3=0 is exactly -P(rho)/rho^3=0, its rational constant M(t) equals H(rho), and multiplying its (1,t,t,1) optimizer by rho gives (rho,1,1,rho). Every compact abelian χ case reduces by Haar pushforward to the earlier circle or cyclic grid case. The only extra assertion, explicit strict failure of the stable constant for N=4,5,6, is obtained by the all-one coefficients and a 3-entry finite check, insufficient to constitute independent novelty/value. The earlier source was read in full rather than relying on a matching search snippet; the timestamp distinction is verified from original Git commits, not guessed from identical publication dates.

## value

FAIL

Sharp L2-to-L4 constants on a four-frequency progression are naturally motivated, and the all-parameter theorem would be valuable if new. But the previous 2026-10-11 four-frequency publication fully establishes the same exact sharp constant and all equality cases; extending its grid/circle result by Haar pushforward does not add a novel invariant. The only remaining small-order nonstability assertion is certified by evaluating the all-ones four-tuple on three tiny cyclic grids. That calculation has no separately motivated structural insight, complete classification of those small orders, or substantive independent mathematical gap. Correctness and reproducibility of that finite witness do not confer research value. This rejection is based on full prior implication plus remaining content, not on a blanket bar against finite mathematics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
