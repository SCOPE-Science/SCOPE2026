# A Bessel detuning law for vertical-translation commutators of Dirichlet-series composition operators

## Finding

Let \(\mathcal H^2\) be the Hardy–Hilbert space of Dirichlet series with square-summable coefficients, and let \(U_\tau f(s)=f(s+i\tau)\). Fix \(a>0\) and \(c>a\), both real, and put
\[
\psi_c(s)=s+c+a2^{-s},\qquad A_{c,\tau}=U_\tau C_{\psi_c}-C_{\psi_c}U_\tau.
\]
Write \(\theta=\tau\log2\), interpreted modulo \(2\pi\). Then \(A_{c,\tau}\) is compact for every such \(c,\tau\), and the following assertions hold.

1. **Exact commutation and Hilbert–Schmidt boundary.** If \(\theta\in2\pi\mathbb Z\), then \(A_{c,\tau}=0\). Otherwise
\[
A_{c,\tau}\in\mathcal S_2\quad\Longleftrightarrow\quad c>a+\tfrac12.
\]
2. **Exact Hilbert–Schmidt formula.** For \(c>a+1/2\), with \(I_0\) the modified Bessel function,
\[
\|A_{c,\tau}\|_{\mathcal S_2}^{2}
=2\sum_{n=2}^{\infty}n^{-2c}
\left[I_0(2a\log n)-\operatorname{Re}I_0(2a(\log n)e^{i\theta/2})\right].
\]
3. **Nonresonant critical blow-up.** For each fixed \(\theta\notin2\pi\mathbb Z\), as \(\varepsilon\downarrow0\),
\[
\sqrt\varepsilon\,\|A_{a+1/2+\varepsilon,\tau}\|_{\mathcal S_2}^{2}
\longrightarrow \frac1{\sqrt{2a}}.
\]
4. **Near-resonant detuning.** If the translation parameter varies so that \(\tau_\varepsilon\log2=\varepsilon v\), for fixed \(v\in\mathbb R\), then
\[
\boxed{\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,
\|A_{a+1/2+\varepsilon,\tau_\varepsilon}\|_{\mathcal S_2}^{2}
=\frac1{\sqrt a}\left[\frac1{\sqrt2}-\operatorname{Re}(2-iav)^{-1/2}\right].}
\]
The principal square root is intended. This even, strictly increasing function of \(|v|\) vanishes at \(v=0\) and approaches \(1/\sqrt{2a}\) as \(|v|\to\infty\). These are separate assertions for fixed nonresonant phase and finite detuning; no uniform claim is made for arbitrary simultaneous phase sequences.

## Assumptions and scope

Precisely,
\[
\mathcal H^2=\left\{f(s)=\sum_{n\ge1}b_n n^{-s}:\sum_{n\ge1}|b_n|^2<\infty\right\},
\qquad \|f\|^2=\sum_{n\ge1}|b_n|^2.
\]
Here \(\{e_n(s)=n^{-s}\}_{n\ge1}\) is orthonormal. The class \(\mathcal S_2\) is the Hilbert–Schmidt ideal. For \(c>a\), the symbol \(\psi_c\) has characteristic one and maps the open right half-plane into itself; the Gordon–Hedenmalm theorem supplies a bounded composition operator. The parameters \(a,c\) are strictly positive real values subject to \(c>a\); the translation parameter is arbitrary real. The theorem concerns this one-prime perturbation and does not assert a multi-prime or general Schatten-\(p\) classification.

## Proof

**1. Compactness and exact columns.** Put \(\delta=c-a>0\) and \(\psi_a(s)=s+a+a2^{-s}\). Then \(C_{\psi_c}=C_{\psi_a}C_{s\mapsto s+\delta}\). The latter factor is diagonal with entries \(n^{-\delta}\) in the Dirichlet basis and is compact; the former is bounded by the composition-symbol criterion, since \(\operatorname{Re}(a+a2^{-s})>0\) in the open right half-plane. Both the composition operator and its commutator with a unitary are therefore compact.

The monomial expansion gives, for every \(n\ge1\),
\[
C_{\psi_c}e_n=n^{-c}\sum_{k\ge0}\frac{(-a\log n)^k}{k!}e_{2^kn},
\]
and hence
\[
A_{c,\tau}e_n=n^{-c-i\tau\log n}
\sum_{k\ge0}\frac{(-a\log n)^k}{k!}
(e^{-ik\theta}-1)e_{2^kn}.
\]
For a fixed input \(n\), the outputs are pairwise orthogonal. Thus
\[
\sum_{n\ge1}\|A_{c,\tau}e_n\|^2
=2\sum_{n\ge2}n^{-2c}\sum_{k\ge0}
\frac{(a\log n)^{2k}}{(k!)^2}(1-\cos(k\theta)).
\]
Using the entire power series \(I_0(z)=\sum_{k\ge0}(z/2)^{2k}/(k!)^2\) yields the announced exact formula, with nonnegative terms before the Bessel rewriting. At \(\theta\in2\pi\mathbb Z\) each coefficient vanishes, and otherwise the \(k=1\) coefficient is nonzero.

**2. Sharp threshold.** For \(x>0\), the standard integral representation of \(I_0\) implies
\[
\left|I_0(2xe^{i\theta/2})\right|\le I_0(2x\cos(\theta/2))
\]
when \(\theta\in[-\pi,\pi]\). If \(\theta\ne0\), the right-hand side has exponential rate strictly below that of \(I_0(2x)\). In particular, as \(x\to\infty\),
\[
I_0(2x)\sim \frac{e^{2x}}{\sqrt{4\pi x}},\qquad
\frac{\operatorname{Re}I_0(2xe^{i\theta/2})}{I_0(2x)}\to0.
\]
The nonresonant contribution from the basis vector \(e_n\) is consequently asymptotic to
\[
\frac{2n^{-2(c-a)}}{\sqrt{4\pi a\log n}}.
\]
The corresponding series converges exactly for \(2(c-a)>1\). This proves the stated necessary and sufficient threshold, including the equality case (where \(\sum n^{-1}/\sqrt{\log n}\) diverges).

