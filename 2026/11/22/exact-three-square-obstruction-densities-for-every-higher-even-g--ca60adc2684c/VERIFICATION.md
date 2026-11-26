---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Starting from the stated recurrence and initial data, the exponential generating function solves (1−z)G'=(v+z)G and G(0)=1, hence is e^(−z)(1−z)^(−v−1). Its coefficients give exactly the signed falling-factorial interpolation, independently of the cited counting convention. Each falling factorial on Z_2 has floor(j/2) even factors; in a telescoping divided difference on odd arguments at most one such factor is dropped, since x−i and y−i have the same parity. This proves uniform convergence of both series. Modulo 2 the divided difference is P'_j(1), equal to 1 for j=1,2,3 and zero otherwise; the corresponding binomials have parities (1,1,1) or (1,0,0) as v is 0 or 2 mod 4, so the quotient is odd. Recurrence parity gives D_n even exactly at odd indices, and the isometry gives an injection and hence a bijection between odd and even residue sets of equal size at each 2-power precision. The compatible inverse limit gives the unique odd zero, exact valuations, digit lifts and the unique preimage of each prescribed shell residue. For even indices an independent finite-sum replay /workspace/record1_replay.py computed the four modulo-eight rows and verified (D_8,D_9)=(D_0,D_1) mod 8 for all parameter residues; recurrence periodicity proves the identity D_(2t)≡1−vt mod 8 at every t. The same replay checked the v=4 and 6 examples and the odd-fiber bijections at 128. Legendre's criterion yields the disjoint progressions, including exactly the stated even-index class when v≡2 mod 4. The odd progression densities sum to 1/24; beyond the first O(log X) shells all indices occupy a single root class of modulus greater than X and contribute at most one, while the omitted geometric main term is bounded. Adding the possible 1/8 gives the claimed densities and discrepancy. The proof is all n for fixed even v≥4; the frozen checker was inspected but not run. Its printed pair-test description is loose: it uses odd n<32 and n<m<42, not literally every odd pair below 42; this does not affect the proof.

## originality

PASS

Ulas states the same-sequence even-parameter questions and only restricted congruence obstructions/lower bounds. The closest exact indexed results solve v=0 and v=2 only; the latter supplies a stronger global isometry at its single parameter but explicitly does not treat v≥4. The broader p-adic interpolation article addresses different sequences and uses a Lipschitz condition rather than this exact odd-input equality. None of these statements furnishes the parameter-uniform theorem for the claimed regime. No priority order between the distinct same-date v=2 record and the audited record is inferred.

## value

PASS

A named arithmetic classification problem for an infinite even-parameter family gets an effective valuation root, full index criteria and a quantitative density. The sharp change between 1/24 and 1/6 comes from an even-index progression absent in one parameter class; it is not visible from a v=2 calculation. Root lifting and the disjoint shell description can be used to decide individual indices as well as predict counts. The method does not claim an elementary closed root or more general representation statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
