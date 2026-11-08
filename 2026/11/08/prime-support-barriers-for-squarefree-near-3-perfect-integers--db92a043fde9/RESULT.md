# Prime-support barriers for squarefree near-3-perfect integers

## Finding
Call an integer \(n>1\) *near-\(3\)-perfect* if \(\sigma(n)=3n+d\), where \(d\) is a positive proper divisor of \(n\) and \(\sigma\) is the sum-of-divisors function. Write \(\omega(n)\) for the number of distinct prime factors.

**Theorem.** Suppose \(n\) is squarefree and near-\(3\)-perfect.

1. If \(n\) is even, it has the form \(n=6\prod_{j=1}^{r}p_j\) with distinct primes \(p_j\equiv1\pmod3\), where \(r\) is odd and \(r\ge13\). Hence \(\omega(n)\ge15\).
2. If \(n\) is odd, then \(\omega(n)\ge122\). If \(3\nmid n\), every prime divisor is \(1\pmod3\); if \(3\mid n\), at most one *other* prime divisor is \(2\pmod3\).

In particular, every squarefree near-\(3\)-perfect integer has at least \(15\) distinct prime factors. The even \(13\)-prime boundary has a stronger finite classification: the only possible prime supports for which \(\sigma(n)>3n\) are
\[
\{2,3,7,13,19,31,37,43,61,67,73,79,q\},
\qquad q\in\{97,103,109\},
\]
and none satisfies the required divisibility \(\sigma(n)-3n\mid n\).

## Assumptions and scope
All positive divisors, including \(1\), are permitted for \(d\), but \(d<n\) is required; the proof uses only \(0<d\mid n\). The integer \(n\) is squarefree. In particular, an omitted-divisors definition of *\(3\)-near-perfect* involving three omissions is **not** the notion considered here. The assertion gives necessary conditions, not the existence of such integers, and it does not classify nonsquarefree near-\(3\)-perfect numbers.

## Proof
**1. Local restrictions at the prime \(3\).** Suppose first that \(n\) is even and squarefree. If \(3\nmid n\), then \(3\mid\sigma(n)\) because \(\sigma(2)=3\). Since \(3\mid3n\), the positive divisor \(d=\sigma(n)-3n\) is divisible by \(3\), contradicting \(d\mid n\). Thus \(6\mid n\). If an odd prime \(p\mid n\), distinct from \(3\), has \(p\equiv2\pmod3\), then \(3\mid p+1\) and \(9\mid\sigma(n)\) (using the factor \(\sigma(2)=3\)); also \(9\mid3n\). Consequently \(9\mid d\), contradicting squarefreeness. Write \(n=6P\), where \(P=\prod_{j=1}^{r}p_j\) and every \(p_j\equiv1\pmod3\).

Here \(\sigma(n)=12\sigma(P)\), so \(d=6D\), with \(D=2\sigma(P)-3P\). Because \(0<d\mid6P\), one has \(0<D\mid P\). Each divisor of \(P\) is \(1\pmod3\), but \(D\equiv2^{r+1}\pmod3\), as \(\sigma(P)=\prod(p_j+1)\equiv2^r\pmod3\). Hence \(r\) must be odd, so \(\omega(n)=r+2\) is odd.

Now let \(n\) be odd. If \(3\nmid n\) but some prime \(p\mid n\) has \(p\equiv2\pmod3\), then both \(\sigma(n)\) and \(3n\) are divisible by \(3\), forcing \(3\mid d\mid n\), a contradiction. If \(3\mid n\) and at least two other prime factors are \(2\pmod3\), their factors \(p+1\) make \(9\mid\sigma(n)\), while \(9\mid3n\); thus \(9\mid d\mid n\), also impossible. These are precisely the stated odd prime-support restrictions.

**2. Odd support count.** Let \(q_1<q_2<\cdots\) be the primes congruent to \(1\pmod3\), beginning \(7,13,19,31,\ldots\). By part 1, a squarefree *odd* candidate has at most one prime congruent to \(2\pmod3\), and if \(3\) is absent it has none. Consequently its increasing sequence of prime factors is coordinatewise at least the initial segment of
\[
3,5,q_1,q_2,q_3,\ldots.
\]
For \(\omega(n)\le121\), multiplicativity and monotonicity of \(1+1/p\) therefore give
\[
\frac{\sigma(n)}n\le\frac43\frac65\prod_{j=1}^{119}\frac{q_j+1}{q_j}<3.
\]
The final inequality is an *exact integer comparison*: \(q_{119}=1567\), and the integer product \(24\prod_{j\le119}(q_j+1)\) is smaller than \(45\prod_{j\le119}q_j\). The attached checker independently confirms this and verifies that adding \(q_{120}=1579\) reverses the inequality. This contradicts \(\sigma(n)/n=3+d/n>3\). Thus \(\omega(n)\ge122\) when \(n\) is odd.

