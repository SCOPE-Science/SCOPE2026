# All-contact Löwner ellipsoids of unequal two-level chain polytopes

## Finding
For integers \(p,q\ge1\), let \(n=p+q\) and let the standard Euclidean chain polytope of two ordered antichains be
\[
P_{p,q}=\operatorname{conv}\bigl(([0,1]^p\times\{0\})\cup(\{0\}\times[0,1]^q)\bigr).
\]
Equivalently it is the stable-set polytope of \(K_{p,q}\). Define
\[
 a=\frac{p+1}{2(n+1)},\qquad b=\frac{q+1}{2(n+1)},\qquad
 w=\frac{4(n+1)}{n(p+1)(q+1)},
\]
and the positive-definite matrix
\[
H=w\begin{pmatrix}(q+1)I_p&J_{p,q}\\J_{q,p}&(p+1)I_q\end{pmatrix},
\qquad c=(a\mathbf1_p,b\mathbf1_q).
\]
The **unique minimum-volume enclosing ellipsoid** of \(P_{p,q}\) is
\[
\boxed{\mathcal L_{p,q}=\{z:(z-c)^{\mathsf T}H(z-c)\le1\}.}
\]
Every one of the \(2^p+2^q-1\) distinct vertices is on its boundary. In particular its volume is
\[
\boxed{\operatorname{vol}_n(\mathcal L_{p,q})=
 \frac{\pi^{n/2}}{\Gamma(1+n/2)}
 \frac{w^{-n/2}}{\sqrt{(q+1)^{p-1}(p+1)^{q-1}(n+1)}}.}
\]
The evaluated **unequal** cases \(p\ne q\) are the contribution here. The equal case was previously established by an explicit hypergeometric contact certificate and is included only to state a uniform formula.

## Assumptions and scope
The ambient inner product is the ordinary coordinate Euclidean inner product on \(\mathbb R^n\). The integers \(p,q\) are positive; the genuinely asymmetric families have \(p\ne q\). All ellipsoids are full-dimensional. We use a precision matrix convention: the inverse precision \(H^{-1}\) is the ellipsoid shape matrix, whose eigenvalues give squared semiaxes. This is the **outer** Löwner ellipsoid, not the maximal inscribed John ellipsoid. The same formula transfers to the order polytope via the Euclidean reflection of the second coordinate block.

## Proof
**1. Vertex classification and positivity.** The independent sets of \(K_{p,q}\) consist of subsets supported in one part only. Thus the distinct vertices are the origin and the nonzero Boolean vectors in one block. The block-contrast eigenspaces of the matrix \(H/w\) have respective positive eigenvalues \(q+1\) and \(p+1\), while its block-constant restriction has matrix
\[
\begin{pmatrix}q+1&\sqrt{pq}\\\sqrt{pq}&p+1\end{pmatrix},
\]
whose determinant is \((p+1)(q+1)-pq=n+1>0\). Hence \(H\) is positive definite; its determinant is
\[
\det H=w^n(q+1)^{p-1}(p+1)^{q-1}(n+1).
\]

**2. Exact boundary equation for every vertex.** At the origin, direct substitution yields
\[
c^{\mathsf T}(H/w)c=\frac{n(p+1)(q+1)}{4(n+1)}=w^{-1}.
\]
For a Boolean vertex with \(k\) ones in the first block, expansion of its quadratic form gives a constant plus \(k\) times
\[
w\bigl[(q+1)(1-2a)-2qb\bigr]=0.
\]
The analogous second-block coefficient is \(w[(p+1)(1-2b)-2pa]=0\). Therefore *every* vertex has squared ellipsoid gauge exactly one. Convexity gives \(P_{p,q}\subseteq\mathcal L_{p,q}\), with all vertices as genuine contacts.

**3. An explicit probability distribution with positive mass at every contact vertex.** For every integer \(m\ge1\), first define an exchangeable subset law on \([m]\) by choosing a size \(K\), then choosing uniformly among all subsets of that size. If \(m\) is odd, assign probabilities \(1/(m+1)\) and \(m/(m+1)\) to sizes \(0\) and \((m+1)/2\). If \(m=2r\) is even, assign probabilities \(1/(m+2)\), \(1/2\), and \(r/[2(r+1)]\) to sizes \(0,r,r+1\). In either case the probabilities sum to one and direct calculation shows
\[
\mathbb E K=m/2,\qquad \mathbb E[K(K-1)]=m(m-1)/4.
\]
Consequently each coordinate is present with probability \(1/2\), and each pair of distinct coordinates is simultaneously present with probability \(1/4\). Define \(Z_m\) by mixing this size-based law, with weight \(3/4\), and the uniform law on all \(2^m\) subsets, with weight \(1/4\). This preserves the inclusion moments and makes the probability of every subset strictly positive. On the polytope vertices put the measure
\[
\nu=\frac{p+1}{n+1}\mathcal L(Z_p,0)
 +\frac{q+1}{n+1}\mathcal L(0,Z_q)
 -\frac1{n+1}\delta_0.
\]
Here \(\mathcal L(\cdot)\) means probability law, **not** the ellipsoid. The total mass is one. The only potentially negative atom is zero, with mass
\[
\frac{(p+1)\Pr(Z_p=0)+(q+1)\Pr(Z_q=0)-1}{n+1}>0,
\]
because each term \((m+1)\Pr(Z_m=0)\) is at least \(3(m+1)/[4(m+2)]\) when \(m\) is even (hence \(m\ge2\), and this bound is at least \(9/16\)), and at least \(3/4\) when \(m\) is odd. Thus \(\nu\) is a bona fide probability measure with full support on the contact vertices.

