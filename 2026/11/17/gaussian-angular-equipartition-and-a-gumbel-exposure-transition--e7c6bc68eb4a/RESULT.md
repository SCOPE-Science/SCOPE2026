# Gaussian angular equipartition and a Gumbel exposure transition in cube–crosspolytope hulls

## Finding
For every integer \(n\ge2\), let \(B_1^n=\{x\in\mathbb R^n:\sum_i|x_i|\le1\}\), and for \(1<t<n\) set
\[
K_n(t)=\operatorname{conv}\bigl([-1,1]^n\cup tB_1^n\bigr).
\]
This full-dimensional unconditional Euclidean polytope has precisely \(2^n+2n\) vertices, partitioned into the \(2^n\) cube corners and the \(2n\) coordinate apices. Let \(p_n(t)\) be the fraction of Haar-uniform supporting directions whose unique exposed vertex is an apex. If \(X_1,\ldots,X_n\) are independent absolute standard normal variables, with \(S_n=\sum_iX_i\), \(M_n=\max_i X_i\), and density \(f(x)=\sqrt{2/\pi}\exp(-x^2/2)\) on \(x>0\), then
\[
p_n(t)=\Pr\{tM_n>S_n\}
=n\int_0^\infty f(x)\int_{[0,x]^{n-1}}\mathbf1\!\left\{\sum_{j=1}^{n-1}y_j<(t-1)x\right\}\prod_{j=1}^{n-1}f(y_j)\,dy\,dx.
\]
The exact spherical normal-cone angle is \(p_n(t)/(2n)\) at each coordinate apex and \((1-p_n(t))/2^n\) at each cube vertex. Therefore the probability that two independent Haar directions expose the same vertex is
\[
C_n(t)=\frac{p_n(t)^2}{2n}+\frac{(1-p_n(t))^2}{2^n}.
\]
There is exactly one parameter \(t_n^*\in(1,n)\) for which **all** \(2^n+2n\) vertices have equal spherical normal-cone measure, characterized by
\[
p_n(t_n^*)=\frac{2n}{2^n+2n}.
\]
It is the unique minimizer of \(C_n(t)\), with \(C_n(t_n^*)=1/(2^n+2n)\). In dimension two, \(p_2(t)=4\arctan(t-1)/\pi\), so \(t_2^*=\sqrt2\): the regular octagon is the angularly balanced member.

Define \(\mu=\sqrt{2/\pi}\) and let \(b_n>0\) solve \(n\Pr\{|Z|>b_n\}=1\) for a standard normal \(Z\). For any fixed real \(s\), put
\[
t_n(s)=\frac{\mu n}{b_n}\left(1+\frac{s}{b_n^2}\right).
\]
For all sufficiently large \(n\) this belongs to \((1,n)\), and the sharp Gaussian-exposure crossover obeys
\[
\lim_{n\to\infty}p_n(t_n(s))=1-\exp(-e^s),\qquad
\lim_{n\to\infty}nC_n(t_n(s))=\frac12\bigl(1-\exp(-e^s)\bigr)^2.
\]
Thus in the transition window the exponentially many cube vertices retain an asymptotically positive *combined* angular probability, but the collision probability is of order \(1/n\) and is controlled by the only \(2n\) apices.

## Assumptions and scope
The Euclidean metric and the canonical coordinate realization are fixed; no affine change of coordinates is implicit. Vertices are exposed by a random standard Gaussian direction, equivalently a Haar-uniform direction on the unit sphere. Normal-cone angles are normalized by the total spherical area; degenerate ties have spherical measure zero. Statements at finite \(n\) require \(n\ge2\) and \(1<t<n\). The large-dimensional statement holds for every fixed real \(s\) along integers \(n\to\infty\).

## Proof
**Vertices and the support function.** The support functions of the cube and crosspolytope are \(\sum_i|g_i|\) and \(t\max_i|g_i|\), respectively. Hence
\[
h_{K_n(t)}(g)=\max\left\{\sum_i|g_i|,\ t\max_i|g_i|\right\}.
\]
Every cube corner \(\varepsilon\in\{-1,1\}^n\) is exposed by \(g=\varepsilon\), because \(n>t\). Every apex \(\pm te_i\) is exposed by \(g=\pm e_i\), because \(t>1\). Since a vertex of the hull of two finite vertex sets must lie in their union, these are all the vertices.

**Angles, integral and collisions.** Rotational invariance reduces random directions to independent Gaussian coordinates. A cube corner wins exactly when \(S_n>tM_n\), and an apex wins exactly when \(tM_n>S_n\). The positive variables \(X_i=|G_i|\) have continuous density \(f\), and both events have positive probability for \(1<t<n\). Signed-coordinate permutations act transitively on each of the two vertex orbits, giving the two claimed individual cone measures. The event \(M_n=X_i\) selects a unique index almost surely; conditioning on its value \(x\) proves the displayed integral. Summing squares of all vertex-cone probabilities yields \(C_n\).

