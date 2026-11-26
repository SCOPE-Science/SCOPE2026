# Sharp BV extremizers and a large-time boundary layer for Poissonized Hardy averaging

## Finding

On the real space \(BV(0,1)\), with unweighted distributional variation on the open interval, let \(Hf(x)=x^{-1}\int_0^x f(u)\,du\) and \(P_t=e^{t(H-I)}\) for \(t>0\). Write
\[
C(t)=\sup_{|Df|((0,1))>0}\frac{\|f-P_tf\|_{L^1(0,1)}}{|Df|((0,1))}.
\]
This sharp error equals the total variation distance (the supremum over measurable events) between an exponential-one law and its convolution with the compound-Poisson sum \(Y_t\) of a Poisson\((t)\) number of independent exponential-one variables. Let \(a_t\) be the unique positive root of \(e^{-t}I_0(2\sqrt{ta_t})=1\), where \(I_0\) is the modified Bessel function. The complete nonconstant equality class is
\[
f=c+d\,\mathbf1_{(s_t,1)},\qquad s_t=e^{-a_t},\quad c,d\in\mathbb R,\ d\ne0
\]
up to almost-everywhere equality. The sharp error is
\[
C(t)=\int_{s_t}^1\!\big[1-e^{-t}I_0(2\sqrt{t\log(1/u)})\big]du=\Pr(Y_t>a_t).
\]
Its short- and large-time behavior is
\[
\begin{aligned}
a_t&=1+t/4+O(t^2),& C(t)&=t/e-t^2/(4e)+O(t^3) &&(t\downarrow0),\\
a_t&=t/4+\tfrac14\log(2\pi t)+O((\log t)^2/t),& 1-C(t)&\sim 2(2\pi t)^{-1/4}e^{-t/4} &&(t\to\infty).
\end{aligned}
\]
In particular, the large-time maximizing jump is asymptotic to \((2\pi t)^{-1/4}e^{-t/4}\), and the deficit is asymptotic to twice its distance from the left endpoint. This concerns the identity-approximation error for a real \(BV\) domain and Lebesgue output measure, not an ordinary \(L^1\) operator norm. At \(t=0\) the error is zero and the uniqueness statement does not apply.

## Proof

