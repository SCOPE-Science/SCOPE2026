# Sharp translate threshold and joint GCD laws for irrational polynomial floors

## Finding

**Theorem (complete joint law and sharp translate threshold).** Fix an integer \(d\ge2\), an irrational real number \(\alpha\), and \(1\le r\le d\) distinct integer shifts \(h_1,\ldots,h_r\). For every sufficiently large positive integer \(n\) put
\[
G_j(n)=\gcd\bigl(n,\lfloor\alpha(n+h_j)^d\rfloor\bigr),\quad 1\le j\le r,
\]
where the gcd is nonnegative. For every positive integer tuple \((m_1,\ldots,m_r)\), the exact natural density of simultaneous divisibility events is
\[
\operatorname{dens}\{n:\ m_j\mid G_j(n)\ (1\le j\le r)\}
=\frac{1}{\operatorname{lcm}(m_1,\ldots,m_r)\prod_{j=1}^r m_j}.
\]
Moreover the entire joint vector has a limiting probability distribution on \(\mathbb N^r\). Its mass at each positive integer vector \(\mathbf a=(a_1,\ldots,a_r)\) is
\[
\Pr(\mathbf G=\mathbf a)=\prod_{p\text{ prime}}w_{p,r}\bigl(v_p(a_1),\ldots,v_p(a_r)\bigr),
\quad
w_{p,r}(\mathbf e)=\sum_{\boldsymbol\delta\in\{0,1\}^r}
(-1)^{\sum_j\delta_j}\,p^{-\max_j(e_j+\delta_j)-\sum_j(e_j+\delta_j)}.
\]
The product is positive and convergent. Equivalently, it is the distribution of \((\gcd(U_0,U_1),\ldots,\gcd(U_0,U_r))\) for independent Haar-uniform profinite integers \(U_0,\ldots,U_r\). This is *not* a claim of independence among the \(G_j\); they share the first coordinate. The law is independent of \(\alpha\), the shifts, and \(d\) within the indicated range.

For two shifts, the Euler factors simplify, with \(i,j\ge0\), to
\[
w_{p,2}(i,j)=\begin{cases}
p^{-3i}(1-2p^{-2}+p^{-3}),&i=j,\\
p^{-i-j-\max(i,j)}(1-p^{-1})(1-p^{-2}),&i\ne j.
\end{cases}
\]
In particular, the density that both GCDs equal one is
\[
\prod_p(1-2p^{-2}+p^{-3}).
\]

The universal range \(r\le d\) is **sharp**: for every \(d\ge2\) there exists an irrational \(\alpha\) for which the \(d+1\) consecutive shifts \(0,1,\ldots,d\) do *not* satisfy the displayed divisibility law.

## Assumptions and scope

The polynomial degree and shifts are fixed while \(n\to\infty\). Any irrational \(\alpha\), including a negative one, is allowed in the positive assertion. Floor values need not be positive. The distribution is pointwise in the positive integer tuples and sums to one; no effective convergence rate or uniformity as the degree or shifts grow is claimed. The source of the large-prime estimate is Holdridge's published theorem, rather than a new estimate proved here.

## Proof

**1. The sharp rank condition.** Write \(f_j(x)=\alpha(x+h_j)^d\). For a nonzero integer vector \(\mathbf c\), the coefficient of \(x^{d-k}\) in \(\sum_jc_j f_j(x)\) is \(\alpha\binom dk\sum_jc_jh_j^k\), for \(0\le k\le d-1\). If every nonconstant coefficient vanished, then the moments \(\sum_jc_jh_j^k\) would vanish for \(k=0,1,\ldots,d-1\). The first \(r\) equations form a Vandermonde system with pairwise distinct shifts, hence force \(\mathbf c=0\), a contradiction. Thus every nontrivial integer combination has a nonconstant irrational coefficient. The same holds after replacing \(x\) by \(Dm+u\) and dividing by any positive integer \(D\): the leading nonzero coefficient remains a nonzero rational multiple of \(\alpha\). By Weyl's criterion the vector \((f_j(Dm+u)/D)_{j=1}^r\) is uniformly distributed modulo one, for each residue \(u\bmod D\).

**2. All fixed-modulus laws.** The condition \(\lfloor f_j(n)\rfloor\equiv a_j\pmod D\) is equivalent to \(\{f_j(n)/D\}\in[a_j/D,(a_j+1)/D)\); endpoints have zero limiting measure. Therefore, as \(n\to\infty\), the residues of \(n,\lfloor f_1(n)\rfloor,\ldots,\lfloor f_r(n)\rfloor\) are jointly uniform modulo \(D\). Taking \(D\) divisible by the prescribed positive integers \(m_j\) proves the simultaneous divisibility formula: \(n\) must be a multiple of their least common multiple and each floor independently a multiple of its own modulus. In particular, for any fixed prime \(p\) and nonnegative exponents \(e_j\), the local simultaneous divisibility mass equals \(p^{-\max_j e_j-\sum_je_j}\). Inclusion–exclusion over whether each GCD valuation exceeds its specified value produces exactly the displayed finite sum \(w_{p,r}\).

