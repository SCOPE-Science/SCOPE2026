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

The difference walk has eigenvalues (1−p+p cos θ_k)². The Fourier Dirichlet solution with value zero at 0 has numerator 1−cos(xθ_k); at separation one it cancels the corresponding factor in 1−λ_k. Aliasing the absolutely convergent Poisson series for (2−p+p cos θ)^(-1) onto multiples of n gives the signed parity factor and the k=0 subtraction −1/(2p). Summands 1/(2p−a_k p²) have positive second derivative. At p↓0 the mean diverges; at p=1 for even n parity is invariant and rules out meeting. For odd n, division by 2 mod n maps the relative walk to a half-lazy nearest-neighbor walk starting at distance coordinate (n±1)/2, with mean 2x(n−x)=(n²−1)/2. The general interior bound at p=2/3 beats this for odd n≥5; the explicit triangle mean does so for n=3. Uniformly near p₀=2/3 the closed form has exponentially small parity error (also after differentiation), giving H′=nG′+1/(2p²)+O(n²ρ^n). The derivative sign brackets the optimizer, and G″(p₀)=81√3/16 gives the stated displacement and mean with their remainders. The event T≥t is determined before tick t and independent of that tick's move count; summing its expected reward gives 2pH. Differentiating then proves strict increase and the unattained limit n−1. Independent checks solved the killed chain rationally for 3≤n≤8 at four rational probabilities each and checked n(2/3−p_n) towards 2√3/27 by derivative bisection for n through 1920. Replay and output: /workspace/branches/47465195-6b34-4c40-b915-ab68e89b7c95/independent_check.py and independent_check.log in that directory. The frozen CHECK.py was read, not run.

## originality

PASS

Pass for the fixed-adjacent all-size optimization with explicit finite-size correction and opposing move-count objective, not for the relative-chain/spectral machinery, generic convexity method, or triangle optimizer. The strongest available Fourier comparison averages over initial separations. The closest exact cycle-strategy source, Alpern (1995), and the cited Alpern–Gal chapter remain material priority risks because their decisive pages were not recovered independently. The frozen Alpern–Zeng characterization is imprecise: its cited triangle optima are for three-agent objectives, and it points to Alpern (1995), §5 for the two-agent rendezvous problem. The independent evidence supports the distinct quantitative finding; it does not certify historical priority.

## value

PASS

Fixed adjacent start is a natural local benchmark, distinct from a uniform-start quadratic-time search. The exact parity-sensitive formula explains an order-n optimized time and supplies a finite-size correction; the strictly conflicting movement objective shows why optimal calendar time does not optimize actual activity. The joint quantitative comparison is useful beyond the routine spectral reduction and the small-cycle examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
