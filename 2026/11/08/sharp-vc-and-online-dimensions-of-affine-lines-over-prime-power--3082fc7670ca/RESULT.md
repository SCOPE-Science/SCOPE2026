# Sharp VC and online dimensions of affine lines over prime-power chain rings

## Finding
For every prime \(p\) and integer \(e\ge1\), let \(R=\mathbb Z/p^e\mathbb Z\). The concept class of all distinct free affine lines in \(R^2\), queried by point membership, satisfies
\[
\operatorname{VCdim}(\mathcal L_{p,e})=2,\qquad
\operatorname{Ldim}(\mathcal L_{p,e})=e+1.
\]
Indeed, **all** two-element point supports are VC-shattered and **no** three-element support is. The complete support-count polynomial is
\[
\Phi_{p,e}(z)=1+p^{2e}z+\binom{p^{2e}}2z^2.
\]
In particular, for any fixed prime the separation between adaptive and static dimensions grows arbitrarily with the chain length \(e\).

## Assumptions and scope
Write \(q=p^e\), \(X=R^2\). A vector \(v=(v_1,v_2)\) is **primitive** when at least one coordinate is a unit in \(R\). A free affine line is
\(L(a,v)=a+Rv=\{a+tv:t\in R\}\), where \(a\in X\) and \(v\) is primitive. Distinct subsets, not repeated parametrizations, are the concepts. The query domain is the full \(X\); its answer for a line is one exactly on that line. The VC dimension concerns fixed point supports; Littlestone dimension concerns complete binary trees of adaptive point queries. All primes, including two, and all positive exponents are covered.

Define \(\mathbb P^1(R)\) as the set of free rank-one submodules \(Rv\) with primitive \(v\). Every affine line has exactly \(q\) points. Each direction has \(q\) affine cosets. There are \(p^{e-1}(p+1)\) directions and hence \(p^{2e-1}(p+1)\) distinct lines.

## Proof
**1. Every pair is shattered.** Take distinct \(x,y\in R^2\). The difference \(y-x\) has a unique valuation \(0\le r<e\), so \(y-x=p^r v\) for some primitive \(v\). The line \(x+Rv\) contains both. Choose any primitive direction reducing modulo \(p\) to one different from the direction of \(v\); the corresponding line through \(x\) avoids \(y\). The analogous line through \(y\) avoids \(x\). Finally, another coset parallel to \(x+Rv\) avoids both (there are \(q\ge2\) parallel cosets). Thus the four required traces occur. Every singleton is also shattered.

**2. No triple is shattered.** If three distinct points \(x,y,z\) are not on one line, their all-positive trace is absent. Otherwise let their parameters on a common line \(a+Rv\) be \(s_x,s_y,s_z\in R\). Choose a pair, say \(x,y\), minimizing the valuation \(r=v_p(s_i-s_j)\) over the three differences (with the convention \(v_p(0)=e\)). Because all parameters are distinct, \(r<e\). Then \(s_z-s_x\) is divisible by \(p^r\), while \(s_y-s_x=p^r u\) for a unit \(u\). Thus \(s_z-s_x=c(s_y-s_x)\) for some \(c\in R\), and \(z=x+c(y-x)\). Every free affine line containing \(x,y\) is an affine \(R\)-submodule translate and necessarily contains \(z\). Hence the trace positive exactly on \(\{x,y\}\) is absent. Heredity of shattering excludes all larger supports. This proves the polynomial and VC dimension.

**3. Geometry of lines through one point.** Fix \(a\in R^2\). Lines through \(a\) are in bijection with \(\mathbb P^1(R)\). Reduction of primitive directions modulo \(p^k\), for \(1\le k\le e\), gives a rooted hierarchy with \(p+1\) first-level classes, and **exactly \(p\) children** for every node at levels \(1,\ldots,e-1\). Its leaves are the distinct directions. If \(x\ne a\), write \(x-a=p^r w\) with \(w\) primitive. A direction \(Rv\) contains \(x-a\) exactly when \(Rv\) and \(Rw\) agree modulo \(p^{e-r}\). Hence the positive answers to any nontrivial point query among the lines through \(a\) form exactly one cylinder at a level \(1\) through \(e\). Every such cylinder is attainable by choosing \(x=a+p^{e-k}w\), where \(k\) is its level. Querying \(a\) itself has constant answer one.

