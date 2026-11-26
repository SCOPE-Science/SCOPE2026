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

Disjoint nonempty branch quartets give independent geometric square classes. The connected tame degree-four cover has eight branch fibers each contributing two to Riemann–Hurwitz, hence genus five. For M in PGL₂ the quartic transformed by a GL₂ representative of M⁻¹ has the same roots as the new branch quartic, so their proportionality constant specifies a twist bit, independent of the matrix representative modulo squares. Projectivity orbits therefore give actual isomorphisms of the normalizations. An analytic check of the orbit computation: the harmonic cross ratios {2,4,6} and equianharmonic ratios {3,5} give respectively 21 and 14 complementary partitions, each transitive. Complementation preserves the two quartet orbits (of unequal cardinality) and a projectivity can swap the two quartets in either representative partition. For the harmonic representative A={∞,0,1,2}, the involution x↦2−x fixes both sets and has quartic multipliers −1 and +1, so flips only A's twist. Conjugating by a swap flips only B's twist. Thus the four twists form one orbit over the harmonic partition. In the equianharmonic case the four twists are identified by their ordered elliptic traces ±4, and the swap is transitive on the two opposite-sign assignments. This gives sizes 14,14,28,84 and stabilizer orders 24,24,12,4 in the base group of size 336. The product quotient is a twist of y²=x⁷−x; over F₄₉ its trace-zero image has six nonzero elements, all squares, and the quotient attains 92 points. Equality in the Weil bound and trace zero over F₇ give numerator (1+7T²)³ for both twists. The three quotient numerators multiply (equivalently, use the quadratic-character identity on fibers, including the disjoint branch fibers). The genus-one traces are 0 for the harmonic pair and ±4 for the equianharmonic pair. The four resulting numerators are distinct: the two same-sign pairs have opposite nonzero linear terms and the mixed and zero cases have quadratic coefficients 19 and 35. Hence no abstract F₇-isomorphism merges different orbits. The point counts and the distinction between base stabilizers and full automorphism groups follow as stated. The frozen note and the nested scripts/verify_orbits.py were inspected, not executed. The independent /workspace/branches/1df7bacd-c46d-4f16-aba9-55e6a98a4540/independent_replay.py exhausts 336 projectivities and 140 presentations, including all projectivity compositions, multiplier and trace checks, and the F₄₉ quotient point count. No assumption that every abstract isomorphism descends to the designated base is needed.

## originality

PASS

Pass for identifying the twist-aware projectivity orbits with the abstract F₇-isomorphism classes, not for the Weil spectrum, marked-model frequencies, or bare partition orbits. The distinct same-day Resultary 2398017db203 covers the identical 140 models, exact Weil numerators and frequencies, and the harmonic/equianharmonic partition calculation. Its proof and verification do not identify the action on the two independently twisted equations; a marked-model spectrum only bounds the number of abstract classes from below. In particular, in the harmonic family all four twists over a partition have the same trace pair, so those arithmetic data cannot establish transitivity. The new input is simultaneous control of both twist multipliers under the projectivity action (for example the independent bit flips verified above), and thus a matching upper bound and exact stabilizers. The same record's date does not establish priority.

## value

PASS

The designated eight points are the entire base rational line, and this is a natural finite complete classification of disjoint elliptic fiber products, not an arbitrary sample. A researcher using the known arithmetic table cannot tell whether its 84 maximal-over-F₄₉ presentations represent one F₇-isomorphism class or many. The twist-aware classification answers exactly that question for every stratum, with explicit base stabilizers and no assumption about extra automorphisms. This makes the isomorphism result useful independently of the overlapping point counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
