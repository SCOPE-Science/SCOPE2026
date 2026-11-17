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

# Reproducibility and limits

Run `python3 -m pip install -r requirements.txt`, then `python3 verify.py`. The package includes `verify.py`, `requirements.txt`, and `verification_output.txt`; the latter is the actual successful run output, not an inferred result. The verifier implements independent exhaustive enumeration of all cells of the multihomomorphism complex at \((m,p)=(3,5)\) and \((3,7)\), exact product-of-simplices signed boundaries, orbit canonicalization including orientation signs, integer checks that each consecutive boundary composition vanishes, sparse modular Gaussian elimination, and integer Smith normal form in the small case.

For \(p=5\), the quotient cells number \((12,36,30)\), and the Smith diagonal of its degree-two boundary has one nonunit invariant factor five. The mod-five Betti vector is \((1,1,6)\); the auxiliary mod-\(1000003\) Betti vector is \((1,0,5)\). For \(p=7\), quotient cells number \((30,180,450,540,258)\), and the mod-seven Betti vector is \((1,1,1,1,18)\), versus \((1,0,0,0,17)\) over the auxiliary prime.

The infinite-prime theorem depends on the published complete-graph Hom sphere-wedge theorem, the geometric proof of the free action, Cartan–Leray/Serre spectral sequences, group cohomology of an odd prime cyclic group, and Euler characteristic. No finite enumeration is asserted to prove all-prime assertions. The recorded checks do not directly calculate cup products; these are proved from the natural cohomology spectral sequence and its ring map.
