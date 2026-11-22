# Thirteen sites are necessary for reentrant three-point hard-core correlations on trees

## Finding
Let \(T\) be a finite tree, let \(\lambda>0\), and independently assign weight \(\lambda^{|I|}\) to each independent set \(I\subseteq V(T)\), normalized to a probability distribution. For distinct vertices \(a,b,c\), write \(X_v=\mathbf1_{\{v\in I\}}\) and define the connected three-point function
\[
C_{a,b,c}(\lambda)=\mathbb E[(X_a-\mathbb EX_a)(X_b-\mathbb EX_b)(X_c-\mathbb EX_c)].
\]
For **every tree with at most twelve vertices** and **every triple of distinct vertices**, \(C_{a,b,c}(\lambda)\) changes sign at most once as \(\lambda\) ranges from zero to infinity. The bound is sharp: the explicitly specified thirteen-vertex tree below has a triple for which the sign is successively positive, negative, positive, with exactly two positive transition activities.

Label the vertices \(0,1,\ldots,12\). The witness has edges
```
(0,1), (1,2), (1,4), (1,6), (0,8), (2,3),
(4,5), (6,7), (8,9), (8,11), (9,10), (11,12)
```
and the triple is \((a,b,c)=(0,2,9)\). Let \(\alpha\in(3,4)\) and \(\beta\in(14,15)\) be the two positive zeros of
\[
P(\lambda)=-1-11\lambda-46\lambda^2-89\lambda^3-73\lambda^4-6\lambda^5+15\lambda^6-\lambda^7.
\]
Numerically, \(\alpha\approx3.256453021665\) and \(\beta\approx14.181582823166\). Then
\[
\operatorname{sgn}C_{0,2,9}(\lambda)=
\begin{cases}
+1,&0<\lambda<\alpha,\\
0,&\lambda=\alpha,\\
-1,&\alpha<\lambda<\beta,\\
0,&\lambda=\beta,\\
+1,&\lambda>\beta.
\end{cases}
\]
These are finite-size analytic correlation reversals, not thermodynamic phase transitions.

## Assumptions and scope
All graphs are finite, simple, undirected **trees**; all vertices share exactly the same positive fugacity \(\lambda\), and nearest-neighbor simultaneous occupation is forbidden. The three measured vertices are distinct. The minimum-order statement is restricted to trees and to **two or more genuine sign reversals** of the connected, centered three-point occupancy correlation. It does not concern two-point covariance (whose sign on a hard-core tree is fixed by parity), higher cumulants, or arbitrary graphs with cycles.

## Proof
**1. Reduction to the median-site occupancy.** Every triple of distinct tree vertices has a unique median \(o\), the intersection of their three pairwise paths. Removing \(o\) separates the measured vertices lying away from \(o\) into different components. Conditional on \(X_o\), those components are independent. Along an oriented tree edge \(u\to v\), a hard-core distribution satisfies
\[
\mathbb E[X_v\mid X_u]=q_{v\mid0}(1-X_u),\qquad 0<q_{v\mid0}<1.
\]
For a measured vertex \(w\) at distance \(d(o,w)\), iterating conditional expectations gives an affine expression
\[
\mathbb E[X_w\mid X_o]=a_w+b_w X_o,
\qquad\operatorname{sgn}(b_w)=(-1)^{d(o,w)},\quad b_w\ne0.
\]
If \(w=o\), take \(a_w=0\) and \(b_w=1\). Conditional independence and centering imply
\[
C_{a,b,c}=b_a b_b b_c\,p_o(1-p_o)(1-2p_o),\qquad p_o=\mathbb P(X_o=1).
\]
This elementary tripod identity is a specialization of the established binary-tree moment factorization; the new claim concerns the sharp **minimum tree order** at which its median factor reverses sign twice.

**2. Exact root criterion.** Define the independence polynomial \(I_H(\lambda)=\sum_{J\subseteq V(H):\,J\text{ independent}}\lambda^{|J|}\) for a graph \(H\), including \(I_\varnothing=1\). At a marked vertex \(o\), let
\[
A_o(\lambda)=I_{T-o}(\lambda),\quad
B_o(\lambda)=\lambda I_{T-N[o]}(\lambda),\quad
P_o(\lambda)=B_o(\lambda)-A_o(\lambda).
\]
Then \(p_o=B_o/(A_o+B_o)\). Because all partition functions are strictly positive at positive activity,
\[
\operatorname{sgn}C_{a,b,c}(\lambda)=
-(-1)^{d(o,a)+d(o,b)+d(o,c)}\operatorname{sgn}P_o(\lambda).
\]
All edge-regression factors are nonzero at finite positive activity, so zeros of the triple correlation coincide exactly with positive zeros of \(P_o\). A median of three distinct vertices must have degree at least two.

