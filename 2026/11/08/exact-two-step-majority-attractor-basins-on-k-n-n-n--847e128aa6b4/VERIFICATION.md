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

# Reproducibility of the majority-basin theorem

The graph \(K_{n,n,n}\) has three labelled sets of \(n\) vertices with all cross-part edges and no within-part edges. Each vertex simultaneously adopts the strict open-neighborhood majority of binary opinions, retaining its own opinion on a tie.

Execute `python3 code/check_direct.py` and `python3 code/check_compressed.py` with standard Python 3. The first script generates actual vertex-level neighbor masks, enumerates every labelled initial state for \(1\le n\le5\), and compares the eventual fate to the binomial formula and strict-middle criterion. The second script uses an independently written count-triple update, enumerates all count triples through \(n=30\), and checks exact weighted population identities, time-two entry and the special fixed-point class. It also prints numerical finite-\(n\) approaches toward the Gaussian prefactor. Recorded outputs are in `verification/direct_output.txt` and `verification/compressed_output.txt`.

The source programs are standalone; no network access, external data, libraries beyond the standard Python library, or previously generated output is used to decide assertions. Exact integer arithmetic establishes finite tested cases only. The universal classification requires the case analysis in `RESULT.md`; the asymptotic requires the hypergeometric central limit theorem and Gaussian cone evaluation. The full work has not received independent scientific validation.
