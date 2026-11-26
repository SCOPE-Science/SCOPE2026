---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Each even cut-edge set is one vertex up to complement; even flips identify all vertex charts. In the zero chart even binary exponents split into weight-two pairs and the pairs generate the even-sum lattice. The degree-sequence inequalities give saturation: for a nonzero even total 2d with maximum ≤d, decrement two largest positive degrees. The new maximum is ≤d−1 (a third degree d is impossible); induction pairs all half-edges without loops. Weight-two generators are extreme rays and give the edges. With q₁₂ inverted, a_i=q₁i/q₁₂ and b_i=q₂i/q₁₂ generate the degree-zero subring, and q_ij/q₁₂=a_i b_j for i,j≥3; a_i,b_i are precisely a rank-one two-row matrix since in the Laurent parameterization they are z_i/z₂,z_i/z₁ and realize the dense torus of that cone. The invertible degree-one coordinate splits off G_m. A rank-one matrix is smooth when an entry is invertible, and the origin is singular for n≥4. The vertex of the full cone has embedding dimension binom(n,2)>n. Thus exactly the incident axes are singular in each chart; gluing gives the stated line arrangement and endpoint count. On the Segre cone the hyperplane class is (1,1), with degree n−2; its divisor class group is Z² modulo (1,1), and the canonical class is (n−4) times a generator up to sign. At a fixed vertex the 2n forms x_i and (Σx)/2−x_i are primitive facet forms (complementary complete graph and star); the map from L is saturated because integral evaluations force both integral coordinates and even sum. Its cokernel has rank n. For localization at an affine toric apex one loses no classes: a non-boundary divisor avoiding the apex is defined on the torus by a Laurent prime f, dividing a chart polynomial with nonzero constant term. With a positive grading, the lowest-degree terms of f and the complementary Laurent factor are inverse monomials up to scalars. Their valuations sum to zero on every boundary divisor, so each factor's lowest monomial already attains every boundary valuation; dividing f by that monomial makes its global divisor principal with no boundary terms. Localization therefore kills only zero classes. The same argument at a non-fixed point applies to the Segre cone times a translated affine line, which is an open enlargement of the local product and adds no divisor class. At a fixed point canonical height one requires x_i=1 and n/2−1=1; n=4 gives an integral solution and the normal semigroup ring is Cohen–Macaulay. The non-fixed canonical test gives the same cutoff. Thus the statement concerns reduced support and ordinary local rings; no nonreduced Jacobian or completed class groups are inferred. Archived numerical edge tests and modular ranks are not used as an all-n proof.

## originality

FAIL

The distinct indexed cycle-cut theorem 47ef75dbf57d gives the complete reduced arrangement, incidence, all edge charts, multiplicity and Gorenstein boundary on the same normal parity toric variety (in arbitrary characteristic). Its proof supplies all 2n primitive rays at the fixed points in the exact dual lattice. The omitted local class-group jump follows mechanically from these explicit rays and the edge germ by the standard toric divisor sequence (the rays generate the full dual lattice) and the standard Segre-cone quotient. Neither the exact monomial presentation of the vertex chart nor the pointwise canonical test introduces a remaining gap in that source's data. This is demonstrable coverage, not a historical priority assertion based on the dates.

## value

PASS

The singular arrangement in arbitrarily large dimension and the local class-group jump are informative geometric features of a natural family. The precise torsion-free groups and canonical behavior are relevant to local factoriality and birational modifications. This judgment concerns the structural content, not whether the mechanically covered information constitutes a separate new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
