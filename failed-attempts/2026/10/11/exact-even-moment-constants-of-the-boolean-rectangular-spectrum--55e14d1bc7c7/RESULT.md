# Exact even-moment constants of the Boolean rectangular spectrum

## Finding

For every integer \(d\ge 1\) and every integer \(h\ge 2\), let
\[
F(z)=\sum_{\varepsilon\in\{0,1\}^d}c_\varepsilon z^\varepsilon
\]
on normalized Haar \(\mathbb T^d\). Then
\[
\|F\|_{L^{2h}(\mathbb T^d)}^{2h}\le \left(2^{-h}\binom{2h}{h}\right)^d\left(\sum_\varepsilon |c_\varepsilon|^2\right)^h.
\]
The constant is sharp, so
\[
K_{2h}(\{0,1\}^d)=\left(2^{-h}\binom{2h}{h}\right)^{d/(2h)}.
\]
For a nonzero coefficient family, equality holds if and only if there are \(\lambda\ne0\) and phases \(|\eta_j|=1\) such that
\[
c_\varepsilon=\lambda\prod_{j=1}^d\eta_j^{\varepsilon_j}.
\]
Equivalently,
\[
F(z)=\lambda\prod_{j=1}^d(1+\eta_jz_j).
\]

## Assumptions and scope

The measure on every torus is normalized Haar measure. The exponent is an even integer \(2h\) with \(h\ge2\). The support is exactly the Boolean rectangular spectrum \(\{0,1\}^d\), although coefficients are allowed to vanish. The result is scalar-valued; a Hilbert-valued auxiliary inequality is used in the proof. No assertion is made here for non-even exponents or for spectra other than Cartesian products of two characters.

## Proof

Let \(H\) be a complex Hilbert space, let \(x,y\in H\), put \(A=\|x\|^2+\|y\|^2\), and put \(b=\langle x,y\rangle\). Expanding the constant Fourier coefficient of \(\|x+zy\|^{2h}\) gives the exact identity
\[
\int_{\mathbb T}\|x+zy\|^{2h}\,dm(z)
=
\sum_{k=0}^{\lfloor h/2\rfloor}
\frac{h!}{(h-2k)!(k!)^2}
A^{h-2k}|b|^{2k}.
\]
Cauchy--Schwarz and the arithmetic--geometric mean inequality give
\[
|b|\le \|x\|\|y\|\le \frac A2.
\]
Every coefficient in the displayed sum is nonnegative, hence
\[
\int_{\mathbb T}\|x+zy\|^{2h}\,dm(z)
\le
A^h
\sum_{k=0}^{\lfloor h/2\rfloor}
\frac{h!}{(h-2k)!(k!)^2}4^{-k}.
\]
The scalar choice \(x=y=1\) identifies the remaining sum exactly. Since
\[
\int_{\mathbb T}|1+z|^{2h}\,dm(z)=\binom{2h}{h},
\]
one obtains
\[
\sum_{k=0}^{\lfloor h/2\rfloor}
\frac{h!}{(h-2k)!(k!)^2}4^{-k}
=2^{-h}\binom{2h}{h}=:B_h.
\]
Thus
\[
\int_{\mathbb T}\|x+zy\|^{2h}\,dm(z)
\le B_h(\|x\|^2+\|y\|^2)^h.
\]
Because \(h\ge2\), the coefficient of the \(k=1\) term is positive. For nonzero \((x,y)\), equality therefore forces \(|b|=A/2\), which simultaneously forces equality in Cauchy--Schwarz and in the arithmetic--geometric mean inequality. Hence equality occurs exactly when \(y=\eta x\) for some \(|\eta|=1\).

Now prove a Hilbert-valued Boolean-spectrum version by induction on \(d\). Write
\[
G(z',z_d)=X(z')+z_dY(z').
\]
Applying the one-coordinate inequality and then the induction hypothesis in the Hilbert direct sum gives
\[
\begin{aligned}
\int_{\mathbb T^d}\|G\|^{2h}
&\le B_h\int_{\mathbb T^{d-1}}(\|X\|^2+\|Y\|^2)^h\\
&\le B_h^d\left(\sum_{\varepsilon\in\{0,1\}^d}\|v_\varepsilon\|^2\right)^h.
\end{aligned}
\]
For equality, the induction equality case makes the coefficient pairs of \((X,Y)\) a common Hilbert vector times coordinate phases, and equality in the final one-coordinate step forces the two common Hilbert vectors to differ by one unimodular scalar. Thus every nonzero equality family has the product-phase form. Specializing \(H=\mathbb C\) proves the claim.

Sharpness follows directly from
\[
F(z)=\lambda\prod_{j=1}^d(1+\eta_jz_j),
\]
because both the \(L^{2h}\) moment and the coefficient \(\ell^2\) norm factor over coordinates.

## Verification

The accompanying `verify.py` checks the central-binomial identity exactly for \(2\le h\le10\), verifies exact equality for flat product coefficients, and checks the inequality for deterministic integer coefficient families for \(1\le d\le4\) and \(2\le h\le5\). Its successful output is

`VERIFY_OK local_identities=9 exact_cases=335 d=1..4 h=2..5`

These finite checks corroborate the symbolic derivation; they are not used as a substitute for the proof for arbitrary \(d\) and \(h\).

## Relationship to prior work

Michels, *Λ(p)-sets and the limit order of operator ideals* (arXiv:math/9904176v1), supplies the classical \(\Lambda(p)\) framework and defines the constants being evaluated here, but its inspected results are structural operator-ideal characterizations rather than exact constants for the Boolean rectangular spectrum. A multiple Steinhaus Khinchine inequality in Cavalcante--Núñez-Alarcón--Pellegrino--Rueda, *Optimal constants of classical inequalities for complex scalars* (arXiv:1912.10313v1), concerns independent Steinhaus coordinates in every tensor block; that probability model is different from the two-character block \(\{1,z_j\}\) here and does not imply the displayed constant or its equality classification.

Database searches for the exact central-binomial constant, multiaffine-torus aliases, Hilbert-valued two-term formulations, and Boolean rectangular \(\Lambda(2h)\) formulations did not return an implication-equivalent statement. A previously recorded sixth-moment result is exactly the specialization \(h=3\); it does not imply the all-even theorem proved here. The new statement is a uniform structural theorem across all even moments rather than another isolated exponent computation.

## Limitations

The proof uses the positivity of the exact even-moment expansion and therefore does not by itself determine sharp constants at non-even exponents. It also relies on the Cartesian two-character factorization of the spectrum. The literature search cannot rule out an older equivalent formulation hidden under different tensor-product or multiaffine terminology; that residual bibliographic risk remains explicit. Independent audit has not been performed.

## References

1. C. Michels, *Λ(p)-sets and the limit order of operator ideals*, arXiv:math/9904176v1, first public 1999-04-30.
2. D. M. Cavalcante, D. Núñez-Alarcón, D. Pellegrino, J. B. Rueda, *Optimal constants of classical inequalities for complex scalars*, arXiv:1912.10313v1.
