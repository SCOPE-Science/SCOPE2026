# A sharp hub-activation threshold for budgeted diagonal conditioning on stars

## Finding
Let \(m\ge2\) be an integer, let \(a>0\), and let \(B\ge0\). On the graph \(K_{1,m}\) with every edge having conductance one, label the hub \(0\) and leaves \(1,\ldots,m\). With its combinatorial Laplacian \(L\), set
\[
 A(d)=aI+L+\operatorname{diag}(d_0,d_1,\ldots,d_m),
 \qquad d_i\ge0,\quad \sum_{i=0}^m d_i=B.
\]
The spectral condition number \(\kappa_2(A)=\lambda_{\max}(A)/\lambda_{\min}(A)\) has **exactly one global minimizer** over this full simplex. Define
\[
 K=a(m+1)+2m+B,\qquad
 x_{\mathrm{free}}=\frac{B+m-1-2m(m-1)/K}{m+1},
 \qquad x_* =\min\left\{\frac Bm,x_{\mathrm{free}}\right\}.
\]
The optimizer is
\[
 d_1=\cdots=d_m=x_*,\qquad d_0=B-mx_*.
\]
The hub-activation threshold is the strictly positive number
\[
 B_c=\frac{m^2-3m-a(m+1)+\sqrt{[a(m+1)+3m-m^2]^2+4am(m-1)(m+1)}}{2}.
\]
For \(0<B\le B_c\), all budget is assigned equally to leaves and the hub receives zero; for \(B>B_c\), both hub and leaves receive positive loading. At \(B=0\), the sole feasible allocation is zero. No restriction to symmetric candidates is assumed in this theorem.

## Assumptions and scope
The graph is a simple undirected unit-weight star with at least two leaves. The baseline shift \(a\) is strictly positive, ensuring that every feasible \(A(d)\) is symmetric positive definite, including at \(B=0\). The vertex loads are nonnegative real numbers with exact total \(B\); there is no requirement of binary groundings or any constraint on the number of loaded vertices. Only spectral two-norm conditioning is optimized. Edge weights and the graph are fixed.

## Proof
**1. Unrestricted symmetry and its strictness.** For any feasible \(d\), let \(y=d_0\) and \(x=(d_1+\cdots+d_m)/m\). Define \(\bar d=(y,x,\ldots,x)\). The leaf-permutation symmetry of \(K_{1,m}\) and extremal-eigenvalue variational inequalities give \(\lambda_{\min}(A(d))\le\lambda_{\min}(A(\bar d))\) and \(\lambda_{\max}(A(d))\ge\lambda_{\max}(A(\bar d))\). For strictness when the leaf loads are not equal, note that the smallest eigenvalue of \(A(\bar d)\) is simple. Its unit eigenvector has a common nonzero coordinate on all leaves: the positive-definite Stieltjes matrix \(A(\bar d)\) is irreducible and its bottom eigenvector can be taken strictly positive (alternatively, use the two-dimensional invariant subspace and its nonzero offdiagonal coupling). For this vector \(v\),
\[
 v^{\mathsf T}A(d)v=v^{\mathsf T}A(\bar d)v=\lambda_{\min}(A(\bar d)).
\]
If equality held in the minimum-eigenvalue comparison, \(v\) would have to be a bottom eigenvector of \(A(d)\). The leaf eigenvector equations, with nonzero common leaf coordinate, then force all \(d_i\) on the leaves to be equal. Thus unequal leaf loading gives a **strictly smaller** minimum eigenvalue and a weakly larger maximum eigenvalue; its condition number is strictly worse. Every global minimizer must therefore have equal leaf loadings.

**2. Exact quotient spectrum.** Put every leaf loading equal to \(x\), and the hub loading \(y=B-mx\); thus \(0\le x\le B/m\). Leaf-difference vectors have eigenvalue \(a+1+x\), with multiplicity \(m-1\). The remaining quotient matrix in the normalized hub/uniform-leaf basis is
\[
 \begin{pmatrix}a+m+B-mx&-\sqrt m\\-\sqrt m&a+1+x\end{pmatrix}.
\]
Write
\[
 H=2a+m+1+B-(m-1)x,\quad D=m-1+B-(m+1)x,
 \quad R=\sqrt{D^2+4m}.
\]
The quotient eigenvalues are \(\lambda_{\pm}=(H\pm R)/2\). Because \(m>0\), they strictly straddle the leaf-difference eigenvalue; therefore they are the full-matrix extreme eigenvalues, with \(0<R<H\) by positive definiteness. Hence \(\kappa_2=(H+R)/(H-R)\).

