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
# Reproducibility and verification

Running `python3 verify.py` from the standalone file directory requires Python's standard library only; no network access, cached tables, or external datasets are used. `verification_output.txt` is the recorded exact successful run.

The checker reconstructs all \(20\) centers and their radius-two balls (\(10\) vertices each), and enumerates every face. It constructs the ten antipodal pairs, verifies that no face is invariant, checks exactly six relabeling orbits that exhaust all \(960\) non-antipodal triples, and verifies the two-skeleton identification.

For both the original complex and the geometric complement quotient, the program constructs actual integer cellular boundary maps, checks every \(\partial^2=0\) identity, and computes the ranks over \(\mathbb Q\) using exact fractions. The quotient is constructed using oriented face orbits (including signs), never using the wrong naive ten-vertex simplicial quotient. It recomputes all rational Betti numbers and Euler characteristics, and confirms the involution traces by the transfer formula.

The infinite-looking topological conclusion \(\pi_1(Y)\cong\mathbb Z/2\) does not arise from a numerical fundamental-group guess: the displayed orbit classification proves \(X^{(2)}=\partial C_{10}^{(2)}\), where \(\partial C_{10}\cong S^9\), and the free complement double cover is then universal. The finite verifier checks the premises for this deduction exactly.

The checker does not compute the integral higher-homology groups, does not assert a complete quotient homotopy type, and does not establish the absolute absence of prior equivalent results. Independent audit has not been performed.
