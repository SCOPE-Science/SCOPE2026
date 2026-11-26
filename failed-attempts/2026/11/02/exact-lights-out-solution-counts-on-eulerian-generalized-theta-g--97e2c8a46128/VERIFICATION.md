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

On an oriented path the homogeneous vertex equations give the repeated values a,s_i,a+s_i in characteristic two. When t_0=0, substituting the forced s_i into the terminal equations gives (1+t_2)a=(1+t_2)b=0, with t_2 and t_1 of the same parity. Otherwise a=b, and with S the sum of the free first internal values, the two constraints are (1+t_1)a+S=0 and (1+t_0+t_1)a+S=0. Since t_0>0, the constraint on S has rank one; the difference t_0 a=0 gives the other bit of rank exactly when t_0 is odd. These reductions are necessary and sufficient even for length two and when r=2. Eulerian degree parity gives (I+A)1=1, so all-on solutions are the translate of the kernel with size 2^nullity.

## originality

FAIL

The full nullity law, not just uniqueness, is a direct characteristic-two codimension reading of Edwards et al. (2010), Corollary 2.8 and Theorem 4.3 on winnable colorings of generalized theta graphs. For a square matrix the codimension of the winnable-color space is the nullity. That equivalence supplies the positive-nullity cases even though the earlier paper emphasizes winnability rather than the count of press subsets.

## value

FAIL

The closed form is a lucid specialization and all-on solution counts are natural, but here both are obtained from already explicit compatibility equations by counting their independent constraints over F_2. The examples and cycle boundary do not add a scientifically distinct result to that specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
