# A geometric boundary layer and Gaussian genus law for high-multiplicity perfect numerical semigroups

## Finding

For every integer \(F\ge3\), let \(\mathcal P_F^{>}\) be the family of numerical semigroups \(S\subseteq\mathbb N_0\) of Frobenius number \(F\), with no isolated gap, and with multiplicity \(m(S)>F/2\). Write \(g(S)=|\mathbb N_0\setminus S|\), let \(h=\lfloor(F-1)/2\rfloor\), and put \(N_F=|\mathcal P_F^{>}|\).

**Counting identities used for the limit law.** For each integer \(2\le t\le h\), the polynomial counting semigroups with \(m(S)=F-t\), where \(u\) marks the number of gaps in \((m(S),F]\) (including the forced gap \(F\)), is the coefficient of \(z^t\) in

\[
A(z,u)=\frac{u^2z^2}{(1-z)(1-uz)-u^2z^3}.
\]

Consequently, the exact genus polynomial for the entire family is

\[
H_F(u)=\sum_{S\in\mathcal P_F^{>}}u^{g(S)}
=u^F+\sum_{t=2}^h u^{F-t-1}[z^t]A(z,u).
\]

The first term is the unique ordinary semigroup \(\{0\}\cup\{F+1,F+2,\ldots\}\), of multiplicity \(F+1\) and genus \(F\). In particular, for each integer \(g\) and \(2\le t\le h\), the number at exact genus \(g\) and multiplicity \(F-t\) is \([z^t u^{g-F+t+1}]A(z,u)\).

**Classical word count in semigroup coordinates.** If \(B_h=N_{2h+1}=N_{2h+2}\) for integers \(h\ge1\), and \(B_0=1\), then

\[
\sum_{h\ge0}B_h z^h=\frac{1-z+z^2}{1-2z+z^2-z^3}.
\]

Let \(r\in(0,1)\) be the unique positive root of \((1-r)^2=r^3\), and let \(\lambda=r^{-1}=1.75487766624669\ldots\). Then

\[
N_F=C\lambda^h+O(\tau^h),\qquad
C=\frac{1-r+r^2}{r(2-2r+3r^2)}=0.722124418303\ldots,
\]

for any fixed \(\tau\) strictly between the modulus of the other two roots of \(\lambda^3-2\lambda^2+\lambda-1\) and \(1\) (for example \(\tau=0.9\)).

**Main result: joint limit law.** Select \(S_F\) uniformly from \(\mathcal P_F^{>}\). Let \(J_F=m(S_F)-(F-h)\), and put

\[
\rho=\frac{2r^2-r+1}{3r^2-2r+2},\quad
v=\frac{(r^2-r+1)(4r^2+1)}{(3r^2-2r+2)^3},\quad
\alpha=\frac{1+\rho}{2},\quad \beta=\frac v2.
\]

Numerically, \(\alpha=0.794252205668\ldots\) and \(\beta=0.140548806171\ldots\). As \(F\to\infty\) over *both* parities,

\[
\left(J_F,\frac{g(S_F)-\alpha F}{\sqrt F}\right)
\ \xrightarrow{d}\ (J,Z),
\]

where \(J\) and \(Z\) are independent, \(\Pr(J=j)=(1-1/\lambda)\lambda^{-j}\) for every integer \(j\ge0\), and \(Z\) is normal with mean \(0\) and variance \(\beta\). Moreover, \(\mathbb E[g(S_F)]=\alpha F+O(1)\) and \(\operatorname{Var}(g(S_F))=\beta F+O(1)\).

## Assumptions and scope

A numerical semigroup is a cofinite additive submonoid of the nonnegative integers containing zero; its Frobenius number is its largest missing nonnegative integer. A gap \(q\) is isolated when both \(q-1\) and \(q+1\) belong to the semigroup. Perfect means no isolated gaps. The only restriction besides fixed Frobenius number and perfectness is strict high multiplicity \(m(S)>F/2\); no claim is made for perfect numerical semigroups of smaller multiplicity. The finite statements include every integer \(F\ge3\). The asymptotic statements concern \(F\to\infty\) with no parity restriction.

