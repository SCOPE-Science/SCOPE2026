---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Every shuffle root has exactly one one, u_k=0^k1 0^(m-1-k). Necessity and sufficiency of two-copy allocation give L=max(ceil(a/2),a+b-m+1), U=min(a,floor((a+b)/2),m-1) for w=0^a1 0^b1 0^c. Requiring at least r roots subtracts 2(r-1) from each gap and bijects to a single-root word at m-3(r-1), giving H(h)=1+3 binom(h,2). Limit tail P(R/m>t)=3/4(1-3t)^2 on (0,1/3), hence mass 1/4 at zero and density 9/2(1-3t). Independent interleaving-dynamic-program checks agree on small all-word cases.

## originality

FAIL

FAIL: a published 2026-11-02 paper already establishes the SAME exact root interval, every r-tail H(n-3r+3), sharp maximum and its achieving-word multiplicities by the same three-gap contraction. The newer weak limit is the immediate elementary scaling of this prior exact spectrum.

## value

FAIL

FAIL: the only mathematically significant exact invariant—the all-length inverse root distribution—was already fully proved. The asymptotic follows routinely by replacing r with floor(tm)+1 in the earlier closed polynomial count, not a separate substantial new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
