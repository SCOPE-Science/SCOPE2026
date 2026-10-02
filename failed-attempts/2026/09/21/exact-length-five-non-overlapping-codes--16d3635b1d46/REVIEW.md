# Independent mathematical audit

## correctness

PASS

Starting from the established SQN(q,5) integer program, the proof correctly uses left-right symmetry and endpoint linearity in the final partition variable. The two remaining quadratic branches are bounded analytically: the unbalanced branch forces the Blackburn pattern at equality, while the balanced branch lies strictly below a universal normalized threshold; q=7 and q=2,3 are handled exactly. The real maximizer of ell^4(q-ell) and adjacent-integer comparison give the stated unique split for every q>=4, and the equality conditions force the claimed structures/count. The verifier independently checks the full endpoint-reduced SQN for small q and larger finite ranges, but the all-q theorem rests on the symbolic inequalities.

## originality

FAIL

A published SCOPE/Resultary record from 2026-09-20, one day earlier than the assigned record, was inspected in full and states the same theorem: S(2,5)=2, S(3,5)=17; for every q>=4, S(q,5)=max ell^4(q-ell); the maximizing split is unique; every maximum code is I^4J or its reverse; and N(q,5)=2 binom(q,ell), with the small-q counts as well. The current notation a(q-a)^4 is exactly the same formula after setting a=q-ell. The earlier record is therefore direct, slightly broader coverage rather than a merely similar result.

## value

FAIL

After crediting the direct earlier all-q theorem, the assigned record contributes only another derivation and reproducibility package for the same exact result. Correctness and independent reproducibility are useful, but they are not a distinct motivated mathematical gap under the required value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
