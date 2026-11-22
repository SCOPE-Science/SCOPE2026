# Exact peak-sidelobe distribution and a logarithmic Barker boundary for four random Fourier phases

## Finding
Let \(a_0,a_1,a_2,a_3\) be independent Haar-uniform complex numbers of modulus one. Define their positive-lag aperiodic autocorrelations by
\[
c_k=\sum_{j=0}^{3-k}a_{j+k}\overline{a_j},\qquad k=1,2,3,
\]
and their unnormalized peak sidelobe by \(R=\max_{1\le k\le3}|c_k|\). Then \(R\) is supported on \([1,3]\), with an atom of mass
\[
\boxed{\Pr\{R=1\}=\frac5{36}}.
\]
For \(1\le s<3\), define \(a=(s-1)/2\), \(b=\min\{1,s/2\}\), and \(G(t)=1/2+\arcsin(\max\{-1,\min\{1,t\}\})/\pi\). Its entire distribution is
\[
\boxed{\Pr\{R\le s\}=\frac2\pi\left[\arcsin a+\int_a^b\frac{G\big((s^2-1-4x^2)/(4x)\big)}{\sqrt{1-x^2}}\,dx\right].}
\]
Set the CDF to zero when \(s<1\), and to one when \(s\ge3\). The atom is followed by a nonanalytic logarithmic boundary law:
\[
\boxed{\Pr\{R\le1+\varepsilon\}=\frac5{36}+\frac{\varepsilon}{\pi^2}\log\frac1\varepsilon+O(\varepsilon)\quad(\varepsilon\downarrow0).}
\]
There is also an exact joint probability density for the squared first two sidelobes \(U=|c_2|^2\), \(V=|c_1|^2\):
\[
f_{U,V}(u,v)=\frac{1}{\pi^2\sqrt{u(4-u)}\sqrt{4u-(v-1-u)^2}}
\]
for \(0<u<4\) and \((1-\sqrt u)^2<v<(1+\sqrt u)^2\), and zero outside that region. Values on boundary sets do not affect the density. The deterministic last sidelobe obeys \(|c_3|=1\).

## Assumptions and scope
The coefficients are four independent continuous Haar phases, not finite-alphabet phases, Gaussian coefficients, correlated multiplicative coefficients, or phases conditioned to have a prescribed sum. The correlation is *aperiodic*, unnormalized, and taken at positive lags; negative lags have the same moduli. The Fourier polynomial \(P(z)=\sum_{j=0}^3 a_jz^j\) on the unit circle has these autocorrelations as the positive Fourier coefficients of \(|P|^2\). The result gives the joint law of the two nonconstant free squared sidelobes and hence the exact distribution of their maximum with the fixed final sidelobe. The \(O(\varepsilon)\) bound is for positive \(\varepsilon\) tending to zero; no rate is asserted uniformly in sequence length because the length is fixed at four.

## Proof
**1. Haar reduction.** Write \(a_j=e^{i\theta_j}\) with independent uniform angles and \(\delta_j=\theta_{j+1}-\theta_j\) modulo \(2\pi\), \(j=0,1,2\). The map from \((\theta_0,\theta_1,\theta_2,\theta_3)\) to \((\theta_0,\delta_0,\delta_1,\delta_2)\) is a determinant-one torus automorphism, so the three differences are independent Haar angles. Directly,
\[
c_1=e^{i\delta_0}+e^{i\delta_1}+e^{i\delta_2},\qquad
c_2=e^{i\delta_1}(e^{i\delta_0}+e^{i\delta_2}),\qquad |c_3|=1.
\]
Put \(X=|\cos((\delta_0-\delta_2)/2)|\). The random variable \(X\in(0,1)\) has density \(2/(\pi\sqrt{1-x^2})\). The remaining phase \(\delta_1-(\delta_0+\delta_2)/2\), with a possible \(\pi\) correction when the cosine is negative, is independent of \(X\) and uniform; call it \(\Phi\). Hence
\[
|c_2|=2X,\qquad |c_1|^2=1+4X^2+4X\cos\Phi,
\]
with independent \(X\) and \(\Phi\). This also proves the support \([1,3]\), since \(|c_1|\le3\), \(|c_2|\le2\), and \(|c_3|=1\); every value between one and three occurs by continuous phase choices and has positive probability in every compatible open interval.

**2. Joint law.** Set \(U=4X^2\). The change-of-variables formula gives \(f_U(u)=1/(\pi\sqrt{u(4-u)})\) for \(0<u<4\). Conditionally on \(U=u\), \(V=1+u+2\sqrt u\cos\Phi\) has the shifted arcsine density \(1/[\pi\sqrt{4u-(v-1-u)^2}]\) on the stated conditional interval. Multiplying the two densities proves the joint formula, without independence between the sidelobes.

