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

A factor 1−p_j+p_j exp(−2πit a_j) can vanish only when p_j=1/2, and then exactly at t a_j∈Z+1/2. With u=qt, the resulting nonzero zero differences are rational and have valuations −s−1 for s among the represented fair scales. The valuation condition alone is not sufficient on all rationals; the proof uses it only for the upper bound until it verifies exact half-integrality on the constructed dyadic family. After translating a family to include zero, at the least permitted valuation its frequencies occupy at most two residue classes in the localization of Z at 2; within either class the least valuation is removed. Induction gives 2^r, covering also r=0 and excluding any infinite orthogonal family. For the proposed family the largest differing scale s gives an odd numerator over 2^(s+1); multiplying by a fair step integer of valuation s gives a half-integer, establishing both distinctness and orthogonality. Changing q adds the common valuation of a positive rational scale factor to all step valuations. Positivity of masses makes the dimension the number of distinct subset sums: representatives of distinct fair valuations give 2^r distinct sums by their unique least valuation in each nonzero signed difference. When r<m, a remaining positive step strictly adds support points by translation; when r=m, there are exactly 2^r atoms and a basis. The uploader's finite rational graph checker was read, not executed; it corroborates selected instances, not the general proof.

## originality

FAIL

The capacity and the specified optimizer are mechanically obtained from the established prime-power gcd-graph bound and the finite homogeneous-tree digit construction. The exact reduction is as follows. If some factor is fair, put M=lcm{2n_j : j fair}, N=ν₂(M), and I={N−s−1:s∈S}. Translate a real orthogonal family to contain zero. For the normalized frequencies u=qλ we then have Mu∈Z. Project Mu modulo 2^N. Distinct elements remain distinct because every nonzero difference has valuation in I⊂{0,…,N−1}. Their residues form a clique of the gcd-graph X_(2^N)(D), D={2^i:i∈I}. Conversely any clique in this graph lifts by a↦a/(q2^N): an edge of valuation i yields a normalized frequency difference with reduced denominator 2^(N−i)=2^(s+1), so a fair factor at s annihilates it exactly, regardless of its odd step multiplier. Thus the two clique numbers are equal; this is not an assumption that all rational differences of the right valuation are zeros. Bašić–Ilić's §5 bound gives at most ∏_(d∈D) f(2^N/d)=2^r, where f is least prime divisor. Fan–Fan–Shi's §2.6 digit construction with free digits at I and all others zero gives 2^r residues; two distinct such residues differ first at an index of I. Its lift is exactly the proposed frequency family. If no factor is fair, there are no zeros. Biases require no extension of either prior result because their Fourier factors never vanish. The application can be correct and useful pedagogically without constituting a distinct exact discovery under this audit standard.

## value

FAIL

The maximum size of an incomplete exponential family is a meaningful question, but in this commensurable setting the asserted exact invariant and given optimizer are mechanically obtained from the classical graph bound, digit construction and the exact dyadic projection. The biases and completeness corollary do not leave an independently valuable new extremal claim. The proof is a useful elementary presentation of an application, not a separate new invariant determination at the required standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
