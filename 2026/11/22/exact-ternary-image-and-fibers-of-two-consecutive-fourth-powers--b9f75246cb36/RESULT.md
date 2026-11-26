# Exact ternary image and fibers of two consecutive fourth powers

## Finding

For every integer \(k\ge1\), write
\[
F(x)=x^4+(x+1)^4,\qquad
V_k=\{F(x)\bmod 3^k:x\in\mathbb Z\}.
\]
The image in the three-adic integers is the disjoint union
\[
F(\mathbb Z_3)=(1+3\mathbb Z_3)\ \sqcup\ \left(\frac18+\frac{27}{4}\,(\mathbb Z_3)^2\right).
\]
Here \((\mathbb Z_3)^2=\{u^2:u\in\mathbb Z_3\}\), and fractions with denominator prime to three are interpreted in \(\mathbb Z_3\). This gives the **complete congruence-solvability criterion**: a target is attained precisely when it lies in one of these two components (modulo the specified power of three).

Put \(Q_3(n)\) for the number of squares modulo \(3^n\), with \(Q_3(0)=1\). Explicitly, for integers \(r\ge0\),
\[
Q_3(2r)=\frac{3\cdot9^r+5}{8},\qquad
Q_3(2r+1)=\frac{9^{r+1}+7}{8}.
\]
Then, for every \(k\ge1\),
\[
\boxed{|V_k|=3^{k-1}+Q_3(\max\{k-3,0\}).}
\]
The initial image sizes are \(2,4,10,29,85,254,760,2279,6835\) at \(k=1,\ldots,9\). Their limiting proportion is exactly
\[
\boxed{\lim_{k\to\infty}\frac{|V_k|}{3^k}=\frac{25}{72}.}
\]

