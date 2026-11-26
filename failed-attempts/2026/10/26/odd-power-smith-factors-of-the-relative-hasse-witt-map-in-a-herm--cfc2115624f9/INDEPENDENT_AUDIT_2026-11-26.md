# Independent mathematical audit

## correctness

PASS

The family can be realized by the plane equation Y^pZ−YZ^p=X^(p+1)+aX²Z^(p−1): the affine chart is smooth by the y-derivative, and at the unique point at infinity the Z-derivative is nonzero. The pole orders of x and y are p and p+1; dx is nonvanishing on the affine étale x-chart and has order 2g−2 at infinity on each fiber. The g monomials x^iy^j dx with i+j≤p−2 are thus regular with distinct orders and give bases by base change. Over the nonperfect parameter ring use relative Cartier into the Frobenius-twisted Hodge bundle (x' pulls back to x^p, y' to y^p), with a a base coefficient. In the expansion of y^j=(y^p−f)^j the selected x-exponents are p(t−s)+(i+t+s); exactly i+t+s=p−1 survives. Relative Cartier consequently has coefficients (−1)^t binom(j,t)binom(t,s)a^s; its Serre dual is the specified linearized Hasse–Witt map, up to transpose, without adjoining a root of a. The weight v=i+2j−(p−1)=r+2h partitions all nonzero entries into blocks with floor(v/2)+1 rows and (p−1)/2−ceil(v/2) columns. Unit row and column rescalings give entries a^(1+h+c)/(1+h+c)!. The t-minors have order at least t², and the leading t-square minor is a^(t²) times a unit by the falling-factorial Vandermonde, with 2t−1<p. This gives 1,3,… per block and multiplicity p+2−4j of 2j−1; the total is (p²−1)/8. This proves the full ideals over F_p[a], not only local orders or fiber ranks. Hand checks give [1], [1,1,1] and [1,1,1,1,1,3] at p=3,5,7. Frozen verify_hasse_witt.py and VERIFICATION.md were inspected, not executed; the conclusion rests on the all-prime proof.

## originality

FAIL

The ambient family, special and generic ranks, and the weighted block matrices are already covered by Almeida Filho–Tafazolian–Vieira. The Smith statement itself was not located verbatim. It does not follow from their rank values alone, but does follow by taking leading submatrices in their explicit coefficient factorization and applying their own binomial Vandermonde lemma. That is direct prior implication of every minor order, not an inference from a keyword miss or residual access risk.

## value

FAIL

An integral Smith profile is a meaningful invariant and detects nonreduced orders invisible to fiber ranks. But for this exact coefficient line all orders are obtained by retaining the published powers and applying the published binomial reduction and Vandermonde lemma to the initial submatrices. The frozen claim offers no separate nonmechanical consequence or extension beyond that computation. This is a useful explicit restatement, not a distinct narrow fact meeting the scientific-value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
