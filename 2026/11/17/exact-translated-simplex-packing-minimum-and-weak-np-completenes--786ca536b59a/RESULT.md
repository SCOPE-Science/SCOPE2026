# Exact translated-simplex packing minimum and weak NP-completeness under moving the origin

## Finding
For \(n\ge2\), let \(e_1,\ldots,e_n\) be the standard basis of \(\mathbb R^n\). Given \(b>0\) and \(a_i>0\) with \(A=\sum_{i=1}^n a_i<b\), define the origin-containing simplex
\[K(a,b)=b\operatorname{conv}\{0,e_1,\ldots,e_n\}-a.\]
Its origin-dependent first packing minimum of Han--Henk--Xue [1] for the integer lattice is
\[
\boxed{\rho_1(K(a,b),\mathbb Z^n)=\frac{1}{\displaystyle b/2+\min_{\varnothing\ne S\subseteq[n]}\left|a(S)-b/2\right|}},
\qquad a(S)=\sum_{i\in S}a_i.
\]
The optimal primitive projection directions are precisely \(\pm\mathbf1_S\) for nonempty minimizing subsets \(S\), with opposite signs representing one unoriented direction.

For positive integer data \(a_i,b\) in binary, with \(A<b\) and even \(b\), the decision problem
\[\rho_1(K(a,b),\mathbb Z^n)=2/b\ ?\]
is weakly NP-complete as \(n\) varies. Nevertheless, the displayed formula can be evaluated in pseudo-polynomial time by subset-sum dynamic programming. Therefore a uniform family of translates and homothetic copies of one right-simplex shape already encodes number partitioning into its first packing minimum.

There is also a sharp non-centroid phenomenon. On the equal-coordinate translation ray \(a_i=a\in(0,b/n)\), the largest possible first packing minimum is \(2/b\), achieved at exactly the distinct values
\[a=\frac{b}{2k},\qquad \lfloor n/2\rfloor<k\le n.\]
Their number is \(\lceil n/2\rceil\). The centroid corresponds to \(a=b/(n+1)\), and attains the maximum exactly when \(n\) is odd.

## Assumptions and scope
The first packing minimum here uses the nonsymmetric, origin-dependent definition in [1]:
\[\rho_1(K,\mathbb Z^n)=\inf\{r>0:(rK+L)\cap\mathbb Z^n\ne L\cap\mathbb Z^n\text{ for every real hyperplane }L\text{ through }0\}.\]
The requirement \(0\in\operatorname{int}K\) holds because the barycentric coordinates of the origin with respect to \(-a,be_1-a,\ldots,be_n-a\) are \(1-A/b\) and \(a_i/b\), all strictly positive. Dimension is part of the binary-encoded integer complexity input; NP-completeness is not claimed for fixed dimension. Neither the original difference-body packing minima [2], which ignore translation, nor higher packing minima are the object of this theorem.

## Proof
**1. Reduction to primitive lattice normals.** Proposition 2.1 and the one-dimensional projection calculation in [1, Section 2, pp. 4--6] give
\[\rho_1(K,\mathbb Z^n)=\max_{z\in\mathbb Z^n\setminus\{0\},\ z\text{ primitive}}\frac1{\max\{h_K(z),h_K(-z)\}},\]
where \(h_K(z)=\max_{x\in K}\langle x,z\rangle\). Indeed the projected one-dimensional lattice along the primitive integer normal \(z\) has spacing \(1/\|z\|_2\), and the projected interval of \(K\) has signed endpoints \(-h_K(-z)/\|z\|_2\), \(h_K(z)/\|z\|_2\). The first nonzero projected lattice point enters at the reciprocal of the larger unnormalized endpoint. Every extremizing projection can therefore be represented by a primitive lattice normal.

**2. Sharp range-one rigidity.** For such a normal \(z=(z_i)\), write
\[M=\max(0,z_1,\ldots,z_n),\quad m=\min(0,z_1,\ldots,z_n),\quad t=\sum_{i=1}^n a_i z_i.\]
Direct evaluation on the simplex vertices gives
\[h_K(z)=bM-t,\qquad h_K(-z)=t-bm,\]
so the denominator is
\[D(z)=\frac b2(M-m)+\left|\frac b2(M+m)-t\right|.\]
Because \(0,z_1,\ldots,z_n\) are integers and \(z\ne0\), \(M-m\) is a positive integer. If \(M-m\ge2\), then \(D(z)\ge b\). For each nonempty subset \(S\subseteq[n]\), however, \(z=\mathbf1_S\) is primitive and yields
\[D(\mathbf1_S)=\max\{a(S),b-a(S)\}<b\]
because \(0<a(S)\le A<b\). Thus every minimizer must satisfy \(M-m=1\). As \(m\le0\le M\) and all values are integers, this forces \((m,M)=(0,1)\) or \((-1,0)\), hence \(z=\pm\mathbf1_S\) for a nonempty subset \(S\). It follows that
\[\min_{\text{primitive }z\ne0}D(z)=\min_{S\ne\varnothing}\max\{a(S),b-a(S)\}=b/2+\min_{S\ne\varnothing}|a(S)-b/2|.\]
This also proves the complete classification of minimizing directions, including ties and all strict boundary assumptions.

