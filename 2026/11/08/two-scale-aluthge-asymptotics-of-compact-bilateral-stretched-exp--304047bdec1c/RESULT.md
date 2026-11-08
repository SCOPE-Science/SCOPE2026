# Two-scale Aluthge asymptotics of compact bilateral stretched-exponential shifts

## Finding

Let \(a>0\), \(\alpha>0\), and \(0<t<1\) be fixed. On the complex Hilbert space \(\ell^2(\mathbb Z)\), define the positive-weight bilateral shift by
\[
We_k=\exp(-a|k|^\alpha)e_{k+1}\qquad(k\in\mathbb Z).
\]
Let \(W_n=\Delta_t^n(W)\), where \(\Delta_t(T)=|T|^tU|T|^{1-t}\) for the polar decomposition \(T=U|T|\), and let \(X_n\sim\operatorname{Bin}(n,t)\), \(\mu_n=nt\), \(\sigma_n=\sqrt{nt(1-t)}\). All \(W_n\) are compact and belong to every Schatten class \(\mathcal S_p\), \(0<p<\infty\). The following constitute one two-scale classification theorem.

**Exact weights and general sharp logarithmic decay.** For every integer \(k\) and \(n\ge0\),
\[
W_ne_k=\exp\bigl(-a\,\mathbb E|k+X_n|^\alpha\bigr)e_{k+1}.
\]
With \(Z\) standard normal and \(m_\alpha=\mathbb E|Z|^\alpha=2^{\alpha/2}\Gamma((\alpha+1)/2)/\sqrt\pi\),
\[
\lim_{n\to\infty}\frac{-\log\|W_n\|}{\sigma_n^\alpha}=a m_\alpha.
\]

**Diffuse Laplace spectral window.** At \(\alpha=1\), write \(c=\sqrt{2/\pi}\). For every fixed \(z\in\mathbb R\), set \(k_n(z)=\lfloor-\mu_n+z\sqrt{\sigma_n}\rfloor\). Then, locally uniformly in \(z\),
\[
\exp(a c\sigma_n)\,\|W_ne_{k_n(z)}\|\longrightarrow\exp(-a c z^2/2).
\]
Moreover,
\[
\|W_n\|=\exp(-a c\sigma_n)(1+o(1)),
\qquad
\|W_n\|_{\mathcal S_p}=\exp(-a c\sigma_n)\,\sigma_n^{1/(2p)}
\left(\frac{2\pi}{a p c}\right)^{1/(2p)}(1+o(1)),
\]
for each fixed \(0<p<\infty\). In particular, the Schatten-to-operator norm ratio diverges at the exact rate \(\sigma_n^{1/(2p)}\), corresponding to \(n^{1/(4p)}\).

**Pinned quadratic window.** At \(\alpha=2\), for all \(n\ge0\),
\[
W_ne_k=\exp\bigl(-a[\sigma_n^2+(k+\mu_n)^2]\bigr)e_{k+1},
\qquad
\|W_n\|=\exp\bigl(-a[\sigma_n^2+\operatorname{dist}(\mu_n,\mathbb Z)^2]\bigr),
\]
and
\[
\|W_n\|_{\mathcal S_p}=\exp(-a\sigma_n^2)
\left(\sum_{j\in\mathbb Z}\exp[-ap(j+\mu_n)^2]\right)^{1/p}.
\]
If \(t\) is irrational, the cluster set of \(\exp(a\sigma_n^2)\|W_n\|\) is exactly \([\exp(-a/4),1]\); the corresponding normalized Schatten cluster set is the range of the continuous nonconstant one-periodic Gaussian theta sum \(\bigl(\sum_{j\in\mathbb Z}e^{-ap(j+x)^2}\bigr)^{1/p}\) for \(x\in[0,1]\). For rational \(t\), these sequences have finite periodic sets of values. Thus the \(\alpha=1\) singular-value window spreads over order \(\sqrt{\sigma_n}\) lattice sites, whereas the \(\alpha=2\) window remains pinned to order-one sites.

## Assumptions and scope

The shift is bilateral, indexed by all integers, and its weights are strictly positive, decreasing to zero at both ends. The parameters \(a,\alpha,t,p\) are held fixed when \(n\to\infty\); \(0<t<1\) excludes the degenerate endpoint transformations. The Schatten quasi-norm formula remains valid for \(0<p<1\). A weighted shift with coefficients \(u_k\) has singular values equal to the decreasing rearrangement of \((|u_k|)_{k\in\mathbb Z}\), so \(\|W_n\|=\max_k|u_k|\) and \(\|W_n\|_{\mathcal S_p}^p=\sum_k|u_k|^p\). The initial shift is quasinilpotent: for every block of \(n\) consecutive integers, a fixed positive proportion have absolute value at least a constant times \(n\), giving \(\|W^n\|\le\exp(-c_\alpha a n^{\alpha+1})\) for some \(c_\alpha>0\).

