# Exact angular-excursion law for the uniform error of a reused Gaussian range sketch

## Finding

Consider a continuous family of real positive-definite matrices whose leading eigenvector rotates through an angular excursion \(\alpha\). Reusing **one** standard Gaussian probe in a rank-one range finder has an exactly computable worst-parameter error distribution. In particular, although the expected squared error at each fixed parameter equals \(\varepsilon\), the maximum error equals the full leading singular value \(1\) with probability \(\min\{\alpha/\pi,1\}\), independently of the small trailing eigenvalue \(\varepsilon\). This is a quantitative separation between parameterwise or integrated accuracy and uniform accuracy.

More precisely, for \(0<\varepsilon<1\), \(T>0\), a continuous real-valued angle \(\theta:[0,T]\to\mathbb R\), and the rotation matrix \(R(\theta)\), set
\[
A_\varepsilon(t)=R(\theta(t))\begin{pmatrix}1&0\\0&\varepsilon\end{pmatrix}R(\theta(t))^{\mathsf T}.
\]
Draw \(g\sim N(0,I_2)\) once, reuse it for all \(t\), and form the one-column randomized-range approximation
\[
\widehat A_\varepsilon(t)=P_{A_\varepsilon(t)g} A_\varepsilon(t),\qquad P_y=yy^{\mathsf T}/(y^{\mathsf T}y).
\]
Let \(E_\varepsilon(t)=\|A_\varepsilon(t)-\widehat A_\varepsilon(t)\|_2\), \(M_\varepsilon=\max_{t\in[0,T]}E_\varepsilon(t)\), and \(\alpha=\max_t\theta(t)-\min_t\theta(t)\). Each error matrix has rank one, so its spectral and Frobenius norms agree, and the best rank-one approximation error in either norm is \(\varepsilon\) at every parameter.

If \(\alpha\ge\pi\), then \(M_\varepsilon=1\) for every nonzero probe. If \(0\le\alpha\le\pi\), then for every \(z\in[\varepsilon,1]\), writing
\[
\delta_\varepsilon(z)=\arcsin\!\left(\varepsilon\sqrt{\frac{z^{-2}-1}{1-\varepsilon^2}}\right),
\]
one has the **exact finite-\(\varepsilon\) tail law**
\[
\Pr\{M_\varepsilon\ge z\}=\min\!\left\{1,\frac{\alpha+2\delta_\varepsilon(z)}{\pi}\right\},\qquad
\Pr\{M_\varepsilon=1\}=\frac{\alpha}{\pi}.
\]
The distribution is parameterization-invariant: only the range of the continuous angle matters, not the speed or number of reversals. Its mean is exactly
\[
\mathbb E M_\varepsilon=\frac{\alpha}{\pi}+\frac{2\varepsilon}{\pi}
\int_0^{(\pi-\alpha)/2}\frac{du}{\sqrt{\sin^2u+\varepsilon^2\cos^2u}},\quad 0\le\alpha\le\pi.
\]
For each fixed \(0\le\alpha<\pi\) and \(\varepsilon\downarrow0\),
\[
\mathbb E M_\varepsilon=\frac{\alpha}{\pi}+\frac{2\varepsilon}{\pi}\log\!\frac{4\tan((\pi-\alpha)/4)}{\varepsilon}+o(\varepsilon),
\]
and for \(\alpha=\pi\) the mean is exactly \(1\). On the other hand, for every fixed \(t\),
\[
\mathbb E\,E_\varepsilon(t)^2=\varepsilon,\qquad
\mathbb E\!\int_0^T E_\varepsilon(t)^2\,dt=T\varepsilon.
\]
Thus positive angular excursion leaves a nonzero limiting expected uniform error, even though the mean squared integrated error vanishes. For a full half-turn, the uniform error is \(1\) for every probe while the best rank-one error is \(\varepsilon\).

## Assumptions and scope

