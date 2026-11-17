# Sharp Lipschitz Poisson norms on finite trees and their extremizers

## Finding

For every finite simple unweighted tree \(T=(V,E)\) with \(n=|V|\ge 2\), write \(L=D-A\) for the combinatorial Laplacian and \(L^+\) for its Moore--Penrose inverse. Give real vertex functions modulo constants the edge Lipschitz seminorm
\[
\operatorname{Lip}_T(f)=\max_{xy\in E}|f(x)-f(y)|.
\]
For each edge \(e=uv\), deletion of \(e\) leaves two components \(A_e,B_e\). Let
\[
W_e=\sum_{x\in A_e}\sum_{y\in B_e}d_T(x,y).
\]
Then the sharp inverse-Poisson Lipschitz operator norm satisfies
\[
\boxed{K(T):=\|L^+\|_{\operatorname{Lip}\to\operatorname{Lip}}
=\frac1n\max_{e\in E}W_e.}
\]
Every maximizing function is, modulo constants and nonzero scalar multiplication, a signed edge ramp for an edge maximizing \(W_e\): for an oriented maximizing edge \(e=uv\), with \(u\in A_e\), \(v\in B_e\), the ramp is
\[
F_e(x)=\begin{cases}d_T(x,u)+1,&x\in A_e,\\-d_T(x,v),&x\in B_e.\end{cases}
\]
The sharp fixed-order inequalities are
\[
\boxed{\frac{2n-3}{n}\ \le K(T)\le\ \frac12\left\lfloor\frac{n^2}{4}\right\rfloor.}
\]
For \(n\ge4\), lower equality holds precisely for stars \(K_{1,n-1}\), and upper equality precisely for paths \(P_n\). For \(n=2,3\), the unique unlabelled tree is both a star and a path. All norming edges and the exact value are obtainable in \(O(n)\) arithmetic operations on the tree's adjacency lists.

## Assumptions and scope

The graph is finite, connected, loopless, unweighted and acyclic, with \(n\ge2\). The input and output fields are real, and the norm is the edge-difference supremum, equivalently the Lipschitz seminorm for unit-edge shortest-path distance. The Laplacian inverse means the unique mean-zero solution \(g=L^+f\) of \(Lg=f-\bar f\mathbf1\), where \(\bar f=n^{-1}\sum_{x\in V}f(x)\); adding a constant to the input or output makes no difference to the norm. The stated equality classification is for nonconstant inputs, with maximizers considered up to a nonzero real scalar and an additive constant.

## Proof

**1. Edge flux identity.** Fix \(e=uv\), and orient the cut so \(u\in A_e\), \(v\in B_e\). Since \(Lg=f-\bar f\mathbf1\), summing \(Lg\) on \(A_e\) cancels every internal edge, leaving exactly \(g(u)-g(v)\). Therefore
\[
g(u)-g(v)=\sum_{x\in A_e}(f(x)-\bar f)
=\frac1n\sum_{x\in A_e}\sum_{y\in B_e}(f(x)-f(y)).\tag{1}
\]
The factor \(1/n\) follows by expanding \(\bar f\) and using \(|A_e|+|B_e|=n\).

**2. Sharp norm and witnesses.** On a tree, \(|f(x)-f(y)|\le\operatorname{Lip}_T(f)d_T(x,y)\) along the unique path. Hence (1) implies
\[
|g(u)-g(v)|\le \operatorname{Lip}_T(f)W_e/n.
\]
For the ramp \(F_e\) in the Finding, every edge difference has absolute value exactly one. For every \(x\in A_e\), \(y\in B_e\), the unique path goes through \(u-v\), so
\[
F_e(x)-F_e(y)=d_T(x,u)+1+d_T(v,y)=d_T(x,y).
\]
Thus \(\operatorname{Lip}_T(F_e)=1\) and (1) is an equality for this edge. Taking the maximum across edges proves the exact formula.

**3. Complete equality classification.** If a nonconstant input attains \(K(T)\), one output edge \(e\) attains the output Lipschitz maximum. Equality must hold in every summand of the triangle inequality and in every cross-cut Lipschitz bound in (1). Since all pair distances across the cut are strictly positive, all differences \(f(x)-f(y)\), \(x\in A_e\), \(y\in B_e\), have a common sign and absolute value \(\operatorname{Lip}_T(f)d_T(x,y)\). Taking first \(y=v\) and then \(x=u\) determines \(f\) exactly as a signed, scaled and translated copy of \(F_e\). Necessarily \(W_e/n=K(T)\). Conversely each such ramp is norming by Step 2, establishing all equality functions.

**4. Unique path maximum.** Write \(a=|A_e|\), \(b=|B_e|\), with \(a+b=n\). As every cross-cut geodesic passes through \(u-v\),
\[
W_e=ab+b\sum_{x\in A_e}d_T(x,u)+a\sum_{y\in B_e}d_T(y,v).\tag{2}
\]
For any rooted tree on \(a\) vertices, the sum of root distances is at most \(a(a-1)/2\): order vertices so each parent precedes its child, and the \(i\)-th discovered vertex has depth at most \(i-1\). Equality forces a single rooted path with the root at an endpoint (the level-by-level depth sequence must be \(0,1,\ldots,a-1\)). Therefore
\[
W_e\le ab+\frac{ba(a-1)}2+\frac{ab(b-1)}2=\frac{nab}{2},
\]
so \(K(T)\le\frac12\lfloor n^2/4\rfloor\). Equality forces \(a,b\) to be the two balanced integers and both shores to be end-rooted paths, making the whole tree a path. Conversely the middle edge of \(P_n\) realizes equality.

