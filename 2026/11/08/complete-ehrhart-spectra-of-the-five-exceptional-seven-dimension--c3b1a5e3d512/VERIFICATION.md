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

# Exact reproducibility checks

Run `python verify.py` with Python 3.11+, NumPy and Numba installed. The script embeds the five fourteen-row binary vertex sets transcribed from Kaibel–Pokutta, Appendix A, Table 3; it has no external data or network dependency. It prints five lines of full-dimensionality witnesses, facet counts, lattice-point count vectors, \(h^*\) vectors and normalized volumes, ending with `ALL EXACT CHECKS PASSED`.

**Checks actually performed:** each column has 14 distinct binary vertices, each coordinate sum is 7, and the first eight augmented points have nonzero exact integer determinant. Every one of the 3432 candidate facet-spanning seven-subsets per polytope was tested by integer cofactor normals; all supporting hyperplanes were checked against every source vertex. All verified facets have seven vertices; the lists contain 144 or 136 facets as expected. Membership in every integer-dilated polytope for dilations 0 through 7 was decided by the resulting exact integer inequalities on the entire \([0,q]^7\) grid. The eight exact point counts were converted by the degree-seven Ehrhart numerator identity. An independent center-star determinant triangulation gives the same normalized volumes as the coefficient sums.

The proof's infinite-dilation conclusion uses the standard Ehrhart series theorem: a seven-dimensional *lattice* polytope has a numerator of degree at most seven. The counted cases therefore suffice to identify the numerator and all subsequent lattice counts. The script is a finite exhaustive checker; it does not re-prove the published classification of all five cube-symmetry orbits, and it does not certify global historical priority. No independent human or external audit has been performed.
