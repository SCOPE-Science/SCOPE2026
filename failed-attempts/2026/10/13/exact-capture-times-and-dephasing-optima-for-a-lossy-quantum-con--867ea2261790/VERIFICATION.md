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

The loss identity is S'=-kappa*rho_00. If a positive trajectory had a positive limiting trace, a nonzero positive accumulation state would evolve at constant trace. Positivity eliminates its hub row and column, and g!=0 then forces the leaf block to annihilate the all-ones vector. Its leaf Hamiltonian consequently commutes with it, and the leaf off-diagonals decay at rate delta. In the limit the diagonal block still annihilates the all-ones vector, so it is zero, a contradiction to the constant positive trace. Since positive matrices linearly span the full matrix space, finite-dimensional semigroup convergence on positive inputs gives negative spectral abscissa; no dilation is needed. Permutation symmetry allows a uniform mixture for the survival trace of a localized input. In the reduced system q=(kappa+delta)/2 and Delta=epsilon-(n-1)h. The integrated hub population, leaf off-diagonal and imaginary hub–leaf coherence are 1/kappa, -1/(n*delta), -1/(2*g*n), respectively; the real coherence integral is Delta/q times the imaginary one. Substitution into the imaginary-coherence equation yields exactly the stated T. At fixed kappa, T'' in delta is 2(n-1)/delta^3+2 Delta^2/[g^2(kappa+delta)^3]>0 and T diverges at both endpoints. At resonance the rate optimization separates; at zero dephasing the norm squared of the invariant dark projection is 1-1/n, while the bright–hub sector decays because g!=0. Twelve independently assembled full Liouvillian inversions for n=2,3,4,5,7 agreed to maximum absolute error 1.07e-14, and bounded direct minimizations agreed with the resonant rates and a detuned stationarity root. Replay: python3 /workspace/branches/304c9f9d-a4a0-4167-9ad5-4d3b39a27142/record5_full_liouvillian_check.py (NumPy and SciPy); these finite checks do not prove the continuous-domain claim.

## originality

FAIL

The physical dynamics have a different local dephasing convention, but the claimed integrated observable reduces exactly to the previously evaluated uniform fully connected mean-time observable of Alterman, Berman and Strauch. The reduction is a rescaling of the two integrated hub–leaf coherences with the corresponding hopping and detuning substitutions, valid at every declared parameter point. The optimizers in the Finding follow by elementary differentiation of that implied formula. There is no claim of full time-domain equivalence.

## value

FAIL

The model and observable make a natural benchmark, but the claimed exact mean is mechanically obtainable from the published uniform-noise formula by a coherence/rate conversion, and the reported optima and dark endpoint are elementary consequences. The finding supplies no additional time-dependent observable, structural threshold, or independently useful unknown exact fact beyond this conversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
