---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Kirchhoff conservation gives 2 outdeg(v) = deg(v) mod 3, forcing column sums a/2 and row sums t mod 3. For a=4 any admissible margins have total 4t and maximum at most 2t: arrange 4t row tokens in four consecutive blocks and pair opposite positions, which never have the same label. These pairs give the columns. Fixed margins are exactly the cycle-reversal classes; interchanges suffice, and no directed reversal changes those margins. The four-row sector count is the central coefficient of (1+z+...+z^(2d))^4; the stated binomial subtraction simplifies to the cubic formula. Two different columns always supply a switch; identical columns make all rows sources or sinks, and satisfy conservation exactly when 3 divides t. The three-residue filter has factors 36, 9, 0 with multiplicities 1, 14, 12; common phase shift reduces 81 phase vectors to 27. Independent exact checks confirmed these multiplicities, sample flow totals and the full K_{4,6} sector profile. The argument also gives the single 90-state K_{4,4} sector and handles d=0.

## originality

PASS

The equivalence of directed-cycle classes with outdegree sequences is a direct prior specialization, and the balanced K_{4,6} count 1860 is explicitly known. The two-row total is elementary after suppressing right-shore degree-two vertices. The distinct contribution supported by the comparison is quantitative: the complete all-order sector census, including non-Eulerian margins for four rows and their aggregate mod-3 flow population. The inspected broader results and exact central-sector record do not cover that census.

## value

PASS

For the first two positive even left sizes for which mod-3 conservation forces an exactly balanced column, the census quantifies how flow counts split into cycle-reconfiguration components. It explains the three-step plateaus and the onset of both singletons and large sectors, and distinguishes the total mod-3 flow population from the classical Eulerian count. For example the balanced K_{4,6} sector has 1860 states, but the labelled flow space has 2106 in 19 components. This numerical and parametric distinction matters for sampling or comparing the full flow space with a single reconfiguration class; the already-known connectivity theorem is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
