# The exact innermost nonzero zero circle of two-prime necklace polynomials

## Finding
For distinct primes \(2\le p<q\) and any integers \(a,b\ge1\), put \(t=p^{a-1}q^{b-1}\), \(n=p^a q^b\), and \(g=\gcd(p-1,q-1)\). The classical necklace polynomial is
\[
M_n(z)=\frac1n\sum_{d\mid n}\mu(d)z^{n/d}.
\]
Let \(\rho_{p,q}\in(0,1)\) be the unique positive solution of
\[
\sum_{j=0}^{q-1}\rho_{p,q}^{\,q-1+(p-1)j}=1,
\qquad R_{p,q,a,b}=\rho_{p,q}^{1/t}.
\]
**Theorem.** The root \(0\) of \(M_n\) has multiplicity exactly \(t\). Every nonzero complex root \(z\) satisfies \(|z|\ge R_{p,q,a,b}\). Equality holds **if and only if**
\[
z=R_{p,q,a,b}\,\zeta,\qquad \zeta^{tg}=1.
\]
These \(tg\) roots are pairwise distinct and simple; no other nonzero root lies in the closed disk of that radius. In particular, the angular multiplicity of the innermost nonzero root circle is governed by \(\gcd(p-1,q-1)\), even though all nonzero root moduli for prime-power-supported lengths depend only on their squarefree kernel by power substitution.

Moreover, for each fixed prime \(p\), as primes \(q>p\) tend to infinity,
\[
1-\rho_{p,q}=\frac{W\!\left(\frac{q-1}{p-1}\right)}{q-1}
+O_p\!\left(\frac{(\log q)^2}{q^2}\right),
\]
where \(W(s)>0\) is the unique real solution of \(W(s)e^{W(s)}=s\). The constant in the error term may depend on the fixed prime \(p\), and the assertion is along primes \(q>p\).

## Assumptions and scope
The Möbius function is denoted by \(\mu\). All roots and multiplicities are over \(\mathbb C\), except the uniquely defined real \(\rho_{p,q}\). The parameters \(p,q\) are distinct primes with \(p<q\); \(a,b\) are arbitrary positive integers. The **innermost nonzero zero circle** is the circle centered at the origin whose radius is the minimum modulus among the nonzero zeros. The polynomial has its conventional rational coefficient normalization \(1/n\), which does not affect its zeros. The Lambert-\(W\) asymptotic holds at fixed \(p\), and does not assert a uniform error as both primes grow.

## Proof
**1. Reduction to two squarefree primes.** Möbius inversion gives, with \(t=p^{a-1}q^{b-1}\),
\[
nM_n(z)=z^{pqt}-z^{pt}-z^{qt}+z^t
=pq\,M_{pq}(z^t).
\]
The coefficient of \(z^t\) in \(nM_n\) is \(1\), while every other nonzero exponent exceeds \(t\). Therefore the zero at the origin has multiplicity exactly \(t\).

**2. A positive-factor separation.** Set \(c=p-1\), \(Q=q-1\), and
\[
H_{p,q}(z)=\sum_{j=0}^{q-1}z^{Q+cj}.
\]
The finite geometric identity gives the exact factorization
\[
pq\,M_{pq}(z)=z(1-z^c)(1-H_{p,q}(z)).\tag{1}
\]
Indeed, \((1-z^c)H_{p,q}(z)=z^Q(1-z^{qc})\), so expansion of (1) is \(z-z^p-z^q+z^{pq}\), the same as the Möbius formula. Every nonzero zero of the factor \(1-z^c\) has modulus one. The function \(H_{p,q}(r)\) is strictly increasing for \(0<r<1\), because all its coefficients are positive and exponents positive, with \(H_{p,q}(0)=0\) and \(H_{p,q}(1)=q>1\). Thus there is precisely one \(\rho\in(0,1)\) satisfying \(H_{p,q}(\rho)=1\).

**3. The exact equality case in the triangle inequality.** If \(H_{p,q}(z)=1\), then
\[
1=\bigl|H_{p,q}(z)\bigr|\le H_{p,q}(|z|),
\]
so strict monotonicity implies \(|z|\ge\rho\). For \(|z|=\rho\), equality in the triangle inequality and the positivity of the sum \(H_{p,q}(z)=1\) imply that **each nonzero summand is positive real**. Write \(z=\rho\zeta\) with \(|\zeta|=1\). Then \(\zeta^Q=1\), and by dividing the phase conditions for consecutive summands, \(\zeta^c=1\). Conversely these two conditions make \(H_{p,q}(\rho\zeta)=H_{p,q}(\rho)=1\). Hence exactly \(g=\gcd(Q,c)\) roots of \(1-H_{p,q}\) lie on its smallest circle, namely \(\rho\zeta\) for \(\zeta^g=1\).

These roots are simple. At such a root, write \(m_j=Q+cj>0\) and compute
\[
H_{p,q}'(\rho\zeta)
=(\rho\zeta)^{-1}\sum_{j=0}^{q-1}m_j\rho^{m_j}\ne0,
\]
since \(\zeta^{m_j}=1\) for all \(j\) and the displayed real sum is positive. They are not zeros of \(1-z^c\), whose zeros are on the unit circle. This proves the complete smallest-modulus classification for \(M_{pq}\).