**3. Fixed nonresonant phase.** Put \(c=a+1/2+\varepsilon\). The complex-Bessel part of the Hilbert–Schmidt sum remains uniformly bounded as \(\varepsilon\downarrow0\), by the strict exponential-rate gap in step 2. For the positive part, the elementary integral comparison and the Bessel asymptotic yield
\[
\sum_{n\ge2}n^{-1-2\varepsilon}e^{-2a\log n}I_0(2a\log n)
\sim\frac1{\sqrt{4\pi a}}\int_0^\infty e^{-2\varepsilon t}t^{-1/2}\,dt
=\frac1{\sqrt{8a\varepsilon}}.
\]
The factor two in the Hilbert–Schmidt identity gives \(1/\sqrt{2a\varepsilon}\), proving assertion 3.

**4. Detuning concentration.** For \(x>0\) define the integer-valued random variable \(K_x\) by
\[
\mathbb P(K_x=k)=\frac{x^{2k}}{(k!)^2I_0(2x)},\quad k\ge0.
\]
Differentiating the Bessel series, or simply using \(k^2/(k!)^2=1/((k-1)!)^2\), gives the exact moment identities
\[
\mathbb E K_x^2=x^2,\qquad
\mathbb E K_x=x\frac{I_1(2x)}{I_0(2x)}.
\]
Since \(I_1(2x)/I_0(2x)\to1\), we have \(K_x/x\to1\) in mean square. For \(x=a\log n\) and \(u=\varepsilon\log n\) in a fixed compact subset of \((0,\infty)\), this implies \(\varepsilon K_x\to au\) in probability, and the bounded continuous observable \(1-\cos(v\varepsilon K_x)\) converges in mean to \(1-\cos(avu)\).

The positive discrete weights, multiplied by \(\sqrt\varepsilon\), converge under \(u=\varepsilon\log n\) to the measure with density \(e^{-2u}/\sqrt{4\pi a u}\). To justify the endpoint passages, use the global estimate \(e^{-2x}I_0(2x)\le C(1+x)^{-1/2}\), integral comparison for the sums, and \(0\le1-\cos\le2\); the contributions from \(u<\eta\) and \(u>R\) are uniformly controlled by the integrals of \(u^{-1/2}\) near zero and \(e^{-2u}u^{-1/2}\) at infinity. Therefore
\[
\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,
\|A_{a+1/2+\varepsilon,\tau_\varepsilon}\|_{\mathcal S_2}^2
=\frac1{\sqrt{\pi a}}\int_0^\infty
u^{-1/2}e^{-2u}(1-\cos(avu))\,du.
\]
The gamma integral evaluates this to the displayed detuning function. Its strict increase in \(|v|\) follows by differentiating the explicit complex-power expression, or from the elementary polar form of \((2-iav)^{-1/2}\). This completes the proof.

## Verification

The standalone file `CHECK.py` tests 60 finite Bessel-versus-column identities, four exact second-moment identities, and three near-critical numerical comparisons. The asymptotic numerical comparisons use a direct finite sum followed by an integral approximation to the far tail; they are supplementary and cannot certify the infinite assertions. The analytic proof above establishes the infinite summations, precise threshold, and scaling law. Run `python CHECK.py` after installing NumPy and SciPy.

## Relationship to prior work

Bayart–Wang–Yao (first publicly available in 2021) study compact differences and linear combinations of composition operators on the Hardy–Hilbert space of Dirichlet series, including characteristic-one symbols. Bayart–Kouroupis (2023 preprint; 2024 journal publication) establish Schatten criteria largely for characteristic-zero composition symbols. Bayart–Yao (2024) study commutants, including characteristic-one symbols of the form here. These results motivate the quantitative question but the inspected relevant sections do not state a Hilbert–Schmidt translation-commutator threshold or a Bessel detuning profile. A related indexed result on arithmetic rotation detuning of composition–differentiation operators acts on coefficient-weighted analytic Dirichlet spaces rather than this Dirichlet-series Hardy space; its stated profile does not imply the present one.

## Limitations

The theorem is confined to a single perturbation frequency \(2^{-s}\), strictly real \(a>0\), real \(c>a\), and the Hilbert–Schmidt ideal. It does not classify other Schatten exponents, general Dirichlet symbols, or uniform limits along all joint parameter sequences. No claim of independently established historical priority is made; unindexed earlier special-case calculations could exist. Numerical checks do not replace the proof, and independent mathematical validation has not been performed.

## References

- F. Bayart, M. Wang, X. Yao, *Topological structure of the space of composition operators on the Hardy space of Dirichlet series*, arXiv:2109.09581 (first submitted 20 September 2021). https://arxiv.org/abs/2109.09581
- F. Bayart, A. Kouroupis, *Schatten class composition operators on the Hardy space of Dirichlet series and a comparison-type principle*, arXiv:2306.05733 (first submitted 9 June 2023). https://arxiv.org/abs/2306.05733
- F. Bayart, X. Yao, *Königs maps and commutants of composition operators on the Hardy-Hilbert space of Dirichlet series*, arXiv:2406.19737 (first submitted 28 June 2024). https://arxiv.org/abs/2406.19737
- F. Bayart, M. Wang, X. Yao, *Linear combinations of composition operators with linear symbols on a Hilbert space of Dirichlet series*, Journal of Operator Theory **86** (2021), 231–251. https://www.mathjournals.org/jot/2021-086-001/2021-086-001-012.html
