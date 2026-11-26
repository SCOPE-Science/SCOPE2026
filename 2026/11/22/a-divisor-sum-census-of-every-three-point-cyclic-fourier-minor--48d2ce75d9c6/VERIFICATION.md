---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the normalized unit-modulus matrix with first row and column ones, singularity is (u−1)(t−1)=(v−1)(w−1). When nonzero, conjugate and divide to get ut=vw, then u+t=v+w, so the pairs coincide and two rows or columns coincide. In the zero case one factor from each side vanishes, giving a row or column equal to the first. The possible (k_R,k_C) are (0,0) at rank 3, (1,0),(0,1),(1,1) at rank 2, and (3,3) at rank 1, so the −9 overlap at rank one explains the +4 correction in the singularity indicator. A difference of gcd a has an annihilator of size a and gives Nφ(N/a)/2 unordered pairs (including the self-opposite nonzero difference, since reversing an ordered pair still changes its endpoints); (N/a)·binom(a,3) counts allowed column triples in annihilator cosets. For simultaneous pairs, N|de iff N|ab by truncated prime valuations, and there are a−2 and b−2 completions in the relevant cosets. A size-one annihilator cannot occur on either side for an admissible simultaneous pair, and a size-two annihilator contributes zero. For rank one, all row differences generate the subgroup with gcd h and a complete column triple lies in a common-annihilator coset. The incidence k|h amounts exactly to k·binom(N/k,3), which inverts to M_h on the divisor lattice. This reconstructs all three formulas, including the prime boundary P=Q=L=0. Independent exact replay at /workspace/branches/3a9629ab-ac15-450f-93ec-7b3369112b66/rank30_exact_replay.py checks every anchored pair via integer cyclotomic reduction, giving (180,15192,149464), with largest reduced coefficient magnitude 6. In a double count with anchors, each unrestricted pair has 9 anchor choices, and each anchored pair has 30² translated preimages with anchors, giving scale 100 even when some triples have stabilizers. The divisor intermediates P=919800, Q=374400, L=18000 agree. This corroborates N=30, not the all-N argument. Complex rank only, no larger minors or stability conclusion.

## originality

PASS

Bounded statement and implication comparisons support originality of the complete arbitrary-modulus rank census, not of the singularity mechanism or special cases. Existing criterion, extremal support and block formulations do not on the checked evidence already supply the all-N multiplicities. Inaccessible material limits the historical verdict.

## value

PASS

The rank is exactly the dimension of the observed signal subspace for a specified three-point cyclic sampling and three selected frequencies. Counting separately one- and two-dimensional deficiencies, including their overlap, is stronger than showing a singular minor exists, classifying extremal supports, or tabulating a few moduli. The formulas replace all-triple enumeration at every cyclic order with integer divisor sums and explicitly pass beyond prime powers and products of two primes. This is a useful exact reference for third-order degeneracy, not a guarantee of good conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
