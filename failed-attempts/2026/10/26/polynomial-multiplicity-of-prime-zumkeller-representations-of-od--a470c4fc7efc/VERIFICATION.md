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

For S=2^(t+1)−1 and K=2^t p, the binary expansion of (S−p)/2 uses powers through 2^(t−1); adding K gives S(p+1)/2. Coprime multiplication preserves the partition by the unique divisor factorization. Minimality of t gives K≤2p². For odd n and p∤n, n−K is odd and nonzero modulo p, hence is coprime to M=2pK≤4p³. Uniform Linnik with L=5 gives q≪p^15. For p in (n^δ,2n^δ] and fixed δ<1/15, q+K=o(n) uniformly, so n−q=K(1+2pj), j≥1, has the required coprime multiplier. The product of more than floor(1/δ) distinct primes >n^δ exceeds n, so this number bounds both the number lost to p|n and the number of parameters producing any one z<n. The dyadic prime number theorem then gives the claimed liminf. This is an analytic reconstruction; no enumeration is required.

## originality

FAIL

The earlier indexed d798476efd98 states and proves a strictly stronger lower bound for the identical R(N) and all sufficiently large odd inputs. Its decisive proof was read and checked, not inferred from the title. The frozen finite constant is dominated: the normalized liminf is already infinite for every fixed δ<1 in that result. A different least-prime proof of the weaker frozen inequality is not a distinct new finding.

## value

FAIL

Pointwise abundance in this published additive question is meaningful, but the frozen result does not supply a needed unknown quantitative fact: the prior same-count theorem gives dramatically more representations for the same inputs, including finiteness of odd exceptions. The alternative prime-parameter packing is a correct proof of a weaker conclusion and supplies no asserted effective numerical cutoff, boundary classification, or additional representation constraint. No distinct surviving claim has been established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
