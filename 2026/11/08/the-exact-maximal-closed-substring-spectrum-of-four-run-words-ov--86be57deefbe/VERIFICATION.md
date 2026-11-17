---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Every four-run word X^aY^bZ^cT^d (positive run lengths, adjacent letters unequal) falls into mutually exclusive equality patterns: all four letters distinct gives exactly 4 whole-run maximal closed occurrences; one nonadjacent repeated pair gives 4+min(repeated run lengths); alternating ABAB gives 5+min(a,c)+min(b,d)-[c<=a]-[b<=d]. The proof partitions closed factors by zero through three transitions. Unary borders across nonadjacent repeated-letter runs yield bridge candidates, with precisely the two extension exclusions in ABAB; the single nonunary border gives the additional alternating interval. Two-variable geometric-series pair sums yield F_q(z,u)=q(q-1)(q-2)(q-3)u^4z^4/(1-z)^4+3q(q-1)(q-2)u^5z^4(1+z)/((1-z)^3(1-uz^2))+q(q-1)u^5z^4(1+uz)^2/((1-z)^2(1-uz^2)^2). At u=1 it reduces to q(q-1)^3 z^4/(1-z)^4. Independently enumerated all substring occurrences and borders for q=2,3,4 and run lengths each 1..3; full all-length result rests on border classification and formal series, not small tests.

## originality

PASS

Best-of-knowledge PASS with qualified prior implication. The earlier published November 8 binary four-run theorem already gives the ABAB count and exact endpoint list (so the q=2 specialization is NOT original). The current claim extends to all alphabets q>=3 and proves the three run-letter coincidence classes and their complete bivariate all-length output-size histogram, which is not implied solely by the binary alternating formula. General Umezaki et al. run-length-encoded enumeration and Fischer–Köppl output-sensitive algorithms can compute individual instances but no accessible evidence states this all-q coefficient GF; their highly relevant full texts were inaccessible, so this noncoverage claim is carefully qualified and kept as residual risk. Exact all-q statistic and q>=3 branches survive.

## value

PASS

Maximal closed substring occurrence count governs output size in string indexing/algorithms. Four runs are the first natural bounded-run class allowing distinct nonadjacent repeated transitions and a nonunary maximal border; the full alphabet-dependent output histogram is a complete motivated exact classification. The q>=3 taxonomy cannot be reduced to the prior binary-only alternating case. No new algorithm or arbitrary-run theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
