# An exact zero-atom Plancherel law for geometric dual polynomial hypergroups

## Finding

Fix real parameters \(q,t\) satisfying
\[
0<q\le\frac{\sqrt6-2}{2},\qquad 2q^3+4q^2\le t<\frac{1-q^2}{2-q^2}.
\]
Let \(P_0(x)=1\), \(P_1(x)=x\), and define a random-walk polynomial sequence by
\[
xP_n(x)=(1-c_n)P_{n+1}(x)+c_nP_{n-1}(x),\quad n\ge1,
\]
where \(c_1=t\) and, for integers \(m\ge1\),
\[
c_{2m}=1-q^{2m},\qquad c_{2m+1}=q^{2m+1}.
\]
Write \(\mu_{q,t}\) for the unique probability orthogonality measure (normalized by \(P_0=1\)). **Its exact spectral atom at the central character** is
\[
\boxed{\displaystyle
\mu_{q,t}(\{0\})=
\left[1+\frac{t(1-q)}{q(1-t)}
\left(\frac{1}{\prod_{j=0}^{\infty}(1-q^{2j+1})}-1\right)\right]^{-1}.}
\]
For the unperturbed example \(t=q\), this becomes the odd-factor Euler product
\[
\boxed{\displaystyle\mu_{q,q}(\{0\})=\prod_{j=0}^{\infty}(1-q^{2j+1})>0.}
\]
For each fixed permitted \(q\), the central atom is strictly decreasing in \(t\). These formulas specify spectral **mass**, rather than merely spectral support or a product over eigenvalue locations.

## Assumptions and scope

Every parameter is real and in the displayed range; the index \(m\) is a positive integer. The recurrence is the **small-odd-coefficient**, i.e. switched, choice in Kahler--Obermaier [1, Theorem 2.1]. The companion with odd and even coefficients interchanged also has nonnegative product linearization, but the atom formula is claimed solely for the stated recurrence. The support of \(\mu_{q,t}\) lies in \([-1,1]\). Products are absolute limits and the spectral mass is measured against total probability one.

The range is nonempty: the lower and upper bounds on \(t\) are compatible throughout \(0<q\le(\sqrt6-2)/2\). Indeed, the lower bound does not exceed \(q\), while \(q<(1-q^2)/(2-q^2)\) in this range. The choice \(t=q\) is therefore admissible.

## Proof

**1. Positive hypergroup recurrence.** Put \(s_1=t\) and \(s_n=q^n\) for every \(n\ge2\). By [1, Theorem 2.1], both recurrence coefficient choices have nonnegative linearization provided
\[
s_2<1-\frac{s_1}{1-s_1},\qquad s_n\le\frac{s_{n-2}}2-2s_{n-1}\quad(n\ge3).
\]
The first is exactly the strict upper bound on \(t\). At \(n=3\), the second is the lower bound \(t\ge2q^3+4q^2\). For \(n\ge4\), it is equivalent to \(q^2+2q\le1/2\), exactly the bound on \(q\). Since \(0<t<1\) all recurrence coefficients are positive and less than one. A bounded Jacobi matrix therefore gives a unique compactly supported probability measure, and the cited criterion gives nonnegative product linearization.

**2. The central eigenvector and its norm.** Define \(a_0=1\) and \(a_n=1-c_n\) for \(n\ge1\), and the Haar/orthogonalization numbers
\[
h(0)=1,\qquad h(n)=\prod_{k=1}^{n}\frac{a_{k-1}}{c_k}.
\]
Then \(p_n(x)=\sqrt{h(n)}P_n(x)\) are orthonormal. At \(x=0\), all odd-indexed values vanish, and induction in the recurrence gives, for \(m\ge1\),
\[
P_{2m}(0)=(-1)^m\frac{t}{1-t}\frac{q^{m^2-1}}{\prod_{j=2}^{m}(1-q^{2j-1})},
\]
where the empty product at \(m=1\) equals one. In the special case \(t=q\), the formulas reduce to
\[
P_{2m}(0)=\frac{(-1)^m q^{m^2}}{\prod_{j=1}^{m}(1-q^{2j-1})},\qquad
h(2m)=q^{-m}\frac{\prod_{j=1}^{m}(1-q^{2j-1})}{\prod_{j=1}^{m}(1-q^{2j})}.
\]
Set \(\rho=t(1-q)/(q(1-t))\). Changing \(t\) affects the even value \(P_{2m}(0)\) by the factor \(\rho\), and the even Haar weight by the factor \(\rho^{-1}\). Consequently
\[
h(2m)|P_{2m}(0)|^2=\rho\frac{q^{2m^2-m}}{\prod_{j=1}^{2m}(1-q^j)},\qquad h(2m+1)|P_{2m+1}(0)|^2=0.
\]
The sum of these squared orthonormal evaluation values converges because \(q^{2m^2-m}\) decays supergeometrically. Thus the sequence \((p_n(0))_{n\ge0}\) is a nonzero square-summable eigenvector of the bounded Jacobi operator at eigenvalue zero. Its first coordinate is one. The spectral theorem and cyclicity of the first basis vector yield
\[
\mu_{q,t}(\{0\})^{-1}=\sum_{n=0}^{\infty}|p_n(0)|^2
=1+\rho\sum_{m=1}^{\infty}\frac{q^{2m^2-m}}{\prod_{j=1}^{2m}(1-q^j)}.
\]
This argument also proves independently that zero is an atom and not merely a support limit point.

