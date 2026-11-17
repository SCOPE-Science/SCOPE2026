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
# Mathematical verification notes

The proof is self-contained apart from the classical periodic Wirtinger inequality, which yields the signed planar isoperimetric inequality. All inputs are absolutely continuous, so the controlled integral is an ordinary Lebesgue integral against \(\dot X\). The first two state components equal the driver components. The third state is its signed area.

For the upper estimate, reflecting the open curve through its endpoint line and then reversing the reflected segment makes a closed curve with perimeter at most \(2B\) and signed area \(2F(X)\). The closed-curve area estimate gives \(|F(X)|\le B^2/(2\pi)\), including non-simple drivers. The reference path compatible with the adversarial transcript has length \(2B/\pi\), strictly below \(B\).

The gap strategy retains an interval containing no reported internal sampling time after every query. The interval is nonempty after any finite number of queries; it need not have any lower width bound uniform in the query budget. Both semicircles over that gap use length exactly \(B\), have equal endpoints and all sampled values, and give \(\pm B^2/(2\pi)\) terminal outputs. Deterministic policies therefore follow the same query and stopping history on both.

Symbolic consistency: write \(R=B/\pi\), \(X(u)=(R(1-\cos\pi u),R\sin\pi u)\). Its derivative has constant length \(\pi R\) over \(u\in[0,1]\), hence its path length is \(B\). Direct integration gives \(\tfrac12\int_0^1 X\wedge X'\,du=-\pi R^2/2=-B^2/(2\pi)\). The reflected semicircle has the opposite sign.

Limitations: no claim for randomized sampling, derivative observations, time-continuous observation, infinite query budgets, or generic nonlinear CDEs. The proof is analytical; symbolic examples only check a finite algebraic identity. Independent audit has not been performed.