**4. Lifting through prime powers.** The substitution \(z\mapsto z^t\) transfers nonzero roots of \(M_{pq}\) to those of \(M_n\). Every nonzero root of \(M_{pq}\) has exactly \(t\) distinct \(t\)-th roots, each simple if its parent root is simple. The minimum radius becomes \(\rho^{1/t}\), and the preimages of \(\rho\zeta\) for \(\zeta^g=1\) are precisely all solutions to \(z^{tg}=\rho^g\). Hence they are exactly \(R_{p,q,a,b}\zeta\) for \(\zeta^{tg}=1\), all simple. No other nonzero root reaches that radius.

**5. A uniform-in-\(q\) logarithmic reduction at fixed \(p\).** For the asymptotic set \(Q=q-1\), \(c=p-1\), and \(u=-Q\log\rho>0\). The defining equation becomes
\[
1=e^{-u}\frac{1-e^{-(cq/Q)u}}{1-e^{-(c/Q)u}}.\tag{2}
\]
Since every exponent in \(H_{p,q}\) is between \(Q\) and \(pQ\), equation \(H_{p,q}(\rho)=1\) yields
\[
q e^{-pu}\le1\le q e^{-u},\qquad
\frac{\log q}{p}\le u\le\log q.\tag{3}
\]
Put \(\alpha=c/Q\), \(\beta=cq/Q\). Then \(\alpha u=O_p(\log q/q)\), while \(\beta\ge1\) and (3) imply \(e^{-\beta u}\to0\). From (2),
\[
e^{-u}=\frac{1-e^{-\alpha u}}{1-e^{-\beta u}}
=O_p(\alpha u)=O_p(\log q/q),
\]
where the denominator is at least \(1/2\) for sufficiently large \(q\). It follows also that \(e^{-\beta u}=O_p(\log q/q)\). Multiplication of (2) by \(ue^u\) and the expansion \(1-e^{-v}=v(1+O(v))\), valid as \(v\to0\), give
\[
u e^u=\frac{Q}{c}\left(1+O_p(\log q/q)\right).
\]
Let \(u_0=W(Q/c)\). The strictly increasing function \(v+\log v\), whose derivative is \(1+1/v\ge1\) for \(v>0\), shows after taking logarithms that
\[
u=u_0+O_p(\log q/q).
\]
Finally \(\rho=e^{-u/Q}\) and \(u=O(\log q)\) yield
\[
1-\rho=\frac{u}{Q}+O\!\left(\frac{u^2}{Q^2}\right)
=\frac{u_0}{Q}+O_p\!\left(\frac{(\log q)^2}{q^2}\right),
\]
as claimed. \(\square\)

## Verification
Run `python3 verify.py` (Python standard library only). It independently expands the Möbius and positive-factor expressions as sparse integer polynomial dictionaries for 36 prime-power parameter combinations, verifies the positive derivative and all predicted minimal-circle angular congruences, and bisects the real defining equation. It also computes nine fixed-prime large-\(q\) examples and compares the normalized approximation errors with the asserted Lambert-\(W\) scale. These are finite consistency checks, not replacements for the unrestricted proof. The output ends with `PASS: 36 exact polynomial factorizations, complex angular constraints, uniqueness of positive radial root, and 9 asymptotic samples.`

## Relationship to prior work
Hyde's *Cyclotomic factors of necklace polynomials* (2018 preprint, 2022 journal article) develops root-of-unity and cyclotomic divisibility criteria for the same \(M_n\), including the two-prime case. Those criteria locate factors on \(|z|=1\), not the first **nonzero interior** root circle or its exact equality angles. Chebolu–Mináč–Nguyen–Tân's *Analytic Properties of Necklace Polynomials* (2026 preprint) proves real-variable monotonicity primarily on \([1,\infty)\) and observes negativity immediately to the left of \(1\) (Remark 4.6). This does not determine the least positive zero, the least complex-root modulus, or its \(q\)-asymptotic. Other inspected studies address residue-ring fibers and discrete necklace-count root ratios rather than complex zeros of the polynomial in its alphabet parameter. The new theorem concerns a different invariant—the exact radial and angular boundary of the nonzero root set—and its large-prime logarithmic boundary layer.

## Limitations
The argument is specific to lengths with exactly two distinct prime divisors. It does not classify remaining nonzero roots outside the innermost circle, or assert an asymptotic uniform in both primes. The Lambert-\(W\) estimate is an asymptotic rather than an exact closed-form solution for \(\rho\). Literature overlap screening covered the sources listed, including two accessible prior records with related necklace-polynomial objects; an exhaustive historical priority guarantee is not asserted, and full text of every potentially relevant older work was not available. No independent mathematical audit has been performed.

## References
1. T. Hyde, *Cyclotomic factors of necklace polynomials*, arXiv:1811.08601v1 (first public 2018-11-21), *Acta Arithmetica* 204 (2022), 287–316, doi:10.4064/aa210304-11-5, primary MSC 11C08. https://arxiv.org/abs/1811.08601
2. S. K. Chebolu, J. Mináč, T. T. Nguyen, N. D. Tân, *Analytic Properties of Necklace Polynomials*, arXiv:2605.11445 (first public 2026-05-12), particularly Theorem 1.1 and Remark 4.6. https://arxiv.org/abs/2605.11445
3. *The exact two-adic fiber law for odd squarefree necklace polynomials*, public research record dated 2026-11-08, theorem on the residue-ring images of \(M_n\). https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-exact-two-adic-fiber-law-for-odd-squarefree-necklace-polynom--44672f88ba38/RESULT.md
4. *Sharp root-ratio thresholds for primitive-necklace counts*, public research record dated 2026-11-02, theorem on count ratios at integer alphabet sizes. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-sharp-root-ratio-thresholds-for-primitive-necklace-counts--776f6cf4f46c/RESULT.md
