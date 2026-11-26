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

E^t examines the forward window of t+1 bits. A one-run therefore loses t sites at its end, retaining its start exactly when its original length exceeds t; zeros cannot disappear. The truncated profile reconstructs the entire output as a union of indexed runs even at extinction, and the all-one word is separately fixed. Two unequal lengths have equal truncated values exactly once both are zero, proving the maximum-discrepancy clock, including t=0. If the surviving profile has a proper period d and no run disappeared, adding t back on its support gives a d-periodic input. Otherwise consecutive surviving starts straddle a vanished run and are at most d apart. They need t+1 or more sites of the preceding run, at least one vanished one and two separating zeros, so d>=t+4>=5. Conversely, runs 11 starting at phase 0 of each d-block and the single isolated one at index 3 give an asymmetric predecessor; one step leaves exactly the phase-0 sites, of least period d. Composite n with maximum proper divisor <=4 is at most 9 (n/p>=p for its least prime p); n>=10 with a proper divisor >=5 is composite. The proof has no finite horizon restriction.

## originality

PASS

The general persistence of stabilizers and classical binary run erosion are prior inputs. The combination of exact indexed per-shift birth times and the vanished-run obstruction with a sharp proper-divisor witness is distinct in the checked evidence. The known local run update makes the clock elementary, not a claim to originality of the erosion operation.

## value

PASS

The theorem concerns a standard local erosion operation and the natural spatial stabilizer along its orbit. It distinguishes exact entry of each shift, birth of genuine nonuniform symmetry, and symmetry due merely to extinction. The sharp all-length boundary and one-step witnesses can be used to compare dynamics of different rules even on rings of the same size; they are not an arbitrary census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
