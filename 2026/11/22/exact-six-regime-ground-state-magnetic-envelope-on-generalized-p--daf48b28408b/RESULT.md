# Exact six-regime ground-state magnetic envelope on generalized Petersen spin strips

## Finding
For each integer \(n\ge5\), consider the three-state antiferromagnetic Potts model on the generalized Petersen graph \(GP(n,2)\), with equal nearest-edge penalty \(J>0\), one distinguished spin color, and a real field \(H\) favoring that color. Write \(h=H/J\) and let \(G_n(h)\) be the minimum energy divided by \(Jn\), i.e., normalized **per two-vertex cell**, not per vertex. Define
\[
 g(h)=\min\left\{\frac12,-\frac h2,-\frac{4h}{5},\frac14-h,\frac35-\frac{6h}{5},3-2h\right\}.
\]
Then \(G_n(h)\ge g(h)\) for all \(n\ge5\) and all real \(h\). **Equality holds for every real \(h\) whenever \(20\mid n\)**, and \(\lim_{n\to\infty}G_n(h)=g(h)\) for every fixed real \(h\), with an error \(O_h(1/n)\). The five distinct critical fields of this limiting envelope are exactly
\[
 h=-1,\quad 0,\quad \frac54,\quad\frac74,\quad3.
\]
For \(20\mid n\) and a field strictly between successive critical values, every ground state has, respectively, \(0,\frac12,\frac45,1,\frac65,2\) preferred-color spins per cell. At a critical field the adjacent periodic witnesses coexist. At every differentiability field, the preferred-color fraction of *any* finite-size minimizer converges to the corresponding slope \(-g'(h)\) per cell as \(n\to\infty\).

## Assumptions and scope
The vertices are \(u_i,v_i\), indexed modulo \(n\). Edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). The three labeled colors are \(\{0,1,2\}\), and the favored color is \(0\). For a coloring \(\sigma\), let \(P(\sigma)=\sum_{xy\in E}\mathbf1_{\sigma_x=\sigma_y}\) and \(K(\sigma)=\sum_x\mathbf1_{\sigma_x=0}\). The physical Hamiltonian is \(J P(\sigma)-H K(\sigma)\) and \(G_n(h)=n^{-1}\min_\sigma(P(\sigma)-hK(\sigma))\). There are exactly \(2n\) vertices and \(3n\) edges. The thermodynamic statement is a zero-temperature *ground-energy-density* limit; no assertion is made about a positive-temperature nonanalyticity.

## Proof
**Finite-state reduction.** Let \(S=\{0,1,2\}^3\). For a transition
\[
 (u,p,q)\longrightarrow (x,y,p),
\]
put
\[
 c=\mathbf1_{u=x}+\mathbf1_{q=y}+\mathbf1_{x=y},\qquad k=\mathbf1_{x=0}+\mathbf1_{y=0}.
\]
Every \(n\)-step closed walk on this 27-state directed graph corresponds to precisely one labeled Potts coloring of \(GP(n,2)\). Its accumulated \(c\) is \(P\): the three terms count, respectively, outer-ring bonds, inner step-two bonds, and spokes, once each. Its accumulated \(k\) is \(K\). This correspondence is valid for every \(n\ge5\).

**Global lower bound.** For each of the five pairs \((h_*,g_*)\) equal to \((-1,1/2)\), \((0,0)\), \((5/4,-1)\), \((7/4,-3/2)\), and \((3,-3)\), the accompanying `verify_potts.py` contains an explicit 27-component integer potential \(\pi\) and a positive integer multiplier \(L\). For **all 243 directed transitions** it verifies the exact integer inequality
\[
 L(c-h_*k-g_*)+\pi(s)-\pi(t)\ge0.
\]
Summing over any closed walk cancels the potential and gives \(P-h_*K\ge ng_*\). Between consecutive listed fields, affine interpolation yields the corresponding straight-line bound. For \(h<-1\), use \(K\ge0\) to extend the \(h=-1\) bound \(P-hK\ge n/2\); for \(h>3\), use \(K\le2n\) to extend \(P-3K\ge-3n\) to \(P-hK\ge n(3-2h)\). Thus \(G_n(h)\ge g(h)\) at every real field. The supplied exact arrays are finite witnesses to each universal inequality, and can be checked by 1,215 integer comparisons without trust in a numerical minimizer.

**Matching periodic upper bound.** The following six periodic words encode consecutive outer/inner spin-color pairs \((u_i,v_i)\). Their periods \(\ell\), total equal-edge costs \(P\), and total favored-color counts \(K\) are verified by direct substitution, including both wrap bonds:

