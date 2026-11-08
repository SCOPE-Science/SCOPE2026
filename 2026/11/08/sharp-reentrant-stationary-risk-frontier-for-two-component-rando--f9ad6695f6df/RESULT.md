# Sharp reentrant stationary-risk frontier for two-component random reshuffling

## Finding

Fix \(a>0\), \(g\ne0\), \(0\le\delta<1\), and the two strictly convex scalar losses
\[
f_1(x)=\tfrac12a(1-\delta)x^2+gx,\qquad
f_2(x)=\tfrac12a(1+\delta)x^2-gx.
\]
Their average objective is \(F(x)=ax^2/2\), with minimizer \(0\). Compare constant-step stochastic gradient descent with independent equiprobable index sampling (WR) against random reshuffling (RR), which independently chooses one of the two permutations each epoch, using exactly two individual gradients per epoch. Observe the last iterate after each complete epoch, not an average of iterates.

Put \(t=\eta a\), \(z=\delta^2\), and restrict to the **common mean-square stable stepsize interval** \(0<t<2/(1+z)\). For the normalized iterate \(Y=ax/g\), the limiting second moments at epoch endpoints exist from every deterministic start and equal
\[
M_{\rm WR}=\frac{t^2}{1-S},\qquad
M_{\rm RR}=t^4\left(\frac{z}{(1-p)^2}+\frac{1}{1-p^2}\right),
\]
where \(S=1-2t+(1+z)t^2\) and \(p=1-2t+(1-z)t^2\). The limiting expected objective loss for either method is \(g^2M/(2a)\).

Their relative risk has the exact sign law
\[
\frac{M_{\rm RR}}{M_{\rm WR}}-1
=\frac{2P_z(t)}{[2-(1-z)t]^2[2-2t+(1-z)t^2]},
\]
with strictly positive denominator in the given domain and
\[
\begin{aligned}
P_z(t)={}&z(1-z)^2t^4+(1-z)(1-3z)t^3\\
&+(-2z^2+5z-5)t^2+(8-2z)t-4.
\end{aligned}
\]

There is one critical \(z_*\in(0,1)\), precisely the root in \((315/1000,316/1000)\) of
\[
R(z)=224z^7+896z^6+96z^5-3405z^4+1956z^3+350z^2-148z-17,
\]
with \(z_*=0.31514695318455168085\ldots\), \(\delta_*=\sqrt{z_*}=0.561379509052968\ldots\), and component-curvature ratio \((1+\delta_*)/(1-\delta_*)=3.559750493374743\ldots\). The exact **reentrant comparison** is:

- If \(0<z<z_*\), there are exactly two simple roots \(1<t_-(z)<t_+(z)<2/(1+z)\) of \(P_z\). RR has **larger** stationary expected loss exactly for \(t_-(z)<t<t_+(z)\), ties at the endpoints, and has **smaller** loss everywhere else in the common stable interval.
- If \(z=z_*\), those roots coalesce at one double root \(t_*=1.1683576417711635\ldots\). RR has smaller loss except for equality at \(t=t_*\).
- If \(z>z_*\), RR has strictly smaller stationary loss at every common stable positive step.
- In the equal-curvature case \(z=0\), RR ties WR only at \(t=1\), is better for \(0<t<1\), and is worse for \(1<t<2\).

The reversals occur even with strictly convex component losses: for \(a=g=1\), \(\delta=1/2\), and \(t=6/5\),
\[
M_{\rm RR}=\frac{5364}{2057}>\frac{12}{5}=M_{\rm WR}.
\]
Thus the risk increase of RR over WR in this example is exactly \(2136/10285\), even though the two individual update slopes are \(2/5\) and \(-4/5\), both strictly contractive in absolute value.

## Assumptions and scope