## Proof

**1. The binary-word bijection.** For nonordinary \(S\) of Frobenius number \(F\) and multiplicity \(m>F/2\), write \(m=F-t\). Because \(m\le F-1\) in the nonordinary case and the Frobenius gap cannot be isolated, \(2\le t\le h\), and both \(F-1\) and \(F\) are gaps. Define a length-\(t\) binary word \(w\) indexed by \(m+1,\ldots,F\), with symbol \(1\) for membership in \(S\) and symbol \(0\) for a gap. There is no isolated gap precisely when the terminal and every other maximal zero-run in \(w\) have length at least two. The initial gap block \(1,\ldots,m-1\) is already of length at least two and is separated from the word by \(m\in S\). Since any two positive elements of \(S\) sum to more than \(F\), every such binary word automatically defines a cofinite additive submonoid \(\{0,m\}\cup\{m+i:w_i=1\}\cup\{F+1,F+2,\ldots\}\). This is a bijection. If the word has \(k\) zeros, then \(g(S)=m-1+k=F-t-1+k\). The ordinary semigroup must be included separately.

**2. Exact generating function.** A valid word consists of an optional initial run of ones, followed by a zero-run of length at least two, followed by any number of pairs (positive run of ones, zero-run of length at least two). Give each position weight \(z\), and each zero an additional factor \(u\). The three building-block series are respectively \((1-z)^{-1}\), \((uz)^2/(1-uz)\), and \([z/(1-z)]\,[(uz)^2/(1-uz)]\). Their product-geometric sum is

\[
\frac{1}{1-z}\frac{(uz)^2}{1-uz}
\left(1-\frac{z}{1-z}\frac{(uz)^2}{1-uz}\right)^{-1}
=\frac{u^2z^2}{(1-z)(1-uz)-u^2z^3}.
\]

This proves the coefficient and genus formulas. For a marker of gaps strictly between \(m(S)\) and \(F\), the polynomial would instead be \(u^{-1}[z^t]A(z,u)\). Substituting \(u=1\) gives \(a_t=[z^t]A(z,1)\); summing \(1+\sum_{t=2}^h a_t\) and cancelling the factor \(1-z\) yields \((1-z+z^2)/(1-2z+z^2-z^3)\). The same \(h\) governs the consecutive Frobenius values \(2h+1\) and \(2h+2\). Equivalently, pad a length-\(t\) admissible word ending in zeros with \(h-t\) ones on its right. Each length-\(h\) word without a singleton zero-run is recovered exactly once by taking its prefix through the last zero, with the all-ones word representing the ordinary semigroup. Thus \(B_h\) is the Austin–Guy word count, after complementing the bits.

