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

# Verification and limits

Run `python3 verify.py` without third-party packages. The program checks all 1024 arc masks by directed reachability, the 901 allowed faces, and the deterministic 450-pair reduced matching. After deleting the empty-to-vertex pair, its complete Hasse-cycle test topologically sorts all 900 nonempty faces, establishing an acyclic matching with only two critical simplices. It independently computes reduced mod-two Betti ranks, then checks the two five-edge directed Hamilton-cycle orbits for each of the four nonidentity rotations.

Recorded exact successful output is embedded separately as `verification_output.txt`. A finite face-by-face enumeration is a valid exhaustive proof here because the theorem concerns this fixed ten-arc complex. The topology of the quotient follows from the fully proved free action and standard covering and rational-transfer arguments, not from a quotient matrix computation. Neither a full integral quotient homology computation nor an independent audit is claimed.
