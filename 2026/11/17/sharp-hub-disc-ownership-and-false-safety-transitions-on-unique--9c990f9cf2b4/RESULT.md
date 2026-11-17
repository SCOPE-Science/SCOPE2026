# Sharp hub-disc ownership and false-safety transitions on unique-hub networks

## Finding

Let \(G\) be any finite connected simple undirected graph with at least three vertices and a unique maximum-degree vertex \(h\), of degree \(\Delta\ge 2\). Write \(A\) for its adjacency matrix, \(d_i\) for each vertex degree, \(D=\operatorname{diag}(d_i)\), and \(\varrho=\lambda_{\max}(A)\). For any \(q\ge 0\), consider the positive-interaction network flow \(\dot z=J_qz\), with

\[
J_q=-I+D^{-q}AD^q.
\]

Set

\[
R_h(q)=\sum_{j\sim h}\left(\frac{d_j}{\Delta}\right)^q.
\]

There are **unique sharp exponents** \(0<q_{\mathrm{spec}}<q_{\mathrm{safe}}<\infty\) specified by

\[
R_h(q_{\mathrm{spec}})=\varrho,\qquad
R_h(q_{\mathrm{safe}})=1.
\]

The dominant eigenvalue \(\varrho-1>0\) belongs to the hub-row Gershgorin disc **if and only if** \(0\le q\le q_{\mathrm{spec}}\); for \(q>q_{\mathrm{safe}}\), that entire hub disc is strictly in the open left half-plane, although the flow is exponentially unstable. For fixed \(G\), its radius tends to zero as \(q\to\infty\), while its complete spectrum is independent of \(q\). Thus, on each fixed eligible graph, the hub radius can be made arbitrarily small without changing the spectrum; the disagreement between the hub disc and the actual growth rate becomes unbounded along growing stars.

On the star \(K_{1,n}\), \(n\ge2\), the transitions are exactly \(q_{\mathrm{spec}}=1/2\) and \(q_{\mathrm{safe}}=1\), whereas its dominant growth exponent \(\sqrt n-1\) becomes arbitrarily large with \(n\). These are exact statements for the displayed flow; they concern **one-row screening**, never the valid all-row Gershgorin theorem.

## Assumptions and scope

The graph is finite, simple, connected, undirected and unweighted; the maximum-degree vertex is unique and has degree at least two. All vertices then have positive degrees, so every diagonal matrix power is well-defined. The interaction is cooperative and fixed in time. In the degree-exponent Jacobian notation of Patil--Meena, this is the special case \((\eta,\mu,\nu,\rho)=(0,0,-q,q)\), with unit interaction weights and diagonal value \(-1\). The system is the exact linear ODE with matrix \(J_q\); no nonlinear steady-state realization, randomness, scale-free degree distribution or asymptotic network limit is assumed. The upper bounds and the star thresholds are not asserted for a hub tied with another maximum-degree vertex.

Define the row-\(h\) Gershgorin disc as \(\mathcal D_h(q)=\{\lambda\in\mathbb C:|\lambda+1|\le R_h(q)\}\). The phrase **false-safe** means the condition \(-1+R_h(q)<0\) holds for this **single** disc despite a positive spectral abscissa; it does not mean that the genuine Gershgorin theorem predicts stability.

## Proof

**Step 1 (the exact spectral invariant).** Since \(D^q\) is invertible,

\[
D^qJ_qD^{-q}=A-I.
\]

Consequently every \(J_q\) has the real spectrum of \(A-I\), and its spectral abscissa is \(\alpha(J_q)=\varrho-1\). Connectedness ensures irreducibility of the nonnegative symmetric \(A\). The Perron row-sum inequality gives \(\varrho<\Delta\), strictly because not all graph degrees can equal \(\Delta\) when the maximum is unique. On the other hand, take the trial vector \(v\) with \(v_h=\sqrt\Delta\), \(v_j=1\) for \(j\sim h\), and \(v_j=0\) otherwise. Its norm squared is \(2\Delta\); every hub--neighbor edge contributes exactly \(2\sqrt\Delta\) to \(v^TAv\). Other edges among neighbors contribute nonnegative terms. The Rayleigh quotient therefore gives \(\varrho\ge\sqrt\Delta>1\). In particular, \(\alpha(J_q)>0\) for every \(q\ge0\).

**Step 2 (the exact hub disc).** Its center is \(-1\), and its nonnegative off-diagonal entries in row \(h\) are \((d_j/\Delta)^q\) for neighbors \(j\). Uniqueness of the degree maximum implies \(0<d_j/\Delta<1\) for every such neighbor. Thus \(R_h\) is continuous, strictly decreasing, and tends to zero; at \(q=0\) it is \(\Delta\). From \(\Delta>\varrho>1\), the intermediate-value theorem yields unique finite roots of \(R_h(q)=\varrho\) and \(R_h(q)=1\), with \(0<q_{\mathrm{spec}}<q_{\mathrm{safe}}\).

