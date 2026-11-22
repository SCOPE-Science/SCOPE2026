# Exact landscape metric speed for arbitrary moving finite barcode endpoints

## Finding

Let \(I\subseteq\mathbb R\) be an open interval, let \(M\geq 1\), and let \(b_i,d_i:I\to\mathbb R\) be differentiable at \(g_0\in I\), with \(b_i(g_0)<d_i(g_0)\), for \(1\leq i\leq M\). The intervals \([b_i(g),d_i(g))\) form a finite barcode near \(g_0\), counted with multiplicity, with labels serving only to track differentiable endpoint branches. Define its full persistence landscape \(\lambda(g)\) as the pointwise decreasing rearrangement of the \(M\) associated tent functions, with zeros in all higher layers.

**Theorem (moving-endpoint speed).** For every \(1\leq p<\infty\), the two-sided metric speed in \(\ell^p(L^p(\mathbb R))\) exists and equals

\[
\lim_{h\to 0}\frac{\|\lambda(g_0+h)-\lambda(g_0)\|_p}{|h|}
=\left[\frac12\sum_{i=1}^M(d_i(g_0)-b_i(g_0))\bigl(|b_i'(g_0)|^p+|d_i'(g_0)|^p\bigr)\right]^{1/p}.
\]

No assumption of common birth, nested tents, distinct bars, or noncrossing intervals is needed. In particular, the squared Hilbert-space metric speed for \(p=2\) is the half-lifetime-weighted sum of squared endpoint speeds, independently of all overlaps of tents.

If all endpoint functions are \(C^1\) on a compact parameter interval \([\alpha,\beta]\subset I\), with strictly positive lifetimes throughout, the landscape path is Lipschitz and its metric length is exactly

\[
\operatorname{Len}_p(\lambda|_{[\alpha,\beta]})=
\int_{\alpha}^{\beta}\left[\frac12\sum_{i=1}^M(d_i(g)-b_i(g))
\bigl(|b_i'(g)|^p+|d_i'(g)|^p\bigr)\right]^{1/p}\,dg.
\]

The formula is a metric-speed assertion. A strong Banach/Hilbert derivative of the landscape itself need not exist at a parameter where tents coincide on a positive-length range and split with different endpoint velocities.

## Assumptions and scope

For a bar \([b,d)\) with \(b<d\), define the tent
\[
\phi_{b,d}(x)=\max\{0,\min\{x-b,d-x\}\}.
\]
For fixed \(g\), the \(k\)-th landscape layer \(\lambda_k(g;x)\) is the \(k\)-th largest of \(\phi_{b_i(g),d_i(g)}(x)\) across \(i=1,\dots,M\), with \(\lambda_k=0\) for \(k>M\). The norm is
\[
\|\lambda\|_p^p=\sum_{k=1}^M\int_{\mathbb R}|\lambda_k(x)|^p\,dx.
\]
Only finite bars are included; any infinite bars are omitted from the landscape. No hypothesis on a particular homological degree or filtration-producing construction is required. The number of finite bars stays fixed locally; each bar has a differentiable tracking near the parameter under consideration. The result concerns the *full* landscape (all layers), not a truncated top-\(k\) landscape or an average of landscapes.

## Proof

