# The exact GCD distribution of two consecutive sums of cubes

## Finding
Put
\[
F(x,y)=x^3+y^3,\qquad H(x,y)=(x+1)^3+(y+1)^3,
\qquad G(x,y)=\gcd(F(x,y),H(x,y)).
\]
For each prime \(p\) and integer \(k\ge1\) define the *simultaneous local root count*
\[
R_{p,k}=\#\{(x,y)\bmod p^k:F(x,y)\equiv H(x,y)\equiv0\pmod{p^k}\}.
\]
The complete local count is
\[
\boxed{
R_{p,k}=\begin{cases}
2^k,&p=2,\quad1\le k\le3,\\
6,&p\ge5,\ p\equiv1\pmod3,\\
0,&\text{otherwise}.
\end{cases}}
\]
For every composite modulus \(m\), the simultaneous count is exactly
\(R_m=\prod_{p^k\parallel m}R_{p,k}\), by the Chinese remainder theorem.

**Exact GCD support and positive density.** A positive integer \(m\) occurs as \(G(x,y)\) for some positive integers \(x,y\) if and only if
\[
\boxed{\nu_2(m)\le3,\quad 3\nmid m,\quad
p\mid m\ \text{and}\ p\ \text{odd}\ \Longrightarrow\ p\equiv1\pmod3.}
\]
Every such \(m\) occurs on a set of ordered positive pairs of strictly positive natural density in expanding squares.

**Limiting distribution.** If \(x,y\) are chosen independently uniformly from \(\{1,\ldots,X\}\), then \(G(x,y)\) converges in distribution to an almost surely finite integer \(G_\infty\). Its prime-adic valuations \(V_p=\nu_p(G_\infty)\) are independent, and for all \(k\ge1\),
\[
\Pr(V_p\ge k)=\frac{R_{p,k}}{p^{2k}}.
\]
In particular, \(\Pr(V_2=0,1,2,3)=(1/2,1/4,1/8,1/8)\), and for every \(p\equiv1\pmod3\),
\[
\Pr(V_p=0)=1-\frac6{p^2},\qquad
\Pr(V_p=e)=6(1-p^{-2})p^{-2e}\quad(e\ge1).
\]
For all other odd primes, \(V_p=0\) almost surely. Hence
\[
\boxed{\Pr(G_\infty=1)=\frac12\prod_{p\equiv1\ (3)}(1-6p^{-2})\approx0.406,}
\qquad
\boxed{\mathbb E[G_\infty^t]<\infty\ \Longleftrightarrow\ t<1}
\]
for every real \(t\). Thus the limiting integer is finite almost surely but has infinite mean.

## Assumptions and scope
The coordinates \(x,y\) are positive integers when considering exact GCD values and natural densities. The local root count uses complete ordered pairs modulo a prime power, including zero residues. The gcd is positive because the two evaluated sums are positive. For a positive integer \(m\), \(\nu_p(m)\) is its usual prime exponent. Natural density of pairs means a limit after division by \(X^2\) over \(1\le x,y\le X\). All statements about moments concern the limiting random variable, not uniform integrability or asymptotics of finite-square moments. \(p\equiv1\pmod3\) always means a prime at least seven.

## Proof
**1. Factor both cubic sums.** Introduce \(s=x+y\) and \(A=x^2-xy+y^2=3x^2-3sx+s^2\). The integer-linear substitution \((x,y)\longleftrightarrow(x,s)\) is invertible over every residue ring, and
\[
F=sA,\qquad H=(s+2)B,\qquad B=A+s+1.
\]
For a prime \(p\ge5\), every simultaneous zero over \(\mathbb F_p\) belongs to one of three mutually exclusive branches, because \(s\) and \(s+2\) cannot simultaneously vanish:
\[
\begin{array}{c|c|c}
\text{branch}&s&\text{quadratic equation in }x\\\hline
I&0&3x^2+1=0\\
II&-2&3(x+1)^2+1=0\\
III&-1&3x^2+3x+1=0.
\end{array}
\]
For branch III, \(A=B=0\) implies \(s=-1\). Every quadratic has discriminant of square class \(-3\). For \(p\ne3\), the element \(-3\) is a square in \(\mathbb F_p\) exactly when the field contains a nontrivial cubic root of unity, equivalently \(p\equiv1\pmod3\). Thus there are exactly six distinct common zeros for \(p\equiv1\pmod3\), and none for \(p\equiv2\pmod3\). No branch overlaps another since \(0,-1,-2\) are distinct modulo \(p\ge5\).

