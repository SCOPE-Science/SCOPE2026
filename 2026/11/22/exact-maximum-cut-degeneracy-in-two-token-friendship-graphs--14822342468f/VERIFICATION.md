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

# Mathematical and computational verification

The main theorem has an all-order proof in `RESULT.md`. Direct exact finite checks corroborate, but do not prove, the infinite statement.

Execute `python3 verify_formula.py`, then `g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct && ./verify_direct` from the directory containing the extracted source files. The first checker independently enumerates all \(16\) binary cross-petal matrices and confirms that the computed state compatibility matrix is
\[
\begin{pmatrix}7&5&5&2\\5&6&6&5\\5&6&6&5\\2&5&5&7\end{pmatrix},
\]
then compares all \(4^q\) ordered hub-state assignments to the closed expression through \(q=6\). Its expected output includes `INDEPENDENT_LOCAL_AND_PAIR_MATRIX_PASS`, `FULL_HUB_STATE_VS_THREE_TYPE_FORMULA_PASS q=1..6`, and `FORMULA_VERIFICATION_OK`.

The second checker explicitly builds the simple token graph from every parent triangle and enumerates all cuts with one token vertex fixed to color zero. It checks \(q=1,2,3\), with cut counts \(3,97,17239\), graph sizes \(3,10,21\), and respective cut values \(2,12,30\). Its expected output ends with `DIRECT_MAXCUT_CENSUS_PASS`.

The normalized asymptotic follows from the proof's analytic sum bounds rather than numerical extrapolation. Published scientific priority remains provisional; independent review is not claimed.
