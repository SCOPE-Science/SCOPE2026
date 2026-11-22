# Bessel extremizers and a quarter-rate boundary layer for Poissonized Hardy averaging

## Finding

Let \(H\) be the real Hardy average on \((0,1)\), and let \(P_t=\exp(t(H-I))\) for \(t>0\). On the real distributional bounded-variation space \(BV(0,1)\), with unweighted interior variation \(|Df|((0,1))\), define
\[
C(t)=\sup_{|Df|((0,1))>0}\frac{\|f-P_tf\|_{L^1(0,1)}}{|Df|((0,1))}.
\]
Let \(I_0\) denote the modified Bessel function with power series \(I_0(z)=\sum_{k=0}^{\infty}(z^2/4)^k/(k!)^2\). There is one \(a_t>0\) with
\[
I_0(2\sqrt{t a_t})=e^t,\qquad s_t=e^{-a_t}.
\]
Then \(C(t)\) is attained, and its unique nonconstant equality functions, modulo almost-everywhere equality, are
\[
f(x)=c+d\,\mathbf1_{(s_t,1)}(x),\qquad c,d\in\mathbb R,\quad d\ne0.
\]
Its exact value has either of the equivalent forms
\[
C(t)=\int_{s_t}^1\!\left[1-e^{-t}I_0\!\left(2\sqrt{t\log(1/u)}\right)\right]du
=\mathbb P\{Y_t>a_t\},
\]
where \(Y_t\) is the compound-Poisson sum of a Poisson\((t)\) number of independent exponential-one variables, with the empty sum zero. The sharp extremizer location and error exhibit the quantitative two-sided regimes
\[
a_t=1+\frac t4+O(t^2),\qquad C(t)=\frac te-\frac{t^2}{4e}+O(t^3)\qquad(t\downarrow0),
\]
\[
a_t=\frac t4+\frac14\log(2\pi t)+O\!\left(\frac{(\log t)^2}{t}\right),\qquad
1-C(t)\sim2(2\pi t)^{-1/4}e^{-t/4}\qquad(t\to\infty).
\]
In particular, the unique worst jump has \(s_t\sim(2\pi t)^{-1/4}e^{-t/4}\) at large time. The result concerns the exact identity-approximation error, not the ordinary operator norm of \(P_t\) on \(L^1\).

## Assumptions and scope

The domain is the open unit interval with Lebesgue output measure, and \(f\) is any real element of \(BV(0,1)\). Its canonical representative may be written \(f(x)=c+\mu((0,x))\) for almost every \(x\), where \(\mu=Df\) is a finite signed measure in the open interval; endpoint values are immaterial. The Hardy map is \((Hf)(x)=x^{-1}\int_0^x f(y)\,dy\) for \(0<x<1\). Because \(H\) is a positive contraction on bounded functions and preserves constants, the bounded-operator exponential \(P_t=e^{-t}\sum_{m=0}^\infty t^mH^m/m!\) acts on every \(BV\) input. At \(t=0\) the defect is identically zero and there is no unique extremizer; all uniqueness assertions require \(t>0\).

## Proof

**1. Probabilistic reduction.** Let \(U_1,U_2,\ldots\) be independent uniform\((0,1)\) variables and \(N_t\) an independent Poisson\((t)\) count. Iterated Hardy averaging has \((H^mf)(x)=\mathbb Ef(xU_1\cdots U_m)\). Thus \((P_tf)(x)=\mathbb Ef(xe^{-Y_t})\), with \(Y_t=-\sum_{j=1}^{N_t}\log U_j\). This identity also follows directly from the absolutely convergent exponential series. Since \(P_t\) fixes constants and the signed-measure representation gives \(f(x)=c+\int\mathbf1_{(s,1)}(x)\,d\mu(s)\), Fubini and the triangle inequality reduce the sharp error to the supremum of single-jump defects.

