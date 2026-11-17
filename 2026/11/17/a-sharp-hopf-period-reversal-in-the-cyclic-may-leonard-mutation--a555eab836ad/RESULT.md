# A sharp Hopf-period reversal in the cyclic May–Leonard mutation flow

## Finding

For the three-species cyclic competition equations with symmetric all-to-all mutation, the stable cycle born at the coexistence Hopf bifurcation can **speed up or slow down** as the mutation rate decreases. At a fixed total competition strength, the direction is selected by the asymmetry of the two cyclic competition coefficients. The first-order physical-period response has an explicit formula and a sharp feasibility threshold among strictly positive coefficients.

Write \(\sigma=1+\alpha+\beta\), \(\lambda=(\alpha+\beta-2)/2\), and \(w=\sqrt3(\beta-\alpha)/2\). Suppose \(\alpha,\beta>0\), \(\lambda>0\) and \(w\ne0\). Let \(\mu_H=\lambda/(3\sigma)\), and take \(\mu=\mu_H-\delta\), with sufficiently small \(\delta>0\). The positive coexistence equilibrium undergoes a supercritical Hopf bifurcation and a locally unique attracting periodic orbit of least period \(T(\delta)\). Its physical time is the time in the original differential equations, without reparametrization.

Set \(T_H=2\pi\sigma/|w|\). Then

\[
\frac{T(\delta)}{T_H}=1+\mathcal P(\lambda,w)\delta+o(\delta),\qquad
\mathcal P(\lambda,w)=\frac{2\sigma}{\lambda(\sigma+3)}\left(3-\lambda+\frac{\sigma\lambda^2}{w^2}\right),\qquad \sigma=2\lambda+3.
\]

Let \(\lambda_*\) be the unique positive root of

\[
\lambda^3-6\lambda^2-15\lambda-9=0,
\qquad\lambda_*=8.012311970500958\ldots.
\]

If \(0<\lambda\le\lambda_*\), then \(\mathcal P>0\) for **every** positive \(\alpha,\beta\) with \(\beta\ne\alpha\). For \(\lambda>\lambda_*\), both period signs occur for admissible coefficients: the period shrinks with decreasing mutation precisely when

\[
\frac{\sigma\lambda^2}{\lambda-3}<w^2<3(\lambda+1)^2.
\]

Equality in the first inequality is a first-order period-neutral locus; it is not asserted to be exactly isochronous. At \(\lambda=10\), both \(w=16\) and \(w=37/2\) give strictly positive \(\alpha=11-w/\sqrt3\) and \(\beta=11+w/\sqrt3\), with period slopes respectively \(0.35108173076923077\ldots\) and \(-0.04949710625386298\ldots\). Thus both signs occur with the same \(\alpha+\beta=22\) and the same Hopf mutation rate \(\mu_H=10/69\).

## Assumptions and scope

For \(i=1,2,3\), with indices interpreted cyclically, consider

\[
\dot m_i=m_i(1-m_i-\alpha m_{i+1}-\beta m_{i+2})+\mu\bigl(m_{i+1}+m_{i+2}-2m_i\bigr),
\qquad m_i\ge0.
\]

Here \(\alpha,\beta>0\), \(\alpha+\beta>2\), \(\alpha\ne\beta\), and \(\mu\) varies through \(\mu_H\) from below. The theorem concerns only the locally bifurcating periodic orbit, not global attractor selection. The positivity condition for the competition coefficients is equivalent, for fixed \(\lambda\), to \(0<|w|<\sqrt3(\lambda+1)\). Define the original-time orbit period by the least positive return time of the full vector \((m_1,m_2,m_3)\).

## Proof

**Exact reduction.** Use the translation and orthogonal cyclic mode coordinates

\[
 m_1=\sigma^{-1}+2x+z,\quad m_2=\sigma^{-1}-x-\sqrt3y+z,\quad m_3=\sigma^{-1}-x+\sqrt3y+z,
 \qquad U=x+iy.
\]

Direct substitution in the three original polynomial differential equations (with no time rescaling) gives the **exact** complex-real system

\[
\dot U=(3\delta+i\omega)U+(\lambda-iw)\overline U^{\,2}+(-c+iw)Uz,
\qquad\dot z=-z-\sigma z^2+2\lambda|U|^2,
\]

where \(\omega=w/\sigma\), \(c=(\sigma+3)/2>0\), and \(\delta=\mu_H-\mu\). At \(\delta=0\), the linear eigenvalues are \(\pm i\omega,-1\). The nonzero-frequency hypothesis \(w\ne0\) supplies a nonresonant simple Hopf pair; the radial growth rate is \(3\delta\).

**Second harmonic and slaved mean.** Let \(r>0\) denote the (real, phase-fixed) first Fourier coefficient of \(U\) on the small periodic orbit, and write \(\vartheta=\nu t\), with \(\nu\) having the sign of \(\omega\). Analytic Hopf expansion, or a Fourier Lyapunov–Schmidt reduction, gives

\[
 U=r e^{i\vartheta}+A_2r^2e^{-2i\vartheta}+O(r^3),
 \qquad A_2=\frac{i(\lambda-iw)}{3\omega},
 \qquad z=2\lambda r^2+O(r^3).
\]

