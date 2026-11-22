# Complete pair-sum spectrum and fourth Kloosterman moments of odd modular hyperbolas

## Finding

Let \(p\) be an odd prime, \(k\ge2\), \(q=p^k\), \(R=\mathbb Z/q\mathbb Z\), \(U=R^\times\), and \(N=|U|=(p-1)p^{k-1}\). For the modular inverse hyperbola
\[
\Gamma_q=\{(u,u^{-1}):u\in U\}\subset R^2,
\]
let \(r_q(s,t)=\#\{(u,v)\in U^2:u+v=s,\ u^{-1}+v^{-1}=t\}\), where pairs are ordered. **Every nonzero value and its frequency are given below**. If two displayed values happen to coincide, add their frequencies.

Define \(m=\lfloor(k-1)/2\rfloor\) and \(N_j=(p-1)p^{k-j-1}\) for \(1\le j<k\). The complete positive-value histogram is:

| Value of \(r_q\) | Number of outputs \((s,t)\) attaining it |
| --- | --- |
| \(N\) | \(1\) |
| \(2p^j\), for each \(1\le j<k\) | \(N_j^2/2\) |
| \(2\) | \(N(p-3)p^{k-1}/2\) |
| \(2p^v\), for each \(1\le v\le m\) | \(N(p-1)p^{k-2v-1}/2\) |
| \(p^{\lfloor k/2\rfloor}\) | \(N\) |

All other outputs have \(r_q(s,t)=0\). In particular, \(|\Gamma_q+\Gamma_q|\) is the sum of the frequencies in the right column (before aggregation), and the *exact additive energy* is
\[
E(\Gamma_q)=\sum_{(s,t)\in R^2}r_q(s,t)^2
=N^2\left(3k-\frac{3}{p-1}\right).
\]

For \(K_q(a,b)=\sum_{u\in U}\exp(2\pi i(au+bu^{-1})/q)\), the unweighted, complete two-frequency fourth moment consequently satisfies
\[
\boxed{\frac1{q^2}\sum_{a,b\in R}|K_q(a,b)|^4
=N^2\left(3k-\frac3{p-1}\right).}
\]
The corresponding second moment is \(q^{-2}\sum_{a,b}|K_q(a,b)|^2=N\). Thus the ratio of the averaged fourth moment to the square of the averaged second moment is exactly \(3k-3/(p-1)\), growing linearly with the prime-power depth.

For a general odd modulus \(n=\prod_i p_i^{k_i}>1\), the Chinese remainder theorem gives a *complete representation histogram* by taking all products of the local representation values, with product frequencies. It also gives
\[
E(\Gamma_n)=\varphi(n)^2\prod_{p^k\parallel n}\left(3k-\frac3{p-1}\right).
\]
The \(k=1\) case is included in the formulas as a known boundary case; no novelty is asserted for that prime-field case.

## Assumptions and scope

All rings are \(\mathbb Z/n\mathbb Z\) with odd \(n\). The expression \(u^{-1}\) is the multiplicative inverse of a unit. Fourier sums are unnormalized; frequency averaging means division by \(n^2\). The claim is an exact classification of \(\mathbf1_{\Gamma_n}*\mathbf1_{\Gamma_n}\) and of its squared \(\ell^2\)-norm. It is **not** a sharp \(\ell^2\to L^4\) extension inequality for arbitrary coefficients, nor does it cover even moduli.

## Proof

**Step 1: reduction to quadratic roots.** Let \(s,t\in R\), \(s\ne0\), and write \(j=v_p(s)<k\), where \(v_p(0)=k\). For units \(u\), \(v=s-u\),
\[
u^{-1}+v^{-1}=\frac{s}{uv}.
\]
Hence \(r_q(s,t)=0\) unless \(v_p(t)=j\). In that case write \(s=p^j a\), \(t=p^j b\), with \(a,b\) units modulo \(p^{k-j}\), and put \(L=k-j\). The equation is exactly
\[
u(s-u)\equiv ab^{-1}\pmod{p^L}.
\]
Every solution modulo \(p^L\) lifts to exactly \(p^j\) allowed units \(u\) modulo \(p^k\). Conversely every allowed ordered pair arises in this way.

**Step 2: positive-valuation strata.** If \(1\le j<k\), reduction modulo \(p\) gives \(u^2\equiv-ab^{-1}\pmod p\). The right side is a unit. It has either zero or two roots. Each root is simple since \(p\) is odd, so each lifts uniquely modulo \(p^L\). Therefore \(r_q(s,t)\) is either \(0\) or \(2p^j\). For each \(s\) of valuation \(j\), exactly half the \(N_j\) choices of \(t\) with valuation \(j\) satisfy the quadratic-residue condition. This proves the row with multiplicity \(N_j^2/2\).

**Step 3: unit-sum stratum.** If \(j=0\), the substitution \(w=ab^{-1}=st^{-1}\) maps unit values of \(t\) bijectively to unit values of \(w\). Completing the square gives
\[
(2u-s)^2\equiv\Delta=s^2-4w\pmod{p^k}.
\]
Every resulting root produces units \(u\) and \(s-u\), since their product equals the unit \(w\). As \(w\) runs over units, \(\Delta\) runs bijectively over residues satisfying \(\Delta\not\equiv s^2\pmod p\).

For a nonzero \(\Delta\) with \(v_p(\Delta)=2v<k\), a root exists precisely if the unit part of \(\Delta\) is a square modulo \(p\); then there are exactly \(2p^v\) roots. Indeed, writing the root as \(p^v z\), Hensel lifting gives two roots modulo \(p^{k-2v}\), each with \(p^v\) lifts modulo \(p^{k-v}\). Odd valuations or nonsquare unit parts give no roots. At \(\Delta=0\), the roots are precisely multiples of \(p^{\lceil k/2\rceil}\), numbering \(p^{\lfloor k/2\rfloor}\).

For fixed \(s\in U\), the number of admissible nonzero-square-residue \(\Delta\) with valuation zero is \((p-3)p^{k-1}/2\): one quadratic-residue class, namely \(s^2\), is excluded. For each \(1\le v\le\lfloor(k-1)/2\rfloor\), the number with valuation \(2v\) and square unit part is \((p-1)p^{k-2v-1}/2\). There is one \(\Delta=0\). Multiplication by the \(N\) choices of \(s\) establishes the last three histogram families.

**Step 4: origin and exhaustion.** When \(s=0\), necessarily \(v=-u\), hence \(t=0\) and exactly \(N\) ordered pairs contribute. These are the only remaining cases, because \(v_p(t)=v_p(s)\) whenever \(s\ne0\).

**Step 5: fourth moment.** By the histogram,
\[
\begin{aligned}
E(\Gamma_q)
&=(2k-1)N^2\\
&\quad+N\left[2\bigl(p-3+(p-1)\lfloor(k-1)/2\rfloor\bigr)p^{k-1}
+p^{2\lfloor k/2\rfloor}\right].
\end{aligned}
\]
The first term combines the origin contribution with the \(k-1\) nonunit-sum strata, each contributing \(2N^2\). Simplification separately for even and odd \(k\) yields \(N^2(3k-3/(p-1))\) in both cases. Orthogonality of additive characters on \(R^2\) gives
\[
\frac1{q^2}\sum_{a,b}|K_q(a,b)|^4
=\sum_{s,t}r_q(s,t)^2.
\]
The analogous second-moment identity follows from injectivity of \(u\mapsto(u,u^{-1})\). Finally, the Chinese remainder theorem identifies the inverse hyperbola and its pair-sum convolution with products of local ones, so both the histogram and energy factor over distinct prime factors.

## Verification

`CHECKER.py` is a standalone Python 3 standard-library program. Run `python CHECKER.py` to enumerate ordered pairs and independently compare the observed histogram with the formula for \((p,k)=(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(11,1),(11,2)\). It also checks the moment identity by evaluating all additive Fourier frequencies at moduli \(3,5,9,15,25,27\). Integer histogram and energy checks are exact; complex Fourier checks use a stated floating-point tolerance. Those finite computations corroborate the preceding proof and are not used to infer the infinite claim.

## Relationship to prior work

Iosevich–Koh (2008) establish Fourier extension estimates for quadratic surfaces over **finite fields** and explain the two-point sum method. Kowalski (2010), explaining the classical Kloosterman computation, gives the prime-field fourth moment and the exceptional opposite-pair solutions. These are precursors, not novel portions of the present claim. Bower–Evans–Luo–Miller (2012) determine *coordinate* sums \(u+u^{-1}\) of individual points on modular hyperbolas, not the two-dimensional Minkowski pair-sums of two curve points. Guo–Geng–Pan (2014) calculate fourth moments **summed over multiplicative characters** with a fixed second additive argument; Wenpeng Zhang (2016) treats fixed-argument, primitive-multiplicative-character Kloosterman moments. None of the inspected statements provides the full two-coordinate pair-sum multiplicity distribution over every odd prime-power modulus. Priority is subject to the stated residual risk from earlier local exponential-sum literature.

## Limitations

The sharp fourth-moment norm over **arbitrary** coefficient functions is not computed. The theorem is for the constant-coefficient Kloosterman family and the full ordered additive convolution. The prime-field boundary case is known. Characteristic two is excluded; no claim is made for even moduli. The calculations are finite spot checks, not exhaustive verification for all primes or exponents. No independent mathematical audit has been performed.

## References

- A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, 2008-04-28. https://arxiv.org/abs/0804.4505
- E. Kowalski, *The fourth moment of Kloosterman sums*, 2010-02-26. https://blogs.ethz.ch/kowalski/2010/02/26/the-fourth-moment-of-kloosterman-sums/
- A. Bower, R. Evans, V. Luo and S. J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930v1, 2012-12-12. https://arxiv.org/abs/1212.2930
- X. Guo, G. Geng and X. Pan, *On the fourth power mean of the general k th Kloosterman sums*, Advances in Difference Equations 2014, article 103, 2014-04-04. https://doi.org/10.1186/1687-1847-2014-103
- W. Zhang, *On the fourth power mean of the general Kloosterman sums*, Journal of Number Theory 169 (2016), 315–326. https://doi.org/10.1016/j.jnt.2016.05.018
