---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the uniquely specified thin-polar direction, the derivative of the squared Frobenius objective along the update ray vanishes at sum(s_i)/r, which is positive at nonzero rank r. The new singular values are the absolute centered deviations, including zeros before the rank is recomputed. Rank one vanishes, and rank two gives an equal pair or zero. Three centered signed numbers sum to zero, so when all three are nonzero the largest absolute deviation is the sum of the other two. On (a,at,a(1-t)) the three deviations in absolute value and units of a are 1/3, |t-2/3|, t-1/3; sorting gives exactly the two stated ratios and scale factors, including t=1/2 and the equal rank-two pair at t=2/3. The fixed equation 3t^2-t-1=0 yields the asymmetric ratio and q=t-1/3; the spectrum never loses rank and the objective scales by q^(2k). Independent replay: python3 /workspace/branches/replay_exact_audit.py 2 verified the exact Q(sqrt(13)) similarity of the spectra and checked 680 integer-spectrum starts with rational arithmetic. The supplied CHECK.py was read but not executed.

## originality

FAIL

Distinct Resultary record 748c30f86df2 covers the principal rank-two/rank-three termination boundary and stronger arbitrary-rank and rectangular cases for the same exact-line-search map. Nuclear scaling only rescales the ray: at the isotropic quadratic G=lambda*E, multiplying the thin-polar direction by lambda*sum(s_i) divides the minimizing coefficient by that factor, leaving the iterate unchanged, even after rank loss. That record derives mean subtraction explicitly and gives the t=1/2 ray. From its general recursion, the sum-zero identity and sorting the three displayed centered deviations give the projective map without any new dynamical premise, and solving one quadratic gives the asymmetric witness. The witness is not quoted as literally printed there; it is an immediate corollary of that recurrence. There is demonstrable coverage and no sufficiently distinct remainder; no first-discovery or chronology claim is made from catalogue dates.

## value

FAIL

The dimension barrier is an instructive idealized optimizer benchmark, but the broader equivalent theorem already supplies that barrier and explicit nontermination. After subtracting that coverage, the claimed increment is just sorting three given absolute deviations and solving the resulting fixed-ratio quadratic. No separate termination classification of the projective trajectories, worst-case rate, or other independent implication is proved. That routine explicit specialization does not establish distinct mathematical value under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
