---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The beta integral gives ||z^k||²=k!/(β+1)_k. The normalized double derivative has t^j coefficient (β+1)_{j+m} binom(j+m,m)^2/(j+m)!, giving the stated prefactor and Euler transform. Pfaff gives Q=(1−t)^m P_m^(0,β)((1+t)/(1−t)); the Cayley map takes positive Jacobi roots precisely into the attainable negative scalar interval (−1,0), excluding x=0. Orthogonality of the divided monic polynomials gives the derivative formula with a positive integrand, also valid near β=0; Legendre parity and the large-β collapse toward x=1 prove all crossings and their simplicity. Directly T_2=(β²−β−4)/2 and T_3=β(−β²+3β+16)/6. In the large-order recurrence, uniform convergence of the off-diagonals applies to the actual entries j=1,...,m−1, not to the artificial a_m=0. At the last row the missing link can only improve the Gershgorin lower bound; the last o(m) but divergent block has the limiting constant coefficients, and alternating sine vectors attain the limiting lower edge. This proves h(c) and by monotonicity the strict two-sided threshold statements. Fixed-order hypergeometric coefficients differ from Laguerre by O_m(β^-1); simplicity and the Cayley map give the stated O_m(β^-2) refinement. Independent bounded replay: python /workspace/reproductions/check.py 4 (252 exact kernel coefficients, m=2,3 crossings, high-order and Laguerre spectrum samples). The finite spectra corroborate but do not prove the limits. The frozen CHECK.py was inspected, not executed.

## originality

PASS

Pass for the complete arbitrary-weight disk pure-jet zero-fibre phase law as an application, not for Jacobi monotonicity, the leading Laguerre contraction, the unweighted case, the general differential Gram representation, or the varying-Jacobi endpoint as a standalone originality claim. The strongest earlier disk record fixes β=1; the classical results supply components of the proof, while the finite weight threshold sequence and strict accessibility count for this kernel were not identified as a covered result.

## value

PASS

The natural weighted differential-evaluation kernel has an exact all-order census of accessible off-diagonal zero fibres, including how many transitions there are, precisely where they occur, and why each threshold excludes the incoming fibre. This is more informative than merely computing the kernel or specializing a fixed-weight zero count; the linear scale of the final transition quantifies when all fibres are available.

The dated certificate retains the supplied scientific assessment, sources and limitations.
