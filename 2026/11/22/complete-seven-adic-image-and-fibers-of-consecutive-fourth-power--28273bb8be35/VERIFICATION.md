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

# Reproduction of the finite residue and fiber checks

Run `python3 checker.py` with Python 3. No third-party libraries and no other data files are required. The source builds every complete histogram for \(F(n)=\sum_{j=1}^n j^4\), for \(0\le n<7^k\) and \(1\le k\le6\), using the exact recursive difference \(F(n+1)-F(n)=(n+1)^4\). Separately it lifts the unique critical point in \(1+7\mathbb Z_7\), counts all modular squares, evaluates the proved closed-form fiber formula for every target, and compares the two histograms target by target.

Observed execution: `PASS 274512 exact checks`, with image sizes `5, 23, 155, 1073, 7505, 52523`. It also checks \(c\equiv43\pmod{49}\), \(A\equiv50\pmod{343}\), and \(u\equiv6\pmod7\). The standalone checker is a reproducibility aid; it does not prove all depths, seven-adic isometry, novelty, or mathematical value. Those require the algebraic and analytical arguments in `RESULT.md`. Independent audit has not been performed.
