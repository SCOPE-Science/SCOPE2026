# Rational-dilation rigidity across all spherical Bessel orders

## Finding

Let \(j_\ell(z)=\sqrt{\pi/(2z)}J_{\ell+1/2}(z)\) denote the spherical Bessel function, where \(\ell\) is a nonnegative integer and the positive-real normalization is used. For all nonnegative integers \(\ell,m\) and all positive rational \(q\), the equations
\[
j_\ell(x)=j_m(qx)=0,\qquad x>0,
\]
have a solution **if and only if** one of the following conditions holds:

1. \(\ell=m=0\), with arbitrary \(q\in\mathbb Q_{>0}\);
2. \(\ell=m\ge1\) and \(q=1\).

In particular, **different spherical harmonic orders never have rationally commensurable positive radial zeros**. The exceptional order-zero case is sharp: \(j_0(x)=\sin(x)/x\), so for \(q=a/b\) with positive integers \(a,b\), the point \(x=b\pi\) is a common zero of \(j_0(x)\) and \(j_0(qx)\).

## Assumptions and scope

The parameters \(\ell,m\) range independently over \(\{0,1,2,\ldots\}\). The multiplier \(q=a/b\) is strictly positive and rational, written with positive integers \(a,b\); no coprimality is needed. Only nonzero positive *arguments* are claimed. The result is unconditional and does not depend on conjectural algebraic independence statements.

Introduce the elementary rational Hankel factor
\[
Q_\ell(z)=\sum_{k=0}^{\ell}\frac{(\ell+k)!}{2^k k!(\ell-k)!}\left(\frac{i}{z}\right)^k,
\]
and the two monic polynomials
\[
A_\ell(z)=z^\ell Q_\ell(z),\qquad
B_\ell(z)=z^\ell Q_\ell(-z).
\]
Both have degree \(\ell\), nonzero constant term, and algebraic coefficients. For \(\ell=0\), both equal 1. For \(\ell\ge1\), their next-to-leading coefficients are respectively \(+i\ell(\ell+1)/2\) and \(-i\ell(\ell+1)/2\).

## Proof

**1. Exact rational phase at a zero.** The terminating half-integer spherical-Hankel formulas give, for \(z\ne0\),
\[
h_\ell^{(1)}(z)=\frac{(-i)^{\ell+1}e^{iz}}{z}Q_\ell(z),
\qquad
h_\ell^{(2)}(z)=\frac{i^{\ell+1}e^{-iz}}{z}Q_\ell(-z),
\]
with \(j_\ell=(h_\ell^{(1)}+h_\ell^{(2)})/2\). The two Hankel functions have a nonvanishing Wronskian at every nonzero argument. Consequently \(A_\ell\) and \(B_\ell\) have no common root: if both vanished at a nonzero point, both independent Hankel solutions would vanish there, contrary to their Wronskian; at the origin neither polynomial vanishes. Define
\[
R_\ell(z)=(-1)^\ell\frac{B_\ell(z)}{A_\ell(z)}.
\]
It is reduced, has exactly \(\ell\) finite poles counted with multiplicity, and no pole at infinity. Every nonzero zero \(\alpha\) of \(j_\ell\) satisfies
\[
e^{2i\alpha}=R_\ell(\alpha),
\]
and the denominator is nonzero at \(\alpha\). The behavior at infinity is
\[
R_\ell(z)=(-1)^\ell\left(1-\frac{i\ell(\ell+1)}z+O(z^{-2})\right).
\]
For \(\ell=0\), this identity reads \(R_0=1\).

**2. Nonzero zeros are transcendental.** Suppose a nonzero zero \(\alpha\) of \(j_\ell\) were algebraic. Then \(R_\ell(\alpha)\) would be algebraic, hence so would \(e^{2i\alpha}\). But the Lindemann–Weierstrass theorem states that the exponential of a nonzero algebraic number is transcendental. Since \(2i\alpha\) is nonzero algebraic, this is impossible. Therefore every nonzero spherical Bessel zero is transcendental, including the order-zero zeros \(n\pi\).

**3. The only possible rational-phase identity.** Let \(q=a/b\) with positive integers \(a,b\). If the rational functions
\[
R_\ell(z)^a\quad\text{and}\quad R_m(qz)^b
\]
were identical, counting their finite poles with multiplicity would yield
\[
a\ell=bm.\tag{1}
\]
Comparison of the \(1/z\) coefficient relative to the nonzero constant at infinity would also yield
\[
a\ell(\ell+1)=\frac bq m(m+1),
\quad\text{equivalently}\quad
a^2\ell(\ell+1)=b^2m(m+1).\tag{2}
\]
If exactly one order is zero, (1) fails. If both orders are positive, substitution of \(a\ell=bm\) from (1) into (2) gives \(\ell=m\), hence \(a=b\) and \(q=1\). If both orders are zero, \(R_0=1\) makes the identity hold at every scale. Thus for every pair other than the two exceptional parameter cases, the difference of these rational functions is nonzero.

