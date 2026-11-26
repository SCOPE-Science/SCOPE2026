---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independent reproduction: /workspace/reproduction/cycle_check.py and cycle_check.log (Python 3, SymPy) use normalized integer-offset faces, exact relative Smith forms, and simultaneous rounds of disjoint elementary pairs free at the start of each round. Faces of size at least two have a unique lifted arc of span ≤6 for n≥13, because the complementary gap is >6; orient by increasing order in that arc. For d=1,2,3 the ranks of relative boundaries ∂1 through ∂5 are (0,0,8,8,2), (0,0,6,8,2), (0,2,8,8,2) and all nonzero Smith factors are 1. Any removed face was witnessed at 0 or d, hence fits in [−3,d+3]; any competing witness and its offsets are determined locally, with no unintended wrap at n≥25. The exact anchored relative pair is then independent of n; all 13≤n≤24 are checked directly. For the collapse, the state at anchor x after one simultaneous round depends only on anchors within distance 6 of x: if x anchors the upper member, the lower anchor a is in [x,x+6], and all its immediate cofaces have anchors in [a−6,a]; if x anchors the lower member the same bound holds. This also follows by lifting an immediate coface through a witness adjacent to the lower anchor. Thus the difference from the intact schedule after ten rounds is contained in [−63,d+63], and the stated corrections are local there. At n≥200 the entire defect and interface agree with the n=200 check, and outside [−70,70] only the unmodified five periodic templates remain. The exterior anchor interval [71,n−71] has connected dual graph: the 0_i,1_i backbone is connected throughout; 4_i attaches at i, 2_i attaches forward to 0_(i+2) or backward via 3_(i−2) and 1_(i−3), and 3_i attaches to 1_(i−1) or, at the left endpoint, via 2_i. Contract this exterior to one vertex. All incident edges and boundary triangles are determined within a bounded collar of the two ends (shared triangles require anchors within six), so this contracted defect graph is independent of n. The check at 200 proves the uniform exposed-boundary condition; orders 13–199 were checked directly. Boundary-rooted dual spanning forests give a unit triangular maximal minor of ∂3, so H3=H^3=0 for the faulted complex. The cited intact parity groups agree with an independent check: straightening each edge of length k≥2 across the triangle (i,i+1,i+k) reduces H1 to the unit cycle; winding shows it has infinite order. In the intact tetrahedral complex the signed dual graph is connected, closed, and has consistent top-chain coefficients [1,−1,1,1,1] times (−1)^i on the infinite templates (checked modulo 200, which contains every signed local adjacency); the 0_i,1_i backbone forces alternating signs, hence obstruction in odd period. Thus H3 and H^3 are respectively Z,Z for even n and 0,Z/2 for odd n. Euler characteristic zero by translation orbits and universal coefficients give the intact H2 groups. The pair LES now gives H1 isomorphism, H2 of rank two and the primitive-even/index-two-odd comparisons, using H^3(Y)=0 to exclude torsion and dimension three after collapse to exclude higher homology. H0 follows from the same LES and connectedness of the intact complex.

## originality

PASS

The intact parity theorem and its broader stable-cycle-power extension are prior, not novel. The all-distance single fault integral and relative result for the open third-power neighborhood complex is distinct from the materially close intact, squared-cycle and flag-complex statements inspected.

## value

PASS

A natural single-edge perturbation in a canonical cyclic family erases both an even-order fundamental class and the odd-order 2-torsion. The two-generator relative response and primitive/index-two distinction answer stronger questions than parity-independent Betti numbers alone, uniformly for every edge rather than selected examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
