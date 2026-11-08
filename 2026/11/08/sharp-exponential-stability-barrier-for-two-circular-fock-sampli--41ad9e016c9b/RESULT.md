# Sharp exponential stability barrier for two circular Fock sampling orbits

## Finding
Let \(\mathcal P_n\) be the polynomials of degree at most \(n\) in the Bargmann–Fock space with norm
\[
\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z).
\]
At two independently selected nonnegative squared radii \(t_1,t_2\), sample at the \(n+1\) equally spaced points on each circle, using full-Fock coherent-state weights. The average-per-orbit measurement form is
\[
\mathcal S_{n;t_1,t_2}(f)=\frac1{n+1}\sum_{j=1}^2\sum_{\ell=0}^n e^{-t_j}\left|f\big(\sqrt{t_j}e^{2\pi i\ell/(n+1)}\big)\right|^2.
\]
The complete Gram spectrum, in the orthonormal monomial basis \(z^k/\sqrt{k!}\), is
\[
\lambda_k=e^{-t_1}\frac{t_1^k}{k!}+e^{-t_2}\frac{t_2^k}{k!},\qquad 0\le k\le n,
\]
with \(0^0=1\). Put \(B_n=\sup_{t_1,t_2\ge0}\min_{0\le k\le n}\lambda_k\). Then
\[
\boxed{\lim_{n\to\infty}-n^{-1}\log B_n=R_*=0.1055733636919129\ldots.}
\]
Precisely, let \(\rho>e\) be the unique root of \(\rho-1=e\log\rho\), and let \(R_*\) be the unique root in \((0,1/\rho)\) of
\[
(\rho-1)R_*-1-\log(\rho R_*)=0.
\]
Then \(\rho=5.7591317337688\ldots\). The choice
\[
 t_1=nR_*,\qquad t_2=n\rho R_*
\]
attains the sharp exponential rate. Moreover, for **every** sequence of radii whose achieved lower-frame exponent tends to \(R_*\), the unordered pair of normalized squared radii converges to
\[
\boxed{\{t_1/n,t_2/n\}\longrightarrow\{R_*,\rho R_*\}}
\]
(with the sense of convergence after sorting). Thus this rate-optimal two-orbit radial design is asymptotically unique.

## Assumptions and scope
The result holds for every integer \(n\ge1\) at the exact finite spectral level, and in the limit as \(n\to\infty\). Each orbit uses exactly \(n+1\) equally spaced angular locations, and both orbit contributions have fixed equal weight. Angular rotation of either orbit leaves the spectrum unchanged. The radial parameters may depend arbitrarily on \(n\), including degenerate radii; the two-orbit optimum is over **all** nonnegative choices. These are full-Fock-normalized point measurements, not the degree-truncated kernel normalization sometimes used for Marcinkiewicz–Zygmund families. Multiplying the measurement form by \(n+1\) changes neither the exponential rate nor its optimal radii.

## Proof
**1. Exact diagonalization.** The monomials \(e_k(z)=z^k/\sqrt{k!}\), \(0\le k\le n\), are orthonormal. For distinct \(k,h\in\{0,\dots,n\}\), the discrete angular average of \(e^{2\pi i(k-h)\ell/(n+1)}\) vanishes. Hence the sampling Gram is diagonal with the stated Poisson-mass eigenvalues. This identity holds even at zero radius, with the natural monomial convention.

**2. The continuous rate problem.** For \(s\in[0,1]\) and \(a>0\), define
\[
 I(s\mid a)=a-s+s\log(s/a),\quad I(0\mid a)=a.
\]
Extend by \(I(0\mid0)=0\), \(I(s\mid0)=+\infty\) for \(s>0\), and \(I(s\mid\infty)=+\infty\) for finite \(s\). The normalized Poisson mass satisfies, uniformly for \(0\le k\le n\) at each fixed \(a>0\),
\[
 \log\left(e^{-na}(na)^k/k!\right)=-n I(k/n\mid a)+O(\log(n+1)).
\]
The prospective minimax exponent is
\[
 \inf_{a,b\ge0}\max_{0\le s\le1}\min\{I(s\mid a),I(s\mid b)\}.
\]

**3. Solve the one-dimensional covering problem exactly.** For a level \(R>0\), the sublevel set \(\{s:I(s\mid a)\le R\}\) is an interval (possibly clipped to \([0,1]\)) because \(I\) is strictly convex in \(s>0\). A single sublevel interval containing both \(0\) and \(1\) needs \(R\ge1/e\): indeed \(I(0\mid a)=a\) and \(I(1\mid a)=a-1-\log a\) have equal minimax value at \(a=1/e\).

Consider \(R<1/e\). Label the two centers so that the first sublevel interval covers \(0\) and the second covers \(1\). The first has \(a\le R\). Its right endpoint is maximal when \(a=R\), and then equals \(eR\), because \(I(eR\mid R)=R\); strictness follows from \(\partial_a I(s\mid a)=1-s/a<0\) for \(s>a\). To reach as far left as possible while covering \(1\), the second center must be the smallest \(b_R<1\) solving \(I(1\mid b_R)=R\). Any larger allowed center has its left endpoint strictly farther to the right, by the same partial derivative argument with \(s<b\).

