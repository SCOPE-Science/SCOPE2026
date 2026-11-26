# Independent mathematical audit

## correctness

PASS

Classifying the units digit gives h_b(bn)=h_b(n)+h_b(n-1) and h_b(bn+r)=h_b(n) for 1≤r<b, including n=0 by the zero convention. Modulo two, the state (h_b(n),h_b(n-1)) transforms by (a+c,c), (a,a+c), or (a,a) for digits 0, 1, or 2 through b-1; at n=0 a leading zero fixes (1,0). The absorbing zero state contributes no count. Count states (10,11,01) by x,y,z: x'=x+y, y'=(b-1)x+(b-2)y+z, z'=y+z, so x-z=1 and A_b=x+y, x_L=A_b(L-1) for L≥1. This gives the asserted inhomogeneous recurrence with (1,b), producing generating-function numerator 1-2t². Subtracting the constant solution 1/b yields characteristic polynomial u²-(b-1)u-2 and positive dominant coefficient as displayed. For b>2 the positive root is in (2,b) by evaluating the polynomial at 2 and b, and the other root has magnitude 2/λ_{b,+}<1; sandwiching arbitrary X between adjacent powers proves the stated Theta law. In base 2, the two Stern recurrences imply the even indices of the value sequence are precisely indices divisible by three: for odd index 2n+1 the sum is even just when n≡1 mod 3 because both adjacent terms are then odd. With h_2(n)=s_2(n+1), the complement of a single residue class gives N_2(X)=2X/3+O(1).

## originality

FAIL

Distinct contribution relative to the inspected archive is not established. A different indexed Resultary record, bb0ad70479bb, states the same all-base theorem for the same h_b: identical exact block counts, recurrence, generating function, eigenvalue coefficient, and sharp positive-density/zero-density and higher-base exponent laws. Its proof also uses the same parity states up to coordinate swap, state reorder and matrix convention. The only superficially stronger binary O(1) estimate follows directly from the classical mod-three characterization and appears in the matched record's proof via that same characterization. The catalog dates and differing record identities establish neither historical priority nor derivation or authorship; the documented issue is exact mathematical coverage and no supported distinct remainder, not that the October record was proved to copy a later record.

## value

PASS

Judged as a mathematical result, the exact contrast between binary positive density and higher-base polynomial sparsity with an explicit exponent is a meaningful distribution question for a natural generalization of Stern's sequence. The level generating function gives substantially more than a small table or an isolated numerical example. This assessment of the theorem's intrinsic interest does not give independent contribution credit to a record that duplicates the result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
