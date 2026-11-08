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
# Verification scope

Run `python3 check.py` from this directory. The program uses only Python's standard library. The exact recorded result is `check_output.txt`; the separate `finite_residue_certificate.csv` lists every one of the \(44\) indices with nontrivial outer-generator gcd in the proved finite range.

The proof has two logically distinct components: (i) a symbolic argument showing that no new symmetric cases occur for any \(n\ge142\), using \(\gcd(P_n,P_{n+2})\mid35\); and (ii) an *exhaustive* finite check of all \(2\le n\le141\). Its two membership procedures agree for each finite case: a modular-inverse test and a direct loop over every possible nonnegative coefficient. It separately checks all pairwise-gcd identities and computes the Apéry sets for the four exceptional semigroups by shortest paths.

The observed complete symmetric list is \(\{2,3,5,40\}\). A separate countercheck finds \(F(4)=287\), \(g(4)=145\), so Frobenius parity alone is insufficient. Exceptional \((F,g)\) pairs are respectively \((43,22)\), \((133,67)\), \((1699,850)\), and \((258529,129265)\). The preexisting OEIS table also records the four Frobenius numbers, which are not novelty claims. This verification is not an independent scientific audit; nor does finite code alone prove the universal classification without its symbolic cutoff.
