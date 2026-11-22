# Genus and five-adic ramification of Fibonacci-weighted exponential curves

## Finding
For each integer \(k\ge2\), let \(F_0=0\), \(F_1=1\), \(F_{n+2}=F_{n+1}+F_n\), and define the formal exponential series
\[
G_k(x)=\exp\!\left(\sum_{n\ge1}5F_n^{2k}\frac{x^n}{n}\right),
\qquad N_k=5^{k-1}.
\]
Let \(C_k\) be the unique smooth projective curve over \(\mathbb Q\) with function field \(\mathbb Q(x,G_k(x))\). Write \(\nu_5(m)\) for the exponent of \(5\) in a positive integer \(m\). Then:

1. The degree-\(N_k\) morphism \(x:C_k\to\mathbb P^1\) is geometrically cyclic, branched at exactly \(2k+1\) geometric points: \(2k\) points in \(k\) conjugate quadratic pairs over \(\mathbb Q(\sqrt5)\), and one rational point. There is no ramification over infinity. The point indexed by \(0\le j\le2k\) has ramification index
   \[
   e_{k,j}=5^{k-1-\nu_5(\binom{2k}{j})}.
   \]
2. Its geometric genus is the exact, nonrecursive integer
   \[
   \boxed{g(C_k)=1+\frac{(2k-1)5^{k-1}-\sum_{j=0}^{2k}5^{\nu_5(\binom{2k}{j})}}{2}.}
   \]
3. If \(2k=\sum_i d_i5^i\) is its base-five expansion, then exactly \(\prod_i(d_i+1)\) of the branch points have full ramification index \(N_k\). In particular, **every branch point is totally ramified if and only if**
   \[
   \boxed{2k+1=5^a\quad\text{or}\quad 2k+1=3\cdot5^a\quad\text{for an integer }a\ge1.}
   \]
   Precisely in these cases \(g(C_k)=(2k-1)(5^{k-1}-1)/2\). In general \(g(C_k)=(k-\tfrac12)5^{k-1}+O(k^2)\).
4. The normal closure of \(\mathbb Q(x,G_k)/\mathbb Q(x)\) has Galois group \(C_{N_k}\rtimes(\mathbb Z/N_k\mathbb Z)^\times\), with the natural unit action on the cyclic group. In particular, its order is \(N_k\varphi(N_k)\).

For instance \(g(C_2)=6\), \(g(C_3)=54\), \(g(C_4)=432\), and \(g(C_7)=101556\); the indices \(k=2\) and \(k=7\) have only totally ramified branch points, whereas \(k=3\) has four fully ramified points and three with index five.

## Assumptions and scope
Everything is in characteristic zero. The curve means smooth projective **normalization** of the affine relation, not the potentially singular plane model itself. The result applies to every integer \(k\ge2\) and to the specific Fibonacci-exponential series above; it asserts no classification of all Fibonacci-weighted algebraic functions. Rational points, genus, and branch points are distinguished from the *degree* of the generating function, which was already established in earlier work.

## Proof
**1. The established rational-power identity.** Define Lucas numbers by \(L_0=2\), \(L_1=1\), \(L_{n+2}=L_{n+1}+L_n\). Theorem 4.1 of Li–Zhong–Zhou [1] gives \(G_k^{N_k}=R_k\), where
\[
R_k(x)=\bigl(1-(-1)^k x\bigr)^{(-1)^{k+1}\binom{2k}{k}}
\prod_{j=0}^{k-1}\bigl(1-(-1)^jL_{2(k-j)}x+x^2\bigr)^{(-1)^{j+1}\binom{2k}{j}}.
\tag{1}
\]
It also proves that \(\mathbb Q(x,G_k)/\mathbb Q(x)\) has degree \(N_k\). The proof below separately establishes geometric irreducibility and then derives the new assertions.

**2. Distinct branch points.** Put \(\alpha=(1+\sqrt5)/2\). By Binet's formula \(\alpha\beta=-1\) and \(L_m=\alpha^m+\beta^m\). Over \(\overline{\mathbb Q}\), the factors in (1) split as \(1-\lambda_jx\) for \(0\le j\le2k\), with
\[
\lambda_j=(-1)^j\alpha^{2(k-j)},\qquad
\operatorname{ord}_{x=\lambda_j^{-1}}(R_k)=(-1)^{j+1}\binom{2k}{j}.
\]
Their absolute values are pairwise distinct because \(\alpha>1\), so all \(2k+1\) points are distinct. The central index \(j=k\) gives the rational point \(x=(-1)^k\). For each \(j<k\), the pair \(j,2k-j\) is the root pair of an irreducible rational quadratic: its discriminant is \(5F_{2(k-j)}^2\), which is nonsquare in \(\mathbb Q\). Thus precisely \(k\) rational quadratic factors occur. Since
\[
\sum_{j=0}^{2k}(-1)^{j+1}\binom{2k}{j}=0,
\]
\(\operatorname{ord}_{\infty}(R_k)=0\). The exponent at \(j=0\) equals \(-1\); hence \(Y^{N_k}-R_k\) is irreducible even over \(\overline{\mathbb Q}(x)\), by a discrete-valuation Eisenstein argument. This proves geometric connectedness and degree \(N_k\).

