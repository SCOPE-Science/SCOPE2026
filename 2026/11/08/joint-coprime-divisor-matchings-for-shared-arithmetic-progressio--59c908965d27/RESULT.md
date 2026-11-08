# Joint coprime divisor matchings for shared arithmetic progressions

## Finding
Fix an integer \(k\ge 2\) and a tuple \(\mathbf n=(n_1,\ldots,n_k)\) of positive integers. Let \(D(n)\) be the positive divisors of \(n\), and put \(N_i=\tau(n_i)\). For positive integers \(a,b\) with \(\gcd(a,b)=1\), let \(\mathcal P_i(a,b)=\{a+bt:0\le t<N_i\}\). The pair \((a,b)\) is *simultaneously admissible* when every \(D(n_i)\) has a bijection to \(\mathcal P_i(a,b)\) pairing relatively prime integers; the bijections may differ between the indices.

For any prime \(p\), define \(e_{i,p}=\nu_p(n_i)\) and
\[
 h_{i,p}=\max\{0,e_{i,p}+1-p\}\,\tau(n_i/p^{e_{i,p}}),\qquad
 \lambda_p(\mathbf n)=\max_{1\le i\le k}\min\{p,h_{i,p}\}.
\]
Only primes dividing \(n_1\cdots n_k\) contribute nonzero \(\lambda_p\). Then the following **exact joint asymptotic** holds, for real \(X\ge2\):
\[
 \#\{(a,b)\in[1,X]^2\cap\mathbb Z^2:\gcd(a,b)=1,\ (a,b)\text{ simultaneously admissible}\}
 =\frac6{\pi^2}\Delta_k(\mathbf n)X^2+O_{\mathbf n}(X\log(2X)),
\]
where
\[
 \boxed{\displaystyle\Delta_k(\mathbf n)=\prod_{p\mid n_1\cdots n_k}
 \left(1-\frac{\lambda_p(\mathbf n)}{p+1}\right).}
\]
In particular, simultaneous constraints at a fixed prime combine by the **maximum** of their local obstructions, not by multiplication of the individual success densities. For example, \(\Delta_2(4,8)=1/3\), whereas the two separate success densities are \(2/3\) and \(1/3\); also \(\Delta_2(27,81)=1/2\).

Let \(J_k\) be the limit, as \(Y\to\infty\), of the mean of \(\Delta_k(n_1,\ldots,n_k)\) over \(1\le n_1,\ldots,n_k\le Y\). For every fixed integer \(k\ge1\), this limit exists and equals
\[
 \boxed{\displaystyle J_k=\prod_{p\ \mathrm{prime}}\frac{1+p(1-p^{-p})^k}{p+1}.}
\]
For \(k=1\), this is the already natural single-input marginal; the **joint law** and its interactions are the new object here. There is strict positive pair correlation:
\[
 \boxed{J_2>J_1^2.}
\]
Numerically, truncation to primes below \(60\) gives \(J_1\approx0.809968275222\), \(J_2\approx0.669351675488\), and \(J_2-J_1^2\approx0.013303068622\). These are finite-product approximations, not formally certified decimal intervals.

## Assumptions and scope
All integers \(n_i\), \(a\), \(b\), and \(k\) are positive. The fixed-tuple asymptotic is for \(X\to\infty\), with an error constant depending on the tuple; the mean limit over tuples is taken after the primitive-pair density is formed. No uniform error for growing tuple size or inputs is claimed. The case \(n_i=1\) is allowed and supplies no local obstruction.

## Proof
**1. The published matching criterion.** Alekseyev and Beyer de Ryke, Theorem 1.1 of [1], prove for each \(n\) and each progression \(\{a+bt:0\le t<\tau(n)\}\) that a coprime matching to \(D(n)\) exists exactly when, for each \(p\mid n\), the number of progression terms divisible by \(p\) is at most \(\tau(n)/(\nu_p(n)+1)\). We use this theorem as a stated prior result; we do not claim a new proof of it.

**2. A maximum rule for shared progressions.** Fix a prime \(p\) and write \(e=e_{i,p}\), \(T=\tau(n_i/p^e)\), and \(N_i=(e+1)T\). If \(e<p\), then \(N_i\le pT\); because an arithmetic progression with \(p\nmid b\) hits a multiple of \(p\) at most \(T\) times among its first \(pT\) terms, the criterion holds automatically. If \(p\mid b\), primitiveness forces \(p\nmid a\), and there are no divisible terms, whatever \(e\).

If \(e\ge p\), write \(N_i=pT+h\) with \(h=(e+1-p)T>0\). For \(p\nmid b\), the progression visits every residue \(p\) exactly \(T\) times in the first \(pT\) positions. Its extra \(h\) positions hit the zero residue if and only if the unique index \(t_0\equiv-a b^{-1}\pmod p\) belongs to the initial \(h\) indices modulo \(p\). When \(h\ge p\), every such progression has too many multiples of \(p\). When \(1\le h<p\), the forbidden values of \(t_0\) are exactly \(\{0,1,\ldots,h-1\}\). For all \(i\) simultaneously, these forbidden sets are nested, so their union has size \(\lambda_p(\mathbf n)\) (or all \(p\) residues if an index has \(h\ge p\)).

Among the \(p^2-1\) pairs \((a,b)\bmod p\) not both zero, there are \(p-1\) acceptable pairs with \(b=0\). Of the pairs with \(b\ne0\), precisely \((p-1)(p-\lambda_p)\) are acceptable. Therefore their fraction is \((p+1-\lambda_p)/(p+1)\). This also proves strict positivity of every factor.

