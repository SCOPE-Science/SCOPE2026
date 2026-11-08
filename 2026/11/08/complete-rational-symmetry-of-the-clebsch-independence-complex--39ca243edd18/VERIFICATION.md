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
# Verification of the Clebsch independence-complex symmetry theorem

Run `python3 verify.py` with Python 3 and its standard library, without network access or external files. The checked numerical values and deterministic output appear in `verification_output.txt`.

The program constructs the graph on \(\mathbb F_2^4\) by XOR with \(1,2,4,8,15\). It exhaustively enumerates every one of the \(2^{16}-1\) nonempty vertex masks, retains exactly \(392\) independent faces, constructs the prescribed \(190\)-pair acyclic matching, and checks a topological sort over all \(1200\) Hasse covers. It performs exact unit-pivot algebraic Morse cancellation, yielding ten critical degree-three generators, one degree-two generator and the integer differential \((1,1,0,0,-1,-1,0,0,-1,-1)\). A separate mod-two boundary rank computation yields \((15,65,95,16)\).

Every affine map \(x\mapsto a+\sigma(x)\) induced by a translation and a permutation of the five generating directions is enumerated and checked to preserve graph edges. The \(1920\) distinct maps exhaust the graph's automorphism group by the stabilizer argument in `RESULT.md`. For each one, the program computes the exact signed simplicial Lefschetz number from all invariant independent faces, subtracts it from \(1\), and compares the result to the closed rational-character formula for the proposed four-plus-five-dimensional decomposition. All comparisons must agree, and the character sum must vanish. The independent integer group-representation interpretation is proved in `RESULT.md`, not inferred solely from a program log.

This finite proof does not verify an infinite family, an integral group-ring decomposition, or priority among inaccessible publications. Independent mathematical review has not been performed.
