# Locally Fourier-thick absolutely normal counterexamples to dyadic square-root tail invariance

## Finding

For any \(0<\theta<1/2\), define \(E_\theta\) to be the set of \(t\in(0,1/4)\) for which \(t\), \(t+1/4\), and \(\sqrt{t+1/4}\) are normal to every integer base \(b\ge2\), but the limit of the frequency of the digit one in the binary expansion of \(\sqrt t\) is \(\theta\). Here normality means that every base-\(b\) word of length \(m\) has frequency \(b^{-m}\). For \(A\subset\mathbb R\), write \(kA\) for its \(k\)-fold sumset.

**Theorem.** There are \(\sigma_\theta>0\) and \(k_\theta\in\mathbb N\) such that, for every nonempty open interval \(J\subset(0,1/4)\), a *singular* Borel probability \(\lambda_{\theta,J}\) satisfies
\[\lambda_{\theta,J}(E_\theta\cap J)=1,\qquad |\widehat\lambda_{\theta,J}(\xi)|\le C_{\theta,J}(1+|\xi|)^{-\sigma_\theta}.\]
The set \(k_\theta(E_\theta\cap J)\) has positive Lebesgue measure, and its difference set contains an open neighborhood of zero. The same \(k_\theta\) works for every \(J\), even though \(E_\theta\) itself is Lebesgue null. All its members violate Isaac's tail-invariance condition for the input pair \(t\) and \(t+1/4\).

## Assumptions and scope

The parameter \(\theta\) is fixed strictly between zero and one half. The decay exponent and sumset order depend only on this parameter; the Fourier constant may depend on the interval. Fourier transforms use \(\widehat\lambda(\xi)=\int e^{-2\pi i\xi x}d\lambda(x)\). We do not assert that the sumset itself contains any interval, only its difference set.

## Proof

**Fourier input.** Let \(\mu_\theta\) be the distribution of \(W=\sum_{j\ge1}\varepsilon_j2^{-j}\), where the independent digits satisfy \(\Pr(\varepsilon_j=1)=\theta\). This is a homogeneous, non-atomic self-similar probability: every word of length \(m\) has mass at most \(\max(\theta,1-\theta)^m\). Mosquera–Shmerkin [2, Theorem 3.1] yields an exponent \(\sigma_\theta>0\), independent of the chosen function, such that every \(C^2\) map \(F\colon\mathbb R\to\mathbb R\) with \(F''>0\) has \(|\widehat{F_*\mu_\theta}(\xi)|\le C_F(1+|\xi|)^{-\sigma_\theta}\). Apply this to \(\phi(x)=x^2/4\) and \(\psi(x)=\sqrt{1+x^2}/2\). They are globally strictly convex: \(\phi''=1/2\) and \(\psi''(x)=1/[2(1+x^2)^{3/2}]>0\).

**Simultaneous digit conditions.** By Davenport–Erdős–LeVeque, polynomial Fourier decay gives almost-sure normality to every integer base [2, §1; 1, §4]. Hence \(\phi(W)\) and \(\psi(W)\) are absolutely normal almost surely. Translation by \(1/4\) only changes a Fourier transform's phase, hence \(\phi(W)+1/4\) is also absolutely normal almost surely. The strong law gives binary digit-one frequency \(\theta\) for \(W/2\), because its binary digits are an initial zero followed by the biased digits. Since \(\sqrt{\phi(W)}=W/2\) and \(\sqrt{\phi(W)+1/4}=\psi(W)\), the measure \(\phi_*\mu_\theta\) assigns full mass to \(E_\theta\). All ambiguities of dyadic expansions have measure zero. The two input arguments have the same binary tail from the third digit onward, while their square-root digit frequencies differ.