**3. Exact finite-order exclusion.** Every unlabelled rooted tree is uniquely a multiset of smaller unlabelled rooted trees attached to its root. At every rooted tree, the exclusion recursions for root-empty and root-occupied polynomials are
\[
A=\prod_j(A_j+B_j),\qquad B=\lambda\prod_j A_j.
\]
The standalone deterministic verifier `verify.py` enumerates every rooted unlabelled tree through twelve vertices with this multiset recursion. The verified counts for orders one through twelve are
\[
1,1,2,4,9,20,48,115,286,719,1842,4766.
\]
Among them there are exactly \(4765\) rooted shapes whose root has degree at least two. For every one, coefficient sign variation (Descartes' rule) gives at most one positive root, **except** two order-eleven root polynomials with ascending coefficient vectors
```
(-1,-9,-29,-39,-17, 2,-1)
(-1,-9,-29,-38,-14, 4,-1)
```
For both exceptions a rational-coefficient Sturm sequence has **zero** positive roots. The certificate evaluates the exact sign variations and rational Euclidean remainders rather than relying on sampled activities. The multiset construction exhausts all possible marked medians, so no tree of order at most twelve can exhibit two reversals.

**4. Thirteen-vertex witness.** For the listed tree, direct independent-set counting, or the same recursion, gives the root-zero and root-one polynomial coefficient vectors
```
A_0 = (1,12,56,129,153,86,17,1)
B_0 = (0,1,10,40,80,80,32)
```
Their difference is precisely \(P\) in the finding. In descending-degree order the nonzero coefficients of \(P\) have exactly two sign variations, bounding the number of positive roots **with multiplicities** by two. Direct integer evaluation yields
\[
P(3)<0<P(4),\qquad P(14)>0>P(15).
\]
Therefore there are exactly two positive roots, one in each indicated interval, both simple. The paths \(0\!\to\!2\) and \(0\!\to\!9\) both have length two; the third measured vertex is the median itself. Hence the regression-factor product is positive, and the triple-correlation signs are the negatives of the corresponding polynomial signs. This proves the claimed positive–negative–positive sequence.

## Verification
Run `python verify.py` using Python 3.10 or later; no third-party packages or external datasets are required. The program regenerates every rooted-tree isomorphism type through order twelve, derives exact integer root-conditioned polynomials, applies coefficient sign variation, executes exact rational Sturm divisions for both exceptional cases, and independently enumerates all \(8192\) occupation masks of the thirteen-site witness. It checks the exact coefficient vectors, two positive-root count and direct three-point cumulant signs at activities \(1\), \(4\), \(15\). The expected terminal line is `TREE_CERTIFICATE_OK`.

This finite enumeration rigorously covers orders at most twelve provided the standard rooted-tree multiset bijection and the implemented rational-arithmetic operations, all included in the proof and source, are correct. It does not enumerate or classify all thirteen-vertex tree witnesses, nor does it infer an all-size upper bound on sign changes.

## Relationship to prior work
Brightwell and Winkler (2003) review hard-core independent-set measures on trees; the hard-core measure and vertex-deletion recursion are established tools. Zwiernik and Smith (2010) give product forms for binary-tree moments and cumulants; **the three-point factorization is background, not the novelty claim**. Yosef, Mizrachi and Kadrawi (2021) compute ordinary unmarked independence polynomials for trees through twenty vertices, addressing coefficient unimodality rather than the root-conditioned probability \(p_o=1/2\) or a sharp two-reversal threshold. The new content here is the **thirteen-vertex minimum**, the explicit reentrant witness and its exact two-transition certificate. Searches of indexed findings and available literature did not identify equivalent stated results; exhaustive historical originality is not established.

## Limitations
The finite minimality step is supported by a full exact enumeration and a small number of exact rational Sturm computations, rather than a short structural inequality for all small trees. The witness is not asserted unique. No assertion is made about graph cycles, heterogeneous site fugacities, asymptotic thermodynamics, or three-point cumulants of larger arbitrary trees. Independent validation has not been performed.

## References
- G. Brightwell and P. Winkler, *Hard Constraints and the Bethe Lattice: Adventures at the Interface of Combinatorics and Statistical Physics* (first posted 2003-04-28), https://arxiv.org/abs/math/0304468.
- P. Zwiernik and J. Q. Smith, *Tree cumulants and the geometry of binary tree models* (first posted 2010-04-25), https://arxiv.org/abs/1004.4360.
- R. Yosef, M. Mizrachi and O. Kadrawi, *On Unimodality of Independence Polynomials of Trees* (first posted 2021-01-17), https://arxiv.org/abs/2101.06744.
- A. Scott and A. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma*, https://arxiv.org/abs/cond-mat/0309352.
