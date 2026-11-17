---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The three displayed commutator equations are necessary and sufficient for Y in T3 to centralize X. Distinct eigenvalues give q^3 distinct conjugated diagonal subalgebras for q>=3 (unitriangular stabilizer trivial). Two equal eigenvalues give three choices of repeated pair, each with split/nonsplit normal form, q^2 orbit centralizers per form; scalar-diagonal nilpotent cases give 1+1+2q+(q-1). Codimension and diagonal-image projections separate the strata. Result: c0=c1=1,c2=3q^2+2q,c3=3q^2+q-1+1_{q>2}q^3; q2=31 and for q>2 total q^3+6q^2+3q+1. Independently recomputed the commutator rowspaces from explicit matrix equations over F2,F3,F5, obtaining 31,91,291 and codim spectra (1,1,16,13),(1,1,33,56),(1,1,85,204). The submitted standard-library checker additionally covers F4,F7; this independent finite work corroborates universal orbit reasoning.

## originality

PASS

PASS best-of-knowledge: Słowik 2018 classifies maximal/minimal elements of the centralizer inclusion poset, not all equal embedded centralizer subalgebras or their finite-field count. Bhunia 2019 classifies conjugacy classes of group centralizers, mainly over infinite fields, with a quotient by conjugacy far coarser than literal embedded equality. Cheraghpour et al. study two-by-two triangular commuting graphs. Related published SCOPE 4x4 strictly-upper-triangular or twisted T3 invariants have different multiplication/statistics. Searches found no exact or stronger T3 embedded centralizer census; nonidentification does not prove absolute novelty.

## value

PASS

PASS: distinct element-centralizer subalgebras and their codimensions are natural complete finite-algebra invariants, measuring distinct commuting-constraint kernels beyond conjugacy. The uniform finite-field classification exposes a genuine q=2 structural exception (no three distinct diagonal eigenvalues). It is a full small-rank classification rather than an arbitrary isolated count and can inform commuting-neighborhood or centralizer-lattice calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