**Uniform localization.** For nonempty open \(J\subset(0,1/4)\), choose a dyadic word \(w\) of length \(m\) whose interval \(T_w([0,1])\) lies in \(\phi^{-1}(J)\cap(0,1)\). Here \(T_w(x)=\sum_{j=1}^m w_j2^{-j}+2^{-m}x\). Conditioning on this word gives the law \(T_{w*}\mu_\theta\), so define \(\lambda_{\theta,J}=(\phi\circ T_w)_*\mu_\theta\). Both \(\phi\circ T_w\) and \(\psi\circ T_w\) have positive second derivatives on all of \(\mathbb R\); the same source theorem therefore supplies the same exponent \(\sigma_\theta\), uniformly in the word (its constant may vary). The biased digit law and all three absolute-normality claims hold for this conditional law by the preceding argument, so \(\lambda_{\theta,J}(E_\theta\cap J)=1\). It is singular since the set of biased binary frequency \(\theta\ne1/2\) is Lebesgue null, and the maps \(T_w\) and \(\phi\) are Lipschitz on \([0,1]\).

**Additive thickness.** Choose once and for all an integer \(k_\theta\) with \(2k_\theta\sigma_\theta>1\). The Fourier transform of \(\lambda_{\theta,J}^{*k_\theta}\) is \((\widehat\lambda_{\theta,J})^{k_\theta}\), which belongs to \(L^2(\mathbb R)\). Plancherel's theorem for finite measures gives an \(L^2\) density for this convolution. Since each factor has mass one on \(E_\theta\cap J\), the convolution has mass one on the analytic and hence measurable sumset \(k_\theta(E_\theta\cap J)\). Therefore this sumset has positive Lebesgue measure, and Steinhaus's theorem yields a neighborhood of zero in its difference set. Because the Fourier exponent was independent of the word, this one \(k_\theta\) works in every interval.

**Nullity.** The strong-law frequency class \(S_\theta=\{x\in[0,1]:\lim_N N^{-1}\sum_{j\le N}d_j(x)=\theta\}\) has Lebesgue measure zero for \(\theta\ne1/2\), by Borel's normal-number theorem. Each \(t\in E_\theta\) has \(2\sqrt t\in S_\theta\); thus \(E_\theta\subset\phi(S_\theta)\). The Lipschitz map \(\phi\) sends null sets to null sets, so \(E_\theta\) is null. This proves the theorem.

## Verification

The cited nonlinear-image theorem was checked in its primary full text, including the explicit independence of \(\sigma_\theta\) from the function. The two second derivatives and the affine-cylinder compositions satisfy its hypotheses. Fourier normality, the strong law, Plancherel and Steinhaus are invoked in their standard scopes. All quantifiers and the exact \(L^2\) threshold are specified; no finite numerical experiment or computer-generated certificate is used as an infinite proof.

## Relationship to prior work

Stephan [1] disproves Isaac's condition and already remarks that biased dyadic Bernoulli measures give counterexamples of Hausdorff dimension approaching one. Neither that established dimension fact nor the existence of counterexamples is claimed as new. Stephan uses Fourier decay for \(\psi(W)\), the shifted square root, but does not assert absolute normality of the input pair, Fourier decay for \(\phi(W)\), or uniform finite additive thickness of every local exceptional subset. Mosquera–Shmerkin [2] establish the general convex-image Fourier theorem but do not identify this simultaneous square-root-frequency exceptional set. The present result combines these established tools in a new arithmetic-size statement; implicit prior coverage remains possible.

## Limitations

The decay exponent and uniform finite sumset order are not explicitly calculated or proved optimal. The sumset itself may have empty interior; only its difference set is proved to contain an interval. The argument does not establish normality for any specified algebraic square root. It relies on the published Fourier and normality theorems and lacks independent mathematical validation.

## References

[1] R. Stephan, *Isaac's Condition (TU) is false*, arXiv:2610.21899v1, 15 October 2026, §§2,4 and Remark 4.5, https://arxiv.org/pdf/2610.21899 .

[2] C. A. Mosquera and P. S. Shmerkin, *Self-similar measures: asymptotic bounds for the dimension and Fourier decay of smooth images*, Ann. Acad. Sci. Fenn. Math. 43 (2018), 823–834, Theorem 3.1, DOI:10.5186/aasfm.2018.4350 .
