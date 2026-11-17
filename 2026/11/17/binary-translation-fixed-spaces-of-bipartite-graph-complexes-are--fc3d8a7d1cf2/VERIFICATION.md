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
# Verification of binary-translation fixed spaces

The standalone `check_binary_bipartite.py` uses Python's standard library only. Execute `python3 check_binary_bipartite.py` in a directory containing that script. For each rank \(1\le r\le4\), it independently enumerates \(2^{2^r-1}\) choices of complete translation edge-orbits, constructs the actual undirected Cayley graph and tests bipartiteness via graph search, then compares this with direct containment in the explicitly generated hyperplane facets. It computes mod-two simplicial boundary ranks for the same face systems and compares the resulting reduced Betti dimensions with the exact formula. It also calculates the Gaussian-binomial/Möbius formula through rank six. The specific bound rank four is a computational bound, not a mathematical restriction on the theorem. Full rigorous validity at arbitrary rank comes from the complete written proof and previously established shellability, not finite experimentation.

The test output is embedded separately as `verification_output.txt`. The reduced mod-two Betti numbers at ranks two, three and four are respectively one in degree one, six in degree two and 91 in degree three; all other reduced Betti numbers tested vanish. Exact integral torsion-freeness at all ranks follows from shellability rather than the mod-two calculation. This verification is an internal mathematical consistency check, not an independent audit.