**3. Entire peak distribution.** Given \(X=x\), the event \(R\le s\) requires \(2x\le s\) and \(1+4x^2+4x\cos\Phi\le s^2\). If \(x\le (s-1)/2\), the second condition is automatic; for \((s-1)/2<x\le\min\{1,s/2\}\), its conditional probability is \(G((s^2-1-4x^2)/(4x))\). Integrating against the arcsine density yields the CDF. When \(s=1\) the integral reduces to
\[
\Pr\{R=1\}=\frac2{\pi^2}\int_0^{1/2}\frac{\arccos x}{\sqrt{1-x^2}}\,dx
=\frac2{\pi^2}\int_0^{\pi/6}\left(\frac\pi2-t\right)dt=\frac5{36}.
\]
The equality \(R=1\) has positive mass because the fixed final autocorrelation always has modulus one and the other two can both be at most one.

**4. Logarithmic approach.** Fix any \(\eta\in(0,1/4)\), write \(s=1+\varepsilon\), and compare the preceding conditional-integral formula at \(s\) and one. The interval \(x\in[0,C\varepsilon]\) contributes \(O_C(\varepsilon)\), since its arcsine measure is \(O_C(\varepsilon)\). The upper cutoff moves from \(1/2\) to \((1+\varepsilon)/2\), contributing \(O(\varepsilon)\); contributions on \([\eta,(1+\varepsilon)/2]\) are \(O_\eta(\varepsilon)\) by a bounded derivative. On \([C\varepsilon,\eta]\) with any fixed sufficiently large \(C\), the conditional argument changes from \(-x\) to \(-x+(2\varepsilon+\varepsilon^2)/(4x)\). The smooth arcsine derivative on these arguments and Taylor's theorem give, uniformly,
\[
\frac2{\pi\sqrt{1-x^2}}\left[G\left(-x+\frac{2\varepsilon+\varepsilon^2}{4x}\right)-G(-x)\right]
=\frac{\varepsilon}{\pi^2 x(1-x^2)}+O_\eta\left(\frac{\varepsilon^2}{x^2}\right).
\]
The remainder integrates to \(O_\eta(\varepsilon)\) because the lower endpoint is \(C\varepsilon\). The principal term integrates to \((\varepsilon/\pi^2)\log(1/\varepsilon)+O_\eta(\varepsilon)\), proving the claimed coefficient with an actual uniform error estimate. No simulation or finite enumeration is used to infer the asymptotic.

## Verification
The accompanying `checker.py` uses independent phase samples to compare the original three complex autocorrelations against the two-variable algebraic reduction, and uses deterministic numerical quadrature to evaluate the CDF at six thresholds against a direct 100,000-sample simulation. It checks the exact atom \(5/36\), the range endpoints, and numerical behavior near the logarithmic boundary. Its random generator seed is fixed; it uses Python standard library only. Reproduce with `python3 checker.py`. Simulation and quadrature are consistency tests, not the proof of the universal distribution or asymptotic error bound. `checker_output.txt` records the expected output.

## Relationship to prior work
Katz and van der Linden (first submitted 2021-08-16) study worst-lag autocorrelation bounds for deterministic Golay–Rudin–Shapiro families, including recursions and asymptotic growth; their binary/recursive coefficient model does not imply the continuous-Haar four-chip joint probability law. Borwein and Ferguson study optimal low-autocorrelation *deterministic* polyphase code construction and describe generalized Barker conditions and empirical search statistics, not the Haar-volume of the Barker region or its threshold singularity. Manda and Kumar study cyclic-algorithm design for fixed polyphase families at much longer lengths. Earlier Friese–Zottmann work defines and searches generalized Barker sequences but its accessible abstract does not resolve this probability question. The exact fourth-norm variance and third-centered-moment results for random four-frequency polynomials concern a scalar sum of squared sidelobes; their moments and the scalar distributions do not determine the joint law needed for the peak. Searches also included aliases involving random phase codes, peak sidelobe level, Barker probability and autocorrelation arcsine laws.

## Limitations
The theorem treats exactly four *independent continuous-phase* chips, with no assertion for other lengths, finite phase alphabets, or correlated sequences. The joint density is singular on edges in an integrable way; the peak has an atom at one. The CDF is an exact one-dimensional integral, not a claimed elementary closed form at every threshold. Literature coverage is best-knowledge rather than an assertion of unique priority; a plausible earlier exact treatment in specialist radar/sequence literature may remain unindexed, and full text of certain historical papers was not accessible. Independent mathematical validation has not been performed.

## References
1. D. J. Katz and C. M. van der Linden, *Peak Sidelobe Level and Peak Crosscorrelation of Golay–Rudin–Shapiro Sequences*, arXiv:2108.07318, first publicly submitted 2021-08-16. https://arxiv.org/abs/2108.07318
2. P. Borwein and R. Ferguson, *Polyphase Sequences with Low Autocorrelation*, available full text at https://www.cecm.sfu.ca/~pborwein/PAPERS/P178.pdf
3. R. Manda and P. R. Kumar, *Polyphase Sequences with Good Correlation Properties and Merit Factor Based on Cyclic Algorithm Approach*, 2021, https://doi.org/10.9734/bpi/aaer/v16/6194D
4. M. Friese and H. Zottmann, *Polyphase Barker Sequences up to Length 31*, 1994, https://doi.org/10.1049/el:19941306
5. K.-U. Schmidt, *Sequences with Small Correlation*, 2016, https://arxiv.org/abs/1602.03722