**2. Exact jump defect.** For \(h_s(x)=\mathbf1_{(s,1)}(x)\), the nonnegative error \(h_s-P_th_s\) vanishes below \(s\). For a realization of \(Y_t\), its integral is the length of \((s,\min\{1,se^{Y_t}\})\), namely \(\min(1,se^{Y_t})-s\). Hence, for \(0<s<1\),
\[
E_t(s):=\|h_s-P_th_s\|_1=\mathbb E[\min(1,se^{Y_t})-s].
\]
The law of \(Y_t\) has an atom of size \(e^{-t}\) at zero and, on \((0,\infty)\), strictly positive density
\[
p_t(y)=e^{-t-y}\sqrt{t/y}\,I_1(2\sqrt{ty}),
\]
which follows by summing the gamma densities conditional on \(N_t=m\ge1\). Here \(I_1(z)=I_0'(z)\). For \(a=-\log s>0\), differentiation under the expectation gives
\[
E_t'(s)=\mathbb E[e^{Y_t}\mathbf1_{\{Y_t<a\}}]-1.
\]
The truncated tilted moment is exactly
\[
\mathbb E[e^{Y_t}\mathbf1_{\{Y_t<a\}}]
=e^{-t}\left(1+\sum_{m\ge1}\frac{t^m a^m}{(m!)^2}\right)
=e^{-t}I_0(2\sqrt{ta}).
\]
The formula includes the atom at zero. Consequently
\[
E_t'(s)=e^{-t}I_0(2\sqrt{t\log(1/s)})-1.
\]
As \(s\) increases from zero to one, this derivative decreases strictly from positive infinity to \(e^{-t}-1<0\). It vanishes exactly at \(s_t\). Since \(E_t(s)\to0\) at both endpoints, \(s_t\) is the unique global maximizer. Integration of \(E'_t\) from \(s\) to one gives the displayed exact integral. At the root, integration by parts in the formula for the expected minimum gives \(E_t(s_t)=\mathbb P(Y_t>a_t)\).

**3. The norm and all equality cases.** For \(\mu=Df\),
\[
\|f-P_tf\|_1\le\int_{(0,1)}E_t(s)\,d|\mu|(s)
\le E_t(s_t)|\mu|((0,1)).
\]
A single jump at \(s_t\) attains equality. If a nonzero signed measure attains equality, the second inequality forces its total variation to be supported on the singleton \(\{s_t\}\), because \(E_t(s)<E_t(s_t)\) at every other point. Thus \(\mu=d\delta_{s_t}\), giving exactly the stated equality class.

**4. Short-time expansion.** The root equation and the series \(I_0(2\sqrt{ta})=1+ta+t^2a^2/4+O(t^3)\), uniformly for \(a\) near one, imply \(a_t=1+t/4+O(t^2)\). Moreover, \(P_t=I+t(H-I)+t^2(H-I)^2/2+O(t^3)\) uniformly on bounded inputs. For the step at \(s=e^{-a}\), \(\|h_s-Hh_s\|_1=sa\) and \(\|h_s-H^2h_s\|_1=s(a+a^2/2)\). Because all the step defects have one sign, their scalar combination expands as
\[
E_t(e^{-a})=t e^{-a}a+\frac{t^2 e^{-a}}2\left(\frac{a^2}{2}-a\right)+O(t^3)
\]
uniformly for \(a\) near one. Substitution of \(a=a_t=1+O(t)\), using stationarity of \(ae^{-a}\) at one, proves the stated coefficient of \(t^2\).

**5. Large-time location.** Put \(z_t=2\sqrt{ta_t}\). The standard positive-real Bessel expansion \(I_0(z)=e^z(2\pi z)^{-1/2}(1+O(z^{-1}))\) yields
\[
z_t=t+\tfrac12\log(2\pi t)+O((\log t)/t).
\]
Squaring and dividing by \(4t\) proves the expansion of \(a_t\) and hence \(s_t\).

**6. Sharp deficit prefactor.** Write \(W_t(y)=e^{-t}I_0(2\sqrt{ty})=\mathbb E[e^{Y_t}\mathbf1_{\{Y_t\le y\}}]\) for \(y>0\), with \(W_t(0)=e^{-t}\). At \(a_t\), \(W_t(a_t)=1\). Stieltjes integration by parts gives
\[
\mathbb P\{Y_t\le a_t\}=e^{-a_t}\left(1+\int_0^{a_t} e^z W_t(a_t-z)\,dz\right).
\]
For each fixed \(z\ge0\), the Bessel derivative ratio \(I_1(r)/I_0(r)=1+O(r^{-1})\) and \(a_t/t\to1/4\) give \(W_t(a_t-z)\to e^{-2z}\). To justify passage under the integral, observe that for \(a_t/2\le y\le a_t\), the logarithmic derivative \(\partial_y\log W_t(y)=\sqrt{t/y}\,I_1(2\sqrt{ty})/I_0(2\sqrt{ty})\) is at least \(3/2\) for all sufficiently large \(t\). Thus \(e^zW_t(a_t-z)\le e^{-z/2}\) for \(0\le z\le a_t/2\). On the remaining interval \(a_t/2\le z\le a_t\), monotonicity gives a total bound \(a_t e^{a_t}W_t(a_t/2)\), which tends to zero since \(I_0(r)\le e^r\) and
\[
-t+a_t+\sqrt{2ta_t}=( -3/4+1/\sqrt2)t+O(\log t)\to-\infty.
\]
Dominated convergence therefore makes the integral tend to \(\int_0^\infty e^{-z}\,dz=1\). As \(C(t)=\mathbb P(Y_t>a_t)\), this proves \(1-C(t)\sim2e^{-a_t}\) and the displayed prefactor. No numeric experiment is used to establish the infinite-time result.

## Verification

The standalone `checker.py` (Python 3 with `mpmath`) checks two independently implemented finite-time formulas: an explicit Poisson mixture of the \(H^m\) step defects and the modified-Bessel integral. It also checks the root equation, nearby maximizing values, and quantitative finite-time consistency with both asymptotic regimes. Running the embedded checker produced `PASS 108 numerical comparisons`. The proof above supplies strict uniqueness and the infinite-time estimates; the numerical samples alone would not prove either.

## Relationship to prior work

The real Hardy average is classical. Arvanitidis and Siskakis (arXiv:1006.1520, first posted 2010-06-08) analyze Cesàro-type operators via dilation semigroups and calculate Hardy-space norms and spectra, rather than the \(BV\)-to-\(L^1\) identity error of \(\exp(t(H-I))\). Miller's 2007 survey concerns analytic Cesàro operators, their spectra and related composition semigroups. The recent real-variable Cesàro spectral study of Belli, Gül, Ross and Siskakis (2026) uses the different nonconstant-preserving kernel \(x^{-1}\int_0^x f(u)/(1-u)\,du\), so its operator-norm and spectral statements do not imply this theorem. Exact sharp bounds for fixed integer iterates of \(H\) also do not determine the Poissonized sharp norm by convex combination: their unique maximizing jumps depend on the integer power. The new exact Bessel threshold and quarter-rate asymptotic require optimizing the full mixture jointly. An exhaustive historical-priority claim is not made.

## Limitations

The theorem is for the specific real one-sided Hardy operator, a Poissonization with a unit-rate jump clock, Lebesgue \(L^1(0,1)\), and unweighted interior distributional variation. It does not assert analogous formulas for weighted interval measures, two-sided averages, non-Poisson mixing laws or general \(L^1\) input functions. The original-source inspection is necessarily limited to accessible texts; possible unindexed equivalent results are a residual historical-priority risk. This is a mathematical argument accompanied by reproducible finite checks, not an independent audit.

## References

- A. G. Arvanitidis and A. G. Siskakis, *Cesàro Operators on the Hardy Spaces of the Half-Plane*, arXiv:1006.1520, first submitted 2010-06-08. https://arxiv.org/abs/1006.1520
- V. G. Miller, *The Cesàro and Related Operators, a Survey*, Banach Center Publications 75 (2007), 233–247. https://doi.org/10.4064/bc75-0-14
- A. Belli, U. Gül, W. T. Ross and A. G. Siskakis, *Crescents and the Real Variable Cesàro Operator*, Integral Equations and Operator Theory 98 (2026), article 42. https://doi.org/10.1007/s00020-026-02865-7
