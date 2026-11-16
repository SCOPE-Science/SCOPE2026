# The exact centered half-frequency zero-count law for three-line Gaussian spectrograms

## Finding
Consider three equally spaced independent Gaussian spectral lines and their Gaussian-window short-time Fourier transform (STFT). The complete law of the number of zeros on the lower side of the *intrinsic balanced frequency*, in one fundamental time cylinder, is exactly a three-point distribution. Let
\[
\beta=\frac{a_1^2}{a_0a_2}e^{2\pi\Delta^2}>0,
\qquad q_\beta=\sqrt{\frac{\beta}{\beta+2}}.
\]
Then almost surely there are exactly two simple zeros per cylinder and no zero on the balanced line, while the lower-half-cylinder count \(N\in\{0,1,2\}\) satisfies
\[
\boxed{\mathbb P(N=0)=\mathbb P(N=2)=\frac{1-q_\beta}{2},\qquad
\mathbb P(N=1)=q_\beta.}
\]
In particular,
\[
\mathbb E N=1,\qquad \operatorname{Var}(N)=1-q_\beta.
\]
The variance decreases strictly from \(1\) to \(0\) across the positive middle-line power range; its precise limits are \(q_\beta\sim\sqrt{\beta/2}\) as \(\beta\downarrow0\) and \(1-q_\beta\sim1/\beta\) as \(\beta\to\infty\). The full count law is analytic for every \(\beta>0\); notably it has no singularity at \(\beta=4\), where the *expected* zero intensity has a known unimodal-to-bimodal transition [2].

## Assumptions and scope
Let \(\Delta>0\) and \(\nu_0\in\mathbb R\). Let \(a_0,a_1,a_2>0\), and let \(Z_0,Z_1,Z_2\) be independent circular complex Gaussians with \(\mathbb E|Z_j|^2=1\). Define
\[
f(t)=\sum_{j=0}^2a_jZ_j e^{2\pi i(\nu_0+j\Delta)t},\quad
g(t)=e^{-\pi t^2},\quad
V_g f(x,\omega)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\omega t}\,dt.
\]
This finite random Fourier series is a smooth stationary Gaussian process with a *purely atomic* spectral measure; it is not required to lie in \(L^2(\mathbb R)\). The STFT integral converges absolutely. Put
\[
\mu=\nu_0+\Delta+\frac{\log(a_0/a_2)}{4\pi\Delta}.
\]
In the half-open temporal cylinder \(0\le x<1/\Delta\), define \(N\) as the number of distinct zeros satisfying \(\omega<\mu\). The endpoint convention counts each time-periodic zero exactly once. All zero statements, including simplicity and absence from \(\omega=\mu\), hold almost surely. A zero of the complex STFT is equivalently a zero of its squared modulus; the latter vanishes to higher order, so multiplicity throughout means analytic multiplicity of the reduced polynomial or real-transverse simplicity of the complex STFT.

## Proof
**1. Exact reduction to a balanced random quadratic.** Completing the square in the Gaussian integral gives
\[
V_gf(x,\omega)=e^{-\pi(\omega-\nu_0)^2}e^{-2\pi i(\omega-\nu_0)x}
\left(A+Bz+Cz^2\right),
\]
where
\[
z=e^{2\pi\Delta(\omega-\nu_0)+2\pi i\Delta x},\quad
A=a_0Z_0,\quad B=a_1e^{-\pi\Delta^2}Z_1,\quad C=a_2e^{-4\pi\Delta^2}Z_2.
\]
The prefactor is nowhere zero. Put \(r=\sqrt{a_0/a_2}e^{2\pi\Delta^2}\) and \(u=z/r\). Dividing the polynomial by \(a_0\) gives precisely
\[
P(u)=Z_0+\sqrt{\beta}Z_1u+Z_2u^2.
\]
Also, \(\log r/(2\pi\Delta)+\nu_0=\mu\). Thus frequency \(\omega<\mu\) is equivalent to \(|u|<1\). For nonzero simple polynomial roots, the exponential map from one temporal period and the real frequency axis to \(\mathbb C\setminus\{0\}\) is bijective (with angular endpoint identified), so \(N\) is exactly the number of roots of \(P\) in the open unit disk. The conditions \(Z_0Z_2=0\), vanishing discriminant, or a unit-circle root each have probability zero by absolute continuity and analytic/algebraic nondegeneracy. Thus the total count is two almost surely.

**2. A root-count criterion with a direct Rouché proof.** Fix a quadratic \(P(u)=A+Bu+Cu^2\) without boundary zeros and put
\[
d=|C|^2-|A|^2,\qquad D=B\overline C-A\overline B,
\qquad P^*(u)=u^2\overline{P(1/\overline u)}=\overline C+\overline Bu+\overline Au^2.
\]
The exact identity
\[
\overline C\,P(u)-A P^*(u)=u(D+du)
\]
holds. On \(|u|=1\), \(|P^*(u)|=|P(u)|\). If \(|C|>|A|\), Rouché's theorem therefore says that \(P\) and \(u(D+du)\) have the same number of roots in the unit disk. Hence \(N=2\) when \(|D|<d\), and \(N=1\) when \(|D|>d\). If \(|A|>|C|\), the same comparison instead equates the root counts of \(P^*\) and \(u(D+du)\). The reversed polynomial has \(2-N\) disk roots, so \(N=0\) for \(|D|<-d\), and \(N=1\) for \(|D|>-d\). Degeneracies have Gaussian probability zero. Altogether,
\[
\boxed{N=1\ \Longleftrightarrow\ |D|>|d|.}
\]
This derivation includes all sign cases without invoking a black-box stability classification.

