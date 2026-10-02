---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Using the stated Hall chain ad_X1(X2)=X12, ad_X1(X12)=X112, ad_X1(X112)=X1112 and step-4 truncation, the vectors X1 and exp(s ad_X1)X2 span exactly five dimensions as s varies, so the endpoint differential has rank 5 and the record's explicitly defined endpoint-map corank is 3. The annihilator is three-dimensional and kills X12,X112,X1112, making the rank-2 Goh scalar vanish. The normal covector X1* gives h1=1,h2=0. These calculations were independently reconstructed exactly. The package's claimed verifier and run log were not present at the audited commit.

## originality

FAIL

The central scientific conclusion that one-parameter subgroups tangent to the distribution are both abnormal and normal is already explicitly covered by Sachkov-Sachkova's published study of this exact free step-4 rank-2 group. Their paper states that the two-parameter family of one-parameter subgroups is nonstrictly abnormal and later identifies straight lines among precisely the nonstrict abnormal trajectories. The submitted normal-abnormal X1 line is therefore a special case of prior primary literature.

## value

FAIL

The X1-line computation is a routine Hall-basis/PMP specialization of a canonical one-parameter subgroup already included in the published normal/abnormal classification. It does not add a substantive new boundary or invariant once that coverage is accounted for.

The dated certificate retains the supplied scientific assessment, sources and limitations.
