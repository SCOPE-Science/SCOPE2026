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

For a0≠0 the linearization Δq(A) is separable and its roots form a d-dimensional Fq-space V. Its nonzero roots modulo the scalar subgroup μℓ correspond to the roots of G, via α↦α^ℓ, with the q-Frobenius action preserved. If A has a proper nonconstant factor D, Δq(D) has a proper nonzero root subspace in V (composition of linearizations gives Δq(A)), invariant under Frobenius, so that action cannot be transitive. If A is irreducible, the Frobenius action makes V a one-dimensional module over Fq[T]/(A); transitivity on V×/μℓ means that a root β of A has ord(β^ℓ)=n. For β=Γ^e, the joint conditions are gcd(e,n)=1 and e≡r mod q−1, by the norm formula and the constant's sign (-1)^d. Primes dividing both n and q−1 impose gcd(r,h)=1, while each other prime divisor of n forbids one class among the U possible progression indices; their square-free product divides U, so complete CRT cycles give the stated product. Every qualifying β has degree d since n≥U>q^(d−1), and its norm is constant over its d conjugates. Summing and using U≡d mod q−1 verifies the total and all-constants criterion, including q=2 (r=0 and h=1) and the empty product cases. Zero constant gives a reducible polynomial because n>1. Fresh direct tests of every polynomial in 12 small systems (268 polynomials including three systems over F4) passed, using gcds against X^(q^k)−X for all k≤n/2 rather than the cyclic-exponent formula. Replay: python /workspace/replay_frozen.py 5. These tests are finite corroboration; no formal proof check or expert attestation is claimed.

## originality

PASS

Pass is for the positive-divisor family with equal coefficient field and Frobenius base, refined by the exact fixed constant. The order characterization, unrestricted sum, and classical primitive-norm special case are not new. The inspected stronger root characterization leaves the distribution across individual constants to be worked out; the closest other sources treat a different order condition or different counting constraints. No distinct indexed record or inspected primary result supplying the full fixed-constant refinement was established.

## value

PASS

The constant is a natural coefficient constraint (equivalently a base-field norm of the ordinary root). The exact distribution determines when a specified constant can be realized in this sparse irreducible family and how many choices result, with a sharp all-constants threshold including nonprimitive quotient regimes. This resolves a substantive existence/counting question not answered by the unrestricted positive count. Value is for the uniform all-parameter refinement, not the CRT technique or isolated examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
