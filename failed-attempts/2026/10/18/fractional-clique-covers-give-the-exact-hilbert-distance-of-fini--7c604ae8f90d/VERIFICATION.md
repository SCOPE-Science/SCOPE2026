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

For any invertible real T to Hilbert space and any x, apply the two operator norm bounds to the coordinate vectors and the signed copies of x: sum_i x_i² = sum_i N(x_i e_i)² ≤ ||T^(−1)||² sum_i ||T(x_i e_i)||² = ||T^(−1)||² E||T(sum_i eps_i x_i e_i)||² ≤ (||T|| ||T^(−1)||)² N(x)². Here the orthogonality is in the Rademacher expectation, not an assumption that the Te_i are orthogonal. The identity attains the resulting sharp bound since N≤||·||_2 with equality on e_i. Substitution t_i=x_i² gives the bounded packing LP, whose dual is exactly fractional cover; the singleton constraints ensure boundedness and the finite rational LP gives rational value. Cliques of G are independent sets of its complement. Perfection gives integrality on every nonempty induced subgraph by complement closure and omega≤chi_f≤chi; conversely the strong perfect graph theorem gives an induced odd hole or antihole. The two matching certificates are uniform weights 1/2 on vertices and on cycle edges for the former, and uniform 1/k on vertices and on the 2k+1 cyclic translates of a maximum independent k-set for the latter. This gives (2k+1)/2 or (2k+1)/k, nonintegral for k≥2. Replay: frozen RESULT.md proof §§1–4 and the Rademacher calculation here. The finite rational checker was inspected, not executed; it is not used to prove any of the general quantifiers.

## originality

FAIL

The closest earlier indexed result supplies the exact same numerical invariant on the square variables, not merely a similar LP: for g_F(u)=max_F sum_(i in F)|u_i| it gives ||id:g_F→ell_1||=tau*(F). Substituting u_i=x_i² makes that norm exactly the squared canonical Hilbert distortion. The standard Hilbert cotype comparison applied just to x_i e_i gives that same distortion as a lower bound for EVERY real-linear isomorphism (calculation under correctness). Thus the older formula and elementary unconditional atomic comparison mechanically give even the unrestricted identity, including optimality of the coordinate comparison. The earlier result itself does not assert unrestricted Banach–Mazur distance. The induced-perfectness statement then follows from the classical coloring bounds and odd-hole/antihole obstruction with uniform weights. There is no separate surviving claimed result beyond these implications. This is implication coverage, not a claim that the same Hilbert-distance sentence was located verbatim.

## value

FAIL

The underlying question about unrestricted distance is natural and the exact value is usable, but the submitted increment is the routine atomic cotype comparison applied to a previously evaluated equivalent norm invariant, followed by the standard odd-hole/antihole obstruction. It claims no additional optimization result (such as classification of optimal forms), obstruction or quantitative invariant beyond that mechanical conversion. No independently useful unknown exact remainder is established as framed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
