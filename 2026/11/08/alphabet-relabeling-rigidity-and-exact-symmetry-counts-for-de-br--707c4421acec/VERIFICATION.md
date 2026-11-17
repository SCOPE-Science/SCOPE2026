---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For an ordinary de Bruijn cyclic word of length q^n, all n-blocks occur exactly once; the word has full primitive period. If sigma(S) is a rotation, its rotation has the order of sigma and must act freely on block positions. Considering constant blocks a^n forces every cycle of sigma to have that same length d>=2. Under this free action the de Bruijn digraph quotient is a voltage graph with q^n/d labeled edge orbits. For n>=3 each source representative has q outgoing edges with one common phase offset, so the total voltage is 0 mod d and a lifted quotient Euler tour cannot be one de Bruijn cycle. For n=2 the total voltage V=m^2*d(d-1)/2 (mod d), generating the phase group iff d=2 and m=q/2 is odd. The directed BEST theorem and matrix-tree cofactor of 2mI-2J yield T_m((2m-1)!)^m with T_m=2^{m-1}m^{m-2} (T_1=1). For n=1, orbit phase indexing and division by q rotations yields phi(d)d^{m-1}(m-1)!. Explicit counting of anchored quotient Euler tours independently yields 1,72,20736000 for m=1,2,3; only m odd lift to de Bruijn cycles. This treats nonidentity alphabet permutations, including uneven and fixed-point cycles, and n=1 boundary. Existence/count is analytical, not inferred from enumeration.

## originality

PASS

PASS best-of-knowledge: Etzion 2025/2026 full six-page primary text defines general binary and nonbinary self-dual cyclic sequences under complement/addition and studies feedback shift registers and single-track Gray codes. It is a broader *class of sequences*, not a stronger theorem counting ordinary complete de Bruijn cycles fixed by arbitrary symbol permutations; full text does not provide the all-permutation voltage-based q^n enumeration. The known binary complement case is explicitly not new; Burris–Motta–Shipman 2016 and Kari–Xu study reversal or antimorphic pseudo/unoriented variants, which do not imply symbolwise relabeling preservation of all n-blocks. No equivalent complete all-q all-n count found in semantic searches. Inaccessible Etzion 1987 article and 2024 monograph are genuine residual priority risks, not automatic novelty failures.

## value

PASS

A complete feasibility classification and exact labeled-alphabet count for symmetry-constrained universal cycles is a natural exact combinatorial invariant, not an arbitrary small census. The quotient-voltage obstruction explains why ordinary complete cycles cannot have any nontrivial alphabet symmetry at order >=3 and pinpoints the exceptional q=2 mod 4 order-two case; BEST converts that structural classification into exact counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
