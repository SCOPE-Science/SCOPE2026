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

Eliminating the conserved free enzymes and setting y_i=X_i+C_i, z_i=C_i gives the stated Jacobian. Binding supplies all z directions, and catalysis together with binding supplies all zero-sum y directions, so sum(y)=0 is the full remaining stoichiometric tangent. The pool incidence Gram matrix is positive semidefinite even for unequal or interleaved pools. The eigenvector equation yields lambda^2+eta*lambda+alpha*k_c*zeta=0, with eta>=alpha+h and zeta in the unit disk centered at 1. For a nonreal eigenvalue with real part u>=0, the disk inequality forces (2u+eta)^2<=2*alpha*k_c, contradicted by (alpha+h)^2>=4*alpha*h>2*alpha*k_c. The real case only permits zero; its eigenvector has z=t*1 and sum(y)=t*[n*(alpha+h)+beta*sum_g(m_g^2)]/alpha, excluding any nonzero such vector in the tangent. Smooth linearization then gives local exponential stability and rules out a Hopf bifurcation at an equilibrium in this positive balanced family. The supporting checker was inspected, not executed: it checks the Jacobian at finite rational sample points, not stability. The analytical argument supplies the universal certificate without relying on those samples.

## originality

PASS

The closest checked work proves unrestricted-assignment steady-state results, a stronger convergence theorem in the no-sharing case, and selected shared-pool instabilities. None gives stability simultaneously for every sharing partition at positive equal-rate balanced states. The exact indexed match is the target itself, not an independent precedent. The other close catalogue result studies a different parameter regime and a Hopf-threshold shift. This is a bounded determination of coverage, not proof of absolute priority.

## value

PASS

Shared-enzyme cycles can lose stability, and arbitrary sharing can break the symmetry necessary for Fourier-mode decoupling. The result gives a precise, easily tested boundary within the full dynamical model where no choice of partition can trigger a local loss of stability. The argument isolates why the pool coupling is harmless at balance without claiming global behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
