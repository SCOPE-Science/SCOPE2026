# Sharp negative-set length in the first three negative-Fourier Hermite modes

## Finding

For the unitary Fourier transform 
\[\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx,\]
consider the real Gaussian–Hermite space
\[\mathcal H_-^{(10)}=\operatorname{span}_{\mathbb R}\{e^{-\pi x^2}L_j^{-1/2}(2\pi x^2):j=1,3,5\},\]
where \(L_j^\alpha\) are generalized Laguerre polynomials. Every element satisfies \(\widehat f=-f\). Among all nonzero \(f\in\mathcal H_-^{(10)}\) with \(f(0)=0\), the smallest Lebesgue length of \(\{x\in\mathbb R:f(x)\le0\}\) is
\[
\boxed{\sqrt{\frac2\pi}\left(\sqrt{\frac{15+\sqrt{105}}4}-\sqrt{\frac{15-\sqrt{105}}4}\right)=1.1347855277\ldots.}
\]
The only extremizers are positive scalar multiples of
\[
f_*(x)=e^{-\pi x^2}z(2z^2-15z+15),\qquad z=2\pi x^2.
\]
The nonpositive set of this extremizer (apart from isolated zeroes) is the symmetric annulus \(r_-\le2\pi x^2\le r_+\), where \(r_\pm=(15\pm\sqrt{105})/4\). This theorem concerns this exact three-mode family, not the unrestricted sign-uncertainty infimum.

## Assumptions and scope

Lebesgue measure is on \(\mathbb R\). Functions are real-valued and nonzero, and their transform normalization is as displayed above. The sign constraint is pointwise \(f(0)=0\), and the nonpositive set includes zeroes; isolated polynomial zeroes have measure zero. No evenness restriction beyond that already forced by the Hermite space is imposed. All coefficients in the three-dimensional real span are allowed, including sign-indefinite ones. If a polynomial has a negative leading coefficient, its nonpositive set has infinite measure and cannot minimize.

## Proof

**1. Fourier spectral reduction.** The generating identity
\[
\sum_{j\ge0}L_j^{-1/2}(z)s^j=(1-s)^{-1/2}\exp\left(-\frac{zs}{1-s}\right)
\]
and the Gaussian Fourier-transform formula show that \(\widehat{e^{-\pi x^2}L_j^{-1/2}(2\pi x^2)}=(-1)^j e^{-\pi x^2}L_j^{-1/2}(2\pi x^2)\). In particular all three selected odd indices have eigenvalue \(-1\).

The condition \(f(0)=0\) reduces the space to the real span of
\[
A(z)=L_3^{-1/2}(z)-\frac{L_3^{-1/2}(0)}{L_1^{-1/2}(0)}L_1^{-1/2}(z)=-\frac{z(2z^2-15z+15)}{12},
\]
\[
B(z)=L_5^{-1/2}(z)-\frac{L_5^{-1/2}(0)}{L_1^{-1/2}(0)}L_1^{-1/2}(z)=-\frac{z(4z^4-90z^3+630z^2-1575z+945)}{480}.
\]
Thus every admissible function is \(e^{-\pi x^2}(aA(z)+bB(z))\), not both coefficients zero. For \(b>0\), or \(b=0,a>0\), the polynomial is negative for all sufficiently large \(z\); hence its nonpositive-set length is infinite. When \(b=0,a<0\), it is the positive ray of \(f_*\), and its nonpositive-set length is the value claimed.

**2. One-parameter family.** For \(b<0\) divide by the positive number \(-b\) and write the polynomial as \(-B+tA=zQ_t(z)/480\) with \(t=a/(-b)\) and
\[
Q_t(z)=4z^4-90z^3+(630-80t)z^2+(-1575+600t)z+945-600t.
\]
Set \(D(z)=z^2-\tfrac{15}{2}z+\tfrac{15}{2}=(z-r_-)(z-r_+)\), so \(Q_t=Q_0-80tD\). Exact polynomial division gives \(Q_t(r_-)=Q_t(r_+)=-180\) for all real \(t\). Whenever \(Q_t\) is strictly negative on an interval \([u,v]\subset(0,\infty)\), the nonpositive-set length is at least \(\sqrt{2/\pi}(\sqrt v-\sqrt u)\). Disjoint interval contributions add.

**3. Rational Bernstein certificates for the central range.** For a real quartic \(P\), write \(P(u+(v-u)s)=\sum_{k=0}^4\beta_k\binom4k s^k(1-s)^{4-k}\). If every \(\beta_k<0\), then \(P<0\) on \([u,v]\). Its coefficients are rational whenever the original coefficients and endpoints are rational, and are affine in \(t\) for \(P=Q_t\); consequently it suffices to check both endpoints of each parameter strip. The following disjoint \(z\)-intervals have **all five Bernstein coefficients strictly negative at both strip endpoints**. The final column gives an exact rational lower bound for the sum of their \(\sqrt v-\sqrt u\) contributions; each bound is verified by integer arithmetic in the standalone checker.