**3. One-dimensional exact minimization.** The ratio \((H+R)/(H-R)\) is strictly increasing in \(R/H\in(0,1)\); minimizing its square is equivalent to minimizing
\[
 F(x)=\frac{D^2+4m}{H^2}.
\]
Set \(K=a(m+1)+2m+B>0\). Direct differentiation, with no omitted boundary cases, gives
\[
 F'(x)=\frac{4(m+1)K}{H^3}\left(x-x_{\mathrm{free}}\right).
\]
Here \(x_{\mathrm{free}}>0\): at \(B=0\), \(x_{\mathrm{free}}=a(m-1)/K>0\), and increasing \(B\) increases it. As \(H>0\), \(F\) strictly decreases up to \(x_{\mathrm{free}}\) and strictly increases afterward. Its **unique** minimizer on \([0,B/m]\) is \(x_*=\min\{B/m,x_{\mathrm{free}}\}\). Combined with step 1, this proves unrestricted uniqueness.

**4. Exact support transition.** Clearing strictly positive denominators in \(x_{\mathrm{free}}=B/m\) yields
\[
 B^2+[a(m+1)+3m-m^2]B-am(m-1)(m+1)=0.
\]
For \(a>0\) and \(m\ge2\), the constant term is negative, so exactly one positive root exists. The quadratic formula gives \(B_c\) above, and the sign shows \(x_{\mathrm{free}}>B/m\) if \(0\le B<B_c\), with the inequality reversed for \(B>B_c\). At equality the optimizer is still unique with zero hub loading. This completes the proof.

## Verification
`verify.py` uses only the Python 3 standard library and is run as `python3 verify.py`. It checks the differentiated rational identity and objective comparisons exactly using fractions over a grid of \(m,a,B,x\), checks quotient eigenvalues by an independently implemented Jacobi symmetric eigensolver, and tests full matrices with independently unequal leaf loads. The executed checker completed **8,962 assertion checks**. In particular, for \(m=2\) and \(a=1\), \(B_c=1\). At budget \(B=2\), the optimal leaf loading is \(23/27\) and the hub loading is \(8/27\). The analytic argument above, not the finite checks, proves the all-parameter theorem.

## Relationship to prior work
Greif and Varah (2006) analyze condition-number minimization for low-rank matrix modifications with free eigenvector directions. Their primary result does not constrain a nonnegative *diagonal* addition to a fixed total budget or provide the star's exact hub-support boundary. Lu and Pong (2011) show how condition-number minimization over a general convex matrix set can be solved via convex programming; the present feasible family falls within that framework, but their general results do not themselves give this closed-form star allocation or its unrestricted uniqueness and sharp threshold. Their diagonal *preconditioning* section concerns multiplicative congruence, a different operation. Kurras, von Luxburg and Blanchard (2014) study vertex-dependent diagonal changes in normalized graph Laplacians from the viewpoint of graph geometry; their statements concern a different operator and objective. Existing graph edge-conductance spectral-gap designs likewise do not determine the fixed-edge, additive vertex-loading optimum.

## Limitations
This is an exact theorem for shifted unit-weight stars only, not a claim about arbitrary weighted trees, general graphs, nonpositive baselines, or unconstrained low-rank modifications. Other objective functions such as trace of the inverse or maximum eigenvalue may have distinct optimizers. The reference comparisons identify an explicit specialization absent from the inspected texts, but do not prove that no unindexed equivalent formula exists. No independent mathematical validation has been performed.

## References
1. C. Greif and J. M. Varah, *Minimizing the Condition Number for Small Rank Modifications*, SIAM J. Matrix Anal. Appl. 29 (2006), 82–97. Published online 21 December 2006. https://doi.org/10.1137/050647554 . Author full text: https://www.cs.ubc.ca/~greif/Publications/gv2006.pdf .
2. Z. Lu and T. K. Pong, *Minimizing Condition Number via Convex Programming*, SIAM J. Matrix Anal. Appl. 32 (2011), 1193–1211. https://doi.org/10.1137/100795097 . Author-provided full text: https://www.researchgate.net/publication/220656493_Minimizing_Condition_Number_via_Convex_Programming .
3. M. Kurras, U. von Luxburg and G. Blanchard, *The f-Adjusted Graph Laplacian: a Diagonal Modification with a Geometric Interpretation*, ICML 2014, PMLR 32. https://proceedings.mlr.press/v32/kurras14.pdf .
