# Exact fibbinary additive energy and the golden-mean convolution dimension

## Finding
For each integer \(r\ge 0\), let
\[
A_r=\left\{0\le n<2^r:\binom{3n}{n}\text{ is odd}\right\},
\qquad
E_r=\#\{(a,b,c,d)\in A_r^4:a+b=c+d\},
\]
where quadruples are ordered and all sums are ordinary integer sums. Then
\[
\boxed{\sum_{r\ge0}E_rz^r=
\frac{1+4z+z^2-4z^3+2z^4}
{1-2z-6z^2+z^3+4z^4-2z^5}.}
\]
In particular \(E_0,E_1,E_2,E_3,E_4=(1,6,19,69,244)\), and for every integer \(r\ge5\),
\[
E_r=2E_{r-1}+6E_{r-2}-E_{r-3}-4E_{r-4}+2E_{r-5}.
\]
Let \(\varphi=(1+\sqrt5)/2\) and let \(\lambda\) be the unique root of
\[
P(t)=t^5-2t^4-6t^3+t^2+4t-2
\]
in \((7/2,18/5)\). Thus \(\lambda=3.5383124471\ldots\). We have \(E_r\sim C\lambda^r\) for some strictly positive \(C\).

The discrete probability measures
\[
\mu_r=\frac1{|A_r|}\sum_{n\in A_r}\delta_{n/2^r}
\]
converge weakly to a probability measure \(\mu\) supported on the usual additive golden-mean binary Cantor set. For \(\nu=\mu*\mu\), the dyadic-grid correlation dimension exists and equals
\[
\boxed{D_2(\nu)=\frac{4\log\varphi-\log\lambda}{\log2}
=0.9539062051\ldots<1.}
\]
Consequently, \(\nu\) has no density in \(L^2(\mathbb R)\). This does not imply that \(\nu\) is singular with respect to Lebesgue measure.

## Assumptions and scope
The range of the finite theorem is every integer \(r\ge0\); the infinite-limit theorem concerns the particular weak limit \(\mu\) defined above, not arbitrary measures on the same support. A binary word is admissible when no two consecutive digits are both one, including leading zeroes. Its numerical value is interpreted in base two. The grid dimension means
\[
D_2(\nu)=\lim_{r\to\infty}-\frac{\log\left(\sum_{k\in\mathbb Z}
\nu([k2^{-r},(k+1)2^{-r}))^2\right)}{r\log2}.
\]
The same exponent holds for the usual pair-distance correlation dimension by fixed-neighbor comparisons of dyadic cells. No claim about \(L^p\) densities for \(p<2\), Fourier decay, or more general forbidden-word languages is made.

## Proof
**1. Binomial parity and the finite language.** Kummer's carry theorem gives
\(\nu_2\left(\binom{3n}{n}\right)\) as the number of carries in the binary addition \(n+2n\). The two summands have adjacent bit patterns. Thus no carry occurs if and only if \(n\) has no adjacent one-bits, or equivalently \(n\mathbin{\&}(2n)=0\). It follows that \(A_r\) is precisely the length-\(r\) golden-mean binary language, and \(|A_r|=F_{r+2}\), using \(F_0=0,F_1=1\).

**2. A twelve-state exact carry transfer.** Read the binary digits of an ordered quadruple \((a,b,c,d)\) from least to most significant. The transfer state is \((m,e)\), where \(m\in\{0,\ldots,15\}\) is the four-bit mask of previously read digits, and \(e\in\{-1,0,1\}\) is the signed incoming carry for \(a+b-c-d\). The initial state is \((0,0)\). From \((m,e)\), a next four-bit mask \(x\) is admissible if \(x\mathbin{\&}m=0\). Write its bits as \(x_a,x_b,x_c,x_d\) (positions zero through three). An edge goes to
\[
\left(x,\frac{x_a+x_b-x_c-x_d+e}{2}\right)
\]
when the displayed quotient is an integer belonging to \(\{-1,0,1\}\). All edges have weight one, and repeated edges are counted with multiplicity. Iterating from \((0,0)\) yields exactly these twelve reachable states, in lexicographic order:
\[
(0,0),(1,0),(2,0),(3,1),(4,0),(5,0),(6,0),
(8,0),(9,0),(10,0),(12,-1),(15,0).
\]
Let \(M\) be their \(12\times12\) edge-multiplicity matrix. Let \(u\) be the row selecting \((0,0)\), and let \(v\) be the column with entry one for terminal carry zero, and zero otherwise. The carry equation is equivalent to the equality of the two ordinary sums after all \(r\) digits precisely when the final carry vanishes. Therefore, for every \(r\ge0\),
\[
E_r=uM^rv.
\]