**3. Complexity and pseudo-polynomial evaluation.** The universal bound \(D(z)\ge b/2\) implies \(\rho_1\le2/b\), and equality holds exactly when some nonempty subset sums to \(b/2\). For integer inputs with even \(b\), a subset \(S\) supplies a polynomial-length NP certificate; its sum is checked by binary integer addition.

For NP-hardness, reduce the standard positive-integer PARTITION problem [3]. Given weights \(w_1,\ldots,w_m>0\), put \(W=\sum_i w_i\), introduce \(m+1\) translation coordinates
\[a_i=2w_i\ (1\le i\le m),\qquad a_{m+1}=2W+1=:q,\qquad b=2(W+q)=6W+2.\]
Then \(A=\sum a_i=4W+1<b\) and \(b/2=W+q=3W+1\). A subset summing to \(b/2\) must include the final coordinate \(q\), since the first \(m\) coordinates total only \(2W<b/2\); the remaining condition is \(\sum_{i\in S\cap[m]}2w_i=W\), exactly PARTITION. This is a polynomial-time many-one reduction, proving NP-completeness. The subset sums can be enumerated by the usual Boolean-reachability dynamic program in \(O(nb)\) arithmetic steps (with polynomial bit costs); hence the hardness is weak.

**4. Equal-coordinate axis.** When all \(a_i=a\), subset sums equal \(ka\) with \(1\le k\le n\). The upper bound \(2/b\) is met precisely when \(ka=b/2\), i.e. \(a=b/(2k)\). The strict interior condition \(a<b/n\) is equivalent to \(k>n/2\). Thus the positions are exactly those listed above. The centroid of \(b\operatorname{conv}\{0,e_1,\ldots,e_n\}\) has every coordinate \(b/(n+1)\); it equals one of the maximizing translations precisely if \(2k=n+1\), or equivalently \(n\) is odd.

## Verification
The proof above handles every dimension, every permitted real translation, and all primitive normals without truncation. A standalone Python 3 checker, `check.py`, uses exact rational arithmetic: for 300 seeded integer cases in dimensions two through five it compares the subset formula and all optimum directions against all primitive integer normals in the coordinate box \([-2,2]^n\); five small PARTITION instances check the many-one encoding. It reports 305 passing cases. These finite checks are regressions, not an exhaustive verification of all integer directions; range-one rigidity supplies the infinite argument.

Reproduce with `python3 check.py` (Python standard library only). The equality case, support-function normalizations, strict interior assumptions, and complexity reduction are proved algebraically above.

## Relationship to prior work
Han, Henk, and Xue [1], first publicly submitted on 2026-01-20, introduce the origin-dependent nonsymmetric packing minima and their projected-lattice characterization. Their Theorem 1.3 calculates *all* packing minima for the single centroid-centered uniformly scaled simplex, while the present result calculates the *first* minimum across the entire origin-position parameter space, its lattice-normal degeneracies, and its variable-dimensional complexity. The one-dimensional projection principle in [1] is used with attribution and is not presented as new. The integer-normal range-one rigidity, discrepancy formula, exact optimal-direction classification, and NP-completeness reduction require additional arguments beyond that principle.

The original packing minima of Henk, Schymura, and Xue [2] use a difference-body construction and are translation-invariant; these cannot distinguish the origin positions or imply the displayed translation-sensitive formula. The input PARTITION hardness [3] is classical and is used only as a reduction source.

## Limitations
The hardness is weak and assumes dimension varies, strictly positive binary-encoded integer translation coordinates and even integer \(b\). It does not imply strong NP-hardness, hardness for a fixed dimension, or hardness of higher packing minima. The geometry formula covers the right-simplex family with standard lattice and strictly interior origin, not every lattice or all simplex shapes. Historical novelty remains open to independent literature review, including possible unindexed equivalent formulations.

## References
[1] M. Han, M. Henk, F. Xue, *Packing minima of convex bodies*, arXiv:2601.13937v1, first posted 2026-01-20. https://arxiv.org/abs/2601.13937

[2] M. Henk, M. Schymura, F. Xue, *Packing minima and lattice points in convex bodies*, arXiv:2005.02234v1, first posted 2020-05-05. https://arxiv.org/abs/2005.02234

[3] M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness*, W. H. Freeman, 1979 (classical PARTITION problem).
