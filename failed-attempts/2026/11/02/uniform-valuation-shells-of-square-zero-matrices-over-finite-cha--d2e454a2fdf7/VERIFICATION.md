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

A primitive square-zero 2×2 matrix Y reduces to rank one. For any lift v of a vector outside the residue kernel, (Yv,v) is a local basis and Y has the square-zero Jordan block in it. For a length-k quotient the invertible stabilizer has size (q^k−q^{k−1})q^k; dividing the GL₂ size gives (q²−1)q^{2k−2}, including k=1 and characteristic two. At shallow valuation s, the primitive solutions over the length-(d−2s) quotient have q^{4s} lifts into the length-(d−s) quotient, which parametrizes the shell bijectively. The deep ideal has q^{floor(d/2)} elements and every matrix over it squares to zero. The deep mass relative to one shallow shell is 1/(q²−1) or q²/(q²−1) by parity; the normalized deep mass vanishes and the equal-weight shallow mesh tends to uniform on [0,1/2]. Independent direct coefficientwise enumeration over F_q[t]/(t^d) at (q,d)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2) agreed, e.g. exact valuation profiles [48,48,15,1] for (2,3) and [192,192,240,15,1] for (2,4). This finite check is restricted to equal characteristic; the proof handles all chain rings.

## originality

FAIL

The distinct earlier indexed record 8ff282635ea5 explicitly proves exactly the shallow-shell, deep-shell and total counts for the same arbitrary finite commutative chain rings, including length one, as part of its image-length census. Once those counts are known the scaled-valuation limit is the ordinary uniform-mesh limit with a vanishing remainder. The exact coverage, not an access problem or the dates alone, determines this verdict.

## value

FAIL

The exact shell statistic is mathematically natural, but it is already explicit in a stronger enumeration. The sole remaining stated conclusion is a routine discretization limit of the previously known equal masses and bounded remainder. No independently useful new invariant or theorem survives this overlap; rewriting the claim as the limit alone would not repair it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