All matrices and Gaussian variables are real, \(g\) is one common probe for the entire continuous parameter interval, and \(0<\varepsilon<1\). A continuous lift \(\theta(t)\) is part of the construction; \(\alpha\) measures its maximum minus minimum (not total variation). The output is the orthogonal-projection approximation \(P_{Ag}A\) from the basic randomized range finder, with **no oversampling** and **no rank-truncation postprocessing**. For the simple analytic example \(\theta(t)=\alpha t/T\), all input matrices are analytic and uniformly positive definite for each fixed \(\varepsilon>0\). No sampling-grid or floating-point approximation is used in the mathematical statement.

## Proof

**1. Exact residual for one parameter.** Rotate coordinates so that the matrix is \(D_\varepsilon=\operatorname{diag}(1,\varepsilon)\) and normalize the direction of the probe to \((\cos\phi,\sin\phi)^{\mathsf T}\). The sketch direction is \(y=(\cos\phi,\varepsilon\sin\phi)^{\mathsf T}\). A perpendicular unit vector is
\[
n=\frac{(-\varepsilon\sin\phi,\cos\phi)^{\mathsf T}}{\sqrt{\cos^2\phi+\varepsilon^2\sin^2\phi}}.
\]
Since \(I-P_y=nn^{\mathsf T}\), the residual is rank one and its only nonzero singular value is \(\|D_\varepsilon n\|_2\). Hence
\[
E_\varepsilon(t)=\frac{\varepsilon}{\sqrt{\cos^2(\phi_0-\theta(t))+\varepsilon^2\sin^2(\phi_0-\theta(t))}},
\]
where \(\phi_0\) is the angle of the original probe. The same expression gives the Frobenius error. The singular values of \(A_\varepsilon(t)\) are \(1\) and \(\varepsilon\), so the optimal rank-one spectral/Frobenius error is \(\varepsilon\).

**2. Geometry of the maximum and exact distribution.** A nondegenerate isotropic Gaussian has a direction \(\phi_0\) uniform modulo \(\pi\). Because \(\theta\) is continuous, its image is the complete closed interval between its extrema. Let \(d\in[0,\pi/2]\) be the shortest angular distance modulo \(\pi\) between \(\phi_0-\pi/2\) and this image. Minimizing the denominator in the preceding display gives
\[
M_\varepsilon=\frac{\varepsilon}{\sqrt{\sin^2d+\varepsilon^2\cos^2d}}.
\]
For \(\alpha\ge\pi\), the image meets every projective direction and \(d=0\). For \(0\le\alpha<\pi\), the circular arc occupied by the image has length \(\alpha\) on a circle of circumference \(\pi\). Thus \(d=0\) has probability \(\alpha/\pi\); for \(0<d<(\pi-\alpha)/2\), the distance has density \(2/\pi\). The event \(M_\varepsilon\ge z\) is equivalent to \(d\le\delta_\varepsilon(z)\). This proves both the stated tail law and the expectation integral, including the endpoints \(\alpha=0,\pi\).

**3. Vanishing-tail asymptotics.** Set \(b=(\pi-\alpha)/2>0\). The relevant integral is
\[
J_\varepsilon(b)=\int_0^b\frac{du}{\sqrt{\sin^2u+\varepsilon^2\cos^2u}}.
\]
For \(b<\pi/2\), substituting \(v=\tan u\) gives
\[
J_\varepsilon(b)=\int_0^{\tan b}\frac{dv}{\sqrt{v^2+\varepsilon^2}\sqrt{1+v^2}}.
\]
Subtract \(\int_0^{\tan b}dv/\sqrt{v^2+\varepsilon^2}=\operatorname{arsinh}(\tan b/\varepsilon)\). Dominated convergence on the difference yields the limit
\[
\int_0^{\tan b}\frac{1/\sqrt{1+v^2}-1}{v}\,dv=\log\!\frac{2}{1+\sqrt{1+\tan^2b}}.
\]
Combining with the logarithmic asymptotic of \(\operatorname{arsinh}\) proves
\[
J_\varepsilon(b)=\log\!\frac{4\tan(b/2)}{\varepsilon}+o(1).
\]
The endpoint \(b=\pi/2\) follows from the same subtraction with a diverging upper bound, or the standard complete elliptic integral asymptotic \(J_\varepsilon(\pi/2)=\log(4/\varepsilon)+o(1)\). Multiplying by \(2\varepsilon/\pi\) proves the mean expansion. For \(\alpha=\pi\), \(d=0\) identically and the result is immediate.

