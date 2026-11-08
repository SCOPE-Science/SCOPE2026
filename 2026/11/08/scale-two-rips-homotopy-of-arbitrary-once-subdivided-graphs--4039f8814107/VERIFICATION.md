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

# Verification and scope

The source file `verify.py` is a standalone Python 3 program using only the standard library. Run `python3 verify.py` in the directory containing it; expected text output is saved in `verification_output.txt`. The program generates each labeled simple graph on at most five vertices, constructs the once-subdivided graph and its squared distance graph, enumerates all flag simplices, and independently builds the proposed core. It checks the exact exceptional-face classification, verifies every proposed elementary-collapse pair has exactly one codimension-one coface in the current complex, and confirms that the final complex is the original clique complex. It computes mod-two homology from the original simplicial boundary matrices and compares it to the predicted decomposition. The same checks are performed for the six named graphs.

There are 1,099 tested labeled graphs on one through five vertices and six additional named cases. The program's finite enumeration is exhaustive *within those indicated finite parameter ranges only*. The mathematical proof for all connected finite simple graphs rests instead on the incidence-distance taxonomy, combinatorial face classification, all-degree collapse sequence and nullhomotopic attaching loops in `RESULT.md`. No externally certified or independent review is claimed, and no result about higher Vietoris–Rips scales is inferred from these tests.
