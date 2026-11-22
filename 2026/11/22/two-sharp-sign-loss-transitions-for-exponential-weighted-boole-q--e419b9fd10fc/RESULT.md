# Two sharp sign-loss transitions for exponential-weighted Boole quadrature

## Finding

For the five fixed nodes \(x_j=j/4\), \(j=0,1,2,3,4\), let \(L_j\) be their degree-four Lagrange cardinal polynomials and let
\[
W_j(\lambda)=\int_0^1 e^{\lambda x}L_j(x)\,dx,\qquad \lambda\in\mathbb R.
\]
These weights define the unique five-node interpolatory quadrature rule for the strictly positive exponential weight, exact for every polynomial of degree at most four. There are exactly two positive numbers \(\alpha<\beta\) with
\[
\alpha\in(3.111841,3.111843),\qquad
\beta\in(3.225119,3.225122),
\]
such that for every \(\lambda\ge0\): \(W_1,W_3,W_4>0\) always; \(W_2\) is positive, zero or negative according as \(\lambda<\alpha\), \(\lambda=\alpha\) or \(\lambda>\alpha\); and \(W_0\) is positive, zero or negative according as \(\lambda<\beta\), \(\lambda=\beta\) or \(\lambda>\beta\). Each zero is unique on the positive real axis. For negative \(\lambda\), the sign pattern reverses its node indices. In particular, all five weights are nonnegative exactly when \(|\lambda|\le\alpha\), and strictly positive exactly when \(|\lambda|<\alpha\).

The first failure belongs to the midpoint node; after the second transition the midpoint and the endpoint opposite the favored exponential tail both have negative weights. The two thresholds are defined intrinsically as the unique positive roots of \(W_2\) and \(W_0\), respectively. No elementary formula for them is assumed.

## Assumptions and scope

The interval is \([0,1]\), the nodes are precisely \(0,1/4,1/2,3/4,1\), and the exponential weight is \(e^{\lambda x}\) without additional changes to nodes or cardinal polynomials. A positive normalization of the integration density would leave every sign unchanged. The conclusion is about the signs of interpolation-based weights, not an error estimate, not an optimized quadrature design, and not quadrature exactness on arbitrary functions. At \(\lambda=0\), the rule becomes ordinary Boole quadrature, with its usual extra degree-five exactness; for general nonzero \(\lambda\), only degree-four exactness is asserted.

## Proof

For \(k\in\mathbb Z_{\ge0}\) put \(m_{j,k}=\int_0^1 x^kL_j(x)\,dx\). Direct expansion and exact rational integration yield the *all-index* identities, with \(D_k=(k+2)(k+3)(k+4)(k+5)\):
\[
\begin{aligned}
m_{0,k}&=-\frac{(k-1)(3k^2-5k+28)}{3(k+1)D_k},\\
m_{1,k}&=\frac{16(k^2-3k+8)}{3D_k},\\
m_{2,k}&=-\frac{4(3k^2-5k-4)}{D_k},\\
m_{3,k}&=\frac{16(3k^2+7k+8)}{3D_k},\\
m_{4,k}&=\frac{(k+1)(3k^2+11k+28)}{3D_k}.
\end{aligned}
\]
All denominators are strictly positive. The numerators prove that \(m_{j,k}>0\) for every \(k\ge0\) and \(j\in\{1,3,4\}\); that \(m_{0,0}=7/90\), \(m_{0,1}=0\), and \(m_{0,k}<0\) for every \(k\ge2\); and that \(m_{2,k}>0\) for \(k=0,1,2\) but \(m_{2,k}<0\) for every \(k\ge3\). Taylor expansion, justified by uniform convergence on the compact interval, gives
\[
W_j(\lambda)=\sum_{k=0}^{\infty}\frac{m_{j,k}}{k!}\lambda^k.
\]
Thus \(W_1,W_3,W_4>0\) for all \(\lambda\ge0\). Also \(W_0(\lambda)=m_{0,0}-\sum_{k\ge2}|m_{0,k}|\lambda^k/k!\) is strictly decreasing on \((0,\infty)\). Further,
\[
\frac{W_2(\lambda)}{\lambda^2}=
\frac{m_{2,0}}{\lambda^2}+\frac{m_{2,1}}{\lambda}+\frac{m_{2,2}}2-
\sum_{k=3}^{\infty}\frac{|m_{2,k}|}{k!}\lambda^{k-2}
\]
is strictly decreasing there. Both \(W_0(0)\) and \(W_2(0)\) are positive, while \(L_0(x)=(x-1)+O((1-x)^2)\) and \(L_2(x)=12(x-1)+O((1-x)^2)\) as \(x\uparrow1\). Laplace's endpoint estimate therefore gives \(W_0(\lambda)\sim-e^\lambda/\lambda^2\) and \(W_2(\lambda)\sim-12e^\lambda/\lambda^2\) as \(\lambda\to\infty\). Hence each has exactly one positive zero and is negative beyond that zero.

