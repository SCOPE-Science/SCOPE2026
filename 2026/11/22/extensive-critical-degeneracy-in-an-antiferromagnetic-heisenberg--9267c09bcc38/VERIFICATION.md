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

The spin operators use eigenvalues \(\pm1/2\), and all listed energies therefore match conventional \(\mathbf S\cdot\mathbf S\) exchange normalization. A standalone `verify_spin.py` directly constructs the Hamiltonian in the \(2^{2m+1}\)-dimensional computational basis. In a mathematically separate calculation it decomposes tensor products of spin-one representations and constructs every predicted energy with its full degeneracy. For each \(m\in\{2,3,4\}\) and \(K/J\in\{0.2,0.5,0.75,1,1.2\}\), all eigenvalues are compared, along with ground energies, ground multiplicities, and gaps to the first distinct excitation. All 15 comparisons passed; the largest spectral discrepancy was \(2.31\times10^{-14}\). Hilbert-space dimension identities were additionally checked for \(m=2,\ldots,10\).

Reproduce with `python verify_spin.py` with NumPy available. These finite matrices do not certify the infinite family. The proof instead uses a complete set of commuting outer-pair Casimirs, exhaustive angular-momentum coupling with multiplicity, and a discrete affine energy minimization. The theorem assumes identical couplings on each bond class and has not been tested against perturbations, magnetic fields or experimental data. Independent scientific validation and definitive historical priority checks are not claimed.
