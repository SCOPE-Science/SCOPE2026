# Sharp Gaussian two-sample quasi-Banach collision law and displacement of the worst evaluation point

## Finding
Fix \(0<p<1\). For the Gaussian kernel \(K(s,t)=\exp(-(s-t)^2)\) on \(\mathbb R\), let the two distinct interpolation sites be \((-h,h)\), \(h>0\). If \(G_h=(K(x_i,x_j))_{i,j=1}^2\) and \(k_h(t)=(K(-h,t),K(h,t))^{\mathsf T}\), define the *powered generalized Lebesgue constant*
\[
\Lambda_p(h)=\sup_{t\in\mathbb R}\|G_h^{-1}k_h(t)\|_p^p
=\sup_{t\in\mathbb R}(|c_-(t)|^p+|c_+(t)|^p).
\]
Then, as \(h\downarrow0\),
\[
\boxed{\displaystyle
\Lambda_p(h)=\frac{2^{1-p}}{(2e)^{p/2}h^p}
\left[1+p\left(p+\frac13\right)h^2+O_p(h^4)\right].}
\]
There is \(h_p>0\) such that for \(0<h<h_p\), the supremum is attained at precisely two points \(\pm t_p(h)\), with
\[
\boxed{\displaystyle t_p(h)=\frac1{\sqrt2}
+\sqrt2\left(\frac23-\frac p2\right)h^2+O_p(h^4).}
\]
Equivalently, the sharp coefficient-quasi-norm amplification \(\Lambda_p(h)^{1/p}\) is
\[
\frac{2^{1/p-1}}{\sqrt{2e}\,h}
\left[1+\left(p+\frac13\right)h^2+O_p(h^4)\right].
\]
By the previously established characterization of relaxed representer factors, \(\Lambda_p(h)\) is also the smallest admissible factor multiplying the powered coefficient penalty in the relaxed representer inequality for these two sites. That identification is an application of prior work, not a new representer theorem.

## Assumptions and scope
The parameter \(p\) is fixed in \((0,1)\) as \(h\downarrow0\); constants in remainder estimates may depend on \(p\). Evaluation ranges over all of \(\mathbb R\), not just the interval between sites. Coefficients are real and the kernel bandwidth is normalized by \(K(s,t)=e^{-(s-t)^2}\); rescaling coordinates translates the statement to other Gaussian widths. The two-site Gram matrix is strictly positive definite for every \(h>0\), since its off-diagonal entry is \(e^{-4h^2}<1\). The definition uses the *\(p\)-th power* of the \(\ell^p\) quasi-norm, in accordance with the generalized Lebesgue constant convention.

## Proof
**1. Exact cardinal functions.** Direct inversion of \(G_h=\left(\begin{smallmatrix}1&e^{-4h^2}\\e^{-4h^2}&1\end{smallmatrix}\right)\) gives
\[
 c_-(t)=\frac{e^{h^2-t^2}\sinh(2h(h-t))}{\sinh(4h^2)},\qquad
 c_+(t)=\frac{e^{h^2-t^2}\sinh(2h(h+t))}{\sinh(4h^2)}.
\]
These formulae yield \(c_-(-h)=c_+(h)=1\) and \(c_-(h)=c_+(-h)=0\). In particular, the objective is continuous, even, and tends to zero at infinity, so its supremum is attained.

**2. Uniform localization of global maximizers.** Put \(F_{p,h}(t)=(|c_-(t)|^p+|c_+(t)|^p)^{1/p}\). At each fixed \(t\), as \(h\downarrow0\),
\[
 hc_\pm(t)\longrightarrow\pm\tfrac12t e^{-t^2}
\quad\text{with the signs assigned respectively to }c_+,c_-.
\]
Convergence is uniform on compact sets; hence
\[
 hF_{p,h}(t)\longrightarrow 2^{1/p-1}|t|e^{-t^2}
\]
locally uniformly, including \(t=0\). It is also uniform after excluding a sufficiently large compact set: for \(0<h\le h_0\) the inequalities \(|\sinh u|\le |u|e^{|u|}\) and \(\sinh(4h^2)\ge4h^2\) imply
\[
 hF_{p,h}(t)\le C_{p,h_0} (|t|+h)
 \exp[-t^2+2h|t|+C h^2],
\]
whose tails tend to zero uniformly in \(h\). The limiting profile has exactly two strict global maxima, at \(\pm t_0\) with \(t_0=1/\sqrt2\). It follows that all global maximizers for small \(h\) lie in any prescribed pair of small disjoint neighborhoods of \(\pm t_0\).

