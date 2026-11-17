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

For fixed selected pair {u,v}, each edge-query cut label is the XOR of the two vertex-incidence rows r_u+r_v. Hence support S is shattered iff all 2^s binary vectors appear among pair sums. The all-one pattern forces S to have a two-vertex cover so t<=s+2 active vertices. With s=5 there are at most C(7,2)+7+1=29 distinct pair traces, less than 32; heredity rules out larger S. For s<=4 one classifies allowed small forests by the all-one cover, and enumerates each type via explicit incidence row sums, checking isolated-vertex thresholds. The formula is 1+C(n,2)z+1_{n>=5}C(C(n,2),2)z²+1_{n>=6}(16C(n,4)+30C(n,5))z³+[1_{n>=7}125C(n,5)+1_{n>=8}90C(n,6)]z⁴. Independent direct pair-shore trace enumerations verified every coefficient at n=3..7. The original proof is correct but not original as a mathematical result.

## originality

FAIL

Already on 2026-11-02 the exact all-parameter theorem for fixed-cardinality same-block comparison labels completely classifies shattering by component-size profiles and explicitly treats shore size two, with VC thresholds. Negating every label converts same-block to XOR cut labels and preserves the shattered support set, so it applies to this submission EXACTLY. A further published 2026-11-08 theorem on cardinality-constrained graph cuts gives complete integer-partition shattering polynomial for all k and n; substituting k=2 yields exactly the submitted motif formula after routine enumeration of <=4-edge forests. The omission of identical small-motif wording does not establish originality.

## value

FAIL

The fixed-two-shore support structure is a straightforward, mechanically enumerable family instance of prior all-shore forest/component-size shattering theorems, including earlier size-two VC thresholds. Its four-edge motif multiplicities are a routine finite component-partition table evaluation and do not add a motivated non-implied invariant, boundary or new classification to the established exact all-cardinality result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
