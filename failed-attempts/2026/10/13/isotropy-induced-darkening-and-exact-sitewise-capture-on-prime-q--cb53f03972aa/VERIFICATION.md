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

For loss -i gamma |o><o| with gamma>0, the detector cyclic subspace is the orthogonal sum of spans of P_E o. Its orthogonal complement has unitary evolution; on the cyclic subspace an eigenvector with real eigenvalue would be an H-eigenvector perpendicular to o, a contradiction. Strict decay there holds even with Jordan blocks. The coefficient identity for the prime cyclotomic polynomial gives the only cosine relation (1,2,...,2), so a rational relation of coefficient sum zero is identically zero. Applied to the energy difference this gives exactly signed-coordinate orbits at unequal rational couplings and signed-permutation orbits at isotropy. For real ratios each unwanted equality has one of the displayed ratios. In each regime the bright projector is independently identified with the group-averaging projector: in Fourier space each orbit has one cyclic direction since the detector coefficients are constant and nonzero. In site space the diagonal of that projector is the reciprocal of the orbit size, proving both sitewise laws and the orbit counts for the ranks (including p=3). Finite-time continuity follows from the matrix exponential; the function of sites, not every individual site's value, jumps in the infinite-time limit. Read VERIFICATION.md and the packaged verification/verify_prime_torus.py and requirements.txt; its exact energy grouping and numerical Fourier/propagation serve distinct purposes and were not rerun. Independent exact rational Krylov projection on the site Hamiltonian checked every site and the rank for p=3,5,7 and weight pairs (1,1),(2,1),(3,2),(4,7); replay: python3 /workspace/reproductions/prime_torus_krylov.py (SymPy). This finite check is not the general proof.

## originality

FAIL

Material equivalent coverage in a distinct Resultary record: the November square specialization for p>=5 gives both sitewise laws, both bright ranks, and the same rational collision criterion with the same loss model, as part of a more general rectangular-prime result. This is an overlap in the published corpus, not evidence that the later record had priority or that this record depended on it. Neither the p=3 endpoint (the two cosine labels are 2 and -1, giving only exchange at ratio 1) nor the extension away from finitely many real resonances (solve each affine two-label energy equality, then reuse the unchanged blocks) is a material independent remainder. There is no claim in the frozen record that resolves the profiles at additional irrational resonances.

## value

PASS

The full analytic sitewise capture theorem is a useful structural result for this natural model: the ordered-to-unordered energy grouping explains an explicit sink-invisible sector and a discontinuity in eventual capture that is not a finite-time transition effect. The ranks also predict the capture for maximally mixed sources. This is scientific utility of the law itself, not incremental value established over the overlapping publication. The minor uncovered extensions alone do not justify an independent repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
