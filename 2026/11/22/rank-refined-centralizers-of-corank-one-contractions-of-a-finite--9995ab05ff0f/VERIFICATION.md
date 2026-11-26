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

The n-1 image-rank layer has exactly one zero increment and start 1 or 2; reflecting conjugates the two start classes. For a=a_{n,i}, f([i]) must lie in [i]. For j>i the exact commuting equation is a(f(j))=f(j-1). If f(i)<i, the only preimage of that value is itself and the right tail is constant; for h prefix rises there are i-1-h allowable endpoints below i, giving (i-1)binom(i-2,h). If f(i)=i, the right tail stays there for an arbitrary number of flat steps, then advances by one at every step, because higher values have singleton preimages. Every binary prefix ending at i and every such tail is allowed. This yields both polynomial branches, including i=1 and the idempotent endpoint. Writing S_m=1+z+...+z^m, (1+z)S_{m-1}-S_m=z+...+z^{m-1}; substituting proves the difference factor, with contiguous positive support up through rank n-1 and the identity's top coefficient unchanged. For the weak limit the two class weights are in ratio (i-1):2(n-i+1); the scaled binomial parts concentrate at theta/2 by their O(n) variance and the independent discrete uniform in the second class converges to Uniform[0,1-theta]. At theta=0 the first weight vanishes, including sequences taking i=1; at theta=1 both supports collapse to 1/2. Only the endpoint i=n-1 is idempotent, since applying a twice to i+2 differs for all other i. For n=2 both corank-one maps are constants, with z+z^2 as stated.

## originality

PASS

Pass for the nonidempotent corank-one rank profile as a family, the strict coefficient ordering and its conditional mixed law. The endpoint clamp overlap is exact and not new; its same-day weighted statement was explicitly compared. Normal forms, unconditioned rank counts and the degenerate single-chain case are not the distinct contribution.

## value

PASS

The first nontrivial rank layer below the units of a standard finite-chain monoid is natural, and it admits a complete, explicit distribution rather than just a count. The constant versus delayed advancing tail yields strict monotonicity below the identity rank and a nontrivial atom beside a continuum for interior scaling parameters. Neither phenomenon follows from the sizes of the idempotent centralizers alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
