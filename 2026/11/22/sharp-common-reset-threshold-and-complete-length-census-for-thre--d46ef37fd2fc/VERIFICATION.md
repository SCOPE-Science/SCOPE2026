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

# Computational verification

Run `python3 triple_catalogue.py` and `python3 triple_bfs.py` from the same directory. The catalogue code enumerates 729 ordered pairs of three-state transformations, records signatures at lengths one through seven and performs an exact weighted 28-cubed signature-triple census. It obtains 549 synchronizing automata and a total of 165,469,149 ordered triples.

The separately coded BFS implementation uses sets of state images and shortest-path searches in three-component subset products; it reaches precisely the same distribution. Both implementations directly inspect the displayed sharp triple. The subset simple-path bound for one three-state machine is a mathematical completeness argument for the synchronization classification. No experiment on larger state sets or component counts is implied.

The recorded text outputs are `catalogue_output.txt` and `bfs_output.txt`. The scripts and exact stdout were reproduced from their accompanying paths. This is reproducibility evidence for a finite census, not an independent scholarly audit.