| Parameter \(t\) | Guaranteed negative \(z\)-intervals | Lower bound on sum |
|---|---|---|
| \([-1,-1/2]\) | \([1,3],[3,5],[5,7],[7,173/20]\) | \(19406/10000\) |
| \([-1/2,0]\) | \([95/100,406/100],[566/100,1063/100]\) | \(19214/10000\) |
| \([0,1/2]\) | \([87/100,291/100],[596/100,1191/100]\) | \(17826/10000\) |
| \([1/2,1]\) | \([73/100,220/100],[606/100,1291/100]\) | \(17599/10000\) |
| \([1,3/2]\) | \([47/100,180/100],[612/100,1376/100]\) | \(18915/10000\) |
| \([3/2,2]\) | \([8/100,158/100],[616/100,1451/100]\) | \(23011/10000\) |

All six lower bounds exceed \(17/10\), whereas the target \(\sqrt{r_+}-\sqrt{r_-}<\sqrt7-1<17/10\), since \(10<\sqrt{105}<11\). Thus every \(t\in[-1,2]\) has strictly greater nonpositive-set length than \(f_*\).

**4. The unbounded parameter tails.** If \(t\ge2\), then \(D>0\) on \([0,1]\cup[7,12]\), so \(Q_t\le Q_2\) there. All Bernstein coefficients of \(Q_2\) are strictly negative on each interval; their combined square-root length is greater than \(18182/10000>17/10\), proving strict excess.

If \(t\le-1\), then \(D\le0\) on \([r_-,r_+]\), and \(Q_t=Q_{-1}-80(t+1)D\le Q_{-1}\). The degree-four Bernstein coefficients of \(Q_{-1}\) on this algebraic interval are, in order,
\[
-180,\quad-\frac{24135+1575\sqrt{105}}{32},\quad-\frac{1945}{4},\quad-\frac{24135-1575\sqrt{105}}{32},\quad-180.
\]
They are all strictly negative. Furthermore \(Q_t(r_-)=Q_t(r_+)=-180\), so continuity forces \(Q_t<0\) on a strictly larger open interval surrounding \([r_-,r_+]\). The nonpositive-set length is therefore strictly greater than the target. The unique extremizing ray is the one with \(b=0,a<0\).

## Verification

Run `python3 verify.py` from the directory containing this document. It uses only Python's standard library, recalculates the two Laguerre identities by rational recurrence, computes every rational Bernstein coefficient at all stated endpoints, derives strict lower bounds using integer square-root arithmetic rather than decimal floating point, independently recomputes the five algebraic Bernstein coefficients in \(\mathbb Q(\sqrt{105})\), and checks \(Q_t\bmod D=-180\) at several exact rational values. These finite algebraic certificates support the universally quantified sign conclusions because the coefficients are affine in \(t\) and the Bernstein basis is nonnegative. The Fourier generating-function identity and interval-continuity steps are proved analytically above rather than inferred from tests. No numerical root-finding or sampling is used to establish the extremum.

## Relationship to prior work

R. Edwin, *Fourier inequalities and sign uncertainty II* (first public version 5 November 2026), introduces a definite-set sign uncertainty question for Fourier eigenfunctions. The present result supplies an exact, explicitly delimited negative-eigenvalue finite-band benchmark; it does not determine the global unrestricted infimum. A published result titled *Sharp negative-set length in the first three positive-Fourier Hermite modes* treats Fourier eigenvalue \(+1\) with orders \(0,4,8\). Its different eigenvalue space and polynomial family do not imply the theorem here. Cohn, Dong and Gonçalves prove a high-dimensional asymptotic sign-radius result for low-degree Gaussian-polynomial functions, not the one-dimensional finite-mode negative-set length here. Classical Gaussian–Hermite and Beurling-type uncertainty results provide further background but not this minimization formula.

## Limitations

Only the exact real span of Hermite orders \(2,6,10\), with the condition \(f(0)=0\), is classified. The theorem gives neither a bound on all Fourier \(-1\) eigenfunctions nor an assertion about sign sets when the initial-value constraint is dropped. The originality comparison is based on accessible primary material and indexed results; an older unindexed exact calculation of the same finite-mode problem cannot be ruled out. No independent audit has been performed.

## References

1. R. Edwin, *Fourier inequalities and sign uncertainty II*, arXiv:2611.08224v1, first submitted 5 November 2026, https://arxiv.org/abs/2611.08224.
2. A. Bonami, B. Demange and P. Jaming, *Hermite functions and uncertainty principles for the Fourier and the windowed Fourier transforms*, Rev. Mat. Iberoam. 19 (2003), https://doi.org/10.4171/RMI/337.
3. *Sharp negative-set length in the first three positive-Fourier Hermite modes*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-sharp-negative-set-length-in-the-first-three-positive-fourier-he--0c4edba5f7b1.
4. L. D. Abreu, U. Chabaud, N. Costa Dias and J. N. Prata, *Inverse problems for the zeros of the Wigner function*, arXiv:2504.20324, https://arxiv.org/abs/2504.20324.
5. H. Cohn, D. Dong and F. Gonçalves, *Sign uncertainty principles and low-degree polynomials*, Proc. Amer. Math. Soc. Ser. B 11 (2024), 224–228, https://arxiv.org/abs/2210.01684.
