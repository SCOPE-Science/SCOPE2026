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

For the expressly named Becker–Baraviera/Reyes shift, Reyes v1 confirms the full transition: after a 1 the next symbol is 1 at or below the threshold and 0 above it (after a 0 either is allowed). The frozen description should spell out the above-threshold branch; treating it as a free choice would instead allow any finite word after a sufficiently long prefix of ones, giving the full shift after closure. For the named system Reyes's Theorems C–D give the entropy and uniqueness, with equality to the coded shift at k=1 and invariant-measure support on the coded subsystem for k≥2. Junction sampling gives the regenerative law q_m=2^(−m), for which entropy per codeword is 2 log 2 and mean length is 2(k+1); the decoded stationary suspension attains the required entropy. The block covering a typical time is size-biased, not part of the junction iid assertion. The iid tail is 2^(−r). A deterministic index sandwich around N/[2(k+1)] via the renewal strong law, without a spurious independence assumption between count and lengths, gives the stated o(1) law because N2^(−r_N) stays bounded. Taking floors away from the lattice phase boundaries gives the subsequential formula. Dyadic tail estimates and monotonic interpolation give the almost-sure logarithmic block maximum. The within-block potential goes from 0 to −km and back, so its difference at times 0 and n is S_n. The initial potential has all stationary moments; for the maximum the completed and all intersecting block maxima sandwich the pathwise depth and have the same asymptotic order and coefficient. This does not assert that the terminal partial block's own length is o(log N). Uniform second moments give zero variance per time.

## originality

FAIL

The prior exact construction in Resultary 40d60d854aab already identifies the same phase-resolved fair Bernoulli-marker process, its Palm law, and the explicit within-block height coboundary with bounded moments and zero variance rate. The apparent new maxima reduce to the classical longest pure run for those iid markers: Gordon–Schilling–Waterman Theorem 1 gives the same lattice weak profile after the deterministic time rescaling and length shift, and the almost-sure logarithmic growth is classical. The sharp discrepancy maximum is the same maximum multiplied by the already-known within-block height factor k, with endpoint effects controlled at smaller scale for the maximum. This is concrete prior implication even though the earlier Resultary Finding does not print the maximum formulas.

## value

FAIL

The contrast between bounded moments and growing pathwise maxima is a useful exposition of this process, but the previously established exact Bernoulli conjugacy and block height reduce both maxima to the classical fair-coin run maximum by an affine scaling and elementary boundary trimming. The frozen result supplies no new extremal invariant or estimate beyond those direct consequences. Removing the already-recorded law and moment statements does not leave a scientifically distinct valuable result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
