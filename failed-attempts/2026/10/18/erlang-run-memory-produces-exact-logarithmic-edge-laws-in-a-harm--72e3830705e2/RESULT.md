# Erlang-run memory produces exact logarithmic edge laws in a harmonic trap

## Finding
Consider a one-dimensional particle satisfying \(\dot X_t=-\kappa X_t+vS_t\), where \(\kappa,v>0\), the velocity sign \(S_t\in\{-1,+1\}\) alternates deterministically at successive renewal epochs, and the independent holding times of both signs have Erlang distribution with integer shape \(m\geq1\) and stage rate \(\lambda>0\). Write \(Z=\kappa X/v\), \(r=\lambda/\kappa\), and let \(f_m\) be the unique stationary density of \(Z\) on \((-1,1)\).

Let \(B_j,C_j\) be iid, mutually independent copies of \(e^{-\kappa T}\), with \(T\sim\operatorname{Erlang}(m,\lambda)\). The stationary entrance deficit is the absolutely convergent positive perpetuity
\[
Y_*\;\overset{d}{=}\;2\sum_{j=0}^{\infty}(1-C_j)\prod_{i=0}^{j-1}(B_iC_i),\qquad 0<Y_*<2\quad\text{almost surely}.
\]
For every \(r>0\), the inverse moment \(\mathbb E[Y_*^{-r}]\) is finite and strictly positive. The stationary density has the sharp, two-sided boundary law
\[
\boxed{\displaystyle
f_m(1-y)=f_m(-1+y)\sim A_m(r)y^{r-1}\bigl(\log(1/y)\bigr)^{m-1},\qquad y\downarrow0,}
\]
where the exact finite positive coefficient is
\[
\boxed{\displaystyle A_m(r)=\frac{r^m}{2m!}\,\mathbb E[Y_*^{-r}].}
\]
Consequently \(\Pr(Z>1-y)\sim A_m(r)y^r(\log(1/y))^{m-1}/r\). For \(r<1\), the density diverges at both edges; for \(r>1\), it tends to zero. At the critical ratio \(r=1\), the Markovian case \(m=1\) has a finite, nonzero edge value, whereas every \(m\ge2\) has a logarithmic divergence of order \((\log(1/y))^{m-1}\). This logarithmic-degree hierarchy is the claim; it is not a claim that the previously known exponential-waiting result is new.

## Assumptions and scope
All \(m\) are positive integers, all \(\kappa,v,\lambda\) are strictly positive, holding times are iid for successive runs, the sign reverses at every tumble, and there is no translational Brownian noise. The normalized stationary support is \([-1,1]\); endpoints have zero mass. The rate \(\lambda\) is the stage rate, so the mean run time is \(m/\lambda\). The density \(f_m\) refers to the normalized coordinate \(Z\), not to dimensional \(X\). An empty product is one. The coefficient is an exact expectation under an explicitly defined convergent perpetuity; a closed expression in elementary constants is not asserted for \(m\ge2\).

