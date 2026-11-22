# Sharp morphism complexity for three-object categorical models of projective-plane wedges

## Finding

For every integer \(r\ge 2\), write \(X_r=\bigvee_{i=1}^{r}\mathbb{RP}^{2}\), and let \(\mu_3(X_r)\) be the minimum number of **nonidentity morphisms** among finite acyclic categories with exactly three objects and classifying space homotopy equivalent to \(X_r\). Then

\[
\boxed{\mu_3(X_r)=(r+1)^2+2=r^2+2r+3.}
\]

Every minimizer has hom-set sizes \((r+1,r+1,r^2+1)\), in one of the two possible orders of the adjacent hom-sets, and explicit tables realize these sizes. The formula also holds at \(r=1\), where the six-morphism model is known from the degree-two Moore-space construction. In particular the minimum for \(r=2,3,4,5\) is \(11,18,27,38\), respectively. This is a statement about categories with **exactly three objects**, not a global minimum across arbitrary object counts.

## Assumptions and scope

A finite acyclic category has no nonidentity endomorphisms and no directed cycles between distinct objects. Its classifying space is the geometric realization of its nerve. A nondegenerate nerve \(k\)-simplex is a string of \(k\) composable nonidentity morphisms. A category realizing \(X_r\) with three objects necessarily has a chain of objects \(0<1<2\): if there were no composable pair, its nerve would be a graph with torsion-free integral first homology.

Write \(a=|\operatorname{Hom}(0,1)|\), \(b=|\operatorname{Hom}(1,2)|\), and \(c=|\operatorname{Hom}(0,2)|\), all positive integers. The category has \(a+b+c\) nonidentity morphisms and exactly \(ab\) nondegenerate two-simplices. Since \(X_r\) is connected with \(H_1(X_r;\mathbb Z)\cong(\mathbb Z/2)^r\) and \(\chi(X_r)=1\), these properties constrain its nerve.

## Proof

**Lower bound.** The Euler characteristic of the three-object nerve is

\[
1=\chi(X_r)=3-(a+b+c)+ab,
\qquad a+b+c=ab+2.
\]

The three-object sink decomposition writes the classifying space as the mapping cone of a graph map \(p:\Gamma\to B\mathcal K_a\), where \(\mathcal K_a\) is the two-object category with \(a\) parallel arrows, so \(B\mathcal K_a\simeq\bigvee^{a-1}S^1\). Here the vertices of the graph \(\Gamma\) are the \(b\) middle-to-last arrows together with the \(c\) first-to-last arrows, and its \(ab\) edges are composable pairs. The mapping-cone long exact sequence gives a surjection from finite \(H_1(X_r;\mathbb Z)\) onto the free abelian group \(\widetilde H_0(\Gamma;\mathbb Z)\), hence \(\Gamma\) is connected. It follows that \(H_1(X_r;\mathbb Z)\) is a quotient of \(H_1(B\mathcal K_a;\mathbb Z)\cong\mathbb Z^{a-1}\). Because \((\mathbb Z/2)^r\) needs at least \(r\) generators, \(a\ge r+1\). Applying exactly the same argument to the opposite category, whose classifying space is homeomorphic to the original, gives \(b\ge r+1\). Therefore

\[
a+b+c=ab+2\ge(r+1)^2+2.
\]

Equality forces \(a=b=r+1\) and \(c=r^2+1\).

**Construction attaining the bound.** Choose arrows \(f_0,\ldots,f_r:0\to1\) and \(g_0,\ldots,g_r:1\to2\), and let the arrows \(0\to2\) be \(h_0,h_1,\ldots,h_r\) together with \(\ell_{i,j}\) for every pair \(1\le i,j\le r\) with \(i\ne j\). Specify all nonidentity compositions by

\[
 g_j\circ f_i=\begin{cases}
 h_0,&(i,j)=(0,0)\text{ or }i=j\ge1,\\
 h_j,&i=0,\ j\ge1,\\
 h_i,&j=0,\ i\ge1,\\
 \ell_{i,j},&i,j\ge1,\ i\ne j.
 \end{cases}
\]

