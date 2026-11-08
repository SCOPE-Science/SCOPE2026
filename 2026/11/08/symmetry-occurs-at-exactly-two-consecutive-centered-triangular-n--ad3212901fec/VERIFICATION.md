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

Run `python3 check.py` using Python 3 standard library. The program computes exact numerical semigroup Apéry representatives by Dijkstra's algorithm for every index from \(2\) through \(120\). It separately evaluates all three possible nontrivial pair-gcd gluings and matches the symbolic classification. It checks \(F(S_2)=25\), \(g(S_2)=13\), \(F(S_8)=2203\), and \(g(S_8)=1102\). Expected console output is in `check_output.txt`. A finite case check does not prove a universally quantified statement; see the complete arithmetic proof in `RESULT.md`, in particular the infinite bounds and exact congruence exclusions. The cited three-generator symmetry criterion is a mathematical premise from the literature.
