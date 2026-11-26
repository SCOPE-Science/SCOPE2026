# Independent mathematical audit

## correctness

PASS

The formulas are correct. In the Gaussian normalization K_w(z)=exp(z conjugate(w)), the kernel adjoint identity gives C_ψ* f(z)=exp(conjugate(d)z)f(conjugate(c)z). Applying this in the two orders gives the displayed W_{β,q,t,γ} tuples: (a conjugate(d),b conjugate(c),b conjugate(d)) and (conjugate(d),b,0). For such W, the proposed displacements satisfy conjugate(u)+q conjugate(v)=β and −qu−v=t, and changing variables in the Gaussian integral shows these displacements are unitary. Given v=−t−qu, the real part of (|u|²+|v|²)/2+q conjugate(v)u is |t|²/2+Δ|u|²/2. The diagonal dilation has exactly the singular sequence |q|^n, with rank one at q=0; thus substitution and geometric summation give all the stated formulas including the p<1 quasi-norms. Independently, expanding the ratio exponent gives the stated Q/(2Δ). Completing the square gives Q=(1−|c|²)|b−(1−q)d/(1−|c|²)|²−|a−c|²|d|²/(1−|c|²). This verifies the determinant, all three order relations for distinct slopes, and the exact rigidity for equal slopes. Read VERIFICATION.md and verification.py without running the frozen program; the operator proof is exact and not dependent on truncation.

## originality

FAIL

The asserted quantitative result is mechanically covered by an earlier Gaussian Fock result with arbitrary translations, not merely by centered special cases. Fatehi arXiv:1809.04829, Proposition 2.3 proof, (d)⇒(a), explicitly identifies the matched exponential weight and affine symbol with a scalar multiple of the centered dilation by unitary equivalence. Apply it to the positive square of each of the two cross products after the elementary kernel identity. This gives every singular value and multiplier even at q=0. Independently, Fatehi's Theorem 4.2 already gives both exact operator norms by direct substitution. The residual paired order sign is the expansion and completion of the square in the difference of these two known log-norm expressions. The exact paired presentation was not located earlier, but there is no distinct scientific step in it beyond applying existing formulas and elementary algebra; this is prior coverage by implication, not a finding that the frozen claim is false.

## value

FAIL

These cross products and sharp Schatten norms are natural and their juxtaposition is convenient, but the submitted exact fact is already mechanically available. A prior explicit unitary reduction of the exact positive square supplies all eigenvalues, and direct substitution into a prior norm theorem followed by one completion of the square supplies the supposedly separate phase classification. Under the standard for narrow exact results, packaging these consequences does not fill a remaining scientific gap. No surviving distinct result is established by dropping the geometric sequence and retaining just the algebraic sign test, so no repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
