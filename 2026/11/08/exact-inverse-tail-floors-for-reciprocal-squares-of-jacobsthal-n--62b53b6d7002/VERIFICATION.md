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

# Reproduction and limits
Run `python3 checker.py` using Python 3 and its standard library. The checker computes exact rational lower and upper bounds for each infinite tail \(S_n\) for \(1\le n\le64\): the first omitted summand index is \(K=2n+24\), and the omitted positive tail is below \(64/(3\cdot4^K)\) because \(J_k>2^{k-2}\) for all \(k\ge3\). Inverting gives a rigorous rational enclosure, and both endpoints have the integer part claimed in the finding. For \(n\ge3\), both endpoints also lie within the strict \(1/9\) enclosure. The checker separately tests rational coefficient inequalities at \(x=1/8\) and the first three modular residues.

The finite program is independent supporting evidence, not an exhaustive infinite search or proof of novelty. The all-index proof consists of the explicit absolutely convergent expansion, the uniform coefficient bound, and the modulo-36 argument in `RESULT.md`. No expert validation or independent audit has been performed.