There is no nonidentity composable triple, so the prescription is automatically associative. The arrow counts are \(a=b=r+1\) and \(c=1+r+r(r-1)=r^2+1\). Its sink graph \(\Gamma\) has \(r\) four-edge cycles sharing the single edge \((h_0,g_0)\), plus \(r(r-1)\) pendant edges: the \(i\)-th cycle runs

\[
 g_0\xrightarrow{f_0^{-1}}h_0\xrightarrow{f_i}g_i
 \xrightarrow{f_0^{-1}}h_i\xrightarrow{f_i}g_0,
\]

where orientations in this display encode traversals of the labelled undirected graph, not inverse morphisms in the category. The pendant edges are the pairs labelled \(f_i\) from \(\ell_{i,j}\) to \(g_j\) with \(i\ne j\) and \(i,j\ge1\). After contracting the shared edge and the pendant trees, \(\Gamma\simeq\bigvee^r S^1\). Under \(p\), the cycle indexed by \(i\) has word \(f_0^{-1}f_if_0^{-1}f_i\); taking \(f_0\) as the tree edge in \(B\mathcal K_{r+1}\), this becomes the degree-\(+2\) loop in the \(i\)-th free generator. Therefore the mapping cone is homotopy equivalent to the wedge of \(r\) degree-two mapping cones,

\[
B\mathcal C_r\simeq\bigvee_{i=1}^r\bigl(S^1\cup_{2} e^2\bigr)
\simeq\bigvee_{i=1}^r\mathbb{RP}^2=X_r.
\]

This achieves the lower bound for every \(r\ge2\).

## Verification

The accompanying standalone Python program constructs the complete nondegenerate cellular boundary operators of this category for \(1\le r\le5\), verifies \(\partial_1\partial_2=0\), checks graph incidence and exact hom-set sizes, and obtains the integral Smith invariant factors of \(\partial_2\). It finds \(r\) factors equal to two, no top-dimensional kernel, and the predicted arrow counts \(6,11,18,27,38\). Those tests are finite checks only; the graph/mapping-cone argument and lower bound above prove the theorem for every integer \(r\ge2\).

Reproduce with Python 3 and SymPy by running `python verify_minimal_morphisms.py`.

## Relationship to prior work

Carcacía-Campos (2026, arXiv:2611.09718v1), Sections 2 and 5, develops the three-object sink-graph method and constructs a three-object, six-nonidentity-morphism model of \(\mathbb{RP}^2\), viewed as a degree-two Moore mapping cone. The paper optimizes **object count**, not the sharp total **morphism count** for wedges of projective planes. The present theorem uses that sink graph and the opposite-category symmetry to prove a sharp quadratic total-morphism minimum for every \(r\ge2\). General existence results for three-object models of finite two-dimensional complexes provide neither this exact lower bound nor the explicitly optimal simultaneous composition tables. A separate optimization for wedges of two-spheres concerns torsion-free second homology and does not imply the present torsion first-homology bound.

## Limitations

The optimization is restricted to finite acyclic categories with exactly three objects; models with more objects may use fewer nonidentity morphisms. It concerns wedges of genuine two-dimensional real projective planes and does not establish a corresponding formula for arbitrary Moore-space orders, arbitrary surface groups, higher-dimensional spaces or morphism counts after categorical joins. Finite Smith computations establish only the tested cases and do not independently verify the infinite-family proof. A complete exhaustive priority search is not claimed.

## References

1. I. Carcacía-Campos, *How many points does it take to see the homotopy of a space? Minimal acyclic categorical models*, arXiv:2611.09718v1 (first public 2026-11-06), especially Sections 2, 5 and 8. https://arxiv.org/abs/2611.09718 ; lawful full text https://borowiecki.dev/pdf/2611.09718 .
2. A. Hatcher, *Algebraic Topology*, Section 1.2 (cellular fundamental groups and homology), freely available at https://pi.math.cornell.edu/~hatcher/AT/AT.pdf .
