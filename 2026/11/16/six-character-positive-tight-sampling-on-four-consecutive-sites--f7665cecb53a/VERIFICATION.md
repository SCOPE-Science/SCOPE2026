---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS: The tight Gram is equivalent after normalization to vanishing Fourier moments k=1,2,3 and conjugates. Any alleged rule at <=5 nodes can be zero-extended to five distinct 2p-th roots, with P=product(z-z_j). The Laurent polynomials z^-2 P, z^-3P supported in [-3,3] and vanish at nodes; their constant coefficients force e3=e2=0. Express each root as epsilon_j zeta_p^rj: e2=0 gives integer pair-sum coefficients c_r all equal by Phi_p=1+...+z^(p-1), hence pc=((sum epsilon)^2-5)/2 in {-2,2,10}, impossible for p>=7. For six roots, choose three pth roots with angular gaps <pi (residues 0,floor(p/3),ceil(2p/3)); strict positive barycentric weights cancel second moments while antipodal pairing kills first and third. Checked independent positive moment residual for 13 primes through p=103, all small <3e-13; the cyclotomic argument, not enumeration, proves infinite p.

## originality

PASS

PASS best-of-knowledge: published nearby three-site/antipodal-triple cases and four-site odd-prime-11 case do not imply the 2p four-consecutive-site six-node threshold. General roots-of-unity vanishing-sums theory alone constrains possible lengths but not the structured elementary-symmetric pair coefficients; the matched five-node obstruction is the essential novel argument under the inspected sources.

## value

PASS

PASS: Exact minimal positive quadrature cardinality on natural four consecutive cyclic time coordinates and order twice a prime, plus a root-of-unity impossibility stronger than positivity, is a motivated finite-sampling cutoff with a uniform-in-prime constructive optimum. It extends adjacent three-site results rather than recomputing a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
