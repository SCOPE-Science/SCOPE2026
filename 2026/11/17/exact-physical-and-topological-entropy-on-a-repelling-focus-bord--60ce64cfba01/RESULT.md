# Exact physical and topological entropy on a repelling-focus border-collision graph

## Finding
Consider the continuous planar piecewise-affine map
\[
F(x,y)=\begin{cases}(x+y+1,0),&x\le0,\\(y+1,-2x),&x\ge0.\end{cases}
\]
Its unique right-half-plane fixed point \(X=(1/3,-2/3)\) is repelling. Every other planar orbit enters, after finitely many iterates, the compact invariant metric graph
\[
K=([-2,1]\times\{0\})\cup(\{1\}\times[-2,0])\cup([-1,1]\times\{-2\})\cup(\{-1\}\times[-2,0]).
\]
There is a unique invariant probability \(\mu\) whose basin has full two-dimensional Lebesgue measure. With respect to \(\mu\), successive visits to the section \(E=[0,1]\times\{0\}\) are independent renewal blocks of lengths \(6,5,5\), selected with probabilities \(1/4,1/4,1/2\). In the **original planar iteration clock**, the metric entropy and topological entropy of the compact invariant graph are respectively
\[
\boxed{h_\mu(F)=\frac{2\log2}{7}},\qquad
\boxed{h_{\mathrm{top}}(F|_K)=\log\lambda},
\]
where \(\lambda\in(1,2)\) is the unique positive solution greater than one of \(\lambda^6-2\lambda-1=0\). These entropies are strictly different: numerically they are \(0.19804205159\ldots\) and \(0.20685980710\ldots\). The unique maximal-entropy invariant probability has independent section-symbol probabilities \((\lambda^{-6},\lambda^{-5},\lambda^{-5})\), which differ from the physical probabilities.

## Assumptions and scope
The map acts on all of \(\mathbb R^2\), and the two formulas agree on the switching line. The metric entropy concerns the invariant probability on the one-dimensional graph, which is singular relative to planar area. The topological entropy is only asserted for the compact invariant set \(K\), not for the noncompact plane. A physical probability has a basin of full planar Lebesgue measure if time averages of every continuous observable on \(K\), after eventual entry, converge to its integral for almost every planar starting point. All stochastic-looking independence claims are distributional under the invariant measure, not a claim that deterministic trajectories contain external random inputs. Endpoint orbits can have exceptional finite return times; assertions about symbols are modulo their measure-zero preimages.

## Proof
**1. The repelling focus and global finite entry.** On the right, the affine map \(F_R(x,y)=(y+1,-2x)\) has the displayed fixed point and satisfies exactly
\[
F_R^2(z)-X=-2(z-X)
\]
for every planar point \(z\). If a point had an infinite strictly right-half-plane itinerary, its even and odd first-coordinate subsequences would both remain positive. The alternating expansion factor \(-2\) forces both first coordinates to equal \(1/3\); the point must be \(X\). Consequently every other orbit reaches the left half-plane. Its next iterate lies on the horizontal axis. On that axis, negative coordinates increase by one until they lie in \([-2,0]\). A coordinate larger than one returns to the left half-plane after two right steps, because its second-iterate first coordinate is \(1-2u<0\), and the following left step sends it to \(-2u\); finitely many unit translations then reach \([-2,0]\). Coordinates in \([0,1]\) already lie in \(K\). Thus every orbit except \(X\) enters \(K\) in finite time.

A direct piecewise-affine image calculation shows that the four edges of \(K\) map, respectively, into the horizontal axis, right vertical edge, bottom horizontal edge, or left vertical edge, hence \(F(K)\subset K\). More specifically, \(K=\bigcup_{j=0}^{5}F^j(E)\), so every graph point has a representation in a finite tower over \(E\).

**2. Three full branches and their original-time lengths.** For interior \(u\in(0,1)\), direct composition until the next hit of \(E\) yields, away from \(u=1/4,1/2\),
\[
(T(u),R(u))=\begin{cases}
(4u,6),&0<u<1/4,\\
(4u-1,5),&1/4<u<1/2,\\
(2-2u,5),&1/2<u<1.
\end{cases}
\]
The time \(R\) counts **iterations of the original planar map**, not iterations of \(T\). Each of the three affine branches maps its domain onto \((0,1)\). Their inverse contractions are
\[
\phi_1(v)=v/4,\qquad\phi_2(v)=(v+1)/4,\qquad\phi_3(v)=1-v/2.
\]
Thus normalized Lebesgue measure \(m\) on \(E\) is invariant and exact under \(T\): branch symbols are independently sampled with probabilities given by their interval lengths \(p=(1/4,1/4,1/2)\). Exactness follows directly from the full-branch inverse coding, whose cylinder diameters decrease exponentially (by at least \(2^{-n}\)). In particular this is the unique absolutely continuous invariant probability for the section map.

