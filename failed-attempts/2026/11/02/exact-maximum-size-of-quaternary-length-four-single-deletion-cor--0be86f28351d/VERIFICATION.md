---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For 256 length-four words a rational deletion-descendant weight of total 25 is at least one on every distinct descendant set. Exactly equality patterns 0000, 0011, 0120, 0123 are tight. A hypothetical 25-code would exactly partition all 64 length-three descendants using only tight types, but for each outer symbol its three nonconstant palindromes aba can be covered only in pairs by 0120 words, an impossible parity partition. Independently enumerated the 24 supplied length-four codewords and verified all 64 deletion outputs are pairwise disjoint and exhaust the universe, so 24 is attained. The universal upper-bound parity proof is symbolic, not inferred from enumeration.

## originality

FAIL

FAIL: the identical quaternary one-deletion optimum N(4,4,1)=24 is already established in Kim, Lee and Oh (2010), Optimal Single Deletion Correcting Code of Length Four Over an Alphabet of Even Size, IEEE Trans. Information Theory 56(7), Theorem 2.2 and Table 2. Their complete even-alphabet formula q^2(q+2)/4 gives exactly 24 for q=4, with explicit 24-word quaternary code. This is decisive stronger prior coverage; an obsolete later 2012 table reporting only 20<=A<=25 cannot make the exact 24 result novel.

## value

FAIL

FAIL: as submitted the exact value 24 and existence of optimal 24-word packing are known from 2010 with precisely the same natural object and parameters. Re-deriving the result with a different fractional-weight parity proof and a codeword list has no independently motivated new theorem; the package does not claim a novel complete classification or a substantially new structural theorem beyond the covered original result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