**3. Even support count and the exhaustive boundary.** Suppose \(n=6P\) with \(r\) odd. Put \(t_j=q_j\) for the increasing primes \(1\pmod3\). Since \(\sigma(n)/n=2\prod_{j=1}^r(1+1/p_j)>3\), if \(r\le10\) then the maximum obtained at the first ten \(t_j\)'s is less than \(3\) (indeed, multiplying by the eleventh gives only \(3.00718\ldots\), so the first ten are still below \(3\)). As \(r\) is odd, the first unresolved case is \(r=11\).

If any of the first ten primes \(p_j\) exceeds \(t_j\), then by increasing order all following primes move up at least one place. The largest possible abundancy index among such deviations is obtained by omitting \(t_{10}=79\) and taking \(t_1,\ldots,t_9,t_{11},t_{12}\). The exact comparison
\[
2\prod_{j=1}^{9}(t_j+1)(t_{11}+1)(t_{12}+1)
<3\prod_{j=1}^{9}t_j\,t_{11}t_{12}
\]
excludes every deviation. Hence \(p_j=t_j\) for \(1\le j\le10\). The last prime \(q=p_{11}\) must satisfy
\[
2\left(\prod_{j=1}^{10}\frac{t_j+1}{t_j}\right)\frac{q+1}{q}>3.
\]
This expression decreases with \(q\), and the exact comparison at \(q=127\) fails. The only possible primes \(1\pmod3\) from \(97\) through \(126\) are \(97,103,109\), as claimed.

For \(Q=\prod_{j=1}^{10}t_j\) and \(B=\prod_{j=1}^{10}(t_j+1)\), the needed divisor is \(d=6D\) with \(D=2B(q+1)-3Qq\). All three \(D\)'s are positive, but exact Euclidean arithmetic gives

| \(q\) | \(P=Qq\) | \(D\) | \(\gcd(P,D)\) |
|---:|---:|---:|---:|
| 97 | 194963444966161417 | 1399885548030949 | 152551 |
| 103 | 207023039500150783 | 1116421565237251 | 1983163 |
| 109 | 219082634034140149 | 832957582443553 | 152551 |

In every row \(\gcd(P,D)<D\), so \(D\nmid P\), a contradiction. Therefore \(r\ne11\). Since \(r\) is odd and the smaller cases failed, \(r\ge13\). Hence \(\omega(n)=r+2\ge15\). This completes the proof.

## Verification
Run `python3 checker.py` with Python 3 and no external dependencies. It generates primes by trial division, checks both sides of the odd \(121\)- and \(122\)-support threshold with arbitrary-precision integers, verifies the even \(13\)-support maximizing inequalities and prime list, and checks all three exact gcd obstructions. The corresponding actual stdout is `verification_output.txt`. The checker is a finite *arithmetic certificate* for the explicitly reduced computations, not a brute-force search over all integers.

## Relationship to prior work
Das and Saikia (2017), *On Near 3-Perfect Numbers*, introduce the same single-redundant-divisor equation and classify ten families with three distinct prime factors, together with examples having four distinct factors. Their inspected propositions and discussion do not state the squarefree prime-support restrictions or the \(15\)/\(122\) bounds. OEIS A289056 reproduces the ten classified three-prime-support cases; its tabulation does not establish any bound on all squarefree solutions. Literature on *\(k\)-near-perfect* numbers with \(k\) omitted divisors uses a different definition, and is not an implication of the single-omission \(\sigma(n)=3n+d\) problem. The proof here uses elementary congruences and exact extremal abundancy products; no originality claim rests solely on unsuccessful keyword search.

## Limitations
The support restrictions are necessary, not sufficient. The conclusion does not assert existence of any squarefree near-\(3\)-perfect integer, nor sharpness of the support lower bounds. The \(122\) threshold for odd candidates is the first support count where the *abundancy inequality alone* allows such a candidate; it is not a construction. The comparison with published work is limited by indexing and may miss equivalent unpublished or obscure results. The finite integer certificate supplements, rather than replaces, the proof of the infinite statements.

## References
1. B. Das and H. K. Saikia, *On Near 3-Perfect Numbers*, Sohag Journal of Mathematics **4** (2017), 1–5, published online 2017-01-01, DOI: 10.18576/sjm/040101. Full text: https://www.naturalspublishing.com/files/published/cm9ns18p8j11z8.pdf
2. OEIS A289056, *Near 3-perfect numbers of the form \(2^a p^t q\)*, https://oeis.org/A289056 (contextual table of the ten 2017 cases).
3. P. Pollack and V. Shevelev, *On perfect and near-perfect numbers*, Journal of Number Theory **132** (2012), 3037–3046, DOI: 10.1016/j.jnt.2012.06.008 (different multiplier, general background).
