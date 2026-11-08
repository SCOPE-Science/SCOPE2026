# Exact reentrant Fourier-correlation frontiers for Gaussian Cayley steps on the circle

## Finding

For the rotational Stratonovich Brownian SDE on the unit circle, the Gaussian Cayley time-step preserves the circle and the uniform invariant law for every stepsize but does not preserve the sign or monotonic decay of the exact diffusion's Fourier correlations. Writing \(\lambda_m(h)\) for its one-step multiplier on the \(m\)-th Fourier mode, the complete conclusions are:

1. For every integer \(m\geq 1\), \(\lambda_m(h)\) has at most \(m\) distinct positive zero stepsizes.
2. The first mode has exactly one positive zero, approximately \(h=10.679542107510\); it is positive below and negative above that zero.
3. The second mode has **exactly two** positive zeros, approximately \(h_-=1.489832571435\) and \(h_+=36.820960093978\). It is positive on \((0,h_-)\), negative on \((h_-,h_+)\), and positive on \((h_+,\infty)\). In particular \(\lambda_2(4)<-1/75\).
4. For each fixed \(m\geq1\), \(\lambda_m(h)\to(-1)^m\) as \(h\to\infty\), whereas the exact Brownian transition eigenvalue \(e^{-m^2h/2}\) tends to zero through positive values. The normalized Haar measure remains the unique invariant probability measure of the numerical chain for every finite \(h>0\).

The **two-root reentrance of the second harmonic**, including a completely analytic sign certificate and root-count proof, is the central numerical-analysis finding. The all-mode zero bound is a structural extension. The displayed decimals are reproducible numerical approximations, not formally certified rational brackets.

## Assumptions and scope

Let \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), and let \(W_t\) be a real standard Brownian motion. The exact equation on \(\mathbb R^2\) is

\[
 dX_t=JX_t\circ dW_t,\qquad \|X_0\|_2=1.
\]

For a fixed stepsize \(h>0\), take independent \(Z_k\sim N(0,1)\) and define the **Gaussian Cayley scheme**

\[
 X_{k+1}=\left(I-\tfrac12\sqrt h Z_kJ\right)^{-1}
 \left(I+\tfrac12\sqrt h Z_kJ\right)X_k.
\]

The factor \(1/2\) is part of the normalization: this mapping has the same linear small-step rotation as \(\exp(\sqrt h Z_kJ)\). Identify \(X_k=(\cos\theta_k,\sin\theta_k)\) and set

\[
 \alpha_h=2\arctan(\sqrt h Z/2),\quad
 P_hf(\theta)=\mathbb E[f(\theta+\alpha_h)],\quad
 \lambda_m(h)=\mathbb E[\cos(m\alpha_h)].
\]

For the exact Brownian equation, \(\theta_t=\theta_0+W_t\pmod{2\pi}\) and the Fourier multiplier is \(e^{-m^2h/2}\). Every assertion about the numerical scheme concerns one fixed Gaussian Cayley step and its iterated homogeneous Markov chain, not general manifold integrators or other noise laws.

## Proof

**1. Exact Fourier–Chebyshev representation.** Because \(J^2=-I\), the step matrix is the rotation by \(\alpha_h\). Reflection symmetry of \(Z\) makes each Fourier multiplier real. Set \(r=h/4\), \(Y=rZ^2\), and let \(T_m\) denote the first-kind Chebyshev polynomial. The double-angle identity gives

\[
 \cos\alpha_h=\frac{1-Y}{1+Y},\qquad
 \lambda_m(h)=\mathbb E\left[T_m\left(\frac{1-Y}{1+Y}\right)\right].
\]

With \(t=2/h>0\) and
\(K_m(y)=T_m((1-y)/(1+y))\), the chi-square density yields

\[
 \lambda_m(h)=\sqrt{\frac t\pi}\int_0^\infty
 y^{-1/2}e^{-ty}K_m(y)\,dy.
 \tag{1}
\]

The rational function \(K_m\) has exactly \(m\) distinct simple positive zeros

