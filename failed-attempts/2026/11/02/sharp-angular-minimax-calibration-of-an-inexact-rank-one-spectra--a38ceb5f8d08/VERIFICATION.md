---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In the Ritz basis the congruence has diagonal entries θ and σ=1+(κ−1)r, r=sin²φ, and determinant κθ/ρ, ρ=κ−(κ−1)r. Its eigenvalue ratio is strictly ordered by F=(θ+σ)²ρ/(κθ). For fixed r the unique minimum is θ=σ; apply this lower bound at R=sin²Φ. At θ=σ(R), the derivative in r has the sign of 2ρ−θ−σ, positive for r<R≤1/2 because ρ(r)≥θ≥σ(r). This attains the endpoint lower bound, including the singleton Φ=0 and the derivative-zero endpoint at Φ=π/4. The endpoint matrix has equal diagonals and squared correlation z/(1+z), which gives the exact condition number, interpolating from 1 to κ. For θ=1, subtracting the unpreconditioned invariant with denominators cleared gives (κ−1)²(1−r)((κ−1)r²+3r−1), whose unique positive root yields the strict cutoff. Its angular scale is κ^(−1/4); z is comparable to κΦ² at large κ on the admitted range and tends to c² for sqrt(κ)Φ→c. These are exact-arithmetic statements in dimension two.

## originality

FAIL

The October 12 Resultary result supplies the full pointwise loss for every rank-one multiplier and the same sharp minimax value and angular scales for a fixed multiplier. A fixed Rayleigh-normalized target is a different family, so equating the two optimizations by substitution alone would be wrong. Nevertheless the frozen optimum follows directly by pointwise domination from the earlier theorem, and the remaining cutoff follows by substitution in its exact loss formula. There is no independent performance law left over.

## value

FAIL

The robustness problem and sharp angle scales are useful, but the earlier result already gives the performance law and those scales. The different parameterization adds a short domination corollary and a cutoff obtained by direct substitution into the known joint formula, rather than a distinct invariant requiring a new argument of independent use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
