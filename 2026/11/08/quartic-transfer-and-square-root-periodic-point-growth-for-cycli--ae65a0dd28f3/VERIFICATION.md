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

# Verification details

The exact definition of the counted object and the unrestricted proof appear in `RESULT.md`. The verification programs are self-contained relative to this directory, except that the optional symbolic determinant step uses SymPy.

Run `python verify_direct.py`: it independently enumerates all cyclic gap vectors with entries from \(\{-3,-2,-1,0,1,2,3\}\), imposes sum zero, reconstructs integer labels, iterates the stated update twice and confirms the counts for every ring order from three through eight. The proved signed-gap lemma makes the finite search exhaustive for **periodic states in these sizes**, though it makes no claim about all possible transient starting configurations. Output: `direct_output.txt`, ending in `DIRECT_OK`.

Run `python verify_transfer.py`: it constructs the Laurent transfer, independently computes the quartic Newton-power sums and central trinomial coefficients through ring order seventeen, checks the displayed counts, and performs the exact symbolic characteristic-polynomial identity when SymPy is installed. Output: `transfer_output.txt`, ending in `SYMBOLIC_CHARPOLY_OK` and `TRANSFER_OK`.

Both commands were replayed from the directory containing the delivered files; their captured output files were compared against the commands' output. The asymptotic spectral step is proved in `RESULT.md` using Perron–Frobenius theory, a strict peripheral spectral inequality and a Gaussian saddle. It is not certified by finite numerical experiments. Neither external mathematical review nor independent audit has been performed.