**3. Exponential count.** The denominator \(D(z)=1-2z+z^2-z^3\) is strictly decreasing on the real line, since \(D'(z)=-3(z-1/3)^2-5/3\). Its sole real zero is simple and lies at \(r\in(0,1)\). The product of the three roots is one, so the conjugate nonreal zeros have modulus \(r^{-1/2}>1\); the corresponding reciprocal roots have modulus \(r^{1/2}<1\). Partial fractions give

\[
B_h=\frac{1-r+r^2}{-rD'(r)}r^{-h}+O(\tau^h),
\]

with \(-D'(r)=2-2r+3r^2\), proving the stated amplitude and error. No unproved cancellation of equally dominant poles is used.

**4. Analytic genus fluctuations.** For \(u\) in a complex neighborhood of \(1\), the denominator \(D(z,u)=(1-z)(1-uz)-u^2z^3\) has a unique simple dominant zero \(r(u)\) varying analytically with \(u\), with \(r(1)=r\). All other zeros remain uniformly farther away. Thus, uniformly near \(u=1\),

\[
[z^t]A(z,u)=c(u)r(u)^{-t}(1+O(q^t)),\qquad
c(u)=-\frac{u^2r(u)}{\partial_zD(r(u),u)},\quad 0<q<1.
\]

Set \(\Lambda(s)=r(e^s)^{-1}\). The logarithm of the normalized probability generating function for the zero count in length-\(t\) words has the expansion \(t(\log\Lambda(s)-\log\Lambda(0))+O(1)\), analytically in a fixed complex neighborhood of zero. Implicit differentiation of \(D(r(e^s),e^s)=0\) gives

\[
\left.\frac{d}{ds}\log\Lambda(s)\right|_{s=0}=\rho,
\qquad
\left.\frac{d^2}{ds^2}\log\Lambda(s)\right|_{s=0}=v>0.
\]

The explicitly positive numerator in the displayed formula for \(v\) proves nonzero variance. With \(\xi\) a fixed real Fourier variable, Taylor expansion at \(s=i\xi/\sqrt t\) and subtraction of the centering term \(\rho t s\) give the limiting log characteristic function \(-v\xi^2/2\): the bounded analytic correction to the normalized log generating function vanishes at \(s=0\), and is therefore \(O(|s|)\) on a smaller disk by Cauchy's estimate. Differentiating at zero also gives expectation \(\rho t+O(1)\) and variance \(vt+O(1)\).

**5. Boundary-layer mixing.** In the nonordinary class at fixed \(F\), write \(t=h-j\), so \(J_F=j\); the ordinary semigroup has \(J_F=h+1\). Since \(a_t=B_t-B_{t-1}\) for \(t\ge2\), for each fixed \(j\) the classical total count in Step 3 gives \(a_{h-j}/N_F\to(1-r)r^j\). The same estimates imply \(a_t\le M r^{-t}\) and \(1/N_F\le M r^h\) for a constant \(M\). Summing geometrically and including the ordinary term gives \(\Pr(J_F\ge J_0)=O(r^{J_0})\) uniformly for nonnegative integers \(J_0\). Given fixed \(j\) and sufficiently large \(F\), the genus is \(F-h+j-1\) plus the zeros in a uniformly selected word of length \(t=h-j\). The conditional centering \(F-h+j-1+\rho t\) differs from \(\alpha F\) by \(O(1)\) at fixed \(j\), and \(t/F\to1/2\). Step 4 gives the same limiting \(\mathcal N(0,v/2)\) at every fixed \(j\). Summing over a fixed finite set of \(j\) and then using the tail bound proves convergence to the independent product law.

For the cumulants, substituting the coefficient estimate of Step 4 into \(H_F(e^s)\) and summing gives, uniformly in a small complex disk about zero,
\[
 H_F(e^s)=e^{s(F-h-1)}c(e^s)\Lambda(s)^h
 \left(\frac{1}{1-e^s/\Lambda(s)}+O(Q^h)\right)
\]
for some \(Q<1\). Indeed, shrink the disk until \(\sup|e^s/\Lambda(s)|<1\); the sum of the coefficient errors is bounded by a constant times \(\sum_{j=0}^{h-2}|e^s/\Lambda(s)|^j q^{h-j}\), exponentially small in \(h\), as are the omitted geometric tail and the normalized ordinary term \(e^s(e^s/\Lambda(s))^h\). The amplitude is analytic and nonzero near zero. Thus after division by \(H_F(1)\), the logarithm differs from \(s(F-h-1)+h(\log\Lambda(s)-\log\Lambda(0))\) by a bounded analytic function on a fixed smaller disk. Its first two derivatives at zero are bounded, giving the asserted mean and variance because \(h=F/2+O(1)\).

## Verification

The standalone `verify_perfect.py` uses integer arithmetic to cross-check the closed formulas against exhaustive subset enumeration and direct semigroup addition checks for all \(3\le F\le18\) (16 independent complete censuses and 298 semigroups). It also verifies 17 polynomial coefficient identities through word length 18 and computes exact first and second genus moments through \(F=1001\), comparing them with the established asymptotic constants. Run `python3 verify_perfect.py` with Python 3; no third-party dependencies are needed. These tests independently corroborate finite identities and constants but are not substituted for the infinite analytic proof above.

## Relationship to prior work

Austin and Guy (1978) already give the equivalent unmarked word sequence (OEIS A005251 at index \(h+2\)), its recurrence, characteristic cubic, root modulus and dominant amplitude. The total census and geometric marginal here are reformulations or consequences of that classical word count, not novelty claims. Finch (2020, §3) gives the same unmarked word generating function and analyzes a position-weighted real encoding of those words, not their Hamming weight. The finite marked counts also follow from prior Hamming-weight enumerations of words by run restrictions: if \(W_t(u)\) marks zeros over all length-\(t\) words without singleton zero-runs, the words ending in one contribute \(W_{t-1}(u)\) by deleting that final one. Hence \([z^t]A(z,u)=W_t(u)-W_{t-1}(u)\) for \(t\ge1\). Balado and Silvestre (§4.1 with zero runs of length one, after complementing the bits) give the word counts with this Hamming-weight condition. The direct generating-function derivation above is included to make the limit calculation self-contained.

Moreno-Frías and Rosales (2023, first public preprint 24 May 2023) give the fixed-Frobenius perfect-semigroup covariety framework and an algorithm enumerating its members at prescribed genus. Singhal's (2022) genus law for unrestricted numerical semigroups includes a leading typical genus of \(3F/4\) and does not determine the law of this restricted population. Bras-Amorós and Torra count all large-multiplicity numerical semigroups, without the no-isolated-gap constraint. The contribution here is the conditional Gaussian genus law with explicit leading mean and variance and its joint asymptotic independence from the geometric multiplicity offset in the high-multiplicity perfect population. Historical priority for that joint law is limited to the literature inspected.

## Limitations

The theorem applies only to perfect numerical semigroups with multiplicity strictly exceeding half their Frobenius number. The ordinary semigroup is included; smaller-multiplicity perfect semigroups are not. The numerical computations are finite checks and do not certify the infinite asymptotics. An unindexed or differently formulated prior limit theorem is not ruled out.

## References

1. M. A. Moreno-Frías and J. C. Rosales, *The covariety of perfect numerical semigroups with fixed Frobenius number*, arXiv:2305.14967 (first posted 24 May 2023); later Czechoslovak Mathematical Journal 74 (2024), 697–714. https://arxiv.org/abs/2305.14967
2. M. A. Moreno-Frías and J. C. Rosales, *Perfect numerical semigroups*, Turkish Journal of Mathematics 43 (2019), 1742–1754, DOI:10.3906/mat-1901-111. https://doi.org/10.3906/mat-1901-111
3. D. Singhal, *Distribution of genus among numerical semigroups with fixed Frobenius number*, Semigroup Forum 104 (2022), 704–723. https://doi.org/10.1007/s00233-022-10282-6
4. M. Bras-Amorós and V. Torra, *Multiparameter counting of numerical semigroups by Frobenius number, genus, and multiplicity*, arXiv:2611.11559 (8 November 2026). https://arxiv.org/abs/2611.11559
5. R. Austin and R. K. Guy, *Binary sequences without isolated ones*, Fibonacci Quarterly 16 (1978), 84–86. https://www.fq.math.ca/Scanned/16-1/austin.pdf
6. The On-Line Encyclopedia of Integer Sequences, *A005251*. https://oeis.org/A005251
7. F. Balado and G. C. M. Silvestre, *Systematic Enumeration of Fundamental Quantities Involving Runs in Binary Strings*, arXiv:2602.10005 (2026). https://arxiv.org/abs/2602.10005
8. S. Finch, *Cantor-solus and Cantor-multus Distributions*, arXiv:2003.09458 (2020). https://arxiv.org/abs/2003.09458
