---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The exact all-parameter theorem follows from the deterministic gate-encounter proof and the independent residue-class count in RESULT.md. Run `python3 verification/check_shells.py` from the package root. The script separately evolves all states of the actual network, checks that the predicted killing times agree with the observed first-periodic-entry times, tests every cumulative layer, tests all final `b` cumulative layers and verifies the terminal size for every cycle pair with lengths between two and six inclusive. Its final marker is `BRUTE_SHELLS_OK 25`.

The numerical tests are finite; the proof establishes all positive integer lengths at least two. Published results already include eventual-periodic projections and general settling bounds; only the newly specified time-resolved counts and sharp arithmetic terminal populations are reviewed here. Independent external validation has not been performed.