**4. Pointwise squared error.** For fixed \(t\), uniformity of \(\phi_0\) gives
\[
\mathbb E\,E_\varepsilon(t)^2=\frac{\varepsilon^2}{\pi}\int_0^\pi\frac{d\phi}{\cos^2\phi+\varepsilon^2\sin^2\phi}=\varepsilon.
\]
The integral is evaluated by symmetry and the substitution \(v=\tan\phi\) over one quadrant. Tonelli's theorem then gives the integrated identity. These exact identities prove the claimed separation without exchanging a maximum and an expectation.

## Verification

The standalone `verify_rotation.py` recomputes 1,200 direct projection residuals against the scalar formula, 1,200 dense-grid lower approximations against the exact continuum supremum, 15 expectation integrals with independent angular quadrature, 60 tail probabilities from deterministic angular-grid measures, 12 small-\(\varepsilon\) asymptotic comparisons, and five pointwise second-moment integrals. All assertions passed with the declared tolerances. Run with Python, NumPy, and SciPy as specified in `requirements.txt`; `verification_output.txt` contains the observed checks. These finite experiments are diagnostics and do not replace Steps 1–4 of the proof.

## Relationship to prior work

Kressner and Lam, *Randomized low-rank approximation of parameter-dependent matrices* (arXiv:2302.12761, first submitted 24 February 2023), propose reusing Gaussian sketches across a continuous parameter family. Their Theorem 5 treats mean integrated Frobenius error; their Theorem 12 gives a non-sharp uniform bound under oversampling requirements \(r\ge2\) and \(p\ge4\). Their Remark 1 notes possible discontinuity when a deterministic sketch loses rank. None of these statements supplies the present exact atom, distribution, or singular small-eigenvalue behavior for a one-column sketch on a full-rank smooth family. Their results are credited as motivation, not claimed as new.

Halko, Martinsson, and Tropp, *Finding structure with randomness* (arXiv:0909.4061, §9.2, Theorem 11), give the foundational pointwise range-finder error framework. Diouane et al., *A general error analysis for randomized low-rank approximation methods* (arXiv:2206.08793, §3), analyze fixed-matrix Gaussian spectral and Frobenius errors. Epperly and Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation* (arXiv:2605.19096, §3, Theorems 3.2–3.3), provide sharp fixed-matrix mean-squared and minimax bounds under sampling-rank conditions; their theorems do not apply to the single-column rank-one target here and do not take a parameter supremum. None of these sources supplies the present distribution for the supremum over a continuously moving dominant eigenspace. The geometric derivation uses standard projective-circle measure, whose application to this uniform-error question is the particular contribution asserted here.

## Limitations

This theorem is exactly about \(2\times2\) real symmetric positive-definite matrices with two fixed eigenvalues, a continuously rotating eigenbasis, and one reused Gaussian probe. It does not assert analogous probabilities in higher dimension, for general varying singular values, for independent sketches at different parameters, or after oversampling and rank truncation. The nonzero uniform-error limit concerns an **unoversampled** rank-one range finder; standard oversampled guarantees are not contradicted. The exact angular law is a model-specific diagnostic, not a universal lower bound for all smooth parameter-dependent problems. Prior-work comparison cannot rule out every alternate formulation in historical projective probability or parametric approximation literature. No external or independent audit is claimed.

## References

1. D. Kressner and H. Y. Lam, *Randomized low-rank approximation of parameter-dependent matrices*, arXiv:2302.12761, v1 24 February 2023; inspected full arXiv HTML v4 (2024), §§2–4. https://arxiv.org/abs/2302.12761
2. N. Halko, P.-G. Martinsson, and J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, arXiv:0909.4061, 2009/2010, §§9–10. https://arxiv.org/abs/0909.4061
3. Y. Diouane, S. Gürol, A. Scotto Di Perrotolo, and X. Vasseur, *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793, 2022, §3. https://arxiv.org/abs/2206.08793
4. E. N. Epperly and R. J. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation*, arXiv:2605.19096, 2026, §3. https://arxiv.org/abs/2605.19096
