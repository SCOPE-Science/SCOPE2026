# Strict reciprocal-coefficient positivity for the diagonal degree-seven Padé approximant

## Finding

Let \(q(z)=q_{7,7}(z)\) be the normalized denominator of the diagonal \([7/7]\) Padé approximant to \(e^z\):
\[
q(z)=1-\frac z2+\frac{3z^2}{26}-\frac{5z^3}{312}
+\frac{5z^4}{3432}-\frac{z^5}{11440}
+\frac{z^6}{308880}-\frac{z^7}{17297280}.
\]
**Theorem.** Every Taylor coefficient of its reciprocal is strictly positive:
\[
\frac1{q(z)}=\sum_{n=0}^{\infty}c_nz^n,
\qquad c_n>0\quad\text{for every integer }n\ge0.
\]
This is an all-index assertion, not positivity through a computational cutoff. The proof below uses an exactly checked finite prefix and a rigorous root-and-residue inequality covering every remaining index.

## Assumptions and scope

All algebraic claims concern the scalar rational function above, with rational coefficients and formal Taylor expansion at the origin. The polynomial is the denominator of the exponential Padé approximant with numerator and denominator degrees both seven, normalized by \(q(0)=1\). No claim is made for other Padé orders, floating-point output, or stability of a numerical matrix-exponential implementation. The primary subject is numerical matrix-function approximation (MSC2020 65F60).

## Proof

