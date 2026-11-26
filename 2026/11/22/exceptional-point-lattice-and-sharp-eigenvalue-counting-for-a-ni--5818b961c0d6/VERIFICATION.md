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

The compact shift has ||S^m||=1/m!, and the functional coefficients are square summable with zero coefficient at e₀, so F is bounded, rank one and square-zero. The positive-coordinate equations give injectivity. Orthogonality to the range implies y₁=0 and yₙ₊₁=−conj(α)y₀ for all n≥1; square summability forces y=0. Compactness on the infinite-dimensional space implies the dense range is not closed and puts zero in the Fredholm essential spectrum. Summing the resolvent matrix element gives e^(1/λ)−1−1/λ; the rank-one inverse formula supplies precisely its reciprocal level set and one-dimensional eigenspaces. Since R′=−R², the rank-one resolvent difference has trace D′/D; the local Riesz projection has rank equal to the zero order. The critical points of e^z−1−z are 2πik with second derivative one. Only k≠0 can occur at the permitted levels, each level produces just one double zero, and reciprocation gives the claimed sign and coefficient of the square-root splitting. For large roots e^Re(z)=|z+1+β| forces Re(z)=log|z|+O(1/|z|); the argument localizes every large root to the indicated disk indexed by j. The principal-log fixed-point map has derivative O(1/|j|) throughout each large-index disk and maps it into itself; a root there uses that same j because its principal argument stays near sign(j)π/2. Thus all but finitely many roots are exhausted. The two |z_j|=2π|j|+O(1) tails give the bounded counting error; the difference from the reference two-sided p-series is uniformly summable near p=1. The Schatten threshold is unchanged by a finite-rank perturbation, including for 0<p<1. Real positive β gives one positive and one negative real root by convexity; equality in the positive-coefficient power-series triangle inequality forces equal phases for the z² and z³ terms, hence positive real z, proving the unique maximum-modulus eigenvalue. The positive root has e^z=β(1+o(1)) and the negative root is −1−β+o(1) as β→+∞. Independently checked tail roots by the log fixed-point equation; finite diagnostics do not certify infinite exhaustion.

## originality

PASS

Pass for the concrete square-zero truncation and its operator spectral classification, particularly the exact coupling lattice with algebraic defect and the resulting contrast with the untruncated shift example. Rank-one resolvents, scalar Lambert W ramification and all-branch asymptotics are antecedents. In particular the scalar two-tail estimate and 1/π counting coefficient are direct corollaries of classical Lambert asymptotics once this specific characteristic function is found, not independent new scalar asymptotic theorems.

## value

PASS

Imposing square-zero on the classical factorial-shift rank-one example by removing its zeroth coefficient is a motivated structural change, not an arbitrary parameter slice. The exact defective coupling lattice accumulating at zero distinguishes a concrete infinite-dimensional perturbation from the untruncated example, which instead has an exceptional quasinilpotent coupling. This gives a calculable test case for rank-one multiplicity and weak-coupling questions: the same family exhibits isolated defective eigenvalues, a membership/counting threshold and two inequivalent real weak-coupling scales. The value rests on that operator construction and exact classification, not on rederiving Lambert W asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