**3. Counting primitive pairs.** Let \(L\) be the squarefree product of primes dividing \(\prod_i n_i\). The Chinese remainder theorem makes the local restrictions independent on the primitive residue-pairs modulo \(L\). Möbius inversion for \(\gcd(a,b)=1\), followed by counting classes modulo the fixed integer \(L\), gives the usual density \(6/\pi^2\), multiplied by the fractions from Step 2, and the error \(O_{\mathbf n}(X\log(2X))\). This proves the first formula.

**4. Typical inputs.** A tuple is *regular* if, for each \(i\) and prime \(p\) with \(e_{i,p}\ge p\), one has \(h_{i,p}\ge p\). Equivalently, no exceptional obstruction lies strictly between \(0\) and \(p\). For each fixed \(p\), an integer \(n=p^e m\) with \(p\nmid m\) and \(0<h=(e+1-p)\tau(m)<p\) has \(\tau(m)<p\); hence \(\omega(m)\) is bounded. Integers with at most a fixed number of distinct prime factors have density zero. One elementary proof restricts to the first \(H\) primes and applies the Chinese remainder theorem: the count of dividing primes has mean \(\sum_{p\le H}1/p\to\infty\) and variance at most its mean, so Chebyshev's inequality bounds the probability of a fixed small count by a quantity tending to zero. For each fixed \(p\), truncate \(e\) and use the geometric bound \(p^{-E}\) on the discarded exponents. Finally, integers with \(p^p\mid n\) for some \(p>P\) have upper density at most \(\sum_{p>P}p^{-p}\to0\). Thus nonregular integers have density zero, and for every fixed \(k\) nonregular tuples have zero limiting proportion.

For regular inputs, each \(\lambda_p\) is either \(0\) or \(p\), with the latter precisely when \(p^p\) divides at least one of the \(n_i\). Consequently
\[
 \Delta_k(\mathbf n)=\prod_{p:\,\exists i\ p^p\mid n_i}\frac1{p+1}
 \quad\text{for regular tuples.}
\]
For each finite set of primes, uniform independent choices of the \(n_i\) have, by the Chinese remainder theorem, probability \((1-p^{-p})^k\) that no \(p^p\) divides any input. Averaging the displayed product therefore gives the local mean factor
\[
 (1-p^{-p})^k+\frac{1-(1-p^{-p})^k}{p+1}
 =\frac{1+p(1-p^{-p})^k}{p+1}.
\]
The tail is uniformly controlled by \(k\sum_{p>P}p^{-p}\). Letting the prime cutoff grow establishes the convergent Euler product for \(J_k\).

**5. Strict correlation.** Put \(t=p^{-p}\) and \(A_p=[1+p(1-t)]/(p+1)\), \(B_p=[1+p(1-t)^2]/(p+1)\). A direct calculation gives
\[
 B_p-A_p^2=\frac{p\,t^2}{(p+1)^2}>0.
\]
All factors are positive and both Euler products converge to positive values. In particular, the \(p=2\) factor already makes the full product inequality strict, giving \(J_2>J_1^2\).

## Verification
Run `python3 joint_verify.py` (Python standard library only). It compares the closed rational formula with direct enumeration of admissible pairs modulo the product of relevant primes for \(19\) tuples. It also independently constructs perfect matchings using an augmenting-path search and checks \(6860\) pairs of inputs and primitive progression parameters. It reports finite Euler-product truncations for \(k=1,2,3,4\) and checks strict positivity of the displayed covariance. Direct finite calculations do not establish the infinite mean, the density-zero exceptional set, or the primitive-pair counting asymptotic; those are proved above.

## Relationship to prior work
Alekseyev and Beyer de Ryke [1] prove the essential single-divisor-set matching criterion, characterize when *every* primitive progression works, and determine when a fixed common difference works for every primitive start. McNew and Pomerance [2] study matching to an initial interval and the density of matchable integers. Those facts are credited, not re-presented as new. The single-input primitive-progression success density is also obtainable from [1] by residue counting; the present result instead determines the **nonmultiplicative joint dependence** of several divisor sets on the *same* parameters \((a,b)\), together with all finite-order mean joint probabilities and the strict pair-correlation formula. The example \((n_1,n_2)=(4,8)\) shows why independent multiplication of single-input densities fails.

## Limitations
The result invokes [1, Theorem 1.1] as a premise rather than reproving its deep matching sufficiency. The numerical Euler products are diagnostic approximations without rigorous decimal bounds. The mean law is an iterated limit with \(k\) fixed; no uniform bound in growing \(k\) or a rate as input cutoffs grow is established. No claim of absolute historical priority is made. Earlier indexed arithmetic literature may contain equivalent simultaneous-sieve or matching-density formulations; an independent literature audit is advisable.

## References
[1] Max A. Alekseyev and Basile Beyer de Ryke, *Coprime matchings of divisor sets*, arXiv:2610.37512 (first public version October 27, 2026), Theorems 1.1 and 1.2; Corollary 4.2; Sections 4–6. https://arxiv.org/abs/2610.37512.

[2] Nathan McNew and Carl Pomerance, *Matchable numbers*, arXiv:2604.05304 (first public version April 7, 2026), introduction, Proposition 1 and density results. https://arxiv.org/abs/2604.05304.
