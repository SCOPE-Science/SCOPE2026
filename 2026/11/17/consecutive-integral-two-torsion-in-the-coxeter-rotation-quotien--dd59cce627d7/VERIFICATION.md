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

# Reproduction and limits

Run `python verify_d5.py` under Python 3 with SymPy. The code constructs all \(1920\) even-signed permutations and exactly \(182\) noncrossing elements; no external group or orbit data are read. Its proper-part chains and quotient cells are enumerated exhaustively. The matrices of sizes \(32\times228\), \(228\times448\), and \(448\times256\) are constructed via alternating face deletion after chain-orbit identification. Both adjacent matrix products vanish over the integers. Exact Smith diagonal multiplicities are \((1^{31})\), \((1^{196},2)\), and \((1^{250},2)\). The computed homology is \((\mathbb Z,\mathbb Z/2,\mathbb Z/2,\mathbb Z^5)\), and the mod-two Betti vector is \((1,1,2,6)\).

`verification_output.json` is the recorded deterministic output, not a substitute for the executable checker. Finiteness makes the enumeration exhaustive; no claim is made about higher-rank type-\(D\) complexes. The derivation of \(\pi_1\) also invokes published shellability and the orbit fundamental-group theorem. No independent mathematical review has been performed.