**4. Exact isotropic contact certificate.** The preceding inclusion probabilities imply \(\mathbb E_{\nu}X=c\). Write \(\Sigma=\operatorname{Cov}_{\nu}(X)\). Its diagonal entries in the first block are \(a-a^2\), its within-first-block off-diagonal entries are \(a/2-a^2\), and similarly \(b-b^2\) and \(b/2-b^2\) in the second block. Cross-block entries equal \(-ab\). Direct multiplication using the displayed formulas for \(a,b,w\) gives the exact identity
\[
\boxed{H\Sigma=\frac1n I_n.}
\]
For any other enclosing ellipsoid with center \(d\) and positive-definite shape \(S\), averaging its defining inequality over the contact distribution gives
\[
\operatorname{tr}(S^{-1}\Sigma)+(c-d)^{\mathsf T}S^{-1}(c-d)\le1.
\]
The arithmetic–geometric mean inequality for eigenvalues and \(\Sigma=H^{-1}/n\) imply
\[
\left(\frac{\det H^{-1}}{\det S}\right)^{1/n}
 \le \frac1n\operatorname{tr}(S^{-1}H^{-1})\le1.
\]
Thus \(\det S\ge\det H^{-1}\), and equality forces \(d=c\), \(S=H^{-1}\). The candidate is globally volume-minimizing and unique without any symmetry assumption on a competitor.

**5. Volume and isometric reflection.** The determinant in step 1 and the Euclidean unit-ball volume give the formula. The affine reflection \((x,y)\mapsto(x,\mathbf1_q-y)\) is orthogonal up to translation and maps this chain polytope to the corresponding order polytope, transferring optimality and contact structure exactly.

## Verification
The accompanying `verify.py` uses the Python standard library only. For all 361 ordered pairs \(1\le p,q\le19\) it checks the origin gauge, the moments and origin mass for the size-based laws before mixing, and the full matrix identity \(H\Sigma=I/n\). For \(p+q\le12\) it additionally checks all Boolean vertex gauges. Its completion line begins `UNBALANCED_TWO_BLOCK_LOEWNER_EXACT_PASS`. The full-support modification preserves the tested moments, and its positivity follows from the bounds in Step 3. These finite tests corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work
Stanley's order/chain-polytopes and the analysis by Ahmad, Fourier and Joswig establish the underlying maximal two-rank poset. The previously published result *A hypergeometric all-vertex Löwner certificate for two-layer chain polytopes* treats only the balanced case \(p=q\), explicitly stating that unequal ranks are outside its scope. Its exact outer ellipsoid specializes from the present expression when \(p=q\); no novelty is claimed for this specialization. The separately published *Exact John ellipsoid of unbalanced two-layer chain and order polytopes* evaluates the **inner** ellipsoid and its facet contacts, not the outer ellipsoid or its vertex contacts. Neither theorem logically gives the unequal outer shape by parameter substitution or polarity of the original body. The new feature is an explicitly evaluated anisotropic unequal-part Löwner shape and a positive design with only pairwise-independent Boolean subset moments, including every contact vertex. Search cannot conclusively exclude an unindexed general theorem under convex hulls of orthogonal boxes or optimal experimental design.

## Limitations
The assertion concerns precisely two complete antichain levels, not arbitrary bipartite graphs, higher-rank posets, or independently rescaled coordinates. The origin subtractions in the contact design require both blocks and should not be reinterpreted as a signed certificate: the *resulting* measure is positive. The finite checker does not prove the all-dimensional theorem. Historical priority remains provisional until broader mathematical verification; independent review has not been performed.

## References
1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, DOI: 10.1007/BF02187680.
2. I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, first posted 2023-09-04, https://arxiv.org/abs/2309.01626.
3. R. Freij-Hollanti, T. Lundström, *f-vector inequalities for order and chain polytopes*, arXiv:2312.13890, first posted 2023-12-21, https://arxiv.org/abs/2312.13890.
4. *A hypergeometric all-vertex Löwner certificate for two-layer chain polytopes*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-a-hypergeometric-all-vertex-l-wner-certificate-for-two-layer-cha--f8245d9b11e4.
5. *Exact John ellipsoid of unbalanced two-layer chain and order polytopes*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-john-ellipsoid-of-unbalanced-two-layer-chain-and-order-pol--c200d8f4f023.
6. A. Mittal, G. A. Hanasusanto, *Finding minimum volume circumscribing ellipsoids using generalized copositive programming*, arXiv:1807.07507, first posted 2018-07-19, https://arxiv.org/abs/1807.07507.
