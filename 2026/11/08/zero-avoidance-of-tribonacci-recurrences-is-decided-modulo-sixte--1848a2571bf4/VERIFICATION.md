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

# Reproduction and mathematical verification

Run `python3 check.py` using standard Python 3 with no extra dependencies and compare its complete standard output to `check_output.txt`.

The program exhaustively partitions all \(4096\) residue triples modulo \(16\) into cycles, identifies the primitive cycles, checks their zero-incidence, and confirms that every one of the 72 zero-containing primitive cycles has an orbit state satisfying \(a_n\equiv0\pmod{16}\) and \(a_{n+1}\not\equiv0\pmod4\). It checks the exact \(T^{16}\) matrix and \((T^{16}-I)/8\pmod4\), then separately tests all starting triples modulo \(2^r\) for \(1\le r\le6\), including cycles of all lengths. The saved expected output reports the exact counts.

The universal conclusion for all \(r\) requires the induction in the Proof section of RESULT.md: for each \(k\ge4\), the matrix identity for \(T^{2^k}\), followed by a choice of one of two powers of \(T\), toggles the next bit of a zero first coordinate while preserving the second coordinate modulo four. Finite computations are the *exhaustive base case* and independent finite cross-checks, not an extrapolation to an infinite theorem.

No third-party proof checker or independent scientific audit was performed. The original general-period matrix congruence appears in Klaška (2008), and the present zero-incidence lifting is independently reasoned here.