It remains to prove the order of the two zeros, not merely observe it numerically. At the rational test point \(z=63/20\), let
\[
P_{j,N}(z)=\sum_{k=0}^{N}\frac{m_{j,k}z^k}{k!},\qquad N=30.
\]
For \(j=0,2\), write \(L_j(x)=\sum_r c_{jr}x^r\) and put \(M_j=\sum_r|c_{jr}|/(r+1)\). Exact polynomial arithmetic gives \(M_0=1957/90\) and \(M_2=1142/15\), hence
\[
|W_j(z)-P_{j,30}(z)|\le
55M_j\frac{z^{31}}{31!},
\]
because \(0<z<4\) and \(e^4<55\). Exact rational comparisons establish
\[
P_{0,30}(z)>55M_0\frac{z^{31}}{31!},\qquad
P_{2,30}(z)<-55M_2\frac{z^{31}}{31!}.
\]
Consequently \(W_2(z)<0<W_0(z)\), which proves \(\alpha<z<\beta\). The same certified Taylor enclosure at the displayed rational bracket endpoints isolates each unique root. The standalone verifier reconstructs every identity and inequality.

Finally \(L_j(1-x)=L_{4-j}(x)\) by uniqueness of cardinal interpolation. Substitution \(x\mapsto1-x\) gives \(W_j(-\lambda)=e^{-\lambda}W_{4-j}(\lambda)\) for every \(\lambda\ge0\), establishing the negative-tilt classification and all boundary cases.

## Verification

Run `python verify.py` with Python 3 and SymPy. The standalone script expands all five cardinal polynomials, derives the all-index rational moment identities, checks interpolation exactness at the nodes, and verifies the rational Taylor remainder certificates for both the interlacing test point and the two explicit root brackets. In particular it verifies \(e^4<55\) with an exact rational series/tail bound. The proof of uniqueness holds for infinitely many Taylor coefficients by the displayed closed forms and their signs; the finite checks are certificates for the bracket inequalities, not substitutes for uniqueness.

## Relationship to prior work

Classical closed Newton–Cotes interpolation and its positive unweighted five-point Boole coefficients are established in Sermutlu (2019), notably the closed-rule coefficient table. Trefethen (2021 preprint; 2022 journal) discusses the limitations of fixed-node Newton–Cotes exactness and why mixed signs matter. The DLMF states the general weighted interpolatory-quadrature construction; weighted Newton–Cotes rules for a Chebyshev weight are studied in Dehghan and collaborators (2005). These frameworks justify the definition of the weights but do not, in the inspected relevant passages, specify the two sharp sign transitions for the exponential weight. The present statement is the classification of those signs for the fixed five-point Boole stencil, not the generic weight formula.

## Limitations

The theorem does not establish error superiority over alternative rules, positivity for other fixed node sets, or the optimality of Boole nodes under exponential tilting. Generic weighted interpolatory formulas contain enough information for case-by-case algebraic recomputation, so an independent historical-priority review is warranted; an inaccessible older weighted-rule article remains a particular comparison risk. Numeric approximations are supported by exact rational enclosures, not floating-point sign tests.

## References

1. E. Sermutlu, *A close look at Newton–Cotes integration rules*, Results in Nonlinear Analysis 2 (2019), 48–60. First available online May 10, 2019 according to the article PDF. https://nonlinear-analysis.com/index.php/pub/article/download/23/22/22
2. L. N. Trefethen, *Exactness of quadrature formulas*, arXiv:2101.09501, first posted January 23, 2021; SIAM Review 64 (2022), 132–150. https://arxiv.org/abs/2101.09501
3. NIST Digital Library of Mathematical Functions, Section 3.5(iv), *Interpolatory Quadrature Rules*. https://dlmf.nist.gov/3.5
4. *The first kind Chebyshev–Newton–Cotes quadrature rules (closed type) and its numerical improvement*, Applied Mathematics and Computation 168 (2005), 479–495. https://doi.org/10.1016/j.amc.2004.09.048