The following also determines the entire fiber, not just image size. Let \(\mathcal N_k(y)=\#\{x\bmod3^k:F(x)\equiv y\pmod{3^k}\}\), let \(c_k=8^{-1}\bmod3^k\), and let \(\rho_j(z)\) count the roots of \(s^2\equiv z\pmod{3^j}\) (with \(\rho_0(0)=1\)). For any \(y\bmod3^k\):

- If \(y\equiv1\pmod3\), then \(\mathcal N_k(y)=2\).
- If \(k\le2\), \(y=c_k\) has \(\mathcal N_k(y)=3^{k-1}\); other targets congruent to \(2\pmod3\) have no preimages.
- If \(k\ge3\) and \(y\equiv c_k\pmod{27}\), set \(z=4(y-c_k)/27\bmod3^{k-3}\), where the quotient is defined after choosing any integer representative of the difference divisible by \(27\). Then \(\mathcal N_k(y)=9\rho_{k-3}(z)\).
- All remaining targets have \(\mathcal N_k(y)=0\).

This formula is effective: \(\rho_0(0)=1\); for \(j\ge1\) the number is \(3^{\lfloor j/2\rfloor}\) when \(z=0\), is \(2\cdot3^a\) when \(\nu_3(z)=2a<j\) and the unit part of \(z\) is \(1\pmod3\), and is zero otherwise.

## Assumptions and scope

The variable \(x\) ranges over all integers modulo \(3^k\), not merely units. The two fourth powers have **consecutive** inputs with an absolute step of one. The image and the formulas are proved for every positive integer \(k\), including the low levels where the singular branch has not yet split. The numerical density refers to counting residue classes, or equivalently Haar measure of the closed image in \(\mathbb Z_3\); it is not an asymptotic density of the integer values of \(F\) in \(\mathbb N\).

## Proof

**1. A centered quartic.** The substitution \(t=2x+1\) is a bijection of \(\mathbb Z_3\) and of each \(\mathbb Z/3^k\mathbb Z\). Direct expansion gives
\[
F(x)=\frac{t^4+6t^2+1}{8}=:G(t),\qquad G'(t)=\frac{t(t^2+3)}2.
\]
For \(t\equiv\pm1\pmod3\), \(G(t)\equiv1\pmod3\), while \(G'(t)\not\equiv0\pmod3\). Thus for every target \(y\equiv1\pmod3\), Hensel's lemma gives exactly one solution in each unit residue class of \(t\pmod3\), hence exactly two solutions \(x\pmod{3^k}\), at every level \(k\). These branches cover the full ball \(1+3\mathbb Z_3\).

**2. A singular quadratic normal form.** The remaining input class is \(t=3s\), where
\[
G(3s)=\frac18+\frac{27}{4}s^2\Bigl(1+\frac32s^2\Bigr).
\]
The quantity \(1+\frac32s^2\) lies in \(1+3\mathbb Z_3\), so has a unique square root congruent to one modulo three. Define the analytic map
\[
H(s)=s\sqrt{1+\frac32s^2}.
\]
Write \(R(s)=\sqrt{1+(3/2)s^2}\) for the root congruent to one modulo three. The difference of squares gives, for distinct \(s,u\),
\[
H(s)-H(u)=(s-u)\left(R(s)+\frac{3u(s+u)}{2(R(s)+R(u))}\right).
\]
Since \(R(s)+R(u)\equiv2\pmod3\), the parenthetical factor is congruent to one modulo three. Thus
\[
\nu_3(H(s)-H(u))=\nu_3(s-u).
\]
The reduction of \(H\) modulo \(3\) is the identity; the same isometry makes its reductions injective, hence bijective, modulo every \(3^j\). Passage to the inverse limit shows \(H\) is a bijective isometry of \(\mathbb Z_3\). Therefore
\[
G(3\mathbb Z_3)=\frac18+\frac{27}{4}(\mathbb Z_3)^2.
\]
Its values are all congruent to \(2\pmod3\), so the two image components are disjoint.

**3. All finite fibers.** For \(k\le2\), every input \(t\equiv0\pmod3\) maps to the single target \(8^{-1}\bmod3^k\); there are \(3^{k-1}\) such inputs. For \(k\ge3\), the same class can contribute only if \(y\equiv8^{-1}\pmod{27}\). Write \(t=3s\) with \(s\bmod3^{k-1}\). By Step 2 the target equation is equivalent to
\[
H(s)^2\equiv4(y-c_k)/27\pmod{3^{k-3}}.
\]
Because \(H\) is a bijection modulo \(3^{k-3}\), there are precisely \(\rho_{k-3}(z)\) solutions in \(s\bmod3^{k-3}\). Each has exactly nine lifts to \(s\bmod3^{k-1}\), giving the asserted factor nine. For a nonzero square target modulo \(3^j\), writing \(z=3^{2a}v\) with \(v\equiv1\pmod3\) shows that there are two square roots modulo \(3^{j-2a}\) and \(3^a\) lifts for each; when \(z=0\) there are exactly \(3^{\lfloor j/2\rfloor}\) roots. This proves every case of \(\rho_j\).

**4. Image counts and the limit.** The first image ball contributes \(3^{k-1}\) distinct targets. The second contributes exactly \(Q_3(\max\{k-3,0\})\): when \(k\le3\) it is one target, and for \(k>3\) two square arguments give the same target precisely when they are congruent modulo \(3^{k-3}\), since \(27/4=3^3/4\) with \(1/4\) a unit. The quadratic residues modulo \(3^n\) are zero together with residues of even valuation \(2a<n\) and square unit part, giving
\[
Q_3(n)=1+\sum_{a=0}^{\lfloor(n-1)/2\rfloor}3^{n-2a-1}\quad(n\ge1).
\]
Summing the geometric series gives the displayed parity formulas, and \(Q_3(n)/3^n\to3/8\). Hence the limiting image density is \(1/3+(1/27)(3/8)=25/72\).

## Verification

Run `python3 CHECK.py` using only Python's standard library. For every \(1\le k\le9\), the checker exhaustively evaluates the quartic for every input modulo \(3^k\), compares its **entire target-by-target fiber** against the closed formula, and compares its exact number of attained residues against the square-count formula. It reports 2, 4, 10, 29, 85, 254, 760, 2279, 6835 images. These are finite consistency checks, not the infinite proof.

## Relationship to prior work

Ding and Zieve's 2023 preprint studies moments of consecutive quadratic-residue patterns over finite fields; its Lemma 3.1 also determines the **number** of values of general even quartics \(X^4+aX^2\) over finite fields. It is relevant because the centered expression is a quartic of this form. The present statement concerns the distinct, non-field rings \(\mathbb Z/3^k\mathbb Z\), their exact fibers, and the singular characteristic-three lifting branch, rather than field-level value-set sums. Finch-Smith, Harrington and Wong's 2023 paper likewise addresses sums of distinct polynomial residues modulo primes \(p\ge5\), not this 3-adic tower. The indexed 2026 studies of a sixth-binomial polynomial modulo powers of three and of quartic Dickson polynomials modulo powers of two illustrate related square-branch methods but concern different maps and invariants. No equivalence or stronger published coverage was identified in the inspected material; implicit or unindexed coverage is possible.

## Limitations

The theorem treats the local prime three and the fixed polynomial \(x^4+(x+1)^4\), not every consecutive-power polynomial or every prime. The fraction \(25/72\) is a three-adic image measure, not the density of the set of integer outputs in the ordinary natural numbers. The computation is finite; mathematical completeness rests on the Hensel and analytic-isometry arguments. Independent review and independent validation have not been performed. A broadly stated prior theorem about quartic prime-power images could implicitly cover this specialization and would supersede a novelty claim.

## References

- Z. Ding and M. E. Zieve, *On sums of powers of consecutive squares over finite fields, and sums of distinct values of polynomials*, arXiv:2309.14979v1 (first posted 2023-09-26), especially Lemma 3.1 and Theorem 1.3. https://arxiv.org/abs/2309.14979
- C. Finch-Smith, J. Harrington, and T. W. H. Wong, *Sums of distinct polynomial residues*, *Integers* 23 (2023), article A63, first published 2023-08-25. https://doi.org/10.5281/zenodo.8283157
- Z.-H. Sun, *Cubic and quartic congruences modulo a prime*, *Journal of Number Theory* 102 (2003), 41–89, especially Section 5. https://doi.org/10.1016/S0022-314X(03)00067-2
