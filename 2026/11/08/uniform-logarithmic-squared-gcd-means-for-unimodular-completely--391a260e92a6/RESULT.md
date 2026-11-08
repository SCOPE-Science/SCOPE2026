# Uniform logarithmic-squared GCD means for unimodular completely multiplicative weights

## Finding
For every completely multiplicative function \(a:\mathbb N\to\mathbb C\) satisfying \(|a(n)|=1\) for all positive integers, set
\[
T_a(N)=\sum_{1\le m,n\le N}\frac{a(m)\overline{a(n)}\gcd(m,n)^2}{mn},\qquad
S_a(q)=\sum_{k=1}^{q}\frac{a(k)}k.
\]
Then **uniformly over all such functions \(a\)** and integers \(N\ge1\),
\[
\boxed{T_a(N)=c(a)N+O\bigl(\log^2(2N)\bigr),\qquad
c(a)=\frac1{\zeta(3)}\sum_{q=1}^{\infty}\frac{|S_a(q)|^2}{q(q+1)}.}
\]
The series is absolutely convergent, and the sharp global upper bound and a universal positive lower bound are
\[
\boxed{\frac1{2\zeta(3)}\le c(a)\le3,\qquad c(a)=3\iff a(n)=1\text{ for every }n.}
\]
In particular, the theorem applies to the completely multiplicative Liouville sign function \(\lambda(n)=(-1)^{\Omega(n)}\), arbitrary sign choices at primes, and complex phase choices such as \(a(n)=n^{it}\) for real \(t\). The Möbius function is not completely multiplicative and is **not** included in this theorem.

## Assumptions and scope
Here \(\mathbb N=\{1,2,\ldots\}\), \(a(mn)=a(m)a(n)\) for all \(m,n\), and \(|a(n)|=1\). The condition forces \(a(1)=1\). The quadratic form is Hermitian, so \(T_a(N)\) and \(c(a)\) are real. The implied constant in the remainder is absolute and **independent** of \(a\); the claim includes all integers \(N\ge1\), without an unproved limiting or randomness assumption.

The exponent \(2\) on the logarithm is an upper bound. No claim that this is the optimal exponent for every fixed \(a\) is made.

## Proof
**1. Jordan decomposition and multiplicativity.** Let \(J_2(d)=d^2\prod_{p\mid d}(1-p^{-2})\). The classical identity \(\gcd(m,n)^2=\sum_{d\mid m,n}J_2(d)\) and complete multiplicativity give
\[
T_a(N)=\sum_{d\le N}\frac{J_2(d)}{d^2}
\left|\sum_{k\le N/d}\frac{a(dk)}k\right|^2
=\sum_{d\le N}f(d)|S_a(\lfloor N/d\rfloor)|^2,
\]
where \(f(d)=J_2(d)/d^2=\prod_{p\mid d}(1-p^{-2})=\sum_{e\mid d}\mu(e)/e^2\). The last formula is the finite divisor expansion of the Euler product, not a heuristic mean-value estimate. Hence, on writing \(d=ej\),
\[
T_a(N)=\sum_{e\le N}\frac{\mu(e)}{e^2}F_a(N/e),\qquad
F_a(x)=\sum_{1\le j\le x}|S_a(\lfloor x/j\rfloor)|^2.
\]

**2. A uniform floor-sum estimate.** Expanding the squares in this finite sum and interchanging the finite indices yields the exact identity, for real \(x\ge1\),
\[
F_a(x)=\sum_{1\le k,l\le x}\frac{a(k)\overline{a(l)}}{kl}
\left\lfloor\frac{x}{\max(k,l)}\right\rfloor.
\]
Define the absolutely convergent real series
\[
B(a)=\sum_{k,l\ge1}\frac{a(k)\overline{a(l)}}{kl\max(k,l)}.
\]
Absolute convergence follows since the total majorant at \(\max(k,l)=r\) is at most \(2H_r/r^2\), with \(H_r=\sum_{j\le r}1/j\), and \(\sum_r H_r/r^2<\infty\). Replacing the floor by its argument on the finite square incurs absolute error at most \(H_{\lfloor x\rfloor}^2\). Inserting the omitted pairs incurs error bounded by
\[
2x\sum_{r>x}\frac{H_r}{r^2}=O(1+\log x).
\]
Thus, independently of the phases of \(a\),
\[
\boxed{F_a(x)=xB(a)+O(\log^2(2x))}\qquad(x\ge1).
\]

