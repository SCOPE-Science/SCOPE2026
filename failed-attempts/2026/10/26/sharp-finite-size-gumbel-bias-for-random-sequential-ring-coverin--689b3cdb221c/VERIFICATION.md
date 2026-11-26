---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Once an anchor proposes, every site in its footprint is covered even if that attempt is rejected, so the process covers by time t exactly when the independent first-proposal bits have no cyclic run of ell zeros, with zero probability q=e^(-t) per bit. Every allowed cyclic word has a 1 and thus uniquely specifies the trailing-zero states at the labeled anchors; the trace counts each word with exactly its Bernoulli weight. It also gives the correct endpoint values at q=1 and q=0. For the dominant eigenvalue near 1, multiplication of the characteristic equation by Lambda-q telescopes to (1-Lambda)Lambda^ell=(1-q)q^ell. The simple root is analytic at 0 and 1-Lambda=O(q^ell), hence log Lambda=-q^ell+q^(ell+1)+O(q^(2ell)). Scaling the remaining eigenvalues by q gives ell-1 bounded branches tending to the simple nontrivial ell-th roots of unity, so their trace contribution is exponentially negligible in the critical window. Taking q=n^(-1/ell)e^(-x/ell) then exponentiating gives the positive stated term and the O(n^(-1)+n^(-2/ell)) remainder, uniformly on compact x sets. Independent standard-library replay /workspace/branches/e4c9f591-58d4-4535-9a71-eab0b6d16d77/replay_ring_cover.py produced 54 exact rational transfer/enumeration equalities and bounded high-size checks (replay_results.txt in the same directory); they support but do not substitute for the asymptotic proof.

## originality

FAIL

The exact law is the known zero-count event for circular Bernoulli runs, given a standard finite-state representation here. More decisively, the sharp positive correction with its stated uniform remainder is a direct consequence of a published local-dependence Poisson bound applied to the standard nonoverlapping starts of runs of length at least ell. This is coverage by implication, not a claim that the same coefficient is explicitly printed in a particular earlier covering paper.

## value

FAIL

A sharp cluster-induced bias in a cover-time law is a natural diagnostic, and the proof is correct. Here the full surviving increment beyond the leading Gumbel law is however already supplied by the standard empty-run-start Poisson approximation at its exact mean, with an error one order scale below the correction. Evaluating the trace for the established finite run law and expanding that mean are useful exposition but do not supply a distinct scientific result under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
