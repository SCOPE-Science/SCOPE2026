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

# Reproducing the checks

Use Python 3.9 or later. Neither program requires external packages. From the directory containing this document, run:

```sh
python3 verification/check_cycles.py
python3 verification/check_spectrum.py
python3 verification/check_contact_identity.py
```

Compare output to the identically named `_output.txt` files for all three programs. The former enumerates all configurations of the four small stated graphs by direct Greenberg–Hastings update and checks an explicit primitive twelve-cycle and a primitive five-cycle on the nonintegral boundary \(C_5\). The second computes exact integer strongly regular graph spectra from \((v,k,\lambda,\mu)\) and checks multiplicities and spectral exclusions. The third independently iterates integer-encoded states and tests the crucial identity at every vertex and every phase on all recurrent small-graph orbits. The verification output was obtained by executing these three included source files.

The all-size result is mathematical, not an extrapolation of these finite checks. Reconstruct the core proof by (i) showing that \(E_{t-1}\cap E_{t+1}=\varnothing\), (ii) counting contacts between \(E_t\) and both disjoint adjacent-phase sets to derive \(|E_{t+1}|\le|E_t|\), (iii) using periodicity to saturate both bounds and get the pointwise identity \(Au_t=r(u_{t-1}+u_{t+1})\), (iv) performing a temporal Fourier transform and invoking integrality of the adjacency eigenvalues, and (v) eliminating one- and two-period nonzero excitation by the refractory rule. The spectral extinction application additionally assumes the independently documented strongly regular graph parameters.

Limits: these scripts do not enumerate the \(3^{56}\) or \(3^{100}\) configurations of the exceptional graphs; extinction there follows from the symbolic theorem plus exact spectrum. The program checks are not an independent external review, and the available literature comparison cannot exhaust all unpublished or unindexed sources.