The second-harmonic coefficient follows by solving \((-2i\omega-i\omega)A_2=\lambda-iw\). The stable \(z\) equation gives its constant Fourier component \(2\lambda r^2\). These expansions hold in smooth periodic-function norms as \(r\to0\). Neither an initial-value simulation nor a truncated enumeration is being treated as proof.

**Fundamental harmonic balance.** At order \(r^3e^{i\vartheta}\), the nonlinear terms give the coefficient

\[
 2(\lambda-iw)\overline{A_2}+2\lambda(-c+iw)
 =-2\lambda c+i\left(2\lambda w-\frac{2(\lambda^2+w^2)}{3\omega}\right).
\]

The real and imaginary fundamental equations therefore yield

\[
 r^2=\frac{3\delta}{2\lambda c}+o(\delta),
 \qquad
 \nu=\omega+\left(2\lambda w-\frac{2(\lambda^2+w^2)}{3\omega}\right)r^2+o(r^2).
\]

In particular \(-2\lambda c<0\) is the radial cubic coefficient, so the Hopf branch is supercritical and attracting for small \(\delta>0\). Taking \(T=2\pi/|\nu|\), using \(\omega=w/\sigma\), \(c=(\sigma+3)/2\), and \(\sigma=2\lambda+3\), produces exactly the stated formula for \(\mathcal P\). The change of the signed angular frequency has been divided by the signed \(\omega\); hence the result holds for either ordering of \(\alpha,\beta\).

**Sharp positive-parameter boundary.** For \(\lambda\le3\), the bracket in \(\mathcal P\) is positive. For \(\lambda>3\), negativity is equivalent to \(w^2>\sigma\lambda^2/(\lambda-3)\). Strict positivity of \(\alpha\) and \(\beta\) imposes \(w^2<3(\lambda+1)^2\). These inequalities are simultaneously satisfiable precisely when

\[
 3(\lambda+1)^2(\lambda-3)-(2\lambda+3)\lambda^2
 =\lambda^3-6\lambda^2-15\lambda-9>0.
\]

The cubic is strictly decreasing until its sole positive turning point \(2+\sqrt9=5\), and strictly increasing afterward; it is negative at \(0\) and crosses zero exactly once on \((5,\infty)\). Hence the root \(\lambda_*\) is unique and the sign diagram is sharp, including strict positivity of all rate constants.

## Verification

The accompanying `CHECK.py` directly compares the original population-vector field to the transformed complex-real field at independent positive test configurations, reconstructs the Hopf and first-period coefficients from the Fourier balance, and verifies the sharp sign inequality and explicit two-sign witnesses. An additional independent numerical shooting test of the exact transformed ODE yielded the following observed finite-difference values of \((T/T_H-1)/\delta\): for \((\lambda,w)=(10,16)\), values \(0.36657,0.35882,0.35417\) at \(\delta=0.001,0.0005,0.0002\), approaching \(0.35108173\ldots\); for \((10,18.5)\), values \(-0.03662,-0.04306,-0.04692\), approaching \(-0.04949711\ldots\). These checks support, but do not replace, the preceding analytic proof. The numerical shooting check used adaptive ODE integration and a three-variable periodic-orbit root solve; the reproducible standard-library checker is self-contained.

## Relationship to prior work

Jaramillo, Mrad and Stepien (arXiv:2210.04342, first publicly posted 2022-10-09) introduced and analyzed the same linearly mutated cyclic May–Leonard flow. Their primary text treats its equilibrium, Hopf transition, cycle existence and stability, and fold diagrams. The present claim does **not** treat Hopf occurrence or supercriticality as independently new: it derives the signed, original-physical-time **first period derivative** and characterizes its sharp sign reversal under strictly positive competition constraints. Standard Hopf normal forms imply how to calculate frequency drift in principle but do not furnish the model-specific formula, sharp feasibility cubic, or positive-parameter two-sign classification. Results for the exchange-symmetric slice \(\alpha=\beta\) do not imply this claim because \(w=0\) and the Hopf frequency vanishes there.

## Limitations

This is a local small-cycle theorem for fixed positive parameters and \(\mu\uparrow\mu_H\) from below. The neutral-coefficient locus concerns only a first-order derivative, not exact isochrony or higher corrections. Global persistence, multiple cycles, bifurcations away from this Hopf point, and spatially extended models are not classified. Searches and inspection of the originating preprint did not identify equivalent published formulas, but completeness of all scholarly literature cannot be certified without independent review. Independent mathematical audit has not been performed.

## References

1. G. Jaramillo, L. Mrad and T. L. Stepien, *Dynamics of a linearly-perturbed May–Leonard competition model*, arXiv:2210.04342 (first version 2022-10-09), later published in *Chaos* **33** (2023), 063121; DOI 10.1063/5.0138150. https://arxiv.org/abs/2210.04342
2. R. M. May and W. J. Leonard, *Nonlinear aspects of competition between three species*, *SIAM Journal on Applied Mathematics* **29** (1975), 243–253; DOI 10.1137/0129022.
3. I. Sorin, A. Nepomnyashchy and V. Volpert, *Stability of Oscillations in the Spatially Extended May–Leonard Model*, *SIAM Journal on Applied Mathematics* **86** (2026), 1230–1255; DOI 10.1137/25M1737201 (different diffusion-modified model; abstract inspected).