**4. Rationally related zeros force a forbidden identity.** Suppose \(j_\ell(\alpha)=0=j_m(q\alpha)\) for some \(\alpha>0\). Applying Step 1 and using \(a\alpha=b(q\alpha)\), gives
\[
R_\ell(\alpha)^a=e^{2ia\alpha}
=e^{2ibq\alpha}=R_m(q\alpha)^b.
\]
If the two rational functions are not identically equal, clearing their algebraic-coefficient denominators produces a **nonzero polynomial with algebraic coefficients** having \(\alpha\) as a root. Hence \(\alpha\) is algebraic, contradicting Step 2. Therefore the rational functions must be identical and Step 3 leaves only \(\ell=m=0\), or \(\ell=m\ge1,q=1\). Both cases really have common positive zeros, as already explained for the first and by the existence of positive spherical Bessel zeros for the second. This completes the classification.

## Verification

The proof uses an exact finite half-integer Hankel identity, a nonzero Wronskian, a rational-function pole count, one Laurent coefficient, and Lindemann–Weierstrass. No numerical zero enumeration enters the infinite argument. For \(\ell=1,m=2,q=2\), for instance, pole counts alone tie at 2, but the next coefficient excludes equality: \(2\cdot1\cdot2\ne(1/2)\cdot2\cdot3\). This illustrates why the Laurent coefficient is essential for different orders.

The attached `check.py` uses SymPy exact arithmetic to check polynomial coprimality, degrees, leading and subleading coefficients through order 15; all incompatible pole-and-coefficient pairs among orders below 12 and rational scales with numerator and denominator below 9; and five direct rational-function identity cases. Run `python check.py` after installing the dependency in `requirements.txt`. Its 8,610 finite assertions supplement the proof but do not establish the general result by enumeration.

## Relationship to prior work

The motivating work of Binyamini, Kiro, Kozma and Pila, *Counting Bessel zeros and applications* (first public October 20, 2026), treats arithmetic constraints on Bessel zeros and in its §§5 and 8 uses rational exponential phases for fixed half-integer orders. In particular its Proposition 8.2 states a **conditional** algebraic-independence conclusion for distinct positive zeros of a *fixed* \(J_{m+1/2}\). The fixed-order rational-phase technique is therefore not presented here as new. The additional order-variable comparison (both pole degree and the \(1/z\) coefficient) proves an **unconditional different-order rational-dilation obstruction**.

The published result *Rationally separated frequency spheres detect every nonconstant spherical harmonic* establishes rational-ratio rigidity among distinct zeros at one **fixed positive spherical order**. That assertion does not by itself forbid zeros at two *different* orders. Classical Bourget-type noncoincidence for unscaled Bessel arguments likewise does not exclude rational scale factors other than 1. DLMF §10.21 documents unscaled common-zero and interlacing facts, while DLMF §10.49 provides the exact terminating Hankel formulas.

## Limitations

No statement is made about irrational or general algebraic dilations, integer-order cylindrical Bessel zeros, an explicit separation bound between approximate zeros, or algebraic independence of several Bessel zeros. The cross-order identity argument is elementary once the terminating Hankel representation and Lindemann–Weierstrass are available. The possibility of an unlocated older equivalent formulation remains a bibliographic limitation. A closely related fixed-order published result could be compared through its indexed statement, but its full public file was not retrievable during this comparison; no assertion about its uninspected details is made.

## References

- G. Binyamini, A. Kiro, G. Kozma, J. Pila, *Counting Bessel zeros and applications*, arXiv:2610.28477, first publicly posted 2026-10-20. https://arxiv.org/abs/2610.28477 (Introduction, Theorem 1.2, Lemma 5.2 and Proposition 8.2 inspected).
- NIST Digital Library of Mathematical Functions, §10.49, *Explicit Formulas* for spherical Bessel functions, https://dlmf.nist.gov/10.49; §10.21, *Zeros*, https://dlmf.nist.gov/10.21.
- *Rationally separated frequency spheres detect every nonconstant spherical harmonic*, publicly indexed 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-rationally-separated-frequency-spheres-detect-every-nonconstant--acdde5641585 (title and abstract retrieved; full text unavailable).
- L. Lorch and M. E. Muldoon, *Transcendentality of zeros of higher derivatives of functions involving Bessel functions*, International Journal of Mathematics and Mathematical Sciences 18 (1995), 551–560 (abstract/introduction inspected through a publicly indexed text copy).
