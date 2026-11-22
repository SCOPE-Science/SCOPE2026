# A geometric boundary layer and Gaussian genus law for high-multiplicity perfect numerical semigroups

## Finding

For every integer \(F\ge3\), let \(\mathcal P_F^{>}\) be the family of numerical semigroups \(S\subseteq\mathbb N_0\) of Frobenius number \(F\), with no isolated gap, and with multiplicity \(m(S)>F/2\). Write \(g(S)=|\mathbb N_0\setminus S|\), let \(h=\lfloor(F-1)/2\rfloor\), and put \(N_F=|\mathcal P_F^{>}|\).

**Exact joint enumeration.** For each integer \(2\le t\le h\), the bivariate polynomial counting semigroups with \(m(S)=F-t\), where the second variable marks the number of gaps strictly between \(m(S)\) and \(F\), is the coefficient of \(z^t\) in

\[
A(z,u)=\frac{u^2z^2}{(1-z)(1-uz)-u^2z^3}.
\]

Consequently, the exact genus polynomial for the entire family is

\[
H_F(u)=\sum_{S\in\mathcal P_F^{>}}u^{g(S)}
=u^F+\sum_{t=2}^h u^{F-t-1}[z^t]A(z,u).
\]

The first term is the unique ordinary semigroup \(\{0\}\cup\{F+1,F+2,\ldots\}\), of multiplicity \(F+1\) and genus \(F\). In particular, for each integer \(g\) and \(2\le t\le h\), the number at exact genus \(g\) and multiplicity \(F-t\) is \([z^t u^{g-F+t+1}]A(z,u)\).

**Sharp total enumeration.** If \(B_h=N_{2h+1}=N_{2h+2}\) for integers \(h\ge1\), and \(B_0=1\), then

\[
\sum_{h\ge0}B_h z^h=\frac{1-z+z^2}{1-2z+z^2-z^3}.
\]

Let \(r\in(0,1)\) be the unique positive root of \((1-r)^2=r^3\), and let \(\lambda=r^{-1}=1.75487766624669\ldots\). Then

\[
N_F=C\lambda^h+O(\tau^h),\qquad
C=\frac{1-r+r^2}{r(2-2r+3r^2)}=0.722124418303\ldots,
\]

for any fixed \(\tau\) strictly between the modulus of the other two roots of \(\lambda^3-2\lambda^2+\lambda-1\) and \(1\) (for example \(\tau=0.9\)).

**Joint limit law.** Select \(S_F\) uniformly from \(\mathcal P_F^{>}\). Let \(J_F=m(S_F)-(F-h)\), and put

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

This proves the coefficient and genus formulas. Substituting \(u=1\) gives \(a_t=[z^t]A(z,1)\); summing \(1+\sum_{t=2}^h a_t\) and cancelling the factor \(1-z\) yields \((1-z+z^2)/(1-2z+z^2-z^3)\). The same \(h\) governs the consecutive Frobenius values \(2h+1\) and \(2h+2\).

**3. Exponential count.** The denominator \(D(z)=1-2z+z^2-z^3\) has one positive simple zero \(r\in(0,1)\), because \((1-z)^2/z^3\) decreases strictly from infinity to zero. Its two other zeros are nonreal, of modulus exceeding one (as also follows from the conjugate roots of \(\lambda^3-2\lambda^2+\lambda-1\), whose moduli are less than one). Partial fractions give

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

The explicitly positive numerator in the displayed formula for \(v\) proves nonzero variance. Taylor expansion of this analytic logarithmic generating function at arguments \(s=it/\sqrt h\), with elementary characteristic-function convergence, proves the central limit theorem for zero counts. It also yields expectation \(\rho t+O(1)\) and variance \(vt+O(1)\).

**5. Boundary-layer mixing.** In the full class at fixed \(F\), write \(t=h-j\), with integer \(j\ge0\). Uniformly for any fixed \(j\), \(a_{h-j}/N_F\to(1-r)r^j\). The exponential estimates from Step 4 bound the mass of \(j\ge J_0\) by \(O(r_1^{J_0})\) for some fixed \(r_1<1\), and the ordinary semigroup has vanishing mass. Given \(j\), the genus is \(F-h+j-1\) plus the zeros in a length-\(h-j\) admissible word. Its centered and \(\sqrt F\)-rescaled fluctuations converge to \(\mathcal N(0,v/2)\), uniformly for fixed \(j\). Tightness of the geometric boundary layer, followed by truncation and then removing the truncation, proves the joint product law and independence. The analytic marked generating function obtained by summing in \(j\), equivalently the asymptotic factor \(e^{s(F-h-1)}c(e^s)\Lambda(s)^h/(1-e^s/\Lambda(s))\), has two differentiable cumulants with bounded lower-order terms; hence the stated mean and variance, uniformly across parities.

## Verification

The standalone `verify_perfect.py` uses integer arithmetic to cross-check the closed formulas against exhaustive subset enumeration and direct semigroup addition checks for all \(3\le F\le18\) (16 independent complete censuses and 298 semigroups). It also verifies 17 polynomial coefficient identities through word length 18 and computes exact first and second genus moments through \(F=1001\), comparing them with the established asymptotic constants. Run `python3 verify_perfect.py` with Python 3; no third-party dependencies are needed. These tests independently corroborate finite identities and constants but are not substituted for the infinite analytic proof above.

## Relationship to prior work

Moreno-Frías and Rosales (2023, first public preprint 24 May 2023) introduced the fixed-Frobenius perfect-semigroup covariety framework and algorithms enumerating its members at prescribed genus. They did not state the restricted high-multiplicity rational joint series or these geometric/Gaussian limits in the inspected sections. Their 2019 paper introduced the perfect-semigroup structure and fixed-multiplicity algorithms. Singhal (2022) proved global genus statistics for all semigroups with a fixed Frobenius number, including a leading typical genus of \(3F/4\); its unrestricted results do not imply the distinct conditioned constant above. The 2026 multiparameter counting work of Bras-Amorós and Torra treats all numerical semigroups at large multiplicity, not the no-isolated-gap constraint. The novelty claim is relative to the inspected literature, not a proof that no equivalent prior argument exists.

## Limitations

The theorem applies only to perfect numerical semigroups with multiplicity strictly exceeding half their Frobenius number. The ordinary semigroup is included; smaller-multiplicity perfect semigroups are not. The numerical computations are finite checks and do not independently certify infinite asymptotics. The 2026 multiparameter source was accessible in abstract form only; the risk of an unindexed or differently formulated equivalent enumeration is not eliminated. Independent validation has not been performed.

## References

1. M. A. Moreno-Frías and J. C. Rosales, *The covariety of perfect numerical semigroups with fixed Frobenius number*, arXiv:2305.14967 (first posted 24 May 2023); later Czechoslovak Mathematical Journal 74 (2024), 697–714. https://arxiv.org/abs/2305.14967
2. M. A. Moreno-Frías and J. C. Rosales, *Perfect numerical semigroups*, Turkish Journal of Mathematics 43 (2019), 1742–1754, DOI:10.3906/mat-1901-111. https://doi.org/10.3906/mat-1901-111
3. D. Singhal, *Distribution of genus among numerical semigroups with fixed Frobenius number*, Semigroup Forum 104 (2022), 704–723. https://doi.org/10.1007/s00233-022-10282-6
4. M. Bras-Amorós and V. Torra, *Multiparameter counting of numerical semigroups by Frobenius number, genus, and multiplicity*, arXiv:2611.11559 (8 November 2026). https://arxiv.org/abs/2611.11559
