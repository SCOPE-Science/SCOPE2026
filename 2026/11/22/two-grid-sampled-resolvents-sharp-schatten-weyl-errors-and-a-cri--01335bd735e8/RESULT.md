# Two-grid sampled resolvents: sharp Schatten–Weyl errors and a critical weak endpoint

## Finding
For a nonnegative compact-resolvent generator with a Weyl counting law, a dyadic combination of two sampled resolvents is trace class at **every fixed mesh**, yet its error has a sharp dimension-dependent Schatten boundary. Specifically, let
\[
Q_h=h\bigl(I-e^{-h(\lambda+A)}\bigr)^{-1},\qquad P_h=2Q_{h/2}-Q_h,\qquad R=(\lambda+A)^{-1}.
\]
The exact operator identity is
\[
P_h=\frac{h}{2\sinh(h(\lambda+A)/2)},\qquad E_h:=R-P_h=h\phi\bigl(h(\lambda+A)\bigr),
\quad \phi(u)=\frac1u-\frac1{2\sinh(u/2)}>0.
\]
For every real \(p>\nu\), including quasi-Schatten exponents below one,
\[
\lim_{h\downarrow0}h^{\nu-p}\operatorname{Tr}(E_h^p)
=C\nu\int_0^\infty\phi(u)^p u^{\nu-1}\,du\in(0,\infty).
\]
For every \(0<p\le\nu\), the error is not in \(\mathcal S_p\) for any fixed positive mesh. At the sharp weak endpoint,
\[
\lim_{h\downarrow0}\|E_h\|_{\mathcal S_{\nu,\infty}}=C^{1/\nu},
\quad \|T\|_{\mathcal S_{\nu,\infty}}:=\sup_{n\ge1}n^{1/\nu}s_n(T).
\]
For \(0<\nu<1\), the nuclear constant is the explicit zeta value
\[
\lim_{h\downarrow0}h^{\nu-1}\operatorname{Tr}(E_h)
=-C\nu\Gamma(\nu)(2^\nu-1)\zeta(\nu)>0.
\]

## Assumptions and scope
Let \(\mathscr H\) be an infinite-dimensional separable Hilbert space. Let \(A\ge0\) be self-adjoint with compact resolvent. Repeat eigenvalues with multiplicity and write them \(\mu_1\le\mu_2\le\cdots\to\infty\). Assume, for fixed constants \(C,\nu>0\),
\[
N_A(x):=\#\{j:\mu_j\le x\}=Cx^\nu+o(x^\nu)\quad(x\to\infty).
\]
Fix \(\lambda>0\); all limits are \(h\downarrow0\). The Schatten quasi-norm at \(0<p<1\) is defined by \(\|T\|_{\mathcal S_p}^p=\sum_j s_j(T)^p\), and the weak ideal quasi-norm is specified above. No upper spectral remainder or elliptic differential structure is required. \(Q_h\) is the grid-sampled Laplace resolvent of \(e^{-tA}\).

## Proof
**1. Exact cancellation and positivity.** Scalar algebra with \(z=e^{-ha/2}\in(0,1)\) gives
\[
2\frac{h/2}{1-z}-\frac h{1-z^2}=\frac{hz}{1-z^2}=\frac h{2\sinh(ha/2)}.
\]
Applying the bounded Borel functional calculus with \(a=\lambda+A\) gives the operator formula. Because \(2\sinh(u/2)>u\) for \(u>0\), \(E_h\ge0\). Taylor expansion and elementary exponential estimates give
\[
\phi(u)=\frac{u}{24}+O(u^3)\ (u\downarrow0),\qquad
\phi(u)=u^{-1}+O(e^{-u/2})\ (u\to\infty).
\]
Thus \(\phi\) is positive, continuous, bounded, and \(\phi(u)\le K\min\{u,u^{-1}\}\) for a universal finite \(K\). The Weyl counting condition implies \(\sum_j e^{-c\mu_j}<\infty\) for every \(c>0\); hence \(P_h\) is trace class. The same condition and \(\phi(u)\to0\) imply \(E_h\) is compact.

**2. Sharp strong-ideal law.** Put \(a_j=\lambda+\mu_j\), and let \(\nu_h=h^\nu\sum_j\delta_{ha_j}\) be measures on \((0,\infty)\). The Weyl law gives vague convergence
\[
\nu_h\ \Longrightarrow\ C\nu u^{\nu-1}\,du.
\]
For \(p>\nu\), \(f(u)=\phi(u)^p\) is integrable against the limiting measure. It also admits uniform truncation: the Weyl upper bound \(N_A(x)\le K(1+x)^\nu\) and integration by parts imply
\[
\limsup_{h\downarrow0} h^\nu\!\sum_{ha_j\le\varepsilon}\!f(ha_j)
\le K_p\varepsilon^{\nu+p},\quad
\limsup_{h\downarrow0}h^\nu\!\sum_{ha_j\ge M}\!f(ha_j)
\le K_p M^{\nu-p},
\]
where \(0<\varepsilon<1<M\). (If the lower region contains no eigenvalues, its sum is zero.) Truncate the measure at both ends, use vague convergence, then send \(\varepsilon\downarrow0\) and \(M\to\infty\). Since \(\operatorname{Tr}(E_h^p)=h^p\sum_j\phi(ha_j)^p\), this proves the stated limit with its positive finite coefficient.