**2. Check smoothness and lift uniquely at each prime at least five.** In branch I, \(A=-1\) and \(s+2=2\) at the common zero, and the derivative with respect to \(x\) of \(B\) is \(6x\ne0\) because \(3x^2=-1\). The gradients of \(F\) and \(H\) are therefore independent. In branch II, \(B=-1\), \(s=-2\), and the \(x\)-derivative of \(A\) is \(6(x+1)\ne0\); again the gradients are independent. In branch III, \(s=-1\), \(A=B=0\), and the \(x\)-derivative of \(A\) is \(6x+3\ne0\); otherwise its quadratic discriminant would vanish, impossible for \(p\ge5\). The common Jacobian determinant is nonzero in every case. Multivariate Hensel lifting therefore supplies **exactly one** solution modulo \(p^k\) above each common zero modulo \(p\), for every \(k\ge1\). This proves the six-or-zero branch of the formula.

**3. Exceptional primes.** Modulo three, cubes reduce to the underlying residue, so \(F\equiv s\pmod3\) while \(H\equiv s+2\pmod3\). They cannot both vanish, giving \(R_{3,k}=0\) at every depth.

Modulo two, \(F\equiv s\) and \(H\equiv s\), so the two common roots are exactly the **same-parity** pairs \((0,0)\) and \((1,1)\). Direct expansion of cubes modulo four shows that the complete set of roots is \(y\equiv2-x\pmod4\) when \(x\) is even, and \(y\equiv-x\pmod4\) when \(x\) is odd. Thus there are four roots modulo four. Modulo eight the complete set is \(y\equiv6-x\pmod8\) for even \(x\), and \(y\equiv-x\pmod8\) for odd \(x\); hence there are eight roots modulo eight. Both descriptions can be verified by checking the four or eight residue classes for \(x\) and evaluating the two cubes; the standalone checker independently enumerates all pairs. To exclude a solution modulo sixteen, note that if the parities differ then \(F\) is odd. If both coordinates are odd, \(A\) is odd and \(16\mid F=sA\) implies \(16\mid s\). Now \(A\equiv3\pmod8\), since \(y\equiv-x\pmod8\) and odd squares are one modulo eight. Hence \(B=A+s+1\equiv4\pmod8\), while \(\nu_2(s+2)=1\), forcing \(\nu_2(H)=3\), contradiction. If both coordinates are even, \(B=A+s+1\) is odd and \(16\mid H\) forces \(s\equiv-2\pmod{16}\), so \(\nu_2(s)=1\). Write \(x=2u\), \(y=2v\), with \(u+v\) odd; then \(A=4(u^2-uv+v^2)\) has valuation exactly two, giving \(\nu_2(F)=3\), contradiction. Therefore \(R_{2,k}=0\) for all \(k\ge4\), completing the local formula.

**4. Control large prime divisors.** Fix \(X\ge1\) and a prime \(p\ge5\). Any \(p\mid G(x,y)\) must have \(s=x+y\equiv0,-1\) or \(-2\pmod p\), and one of at most two corresponding \(x\)-classes for each of these three branches. There are at most \(2X/p+1\) possible values of \(s\) in \([2,2X]\) in a fixed class and at most \(X/p+1\) values of \(x\) in \([1,X]\) in a given class. Thus
\[
\#\{(x,y)\in[1,X]^2:p\mid G(x,y)\}
\le6(2X/p+1)(X/p+1).
\]
Moreover, such a prime must divide one of \(s,s+1,s+2\), all positive and at most \(2X+2\); hence \(p\le2X+2\). Summing over primes \(M<p\le2X+2\) and dividing by \(X^2\) gives
\[
\limsup_{X\to\infty}\Pr\{\exists p>M:p\mid G(x,y)\}
\le\frac{12}{M}
\]
(for instance, bound the prime sums by the corresponding integer sums). Consequently the contribution of unbounded primes vanishes uniformly in the limit as \(M\to\infty\).