**3. Pass from finite moduli to the full joint law.** The equidistribution statement alone does not justify the infinite Euler product. For each fixed \(j\), Holdridge's Theorem 1.3, applicable because \(f_j\) has an irrational nonconstant coefficient and \(d\ge2\), gives
\[
\lim_{R\to\infty}\limsup_{N\to\infty}\frac1N
\#\{n\le N:\exists p>R,\ p\mid n,\ p\mid\lfloor f_j(n)\rfloor\}=0.
\]
A union over the finitely many \(j\) controls all large prime divisors of all \(G_j\). For a fixed prime \(p\), step 2 gives density \(p^{-2K}\) for the event \(p^K\mid G_j(n)\). A finite union over \(p\le R\) and \(j\), followed by \(K\to\infty\), controls arbitrarily high valuations. Consequently the gcd vector is tight on \(\mathbb N^r\), and its exact mass at any fixed tuple is obtained by a finite-prime/finite-exponent truncation followed by these two tails. Its finite-dimensional prime-power laws equal those of independent Haar-uniform profinite integers. Their gcd vectors are almost surely finite: the probability that a prime \(p\) divides any coordinate is at most \(r/p^2\) and the sum over primes converges. The resulting law has total mass one. All its integer-tuple masses are strictly positive (each required valuation profile has positive probability at the finitely many relevant primes); for all other primes the local factor is \(1-p^{-1}+p^{-1}(1-p^{-1})^r=1-O_r(p^{-2})\), so the Euler product is positive and convergent.

**4. The universal cutoff fails beyond \(d\) translates.** Choose any irrational \(\alpha>2^d/d!\), take shifts \(h_j=j\) for \(0\le j\le d\), and put \(a_j(n)=\lfloor\alpha(n+j)^d\rfloor\). The integer
\[
S(n)=\sum_{j=0}^d(-1)^{d-j}\binom dj a_j(n)
\]
satisfies \(\alpha d!-2^d<S(n)<\alpha d!+2^d\): the exact \(d\)-th finite difference of \(\alpha n^d\) is \(\alpha d!\), and the sum of absolute floor-error coefficients is \(2^d\). Thus \(S(n)>0\). Choose a prime \(p>\alpha d!+2^d\), so \(0<S(n)<p\) for every \(n\). The \(d+1\) floor values cannot all be divisible by \(p\), since then \(p\mid S(n)\). Hence the actual density of \(\{n:p\mid G_j(n),\ 0\le j\le d\}\) is zero, whereas the proposed independent-residue formula would give \(p^{-(d+2)}>0\). This proves sharpness without invoking an unproved general non-equidistribution claim.

## Verification

The standalone Python program `verify.py` checks exact CRT residue counts, enumerates two-coordinate local \(p\)-adic probability profiles for selected prime powers, compares six predicted quadratic joint GCD masses with integer-square-root enumeration at 120,000 inputs, checks a cubic three-shift divisibility probability at 60,000 inputs, and tests the explicit quadratic three-translate obstruction for 20,000 inputs. All checks passed. They confirm the formulas in finite samples, not the analytic limiting or large-prime claims. To reproduce, run `python verify.py` using the Python standard library.

## Relationship to prior work

Philippa Holdridge's November 2026 paper establishes a coprimality density for the *single common GCD* of \(n\) and several integer-part polynomial values, and crucially its Theorem 1.3 supplies the large-prime estimate invoked here. The distinction is that this theorem determines the *entire joint distribution of separate GCDs*, including their dependence through \(n\), and proves a sharp number-of-translates threshold. Banks–Shparlinski concerns related gcd questions under Diophantine restrictions; neither its individual-density results nor Holdridge's common-GCD equality states the joint mass formula. The published result *Coprimality densities for split integer polynomials and equidistributed integer parts* concerns one GCD with a split polynomial as its first coordinate, rather than the separate shared-coordinate translate vector. The \(r=1\) specialization of this theorem is a previously known single-GCD distribution and is not claimed as an original result; the contributions are the joint law for at least two translates and the sharp boundary. These prior theorems and standard equidistribution are essential foundations, not claimed as new results.

## Limitations

The law is not asserted for arbitrary polynomial families, for \(r>d\), or for independently growing shifts. Failure at \(d+1\) is an explicit counterexample to universality, not a classification of all possible coefficient choices beyond the threshold. A general adelic or multivariate distribution theorem in less directly related literature may implicitly include the joint law; bibliographic coverage cannot rule out every such source. No independent mathematical validation is claimed.

## References

1. Philippa Holdridge, *On the probability that the integer parts of polynomials are coprime*, arXiv:2611.02223v1 (first public 2026-11-01), https://arxiv.org/html/2611.02223v1; Theorems 1.2 and 1.3 and proof of the latter in Section 6.
2. William Banks and Igor E. Shparlinski, *On the greatest common divisor of integer parts of polynomials*, arXiv:2205.00253v3, https://arxiv.org/html/2205.00253v3.
3. Zakhar Kabluchko and Alexander Marynych, *Divisibility properties of polynomial expressions of random integers*, arXiv:2311.05369v1, https://arxiv.org/html/2311.05369v1 (a distinct random-input model).
4. *Coprimality densities for split integer polynomials and equidistributed integer parts*, published research result, https://github.com/published-finding corpus/2026.