**3. Smooth expansion near the positive maximizer.** Fix a compact neighborhood of \(t_0\) inside \((0,\infty)\). For small \(h\), this neighborhood lies in \(t>h\), so \(c_-(t)<0<c_+(t)\). Taylor expansion of the two positive hyperbolic-sine factors, with derivatives in \(t\), gives uniformly on that neighborhood
\[
 hF_{p,h}(t)=2^{1/p-1}t e^{-t^2}
 \left[1+h^2G_p(t)+O_p(h^4)\right],
\qquad
 G_p(t)=1+\frac23t^2+\frac{p-1}{2t^2}.
\]
All necessary first and second derivatives have the same uniform expansion. There are no odd powers of \(h\), by the symmetry of the two sites after exchanging their labels.

**4. Uniqueness and the point displacement.** The second derivative of \(\log(t e^{-t^2})\) at \(t=t_0\) equals \(-4\). Therefore the smooth positive branch is strictly concave in a sufficiently small fixed neighborhood of \(t_0\) for small \(h\), and its derivative has exactly one zero there. The localization in Step 2 excludes all competing global maximizers; even symmetry provides the sole negative maximizer. The implicit function expansion of the derivative yields
\[
 t_p(h)=t_0+\frac{G_p'(t_0)}4h^2+O_p(h^4),
\quad G_p'(t_0)=\sqrt2\left(\frac83-2p\right),
\]
which is the asserted displacement.

**5. Sharp value and the powered factor.** Since the leading objective is stationary at \(t_0\), moving the evaluation point by \(O_p(h^2)\) changes its value only at relative order \(O_p(h^4)\). At \(t_0\), \(G_p(t_0)=p+1/3\) and \(t_0e^{-t_0^2}=1/\sqrt{2e}\). Consequently
\[
\sup_t F_{p,h}(t)=\frac{2^{1/p-1}}{\sqrt{2e}\,h}
\left[1+\left(p+\frac13\right)h^2+O_p(h^4)\right].
\]
Raising to the positive power \(p\) gives the claimed expansion for \(\Lambda_p(h)\). Because the expression is the actual supremum, all coefficients are sharp. The link between this powered constant and the optimal relaxed representer factor is Theorem 27 of the cited foundational paper.

## Verification
The exact coefficient formula follows by multiplying by the two-by-two Gaussian Gram matrix. The global-maximizer step uses an analytic uniform-tail argument, not finite sampling. A standalone standard-Python script, `gaussian_collision_check.py`, checks Gram inversion and the predicted coefficient and location asymptotics for several quasi-Banach exponents and shrinking separations. The numerical checks support but do not replace the preceding proof. The scope of the result is the fixed-exponent, two-site collision limit.

## Relationship to prior work
Wang, Song and Zhang (arXiv:2611.08032v1, Sections 3 and 4) define the powered generalized Lebesgue constant, show that it characterizes the least relaxed representer factor, and give broader spacing and decay estimates. Their inspected two-point calculations concern Brownian/triangular and Laplacian kernels; their Gaussian discussion gives kernel admissibility and numerical learning experiments, but not the Gaussian collision expansion or the exact optimizer displacement stated here.

For comparison, the Laplacian kernel \(e^{-|s-t|}\) has bounded two-site generalized Lebesgue factor as the sites collide: its limiting interpolation coefficients between the sites are ordinary barycentric weights. The Gaussian kernel instead has a sharp \(h^{-p}\) blow-up and two off-sample extremizers staying a positive distance away from the colliding sites. Related Gaussian RBF stabilization literature treats interpolation conditioning, but no inspected result states the exact powered quasi-Banach constant together with its second-order displacement.

## Limitations
The result is asymptotic as \(h\downarrow0\); it does not classify global maximizers for all positive separations, nor generalize to three or more sites or all smooth positive-definite kernels. The remainder estimates are not asserted uniform as \(p\downarrow0\) or \(p\uparrow1\). It does not give a new abstract representer theorem or claim independent mathematical validation. Older equivalent Gaussian-cardinal-function asymptotics could exist under a different terminology and remain a bibliographic risk.

## References
1. T. Wang, G. Song, H. Zhang, *Reproducing Kernel (Quasi-)Banach Spaces with the \(\ell^p\) Coefficient Norms*, arXiv:2611.08032v1, first posted 2026-11-05. https://arxiv.org/abs/2611.08032
2. *A stable method for the evaluation of Gaussian radial basis function solutions of interpolation and collocation problems*, 2016, DOI:10.1016/j.camwa.2016.04.048 (context for Gaussian interpolation and cardinal formulae; no full-text noncoverage assessment).
3. *Sharp two-sample quasi-Banach Lebesgue constants and a symmetry-breaking transition for the Laplace kernel*, published-finding corpus research record (2026-11-17), cited only for the comparison with the distinct nonsmooth kernel. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-two-sample-quasi-banach-lebesgue-constants-and-a-symmetry--0756c0c12758
