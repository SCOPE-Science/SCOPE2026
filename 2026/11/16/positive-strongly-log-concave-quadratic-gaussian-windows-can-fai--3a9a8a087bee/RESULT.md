# Positive strongly log-concave quadratic–Gaussian windows can fail at Gabor redundancy two

## Finding
For every real \(0<\gamma\le \pi^2/6\), define
\[
\Theta(\gamma)=\sum_{k\in\mathbb Z}(-1)^k e^{-\gamma k^2},\qquad
c_\gamma=\frac{\Theta'(\gamma)}{\Theta(\gamma)},\qquad
g_\gamma(t)=(t^2+c_\gamma)e^{-\gamma t^2}.
\]
Then \(\Theta(\gamma)>0\) and \(\gamma c_\gamma>1\). In particular \(g_\gamma\) is everywhere positive, even, real analytic, Schwartz, strictly decreasing on the positive half-line, and **uniformly strongly log-concave**:
\[
\frac{d^2}{dt^2}\log g_\gamma(t)
\le-2\left(\gamma-\frac1{c_\gamma}\right)<0
\quad (t\in\mathbb R).
\]
Despite this regularity, the density-two Gabor system
\[
\mathcal G_\gamma=\left\{e^{2\pi i mt}g_\gamma(t-j/2):m,j\in\mathbb Z\right\}
\]
**fails to be a frame for \(L^2(\mathbb R)\)**. A nonzero alternating integer-shift combination gives the exact obstruction:
\[
H_\gamma(t)=\sum_{k\in\mathbb Z}(-1)^k g_\gamma(t-k),
\qquad H_\gamma(j/2)=0\quad(j\in\mathbb Z).
\]
For example, at \(\gamma=1\), the exact theta-quotient \(c_1\) has numerical value \(1.9674011530804077752\ldots\); the resulting strictly positive, strongly log-concave window still has a non-frame at time step \(1/2\) and frequency step \(1\).

## Assumptions and scope
All sums are absolutely convergent for every fixed \(\gamma>0\); derivatives converge locally uniformly in \(\gamma\). The Fourier transform uses \(\widehat f(\xi)=\int_\mathbb R f(t)e^{-2\pi i\xi t}\,dt\). The Zak transform uses
\[
Zf(x,\omega)=\sum_{k\in\mathbb Z}f(x-k)e^{2\pi i k\omega}.
\]
A Gabor frame means there exist \(A,B\) with \(0<A\le B<\infty\) such that, for every \(f\in L^2(\mathbb R)\),
\[
A\|f\|_2^2\le\sum_{m,j\in\mathbb Z}
\left|\left\langle f,e^{2\pi i m\cdot}g_\gamma(\cdot-j/2)\right\rangle\right|^2\le B\|f\|_2^2.
\]
The theorem asserts failure only for this specified rectangular lattice and family of window parameters. The interval \(0<\gamma\le\pi^2/6\) is an explicit sufficient range for the asserted strong log-concavity, not a claimed maximal parameter range.

## Proof
**1. Positivity and exact coefficient from theta duality.** Poisson summation for an alternating Gaussian yields
\[
\Theta(\gamma)=\sqrt{\frac\pi\gamma}
\sum_{m\in\mathbb Z}\exp\left(-\frac{\pi^2(m+1/2)^2}{\gamma}\right)>0.
\]
Define the probability weights proportional to the summands on the right and their second moment \(M_\gamma\). Every dual lattice point satisfies \((m+1/2)^2\ge1/4\), with strict inequality at some points of positive weight. Therefore \(M_\gamma>1/4\), and differentiating the absolutely convergent Poisson series gives
\[
c_\gamma=-\frac1{2\gamma}+\frac{\pi^2}{\gamma^2}M_\gamma
> -\frac1{2\gamma}+\frac{\pi^2}{4\gamma^2}.
\]
If \(0<\gamma\le\pi^2/6\), the rightmost quantity is at least \(1/\gamma\). The strict inequality persists at the endpoint, so \(c_\gamma>1/\gamma>0\).

**2. Shape and quantitative strong log-concavity.** Positivity, evenness, real analyticity and Schwartz decay are immediate from \(c_\gamma>0\). Direct differentiation gives
\[
(\log g_\gamma)''(t)=
\frac{2(c_\gamma-t^2)}{(c_\gamma+t^2)^2}-2\gamma
\le \frac2{c_\gamma}-2\gamma<0.
\]
Indeed \((c-t^2)/(c+t^2)^2\le1/c\) whenever \(c>0\). Since the log derivative vanishes at the origin and has strictly negative derivative on \(\mathbb R\), \(g_\gamma\) is strictly decreasing on \((0,\infty)\), with a unique maximum at the origin.

**3. A complete half-integer zero lattice of a nontrivial translate combination.** Put
\[
H_\gamma(t)=\sum_{k\in\mathbb Z}(-1)^k g_\gamma(t-k).
\]
It converges absolutely and locally uniformly with all derivatives and satisfies \(H_\gamma(t+1)=-H_\gamma(t)\). The definition of \(c_\gamma\) implies
\[
H_\gamma(0)=\sum_k(-1)^k(k^2+c_\gamma)e^{-\gamma k^2}
=-\Theta'(\gamma)+c_\gamma\Theta(\gamma)=0.
\]
Evenness of \(g_\gamma\) pairs the \(k\) and \(1-k\) summands at \(t=1/2\) with opposite signs, whence \(H_\gamma(1/2)=0\). Antiperiodicity proves \(H_\gamma(j/2)=0\) for every integer \(j\).

For completeness the sum is not identically zero. Poisson summation gives its antiperiodic Fourier coefficients \(\widehat g_\gamma(n+1/2)\) for \(n\in\mathbb Z\), with
\[
\widehat g_\gamma(\xi)=\sqrt{\frac\pi\gamma}
 e^{-\pi^2\xi^2/\gamma}
\left(c_\gamma+\frac1{2\gamma}-\frac{\pi^2\xi^2}{\gamma^2}\right).
\]
The parenthetical quadratic has at most two real zeros, whereas there are infinitely many distinct half-integer frequencies. Therefore at least one Fourier coefficient is nonzero and \(H_\gamma\not\equiv0\).

**4. The Zak-fiber frame obstruction.** The absolutely convergent Zak transform satisfies
\[
Zg_\gamma(0,1/2)=H_\gamma(0)=0,\qquad
Zg_\gamma(1/2,1/2)=H_\gamma(1/2)=0.
\]
At the lattice \((a,b)=(1/2,1)\), even-index and odd-index translations give the two Zak fibers. Specifically, for Schwartz \(g\), applying Fourier-series Parseval to the integer modulations and the even/odd translation classes yields
\[
\sum_{m,j\in\mathbb Z}|\langle f,M_mT_{j/2}g\rangle|^2
=\int_0^1\!\int_0^1 |Zf(x,\omega)|^2
\bigl(|Zg(x,\omega)|^2+|Zg(x-1/2,\omega)|^2\bigr)
\,d\omega\,dx.
\]
The change from \(x+1/2\) to \(x-1/2\) only alters an irrelevant Zak quasiperiodic phase. Both nonnegative summands of this continuous fiber weight vanish at \((x,\omega)=(0,1/2)\). Hence the weight has essential infimum zero. As the Zak transform is unitary, no strictly positive lower frame bound can exist. Alternatively, the bounded sequence \(((-1)^k)_{k\in\mathbb Z}\) gives the exact noninjective pre-Gramian in Lemvig's Proposition 2.1, evaluated on \(\frac12\mathbb Z\). This concludes the claim for every parameter in the stated range.

## Verification
Execute `python3 verify.py` after installing `mpmath` if needed. The checker uses high-precision direct and dual Gaussian sums to compare \(\Theta\) and \(\Theta'\), checks the strict dual-moment bound, verifies numerical cancellation at eleven half-integer nodes, samples the log-curvature bound, and computes a nonzero alternating-shift value away from the nodes. It passed 132 individual checks at six values of \(\gamma\), including \(\gamma=\pi^2/6\). All full-parameter assertions are established analytically in the preceding proof; finite arithmetic checks cannot establish the infinite theorem or publication priority.

## Relationship to prior work
Lemvig (arXiv:2611.05337v1, first posted 3 November 2026) proves that polynomial-times-Gaussian windows of degree \(n\) frame every irrational lattice product below one and every rational product \(p/q<1\) with \(q-p>n\). The present degree-two window at \(ab=1/2\) lies precisely outside those sufficient ranges; that source supplies a compatible pre-Gramian characterization but not the explicit positive and strongly log-concave obstruction proved here.

Ulanovskii and Zlotnikov (arXiv:2606.31450) prove parity-driven nonuniqueness and show existence of degree-at-most-\(N\) nonframe generators at product \(1/(N+1)\). Their degree-two construction concerns product \(1/3\), not the present product \(1/2\) with strict shape constraints. Established first-Hermite and Gaussian–first-Hermite classifications apply to degree-one windows; the positive Gaussian scale-mixture class has a unique Zak zero and therefore produces redundancy-two frames. Neither result implies a nonframe in the present even degree-two, strongly log-concave class.

Janssen's earlier sufficient criteria for positive even windows use a stronger superconvexity or special Zak-zero hypothesis, not mere strong log-concavity. The present construction shows why one cannot infer redundancy-two frame behavior from positivity, analytic regularity, unimodality, or uniform log-concavity alone.

## Limitations
This is a concrete one-parameter family, not a characterization of all log-concave windows or of all Gabor lattices. The range \(\gamma\le\pi^2/6\) comes from a simple explicit dual-moment estimate and need not be optimal. No optimal frame bounds for perturbed windows are determined. The nonframe property is exact and no numerical cutoff is used. An equivalent older theta-function construction could exist in less directly indexed Gabor or shift-invariant-sampling literature; accessible literature and a mathematical research-index comparison reduce but cannot eliminate publication-priority risk. Independent audit has not been performed.

## References
1. J. Lemvig, *On the Gabor frame set of polynomial–Gaussian windows*, arXiv:2611.05337v1, 3 November 2026. https://arxiv.org/html/2611.05337v1
2. A. Ulanovskii and I. Zlotnikov, *Periodic Non-uniqueness Sets for Shift-invariant Spaces and Parity-Based Obstructions to the Frame Property for Gabor Systems*, arXiv:2606.31450, 30 June 2026. https://arxiv.org/abs/2606.31450
3. A. J. E. M. Janssen, *Zak Transforms With Few Zeros and the Tie*, 2001. https://doi.org/10.1007/978-1-4612-0133-5_3
4. A. J. E. M. Janssen, *On Generating Tight Gabor Frames at Critical Density*, Journal of Fourier Analysis and Applications 9 (2003), 175–214. https://doi.org/10.1007/s00041-003-0011-3
