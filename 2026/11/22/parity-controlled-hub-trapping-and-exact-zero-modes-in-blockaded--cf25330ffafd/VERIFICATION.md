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

# Reproducibility and scope

The exact analytical reduction uses \(H=\begin{pmatrix}A&|v\rangle\\\langle v|&0\end{pmatrix}\), with \(A\) the Cartesian sum of local \(K_{1,r}\) adjacency operators. Its eigenvalue multiset and vacuum spectral weights give the exact kernel census and phase-dependent overlap. The parity return bounds are elementary consequences of the spectrally resolved vacuum and Duhamel's estimate. Their proofs appear in `RESULT.md`.

Run `python verify.py` with Python, NumPy and SciPy. The program independently enumerates allowed physical spin configurations by bitmask, creates the full spin-flip Hamiltonian from the original graph, and checks modular rank, numerical zero-energy multiplicity, hub zero-mode weight, and selected finite-time bounds. Seven finite \((m,r)\) pairs pass. The program also evaluates two large finite binomial sums as asymptotic spot checks. Modular ranks, floating-point spectra and asymptotic spot checks are finite consistency evidence, not proofs about arbitrary \(m\); the required infinite statements follow from the analytic argument.

No external or independent audit has been carried out. Finite coherent models with ideal homogeneous blockade only; no verification is offered for finite detuning, finite blockade strength, noise, or experimental apparatus.