The following **exact finite integer identities** hold for the stated explicit matrix; `CHECK.py` reconstructs and checks them from the digit rule:
\[
\begin{aligned}
&(M^5-2M^4-6M^3+M^2+4M-2I)v=0,\\
&\det(tI-M)=t^2(t-1)(t+1)^2(t^2-2)P(t).
\end{aligned}
\]
The first identity proves the order-five recurrence for every depth without extrapolation. Direct multiplication gives \((E_0,\ldots,E_4)=(1,6,19,69,244)\); multiplying by the denominator of the recurrence gives the displayed rational generating function. The twelve-state directed graph is strongly connected and has a self-loop, so \(M\) is primitive. Perron--Frobenius therefore gives \(E_r\sim C\rho(M)^r\) with \(C>0\). The characteristic factorization, the strict positivity of \(P'(t)\) for \(t\ge7/2\), and \(P(7/2)=-253/32<0<P(18/5)=44258/3125\) identify \(\rho(M)=\lambda\).

**3. Exact cylinder weights for the limiting measure.** For every \(r\ge1\), an admissible prefix of \(r\) bits has \(F_{L+2}\) admissible completions of length \(L\) when it ends in zero, and \(F_{L+1}\) when it ends in one. Dividing by \(F_{r+L+2}\) and taking \(L\to\infty\) shows that the weak limit exists, and that the probability of any admissible \(r\)-bit prefix is exactly
\[
p_r(w)=\begin{cases}\varphi^{-r},&\text{last digit zero},\\
\varphi^{-r-1},&\text{last digit one}.
\end{cases}
\]
In particular \(\varphi^{-r-1}\le p_r(w)\le\varphi^{-r}\). This is a Markov measure with transition probabilities \(0\to0\) equal to \(\varphi^{-1}\), \(0\to1\) equal to \(\varphi^{-2}\), and \(1\to0\) equal to one. Its digits cannot contain adjacent ones. Therefore its support is contained in \([0,2/3]\), and the sum of two independent conditional tails after any prescribed \(r\)-bit prefixes is less than two.

**4. Correlation dimension from the exact energy.** Let \(w_{r,s}\) be the probability that the integer values of the first \(r\) digits of two independent \(\mu\)-distributed numbers sum to \(s\). Let \(R_r(s)=\#\{(a,b)\in A_r^2:a+b=s\}\). The cylinder bounds imply
\[
\varphi^{-2r-2}R_r(s)\le w_{r,s}\le\varphi^{-2r}R_r(s).
\]
Consequently
\[
\varphi^{-4r-4}E_r\le\sum_sw_{r,s}^2\le\varphi^{-4r}E_r.
\]
After multiplying the continuous sum by \(2^r\), the two conditional tails shift a given integer prefix sum \(s\) into grid cell \(s\) or \(s+1\), never any other cell. Split \(w_{r,s}=w_{r,s}^{(0)}+w_{r,s}^{(1)}\) according to those two outcomes. The actual grid-cell mass is \(v_{r,k}=w_{r,k}^{(0)}+w_{r,k-1}^{(1)}\). Nonnegativity and the inequality \((a+b)^2\le2(a^2+b^2)\) give
\[
\frac14\sum_sw_{r,s}^2\le\sum_kv_{r,k}^2
\le2\sum_sw_{r,s}^2.
\]
Therefore the dyadic mass-squared sums lie between positive constants times \(E_r\varphi^{-4r}\). The positive Perron asymptotic yields the stated exact value of \(D_2(\nu)\). Because \(\varphi^4/2=(7+3\sqrt5)/4<7/2<\lambda\), this dimension is strictly below one.

**5. Failure of a square-integrable density.** If \(\nu=f(x)\,dx\) with \(f\in L^2(\mathbb R)\), applying Cauchy--Schwarz on each dyadic interval would force \(2^r\sum_kv_{r,k}^2\le\|f\|_2^2\) at every depth. But the preceding lower bound grows at least as a positive constant times \((2\lambda/\varphi^4)^r\), whose base exceeds one. This is impossible. The usual radius-based correlation exponent equals the grid exponent because pairs with distance less than a dyadic cell length occupy the same or adjacent cells; conversely pairs in one cell have distance less than that length. Cauchy--Schwarz compares the two quantities up to absolute factors.

## Verification
Run `python3 CHECK.py` with Python's standard library. It independently builds the reachable carry graph, checks the exact characteristic polynomial and annihilating identity, checks the depth recurrence through depth 47, directly enumerates all additive quadruples through depth 11 using two-sum histograms, and verifies Kummer parity for the first 257 indices. The execution returned `CHECK_OK` with 353 exact assertions. The universal statements rely on the displayed matrix and analytic arguments, not on the finite enumerations.

## Relationship to prior work
Kummer's carry theorem gives the binomial parity characterization, and Kenyon--Peres--Solomyak discuss the ordinary additive golden-mean subshift and its support dimension in the introduction of their 2011 paper. Their theorem concerns the *multiplicative* golden-mean shift, characterized by digit constraints at positions \(k\) and \(2k\), rather than ordinary four-point additive energy of the adjacent-digit language. An existing exact dyadic valuation law for \(\binom{3n}{n}\) determines the Fibonacci cardinality of its odd-index set, not its integer two-sum collision counts. Other exact studies count three-term progressions in that same set, a distinct equation with no determination of all additive quadruples. Existing two-sum-energy evaluations for odd Pascal-row supports and for an independent-digit four-adic measure concern different supports; neither supplies the twelve-state binary forbidden-adjacency calculation. General finite-type and transfer-matrix methods can frame such questions, but the specific rational energy identity and corresponding limiting convolution dimension are not consequences of the explicit statements inspected. The method itself is not claimed as new.

## Limitations
The result is for parity of the proportional binomial family \(\binom{3n}{n}\), the initial dyadic cutoffs, and the particular limiting maximal-entropy golden-mean measure. It neither determines all additive representation multiplicities nor establishes absolute continuity or singularity of the convolution. Unindexed prior calculations of the same additive energy, or evaluations implicit in general Markov-convolution literature, remain an originality risk.

## References
1. E. Kummer, classical theorem identifying binomial valuations with carries (1852), summarized at https://en.wikipedia.org/wiki/Kummer%27s_theorem.
2. R. Kenyon, Y. Peres, B. Solomyak, *Hausdorff dimension of the multiplicative golden mean shift*, arXiv:1105.3441, first public version 2011-05-17; specifically the usual adjacent-digit golden-mean shift in the introduction. https://arxiv.org/abs/1105.3441.
3. L. Spiegelhofer, M. Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089, first version 2016-04-24. https://arxiv.org/abs/1604.07089.
4. *Exact dyadic valuation law for \(\binom{3n}{n}\)*, public result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-dyadic-valuation-law-for-binom-3n-n--499526ba814d/RESULT.md.
5. *Exact two-sum spectra and dyadic additive energy of odd Pascal-row positions*, public result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-two-sum-spectra-and-dyadic-additive-energy-of-odd-pascal-r--fd21e3c6e379/RESULT.md.
6. *Exact correlation dimension and an \(L^2\) obstruction for a three-digit four-adic convolution*, public result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-correlation-dimension-and-an-l-obstruction-for-a-three-dig--0a6383f8b10e/RESULT.md.
