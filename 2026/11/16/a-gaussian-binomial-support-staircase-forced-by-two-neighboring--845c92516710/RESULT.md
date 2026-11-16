# A Gaussian-binomial support staircase forced by two neighboring cyclic STFT slices

## Finding
For an integer \(N\ge3\), write \(\omega=e^{2\pi i/N}\) and define the normalized cyclic short-time Fourier transform
\[
V_gf(x,k)=\frac1{\sqrt N}\sum_{n\in\mathbb Z_N}f(n)\overline{g(n-x)}\omega^{-kn}.
\]
Let \(f,g:\mathbb Z_N\to\mathbb C\) be nonzero. Fix \(x_0,s\in\mathbb Z_N\) with \(\gcd(s,N)=1\). Assume that the frequency slice \(V_gf(x_0,\cdot)\) has exactly one nonzero coefficient, while \(V_gf(x_0+s,\cdot)\) has exactly two. Let \(b,c\in\mathbb Z_N\) be the two frequency indices in the latter slice, and put \(d=N/\gcd(N,c-b)\), the additive order of their difference. Then, for every integer \(0\le j<N\),
\[
\left|\operatorname{supp}V_gf(x_0+js,\cdot)\right|=1+(j\bmod d),
\qquad
\left|\operatorname{supp}V_gf\right|=\frac{N(d+1)}2.
\]
Every divisor \(d>1\) of \(N\) is realized by some everywhere-nonzero pair \(f,g\). In particular, for prime \(N=p\), the successive slice sizes are exactly \(1,2,\ldots,p\), and the total support is \(p(p+1)/2\), independent of the nonzero coefficients in the second slice.

## Assumptions and scope
All supports are exact, not thresholded; the two specified slices are full \(N\)-frequency discrete Fourier transforms. The step \(s\) generates the cyclic group, and the second slice has two *distinct* frequencies with *nonzero* coefficients. No restriction on the magnitudes or phases of \(f\) and \(g\) is otherwise imposed. In fact, the one-frequency assumption forces \(f(n)\) and \(g(n)\) to be nonzero at every \(n\). The result includes composite cyclic orders and all permitted two-frequency separations.

## Proof
Put \(h_j(n)=f(n)\overline{g(n-x_0-js)}\). By discrete Fourier inversion, the first hypothesis gives \(h_0(n)=C\omega^{an}\) with \(C\ne0\) and some \(a\in\mathbb Z_N\). Therefore \(f,g\) are nowhere zero. The second gives \(h_1(n)=A\omega^{bn}+B\omega^{cn}\), where \(AB\ne0\) and \(b\ne c\). Define
\[
R(n)=\frac{h_1(n)}{h_0(n)}=\alpha\omega^{un}+\beta\omega^{vn},
\quad \alpha=A/C\ne0,\ \beta=B/C\ne0,\ u=b-a,\ v=c-a.
\]
Since \(R(n)=\overline{g(n-x_0-s)}/\overline{g(n-x_0)}\), it is nowhere zero; the telescoping relation gives
\[
h_j(n)=h_0(n)\prod_{\ell=0}^{j-1}R(n-\ell s).
\]
Set \(m=v-u=c-b\), \(z=\omega^{mn}\), \(q=\omega^{-ms}\), and \(t=\beta/\alpha\). The root \(q\) has exact order \(d=N/\gcd(N,m)\), since \(s\) is a unit modulo \(N\). Factoring each ratio yields
\[
h_j(n)=C\alpha^j\omega^{(a+ju)n-usj(j-1)/2}
\prod_{\ell=0}^{j-1}(1+tq^\ell z).
\]
The preceding scalar is nonzero for every \(j,n\). The full-order cyclotomic identity is
\[
\prod_{\ell=0}^{d-1}(1+tq^\ell z)=1-(-tz)^d=1-(-t)^d
\]
because \(z^d=1\). This constant is nonzero: every factor on the left is one of the nonzero values \(R(n-\ell s)\), after removal of its nonzero monomial. Write \(j=ad+r\) with \(0\le r<d\). The product for \(j\) therefore equals the nonzero constant \([1-(-t)^d]^a\) times the length-\(r\) product.

For \(0\le r<d\), the finite Gaussian-binomial identity gives
\[
\prod_{\ell=0}^{r-1}(1+tq^\ell z)
=\sum_{h=0}^r t^h q^{h(h-1)/2}
\frac{\prod_{i=0}^{h-1}(1-q^{r-i})}{\prod_{i=1}^h(1-q^i)}z^h.
\]
For \(h=0\) both empty products equal one. As \(q\) has order \(d>r\), each numerator and denominator factor displayed for \(h\ge1\) is nonzero. Thus *all* \(r+1\) coefficients are nonzero. The characters \(z^h=\omega^{mhn}\), \(0\le h\le r\), are distinct because \(m\) has order \(d\); multiplication by the prefactor character only translates their frequency indices. This proves the claimed slice-size staircase. Since \(d\mid N\), summation over \(N/d\) periods yields \(N(d+1)/2\).

For attainability, fix any divisor \(d>1\) of \(N\), choose \(m=N/d\), \(s=1\), \(x_0=0\), and let \(0<\beta=7/10<1\) and \(\alpha=(1+(-\beta)^d)^{1/d}>\beta\) (positive real root). Then \(R(n)=\alpha+\beta\omega^{mn}\) is nowhere zero, and
\[
\prod_{n=0}^{N-1}R(n)=\big(\alpha^d-(-\beta)^d\big)^{N/d}=1.
\]
Thus the cyclic recurrence \(\overline{g(n-1)}=R(n)\overline{g(n)}\) has a nowhere-zero solution \(g\). Let \(f(n)=1/\overline{g(n)}\). Its first slice is the Fourier transform of \(1\), and the next is the Fourier transform of \(R\), supported at precisely \(0\) and \(m\). The general argument applies and proves realization of every \(d\).

## Verification
The proof is algebraic and applies to every integer \(N\ge3\), not just tested cases. The standalone `check_staircase.py` constructs a nonzero window and signal for each divisor order \(d>1\) and \(3\le N\le26\), computes each STFT slice, and compares its support count and total with the theorem. Running `python check_staircase.py` passed 19,058 checked STFT entries. This is supplemental finite verification; floating-point thresholds are not a proof of exact support or nonvanishing.

## Relationship to prior work
Nicola's 2022 paper classifies cyclic STFT pairs attaining the *absolute minimum* support \(N\). Krahmer, Pfander and Rashkov develop general finite-group STFT uncertainty/support estimates and generic-window behavior. These results motivate asking what exact structure is forced by *one monochromatic slice together with a neighboring two-frequency slice*; they do not themselves state the divisor-dependent staircase. The binomial product identity is classical and is used here as a tool, not claimed as a new algebraic identity. Existing unrestricted support lower bounds do not determine the exact conditional row-support sequence of this theorem.

## Limitations
The assertion requires the time step to generate \(\mathbb Z_N\), a first slice with exactly one nonzero Fourier coefficient, and exactly two nonzero coefficients in the next slice. It does not characterize arbitrary higher slice sparsities, non-generating steps, perturbation robustness, or all possible support patterns. Numerical tests use nonzero thresholds and are illustrative only. Historical priority is assessed from inspected relevant literature and available mathematical research records; an earlier specialized result or a stronger general theorem could imply the conclusion, and independent priority verification has not been performed.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1, first public 2022-04-29. https://arxiv.org/html/2204.14176v1
2. F. Krahmer, G. E. Pfander, P. Rashkov, *Uncertainty in time–frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, first public 2006-11-16. https://arxiv.org/abs/math/0611493