**3. No cancellation of branch loci.** For \(k=2\), \(\binom42=6\) and all \(\binom4j\) are prime to five. For \(k\ge3\), \(\binom63=20<25\); the ratio of successive central binomial coefficients is
\[
\frac{\binom{2k+2}{k+1}}{\binom{2k}{k}}=4-\frac{2}{k+1}<5.
\]
Induction gives \(\binom{2k}{j}\le\binom{2k}{k}<5^{k-1}\) for every \(k\ge3\). Therefore \(\nu_5(\binom{2k}{j})<k-1\) at every index (also for \(k=2\)), so every listed geometric point is genuinely branched. For a tame Kummer cover \(y^{N_k}=R_k(x)\), a point of valuation \(m\) has exactly \(\gcd(N_k,m)\) points above it, each of ramification index \(N_k/\gcd(N_k,m)\). This gives the displayed indices.

**4. Genus.** Apply the Riemann–Hurwitz formula to the geometrically connected degree-\(N_k\) map to \(\mathbb P^1\). The aggregate different contribution at index \(j\) is \(N_k-\gcd(N_k,\binom{2k}{j})\). Infinity contributes zero. Hence
\[
2g(C_k)-2=-2N_k+\sum_{j=0}^{2k}\left(N_k-\gcd(N_k,\binom{2k}{j})\right).
\]
Using \(\gcd(N_k,\binom{2k}{j})=5^{\nu_5(\binom{2k}{j})}\) proves the genus formula, with all boundary terms included.

**5. Base-five digits.** Lucas's binomial congruence theorem says \(\binom{2k}{j}\not\equiv0\pmod5\) exactly when every base-five digit of \(j\) is at most the corresponding digit \(d_i\) of \(2k\). Thus there are exactly \(\prod_i(d_i+1)\) such \(j\), and these are precisely the totally ramified points. Every \(0\le j\le2k\) has this property if and only if all base-five digits of \(2k\) below its leading digit are four. Because \(2k\) is even, its leading nonzero base-five digit is even, hence either two or four. Consequently \(2k+1\) is \(3\cdot5^a\) or \(5^{a+1}\) for \(a\ge0\); restricting to \(k\ge2\) gives exactly the claimed possibilities with exponent at least one. Full ramification is equivalent to all \(\gcd\) terms being one, giving the simplified genus.

Kummer's carry interpretation of \(\nu_5(\binom{2k}{j})\) bounds it by the number of base-five digits of \(2k\) minus one. Hence \(5^{\nu_5(\binom{2k}{j})}\le2k\) and the genus correction sum is \(O(k^2)\). This proves the asymptotic with its stated error.

**6. Arithmetic Galois closure.** The rational-power identity has \(R_k(0)=1\), so the absolutely irreducible curve has a nonsingular rational point \((x,y)=(0,1)\) (since \(N_k\ne0\) in characteristic zero). It is geometrically connected with constant field \(\mathbb Q\). After adjoining a primitive \(N_k\)-th root of unity \(\zeta\), the Kummer extension is cyclic of degree \(N_k\), generated by \(y\mapsto\zeta y\). Every automorphism of \(\mathbb Q(\zeta)/\mathbb Q\) extends by fixing \(x,y\), because \(R_k\) has rational coefficients. This supplies a splitting of the cyclotomic quotient, whose conjugation action is multiplication by the corresponding unit modulo \(N_k\), establishing the stated semidirect product.

## Verification
Run `python3 check_fibonacci_curves.py` from the package directory. The independent standard-library checker verifies 192 exact Fibonacci–Lucas power identities (the exponentiated product's logarithmic coefficients), 100 infinity-exponent cancellations, and 98 complete genus/digit/inertia comparisons for \(2\le k\le99\), along with six explicit numerical fixtures. All checks use Python exact integers. These finite tests do not establish the all-\(k\) statements; Steps 1–6 above do.

## Relationship to prior work
Li, Zhong, and Zhou [1, §4, Theorem 4.1] prove the rational-power equation (1), algebraic degree, and examples for \(k=1,2,3\). Their published statements do not supply a geometric genus, all-point ramification profile, digit criterion for total ramification, or normal-closure group. A separate prior calculation of the degrees of general even-polynomial Fibonacci exponentials gives the exact algebraic degree but not these geometric invariants. Generic Kummer Riemann–Hurwitz and Lucas congruence formulas [2,3] are **standard ingredients**, not new claims; the specific all-index synthesis and arithmetic classification for this natural infinite family are the present contribution. An earlier implicit computation of these invariants is possible, and source/database coverage cannot prove absolute priority.

## Limitations
The genus is geometric and concerns characteristic zero. No assertion is made about arithmetic genus of an unnormalized plane model, Jacobian decomposition, rational point ranks, or characteristic-five reduction. The published rational-power relation, standard Kummer ramification theorem, Riemann–Hurwitz, Lucas's theorem, and Kummer's carry theorem are used with attribution. Search and comparison can leave undetected equivalent prior claims, and no independent audit has been performed.

## References
[1] J. P. Li, Y. M. Zhong, Y. B. Zhou, *Integral Exponential Series: Fibonacci Weights and Implicit Equations*, arXiv:2611.16283v1 (first posted 2026-11-12), §4, Theorem 4.1, https://arxiv.org/abs/2611.16283.

[2] Generic tame Kummer branch-index and genus formulas for cyclic covers \(y^m=f(x)\), via Riemann–Hurwitz; see standard exposition *Superelliptic curve*, https://en.wikipedia.org/wiki/Superelliptic_curve.

[3] É. Lucas, binomial congruence theorem (1878), and E. Kummer, theorem on prime-power binomial valuations (1852); standard classical number-theoretic results.

[4] P. D. Hanna, OEIS A207969 and A207970, initial small-index Fibonacci-exponential identities, https://oeis.org/A207969 and https://oeis.org/A207970.
