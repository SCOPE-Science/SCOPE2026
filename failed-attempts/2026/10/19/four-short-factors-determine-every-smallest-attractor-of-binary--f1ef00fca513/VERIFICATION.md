---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the finite linear word (0^a1^b)^m with a,b,m at least two, the singleton factors force one position per symbol. The 01 and 10 tests require, respectively, an internal-block boundary endpoint and an inter-block boundary endpoint. The first and last positions of each constant run are distinct, leaving just the two stated families. For sufficiency of a last-position pair, the first change of any mixed factor fixes its start residue r modulo p=a+b. If its length is at least p-r, it reaches the last one of its starting block. Place the occurrence in the chosen one's block if that start fits; otherwise the rightmost occurrence starts before that position and ends at least at (m-1)p, since less than one period can be left unused on its right. If the length is smaller than p-r it must start with zeros, cross 01, and fit in the chosen zero's block. Constant factors fit through the selected run ends, and reversal with complementation maps the first-position family to the last-position family with run lengths swapped. Thus the boundary restrictions, optimal size and count 2m(m-1) all follow. An independent occurrence-interval program checked every candidate pair and the four-test equivalence for 30 parameter triples; replay: python3 /workspace/branches/exact_review_checks.py 5. The frozen checker and its output were inspected, not executed; both finite checks are corroborative, not the proof.

## originality

FAIL

A distinct indexed Resultary finding explicitly covers every frozen claim and extends the domain. Converting its one-based positions to zero-based and renaming k to m identifies the two families term for term, as well as the minimum, exact count, and four-factor iff certificate. This is demonstrable catalogue coverage, not an allegation about authorship or historical priority. The compared catalogue path is later than the frozen path; these dates alone do not determine the scientific relationship. No genuinely distinct remainder is claimed in the assigned finding.

## value

PASS

As mathematical content, the four-factor criterion replaces checking unbounded factor lengths, and the complete pair families explain both the terminal restrictions and why multiplicity is independent of the two run lengths. This directly informs verification and counting in a natural periodic family, not just an optimum-size calculation. The content is useful; it supplies no additional catalogue contribution beyond the broader match identified on originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
