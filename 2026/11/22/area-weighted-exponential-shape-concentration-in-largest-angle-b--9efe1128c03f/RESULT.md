# Area-weighted exponential shape concentration in largest-angle bisection

## Finding

Given any nondegenerate Euclidean triangle, repeatedly bisect the largest interior angle in *every* descendant triangle. At level \(n\), weight each descendant by its Euclidean area divided by the initial area, rather than by the equal weight \(2^{-n}\). The resulting probability measure on unordered triangle shapes converges weakly to the point mass at the right-isosceles shape \(p\). Moreover, at every fixed positive projective distance threshold the area fraction outside that threshold has an exponentially decreasing **finite-depth binomial bound** described below. This assertion concerns complete, unconstrained bisection trees; it does not assert regularization under conforming completion or adaptive pruning.

Write the ordered angles of the root triangle as \(\alpha_0\ge\beta_0\ge\gamma_0>0\) with sum \(\pi\), and put
\[
 c=\min\{\gamma_0,\alpha_0/2\},\qquad
 \eta=c/\pi,\qquad s=\frac{\sin c}{1+\sin c}>0.
\]
For each shape \(z=(x,y)\), with \(1\ge x\ge y>0\), define
\[
 D(z)=\log\frac{\max\{x,1/2\}}{\min\{y,1/2\}},\qquad
 p=(1/2,1/2),\qquad D_0=D(z_0).
\]
The maps \(L,R\) are defined explicitly under Assumptions. If \(0<\varepsilon\le D_0\), define the *positive computable decrement*
\[
 \Delta_\varepsilon=
 \min_{\substack{1\ge x\ge y\ge\eta\D(x,y)\ge\varepsilon}}
 \min\{D(z)-D(RLz),\ D(z)-D(LRz)\}>0
\]
and the positive integer
\[
 m_\varepsilon=1+\left\lfloor\frac{D_0-\varepsilon}{\Delta_\varepsilon}\right\rfloor.
\]
Let \(\nu_n\) denote the area-weighted shape distribution at level \(n\). Then for every integer \(n\ge0\), with \(N=\lfloor n/2\rfloor\),
\[
 \boxed{\nu_n\{D\ge\varepsilon\}\ \le\
 \sum_{j=0}^{\min\{m_\varepsilon-1,N\}}
 {N\choose j}s^j(1-s)^{N-j}.}
\]
For \(\varepsilon>D_0\), the left side is zero. For every fixed \(\varepsilon>0\), the right side decays exponentially as \(n\to\infty\); in particular \(\nu_n\Rightarrow\delta_p\).

## Assumptions and scope

The tree uses exact Euclidean largest-angle bisection of each triangle without conforming closure, coarsening, selective marking, or error weighting. Ties among largest angles can be broken consistently; changing the ordering convention only exchanges the two child names, and all estimates hold for either choice. Descendants are indexed by words, so coincident similarity classes retain their area multiplicities. The projective shape chart is \(x=\beta/\alpha\), \(y=\gamma/\alpha\) after descending-angle ordering. Let \(\operatorname{sort}\) arrange three positive entries in descending order and let \(\chi(a,b,c)=(b/a,c/a)\) when sorted. Then, writing \(z=(x,y)\),
\[
 Lz=\chi\bigl(\operatorname{sort}(1/2,x,y+1/2)\bigr),\quad
 Rz=\chi\bigl(\operatorname{sort}(1/2,y,x+1/2)\bigr).
\]
The compact search domain defining \(\Delta_\varepsilon\) includes all descendants because all descendant angles are at least \(c\), and hence their ordered chart satisfies \(y\ge c/\pi=\eta\). The minimum is a finite-dimensional, explicitly specified optimization over continuous elementary functions, not a claim of a closed-form numerical constant. When \(D_0=0\), all shapes equal \(p\) exactly and the positive-threshold assertions are immediate.

## Proof

**Area-weighted paths.** Select a point uniformly from the root triangle with respect to planar area, outside the zero-area union of cut boundaries. Follow its unique containing descendant at each depth. The law of its depth-\(n\) unordered shape is precisely \(\nu_n\): the event of selecting a given descendant has probability equal to its area fraction.

**Uniform positive conditional branch probability.** For any parent with ordered angles \(\alpha\ge\beta\ge\gamma\), the angle bisector partitions the opposite side into segments in the ratio of the two adjacent side lengths. By the sine law, the two child area fractions are \(\sin\beta/(\sin\beta+\sin\gamma)\) and \(\sin\gamma/(\sin\beta+\sin\gamma)\). Since all descendant angles are at least \(c\) and both \(\beta,\gamma\) are at most \(\pi/2\), their sines lie in \([\sin c,1]\). Each of the two child probabilities therefore belongs to \([s,1-s]\). This is a conditional bound, valid even though successive area-weighted selections are neither independent nor identically distributed.