Each Hardy application acts by replacing \(x\) by \(xU\) for independent uniform \(U\in(0,1)\); Poisson mixing shows \(P_tf(x)=\mathbb E f(xe^{-Y_t})\). This follows from the exponential series on bounded functions, which includes \(BV(0,1)\). For a step \(h_s=\mathbf1_{(s,1)}\), its error is nonnegative pointwise, with integrated defect
\[
E_t(s)=\mathbb E[\min(1,se^{Y_t})-s].
\]
For independent uniform \(X\in(0,1)\), the law of \(Xe^{-Y_t}\) has distribution function \(s+E_t(s)\) on the interval and density \(W_t(-\log s)\), where
\[
W_t(a)=\mathbb E[e^{Y_t}\mathbf1_{\{Y_t<a\}}]=e^{-t}\sum_{m\ge0}\frac{(ta)^m}{(m!)^2}=e^{-t}I_0(2\sqrt{ta})\qquad (a>0).
\]
The sum conditions on the Poisson count and integrates the resulting gamma densities, including the mass \(e^{-t}\) at zero. Thus \(E_t'(s)=W_t(-\log s)-1\) decreases strictly in \(s\) from positive infinity to \(e^{-t}-1\); there is exactly one maximizing step, at \(s_t\). The set on which the density of \(Xe^{-Y_t}\) exceeds that of \(X\) is \((0,s_t)\), so the maximum difference of probabilities is \(E_t(s_t)\). Under the change of variables \(x\mapsto-\log x\) this is the asserted total variation. Integrating the derivative of \(E_t\) from \(s_t\) to 1 yields the integral formula; splitting the expected minimum at \(Y_t=a_t\) and using \(W_t(a_t)=1\) yields \(E_t(s_t)=\Pr(Y_t>a_t)\).

Writing \(f=c+\int h_s\,d\mu(s)\) almost everywhere, with \(\mu=Df\) a finite signed measure on the open interval, gives
\[
\|f-P_tf\|_1\le\int E_t(s)\,d|\mu|(s)\le E_t(s_t)|\mu|((0,1)).
\]
The integral representation and Fubini apply since the steps are bounded and the measure is finite. A jump at \(s_t\) attains the bound. Strictness of the maximum forces all variation of an equality function to be supported at \(s_t\), giving exactly the stated affine family of jumps.

At small \(t\), divide the root equation \(I_0(2\sqrt{ta})=e^t\) after subtraction of 1 by \(t\). The resulting analytic equation is \(a-1+t(a^2/4-1/2)+O(t^2)=0\). Its derivative in \(a\) at \((t,a)=(0,1)\) is 1, so the unique root satisfies \(a_t=1+t/4+O(t^2)\). On a bounded range of \(a\) around one, expanding \(W_t\) and integrating gives
\[
E_t(e^{-a})=\int_0^a e^{-v}(1-W_t(v))\,dv=e^{-a}\big[ta+t^2(a^2/4-a/2)\big]+O(t^3).
\]
Since \(a e^{-a}\) is stationary at 1, the expansion of \(C(t)\) follows.

For large \(t\), set \(z_t=2\sqrt{ta_t}\). From \(I_0(z)=e^z(2\pi z)^{-1/2}(1+O(z^{-1}))\) on the positive real axis, first \(z_t/t\to1\), then \(z_t=t+\tfrac12\log(2\pi t)+O((\log t)/t)\). Squaring and dividing by \(4t\) gives the claimed location. For the prefactor, let \(A\sim\operatorname{Poisson}(t)\) and \(B\sim\operatorname{Poisson}(a_t)\) be independent. Realize \(Y_t\) as the \(A\)-th arrival time of a separate unit-rate Poisson process, at time zero if \(A=0\), and take \(B\) as its count by time \(a_t\). Then \(1-C(t)=\Pr(A\le B)\). From the two Poisson mass formulas, for integer \(k\ge0\),
\[
\Pr(B-A=k)=e^{-t-a_t}(a_t/t)^{k/2}I_k(z_t),
\]
where \(I_k\) is the modified Bessel function of order \(k\). The tie probability is exactly \(e^{-a_t}\) by the root equation. For fixed \(k\), \(I_k(z_t)/I_0(z_t)\to1\); this follows from the Fourier integral of \(e^{z_t\cos\theta}\) against \(\cos(k\theta)\), normalized by its integral, since that measure concentrates near \(\theta=0\). The ratio has absolute value at most 1. Since \(a_t/t\to1/4\), the sum over \(k\ge0\) after division by the tie probability has terms dominated by \((2/3)^k\) for sufficiently large \(t\); its limit is \(\sum_{k\ge0}2^{-k}=2\). This gives the asymptotic prefactor, not only the exponential rate.

## Relationship to prior work and scope

The **scalar threshold and exact error** have a classical equivalent in equal-prior noncoherent on–off keying in additive Gaussian noise. For example, the Technical University of Munich teaching material [*Coherent and Non-Coherent On-Off Keying*, §2.3](https://en.lntwww.lnt.ei.tum.de/Applets:Coherent_and_Non-Coherent_On-Off_Keying) gives the Rayleigh/Rice densities, the two error integrals and the optimal threshold at the density intersection. With Gaussian component variance \(\sigma^2\), nonzero signal amplitude \(M\), and received envelope \(\eta\), set \(t=M^2/(2\sigma^2)\) and \(y=\eta^2/(2\sigma^2)\). Their two densities transform into \(e^{-y}\) and \(e^{-y}W_t(y)\), exactly the two laws in the total variation formula above. The density intersection is the Bessel root and the optimal average error is \((1-C(t))/2\). No originality is claimed for this scalar testing problem, its threshold equation, or its exact error characterization.

The [fixed-iterate BV calculation](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-exact-bounded-variation-error-of-iterated-ces-ro-averaging--fa8ba69dbe73/RESULT.md) gives sharp step errors for individual \(H^m\), with maximizing location \(\exp[-(m!)^{1/m}]\). This does not give equality for the Poisson mixture by averaging those sharp values: even \(m=1,2\) require different jumps and both have positive weights. Arvanitidis and Siskakis ([arXiv:1006.1520](https://arxiv.org/abs/1006.1520)) study dilation semigroups and analytic Hardy-space Cesàro operators rather than this real \(BV\) norm problem. Belli, Gül, Ross and Siskakis ([DOI](https://doi.org/10.1007/s00020-026-02865-7)) use a different, nonconstant-preserving kernel. The contribution assessed here is the reduction of the sharp Hardy identity error to the testing distance, the resulting full BV extremizer classification, and the quantitative jump/deficit asymptotics. A bounded comparison does not exclude an earlier equivalent sharp asymptotic from the detection literature.

The accompanying `checker.py` provides finite numerical comparisons between the step-defect integral and its Poisson-mixture representation; it is not needed for the proof or for either limiting statement.