**Unique angular equipartition.** The random ratio \(R_n=S_n/M_n\) lies strictly between \(1\) and \(n\) almost surely and has positive probability in every nonempty open subinterval of \((1,n)\): positive coordinate vectors near \((a,1,\ldots,1)\) realize every ratio \(1+(n-1)/a\) for \(a>1\). Its law has no atoms, since fixing all but one coordinate makes the equation \(S_n=tM_n\) a finite union of one-dimensional level sets, each of zero Lebesgue measure for \(1<t<n\). Consequently \(p_n(t)=\Pr(R_n<t)\) is continuous and strictly increasing from zero to one. The strictly convex quadratic \(p^2/(2n)+(1-p)^2/2^n\) has its unique minimum at \(p=2n/(2^n+2n)\), when both vertex-cone measures equal \(1/(2^n+2n)\). For \(n=2\), write \(X_1=r\cos\theta\), \(X_2=r\sin\theta\). The angle \(\theta\) is uniform on \((0,\pi/2)\), so the apex region is \(\min(X_1,X_2)<(t-1)\max(X_1,X_2)\) and has probability \(4\arctan(t-1)/\pi\). This gives \(t_2^*=\sqrt2\).

**Sharp critical window.** Standard Gaussian tail integration by parts yields \(\Pr\{|Z|>u\}=\sqrt{2/\pi}e^{-u^2/2}u^{-1}(1+O(u^{-2}))\) as \(u\to\infty\). Thus \(b_n\sim\sqrt{2\log n}\) and, for each fixed real \(x\),
\[
 n\Pr\{|Z|>b_n+x/b_n\}\longrightarrow e^{-x}.
\]
By independence, \(b_n(M_n-b_n)\) converges in distribution to the standard Gumbel random variable \(G\) with \(\Pr(G\le x)=\exp(-e^{-x})\). The half-normal law has finite variance and mean \(\mu\), so \(S_n=\mu n+O_{\Pr}(\sqrt n)\). Because \(b_n^2/\sqrt n\to0\),
\[
 b_n^2\left(\frac{t_n(s)M_n}{\mu n}-\frac{S_n}{\mu n}\right)
 =s+b_n(M_n-b_n)+o_{\Pr}(1)
 \ \Longrightarrow\ s+G.
\]
The limiting law has no atom at zero, hence the probabilities of positivity converge to \(\Pr(G>-s)=1-\exp(-e^s)\). Substitute this into the exact collision formula; \(n/2^n\to0\) yields the second limit. This completes the proof.

## Verification
The accompanying standalone standard-library Python checker regenerates the complete finite vertex list and independently compares direct vertex maximization with the derived support formula for \(3,000\) Gaussian test instances in dimensions two through five. It also compares the exact two-dimensional angle formula against \(480,000\) deterministic-seed Gaussian samples at three parameters and checks the exact equipartition at \(t=\sqrt2\). Successful execution prints `CUBE_CROSS_GAUSSIAN_ANGLE_DIAGNOSTICS_PASS`. These computations test finite cases; the full-dimensional theorem and the limiting laws are established by the analytic proof above.

## Relationship to prior work
Kohl, Olsen and Sanyal study unconditional polytopes and their combinatorial, reflexive, and antichain-theoretic structures (first public preprint 2019-06-03). Böröczky, Fodor and Hug investigate Gaussian-integral mean-width comparisons and stability for symmetric convex bodies, especially cubes and crosspolytopes (first public preprint 2024-10-15). Their geometric and probabilistic frameworks motivate the present question, but their inspected published treatments do not provide the two-orbit angle law or Gumbel transition for this scaled convex hull. The polar relation \(K_n(t)^\circ=B_1^n\cap t^{-1}[-1,1]^n\) connects the family to clipped crosspolytopes; duality by itself does not turn volume, isotropy, or facet counts of an intersection into the Gaussian vertex-exposure law here. Standard Gaussian maxima and the law of large numbers are used as known probabilistic inputs rather than claimed new results.

## Limitations
Priority remains provisional: other terminology for cube–crosspolytope hulls or their polars may conceal earlier equivalent angular formulas. The critical-window result is a pointwise limit for fixed \(s\), not a uniform error bound. The angular equipartition parameter is characterized exactly by a probability equation, not by an elementary closed formula in all dimensions. The uniqueness claim concerns the parameter interval \((1,n)\), not arbitrary affine realizations.

## References
- F. Kohl, M. Olsen, R. Sanyal, *Unconditional reflexive polytopes*, arXiv:1906.01469 (initial public posting 2019-06-03), https://arxiv.org/abs/1906.01469 ; open-access journal text https://link.springer.com/article/10.1007/s00454-020-00199-8 .
- K. J. Böröczky, F. Fodor, D. Hug, *Strengthened inequalities for the mean width and the \(\ell\)-norm of origin symmetric convex bodies*, arXiv:2410.11460 (initial public posting 2024-10-15), https://arxiv.org/abs/2410.11460 ; open-access journal text https://link.springer.com/article/10.1007/s00208-025-03228-0 .
