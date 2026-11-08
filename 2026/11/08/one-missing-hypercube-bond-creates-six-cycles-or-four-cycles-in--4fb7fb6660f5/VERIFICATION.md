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

# Exact verification and scope

Run `python check_direct.py` and `python check_block.py` with a standard Python 3 installation; both require no third-party packages. The first constructs the full deleted-edge cube matrix as bit rows, calculates finite-field ranks and compares binary state trajectories with exact theoretical joint entry/period counts. The second independently uses bipartite even/odd blocks, rank-one deletion and block-square identities. Output files from successful runs accompany this result.

The exhaustive state counts cover only dimensions two to four, and matrix identities are verified only through dimension seven. Neither finite computation establishes all dimensions or all characteristic-two fields; the self-contained block-algebra proof in `RESULT.md` supplies the general argument. Self-review passed; no independent or external audit was performed.