Fix \(g_0\), abbreviate \(b_i=b_i(g_0)\), \(d_i=d_i(g_0)\), and \(m_i=(b_i+d_i)/2\). Except at the finite set \(\{b_i,m_i,d_i:1\le i\le M\}\), differentiability of endpoints gives the pointwise derivative of the unsorted tent:
\[
 v_i(x)=\begin{cases}
 -b_i'(g_0),&b_i<x<m_i,\\
 d_i'(g_0),&m_i<x<d_i,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Write \(u_i(h;x)=\phi_{b_i(g_0+h),d_i(g_0+h)}(x)\), so that \(u_i(h;x)=u_i(0;x)+hv_i(x)+o(|h|)\) for almost every fixed \(x\).

**Sorting lemma.** Given finitely many real numbers \(a_i\) and perturbations \(a_i(h)=a_i+hv_i+o(|h|)\), sort the perturbed entries in decreasing order, and compare with the decreasing sort of \((a_i)\). For \(h>0\), within each equal-value block the difference quotients tend to the decreasing rearrangement of the corresponding \((v_i)\); for \(h<0\) they tend to the increasing rearrangement. Blocks of distinct base values never mix for sufficiently small \(h\). Consequently, for either sign,
\[
\lim_{h\to0^\pm}\sum_{k=1}^{M}\left|\frac{\operatorname{sort}(a(h))_k-\operatorname{sort}(a)_k}{h}\right|^p=\sum_{i=1}^{M}|v_i|^p.
\]
This follows directly by grouping equal base values, expanding the finitely many perturbed coordinates, and noting that permutations leave the sum of absolute \(p\)-th powers unchanged. It does **not** assert the sorted vector has a two-sided derivative at a tie.

Apply the sorting lemma at every \(x\) outside the finitely many tent breakpoints. Endpoint differentiability implies local bounds \(|b_i(g_0+h)-b_i|+|d_i(g_0+h)-d_i|\le C|h|\). Each tent is pointwise \(C|h|\)-Lipschitz under this change, and every order statistic is \(C|h|\)-Lipschitz in the coordinatewise maximum norm. Moreover, all tents for nearby parameters are supported in a common bounded interval. The integrand of the \(p\)-th power of the landscape difference quotient is thus uniformly dominated by an integrable constant on a compact set. Dominated convergence gives
\[
\lim_{h\to0}\frac{\|\lambda(g_0+h)-\lambda(g_0)\|_p^p}{|h|^p}
=\sum_{i=1}^M\int_{\mathbb R}|v_i(x)|^p\,dx
=\frac12\sum_{i=1}^M(d_i-b_i)(|b_i'|^p+|d_i'|^p).
\]
Taking the nonnegative \(p\)-th root proves the speed formula, including all ties and collisions.

On a compact interval with \(C^1\) endpoints and positive lifetimes, the landscape is Lipschitz as an \(\ell^p(L^p)\)-valued path by the same support and difference bounds. The usual length formula for a Lipschitz curve in a metric space (integration of its almost-everywhere metric derivative) applies, and the already-proved formula computes that derivative everywhere; hence the claimed length integral.

**Boundary of strong differentiability.** At \(g_0=0\), take two bars \([g,4)\) and \([-g,6)\) for \(|g|<1\). At \(g=0\), the two tents have the same rising side throughout \(0<x<2\), but their first-layer right and left difference quotients on that interval are \(+1\) and \(-1\), respectively. Therefore the landscape is not strongly differentiable in \(\ell^2(L^2)\) at zero, although the two-sided metric speed exists and equals \(\sqrt{5}\) by the formula. This illustrates why the theorem is stated using metric speed.

## Verification

The supplied standalone `check.py` enumerates exact rational tent breakpoints and tent-tent intersections, integrates powers of differences of sorted landscapes exactly on each affine segment, and compares secant speeds against the formula. It verifies \(p=1,2,3\), 18 families (including fully overlapping, shared-birth, shared-death, coincident and crossing bars, plus deterministic pseudorandom configurations), both perturbation directions, and three step sizes, totaling 324 exact-rational comparisons. The tightest step is \(1/16384\). The checker is corroborative only: the proof above, not finite tests, establishes the general assertion.

To reproduce, run `python check.py` using Python 3 with no third-party packages. It terminates with a `PASS` summary if all assertions hold.

## Relationship to prior work

Belchí and Statuto (arXiv:2611.11358v1, first public 2026-11-08) introduce landscape velocity and establish a closed Hilbert-speed formula for barcodes whose finite bars share a fixed birth time. Their Theorem 9 and Corollary 10 cover fixed common births; their discussion explicitly excludes unequal or moving births from that formula and identifies them as future work. The present result extends metric speed to *every* fixed-cardinality differentiable family of finite barcodes and, separately, to every finite \(p\)-norm, by using the geometry of pointwise sorting rather than requiring nested tents. It also handles barcode collisions in the metric sense.

Bubenik's 2015 persistence-landscape construction supplies the order-statistics definition and Banach-space setting, not this moving-endpoint speed identity. General stability statements and algorithms for evaluating complete landscapes do not themselves state a formula for the local speed of arbitrary moving barcode endpoints. Existing theoretical implications remain a priority risk; the result is not presented as independently certified.

## Limitations

The theorem requires locally constant finite-bar count, differentiable endpoint tracks and positive lengths at the parameter. It does not address creation or disappearance of bars through zero length, infinite bars, unlabelled paths lacking differentiable local lifts, the speed of an average of landscapes, top-layer truncations, the \(p=\infty\) norm, multiparameter barcodes, or stability of endpoint derivatives under measurement noise. Strong differentiability of the landscape may fail at a tie even when its metric speed exists. The computational checker tests only finitely many exact inputs. Independent mathematical audit and exhaustive historical priority assessment have not been performed.

## References

1. Francisco Belchí and Nahuel Statuto, *Persistence landscape velocity: Closed formulas and a topological probe of quantum criticality*, arXiv:2611.11358v1 (2026-11-08), https://arxiv.org/abs/2611.11358 . In particular Theorem 9, Corollary 10, Remark 11 and the stated future direction beyond common births.
2. Peter Bubenik, *Statistical Topological Data Analysis using Persistence Landscapes*, Journal of Machine Learning Research 16(3), 77–102 (2015), https://www.jmlr.org/papers/v16/bubenik15a.html .
3. Peter Bubenik and Paweł Dłotko, *A persistence landscapes toolbox for topological statistics*, arXiv:1501.00179 (2014/2015), https://arxiv.org/abs/1501.00179 .
