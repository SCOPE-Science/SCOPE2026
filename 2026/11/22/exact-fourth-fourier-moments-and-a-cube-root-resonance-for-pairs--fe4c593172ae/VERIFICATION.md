---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On a two-sum fiber with first coordinate s, completing the square gives 1+chi((a+b)t-ab s^2) for a+b nonzero; at a+b=0 the exceptional fiber is s=0 with mass q at t=0. The three centered convolutions have squared norm q(q-1), and their off-diagonal products cancel between s=0 and s!=0 by the two-root sum; for an opposite-curvature mixed term the s=0 pairing cancels directly. This proves weighted energy 22q^2-6q. Removing the duplicate origin changes f*f to f*f-2f+delta_0. Evaluating the mixed incidence on the branches and the exceptional sum at zero gives exactly the base polynomial and the two character terms plus the opposite correction. Expanding the sign indicators gives both censuses, with the product sign reducing to chi(lambda) away from the omitted points in characteristic three. The cubic is squarefree in characteristic >=5 and the Hasse lower bounds ensure the required non-opposite sign classes for q>=31; the characteristic-three count handles q>=27 and the finite transition table reaches q=17. The opposite value beats all others when q=2 mod 3, but the original SLOGAN.txt asserted an unqualified iff, false at q=3 where -1 is the sole admissible ratio. The replacement slogan limits the iff to q>=17 and identifies the lower envelope as the one first attained at 17; this matches the proved Result. The frozen CHECK.py did not assert the named transition table or the characteristic-three sign census. The replacement checker now checks those items, all small extrema and both versions of the energy on the same 240 cases. It ran successfully. A separate independent difference-counting implementation checked 319 ratios, including q=81, and reproduced the small and transition tables and both sign-census formulas. The theorem in RESULT.md is unchanged; the pass is for the repaired package, not the original unqualified slogan.

## originality

PASS

The result supported as distinct is the whole-curvature weighted and union energy profiles, full sign census and sharp envelopes, not the generic Fourier/energy reduction, standard Gauss and Hasse facts, or the opposite-prime-field moment recoverable from a previously given kernel. Narrowing the headline to the proved large-field unique-maximizer classification leaves this mathematical increment intact.

## value

PASS

For equal-size reducible conic supports, the fourth moment naturally measures the contribution of cross-branch coincidences. The exact comparison between the constant multiplicity energy and the variable ordinary union energy isolates a single-point correction, and the character census and sharp smallest persistent lower cutoff quantify effects that the known opposite case cannot detect. This is a family-wide invariant and a maximizer classification, not a recomputation of the known endpoint norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
