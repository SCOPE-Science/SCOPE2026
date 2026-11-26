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

For the geometric hyperelliptic fibre H, use 2P_i∼H, K∼3H and ΣP_i∼5H. For odd |S| the theta class is Σ_{i∈S}P_i+(3−|S|)H/2, invariant under S↔S^c. Distinctness except complements follows from the even-subset 2-torsion model: a putative nonempty relation can be complemented to even size at most 4. Choose a branch point outside that subset at infinity and take H twice that branch; functions with only a pole there of order ≤4 are polynomials in x, so cannot have the required simple zeros at finite branch points. The 256 classes exhaust the geometric theta torsor. For S of sizes 1,3,5 put a branch outside S at infinity in a degree-nine model. Multiplying a section by ∏_{i∈S}(x−x(P_i)) converts it to a polynomial function with pole order ≤3+|S|≤8 at infinity and zeros at those x-coordinates; y has order of pole 9, so only polynomials in x occur. This gives h⁰=2,1,0 respectively. The divisor construction is Frobenius-equivariant without a rational branch assumption. A fixed triple is a union of cycles; a fixed complementary pair of five-subsets arises from a fixed representative or from membership alternating on every branch cycle. The latter has 2^c representatives on c all-even cycles and zero otherwise. Independent orbit traversal on all 42 partitions, checked against both formulas through each order, confirms 40 joint, 40 odd-only, 37 even-only spectra and both stated collisions. Signatures refine from 22 to 33 to 39 to 39 to 40, so the five-count partition of branch types equals the full joint-spectrum partition; (10) and (5,5) demonstrate strict insufficiency through four. The orbit multiplicities give the two finite étale zeta functions. For odd descent one can fix a triple by an extension equal to the length of any branch cycle of length ≥3 (degree ≤10), or degree at most two if all cycles are shorter; a ten-cycle cannot stabilize a three-subset under any nonidentity subgroup, establishing sharpness. Exact irreducibility tests confirm all seven F₃ factors and six squarefree realizations. Replay: python3 /workspace/branches/ff3a3b34-edc5-46ed-9228-354f6c4d6c51/independent_check.py; independent_check.txt records the results. The bundled TSV was located in the frozen source and separately checked read-only row by row for all 42 spectra and displayed first-five pairs by the fixed-point formulas at powers through branch order and at least five; no supplied script was executed.

## originality

PASS

The distinct claim is the complete genus-four classification of the joint spectra (including that these are the only two collisions), together with the exact extension cutoff and witnesses. The (8,2)/(8,1,1) collision in isolation is demonstrably covered by the r=1 case of the distinct 55c98e92ef95 catalogue theorem and is not credited as an original component. Same-day dating does not order the results. The classical theta correspondence is not claimed as new.

## value

PASS

The two finite étale theta schemes are natural arithmetic invariants of a hyperelliptic curve. The classification separates permanent limits to identifying branch splitting from an apparent ambiguity that just one more extension resolves. A sharp cutoff for their zeta functions is useful independent of reconstructing the curve itself; it is stronger than enumerating sample curves, or using the order of a branch permutation as a generally larger cutoff. The realized witnesses make both types of informational obstruction concrete.

The dated certificate retains the supplied scientific assessment, sources and limitations.
