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

For the probability-area orthonormal basis, the associated Legendre amplitude factor squared is (2ℓ+1)(ℓ−|m|)!/(ℓ+|m|)!. Equatorial reflection separates the two channels; extracting the constant or linear term from Rodrigues' polynomial gives the two positive factorial weights with the recorded derivative scaling. DFT orthogonality groups columns by (m mod M, parity of ℓ+m); each block has one nonzero eigenvalue equal to its squared column norms summed, with multiplicities counted by blocks. For odd M the two step-two runs give min(M,ℓ+1)+min(M,ℓ) blocks; for even M congruence already fixes parity so the rank is min(M,2ℓ+1). This includes M=1,2 and yields the stated minimum within regular grids. The value weights grow strictly with |m| in steps of two while derivative weights decrease; the central pair is equal by the Legendre equation and the endpoint ratio is (ℓ+1)/2. For ℓ=1 both extrema are 3/2. This is the squared, not unsquared, operator condition number. An irregular-grid minimum is not asserted: ℓ+1 sites distinct modulo π give two Vandermonde systems, even for odd ℓ. The recorded Python check was inspected, not executed; the analytic checks do not depend on its finite output. An independent residue count at M=ℓ+1 for ℓ=1 through 5 gave ranks 2,5,4,9,6.

## originality

PASS

The supported contribution is the complete finite-grid alias spectrum and sharp normalized conditioning of this particular scalar first-jet observation map. Legendre parity and DFT aliasing are established ingredients, not new claims. The closest available statements have different measured channels, eigenspaces or sites and do not establish the combined theorem. The conclusion is bounded by the accessible evidence, not a priority guarantee.

## value

PASS

The pure degree is a natural eigenspace and the two observations form its equatorial Cauchy data. A sharp site threshold distinguishes near-dimension-optimal odd grids from even grids with twice as many required sites asymptotically; the full spectrum identifies exactly what a smaller grid loses. The exact lower frame bound and its normalization quantify noise amplification and explain why oversampling on a full-rank regular grid does not improve the condition number. This goes beyond checking dimensions or evaluating a single harmonic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