**3. Summing the Möbius divisor expansion.** Substitution gives
\[
T_a(N)=NB(a)\sum_{e\le N}\frac{\mu(e)}{e^3}
+O\left(\sum_{e\le N}\frac{\log^2(2N/e)}{e^2}\right).
\]
The error is \(O(\log^2(2N))\). Absolute convergence of the Dirichlet series gives \(\sum_{e\ge1}\mu(e)/e^3=1/\zeta(3)\), and the omitted tail changes the leading term by at most \(O(N^{-1})\). Therefore \(T_a(N)=NB(a)/\zeta(3)+O(\log^2(2N))\).

**4. The positive constant and the sharp maximum.** The elementary telescoping identity \(\sum_{q\ge\max(k,l)}1/[q(q+1)]=1/\max(k,l)\) gives
\[
B(a)=\sum_{q\ge1}\frac{|S_a(q)|^2}{q(q+1)}.
\]
All terms are nonnegative, and \(S_a(1)=1\); hence \(B(a)\ge1/2\). By the triangle inequality, \(|S_a(q)|\le H_q\), so \(B(a)\le B(\boldsymbol1)\), where \(\boldsymbol1(n)=1\). Separating terms by \(r=\max(k,l)\) gives
\[
B(\boldsymbol1)=2\sum_{r\ge1}\frac{H_r}{r^2}-\zeta(3)=3\zeta(3).
\]
For completeness, the Euler sum used here is
\[
\sum_{r\ge1}\frac{H_r}{r^2}
=\int_0^1\frac{\log^2(1-x)}x\,dx
=\int_0^1\frac{\log^2 t}{1-t}\,dt=2\zeta(3),
\]
where the first equality follows by inserting \(H_r=\int_0^1(1-x^r)/(1-x)\,dx\), exchanging nonnegative sums, and integrating by parts; the last follows by the geometric series and elementary logarithmic moments. Therefore \(c(a)\le3\), with equality for \(a\equiv1\).

If equality holds, every nonnegative term \(H_q^2-|S_a(q)|^2\) must vanish. Since \(a(1)=1\), equality in the triangle inequality for \(S_a(q)\) forces \(a(1),\ldots,a(q)\) all to have phase \(1\). Every positive integer is therefore assigned \(1\), establishing uniqueness.

## Verification
The accompanying standalone `verify.py` computes the original double sum, the Jordan-square decomposition, and the Möbius-convolution expression using rational arithmetic for three nontrivial completely multiplicative sign choices and nine cutoff values through \(24\). Additional numerical checks test a complex fourth-root-of-unity weight at cutoffs \(3,6,9,14\) and evaluate truncated positive constants. The checks and their observed outputs are in `check_output.txt` and `VERIFICATION.md`. These are finite corroborations; all infinite assertions follow from the proof above.

## Relationship to prior work
Azimifard, *A power-saving asymptotic for a Möbius-weighted GCD quadratic form* (2026, arXiv:2611.00525v1), proves an \(N^{2/3+\varepsilon}\) remainder for the **specific Möbius vector**. Its Jordan decomposition is a classical common tool, but \(\mu\) is not completely multiplicative: the source requires squarefree and coprimality corrections. The present theorem treats a different, broad unimodular completely multiplicative family (including Liouville) with a logarithmic-squared uniform remainder and exact extremal constant. It does **not** purport to improve the cited Möbius result.

Lindqvist–Seip (1998) and Aistleitner–Berkes–Seip–Weber (2015) study GCD matrices and spectral/functional-analytic questions. Ehm (2024) develops different Gram kernels in a Nyman–Beurling context. These are structural background, not claimed as discoveries here. Source accessibility and possible previously unindexed formulations remain priority risks.

## Limitations
No assertion is made for weights with zeros or non-unit modulus, including the Möbius function. No sharp remainder lower bound is claimed for a fixed nonconstant weight. The theorem concerns a fixed GCD-square kernel on consecutive integer indices; it is not an estimate for the largest eigenvalue of arbitrary GCD matrices. Exhaustive identification of all historically equivalent but differently formulated results is not established. The verification programs are finite checks, not independent mathematical certification.

## References
1. A. Azimifard, *A power-saving asymptotic for a Möbius-weighted GCD quadratic form*, arXiv:2611.00525v1, first posted 2026-10-31, https://arxiv.org/html/2611.00525v1.
2. P. Lindqvist and K. Seip, *Note on some greatest common divisor matrices*, Acta Arith. 84 (1998), 149–154, DOI:10.4064/aa-84-2-149-154.
3. C. Aistleitner, I. Berkes, K. Seip, and M. Weber, *Convergence of series of dilated functions and spectral norms of GCD matrices*, Acta Arith. 168 (2015), 221–246, arXiv:1407.5403.
4. W. Ehm, *On certain Gram matrices and their associated series*, arXiv:2405.06349v2 (2024).
