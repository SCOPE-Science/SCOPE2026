---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The regular Fourier fibers are complete (two full cyclic Fourier bases with opposite frequency signs), L_x=diag(ζ^k,ζ^−k), L_y off-diagonal with entries (−1)^k and 1. Left translation multiplies by an invertible operator. For a pure normalized support the scalar 1+ζ^{ka}+ζ^{kb} vanishes exactly when its final two terms are the opposite primitive cube roots. Bezout for gcd(a/d,b/d,2n/d)=1 forces k to have order three modulo M; the opposite residue condition admits both such k, with d lifts each and two kernel directions per lift. A mixed block has determinant |1+ζ^{ka}|²−(−1)^k. Odd blocks are invertible; even blocks lose one rank at each of the 2d solutions of the two cube-root congruences exactly when 3|n/d. This also handles a=n (no singularity). For eligible mixed d there are 2φ(n/d) admissible differences; count ordered pairs and singleton then divide by two. Proof line 84's phrase 'for each divisor' overstates the raw nonzero-difference count for d=n, where there is one; this ineligible class is never used in the census. For the pure side count primitive ordered pairs with opposite nonzero residues modulo three by CRT, multiply by 4n base points and divide by six; the gcd and residue class are invariant under reanchoring. Summing the mixed totients gives 8n³(1−3^−v); summing the pure local factors gives (2n³/3)(1−3^−2v). Maximal d=2n/3 in the pure case forces the subgroup cosets and beats the mixed maximum 2n/3. Verified the frozen checker is modular for sampled ranks and does not prove complex ranks. Independent replay /workspace/branches/frozen-review-replay.py exhausts n=2,3,6 by exact rational rank of full integer convolutions up to left translation; n=6 has frequencies {0:744,2:576,4:672,8:24,16:8}.

## originality

FAIL

The full dihedral census in Resultary 2bbf4bdce108 mechanically implies the frozen census, not just an analogy with a different group. Pure supports use the identical cyclic operator on two cosets, hence the pure part of the dihedral theorem at rotation order 2n. Mixed supports have exactly the quotient-dihedral nullity: the central-odd sector of the dicyclic regular representation is invertible, while its central-even sector is the regular representation of the dihedral quotient at rotation order n. All three-element mixed quotient supports lift with exactly eight choices, and collapsing pairs are invertible. Thus both divisor counts, the total and the extremizing geometry are transferred, leaving no distinct three-tap invariant in the claim. This is an implication assessment, not a conclusion about authorship or public priority from path dates.

## value

FAIL

Exact singular-support distributions are a worthwhile type of invariant, but this census is a mechanical finite-cover/quotient transfer of an existing exact census. The frozen claim offers no remaining distinct invariant, twisted-sector spectrum, or broader new transfer result. No repair proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