The two component indices each have probability \(1/2\); WR samples independently at every individual gradient update. RR draws a new independent uniform permutation at every two-step epoch. Gradients are exact, the stepsize is fixed, components have strictly positive scalar curvature, and the comparison concerns the limiting expected **last-iterate** loss after complete epochs. The normalized functions and time step cover any such two-component scalar quadratic pair after translating the mean minimizer to zero, scaling the mean curvature to \(a\), and assuming opposite nonzero gradients there. Results do not concern optimization rates for averaged iterates or tuned diminishing stepsizes. Both methods are mean-square stable on the stated open interval; no assertion about their relative finite-epoch losses is needed.

## Proof

Write \(q_1=1-t(1-\delta)\) and \(q_2=1-t(1+\delta)\). The two normalized individual-gradient updates are \(Y\mapsto q_1Y-t\) and \(Y\mapsto q_2Y+t\). Under WR, the mean evolves as \(\mathbb E Y_{j+1}=(1-t)\mathbb E Y_j\); its second moment has the exact recursion
\[
\mathbb E Y_{j+1}^2=S\mathbb E Y_j^2+t^2-2t^2\delta\,\mathbb E Y_j.
\]
Since \(0<t<2/(1+z)\), \(0\le S<1\), and \(|1-t|<1\), so the mean tends to zero and the second moment tends to \(t^2/(1-S)\).

Under RR, one complete epoch is \(Y_{k+1}=pY_k+\xi_k\), with \(p=q_1q_2\) and independent equiprobable offsets \(\xi_k=t^2(1+\delta)\) or \(t^2(\delta-1)\). Therefore \(\mathbb E\xi_k=t^2\delta\) and \(\operatorname{Var}(\xi_k)=t^4\). As \(|p|\le S<1\), its invariant mean and variance are \(t^2\delta/(1-p)\) and \(t^4/(1-p^2)\), proving the exact moment formulas. Direct reduction gives the displayed rational difference with strictly positive denominator.

For \(z=0\), \(P_0(t)=(t-1)(t-2)^2\). Suppose \(0<z<1\). We have
\[
P_z(1)=z^2(z-1)<0,\qquad
P_z\!\left(\frac2{1+z}\right)=-\frac{16z^2(1-z)^2}{(1+z)^4}<0.
\]
Moreover, substituting \(t=1/(1+u)\), \(u\ge0\), gives
\[
(1+u)^4P_z\!\left(\frac1{1+u}\right)
=-4u^4-2(z+4)u^3-(2z^2+z+5)u^2-(z^2+1)u+z^2(z-1)<0.
\]
Thus only \(1<t<2/(1+z)\) can contain a reversal.

Map that open interval to \(u>0\) using \(u=(t-1)/(2/(1+z)-t)\). The transformed polynomial \((1+z)^4(1+u)^4P_z((1+2u/(1+z))/(1+u))=\sum_{j=0}^4A_j(z)u^j\) has coefficients, in increasing order,
\[
\begin{aligned}
A_0&=z^2(z-1)(1+z)^4,\\
A_1&=(z-1)(1+z)^3(7z^2-1),\\
A_2&=(1-z)(1+z)^2(2z^3-19z^2+4z+1),\\
A_3&=2z(1-z)(1+z)(5z^2-10z+1),\\
A_4&=-16z^2(1-z)^2.
\end{aligned}
\]
The sign changes in this sequence (zero coefficients omitted) are at most two. Indeed, the three internal coefficients switch from positive to negative in the order \(A_3\), \(A_2\), \(A_1\), at respectively \(1-2/\sqrt5\), the unique root of \(2z^3-19z^2+4z+1\) in \((0,1)\), and \(1/\sqrt7\); these numbers are strictly increasing. Descartes' rule therefore bounds the number of positive roots, counted with multiplicity, by two. Once \(z\ge1/\sqrt7\), all five coefficients are nonpositive, with negative endpoints, and there are no positive roots.

