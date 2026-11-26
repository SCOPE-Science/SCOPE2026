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

For n=7m+d and j=7k+e, Lucas factors the low digits. A carry from d+e>=7 makes the units digit of n+j smaller than e, so these terms vanish. This is also precisely where the corresponding low-digit binomial for A(d) vanishes; the surviving sum separates. Original-binomial evaluation at d=0,...,6 gives residues (1,5,3,3,3,5,1), and hence nonvanishing signs and digit sum -3. Splitting the cyclic correlation into low-digit carry classes proves the stated recurrence with the top-block wrap. The no-carry and carry signed sums give the displayed rows. With L=7^(r-1) and c=C_(r-1)(1)=(L+2)/3, the only boundary minimum is c-2L at h=5 and its negative; the boundary maximum is 2L+c<3L for L>=7. Interior cases have absolute value at most 9L/7, below (5L-2)/3. Multiples of seven inherit the sharp maximum and miss the new minimum by at least 4, including the step from r=1. The sign-pair count is obtained by expanding (1+sigma*s(n))(1+tau*s(n+h))/4 and using equality of the two cyclic marginals. Independent replay `python3 /workspace/reproduce_frozen.py 5` computes original binomial sums through n=342 and checks every correlation and sign-pair count at depths 1–3 (399 depth/lag pairs); the supplied CHECK.py was inspected, not executed. The proof, not the bounded checks, covers all depths.

## originality

PASS

The mod-seven digit residues and nonvanishing are known. The supported distinct contribution is the exact finite cyclic all-shift extremal classification for the quadratic character, not the Lucas congruence, a generic two-state carry method, or the elementary inversion of two signs alone. The closest distinct same-day Apéry record concerns a different character and base and takes an unwrapped limit; no implication of the assigned finite classification was established.

## value

PASS

A natural sign sequence from an established nonvanishing Apéry congruence has a precise scale-dependent distinction: the positive maximizer moves with the block depth while the most negative shift stays fixed up to sign. The exact finite extrema and their full equality sets quantify this difference; complete pair frequencies follow without assuming an unwrapped limit. This is not just a new tabulation of digit residues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