| Regime | Encoded period | \(\ell\) | \(P\) | \(K\) |
|---|---|---:|---:|---:|
| \(h<-1\) | `11211222` | 4 | 2 | 0 |
| \(-1<h<0\) | `01120221` | 4 | 0 | 2 |
| \(0<h<5/4\) | `0110200212` | 5 | 0 | 4 |
| \(5/4<h<7/4\) | `00100112` | 4 | 1 | 4 |
| \(7/4<h<3\) | `0010010110` | 5 | 3 | 6 |
| \(h>3\) | `00` | 1 | 3 | 2 |

Each witness attains the corresponding affine branch of \(g(h)\). As every period divides 20, for \(20\mid n\) all six tilings exist as closed spin assignments, so \(G_n(h)\le g(h)\), proving equality. For any general \(n\), repeat a branch's word for the first \(n\) cells and close the rings. Only a bounded number of outer and inner wrap bonds, and at most four incomplete-period cell occupations, differ from an integral number of periods; therefore the excess energy is \(O_h(1)\). Combined with the lower bound this proves \(G_n(h)=g(h)+O_h(1/n)\).

**Spin occupancies.** For a fixed \(n\) and an interval where \(G_n(h)=g(h)\) is affine, any minimizing coloring corresponds to an affine line \((P-hK)/n\) touching the lower envelope. Since it is not below the envelope on either side of the field, its slope must equal \(g'(h)\), proving the exact densities for \(20\mid n\). For arbitrary \(n\), the same conclusion in the limit follows from convergence of concave functions \(G_n\to g\) and the standard left- and right-secant slope bounds at every differentiability point. The strict changes of slopes prove that the five stated fields and no others are breakpoints of \(g\).

## Verification
Run `python3 verify_potts.py` using Python 3 and the standard library. The exact checker evaluates all 1,215 transition dual inequalities, all six periodic witnesses, and an *independent* min-plus dynamic-programming computation of the length-20 closed-walk optimum at eleven rational field values. Successful output includes `POTTS_DUAL_CERTIFICATES_OK 1215`, `PERIODIC_WITNESSES_OK 6`, and `INDEPENDENT_MINPLUS_CLOSURES_OK 11`. The dynamic-programming cases are supplementary finite checks; universal correctness comes from the five exact dual certificates plus the periodic construction, not from extrapolating finite computations. The exact checker also verifies the ten-cell dodecahedron at \(h=3/2\) has total optimized \(P-hK=-12\), not \(-5n/4\) from the new limiting envelope at that field.

## Relationship to prior work
Chang and Shrock (2000) give exact zero-field Potts solutions for next-nearest-neighbor coupled square-lattice strips, which are degree-five strip graphs, **not** the degree-three \(GP(n,2)\) family. Chang and Shrock (2009) and Shrock and Xu (2010) establish general external-field Potts transfer-matrix frameworks; neither inspected paper supplies the six affine branches and five exact critical fields on the present graph sequence. An existing finite exact field diagram for the dodecahedron \(GP(10,2)\) has middle transition \(h=3/2\), whereas at sizes divisible by 20 the present argument proves two distinct transitions \(h=5/4,7/4\); the old ten-cell theorem by itself cannot imply this family-wide distinction. Generalized-Petersen chromatic-polynomial work concerns proper colorings or zero-field quantities, not the nonzero-field, improper-coloring ground-state envelope. These comparisons do not assert that every historical paper has been exhausted.

## Limitations
The model has exactly three labeled spin colors, equal positive antiferromagnetic edge penalty, uniform field on one color, and inner step two. The exact finite-size equality is proved only for \(20\mid n\); arbitrary \(n\) have an asymptotic equality, not necessarily the same exact thresholds. Neither finite-temperature analyticity nor full degeneracy/entropy is classified. The lower bounds rely on supplied finite arithmetic certificates, not on a short structural decomposition of every minimizer. An earlier unindexed treatment of this particular zero-temperature transfer problem remains possible. Independent external audit has not been performed.

## References
1. S.-C. Chang and R. Shrock, *Exact Partition Function for the Potts Model with Next-Nearest Neighbor Couplings on Strips of the Square Lattice*, arXiv:cond-mat/0007505, first publicly submitted 2000-07-31, https://arxiv.org/abs/cond-mat/0007505.
2. S.-C. Chang and R. Shrock, *Structure of the Partition Function and Transfer Matrices for the Potts Model in a Magnetic Field on Lattice Strips*, arXiv:0907.0925, first publicly submitted 2009-07-06, https://arxiv.org/abs/0907.0925.
3. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182, first publicly submitted 2010-09-07, https://arxiv.org/abs/1009.1182.
4. *Complete zero-temperature magnetic-field diagram of the three-state Potts antiferromagnet on the dodecahedron*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-zero-temperature-magnetic-field-diagram-of-the-three-st--b67d093a5d08, comparison of the exact ten-cell specialization only.