\[
 y_j=\tan^2\left(\frac{(2j-1)\pi}{4m}\right),
 \quad 1\le j\le m,
\]

and changes sign at each one: its Chebyshev argument decreases strictly from \(1\) to \(-1\).

**2. Exponential-kernel zero-count lemma.** Suppose a continuous, nontrivial, locally integrable function \(g(y)\) on \((0,\infty)\), absolutely integrable after multiplication by \(e^{-ty}\) for each \(t>0\), changes sign at exactly \(m\) distinct points \(y_1<\cdots<y_m\). Then its Laplace transform \(F(t)=\int_0^\infty e^{-ty}g(y)\,dy\) has at most \(m\) distinct zeros for \(t>0\), provided the defining integrals converge absolutely.

To prove this lemma, assume \(F(t_i)=0\) for \(m+1\) distinct positive \(t_i\). The \(m\) homogeneous conditions \(\sum_{i=1}^{m+1}c_i e^{-t_i y_j}=0\) admit a nonzero real coefficient vector. Thus the exponential polynomial \(q(y)=\sum c_i e^{-t_i y}\) vanishes at all \(m\) prescribed sign-change points. A nonzero sum of \(m+1\) real exponentials with distinct rates has at most \(m\) real zeros counted with multiplicity: divide by the exponential with smallest rate and apply Rolle's theorem inductively to its derivative. Consequently \(q\) has precisely these zeros, all simple, and no other positive zeros. The product \(g(y)q(y)\) therefore has a constant nonzero sign away from these points. Its integral is strictly nonzero, contradicting \(\int gq=\sum c_iF(t_i)=0\). This establishes the lemma. Applying it to \(g(y)=y^{-1/2}K_m(y)\) in (1), and using the positive prefactor and one-to-one correspondence \(t=2/h\), proves the all-mode bound.

**3. Exact first two modes.** Define \(A(r)=\mathbb E[(1+rZ^2)^{-1}]\). A one-dimensional Gaussian integration, or the identity \((1+rZ^2)^{-1}=\int_0^\infty e^{-s(1+rZ^2)}ds\), gives

\[
 A(r)=\sqrt{\frac\pi{2r}}\,e^{1/(2r)}
 \operatorname{erfc}\left(\frac1{\sqrt{2r}}\right).
 \tag{2}
\]

Because \(T_1(u)=u\),
\[
 \lambda_1(h)=2A(r)-1.
 \tag{3}
\]

Writing \(B(r)=\mathbb E[(1+rZ^2)^{-2}]\), Gaussian integration by parts applied to \(z/(1+rz^2)\) gives
\(2B(r)-A(r)=(1-A(r))/r\). Inserting \(T_2(u)=2u^2-1\), we obtain the exact closed form

\[
 \lambda_2(h)=1+\frac4r-4\left(1+\frac1r\right)A(r).
 \tag{4}
\]

**4. A nonnumerical negative-value certificate.** At \(r=1\), i.e. \(h=4\), (4) becomes \(\lambda_2(4)=5-8A(1)\). From the error-function series,

\[
 A(1)=\sqrt e\left[\sqrt{\pi/2}
 -\sum_{k=0}^\infty\frac{(-1)^k}{2^kk!(2k+1)}\right].
\]

The alternating sum has strictly decreasing positive term magnitudes, so it is less than \(1-1/6+1/40=103/120\). Elementary bounds \(\sqrt{\pi/2}>5/4\) and \(\sqrt e>8/5\) therefore give

\[
 A(1)>\frac85\left(\frac54-\frac{103}{120}\right)
 =\frac{47}{75}>\frac58,
\]

hence **\(\lambda_2(4)<-1/75\)**. No numerical root finding is used in this sign proof.

**5. Exact root counts and global signs.** Dominated convergence in the Chebyshev expectation gives \(\lim_{h\downarrow0}\lambda_m(h)=1\) and \(\lim_{h\to\infty}\lambda_m(h)=(-1)^m\), since \(Z\ne0\) almost surely. Continuity holds for \(h>0\). Thus \(\lambda_1\) has at least one positive zero and, by Step 2 with \(m=1\), exactly one. The second mode is positive near both endpoints but negative at \(h=4\). The intermediate value theorem forces at least two distinct positive zeros; Step 2 with \(m=2\) permits no more. The stated sign intervals follow from continuity and absence of further zeros. Equations (3)–(4) specify their **exact implicit definitions**.

