# Universal logarithmic shape and marked-volume laws for tiny Poisson cuboids

## Finding

For every fixed integer \(d\ge2\), consider independent, stationary, one-dimensional Poisson processes of positive intensities \(\lambda_1,\ldots,\lambda_d\), and through every point of process \(i\) draw the hyperplane perpendicular to coordinate axis \(i\). The resulting stationary tessellation consists of cuboids. Distinguish the stationary **typical cell**, selected by cell intensity, from the **zero cell**, which contains a fixed origin.

For either selection convention, let \(W_i\) be the cuboid's side length in direction \(i\), let \(V=\prod_iW_i\), and put \(a=\varepsilon\prod_i\lambda_i\), \(L=\log(1/a)\). We consider \(0<a<1\) and \(\varepsilon\downarrow0\). Set \(k=1\) for the typical cell and \(k=2\) for the zero cell.

**Sharp two-term rare-volume law.** For either type of cell,

\[
\Pr\{V<\varepsilon\}
=\frac{a^k}{k\,(d-1)!}\left[L^{d-1}+(d-1)\left(\frac1k-d\gamma\right)L^{d-2}+o(L^{d-2})\right],
\]

where \(\gamma\) is the Euler--Mascheroni constant. In particular, the typical-cell rare-volume probability has exponent one, while the origin-containing cell has exponent two, with the same dimension-dependent logarithmic power.

**Complete conditional logarithmic shape law.** Write \(T_i=-\log(\lambda_iW_i)\), and \(Z=\log(\varepsilon/V)\). Conditional on \(V<\varepsilon\),

\[
\left(T_1/L,\ldots,T_{d-1}/L,Z\right)
\xrightarrow[\varepsilon\downarrow0]{\mathrm{TV}}
\left(U_1,\ldots,U_{d-1},E_k\right),
\]

where \((U_1,\ldots,U_d)\) is uniform on the standard \((d-1)\)-simplex, equivalently \(\operatorname{Dirichlet}(1,\ldots,1)\), and \(E_k\sim\operatorname{Exponential}(k)\) is independent. Consequently \(V/\varepsilon\) converges in total variation to \(\operatorname{Beta}(k,1)\), independently of the first \(d-1\) logarithmic proportions. The **full** exponent vector \((T_1/L,\ldots,T_d/L)\) converges **weakly**, not in total variation, to the Dirichlet vector.

For the zero cell, if \(R_i\) denotes the proportion of its width in direction \(i\) lying on the negative side of the origin, \(R_1,\ldots,R_d\) are, even before conditioning, independent \(\operatorname{Uniform}(0,1)\) variables independent of all side lengths. Thus the above total-variation convergence holds jointly with this independent origin-location mark.

The conclusions remain valid for nonorthogonal parallelepiped tessellations obtained by a fixed nonsingular linear transformation: replace the dimensionless threshold \(a\) by \(\varepsilon\prod_i\lambda_i/|\det B|\), with the columns of \(B\) the physical edge vectors corresponding to unit coordinate increments.

## Assumptions and scope

The dimension \(d\ge2\) is fixed; all intensities are finite and strictly positive; hyperplane processes are independent and stationary. Each sample is obtained using its stated cell-selection convention, not by treating the typical and zero cells as interchangeable. The logarithmic normalization is meaningful only once \(a<1\). All limits are for \(a\downarrow0\) with fixed rates and dimension. The distribution statements refer to volume measured in the physical Euclidean coordinate system. A nonorthogonal affine image has the deterministic volume multiplier \(|\det B|\).

The claim is **not** about isotropic Poisson line tessellations with continuously distributed directions, Poisson--Voronoi cells, or growing dimension. Here \(\gamma\) denotes the Euler--Mascheroni constant, not the hyperplane intensity.

## Proof

**1. Exact cell-length laws.** The consecutive gaps of a rate-\(\lambda_i\) stationary Poisson process have an exponential law \(\operatorname{Exp}(\lambda_i)\). Under stationary typical-cell selection, the \(d\) side lengths are independent exponential gaps. At a deterministic origin, the distances to the nearest process points on its negative and positive sides are independent \(\operatorname{Exp}(\lambda_i)\). The zero-cell width is their sum, hence \(\operatorname{Gamma}(2,\lambda_i)\). Independence across axes holds by construction. Thus

\[
X_i:=\lambda_iW_i\quad (1\le i\le d)
\]