**3. The physical probability and entropy.** The mean original-time return length is
\[
\bar R=\tfrac14\cdot6+\tfrac14\cdot5+\tfrac12\cdot5=\tfrac{21}{4}.
\]
The normalized return tower defines
\[
\mu=\frac1{\bar R}\sum_{j=0}^{5}(F^j)_*\bigl(m|_{\{u:R(u)>j\}}\bigr).
\]
Its invariance and ergodicity follow by summing consecutive tower levels and using \(T_*m=m\). Since all nonfixed planar points enter \(K\) and subsequently meet \(E\), and because finite affine branch preimages of section-null sets are planar-null, Birkhoff-generic section points lift to a full-planar-measure basin. Any other invariant probability with such a full-measure basin must equal \(\mu\), by uniqueness of almost-everywhere time averages.

The Bernoulli entropy per section return is
\[
H(p)=-\sum_{i=1}^{3}p_i\log p_i=\tfrac32\log2.
\]
Abramov's return-entropy identity gives \(h_\mu(F)=H(p)/\bar R=(2/7)\log2\). This division by \(\bar R\) is essential: section-time entropy \(\tfrac32\log2\) is not the physical-time entropy of the planar map.

**4. The full graph entropy and strict gap.** The three inverse contractions give a full three-symbol return coding, with original-time roof lengths \((6,5,5)\). On the finite tower, admissible weighted words have exponential growth \(\lambda^n\) at original time \(n\), where the renewal characteristic equation is
\[
\lambda^{-6}+2\lambda^{-5}=1.
\]
One can derive this from the finite Markov graph consisting of one base state and three deterministic excursions of lengths \(6,5,5\). Its Perron root is the unique \(\lambda>1\) satisfying \(\lambda^6-2\lambda-1=0\). The natural factor from the compact coded tower onto \(K\) is finite-to-one except at the countable collection of iterated branch endpoints. Every point of \(K\) has at most finitely many presentations by a tower level and the finitely many affine preimages on that level. The endpoint itineraries have zero entropy. Thus the compact finite-to-one Markov coding preserves topological entropy, yielding \(h_{\mathrm{top}}(F|_K)=\log\lambda\).

Equivalently, for any stationary section-symbol law with probabilities \(q_i\) and positive roof mean, the entropy per physical time is bounded by
\[
\frac{H(q)}{\sum_iq_iR_i}\le\log\lambda,
\]
by the relative-entropy inequality against the probability vector \(q_i^*=\lambda^{-R_i}\). Equality holds only for independent symbols with \(q=q^*\); this yields the unique maximal-entropy law on the graph. Since \(p_2\ne p_3\) whereas \(q_2^*=q_3^*\), strict inequality follows for the physical law.

## Verification
The accompanying standalone `verify.py` (Python 3 standard library) was actually run. It passed 1,198 exact rational branch/graph test cases, confirmed the right-branch square identity, three section slopes and lengths, roof mean \(21/4\), and the numerical Perron root and strict entropy inequality. The checker additionally computes a renewal-count variance as a supplementary diagnostic; this variance is not part of the finding. Finitely many tests do not prove the global statements; the algebraic and symbolic arguments above supply the proof.

## Relationship to prior work
Simpson [1, §§1–5] proves the general one-dimensional first-return configuration in the repelling-focus regime, including the available return-time ordering, but does not determine an exact physical probability, its planar basin, and both entropies in the original clock at this integer resonance. The earlier zero-determinant analysis [2] concerns broader parameter-space dynamics; its return-map framework is credited, not claimed as new. Simpson's boundary-Hopf normal form [3] contains the trace choices leading to other exact renewal calculations, but those have a *zero right determinant*, whereas the present model has the strictly expanding right focus with determinant two. The general Markov-coding and return entropy theorems used here are standard; the evaluated complete planar capture/physical-versus-maximal entropy comparison is the parameter-specific contribution.

## Limitations
The displayed entropies are exact only for the stated trace/determinant/forcing parameters, not for an open robustness neighborhood. Other invariant probabilities, including the mass at the repelling focus, exist; unique **physical** probability does not mean unique invariant probability. The compact graph has one-dimensional support; this is not a claim of a two-dimensional absolutely continuous invariant probability. The statements do not classify nonlinear perturbations or all parameter values. Related work on finite-state Markov graph maps might provide equivalent specializations not located in the inspected records. Independent scientific validation has not been performed.

## References
[1] D. J. W. Simpson, *One-Dimensional First Return Maps for the Two-Dimensional Border-Collision Normal Form with a Zero Determinant*, arXiv:2606.08901v1 (first public 2026-06-08), later *Qualitative Theory of Dynamical Systems* **25**, article 160 (2026), https://doi.org/10.1007/s12346-026-01576-z.

[2] D. J. W. Simpson, *The Two-Dimensional Border-Collision Normal Form with a Zero Determinant*, arXiv:2408.04790 (first public 2024-08-08), https://arxiv.org/abs/2408.04790.

[3] D. J. W. Simpson, *Boundary Hopf Bifurcations in Three-Dimensional Filippov Systems*, arXiv:2604.06570 (first public 2026-04-08), https://arxiv.org/abs/2604.06570.

[4] P. Glendinning, *Invariant Measures for the n-Dimensional Border Collision Normal Form*, *International Journal of Bifurcation and Chaos* (2014), https://eprints.maths.manchester.ac.uk/2252/.
