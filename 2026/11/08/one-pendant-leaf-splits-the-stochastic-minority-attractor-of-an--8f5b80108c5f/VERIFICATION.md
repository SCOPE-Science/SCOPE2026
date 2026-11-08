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

The direct exhaustive checker `check_exhaustive.py` generates the exact closed-neighborhood single-vertex transition digraph for every binary labelling of the pendant-clique graphs with clique sizes 3, 5, 7 and 9. It enumerates terminal strongly connected components without invoking the proposed structural proof, then compares them with the formula-defined classes. The four tests cover 1,360 labelled states and establish the finite checks reported in `check_exhaustive.out`.

The independent checker `check_spectrum.py` constructs inclusion graphs between two adjacent ranks of even-dimensional Boolean cubes. For dimensions 2, 4 and 6 it compares exact integer Laplacian characteristic polynomials, as computed by SymPy, with the claimed complete eigenvalue/multiplicity formula. See `check_spectrum.out`. The method does not use numerical approximations or graph packages for these spectral comparisons.

For replay, use a Python 3 environment, with SymPy installed for the spectral checker. Run `python check_exhaustive.py` and `python check_spectrum.py`; no network access or undocumented input file is required. The scripts and recorded outputs are included alongside these documents.

These are finite regression checks, not exhaustive proofs for unbounded sizes. The all-size classification follows from the constructive reachability argument and the inclusion-graph decomposition in `RESULT.md`; the all-size gap follows from its incidence-operator commutator proof. Independent external audit has not been performed.
