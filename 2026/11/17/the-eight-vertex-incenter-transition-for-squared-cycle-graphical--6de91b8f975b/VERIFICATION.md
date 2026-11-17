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

# Verification of the exact squared-cycle incenter classification

The proof in `RESULT.md` establishes the claimed classification in every integer order \(n\ge6\). The standalone `verify.py` checks additional finite cases; these are not represented as an infinite proof or independent mathematical assessment.

Running `python3 verify.py` reconstructs all undirected edges, enumerates every nontrivial cut in orders \(6\) through \(16\), tests normalized cut values using exact integer cross-multiplication, and checks the active-normal rank by rational elimination. It also generates all extreme centers of the claimed loci for orders \(8,10,12,14\) and checks all nontrivial cut constraints using high-precision decimal radicals. Observed output ended:

`VERIFIED squared-cycle graphical zonotopes cuts 130986 center constraint masks 21752`

The exceptional radius scale \(b_4=2-3\sqrt7/4\) follows symbolically from singleton-cut inequalities; the higher-even-order scale follows from the strictly decreasing near-balanced-interval slack. The proof also checks all non-tangent facet inequalities, notably using \(mb_m<1\), and enumerates all optimal centers and their vertices. No claim of independent audit, exhaustive testing for every dimension, or originality certification is made.
