# Independent mathematical audit

## correctness

PASS

PASS: Define 49 queen squares (r,c)∈(Z/7)^2, attacks on equal rows, columns or either wrapped diagonal. Independent exhaustive increasing-row/column placements reproduce exactly augmented face vector (1,49,588,2156,2450,882,196,28), 6350 total including empty. Independently rebuilt boundary matrices have ranks over F2 and F5 (1,48,540,1616,714,168,28), over F3 (1,48,540,1615,714,168,28), detecting 3-primary torsion; a field-rank drop alone cannot distinguish Z/9 from Z/3 or (Z/3)^2. Inspected actual package verify.py, which specifies integral elementary unit-cancellation counts (28,168,714,1615,540,48,1) descending, a 541×121 residual 4-to-3 boundary whose 84 nonzero columns are rationally rank one, integer primitive scalar gcd one and entry gcd nine, then exact survivor/chain-identity check. Its unimodular rank-one Smith invariant is nine and final chain groups C3=Z^121, C2=Z, giving H̃2=Z/9 and H̃3=Z^120. Crucially an independent earlier full 2026-10-25 published construction of the same complex and integral Morse Smith certificate also yields invariant nine, independently corroborating the principal finite claim. We did not rerun the current full integral reduction; field checks are explicitly subordinate to the exact integral argument.

## originality

FAIL

FAIL: The complete claimed integral homology of the same 7×7 wrapped queens nonattack-placement complex was published 2026-10-25, including H̃2=Z/9 and H̃3=Z^120 and no others. The earlier work also gives a Paley(49) clique-complex isomorphism, hence dominates the current homology finding. Different integral chain elimination algorithm, timing or absent Paley vocabulary does not restore novelty.

## value

FAIL

FAIL: The exact integral torsion phenomenon is intrinsically worthwhile but has already been fully computed for precisely this natural toroidal board, and the present new finite verification procedure adds no separately motivated unknown invariant or stronger mathematical conclusion. Thus the submitted unchanged principal result lacks independent research value as a new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
