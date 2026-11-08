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

# Reproducible finite checks

Run `python3 verify.py certificate.json` using Python 3 and only the standard library. The supplied output is in `verification_output.txt` and was obtained by rerunning the checked source with the packaged certificate.

The verifier enumerates each matching as an increasing edge-index set, verifies the complete face vector \((24,172,416,306,32)\), reconstructs all 468 Morse pairs, topologically sorts all 951 vertices of the reversed Hasse directed graph, calculates the signed 4-by-11 integral Morse differential from exact gradient recursions, proves its rank two and primitive image by row relations and a unit minor, then separately calculates all simplicial boundary ranks over \(\mathbb F_2\). It compares reconstructed matching pairs, critical faces and matrix with `certificate.json`.

The Morse chain groups contain four 2-cells and eleven 3-cells, giving integral homology ranks two and nine. Since there is one 0-cell and no 1-cells, the 3-cell attaching maps lie in \(\pi_2(\bigvee^4S^2)\cong\mathbb Z^4\) and are classified by the verified matrix. Smith factors \((1,1)\) permit two cancellations and the claimed wedge homotopy type. All conclusions are finite and exact for this graph only; they are not evidence for a formula across other bipyramids. No independent audit was performed.
