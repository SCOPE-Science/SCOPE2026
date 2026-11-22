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

# Finite exact verification

The finding concerns a fixed fourteen-vertex graph. Its central arithmetic classification is based on exhaustive enumeration, not a statistical simulation or an incomplete sample.

**`verify_smith.py`** uses a cyclic Fano incidence model with seven lines \(\{j,j+1,j+3\}\pmod7\). It enumerates every seven-vertex subset containing the distinguished point vertex: exactly \(\binom{13}{6}=1716\) cuts, one per unordered bipartition. It computes the integral Smith normal form of each exact integer seven-by-seven cross adjacency matrix, asserts the complete eleven-class histogram, and deduces the rank histograms at six primes. It also constructs all 28 noncollinear-triangle cuts and asserts that their union with the canonical point-line cut is *exactly* the characteristic-three deficient set. Run `python3 verify_smith.py` with Python 3.10+ and SymPy.

**`verify_modular.py`** independently constructs the Fano plane from the nonzero vectors and nonzero linear forms on \(\mathbb F_2^3\), computes each cross-rank from complementary submatrices by its own modular row-reduction implementation, and checks all 1716 cuts at primes 2, 3, 5 and 101. It independently verifies the same exceptional geometric set. Run `python3 verify_modular.py` with Python 3.10+ and only the standard library.

The exact nonzero Smith factors have prime support contained in \(\{2,3\}\); this is what extends the table from a few tested primes to **every** prime at least three. The computations do not establish historical priority, applicability to other finite graphs, resistance to noise, or independent validation.