## Proof

**1. Iteration.** The polar partial isometry of \(W\) is the bilateral forward unitary \(Ue_k=e_{k+1}\). For any positive weighted shift with weights \((w_k)\), a single generalized Aluthge transform replaces them by \(w_k^{1-t}w_{k+1}^t\). Therefore the logarithmic weights undergo repeated averaging by \((1-t)I+tS\), where \(S\) translates the index one step. The binomial theorem yields the exact formula displayed above. Positivity and superpolynomial decay of \(w_k\) at both ends imply every iterate belongs to every \(\mathcal S_p\).

**2. Universal logarithmic rate.** Define \(Y_n=(X_n-\mu_n)/\sigma_n\), which converges in law to \(Z\). Since the centered binomial variables possess uniformly bounded moments of every fixed order (e.g., via Hoeffding's subgaussian estimate), for every bounded sequence \((h_n)\) with \(h_n\to h\),
\[
\mathbb E|Y_n+h_n|^\alpha\longrightarrow\mathbb E|Z+h|^\alpha.
\]
For \(h\ne0\) and \(r>0\), a symmetric strictly unimodal Gaussian satisfies \(\mathbb P(|Z+h|<r)<\mathbb P(|Z|<r)\). Layer-cake integration for \(|\cdot|^\alpha\) thus implies \(\mathbb E|Z+h|^\alpha>m_\alpha\). This strict minimum applies also when \(0<\alpha<1\), without a convexity assumption. Choosing an integer \(k\) nearest \(-\mu_n\) gives the upper bound for the minimum normalized expectation. Conversely, if \(|k+\mu_n|/\sigma_n\to\infty\), then \(\mathbb E|k+X_n|^\alpha/\sigma_n^\alpha\to\infty\): on an event where \(|Y_n|\le R\), whose probability is bounded below for a suitable fixed \(R\), the absolute value exceeds \(|k+\mu_n|/\sigma_n-R\). Thus the minimizing centers have bounded scaled displacement, and every subsequential center has the unique limiting minimizer zero. This proves the norm limit.

**3. Absolute deviation and the local central window.** Set \(F_n(x)=\mathbb E|X_n-x|\), and \(G_n(x)=\mathbb E|\mu_n+\sigma_nZ-x|\). For \(m=\lfloor\mu_n\rfloor\), the binomial recursion
\[
(j-nt)\,\mathbb P(X_n=j)=nt(1-t)\bigl[\mathbb P(X_{n-1}=j-1)-\mathbb P(X_{n-1}=j)\bigr]
\]
(taking the missing endpoint probabilities to be zero) telescopes to the **exact identity**
\[
F_n(\mu_n)=2\sigma_n^2\,\mathbb P(\operatorname{Bin}(n-1,t)=m).
\]
The fixed-parameter local Stirling expansion at \(m=nt+O(1)\) gives \(F_n(\mu_n)=c\sigma_n+O(\sigma_n^{-1})\). Berry--Esseen's uniform binomial CDF estimate gives, for all real \(x\),
\[
\big|[F_n(x)-F_n(\mu_n)]-[G_n(x)-G_n(\mu_n)]\big|
\le C_t|x-\mu_n|/\sigma_n.
\]
This follows by integrating the distribution-function formulas for their derivatives, so it remains true across integer locations by absolute continuity. Direct Gaussian differentiation gives \(G_n''(\mu_n)=c/\sigma_n\), and uniformly for bounded \(z\),
\[
G_n(\mu_n+z\sqrt{\sigma_n})-G_n(\mu_n)
=cz^2/2+O_z(\sigma_n^{-1}).
\]
Changing an argument by a bounded amount affects the preceding differences by \(o(1)\) on the stated local scale. The coefficient profile follows.

To pass from local convergence to a full Schatten sum, observe that for \(h\in\mathbb R\), the Gaussian absolute-deviation defect satisfies
\[
G_n(\mu_n+h)-G_n(\mu_n)\ge c_0\min\{h^2/\sigma_n,|h|\}
\]
for a fixed positive \(c_0\). The Berry--Esseen comparison implies, for all sufficiently large \(n\),
\[
F_n(\mu_n+h)-F_n(\mu_n)
\ge c_1\min\{h^2/\sigma_n,|h|\}-C_1/\sigma_n
\]
by completing the square for \(|h|\le\sigma_n\), and absorbing the linear error when \(|h|\ge\sigma_n\). It follows that the minimum over integer \(x\) is \(c\sigma_n+O(\sigma_n^{-1})\), since an integer within distance one of \(\mu_n\) supplies the matching upper bound. This also supplies a Gaussian-in-the-center domination for the normalized sum and an exponential bound beyond \(|h|\ge\sigma_n\). Hence the Riemann-sum limit is
\[
\frac{\exp(apc\sigma_n)}{\sqrt{\sigma_n}}
\sum_{k\in\mathbb Z}\exp[-apF_n(-k)]
\longrightarrow\int_{\mathbb R}\exp(-apc z^2/2)\,dz
=\sqrt{\frac{2\pi}{apc}}.
\]
Taking \(p\)-th roots and using the integer minimum gives the stated norm and Schatten asymptotics.

**4. Quadratic pinning and arithmetic modulation.** The identity
\(\mathbb E(k+X_n)^2=(k+\mu_n)^2+\sigma_n^2\)
immediately gives the exact quadratic coefficients. Summing their \(p\)-th powers yields the theta expression. The distance-to-integers function maps a dense orbit \(\{nt\bmod1\}\) for irrational \(t\) onto a set dense in \([0,1/2]\), and is periodic for rational \(t\). Continuity of the Gaussian theta sum gives the stated cluster sets. The theta sum is not constant, since its Poisson series has a strictly positive first Fourier coefficient \(\sqrt{\pi/(ap)}e^{-\pi^2/(ap)}\); this equality can equally be obtained by integrating one period of the Gaussian against the first Fourier mode.

## Verification

The self-contained companion script `check.py`, executable using Python 3 without third-party packages, checks 3,276 finite identities or diagnostics: exact rational recursions and binomial convolution, exact quadratic moments, the telescoping absolute-deviation identity at several parameter values, and the predicted leading Laplace norm and Schatten factors at increasing iteration counts. All checks passed. These finite tests do not establish asymptotic quantifiers; those follow from the proof above. Reproducibility: run `python3 check.py` in a directory containing this file and the companion script.

## Relationship to prior work

Bala's February 2026 paper proves norm convergence of iterated Aluthge transforms for compact operators; it does not state sharp rates for this bilateral family. The 2005 work of Antezana, Massey and Stojanoff develops generalized transforms and Schatten ideals. The later Stanković paper, first made public November 5, 2026, establishes singular-value and Schatten convergence principles for compact operators, including the general binomial weights of a **unilateral** shift in Proposition 5.8, but neither a quantitative interior Gaussian-width law nor the exact bilateral arithmetic pinning formula. The binomial averaging identity is not claimed as new. Relevant earlier unilateral stretched-exponential boundary results have a fixed-edge singular-value window; they do not imply the bilateral \(\sqrt{\sigma_n}\)-width result. The contribution here is the explicit two-scale quantitative classification and the sharp constants for bilateral compact shifts.

## Limitations

All parameters are fixed. No uniform statement is made as \(t\to0\), \(t\to1\), \(a\to0\), \(p\to0\), or \(\alpha\to0\). The full sharp Schatten prefactor is proved for \(\alpha=1\), while \(\alpha=2\) admits an exact formula and the universal logarithmic rate covers general \(\alpha>0\). No claim is made for arbitrary bilateral weight profiles or optimal rates in every Schatten ideal. Possible priority overlap with broader discrete heat-kernel Laplace asymptotics remains to be investigated.

## References

1. N. Bala, *The iterated Aluthge Transforms of compact operators*, arXiv:2602.07916, first public 2026-02-08. https://arxiv.org/abs/2602.07916
2. J. Antezana, P. Massey, and D. Stojanoff, *\(\lambda\)-Aluthge transforms and Schatten ideals*, 2005. https://sedici.unlp.edu.ar/handle/10915/83154
3. H. Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728, first public 2026-11-05 (read for priority comparison; not used to establish source-date eligibility). https://arxiv.org/abs/2611.07728
4. S. Lahiri, S. Ojha, and R. Birbonshi, *Iterated Aluthge transforms of some composition operators on weighted Bergman spaces*, arXiv:2604.27762, 2026-04-30. https://arxiv.org/abs/2604.27762