**3. Exact Euler summation.** Let \((q;q)_n=\prod_{j=1}^{n}(1-q^j)\), with \((q;q)_0=1\). Euler's classical \(q\)-binomial identity [3] is
\[
\sum_{n=0}^{\infty}\frac{q^{n(n-1)/2}z^n}{(q;q)_n}=\prod_{k=0}^{\infty}(1+zq^k)
\]
for \(|q|<1\) and bounded \(z\). Setting \(z=1\) yields twice \(\prod_{k\ge1}(1+q^k)\), whereas setting \(z=-1\) yields zero (its first product factor vanishes). Taking their half-sum extracts the even terms:
\[
\sum_{m=0}^{\infty}\frac{q^{2m^2-m}}{(q;q)_{2m}}
=\prod_{k=1}^{\infty}(1+q^k)
=\frac1{\prod_{j=0}^{\infty}(1-q^{2j+1})}.
\]
The last step uses \(1+q^k=(1-q^{2k})/(1-q^k)\). Substitution in Step 2 proves the stated formula. Since the sum beyond the first term is positive and \(\rho=t(1-q)/(q(1-t))\) increases strictly with \(t\), the mass decreases strictly with \(t\).

## Verification

The self-contained file `CHECK.py` verifies the admissible inequalities, exact central recurrence, Haar products, and the finite forms of the even Euler identity for multiple rational parameter pairs. Its floating-point evaluations of the infinite product and spectral-mass formula are supporting diagnostics only. The proof above establishes the infinite series identity, existence of the atom, and every claimed quantifier independently of finite checks. Execute with `python CHECK.py`; only Python standard-library modules are used.

## Relationship to prior work

Kahler and Obermaier [1], Section 2, introduce this dual-positive family and prove nonnegative linearization; their Section 4 describes qualitative discrete support and the occurrence of zero in the dual. These structural results are used, not claimed new. A prior public published-finding corpus result [2] obtains quantitative edge counts and eigenvalue product identities for the **opposite** geometric recurrence; its text explicitly excludes individual spectral atom masses and the switched recurrence. Neither result asserts the central spectral mass here. Euler's product identity [3] is classical. The claim is its spectral interpretation, closed mass formula, and exact first-coefficient response throughout a nontrivial parameter domain, not an independent \(q\)-series identity.

## Limitations

Only the mass of the zero eigenvalue is computed. No formula for the other atoms, no classification of the complete spectral support as a function of \(t\), and no claim for an arbitrary sequence satisfying [1, Theorem 2.1] is made. The parameter domain is sufficient, not asserted maximal. An equivalent formula might exist under older Jacobi-matrix or special-function terminology; comprehensive historical priority and independent mathematical audit have not been established.

## References

[1] S. Kahler and J. Obermaier, *A new class of orthogonal polynomials*, arXiv:2603.17983v1, first posted 2026-03-18; Theorem 2.1 and Section 4. https://arxiv.org/html/2603.17983v1

[2] *Logarithmic spectral edge law and Euler product for a geometric random-walk polynomial hypergroup*, published 2026-11-01; comparison to the opposite recurrence. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-logarithmic-spectral-edge-law-and-euler-product-for-a-geometric--4247c3e219b0

[3] Euler's \(q\)-binomial identity, standard in the theory of basic hypergeometric series. The displayed generating-function identity is used with \(z=\pm1\) and is proved by finite-product coefficient extraction or the standard limiting \(q\)-binomial theorem.
