# Independent audit — 2026-09-26

Record: `2026/09/09/051`. Verdict: **correctness FAIL (Vámos premise); originality PASS (explicit coordinate certificate); scientific value PASS (bounded realization).** Disposition: archive full original package.

## Correctness
The coordinate certificate is valid. I independently evaluated all 126 homogeneous 4×4 determinants by permutation expansion. Exactly 1234, 1256, 3456 and 3478 vanish, det(5678)=2, and all 56 quadruples containing 9 are bases. There are 122 nonzero determinants, 73 positive and 49 negative. The affine combination −16p5+6p6−39p7+50p8 equals (7,11,13), coefficients sum to 1, and det(9,1,2,3)=−39 with the record's order. These prove a Q-representation of the stated relaxation and free extension, hence orientability of both.

The Context's premise that the Vámos matroid V8 is a **canonical minimal non-orientable matroid** is false. Kowalenko–Mautner, *A category O for oriented matroids* (J. Comb. Algebra 7, 2023), Example 2.26 explicitly states that Vámos is not representable over any field **but is orientable**, citing Bland–Las Vergnas. Representability and orientability are different questions. Therefore “relaxing one circuit-hyperplane can restore orientability” is not a valid motivation or implication for this V8 case, even though the new coordinates do show representability. This material misstatement fails the record's correctness axis.

## Originality
The cited eight-point oriented-matroid enumeration and realization-space papers do not contain this specific nine-column Q-coordinate certificate in the passages compared. The free extension step is elementary once the eight-point realization is available, so originality is narrow: a fixed labelled relaxation witness, not the fact that V8 can be oriented.

## Scientific value
The exact representation of this labelled relaxed neighbor gives a useful positive test case, and the generic ninth column provides a readily reusable extension. It says nothing about the other relaxations, realization spaces, or V8 representability; it must be reintroduced with the correct historical orientability premise.

Sources: original RESULT.md and output/artifacts/verify_m9.py; https://ems.press/content/serial-article-files/37171, Example 2.26; https://arxiv.org/abs/1204.0645.
