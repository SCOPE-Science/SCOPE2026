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

# Verification record

`python verify.py` reads the neighboring `torsion_witness.json` and uses only standard-library exact modular arithmetic. It verifies the complete \(21\)-vertex, \(105\)-edge, \(105\)-triangle matching complex, the complete mod-three triangle-boundary rank \(84\), the integral five-edge cycle, the cycle's nonzero mod-three class, and a supplied 32-triangle two-chain whose boundary is the cycle plus its coordinate-transposed image. It also recomputes the \(84,1680,6720\) inflated face counts and the \(5103\) additional two-sphere count. Full output is embedded separately in `verification-output.txt`.

The published integral homology calculation \(\widetilde H_1(M_7;\mathbb Z)=\mathbb Z/3\mathbb Z\), \(\widetilde H_2(M_7;\mathbb Z)=\mathbb Z^{20}\), and the inflation homotopy theorem are external mathematical premises, not claims of independently recomputed Smith form. The direct mod-three chain check does not itself prove those integral premises or the general homotopy decomposition. No independent audit has been carried out.