**Step 3 (ownership and false safety).** The dominant eigenvalue is the positive real number \(\varrho-1\), whose distance from the center \(-1\) is exactly \(\varrho\). Hence it lies in \(\mathcal D_h(q)\) exactly when \(R_h(q)\ge\varrho\), or \(q\le q_{\mathrm{spec}}\). The entire hub disc lies in the open left half-plane exactly when \(-1+R_h(q)<0\), or \(q>q_{\mathrm{safe}}\). Meanwhile Step 1 still gives the positive growth exponent \(\varrho-1\). Moreover, with \(\theta=\max_{j\sim h}d_j/\Delta<1\), the explicit estimate \(R_h(q)\le\Delta\theta^q\) shows geometric decay of the misleading disc radius as \(q\to\infty\). The other row discs cannot all be left-half-plane discs, because the true positive eigenvalue must lie in their union.

**Step 4 (sharp star cutoffs).** On \(K_{1,n}\), the hub has degree \(n\) and each leaf degree one. Therefore \(R_h(q)=n^{1-q}\), every leaf radius is \(n^q\), and the exact full spectrum is

\[
\left\{-1+\sqrt n,\,-1-\sqrt n,\,\underbrace{-1,\ldots,-1}_{n-1\ \mathrm{times}}\right\}.
\]

The dominant eigenvalue belongs to the hub disc precisely for \(n^{1-q}\ge\sqrt n\), or \(q\le1/2\), and belongs to each leaf disc precisely for \(n^q\ge\sqrt n\), or \(q\ge1/2\). The hub disc is strictly left of zero precisely when \(n^{1-q}<1\), or \(q>1\). Its rightmost point tends to \(-1\) for each fixed \(n\) as \(q\to\infty\); for fixed \(q>1\) and \(n\to\infty\), that point also tends to \(-1\) while the true growth rate \(\sqrt n-1\to\infty\). All claimed thresholds are necessary and sufficient, including the equality cases.

## Verification

The standalone Python/SymPy checker `verify.py` evaluates exactly the diagonal similarity, complete star characteristic polynomial, and star disc ownership/false-safe cutoffs for twenty-four star parameter pairs. It also checks three weighted-by-degree matrix realizations on a non-star, uniquely maximum-degree graph. Numerical finite-graph root calculations corroborate the general ordering \(q_{\mathrm{spec}}<q_{\mathrm{safe}}\) in three examples. The observed output is:

```
VERIFY_OK similarity_cases=27 star_cases=24 nonstar_cases=3
VERIFY_OK universal_threshold_examples=3
```

The finite checks are not a proof for all graphs or all real \(q\). Steps 1--4 are the complete analytic argument.

## Relationship to prior work

Patil and Meena (2026, equations 6, 10--14, and Sections 3--6) propose the hub-associated Gershgorin disc as a computational shortcut for network stability, and explicitly observe some empirical misclassifications when the dominant eigenvalue is not inside that disc. The present result gives a graph-uniform, sharp and arbitrarily severe **exact boundary** for that shortcut on a fixed degree-exponent family. It does not dispute the standard all-row sufficient condition.

Meena et al. (2020 preprint, supplementary Section 2.1) already give the star Jacobian and its dominant eigenvalue; the displayed star spectrum is therefore treated here as a check and tool, **not** as a new eigenvalue formula. Dawn et al. (2025 preprint, Section II) explicitly identify diagonal symmetrization for same-sign factorizable Jacobian weights; diagonal similarity itself is likewise prior background, **not** claimed new. The distinction is the exact two-transition **hub-disc** theorem on *every* finite connected graph with one strict degree maximum, and the arbitrarily strong false-safe gap.

## Limitations

This is a counterexample and sharp scope test for using **only** a hub row, not a failure of Gershgorin's theorem itself. It supplies no probabilistic error rates for a particular random graph ensemble and no result for graphs with tied maximum degrees. It does not show failure of every possible degree-exponent classifier or of full-matrix spectral analysis. Strictly speaking the linear matrices are valid members of the degree-exponent Jacobian family, but a specific nonlinear physical realization and its biologically admissible state region are not asserted. Prioritization relative to all classical work on diagonally scaled Gershgorin discs remains an external historical question.

## References

1. Y. P. Patil and C. Meena, *Stability of large dynamical systems using Gershgorin Disc Theorem* (2026), arXiv:2611.08692v1, https://arxiv.org/html/2611.08692v1 (first public 2026-11-05).
2. C. Meena, C. Hens, S. Acharyya, S. Haber, S. Boccaletti and B. Barzel, *Emergent stability in complex network dynamics* (2020 preprint), arXiv:2007.04890, supplementary Section 2.1, https://arxiv.org/abs/2007.04890.
3. S. Dawn, S. Ghosh, C. Meena, T. Rogers and C. Hens, *Origins of Instability in Dynamical Systems on Undirected Networks* (2025 preprint), arXiv:2512.09765, Section II, https://arxiv.org/abs/2512.09765.