are independent \(\operatorname{Gamma}(k,1)\), with \(k=1\) or \(2\), and \(V=(\prod_iX_i)/(\prod_i\lambda_i)\). In the zero-cell case, the density of independent left/right exponential gaps \((A_i,B_i)\) transforms under \((A_i,B_i)=(W_iR_i,W_i(1-R_i))\) to \(\lambda_i^2 W_i e^{-\lambda_iW_i}\), independent of \(R_i\in(0,1)\). This proves the exact independent uniform marks.

**2. Logarithmic gamma-product density.** Define \(T_i=-\log X_i\) and \(S=\sum_iT_i=-\log(\prod_iX_i)\). Their density is

\[
f_T(t)=\frac{e^{-kt}}{\Gamma(k)}e^{-e^{-t}},\quad t\in\mathbb R.
\]

Let \(h(t)=e^{-e^{-t}}\) and \(H(t)={\bf1}_{(0,\infty)}(t)\). Writing \(q=h-H\), the function \(q\) has finite absolute moments of every order; it decays exponentially as \(t\to\infty\) and superexponentially as \(t\to-\infty\). Its integral satisfies

\[
\int_{\mathbb R}q(t)\,dt
=\int_0^1\frac{e^{-x}-1}{x}\,dx+\int_1^\infty\frac{e^{-x}}x\,dx=-\gamma.
\]

Denote convolution by \(*\). For \(s>0\), \(H^{*d}(s)=s^{d-1}/(d-1)!\). Expanding \((H+q)^{*d}\) and applying the finite-moment bounds for \(q\) gives

\[
h^{*d}(s)=\frac{s^{d-1}}{(d-1)!}-\frac{d\gamma\,s^{d-2}}{(d-2)!}+o(s^{d-2}),\qquad s\to\infty.
\]

For rigor, the term with one \(q\) equals \(\int q(t)(s-t)_+^{d-2}/(d-2)!\,dt\), whose first coefficient is its total mass. Terms with two or more copies of \(q\) are \(O(1+s^{d-3})\) for \(d\ge3\), by convolution with integrable, finite-moment kernels and the lower polynomial powers of \(H\); for \(d=2\), the two-copy term \((q*q)(s)=o(1)\). The exponentially small tails of \(q\) justify truncating the integrals and interchanging these asymptotics.

Because the density of \(S\) equals \(e^{-ks}h^{*d}(s)/\Gamma(k)^d\), integrating from \(L\) to infinity yields

\[
\Pr\{S>L\}
=\frac{e^{-kL}}{k\Gamma(k)^d}
\left[\frac{L^{d-1}}{(d-1)!}+
\frac{(1/k-d\gamma)L^{d-2}}{(d-2)!}+o(L^{d-2})\right].
\]

Since \(\Gamma(1)=\Gamma(2)=1\), \(S>L\) is precisely the event \(V<\varepsilon\) and the claimed sharp expansion follows. This calculation uses a genuine asymptotic expansion of an absolutely integrable convolution, not a numerical estimate.

**3. Marked conditional limit in total variation.** Put \(z=S-L>0\) and, for \(i<d\), \(u_i=T_i/L\), so \(T_d=L(1-\sum_{i<d}u_i)+z\). The linear coordinate change has Jacobian \(L^{d-1}\). Conditional on \(S>L\), the joint density of \((u_1,\ldots,u_{d-1},z)\), relative to Lebesgue measure on \(\mathbb R^{d-1}\times(0,\infty)\), is

\[
p_L(u,z)=\frac{L^{d-1}e^{-k(L+z)}}{\Gamma(k)^d\Pr(S>L)}
\prod_{i=1}^d e^{-e^{-T_i}}.
\]

For a.e. \(u\) in the open simplex \(\{u_i>0,\sum_{i<d}u_i<1\}\) and each \(z>0\), all \(T_i\to+\infty\), so the product tends to one. For a.e. \(u\) outside the closed simplex at least one \(T_i\to-\infty\) and the product tends to zero. Substituting the leading asymptotic of \(\Pr(S>L)\) gives pointwise a.e.

\[
p_L(u,z)\longrightarrow k(d-1)! e^{-kz}\,\mathbf1_{\{u_i>0,\sum_{i<d}u_i<1,\ z>0\}}.
\]

