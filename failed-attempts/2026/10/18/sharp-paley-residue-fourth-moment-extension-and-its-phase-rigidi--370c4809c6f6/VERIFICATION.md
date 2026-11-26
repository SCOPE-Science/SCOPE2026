---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Paley autocorrelation count is (q-3)/4 on each nonzero difference, by cancellation of the two linear character sums and the squarefree quadratic sum -1. Additive orthogonality gives q k^{-4} times the autocorrelation energy under the stated target counting and source 1/k normalizations. Subtracting the fiber Cauchy–Schwarz identities and the variance of |f|^2 gives the two exact nonnegative terms, with sharp constant q(q^2-2q+5)/(q-1)^3 and constant-function witness. For q=3 the support is a singleton; q=7 has singleton nonzero difference fibers, leaving all phases of flat-modulus inputs unconstrained. Otherwise equality gives flat modulus and a well-defined phase ratio c_d on each nonzero difference. A point common to D,D+a,D+a+b gives c_(a+b)=c_a c_b; inversion covers the zero cases. Hasse's squarefree cubic bound gives triple intersections at least (q-15-2 sqrt(q))/8, positive from q=27, valid over extensions as well as primes. The exact reviewer replay `python3 /workspace/review-evidence/3.py` checks all 306 and 462 distinct ordered shift pairs at q=19,23 (minimum one in each), and derives and checks the order-11 normalized torus relation determinant -11. Its index is 11; 11 distinct normalized character restrictions attain equality. Finally d↦psi(ad) exhausts the additive dual: the parameter map is injective by surjectivity of multiplication by each nonzero a and nontriviality of psi, and the dual has order q. D-D=F_q proves uniqueness up to the specified scalar. The finite replay does not verify Hasse's theorem or prove the all-order result; the analytic steps do. Frozen artifacts/verify.py inspected, not run.

## originality

FAIL

Two checked catalogue statements together cover the norm, deficit and prime-field rigidity. For nonprime fields the earlier Paley proof's only prime-specific character step is the parametrization of the additive dual. The same squarefree cubic Hasse–Weil bound and the same numerical positivity check work verbatim from q=27, the first admissible extension order; the standard additive dual parametrization finishes. No new incidence or rigidity lemma is needed. This is mathematical coverage by exact specialization and direct implication, not a priority adjudication.

## value

FAIL

Exact rigidity is a meaningful mathematical question, but the submitted additions to the checked results consist of putting the known deficit into a termwise square form and applying the same rigidity argument with the standard additive dual for extension fields. The finite certificates repeat known cases and no further quantitative or structural conclusion survives as a separately useful new claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
