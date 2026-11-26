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

For a harmonic quartic, the x_i² coefficient in its Laplacian is 12a_i+2Σ_{j≠i}b_ij, and only the indicated pure, pair-even and pair-odd monomials can affect the samples. Substitution gives (1). Conversely the pair-odd term in (5) is harmonic, since Δ[x_i x_j(x_i²+x_j²)]=12x_i x_j and Δ[r²x_i x_j]=2(n+4)x_i x_j, and its difference on its own samples is (n−2)/(n+4); the even part is harmonic by (1). Independence of the equations follows from q_i+q_j=0 for each pair, which forces q=0 for n≥3. For the spectrum, the degree-four zonal kernel normalized to dimension at equal points gives (6). A difference of the sign samples cancels all cross-pair entries and contributes k_1−k_0. For the sum samples, distinct edges sharing one vertex give 2k_q and disjoint edges 2k_0, giving exactly (7). The incidence decomposition MM*= (n−2)I+J gives the pair sector and the standard and constant 2×2 blocks. Those blocks each have one zero eigenvalue in every copy, by the already proved rank and their positive short-root diagonal; their traces factor as stated in (2). For the collision and extremum checks write c=n(n+6)/24. In units of c the differences std−odd, pair−odd, std−pair, triv−pair and triv−std factor as (n+2)(n−8)²/8, (n+2)(20−n)/4, (n+2)(n−12)(n−2)/8, (n+4)(n−1)(n−6)/4, and n(n+10)(n−4)/8, respectively. The remaining difference triv−odd is (n³−4n²−4n+64)/4>0 for n≥3. These give the asserted collisions and active extrema with the absent pair sector at n=3. The ratios at n=3,4,5,6 are 33/8, 3, 9/4, 15/8; the next ratio at n=7 is 121/60. The two rational formulas in the proof are strictly increasing on their subsequent intervals by their given derivatives and agree at n=20. Thus the sharp minimizer and normalization are correct. Replay: RESULT.md equations (1)–(7) and steps 3–4. The supplied symbolic/finite diagnostic code was read, not executed.

## originality

FAIL

The strongest distinct indexed record gives all-degree unweighted sampling on precisely the same two normalized root orbits. Its parity reduction and dimension normalization account for the apparent differences in the Gram matrices. At degree four its sectors are exactly those underlying this Finding; the spectrum, rank and range relations follow by elementary specialization, and the collision and minimizer reduce to comparison of the resulting four polynomials. The monomial interpolant is a convenient explicit implementation, but in the stated scope it does not establish a separate invariant or interpolation guarantee beyond the known blocks. The frozen result is mathematically correct; substantial coverage and direct implications, not dates or inaccessible papers, dispose of the originality claim. No priority or derivation order is asserted.

## value

PASS

Exact image constraints and spectral conditioning matter for solvability and noise amplification on a natural two-orbit sample set. The family-specific n=6 comparison is useful as an interpretation of the spectrum, not a global design optimum. The covered formulas and direct specializations remain useful mathematics, but the narrower monomial recipe alone does not supply a distinct contribution worth proposing as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