**Projective decrement.** On the compact domain \(K_\eta=\{1\ge x\ge y\ge\eta\}\), the continuous function \(D\) is nonincreasing under \(L\) and \(R\). The mixed maps \(RL\) and \(LR\) satisfy \(D(RLz)<D(z)\) and \(D(LRz)<D(z)\) whenever \(z\ne p\). These are the projective Lyapunov results of Michaud, Theorem 8 and Lemmas 2 and 4 (full argument and piecewise maps in the cited paper). The compact set \(K_\eta\cap\{D\ge\varepsilon\}\) excludes \(p\), so the continuous minimum \(\Delta_\varepsilon\) is strictly positive.

**Binomial comparison.** Partition the first \(2N\) choices into consecutive disjoint pairs. Conditional on any previous pairs, the chance that the next pair consists of different child symbols is at least \(s\): after revealing its first symbol, the other child has conditional probability at least \(s\). Thus the number \(S_N\) of mixed pairs stochastically dominates a \(\operatorname{Binomial}(N,s)\) variable (couple each pair's conditional Bernoulli event to an independent uniform random variable). If the final shape has \(D\ge\varepsilon\), projective nonincrease implies that before each pair the shape has \(D\ge\varepsilon\). Each of its \(S_N\) mixed pairs decreases \(D\) by at least \(\Delta_\varepsilon\); every other step can only decrease it further. Consequently \(D_n\ge\varepsilon\) implies
\[
 S_N\le\left\lfloor\frac{D_0-\varepsilon}{\Delta_\varepsilon}\right\rfloor=m_\varepsilon-1.
\]
The stochastic domination now gives the displayed binomial tail. For fixed \(m_\varepsilon\), this tail is bounded by a polynomial in \(N\) times \((1-s)^N\), hence decreases exponentially (after any finite initial segment). Since \(D\) metrizes convergence to \(p\) on \(K_\eta\), concentration at every positive threshold implies weak convergence of \(\nu_n\) to \(\delta_p\). This proves the result.

## Verification

The critical assumptions and quantifiers were checked against the exact source: the uniform minimum-angle bound, explicit angle maps, one-step nonincrease, and strict decrease for both mixed two-step words. The new argument independently derives the conditional area-sampling lower bound, the adapted binomial domination, and the consequent quantitative tail inequality. The analytic proof holds for every nondegenerate initial triangle and every depth; finite enumeration is not used to infer an infinite statement. The included checker reproduces child areas by the sine law and checks selected finite-level identities, but it is not an independent certification of the analytic theorem.

## Relationship to prior work

Michaud, *Largest-Angle Bisection and Statistical Regularization of Triangle Shapes* (arXiv:2611.06492v1, first publicly submitted 2026-11-04), proves deterministic convergence for itineraries with infinitely many switches and uniform-count/equal-child Bernoulli convergence. Its conclusion explicitly identifies area-weighted sampling as an open extension. The earlier Ismailescu–Kim–Kim–Lee analysis provides a nondegeneracy bound but not a probabilistic shape distribution. A previously published sharp mixed-child contraction result gives an improved equal-count concentration rate, but counting descendant nodes equally cannot determine the physical-area weighting, since area fractions vary with shape and path. The present claim is **only** the area-weighted stochastic comparison and its finite-depth tail, not any new claim about the already-known projective contraction.

## Limitations

The bound depends on the initial triangle and on a compact optimization quantity \(\Delta_\varepsilon\); neither the exponential rate nor the constant is claimed sharp. An arbitrary adaptive refinement scheme, conforming closure, or error-based weights can change conditional child probabilities and is outside scope. The result assumes known source theorems about the deterministic LAB projective dynamics; no independent audit of those prior theorems is asserted. No exhaustive historical-priority guarantee is claimed.

## References

1. J. Michaud, *Largest-Angle Bisection and Statistical Regularization of Triangle Shapes*, arXiv:2611.06492v1 (2026-11-04), https://arxiv.org/abs/2611.06492.
2. D. Ismailescu, J. Kim, K. Kim, J. Lee, *The largest angle bisection procedure*, arXiv:1908.02749 (2019), https://arxiv.org/abs/1908.02749.
3. *Sharp mixed-child contraction and exponential shape concentration for largest-angle bisection*, published-finding corpus research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-mixed-child-contraction-and-exponential-shape-concentratio--30fda51bbc9b.
