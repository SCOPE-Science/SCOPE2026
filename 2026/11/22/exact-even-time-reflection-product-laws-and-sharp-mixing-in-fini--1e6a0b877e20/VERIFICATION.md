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

I rechecked the final RESULT.md in repairs/5. An ordered pair of distinct eigenspaces parametrizes the split trace-zero involutions, so there are q(q+1); an even product lies in H and negating one factor preserves its law. For nonscalars, the companion form of g and the condition tr(rg)=0 give (a-tb/2)^2-(t^2-4)(b/2)^2=1, with exactly 2q, q-1 or q+1 solutions depending on the discriminant. The scalar cases allow every r. Pantangi–Sin Table 1 yields the even-pair scalars 1, q^-2, 4/(q+1)^2 and 0. Determinant twists give the uniform law on H and q-1 identical Steinberg restrictions give q^(1-2k)S in the relative density. The other surviving sector has a single decay base, so matching the two-factor law fixes C uniquely for all positive k; inserting the fiber counts reproduces the four entries. The type cardinalities follow from the Jordan centralizer and split/nonsplit inverse eigenvalue pairs. The split density deviation is strictly negative since the ratio of the competing positive term to the negative magnitude is q/(q+1)*((q+1)/(2q))^(2k)<1; the nonsplit deviation is purely negative and the repeated-root deviation is nonnegative. Hence the same test set {Delta=0} attains total variation at every time. Its two type counts give the displayed coefficients, while the table gives E S^2=1, E SC=0 and E C^2=(q-3)(q+1)^2/4 for chi-square. For q=3 there is no split-regular class and C vanishes identically; q>3 has the stated larger dominant decay base. All arguments work over odd extensions. In the repaired literature comparison, antisymmetrizing Ad_r on traceless matrices gives the orthogonal reflection -Ad_r about the Q=-det norm-square axis; independently changing signs of the two lifts leaves two lifts to each prescribed determinant-one representative. This is consistent with the degree-two and projective counts.

## originality

PASS

This is a pass on the repaired scope only. The frozen novelty framing included the displayed formulas without separating the known exact two-factor law from the all-time reduction. Parashar–Patel implies every two-factor fiber, not just support, and the same-date orthogonal result also recovers those fibers via the degree-two quotient. The corrected file preserves the formulas with explicit credit and does not claim novelty for the pair counts, character eigenvalues or chi-square from multiplicities. The surviving claim is the evaluated all-time total variation obtained by resumming the density into four strata and proving a common extremizing set. The older general class-product and class-scheme results supply the initial data and eigenvalues, but no evaluated all-time positive-part formula for this walk was found in the inspected sources.

## value

PASS

For a natural central walk with determinant periodicity, mixing on the even-time coset is an intrinsic question. The exact TV, unlike a spectral rate or chi-square, identifies a time-independent event attaining the maximal discrepancy and quantifies the full finite-time error. It detects the loss of the second mode at q=3 and distinguishes two-point mixing in the single-class walk from a mixture of orthogonal reflection types. The repair does not assign standalone value to rediscovering pair counts or recomputing a character table; it isolates the evaluated sign-sensitive invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