## Proof
**1. Existence, entrance law, and independence.** In normalized coordinates, \(\dot Z=\kappa(S-Z)\). Two solutions driven by the same sign path contract at rate \(\kappa\), so the stationary position is unique; the stationary alternating renewal process has equal sign probabilities and is itself uniquely determined. At the beginning of a positive run let \(Y=1-Z\). Over the positive run of duration \(T_+\), the deficit is multiplied by \(B=e^{-\kappa T_+}\). Over the following negative run of duration \(T_-\), it evolves to \(2(1-C)+CBY\), where \(C=e^{-\kappa T_-}\). Thus the entrance deficits obey the affine recursion \(Y'=2(1-C)+BCY\). Since \(B,C\in(0,1)\), iteration gives the displayed perpetuity; convergence follows because \(\mathbb E\log(BC)=-2m/r<0\). The bound \(0<Y_*<2\) follows termwise from \(1-C\le 1-BC\) and the telescoping product. At a stationary time conditional on the positive sign, the current run's backward age \(A\) is independent of \(Y_*\), because the current holding time is sampled independently of the past; its equilibrium-age density is \(\Pr(T>a)/\mathbb ET\).

**2. Exact positive-sign density.** The Erlang survival probability and mean give
\[
 h_A(a)=\frac{\lambda}{m}e^{-\lambda a}\sum_{j=0}^{m-1}\frac{(\lambda a)^j}{j!},\qquad a>0.
\]
During the current positive run, \(1-Z=Y_*e^{-\kappa A}\). Put \(y=1-z\). A change of variables in the age density shows that the **joint** stationary density for \(Z=z,S=+1\), denoted \(p_+(z)\), is
\[
 p_+(1-y)=\frac{r}{2m}y^{r-1}\mathbb E\!\left[Y_*^{-r}\,\mathbf{1}_{\{Y_*>y\}}\sum_{j=0}^{m-1}\frac{\bigl(r\log(Y_*/y)\bigr)^j}{j!}\right],\quad 0<y<2.
\]
The factor \(1/2\) is the stationary probability of the positive orientation. The corresponding negative-sign density exists in the open support. Stationarity of the position marginal makes its flux constant: \(\kappa(1-z)p_+(z)-\kappa(1+z)p_-(z)=J\). Since the support is compact, the stationary flux is \(J=0\). Consequently \(p_-(1-y)=y\,p_+(1-y)/(2-y)\), and hence the **exact full-density identity** is
\[
\boxed{\displaystyle
 f_m(1-y)=\frac{r}{m(2-y)}y^{r-1}\mathbb E\!\left[Y_*^{-r}\mathbf{1}_{\{Y_*>y\}}\sum_{j=0}^{m-1}\frac{\bigl(r\log(Y_*/y)\bigr)^j}{j!}\right].}
\]
This formula holds for the full continuum of \(0<y<2\), not only asymptotically.

**3. Crucial finiteness of the negative entrance moment.** This is not inferred from simulations. Set \(L(t)=\mathbb E[e^{-tY_*}]\). For \(B=e^{-\kappa T}\), the density on \((0,1)\) is \(r^m(-\log b)^{m-1}b^{r-1}/(m-1)!\). Its small-\(b\) tail has power \(r\), up to a logarithmic factor. Splitting the fixed-point equation at \(C=1/2\), for \(t\ge1\), gives
\[
 L(t)\le e^{-t}+H(t)\,\mathbb E[L(tB/2)],\qquad
 H(t)=\mathbb E[e^{-2t(1-C)}\mathbf{1}_{\{C\ge1/2\}}]=O(t^{-m}).
\]
The last bound follows from the density of \(1-C\) near zero being \(O(u^{m-1})\). For every \(s\ge0\) and \(\epsilon>0\), direct integration against the displayed density of \(B\) gives
\[
 L(t)=O(t^{-s})\quad\Longrightarrow\quad
\mathbb E[L(tB/2)]=O\bigl(t^{-\min(s,r)+\epsilon}\bigr).
\]
Starting from \(L\le1\) and iterating finitely many times, the exponent increases by essentially \(m\) until it exceeds \(r\); one further iteration gives \(L(t)=O(t^{-q})\) for every \(q<r+m\). Indeed, the errors \(\epsilon\) can be chosen arbitrarily small at each of the finitely many steps. The Mellin--Laplace identity \(\mathbb E[Y_*^{-p}]=\Gamma(p)^{-1}\int_0^\infty t^{p-1}L(t)\,dt\), for \(p>0\), proves \(\mathbb E[Y_*^{-p}]<\infty\) for all \(p<r+m\). Choosing \(r<p<r+m\) also proves \(\mathbb E[Y_*^{-r}(1+|\log Y_*|^{m-1})]<\infty\).

**4. Exact boundary limit.** Divide the full-density identity by \(y^{r-1}(\log(1/y))^{m-1}\). For each fixed \(Y_*=z>0\), the highest term in the sum tends to \(r^{m-1}z^{-r}/(m-1)!\), while lower-degree terms vanish (with the same interpretation for \(m=1\)). For \(0<y<e^{-1}\), \(z\in(y,2)\), the normalized summand is bounded by a constant times \(z^{-r}(1+|\log z|^{m-1})\). This is integrable by Step 3. Dominated convergence and \(2-y\to2\) therefore give exactly \(r^m\mathbb E[Y_*^{-r}]/(2m!)\). Symmetry under simultaneous reversal of position and sign gives \(f_m(-z)=f_m(z)\). Integration of the positive regularly varying density gives the stated upper-tail probability. Since powers dominate logarithms, the endpoint classification follows.

## Verification
The standalone `check.py` is a standard-library Python program. It solves the \(2m\)-phase stationary Markov-generator moment equations over exact rational arithmetic and independently computes the same moments from the renewal-entry affine recursion and equilibrium-age transform. Across \(m=1,2,3,4\), \(r=1/2,1,2,3\), and orders through six, **216 exact rational assertions pass**. At \(r=1\), the first two nontrivial moments, for \(m=1,2,3,4\), respectively, are \((1/3,1/5)\), \((2/5,9/34)\), \((13/27,883/2535)\), and \((19/34,891/2056)\). These are independent checks on model normalization and the regenerative construction, not numerical proofs of a boundary limit.

For \(m=1\), the established exact Markovian density is \(f_1(z)=\Gamma(r+1/2)(1-z^2)^{r-1}/(\sqrt\pi\Gamma(r))\). It agrees with the theorem's amplitude because \(\mathbb E[Y_*^{-r}]=2^r\Gamma(r+1/2)/(\sqrt\pi\Gamma(r+1))\); in particular \(r=1\) yields the uniform density \(f_1=1/2\). The proof itself supplies the all-parameter, all-integer-shape result independently of this consistency check.

## Relationship to prior work
Farago and Smith, arXiv:2401.01576v1 (3 January 2024; subsequently Phys. Rev. E 109, 044121), develop a general steady-state integral-equation and numerical framework for non-Markovian tumbling in confining potentials. Their explicit examples use exponential, semi-Gaussian, and half-\(t\) waiting laws, not the Erlang-shape boundary expansion. Their equations implicitly encode the model, but do not state the present logarithmic-degree theorem, exact entrance-perpetuity coefficient, or its inverse-moment justification. The exponential case is previously known, and is reproduced only as a boundary check.

Di Crescenzo and Martinucci, arXiv:0803.1067, analyze gamma-distributed alternating velocities **without** a harmonic confining force; their finite-time integrated telegraph law is not the present stationary edge law. Dhar et al., arXiv:1811.03808, analyze the Markovian run-and-tumble harmonic-trap baseline. Hahn, arXiv:2506.02274, studies qualitative invariant-density regularity for broader switching PDMPs; its relevant statements are not a sharp Erlang-boundary asymptotic with a logarithmic hierarchy and coefficient. A stronger unlocated general theorem on phase-type PDMP singularities remains a priority risk.

## Limitations
The proof is restricted to integer-shape Erlang holding times, symmetric alternation, a linear trap and zero translational Brownian noise. It does not classify bulk modes, derive finite-time relaxation rates, or establish a closed elementary formula for \(\mathbb E[Y_*^{-r}]\) at general shape. The boundary limit is asymptotic with fixed physical parameters and fixed integer \(m\); uniformity as \(m\to\infty\) is not asserted. The finite checker is corroborative and does not substitute for the all-parameter analytic boundary proof.

## References
1. O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics*, arXiv:2401.01576v1 (3 January 2024), https://arxiv.org/abs/2401.01576 .
2. A. Di Crescenzo and B. Martinucci, *Random motion with gamma-distributed alternating velocities in biological modeling*, arXiv:0803.1067v1 (7 March 2008), https://arxiv.org/abs/0803.1067 .
3. A. Dhar, A. Kundu, S. N. Majumdar, S. Sabhapandit, and G. Schehr, *Run-and-tumble particle in one-dimensional confining potential: steady state, relaxation and first passage properties*, arXiv:1811.03808v1 (9 November 2018), https://arxiv.org/abs/1811.03808 .
4. L. Hahn, *Invariant-measure regularity for one-dimensional PDMPs with applications to shape transitions in run-and-tumble particle systems*, arXiv:2506.02274 (2025), https://arxiv.org/abs/2506.02274 .
