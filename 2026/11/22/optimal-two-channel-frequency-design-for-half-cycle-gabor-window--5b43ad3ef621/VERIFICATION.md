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

Independently reconstructed the Fourier optimization in RESULT.md lines 49–95. Summing over all translations annihilates the off-diagonal Fourier entries. The geometric sum gives R(0)=m, R(k)=0 at other even residues, and R(k)=1/(m sin²(πk/(2m))) on odd residues. Thus an even gap leaves an even Fourier index uncovered for m≥3; an odd gap covers every index. Swap weights by j→s−j and average, which cannot raise the maximum or lower the minimum. For an odd gap the equal-power maximum is m+R(s) at the two channel labels; their larger eigenvalue grows strictly under imbalance because R(s)<m (the geometric sum is strict off zero). The remaining eigenvalues consist of two odd-residue lists omitting s and −s, respectively. At odd m the unique smallest response at m disappears from both lists only at s=m; the next responses are at m±2. At even m the two minima at m±1 cannot both disappear. Minimizing the maximum and maximizing the minimum therefore singles out the asserted gaps and bounds. At m=2 the even gap has spectrum (2w0,2w1,2,2), while the odd gaps have equal-power ratio 3. Substitution and the cosine Taylor expansion reproduce both constants beyond m². The subsection heading 'for each gap' applies to spanning gaps for strictness; all weights on a singular gap have infinite ratio, which does not affect global uniqueness. The 85,546 assertions are reported source diagnostics, not an independent run or the all-m proof.

## originality

PASS

The supported distinct result is the complete parity-sensitive half-cycle-boxcar gap and power optimum, not the general Fourier reduction or equal-power symmetry. None of the strongest inspected statements includes this window and solves that optimization.

## value

PASS

The problem is a natural minimal two-channel design at fixed window and full translations. The exact parity classification is actionable: in even half-lengths at least four the intuitive antipodal design fails to span, whereas the nearest odd gaps are uniquely best up to reversal. Even optimally weighted, the squared condition number grows quadratically; the result separates correct channel placement from intrinsic ill-conditioning. No broader window or sensing-model claims are needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