**3. Failure of strong endpoint and the weak coefficient.** For each fixed \(h>0\), the eigenvalues of \(E_h\) at spectral level \(a_j\) are asymptotic to \(a_j^{-1}\). The Weyl law implies \(a_j\sim(j/C)^{1/\nu}\), and, after ordering the positive eigenvalues,
\[
s_n(E_h)\sim (C/n)^{1/\nu}\qquad(n\to\infty).
\]
A finite number of exceptional spectral levels cannot affect this tail. Consequently \(E_h\in\mathcal S_p\) exactly when \(p>\nu\), and its weak critical quasi-norm is finite and at least \(C^{1/\nu}\). For the reverse bound as \(h\downarrow0\), observe \(0\le E_h\le R\) and \(\|E_h\|\le h\sup\phi\). For every \(\eta>0\) choose a finite spectral cutoff \(a_j\le L\) such that the tail counting function satisfies \(N_{R|_{a_j>L}}(t)\le(C+\eta)t^{-\nu}\) for *all* \(t>0\); this follows directly from the Weyl upper estimate for sufficiently large \(L\). On the finitely many excluded modes, the error is \(O_L(h^2)\). Therefore, for any fixed \(\delta>0\) and small enough \(h\), the counting bound for the full error is \(N_{E_h}(t)\le(C+2\eta)t^{-\nu}\) both when \(t\) is below the finite-mode error scale (using the asymptotic Weyl bound for \(R\) at small \(t\)) and when \(t\) is above that scale (where no excluded mode contributes). The singular-value distribution identity \(\sup_n n^{1/\nu}s_n(E_h)=\sup_{t>0} t\,N_{E_h}(t)^{1/\nu}\), interpreted with one-sided thresholds, yields \(\limsup_{h\downarrow0}\|E_h\|_{\nu,\infty}\le(C+2\eta)^{1/\nu}\). Let \(\eta\downarrow0\).

**4. Nuclear zeta coefficient.** For \(0<\nu<1\), expansion of \((2\sinh(u/2))^{-1}=\sum_{k\ge0}e^{-(k+1/2)u}\) and the standard analytically continued Mellin identity, with the singular \(1/u\) term subtracted before integration, yield
\[
\int_0^\infty\phi(u)u^{\nu-1}\,du
=-\Gamma(\nu)\zeta(\nu,1/2)
=-\Gamma(\nu)(2^\nu-1)\zeta(\nu).
\]
Here the integral converges absolutely at both endpoints; \(\zeta(\nu)<0\) for \(0<\nu<1\). Substitute \(p=1\) in the strong-ideal law.

## Verification
The accompanying standalone `verify.py` checks the scalar two-grid identity, positivity, the small-argument cancellation coefficient, and convergence of normalized finite spectral sums for the Dirichlet interval Laplacian. These diagnostics do not certify the infinite-dimensional Weyl theorem; Steps 1–4 above are analytical. For \(A\) the Dirichlet Laplacian on an interval of length \(L\), \(C=L/\pi\) and \(\nu=1/2\); hence
\[
\lim_{h\downarrow0}h^{-1/2}\operatorname{Tr}(E_h)
=\frac{L(\sqrt2-1)|\zeta(1/2)|}{2\sqrt\pi}.
\]

## Relationship to prior work
Nicholas Castillo's 2026 sampled-resolvent paper establishes the rectangle rule, trapezoid correction, dyadic identity, operator-norm rates, and Romberg extrapolation on smoother domains; specifically its Corollary 5.2 and Proposition 5.10 concern operator/vector norms, not spectral \(\mathcal S_p\) norms, positive two-grid trace-class compactification, or the Weyl/zeta constants proved here. These sampling identities and the classical spectral Weyl law are treated as prior input, not claimed as discoveries. Castillo's earlier dyadic spectral-zeta paper concerns reconstruction of spectral data from unitary samples; its accessible abstract does not assert the present heat-semigroup two-grid Schatten-error constants. The classical Weyl eigenvalue-counting theorem determines the counting input but not this particular filter's sharp coefficient without an additional spectral integration argument.

## Limitations
The claims require a nonnegative **self-adjoint** generator with compact resolvent and a genuine counting-law coefficient. They do not cover unbounded continuous-spectrum generators, nonnormal semigroups, operators without Weyl asymptotics, or noisy/truncated observational records. The strong Schatten error diverges at and below the spectral dimension for every fixed mesh; a bound in operator norm does not change this. The relevant preexisting literature may contain an equivalent general spectral trace theorem or an unindexed explicit filter calculation, so bibliographic priority is not independently established.

## References
1. N. Castillo, *Sampled resolvents of \(C_0\)-semigroups: aliasing and sharp rates on the Crandall–Pazy scale*, arXiv:2611.15563v1 (first public 2026-11-11), https://arxiv.org/html/2611.15563v1.
2. N. Castillo, *Dyadic resolvent representations of self-adjoint operators: propagator expansions, spectral measures, and zeta functions*, arXiv:2607.21278 (first public 2026-07-23), https://arxiv.org/abs/2607.21278.
3. R. L. Frank and S. Larson, *Two-term spectral asymptotics for the Dirichlet Laplacian in a Lipschitz domain*, arXiv:1901.09771 (2019), https://arxiv.org/abs/1901.09771.
4. NIST Digital Library of Mathematical Functions, Hurwitz and Riemann zeta identities, https://dlmf.nist.gov/25.