**5. Unique star minimum.** Let \(v\) be a leaf, with neighbor \(u\), and take its incident edge. Its cross-cut sum is
\[
W_{uv}=\sum_{x\ne v}d_T(v,x)
=n-1+\sum_{x\notin\{u,v\}}d_T(u,x)\ge2n-3.
\]
Equality here requires \(u\) adjacent to every other vertex. Hence every tree satisfies \(K(T)\ge(2n-3)/n\), and a nonstar tree has strictly greater value for every leaf edge (therefore strictly greater \(K(T)\)). In a star, leaf-edge cross-cut sums are all \(2n-3\), so the bound is sharp exactly there.

**6. Linear-time exact evaluation.** Root \(T\) at any vertex \(o\). For a nonroot vertex \(c\) with parent \(p\), let \(s_c\) be its subtree size and \(q_c=\sum_{x\in\mathrm{subtree}(c)}d_T(c,x)\). Let \(R_p=\sum_{x\in V}d_T(p,x)\). Formula (2) gives
\[
W_{pc}=s_c(n-s_c)+(n-s_c)q_c+s_c(R_p-q_c-s_c).\tag{3}
\]
Compute the \(s_c\) and \(q_c\) bottom-up, starting from \(s_v=1\), \(q_v=0\), and for each child \(c\) of \(v\) adding \(s_c\) to \(s_v\) and \(q_c+s_c\) to \(q_v\). Initialize \(R_o=\sum_{x}d_T(o,x)\), and reroot along parent-child edges via \(R_c=R_p+n-2s_c\). Each edge and vertex participates in a constant number of arithmetic operations. Evaluate (3) for every edge; its maximum divided by \(n\) is \(K(T)\), and its maximizers are precisely the norming edges.

## Verification

The accompanying self-contained `check_tree_poisson.py` (Python standard library, no external dependencies) independently inverts the rational matrix \(L+\mathbf1\mathbf1^{\mathsf T}/n\), removes the constant projection to obtain \(L^+\), and constructs the induced operator on edge-increment coordinates. A second implementation obtains the cross-cut values by breadth-first graph distances. The checker compares the independent calculations on every labelled tree through six vertices, plus selected larger trees, verifies sharp endpoints, and checks exact cube-vertex witnesses. Running `python check_tree_poisson.py` produced:

```
EXACT_PSEUDOINVERSE_VS_CROSS_CUT_DISTANCE_PASSED 1441
ADDITIONAL_EXACT_RANDOM_TREES_PASSED 120
SHARP_STAR_AND_PATH_ENDPOINTS_PASSED 14
ALL_TREE_POISSON_CHECKS_PASSED
```

These are finite diagnostic computations, not a replacement for the proof for arbitrary trees. The exact general theorem and the complete maximizer classification follow from Steps 1--5. The algorithmic claim follows from Step 6.

## Relationship to prior work

Graph distance and tree Wiener-index extremal questions are classical: Dankelmann and Entringer (2000) address average graph distance and spanning trees. The combinatorial Laplacian, distance matrices and their relations are treated by Bapat, Kirkland and Neumann (2005), including an exact tree distance-matrix inverse. Chung and Yau (2000) develop discrete Green-function representations. Székely and Wang (2013) study tree distance and subtree-ratio extremal problems. These are acknowledged as structural ingredients and context, not claimed as new.

The present norm depends on the **largest cross-cut distance sum** rather than the all-pairs Wiener sum. It is the \(\operatorname{Lip}\to\operatorname{Lip}\) norm of the inverse graph Laplacian, not the Euclidean norm, a Green-function entry, or the inverse of a distance matrix. It additionally gives the exact norm on each tree, all norming inputs, linear-time computation, and sharp fixed-order star/path classifications. A historically implicit equivalent reformulation of tree pseudoinverse or distance-matrix identities is a remaining priority risk; database searches alone do not establish publication novelty.

## Limitations

Only real functions on finite unweighted trees with counting measure and the unnormalized combinatorial Laplacian are treated. Positive edge weights, other normalizations, cycles, and \(L^p\)-type operator norms are not covered. A full historical literature survey is not claimed; some related older graph-inequality papers were inspected through their abstracts rather than complete text. Independent mathematical evaluation has not been performed.

## References

1. P. Dankelmann and R. Entringer, *Average distance, minimum degree, and spanning trees*, Journal of Graph Theory 33 (2000), 1--13, doi:10.1002/(SICI)1097-0118(200001)33:1<1::AID-JGT1>3.0.CO;2-L (first published online 14 December 1999).
2. F. R. K. Chung and S.-T. Yau, *Discrete Green's functions*, Journal of Combinatorial Theory, Series A 91 (2000), 191--214, doi:10.1006/jcta.2000.3094.
3. R. Bapat, S. J. Kirkland and M. Neumann, *On distance matrices and Laplacians*, Linear Algebra and Its Applications 401 (2005), 193--209, doi:10.1016/j.laa.2004.05.011 (available online 20 July 2004).
4. L. A. Székely and H. Wang, *Extremal values of ratios: distance problems vs. subtree problems in trees*, Electronic Journal of Combinatorics 20 (2013), P67, doi:10.37236/3020.
