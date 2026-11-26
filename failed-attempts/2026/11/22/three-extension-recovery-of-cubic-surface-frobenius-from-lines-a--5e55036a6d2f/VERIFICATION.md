---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The blow-up description and the W(E6) action on the line classes of a geometrically smooth cubic apply in all characteristics. The classes span the geometric Picard lattice (the six exceptional classes and H-E1-E2 already span), so the line-permutation representation is faithful. The anticanonical triples are exactly the plane sections supported on three distinct lines: an effective triple summing to the anticanonical class is a hyperplane section, and a plane section cannot contain a multiple line on a smooth cubic (intersecting the class of that line would give (-K).L=1 but 2L²+L.M<=-1). Descent counts fixed unordered triples, not fixed triples of descended lines. The supplied exact certificate and CSV were inspected, not executed. Independent replay `python3 /workspace/branches/f9e72d04-57ec-4c6c-a718-b3c316eb22bf/independent_e6.py` on the six simple-root reflections confirmed the 45 triples by both lattice and graph definitions, all 51840 elements, 25 conjugacy classes, and 20/24/25 cycle-spectrum counts and 19/23/25 successive profile counts. The degree-two collisions are exactly ((0,1),(0,3)) separating into (3,7) and (3,13) and ((0,3),(0,3)) separating into (15,15) and (27,45). Fixed counts of powers are the sums of lengths of cycles dividing the power; complete cycle decompositions determine the finite étale zeta functions by products of (1-z^d)^(-1), and Weyl conjugacy implies conjugacy on Picard. The geometric sharpness for actual surfaces holds over sufficiently large fields by the cited realization results, not asserted over every small field.

## originality

FAIL

A distinct same-day Resultary record supplies exact coverage of the decisive finite result, not just nearby parameters: its opening table already tabulates both permutation spectra for every abstract W(E6) conjugacy class. The six-count criterion, its sharpness, and the stated enumerative data then follow by the ordinary cycle-to-fixed-point formula and row comparisons, with no new incidence or arithmetic input. This is a statement-level coverage failure; the checked evidence does not establish which same-day record preceded the other.

## value

FAIL

A sharp low-degree cutoff is a natural and useful question. In this submission, however, all distinguishing and obstruction data are immediate row projections of a complete existing abstract cycle table, not a previously undetermined invariant requiring new mathematics. The arithmetic addendum is established realization applied to those rows. The independent computation corroborates the data, but the scoped claim offers no separate substantive contribution beyond that covered deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
