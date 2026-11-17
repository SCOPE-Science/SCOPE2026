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
# Verification notes

The mathematical identity and rigidity are proved in RESULT.md by explicit second-order expansions and a compactness/minimax argument. Neither a numerical grid nor a negative database search is used as an infinite proof or as a certificate of novelty.

To repeat the finite diagnostic examples from a clean directory containing this package, execute `python3 check_examples.py`. Only Python's standard library is needed. The script checks five separations at two radii (ten examples), verifying exact positive coordinates, exact \(\ell_1\) separation, the nonnegative transverse norm difference, and a controlled comparison with the analytical leading coefficient. Its conclusions are finite corroboration only.

At fixed \(0<d<2\), expansion validity follows from both positive coordinates remaining bounded below as the perturbation radius tends to zero. The lower bound does not rely on an unproved uniform expansion at a vanishing coordinate: the proof first excludes this case with the exact symmetric-increment identity. Equality and limiting rigidity are at the strictly balanced minimax of the two reciprocal products.

Scientific limitations: no generalization to more than two atoms, no finite-radius exact modulus, and no endpoint \(d=2\). Independent audit has not been performed.
