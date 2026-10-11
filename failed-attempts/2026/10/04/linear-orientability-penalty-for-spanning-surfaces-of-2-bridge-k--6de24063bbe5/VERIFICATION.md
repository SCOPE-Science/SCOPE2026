---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Linearity of expectation and the two published asymptotics give the mean coefficient and constant exactly. Since the penalty is nonnegative and is strictly less than c, normalizing by c gives a random variable in [0,1); splitting its expectation below and above any fixed delta yields the stated lower bound after taking limits. The special delta=1/12 value simplifies to 1/11.

## originality

FAIL

The claimed mean orientability penalty is exactly twice the published average Seifert-genus asymptotic minus the published average unoriented-genus asymptotic on the same ensemble. The positive-density statement is then the generic bounded-variable inequality obtained from 0<=D/c<1 and the mean limit 1/6. No new topological input or joint genus information enters. Under the audit rule that direct corollaries of existing results are covered, this fails originality despite the absence of the phrase 'orientability penalty' in the source papers.

## value

FAIL

The interpretation is intuitive, but the quantitative theorem contains no new topological lemma, distributional information, or nontrivial finite classification: it is a direct subtraction of two known marginals followed by the standard one-moment tail bound. Under the common value bar this is routine repackaging.

The dated certificate retains the supplied scientific assessment, sources and limitations.