**5. Distribution and exact-value realization.** For any fixed finite collection of primes and powers, uniform distribution of positive integer pairs in residue classes together with the Chinese remainder theorem yields independence of prime-primary divisibility and the exact tails \(R_{p,k}/p^{2k}\). The events of arbitrarily high exponent at a fixed prime have probability zero, by the displayed tails. The union bound in Step 4 makes these finite-prime laws tight as a full integer-valued distribution. Indeed, \(\sum_{p\ge5}6p^{-2}<\infty\), so the independent limiting valuations are nonzero at only finitely many primes almost surely. The local masses listed above multiply to a positive probability for every integer with the stated permitted prime support: the remaining infinite product is positive since \(\sum_p6/p^2<\infty\). Integers with forbidden prime factors or too large a two-exponent have probability zero and are, by the local obstruction, never attained. This proves both the support classification and the strict positive density for each permitted exact GCD value (hence actual positive-integer realizations).

**6. Moment boundary.** For \(p\equiv1\pmod3\), the individual valuation moment when \(t<2\) is
\[
\mathbb E[p^{tV_p}]=1+\frac{6(p^t-1)}{p^2-p^t}.
\]
For \(0<t<1\), its excess over one is \(O(p^{t-2})\), summable over all primes, while the two-primary factor is finite, proving finite moments. For \(t\le0\), \(G_\infty^t\le1\). At \(t=1\), the split-prime factor equals \(1+6/p\), and \(\sum_{p\equiv1\ (3)}1/p=\infty\) (the standard divergence of reciprocal primes in a reduced arithmetic progression), forcing infinite mean. Every \(t>1\) also diverges by monotonicity since \(G_\infty\ge1\). This proves the exact transition.

## Verification
Run `python3 verify_cubic_gcd.py` with Python 3 (standard library only). The independent residue enumerator checks \(R_{p,k}\) for 32 finite prime-power moduli, including all dyadic depths up to the first empty one. A separate single-lift test checks 24 smooth roots, and an exact integer-grid scan checks the prime support obstruction for 22,500 pairs. All tests passed. They corroborate the algebraic steps but do not prove the unrestricted theorem; the proof rests on Steps 1–6. The observed coprimality frequencies in squares of sides 100, 300 and 600 are approximately 0.4068, 0.40504 and 0.40543, consistent with the Euler product but not an error estimate.

## Relationship to prior work
Kabluchko and Marynych (2023), particularly their theorem on limiting GCD distributions of polynomial values, provide a general convergence framework. The present theorem computes *all* local root counts for a specific pair of translated diagonal cubic sums and, using a direct large-prime sieve, determines exact-value support and the sharp moment frontier not supplied by the general convergence statement. Bodin and Dèbes (2021/2023) give a general coprimality density framework in several variables; its unevaluated Euler factors do not determine the explicit split-prime six-root law or the dyadic cutoff. Brüdern and Vaughan (2021) analyze the distribution of representations of a *single* sum of two cubes, not the GCD of two translated sums.

The previously published exact collision/fibre calculation for the single map \(x^3+y^3\) counts equal *outputs of that one map* and does not compare it with its simultaneous shift. Similarly, the finite-resultant correction for a pair of homogeneous binary forms does not apply directly to \(F,H\), because \(H\) is nonhomogeneous in \(x,y\). These are statement-level distinctions, not deductions of novelty from titles alone.

## Limitations
The moment threshold is for the limiting law, not a uniform statement for moments at finite \(X\). The theorem covers the simultaneous unit translation of both variables; other shifts can exhibit different branches and bad-prime behavior. The full literature search may miss equivalent results expressed via p-adic intersection multiplicities, local zeta functions or resultants; no independent audit or exhaustive priority certification is claimed. Modular experiments verify finite cases only.

## References
- Z. Kabluchko and A. Marynych, *Divisibility properties of polynomial expressions of random integers*, arXiv:2311.05369v1 (first public 9 November 2023), https://arxiv.org/abs/2311.05369 .
- A. Bodin and P. Dèbes, *Coprime values of polynomials in several variables*, arXiv:2105.13883v1 (first public 28 May 2021), Israel Journal of Mathematics **257** (2023), 25–55, https://arxiv.org/abs/2105.13883 .
- J. Brüdern and R. C. Vaughan, *A Montgomery–Hooley Theorem for sums of two cubes*, European Journal of Mathematics **7** (2021), 1616–1644, https://doi.org/10.1007/s40879-021-00495-4 .
- *Exact finite-level collision moments and p-adic fibres for sums of two cubes* (published research result, 18 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-finite-level-collision-moments-and-p-adic-fibres-for-sums--8251985a3185 .
- *Finite-resultant correction for coprime values of homogeneous binary forms* (published research result, 4 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-resultant-correction-for-coprime-values-of-homogeneous-bi--0efa4a963ad2 .