**Step 1: seven simple certified roots.** Set \(r=10^{-6}\). Introduce four rational complex centers
\[
\begin{aligned}
\zeta_0&=9.9435737,\\
\zeta_1&=9.5165811+3.4785721i,\\
\zeta_2&=8.1402783+7.0343481i,\\
\zeta_3&=5.3713538+10.8413883i.
\end{aligned}
\]
Also use their conjugates \(\overline\zeta_1,\overline\zeta_2,\overline\zeta_3\). For each of these seven centers \(c\), the exact rational inequalities checked by `verify_pade77.py` establish
\[
 |q(c)|+\frac{15r^2}{2}<r|q'(c)|,
 \qquad |c|+r<14,
 \qquad \sup_{|z|\le14}|q''(z)|<15.
\]
The first inequality follows using rational upper bounds on the absolute real and imaginary parts of \(q(c)\), and a rational lower bound on \(|q'(c)|\). Taylor's theorem along a line segment gives \(|q(c+w)-q(c)-q'(c)w|\le15r^2/2\) for \(|w|=r\). Rouché's theorem, comparing \(q(c+w)\) with \(q'(c)w\), yields exactly one root, counted with multiplicity, in each open disk \(|z-c|<r\). The seven disks are pairwise disjoint, so these are all the roots, and each is simple. The unique root in the disk about \(\zeta_0\) is real, positive, and has negative derivative, by conjugation and the exact derivative bounds.

**Step 2: conservative residue bounds.** Write the positive real root as \(R\) and the other roots in conjugate pairs \(z_j,\overline z_j\), \(1\le j\le3\). The same rational certificate establishes
\[
 0<R<9.944,\qquad 0<-q'(R)<0.0052,
\]
and the following strictly valid lower bounds, with the corresponding upper bounds on the absolute partial-fraction coefficients:

| Pair | \(\lvert z_j\rvert\) exceeds | \(\lvert q'(z_j)\rvert\) exceeds | \(\lvert 1/(z_jq'(z_j))\rvert\) is below |
|---|---:|---:|---:|
| 1 | \(10.132\) | \(0.0071\) | \(15\) |
| 2 | \(10.758\) | \(0.0202\) | \(5\) |
| 3 | \(12.098\) | \(0.157\) | \(1\) |

For example, derivative bounds at the root follow from those at the rational center and \(|q'(z_j)-q'(\zeta_j)|<15r\). Root-modulus bounds use the exact rational squares of the centers. Since \(9.944\cdot0.0052\cdot19<1\), the positive real root contributes a coefficient \(B=-1/(Rq'(R))>19\).

**Step 3: infinite tail.** Partial fractions, valid because all seven roots are simple, yield
\[
 c_n=\frac{B}{R^n}
   -\sum_{j=1}^{3}\left(
       \frac{1}{z_jq'(z_j)z_j^n}
      +\frac{1}{\overline z_jq'(\overline z_j)\overline z_j^n}
      \right).
\]
Consequently, for every \(n\ge0\),
\[
 c_n>\frac1{9.944^n}\left[
  19-2\left(
    15\left(\frac{9.944}{10.132}\right)^n
   +5\left(\frac{9.944}{10.758}\right)^n
   +\left(\frac{9.944}{12.098}\right)^n
  \right)\right].
\]
Every ratio in parentheses is strictly below one. The exact rational computation
\[
 2\left(15\left(\frac{9.944}{10.132}\right)^{32}
 +5\left(\frac{9.944}{10.758}\right)^{32}
 +\left(\frac{9.944}{12.098}\right)^{32}\right)<19
\]
therefore establishes \(c_n>0\) for **every** \(n\ge32\).

**Step 4: finite prefix.** Set \(q(z)=\sum_{j=0}^{7}q_jz^j\), with \(q_0=1\). Equating Taylor coefficients gives the exact recurrence
\[
 c_0=1,\qquad
 c_n=-\sum_{j=1}^{\min(7,n)}q_jc_{n-j}.
\]
The standalone rational-arithmetic verifier computes this recurrence and checks \(c_n>0\) at each of the 32 indices \(0\le n\le31\). No floating-point approximation is used for the root disks, derivative inequalities, residue comparisons, or finite coefficients. Steps 3 and 4 cover all nonnegative integers and prove the theorem.

## Verification

Run `python3 verify_pade77.py` with the Python standard library. Expected first line: `VERIFY_OK q_7_7: 7 disjoint Rouche root discs; exact residues; n=0..31 positive; tail n>=32 positive`. The code tests the rational coefficients of \(q\), bounds \(q''\), proves all seven Rouché inequalities and disk disjointness, encloses the needed moduli and derivatives, proves the exact rational tail estimate at index \(32\), and evaluates the first 32 reciprocal coefficients as `Fraction` objects. The positive tail uses a proved monotonicity bound, not an inference from finite enumeration. The centers are decimal representations of **exact rational numbers**, not purported exact roots.

## Relationship to prior work

Fasi and Higham (2019), Conjecture 3.2, propose positivity of the reciprocal coefficients for every odd denominator degree. Scardino (2026) disproves that unrestricted conjecture off the diagonal, proves conditional eventual positivity via the dominant positive root, and explicitly leaves the diagonal case open. The partial-fraction framework is therefore known; the claim here is the concrete **complete all-index degree-seven diagonal result** backed by new rational root disks and finite-prefix certificates. Classical reverse-Bessel polynomial zero computations address the zeros, not this all-coefficient sign assertion. Earlier degree-three and degree-five positivity results do not imply degree-seven positivity. No unrestricted conjecture or broader diagonal family is asserted.

## Limitations

The certificate establishes one natural diagonal Padé degree only. It does not show that all odd diagonal degrees satisfy the conjecture, nor does it justify a global algorithmic complexity improvement without other analytic assumptions. The mathematical verification is same-source reproducible exact arithmetic, not an independent review. Potential historical priority from unindexed reverse-Bessel literature remains a residual risk.

## References

1. F. Scardino, *On a positivity conjecture of Fasi and Higham for Padé approximants to the matrix exponential*, arXiv:2610.39051v1, 28 October 2026. https://arxiv.org/abs/2610.39051
2. M. Fasi and N. J. Higham, *An Arbitrary Precision Scaling and Squaring Algorithm for the Matrix Exponential*, SIAM J. Matrix Anal. Appl. 40 (2019), 1233–1256, Conjecture 3.2. https://doi.org/10.1137/18M1228876 ; https://eprints.maths.manchester.ac.uk/2721/
3. T. M. Dunster, A. Gil, D. Ruiz-Antolín, and J. Segura, *Computation of the reverse generalized Bessel polynomials and their zeros*, Comput. Math. Methods 3 (2021), e1198. https://doi.org/10.1002/cmm4.1198