**4. The pencil has exact online dimension \(e\).** The cylinder family is laminar. On the all-positive path of a complete shattered mistake tree, each query must genuinely split the current hypotheses and its positive branch strictly refines the preceding cylinder. A strict cylinder chain can have at most \(e\) such refinements; no depth-\(e+1\) tree is possible. Conversely, a full cylinder at level \(k<e\) contains \(p\ge2\) full child cylinders. A query selecting one child has both positive and negative branches containing a full child cylinder; iterate this construction for \(e-k\) rounds. At the root, use two of the \(p+1\) full first-level cylinders. This gives a depth-\(e\) tree for every complete pencil of lines through \(a\).

The same lower construction applies if just **one direction is removed** from a complete pencil: of the \(p+1\ge3\) first-level cylinders, at least two remain intact. The first split between them has two depth-\(e-1\) descendants, proving depth \(e\). This argument also covers \(e=1\).

**5. Upper and lower bounds for all affine lines.** In any complete mistake tree for \(\mathcal L_{p,e}\), the first positive branch at a queried point \(a\) is a subclass of the pencil through \(a\), which has Littlestone dimension \(e\). A depth-\(e+2\) tree is therefore impossible; \(\operatorname{Ldim}(\mathcal L_{p,e})\le e+1\).

For the reverse bound, query \(a=(0,0)\) first. The positive branch includes a full pencil and supports depth \(e\). Choose \(b=(1,0)\). The negative branch includes all lines through \(b\) **except** the unique line that also contains \(a\); uniqueness follows because \(b-a\) is primitive. As shown above, this punctured pencil still supports depth \(e\). Attaching these two trees below the first query gives a full depth-\(e+1\) tree. This proves the exact Littlestone dimension.

## Verification
The standalone file `affine_chain_line_checker.py` constructs the actual lines as bitsets for \((p,e)=(2,1),(3,1),(5,1),(2,2),(3,2),(2,3)\). For all six cases it exhaustively verifies that every pair is shattered and no triple is. It also constructs and checks a depth-\(e+1\) tree, including its \(2^{e+1}\) leaf traces, in each case. An independent exhaustive minimax recursion confirms the exact Littlestone upper bound for \((p,e)=(2,1),(3,1),(2,2)\). Finite verification does not replace Steps 1–5 for all primes and exponents. Run `python3 affine_chain_line_checker.py` with Python 3.10 or newer; no third-party packages are needed.

## Relationship to prior work
Guingona, Kolesnikov, Nierwinski and Soucy (arXiv:2109.04805v1, first public September 10, 2021) prove equal VC and Littlestone dimensions for zero sets of nontrivial linear combinations over **fields**. Their result explains the ordinary affine-plane case \(e=1\), but its field hypotheses do not imply the ring-depth dependence here. The affine Hjelmslev point-line setting is classical; Bajalan, Landjev and Rousseva (2023) examine the **incidence-matrix rank** of projective Hjelmslev planes over finite chain rings, a different invariant. No identical ring-depth learning-dimension statement was identified in the inspected accessible material. That is a bounded literature comparison, not a proof of historical uniqueness.

## Limitations
Only lines generated by **primitive** directions in the two-dimensional module \(R^2\) are included. This is not a theorem for arbitrary nonfree solution sets of linear congruences, for all affine submodules, for higher-dimensional modules, or for infinite local rings. The result supplies an exact realizable deterministic mistake-tree rank; it does not establish randomized, noisy, or distributional sample complexity. Independent external verification and comprehensive historical priority assessment have not been performed.

## References
1. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1 (2021), https://arxiv.org/abs/2109.04805.
2. M. Bajalan, I. Landjev and A. Rousseva, *On the p-Rank of the Incidence Matrix of a Projective Hjelmslev Plane*, CSECS 2023, DOI:10.1007/978-3-031-44668-9_2, https://doi.org/10.1007/978-3-031-44668-9_2.
3. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, PMLR 132 (2021), pp. 686–696, https://proceedings.mlr.press/v132/ghazi21a.html.
