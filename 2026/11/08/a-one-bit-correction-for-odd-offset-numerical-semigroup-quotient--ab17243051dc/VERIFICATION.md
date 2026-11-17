---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For divisor p|a, m=a/p>=2, gcd(a,d)=1, odd q between 3 and a-1, coin offsets 1,3,...,q, the least number of offset coins at x=uq+v (1<=v<=q) is u+1+1_{v even}. Capacity and parity show this for all x; the inequalities lambda(x+2)>=lambda(x) and lambda(x+a)>=lambda(x) for a>q justify minimal quotient Apéry representatives w_{dr}=hm lambda(pr)+dr. They strictly increase along r by steps of 2, so only final/penultimate residues compete; comparing t=a-p-q floor((a-p-1)/q) yields F=B+1_{p,t odd, t>p} max(hm-d,0). Boundary m=2 has no penultimate admissible candidate and no correction; p=1 allowed. Fresh independent Dijkstra shortest-residue calculations match examples (12,3,2,1,9)->14, (15,3,4,2,11)->43, (20,4,1,3,13)->17. Pinned verify_exact.py is an independent broader Dijkstra implementation but its saved 125586-case log was not used as infinite proof.

## originality

PASS

The full 2023 Liu preprint establishes the same quotient Apéry framework and the even-terminal case, explicitly leaves an odd-terminal remainder without a closed Frobenius formula. The audited one-bit switch decides precisely that missing branch. Later 2025 journal revision was not fully read; that is a genuine priority risk but not evidence of covering. No broader published Resultary closed rule for this many-generator odd-offset family was verified.

## value

PASS

The odd-terminal remainder is a stated concrete gap in a specific published Frobenius-number classification. A uniform two-candidate exact formula, including arbitrarily positive correction and attaining-residue switch, answers a natural semigroup quotient invariant across infinitely many parameters; it is not merely another numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
