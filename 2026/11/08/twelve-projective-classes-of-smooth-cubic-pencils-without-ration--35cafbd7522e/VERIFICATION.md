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

# Verification of the smooth-pencil classification

The standalone Python program `verify_binary_smooth_pencils.py` uses only Python's standard library and SymPy. It generates all \(2^{10}-1\) nonzero homogeneous cubic forms over \(\mathbb F_2\), computes exact polynomial ideals of partial derivatives and tests their zero-dimensionality over the coefficient field to establish smoothness over its algebraic closure. The cubic Euler identity proves that this is the required singularity test. The independent finite-field singularity search over \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_{16}\) is an additional check, not an unsupported replacement for the algebraic-closure proof.

The program then enumerates all \(174,251\) two-dimensional subspaces of the ten-dimensional cubic-form vector space in two ways, verifies the empty rational base locus and every rational incidence value, and computes images under all \(168\) projective coordinate changes. It independently counts the net-extension cosets, checks each of the twelve orbit representatives, and cross-checks the incidence and net-extension histograms. Expected output concludes with `BINARY_SMOOTH_BASEPOINTFREE_CUBIC_PENCILS_PASS`. No table outside the packaged program is required; the assertions fail rather than print a success marker upon disagreement.

Verified exact counts: 336 smooth nonzero cubics; 5,544 all-smooth pencils; 2,016 with empty rational base locus; twelve free projective orbits; blocking-member histogram \(\{0:672,1:1344\}\); containing-smooth-net histogram \(\{0:504,1:840,2:672\}\).

The program is a finite exhaustive certificate. It makes no assertion about curve singularities over arbitrary extensions beyond those resolved by its exact Gröbner test, and no assertion of independent audit or historical novelty certification.