**6. Invariance and large-step comparison.** Each Cayley matrix is orthogonal of determinant one, so it preserves the unit circle. The transition is a convolution on the circle by a smooth symmetric increment law with strictly positive density in \((-\pi,\pi)\). Haar measure is invariant; every nonzero Fourier mode has \(|\lambda_m(h)|<1\), proving Haar is the unique invariant probability measure for each finite \(h>0\). Formula (2) yields

\[
 A(r)=\sqrt{\frac\pi{2r}}-\frac1r+O(r^{-3/2}),\qquad r\to\infty.
\]

Hence \(\lambda_1(h)=-1+2\sqrt{2\pi/h}+O(h^{-1})\) and \(\lambda_2(h)=1-4\sqrt{2\pi/h}+O(h^{-1})\). In contrast, the exact diffusion multipliers are positive and tend exponentially to zero.

## Verification

Run `python verify.py` with Python 3 and `mpmath`. The script reproduces the displayed roots via (3)–(4), numerically integrates the Gaussian angle distribution as a separate representation, checks the Chebyshev angle identity at specified points, and checks the analytic sign certificate's implication. Its recorded result is in `verify_output.txt`, including 151 successful deterministic assertions. These numerical checks **do not certify the global zero-count lemma or an infinite-domain assertion**; both are supplied by the analytic proof above. Root decimals are approximate and should not be used as validated interval enclosures.

## Relationship to prior work

Jauch–Hoff–Dunson (2018 preprint, later Bernoulli 2020) establish Cayley parametrization of random orthogonal/Stiefel matrices, their change-of-variables densities, and related Gaussian approximations. Their finite-dimensional distributional statements are not a Fourier spectral classification of repeated Gaussian Cayley Brownian steps. Muniz–Ehrhardt–Günther (2020 preprint; 2021 journal) describe stochastic Lie-group numerical integration and explicitly propose the Cayley map as an alternative to the matrix exponential; their actual reported covariance-flow simulations use the exponential parametrization. This is the closest methodological precedent, not a claim that the Cayley step is new. Armstrong–King (2022) treat invariant-manifold SDE approximations and convergence rather than this modewise sign classification. The Chebyshev and exponential-polynomial zero-count ingredients are classical tools; the assessed new statement is their sharp application to the exact one-dimensional Gaussian Cayley transition, especially the two-root second-harmonic frontier.

## Limitations

Only standard Gaussian independent increments, the drift-free planar rotational Stratonovich SDE, and the specified half-scaled Cayley map are covered. The exact two-root classification is proved for Fourier mode \(m=2\), not for all modes; the general result is only an upper bound on zero counts. Step sizes refer to a single fixed homogeneous transition and do not compare arbitrary variable-step composition. The source comparison is best-knowledge rather than a guarantee of worldwide publication priority; older or obscure spectral treatments of Gaussian Cayley random walks may exist. Formal independent audit has not been performed.

## References

- M. Jauch, P. D. Hoff, D. B. Dunson, *Random orthogonal matrices and the Cayley transform*, arXiv:1810.02881, first public preprint 5 October 2018; Bernoulli 26 (2020), 1560–1586. https://arxiv.org/abs/1810.02881
- M. Muniz, M. Ehrhardt, M. Günther, *Approximating correlation matrices using stochastic Lie group methods*, BUW-IMACM preprint 20/05, dated March 2020; Mathematics 9 (2021), 94. https://imacm.uni-wuppertal.de/fileadmin/imacm/preprints/2020/imacm_20_05.pdf ; https://doi.org/10.3390/math9010094
- J. Armstrong, T. King, *Curved schemes for stochastic differential equations on, or near, manifolds*, Proc. R. Soc. A 478 (2022), 20210785. https://doi.org/10.1098/rspa.2021.0785