Eliminating \(t\) between \(P_z(t)\) and \(\partial_tP_z(t)\) gives the exact resultant
\[
\operatorname{Res}_t(P_z,\partial_tP_z)=-4z^3(z-1)^4R(z).
\]
An exact rational Sturm computation finds precisely two simple roots of \(R\) in \((0,1)\), isolated respectively in \((315/1000,316/1000)\) and \((819/1000,820/1000)\). One reproducible certificate is that the Sturm sign variation counts at \(0,315/1000,316/1000,819/1000,820/1000,1\) are \(4,4,3,3,2,2\). The second root is beyond \(1/\sqrt7\), where positivity is impossible, so the **only** possible root-count transition within the active region occurs at \(z=z_*\). Exact rational Sturm counts on \(1<t<2/(1+z)\) are two at \(z=1/4\) and zero at \(z=1/3\). The boundary evaluations above prevent roots entering or leaving through the interval endpoints. Consequently the number of positive roots is exactly two below \(z_*\), zero above it, and a single double root at \(z_*\) (by the at-most-two multiplicity bound). The sign of \(P_z\) is negative at both endpoints of the interval, hence it is positive only between the two simple roots, and nonpositive with one zero at tangency. This establishes every case.

## Verification

The accompanying `verify.py` uses exact rational/SymPy arithmetic to verify the affine epoch maps, moment-risk factorization, change-of-variables coefficients, resultant, Sturm counts and rational witness. It also checks the asserted sign on several exact rational parameter pairs. The polynomial proof is independent of floating-point output; decimal thresholds are only approximations to the exact isolated roots. Invoke `python verify.py` with Python 3 and SymPy installed.

## Relationship to prior work

Ying, Yuan, Vlaski and Sayed (2018) derive constant-step random-reshuffling steady-state formulas, including an exact common-Hessian quadratic example, and the favorable small-step scaling. Their common-Hessian least-squares model has state-independent gradient noise; the different-curvature components here instead yield state-dependent noise and a different exact stationary formula. Domingo-Enrich (2022) studies stationary noise spectra for SGD, reshuffling and shuffle-once under a shared-Hessian/noise approximation; its ordered variance conclusions are approximation- and stepsize-regime-dependent, not the complete large-step exact two-component comparison. De Sa (2020) gives broader counterexamples to universal reshuffling superiority; the **existence of a reversal** is therefore not novel. The distinctive finding here is the exact two-root reentrant interval, its disappearance at an explicit degree-seven algebraic threshold, and the resulting curvature-ratio frontier. Safran and Shamir (2021) provide convergence comparisons and lower bounds rather than this exact stationary last-iterate classification. Liu (2026) analyzes convergence rates for averaged iterates under bounded stepsizes; those comparisons do not assert the exact stationary last-iterate ordering on this aggressive-step interval. A specialized earlier exact computation cannot be ruled out solely by these searches.

## Limitations

The theorem concerns only two scalar convex quadratic summands with balanced opposite optimum gradients, equal sampling weights and independent fresh shuffles. It is not a worst-case guarantee for arbitrary data, higher dimensions, adaptive steps or averaged iterates. It does not establish a universal advantage of either sampling method outside the common mean-square stable interval, and finite-epoch transients may have different orderings. Independent specialist validation and a complete publication-priority audit have not been performed.

## References

1. B. Ying, K. Yuan, S. Vlaski and A. H. Sayed, *Stochastic Learning under Random Reshuffling with Constant Step-sizes*, arXiv:1803.07964 (first version March 21, 2018), https://arxiv.org/abs/1803.07964.
2. C. Domingo-Enrich, *Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis*, arXiv:2206.00632 (first version June 1, 2022), https://arxiv.org/abs/2206.00632.
3. C. De Sa, *Random Reshuffling is Not Always Better*, NeurIPS 2020, https://papers.neurips.cc/paper_files/paper/2020/file/42299f06ee419aa5d9d07798b56779e2-Paper.pdf.
4. I. Safran and O. Shamir, *Random Shuffling Beats SGD Only After Many Epochs on Ill-Conditioned Problems*, arXiv:2106.06880 (2021), https://arxiv.org/abs/2106.06880.
5. Z. Liu, *Random Reshuffling Dominates Stochastic Gradient Descent*, arXiv:2606.32005 (2026), https://arxiv.org/abs/2606.32005.