The right-hand side integrates to one. Since every \(p_L\) is itself a probability density, Scheffé's lemma yields \(L^1\), hence total-variation convergence, with the simplex component independent of \(z\). Under the bijection \(v=e^{-z}\), \(v\in(0,1)\), the limit has density \(kv^{k-1}\), giving the Beta law. The omitted final exponent satisfies \(T_d/L=1-\sum_{i<d}u_i+z/L\), implying only *weak* convergence of the full exponent vector: its finite-\(L\) support lies in \(\sum_iT_i/L>1\), whereas the limiting Dirichlet law lies exactly on \(\sum_iU_i=1\); total variation for the full vector would be false.

**4. Geometric implications.** Every component \(U_i\) is strictly positive a.s. and their pairwise values are distinct a.s. Consequently every physical side length tends to zero in conditional probability, yet their relative lengths are exponentially separated: for any distinct \(i,j\), \(\log(W_i/W_j)/L\Rightarrow U_j-U_i\), a nondegenerate distribution. An equal-shape limit is therefore impossible under volume conditioning; the normalized logarithmic proportions provide its complete nondegenerate replacement. Fixed nonsingular linear changes preserve volume up to a constant Jacobian and carry the same edge-coordinate proof.

## Verification

The accompanying `checks/check.py` uses independent high-precision Bessel-function identities in dimension two to verify the sharp constant and second term for both selection conventions. It also verifies the exponential and Gamma width moments by direct Poisson-gap simulation and tests numerical convergence of the conditional logarithmic-shape law in dimension three. Execute it with `python checks/check.py` after installing `checks/requirements.txt`. The exact first two checks are diagnostics and not substitutes for the arguments above.

## Relationship to prior work

Beermann, Redenbach and Thäle (arXiv:1211.5488; first submitted November 23, 2012), *Asymptotic shape of small cells*, Proposition 4, identify independent exponential lengths for the **typical** Poisson cuboid, while Theorem 2 determines qualitative collapse for planar area-small typical cells. Section 2.3 explicitly treats dimensions at least three as an unresolved extension for their small-volume shape statements. The present theorem gives a quantitative all-dimensional logarithmic simplex limit, a complete marked volume law, and a distinct origin-containing zero-cell law. It uses their known exponential typical-length fact, not as a claimed discovery. The elementary Poisson-gap construction is separately given here.

Bonnet (arXiv:1702.01964; first submitted February 7, 2017), *Small cells in a Poisson hyperplane tessellation*, treats broad conditional small-cell shape and facet limits. His shape-limit results with a nondegenerate geometric size condition do not supply the logarithmic mark for product-volume conditioning in the finitely atomic orthogonal model; the paper explicitly identifies the parallelepiped case as a special configuration. The current results do not imply his general results. Product distributions from Mellin-transform theory make the scalar lower-tail exponent accessible, but neither the cited cell papers nor the matched searches supplied the conditional joint logarithmic proportions, independent Beta volume undershoot, zero-cell origin marks, and two-term coefficient as this single geometric statement. The existence of a broader implicit product-limit theorem remains a priority risk; no uniqueness or independent verification is asserted.

## Limitations

The dimension is fixed (no uniformity as \(d\to\infty\)); the cell generators have precisely \(d\) independent direction families; positive intensities are fixed. The full \(d\)-vector logarithmic-shape convergence is **weak only**, while total variation holds for the \((d-1)\)-coordinate chart jointly with the volume mark. The two-term expansion has an unquantified lower-order remainder. No statement is made for arbitrary Poisson hyperplane directional measures, isotropic line tessellations, or other size functionals. Mathematical novelty remains provisional pending broader historical-priority assessment; no independent audit has been performed.

## References

1. M. Beermann, C. Redenbach, C. Thäle, *Asymptotic shape of small cells*, arXiv:1211.5488, submitted 2012-11-23; Proposition 4, Theorem 2, Section 2.3. https://arxiv.org/abs/1211.5488
2. G. Bonnet, *Small cells in a Poisson hyperplane tessellation*, arXiv:1702.01964, submitted 2017-02-07; introduction, Section 3 and its size-functional hypotheses. https://arxiv.org/abs/1702.01964
3. R. Schneider and W. Weil, *Stochastic and Integral Geometry*, Springer, 2008, Chapter 10.4 (standard stationary Poisson-cell conventions and tessellation background).
4. NIST Digital Library of Mathematical Functions, sections on the modified Bessel functions and Gamma function, https://dlmf.nist.gov/10 and https://dlmf.nist.gov/5 (independent scalar diagnostics).
