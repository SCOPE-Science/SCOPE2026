---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Mathematical verification
The proof is universal and exact: the defining inequalities for h-perfect graphs imply competing clique barriers \(1/(s+\sqrt s)\) and odd-cycle barriers \((1-1/\sqrt\ell)/2\). Their strict monotonicity proves that only maximum cliques and, exceptionally for clique number two, five-cycles can be active at the uniform center. Equality forces the coordinates on each active support. The five-cycle facet assertion is established by explicit affinely independent stable-set vertices.

## Reproduction
Run `python verify.py` in this directory with Python 3, NumPy and SciPy. Successful output:

`HPERFECT_EUCLIDEAN_INBALL_CHECKS_PASSED profiles= 14 cliques= 169 odd_cycles= 15 coordinates= 85`

The checker solves finite halfspace Chebyshev-center linear programs and tests feasibility of the claimed uniform balls. These profiles include both short and long odd cycles, graphs with maximum cliques, and disjoint unions.

## Limits
The finite tests do not establish the general theorem or verify the h-perfect property of arbitrary input graphs. They are complementary to the symbolic argument. Originality remains provisional pending an independent literature review, and no external independent mathematical audit has been performed.
