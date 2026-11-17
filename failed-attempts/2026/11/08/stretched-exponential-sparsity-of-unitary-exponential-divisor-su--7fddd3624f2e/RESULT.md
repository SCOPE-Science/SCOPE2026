# Stretched-exponential sparsity of unitary–exponential divisor-sum coincidences

## Finding

Define the two multiplicative arithmetic functions \(U(1)=T(1)=1\) by the prime-power values
\[
U(p^a)=1+p^a,\qquad T(p^a)=\sum_{d\mid a}p^d
\]
for each prime \(p\) and integer \(a\ge1\). Thus \(U(n)=\sigma^*(n)\), the sum of unitary divisors of \(n\), and \(T(n)=\sigma^{(e)}(n)\), the sum of exponential divisors of \(n\). Let
\[
E(X)=\#\{n\in\mathbb Z:1\le n\le X,\ U(n)=T(n)\}.
\]
There is an absolute \(C>0\) such that for every real \(X\ge e^{16}\),
\[
\boxed{E(X)\le C X(\log X)^2\exp\!\bigl(-\sqrt{\log X}\bigr).}
\]
In particular, the set of solutions of \(\sigma^*(n)=\sigma^{(e)}(n)\), recorded as OEIS A236474, has natural density zero. The stronger, quantitative statement is the principal result.

## Assumptions and scope

All logarithms are natural. For \(X\ge1\) and \(y\ge2\), let \(\Psi(X,y)\) be the number of positive integers at most \(X\) having no prime factor greater than \(y\), including \(1\). The value \(n=1\) is included in \(E(X)\). No assumptions on prime distribution beyond the classical upper bound \(\sum_{p\le y}p^{-1}\le\log\log y+O(1)\) are needed. The theorem concerns a counting bound and does not resolve infinitude of solutions.

## Proof

**Step 1 (uniqueness of a large exponent-one prime).** If a prime \(p\) divides \(n\) exactly once, put \(n=pm\) with \(p\nmid m\). The prime-power definitions and multiplicativity give
\[
U(n)=(p+1)U(m),\qquad T(n)=pT(m).
\]
Thus equality \(U(n)=T(n)\) forces
\[
p\bigl(T(m)-U(m)\bigr)=U(m).
\]
Since \(U(m)>0\), the difference \(T(m)-U(m)\) is positive, and the prime \(p\) is uniquely determined by \(m\):
\[
p=\frac{U(m)}{T(m)-U(m)}.
\]
In particular, for a fixed \(m\), at most one prime \(p\) yields an equality solution of this form. This is a necessary condition, not an assertion that the displayed quotient is a prime.

**Step 2 (uniform smooth-number reduction).** Fix \(2\le y\le X\). Partition solution integers \(n\le X\) according to whether their largest prime divisor is at most \(y\) (the \(y\)-smooth case), greater than \(y\) and occurs once, or greater than \(y\) and occurs to exponent at least two. The first part has at most \(\Psi(X,y)\) elements. In the second part write \(n=pm\) with \(p>y\) its largest prime divisor, occurring exactly once. Here \(m<X/y\), and Step 1 permits at most one \(p\) per such \(m\), so there are at most \(\lfloor X/y\rfloor\) elements. Every integer in the third part is divisible by \(p^2\) for some prime \(p>y\), and the union bound gives at most \(X\sum_{p>y}p^{-2}\) elements. Hence
\[
\boxed{E(X)\le\Psi(X,y)+\lfloor X/y\rfloor+X\sum_{p>y}p^{-2}.}
\tag{1}
\]
No primality distribution or disjointness is required for this upper bound. For \(y\ge2\), \(\sum_{p>y}p^{-2}\le\sum_{m>y}m^{-2}\le2/y\).

**Step 3 (a quantitative smooth-number estimate).** For \(y\ge e^4\) put \(\alpha=1-1/\log y\), so \(3/4\le\alpha<1\). The Rankin bound, obtained by multiplying the Euler geometric series over primes at most \(y\), gives
\[
\Psi(X,y)\le X^\alpha\prod_{p\le y}\frac1{1-p^{-\alpha}}.
\tag{2}
\]
For \(p\le y\), \(p^{-\alpha}=p^{-1}p^{1/\log y}\le e/p\). Also, because \(\alpha\ge3/4\), the quadratic corrections in \(-\log(1-p^{-\alpha})\) have bounded sum: explicitly, \(-\log(1-t)\le t+t^2/(1-t)\) and \(t=p^{-\alpha}\le2^{-3/4}\), while \(\sum_p p^{-2\alpha}\le\sum_{m\ge2}m^{-3/2}<\infty\). Using the classical prime-harmonic upper bound,
\[
\log\prod_{p\le y}(1-p^{-\alpha})^{-1}
\le e\sum_{p\le y}p^{-1}+O(1)
\le e\log\log y+O(1).
\]
Therefore a universal constant \(C_0>0\) satisfies
\[
\Psi(X,y)\le C_0X\exp\!\left(-\frac{\log X}{\log y}\right)(\log y)^e.
\tag{3}
\]

**Step 4 (balance).** For \(X\ge e^{16}\), choose \(y=\exp(\sqrt{\log X})\). Then \(y\ge e^4\), \(2\le y\le X\), and (1)–(3) imply
\[
E(X)\le C_0X\exp(-\sqrt{\log X})(\log X)^{e/2}
+3X\exp(-\sqrt{\log X}).
\]
Here \(e\) denotes the base of the natural logarithm and \(e/2<2\); hence the claimed absolute-constant bound follows. Dividing by \(X\) and letting \(X\to\infty\) proves natural density zero. \(\square\)

## Verification

Run `python verify_equality_sparsity.py` using Python 3, which requires no external packages. It independently computes the two multiplicative functions by exact prime factorization for every integer through \(500000\), tests the exponent-one prime-removal identity for each eligible prime factor, and checks that equality occurs precisely at \(1,20,45,320,6615,382200\) in this interval. The proof above does not rely on finite testing. The analytic input is the classical prime-harmonic upper bound; no numerical estimate for its constant is required.

## Relationship to prior work

Trudgian's 2013 preprint asks whether there are infinitely many equality solutions and discusses the density of the strict inequality \(\sigma^*(n)>\sigma^{(e)}(n)\). The present theorem does **not** answer the infinitude question and does **not** compute the strict-inequality density; instead it gives a quantitative zero-density theorem for the equality boundary. OEIS A236474 records known solutions without a corresponding counting bound. Other published comparisons provide finite prime-exponent classifications or positive lower bounds for the strict-inequality density, neither of which directly supplies the global stretched-exponential upper bound claimed here. The elementary uniqueness mechanism in Step 1, combined with the smooth-number reduction, is the specific contribution.

## Limitations

The upper bound may be far from optimal. It neither proves that infinitely many solutions exist nor determines their eventual counting asymptotic, and no lower bound beyond known examples is established. Historical priority is not independently certified: a similar argument could occur in broader literature on coincidences of multiplicative functions or in inaccessible source text.

## References

1. Tim Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615, first submitted December 17, 2013; especially Section 4 (conclusion and questions). https://arxiv.org/abs/1312.4615
2. OEIS Foundation, A236474, *Numbers whose sum of unitary divisors is equal to the sum of exponential divisors*. https://oeis.org/A236474
3. OEIS Foundation, A322446, *Counts for the strict unitary–exponential divisor-sum inequality*. https://oeis.org/A322446
4. G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, for standard smooth-number and prime-harmonic estimates. The only analytical estimate used here is the displayed elementary Rankin argument with the classical prime-harmonic upper bound.
