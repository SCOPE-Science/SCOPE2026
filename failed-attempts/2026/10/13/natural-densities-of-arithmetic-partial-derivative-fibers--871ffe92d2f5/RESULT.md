# Natural densities of arithmetic partial-derivative fibers

## Finding
Fix a prime \(p\). For each positive integer \(y\), let its arithmetic partial derivative be
\[
D_p(y)=\frac{y\nu_p(y)}{p},
\]
where \(\nu_p(y)\) is the exponent of \(p\) in \(y\). For \(x\ge1\), let \(i_p(x)=\#\{y\ge1:D_p(y)=x\}\). This number is finite. For each integer \(j\ge0\), the natural density
\[
\delta_{p,j}=\lim_{X\to\infty}\frac{\#\{1\le x\le X:i_p(x)=j\}}{X}
\]
exists, is strictly positive, and admits the exact, effectively approximable formula below. Moreover, \(\sum_{j\ge0}\delta_{p,j}=1\).

For each integer \(a\ge0\), define the finite divisor set
\[
\mathcal D_{p,a}=\left\{d\ge1:\ d=\frac{a+1-b}{p^b}\ \text{for some integer }0\le b\le a,\quad p\nmid d\right\},
\]
where membership requires the displayed quotient to be an integer, and put \(L_{p,a}=\operatorname{lcm}(\mathcal D_{p,a})\), taking \(L_{p,a}=1\) for an empty set. Then
\[
\boxed{\delta_{p,j}=\frac{p-1}{p}\sum_{a=0}^{\infty}\frac{1}{p^a L_{p,a}}
\#\left\{1\le r\le L_{p,a}:\ \sum_{d\in\mathcal D_{p,a}}\mathbf1_{d\mid r}=j\right\}.}
\]
For every prime \(p\), every \(j\ge0\), and every integer \(A\ge1\), truncation to \(0\le a<A\) has error between \(0\) and \(p^{-A}\).

In particular, the image of \(D_p\) on positive integers has natural density \(\delta_p=1-\delta_{p,0}\), with the more efficient exact formula
\[
\boxed{\delta_p=\frac{p-1}{p}\sum_{a=0}^{\infty}\frac{1}{p^a}
\sum_{\varnothing\ne S\subseteq\mathcal D_{p,a}}
\frac{(-1)^{|S|+1}}{\operatorname{lcm}(S)}.}
\]
The empty inner sum is zero. This density satisfies the uniform-in-primes estimate
\[
\boxed{\left|\delta_p+(p-1)\log\left(1-\frac1p\right)\right|\le p^{1-p}.}
\]
Consequently, along primes tending to infinity,
\[
\delta_p=1-\frac1{2p}-\frac1{6p^2}+O\left(p^{-3}\right).
\]
For example, exact rational truncations yield \(\delta_2\approx0.65096614189210\), \(\delta_3\approx0.80469100455430\), and \(\delta_5\approx0.89253153486599\).

## Assumptions and scope
All inputs and antiderivatives are **positive integers**, not rational, negative, or \(p\)-adic numbers; zero is excluded because it has infinitely many positive antiderivatives. The prime \(p\) is arbitrary and fixed when a density is taken. The variable \(X\) tends through real numbers to infinity. The argument uses ordinary natural density, not relative density within the image of another function. Each \(\mathcal D_{p,a}\) is finite because \(b\le a\) and \(a+1-b\) must be positive. Its members are coprime to \(p\), hence so is \(L_{p,a}\). As usual \(\mathbf1\) denotes an indicator and \(\nu_p\) a prime-adic valuation.

## Proof
**1. Complete inverse parameterization.** If \(D_p(y)=x>0\), then \(y=t p^k\) for unique \(k\ge1\) and \(p\nmid t\), and \(x=t k p^{k-1}\). Factor \(k=d p^b\) with \(p\nmid d\). Writing \(x=p^a m\), \(p\nmid m\), gives the two exact equations
\[
a+1=d p^b+b,\qquad m=td.
\]
Thus \(d\in\mathcal D_{p,a}\) and \(d\mid m\). Conversely each such divisor \(d\mid m\) specifies \(b\) and then the positive antiderivative \(y=(m/d)p^{d p^b}\). For a fixed \(d\), the function \(b\mapsto d p^b+b\) is strictly increasing, so no two values of \(b\) yield the same divisor \(d\). Hence this correspondence is bijective and
\[
\boxed{i_p(p^a m)=\sum_{d\in\mathcal D_{p,a}}\mathbf1_{d\mid m},\qquad p\nmid m.}
\]
The form agrees with the earlier inverse criterion of Emmons--Xiao but is rederived here to establish exact multiplicities.

**2. Local periodicity and density.** Fix \(a\ge0\). The right side is periodic in \(m\) modulo \(L_{p,a}\). Since \(p\nmid L_{p,a}\), the Chinese remainder theorem says that among positive integers \(m\) with \(p\nmid m\), residues modulo \(L_{p,a}\) are equidistributed. For a fixed residue \(r\bmod L_{p,a}\), the integers \(x=p^a m\le X\) with \(p\nmid m\) and \(m\equiv r\pmod{L_{p,a}}\) have density \((p-1)/(p^{a+1}L_{p,a})\). Summing these disjoint residue classes proves the displayed summand for \(\delta_{p,j}\).

There is no unjustified limit interchange. For any \(A\ge1\), the as-yet-unaccounted integers have \(\nu_p(x)\ge A\) and lie among multiples of \(p^A\), a set of density \(p^{-A}\). Its upper density also does not exceed \(p^{-A}\). Letting \(A\to\infty\) proves existence of each density, the claimed truncation error, and \(\sum_{j\ge0}\delta_{p,j}=1\) by summing the nonnegative local distributions.

**3. Image density.** Membership \(x=p^a m\in\operatorname{im}(D_p)\) means that at least one \(d\in\mathcal D_{p,a}\) divides \(m\). Uniformity of residues modulo \(L_{p,a}\) and inclusion--exclusion give its conditional proportion as
\[
\rho_{p,a}=\sum_{\varnothing\ne S\subseteq\mathcal D_{p,a}}
\frac{(-1)^{|S|+1}}{\operatorname{lcm}(S)}.
\]
Since \(0\le\rho_{p,a}\le1\), the weighted series converges absolutely; the same valuation tail proves its exact formula and error certificate.

**4. Uniform prime asymptotic.** For every \(0\le a\le p-2\), necessarily \(b=0\) in the divisor-set definition: if \(b\ge1\), the positive integer \(a+1-b\) is smaller than \(p\) and cannot be divisible by \(p^b\). Thus \(\mathcal D_{p,a}=\{a+1\}\) and \(\rho_{p,a}=1/(a+1)\). The comparison series is
\[
\frac{p-1}{p}\sum_{a\ge0}\frac1{(a+1)p^a}
=-(p-1)\log(1-p^{-1}).
\]
The actual and comparison local probabilities lie in \([0,1]\) and agree for every \(a<p-1\). Their weighted tails have total mass
\[
\frac{p-1}{p}\sum_{a=p-1}^{\infty}p^{-a}=p^{1-p},
\]
proving the uniform absolute error. Taylor expansion of the logarithm proves the stated two-term density asymptotic.

**5. Positivity of every multiplicity.** When \(a=p-1\), the divisor set is empty: at \(b=0\), the only prospective \(d\) is \(p\), while for \(b\ge1\) the positive numerator is smaller than \(p\). Thus every positive integer with exact \(p\)-adic valuation \(p-1\) has \(i_p(x)=0\), and \(\delta_{p,0}>0\). For each \(j\ge1\), Emmons--Xiao, Theorem 21, constructs a positive integer \(x_0=p^a m_0\) with \(i_p(x_0)=j\). All \(m\equiv m_0\pmod{L_{p,a}}\) with \(p\nmid m\) give the same value of \(i_p(p^a m)\), by Step 1, and occupy the strictly positive density \((p-1)/(p^{a+1}L_{p,a})\). Therefore every \(\delta_{p,j}\) is positive. This last assertion uses the published existence theorem; all density formulas and the asymptotic are proved independently above.

## Verification
The standalone standard-library script `verify.py` computes \(\mathcal D_{p,a}\), the exact rational inclusion--exclusion sums, and certified intervals with tail \(p^{-A}\). It independently enumerates all possible positive antiderivatives for every output up to \(60{,}000\) for \(p\in\{2,3,5\}\), using the rigorous preimage bound \(y\le p x\), and compares each image membership with the inverse divisor formula. It compares inverse multiplicities independently for \(a\le29\), \(m\le300\), and checks residue-distribution counts against inclusion--exclusion. The full actual program output appears in `verification_output.txt`; `VERIFICATION.md` records scope and limitations. These finite regressions are not substituted for Steps 1--5.

## Relationship to prior work
Emmons and Xiao, *The Arithmetic Partial Derivative* (arXiv:2201.12453, first posted January 28, 2022; Journal of Integer Sequences 25 (2022), Article 22.4.7), formulate the exact anti-partial derivative criterion (Lemma 14), an explicit inverse-count framework (Theorem 17), and construct infinitely many outputs having any prescribed positive finite number of antiderivatives (Theorem 21). The present theorem retains those antecedents but answers a different **frequency** question: the density of every fiber and of the whole image, with computable constants and an exponentially accurate prime-parameter asymptotic. In particular, infinitely many witnesses alone give no positive-density assertion without the periodicity argument and its counting justification.

Emmons and Xiao's 2023 follow-up on \(p\)-adic and number-field extensions develops derivative dynamics in other ambient rings. Kovič (2012) and Haukkanen--Merikoski--Tossavainen (2016) study arithmetic derivative equations; Pandey--Saxena (2017) studies related conjectures. None of the sections materially checked stated the density-distribution or prime-asymptotic theorem. Absence from searched literature cannot establish exhaustive bibliographic uniqueness.

## Limitations
The proof gives convergent series and rigorously bounded rational intervals, not an elementary closed form for each \(\delta_{p,j}\) or \(\delta_p\). The displayed decimals are approximations; certified values come from rational truncation and the explicit tail bound. No statistical independence of distinct divisor events is assumed: the exact least-common-multiple inclusion--exclusion is essential. No assertion is made about the density of the full (unrestricted, all-primes) arithmetic derivative's image, about rational anti-partial derivatives, or about negative inputs. The existence of every positive multiplicity rests on the cited published Theorem 21, not an independent classification supplied here. Bibliographic coverage is necessarily limited to checked sources.

## References
1. B. Emmons and X. Xiao, *The Arithmetic Partial Derivative*, arXiv:2201.12453 (first public preprint January 28, 2022); *Journal of Integer Sequences* **25** (2022), Article 22.4.7. https://arxiv.org/abs/2201.12453 ; https://cs.uwaterloo.ca/journals/JIS/VOL25/Xiao/xiao3.pdf . Primary MSC 11A25 as printed on page 14.
2. B. Emmons and X. Xiao, *A Generalization of Arithmetic Derivative to p-adic Fields and Number Fields*, arXiv:2307.04912 (2023); *Notes on Number Theory and Discrete Mathematics* **30** (2024), 357--382. https://arxiv.org/abs/2307.04912 .
3. J. Kovič, *The Arithmetic Derivative and Antiderivative*, *Journal of Integer Sequences* **15** (2012), Article 12.3.8. https://cs.uwaterloo.ca/journals/JIS/VOL15/Kovic/kovic4.html .
4. P. Haukkanen, J. K. Merikoski, and T. Tossavainen, *On Arithmetic Partial Differential Equations*, *Journal of Integer Sequences* **19** (2016), Article 16.8.6.
5. R. K. Pandey and R. Saxena, *On Some Conjectures about Arithmetic Partial Differential Equations*, *Journal of Integer Sequences* **20** (2017), Article 17.5.2.