**3. Gaussian orthogonalization and an exact scalar integral.** Take \(A=Z_0\), \(C=Z_2\), \(B=\sqrt{\beta}Z_1\) as above. Conditional on \(B=be^{i\theta}\), with \(b\ge0\), rotational symmetry allows the iid Gaussian endpoints to be replaced by \(A'=Ae^{-2i\theta}\) and \(C\). Thus \(|D|=b|\overline C-A'|\) and \(d=|C|^2-|A'|^2\). The orthogonal combinations
\[
X=\overline C-A',\qquad Y=\overline C+A'
\]
are independent circular complex Gaussians of variance \(2\), and \(d=\operatorname{Re}(X\overline Y)\). Conditional on any \(X\ne0\), the real variable \(T=\operatorname{Re}(X\overline Y)/|X|\) is standard normal, independent of \(b\). Therefore
\[
N=1\quad\Longleftrightarrow\quad |T|<b.
\]
Because \(|B|^2\) is exponential with mean \(\beta\), its conditional survival probability at \(t^2\) is \(e^{-t^2/\beta}\). Consequently
\[
\mathbb P(N=1)=\mathbb E_{T\sim\mathcal N(0,1)}e^{-T^2/\beta}
=\frac{1}{\sqrt{1+2/\beta}}=q_\beta.
\]
Reversal \((A,B,C)\mapsto(\overline C,\overline B,\overline A)\) preserves the coefficient law and exchanges inside/outside roots, so \(\mathbb P(N=0)=\mathbb P(N=2)\). Since these probabilities sum to \(1-q_\beta\), the stated distribution follows. Its moments and strictly decreasing variance are immediate, and its elementary asymptotic expansions establish the endpoint laws.

## Verification
The standalone `verify.py` (Python standard library only) checks the disk-root classification against direct complex quadratic roots for 9,000 independent random coefficient triples, the exact Gaussian-STFT cancellation at all sampled polynomial roots, the unequal-amplitude normalization in 2,700 further random cases, and Monte Carlo root-count probabilities at four middle-line scales. Running `python verify.py` printed `THREE_LINE_HALF_STRIP_CHECKS_PASSED 451910`. The proof above, not randomized finite sampling, establishes the universal formulas. The check is reproducible using only the bundled source file.

## Relationship to prior work
Escudero, Koliander and Romero [1] provide expected Gaussian-spectrogram zero counts and spatial first-intensity formulas for colored stationary noise. Their accessible abstract does not provide the finite-period three-line joint root-count law. A fully inspected public three-line calculation [2] gives an exact one-point expected zero-intensity profile and a sharp modality threshold \(\beta=4\), but explicitly limits itself to expected intensity, not the number of zeros in each realization. Its expected cumulative count at the balanced frequency equals one; that **mean** does not determine the probabilities derived here. A fully inspected two-line calculation [3] has one zero per period, so it cannot imply the present three-point random count on a half-cylinder. The general complex-Gaussian polynomial zero statistics of Forrester and Honner [4] are relevant older background: a general two-point density could in principle be integrated to produce a degree-two disk-count law, but the accessible abstract does not settle the exact present parameterized formula. The contribution claimed is only this explicit three-line centered-half-frequency distribution, its strict variance law, and its contrast with the previously published first-intensity bifurcation—not the Schur reduction, Gaussian angular invariance, or earlier intensity results.

## Limitations
The result concerns three equally spaced spectral atoms with independent circular Gaussian coefficients; no absolutely continuous broadband component, four-line input, nonlinear window, or arbitrary unequal spacing is covered. The specific frequency boundary \(\mu\) is the intrinsic balance point of the outer powers, not an arbitrary physical frequency threshold. Its count law is an exact finite-cylinder property, not an ergodic limit theorem. Full text of [1] and [4] was not accessible during this comparison, leaving a residual older-equivalence and publication-priority risk. The elementary proof does not assert novelty of its classical Rouché or Gaussian identities. Independent external validation has not been performed.

## References
1. L. A. Escudero, G. Koliander and J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689, first posted 2026-09-16, https://arxiv.org/abs/2609.18689.
2. *Exact modal bifurcation of three-line Gaussian spectrogram zeros*, public full result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-modal-bifurcation-of-three-line-gaussian-spectrogram-zeros--106a484313d3/RESULT.md.
3. *Exact zero-count laws and non-self-averaging for two-line Gaussian spectrograms*, public full result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-zero-count-laws-and-non-self-averaging-for-two-line-gaussi--6079d35cb6de/RESULT.md.
4. P. J. Forrester and G. Honner, *Exact statistical properties of the zeros of complex random polynomials*, Journal of Physics A 32 (1999), 2961, https://doi.org/10.1088/0305-4470/32/16/006.