At the sharp two-interval contact, the two boundary points coincide at \(s_*=eR\). The equations \(I(s_*\mid R)=I(s_*\mid b_R)=I(1\mid b_R)=R\) imply, writing \(\rho=b_R/R\),
\[
\rho-1=e\log\rho,\qquad (\rho-1)R-1-\log(\rho R)=0.
\]
The first equation has exactly one root \(\rho>e\) (in addition to its inadmissible coincident-center root \(\rho=1\)); the second decreases strictly from \(+\infty\) to a negative value on \((0,1/\rho)\), giving the unique \(R_*\). Direct substitution shows \(0<R_*<eR_*<\rho R_*<1\). At these centers, convexity ensures the first interval covers \([0,eR_*]\) and the second covers \([eR_*,1]\), so the interval is covered at level \(R_*\).

For any \(R<R_*\), the first right endpoint is at most \(eR<eR_*\); the second, constrained to contain \(1\), must have center at least \(b_R>b_*:=\rho R_*\), and its left endpoint lies strictly to the right of \(eR_*\). Indeed \(I(eR_*\mid b_R)>I(eR_*\mid b_*)=R_*>R\) and \(eR_*<b_R\). Thus a gap remains. At level \(R_*\), equality requires both extreme centers, establishing unique optimality up to interchange.

**4. Return to the exact finite problem.** Fix \(a=R_*\), \(b=\rho R_*\) and take \(t_1=na\), \(t_2=nb\). The uniform factorial estimate in step 2 and the fact that \(\min\{I(s\mid a),I(s\mid b)\}\le R_*\) for all \(s\in[0,1]\) imply \(\min_k\lambda_k\ge e^{-nR_*-O(\log(n+1))}\).

Conversely, assume a subsequence of optimized two-radius choices had an exponent strictly smaller than \(R_*\). Pass to a subsequence where the two scaled radii converge in the compact extended half-line \([0,\infty]\). For each fixed \(s\in[0,1]\), apply Stirling's formula to \(k_n=\lfloor ns\rfloor\) (and take \(k_n=0\) at \(s=0\)). If the lower eigenvalues are at least \(e^{-n(R_* -\delta)}\), the limiting Poisson rate forces \(\min\{I(s\mid a),I(s\mid b)\}\le R_* -\delta\). The assertion also holds for scaled radius limits \(0\) or \(\infty\) by direct Poisson-tail bounds. Since this would cover the whole interval below its sharp covering level, it is impossible. Therefore \(-n^{-1}\log B_n\to R_*\).

The same compactness argument shows that any design attaining exponent \(R_*+o(1)\) has limiting centers that cover \([0,1]\) at rate \(R_*\). The covering optimum is unique, so the unordered scaled radii converge to the announced pair.

## Verification
The companion standalone `check.py` tests the contact equations, compares independent complex-valued sampling matrices with the diagonal Gram predictions for dimensions up to 13, checks the global continuous covering-radius inequality on 15,000 deterministic random pairs, and evaluates finite-dimensional lower bounds up to degree 4,000 using logarithmic Poisson masses. It reports `TWO_RING_FOCK_CHECKS_PASS 19561`. These finite numerical tests are not a substitute for the covering and asymptotic proof above.

## Relationship to prior work
Gröchenig and Ortega-Cerdà (arXiv:2109.11825, first posted 2021-09-24; published 2022) establish general relations between Fock-polynomial Marcinkiewicz–Zygmund families and full Fock sampling, including consequences for truncated Hermite/Gabor bands; they do not compute the constrained sharp two-circular-orbit exponential loss or the unique asymptotic optimal radii in their inspected results. Their MZ normalization uses the **truncated** polynomial reproducing kernel, whereas this theorem fixes the full-Fock coherent-state weight. Their general existence theorems therefore neither imply nor contradict this sharp constrained-design result. Gröchenig and Lyubarskii (arXiv:1905.09927, 2019) analyze lattice sampling and multivariate Fock frames, a different infinite-lattice operator. Gröchenig and collaborators' 2021 work on Bergman/Hardy MZ inequalities concerns disk spaces and general sampling families, not two Fock orbits. An equivalent special information-geometric two-center solution in earlier quantization or experimental-design literature remains a priority risk.

## Limitations
The optimization is constrained to **two** rings with \(n+1\) equally spaced points on each and equal per-ring weighting. It does not optimize arbitrary planar sampling points, unequal ring weights, different numbers of points per ring, or degree-truncated-kernel normalization. The result identifies an exponential rate, not the sharp polynomial prefactor or exact finite-\(n\) optimizing radii. Although the proof is self-contained, independent validation and a fully exhaustive historical-priority search have not occurred.

## References
- K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz-Zygmund inequalities for polynomials in Fock space*, arXiv:2109.11825, posted 2021-09-24; *Mathematische Zeitschrift* 302 (2022), 1409–1428, doi:10.1007/s00209-022-03087-4.
- K. Gröchenig and Y. Lyubarskii, *Sampling of Entire Functions of Several Complex Variables on a Lattice and Multivariate Gabor Frames*, arXiv:1905.09927, posted 2019-05-23.
- K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund inequalities for polynomials in Bergman and Hardy spaces*, *Journal of Geometric Analysis*, doi:10.1007/s12220-020-00599-5.
