# A one-edge conductance defect on the four-cycle: sharp heat-Lipschitz transition and amplification

## Finding
Let \(G\) be the four-cycle with cyclically ordered vertices \(0,1,2,3\). Give edge \(01\) heat conductance \(r>0\), and edges \(12\), \(23\), and \(30\) conductance one. All edges retain **unit metric length**; the metric does not vary with conductance. For the counting-measure conductance Laplacian \(L_r\), put \(H_t=e^{-tL_r}\) and
\[
\operatorname{Lip}(f)=\max_{ij\in E(G)}|f(j)-f(i)|,\qquad
\Lambda_r(t)=\sup_{\operatorname{Lip}(f)>0}
\frac{\operatorname{Lip}(H_tf)}{\operatorname{Lip}(f)}.
\]
Set
\[
D_r=\sqrt{(r-1)^2+1},\qquad
\alpha_r=r+2-D_r,\qquad \beta_r=r+2+D_r.
\]
Then the following exact norm formula holds for **every real \(r>0\) and \(t\ge0\)**:
\[
\boxed{\Lambda_r(t)=
\begin{cases}
 e^{-(r+2)t}\!\left[\cosh(D_rt)+\dfrac{2-r}{D_r}\sinh(D_rt)\right],&0<r<1,\\[5pt]
 e^{-2t}+\dfrac{r-1}{2D_r}\left(e^{-\alpha_rt}-e^{-\beta_rt}\right),&r\ge1.
\end{cases}}
\]
For \(t>0\), the unique maximizing *edge* when \(0<r<1\) is the exceptional edge \(01\); when \(r>1\), precisely the two edges adjacent to it, \(12\) and \(30\), maximize. All four edges tie when \(r=1\).

Write the cyclic edge gradients as \(g=(f(1)-f(0),f(2)-f(1),f(3)-f(2),f(0)-f(3))\). Up to nonzero real scaling and addition of constants, the **complete nonconstant equality cases** at every \(t>0\) are as follows:

- For \(0<r<1\), \(g=(1,s,-1,-s)\) with any \(-1\le s\le1\).
- For \(r>1\), \(g=(1,1,-1,-1)\) or \(g=(1,-1,-1,1)\).
- For \(r=1\), every nonzero gradient satisfying \(g_0=-g_2\) and \(g_1=-g_3\), and no others.

The norm is **strictly decreasing for positive time** exactly when \(0<r\le3\). For \(r>3\) it initially increases, reaches one strict maximum at a positive time, then decreases strictly to zero. Consequently, transient amplification \(\Lambda_r(t)>1\) occurs exactly when \(r>3\), and the sharp, unattained family envelope is
\[
\boxed{\sup_{r>0,\ t\ge0}\Lambda_r(t)=\frac32.}
\]
For example, \(r=5\) has a unique peak near \(t=0.052821007\), with value approximately \(1.046881460\). A triangle cannot exhibit this phenomenon under any positive symmetric edge conductances when the graph distance assigns length one to every edge, because its Lipschitz seminorm is the oscillation, which a Markov semigroup contracts. Thus the four-cycle is the smallest simple cycle supporting positive-time Lipschitz amplification.

## Assumptions and scope
Functions are real valued on the four vertices, modulo constants. The vertex measure is counting measure; heat conductances are symmetric and strictly positive. The Laplacian is unnormalized:
\[
(L_rf)(i)=\sum_{j\sim i}c_{ij}(f(i)-f(j)).
\]
There is no conductance adjustment of graph-distance edge lengths. The same result for edges of common baseline conductance \(b>0\) and one exceptional conductance \(a>0\) follows by the identity \(H_t(a,b)=H_{bt}(a/b,1)\). At \(t=0\), \(\Lambda_r(0)=1\) and every nonconstant function is an extremizer; the preceding equality classification is for \(t>0\).

## Proof
**1. Exact gradient evolution.** Orient the edges cyclically and define \(g_i\) as above. The only compatibility relation is \(g_0+g_1+g_2+g_3=0\). Direct differentiation of \(f_t=H_tf\) gives
\[
\frac{d}{dt}g=B_rg,\quad
B_r=\begin{pmatrix}
-2r&1&0&1\\r&-2&1&0\\0&1&-2&1\\r&0&1&-2
\end{pmatrix}.
\]
Put \(h=g_0\), \(k=g_2\), \(z=(g_1+g_3)/2=-(h+k)/2\), and \(d=(g_1-g_3)/2\). Then
\[
\binom{h'}{k'}=
\begin{pmatrix}-(2r+1)&-1\\-1&-3\end{pmatrix}
\binom hk,\qquad d'=-2d.
\]
The two-by-two matrix is \(-(r+2)I+J\), where
\[
J=\begin{pmatrix}1-r&-1\\-1&r-1\end{pmatrix},\qquad J^2=D_r^2I.
\]
Thus its exponential is exactly
\[
e^{-(r+2)t}\!\left(\cosh(D_rt)I+\frac{\sinh(D_rt)}{D_r}J\right).
\]

**2. Exhaustive norming polytope.** The Lipschitz unit ball in gradient coordinates is
\(\mathcal P=\{g\in[-1,1]^4:\sum_i g_i=0\}\). Its only vertices are the six permutations of \((1,1,-1,-1)\). Indeed, at a vertex three cube coordinates must be saturated; the fourth is then forced to be \(\pm1\), and the zero-sum condition requires exactly two positive coordinates. Up to an overall minus sign, the six vertices correspond to the following three initial triples:
\[
(h,k,d)=(1,1,0),\quad(1,-1,1),\quad(1,-1,-1).
\]
As a linear functional reaches its maximum over a compact polytope at a vertex, these cases exhaust all candidate edge norms. Define
\[
X=e^{-(r+2)t}\cosh(D_rt),\quad
Y=e^{-(r+2)t}\frac{\sinh(D_rt)}{D_r},\quad Z=e^{-2t}.
\]
For the first triple, the gradients evolve as
\[
(h,k,z,d)=(X-rY,\ X+(r-2)Y,\ -X+Y,\ 0).
\]
For the second and third, the respective gradients are
\[
(h,k,z,d)=(X+(2-r)Y,\ -X-rY,\ (r-1)Y,\ \pm Z).
\]
Because \(D_r>|r-1|\), \(X+(1-r)Y>0\) and \(X+(r-1)Y>0\). The exceptional-edge and opposite-edge row norms are consequently
\[
N_{01}=X+(2-r)Y,\qquad N_{23}=X+rY.
\]
Indeed, for the exceptional edge the second/third triple strictly dominates the absolute first-triple output, and similarly for the opposite edge. For either side edge, the second/third triple gives \(Z+|r-1|Y\), while the first gives \(X-Y>0\). The former is strictly larger at \(t>0\): if \(r\ge1\), the coefficientwise exponential comparison below gives \(Z\ge X+Y\); if \(0<r<1\), set \(c=(2-r)/D_r>1\), so
\[
 e^{rt}> e^{-D_rt}\ge\cosh(D_rt)-c\sinh(D_rt),
\]
which is precisely \(Z+(1-r)Y>X-Y\) after multiplication by \(e^{-(r+2)t}\). Hence
\[
N_{12}=N_{30}=Z+|r-1|Y.
\]

**3. Comparison and exact maximum.** For every \(t>0\), compare \(e^{rt}\) with \(\cosh(D_rt)+D_r^{-1}\sinh(D_rt)\). The even Taylor coefficients of the latter are \(D_r^{2j}\), and its odd coefficients are \(D_r^{2j}\), versus \(r^{2j}\) and \(r^{2j+1}\) for \(e^{rt}\). Since \(D_r^2-r^2=2(1-r)\), the latter is strictly larger when \(r>1\), strictly smaller when \(0<r<1\), and identical when \(r=1\). Equivalently, \(Z-(X+Y)\) has the respective signs positive, negative, zero. Also,
\[
N_{01}-N_{23}=2(1-r)Y,
\]
\[
N_{01}-N_{12}=X+Y-Z\quad(0<r<1),\qquad
N_{12}-N_{23}=Z-X-Y\quad(r>1).
\]
This proves the claimed maximizing-edge sets and the exact piecewise formula, including \(r=1\).

**4. All equality cases.** For \(t>0\) the comparisons above are strict whenever \(r\ne1\). If \(r<1\), only edge \(01\) can norm the output. Its maximizing face of \(\mathcal P\) consists exactly of the segment joining the two vertices \((h,k,d)=(1,-1,\pm1)\) and its negative, yielding \(g=(1,s,-1,-s)\) after scaling. If \(r>1\), the two side edges norm the output, and each has exactly one maximizing vertex up to sign, producing the two stated sign patterns. For \(r=1\), all edges tie. The maximizing faces consist of gradients \((h,d,-h,-d)\) with \(\max(|h|,|d|)=1\) after normalization. Their union gives exactly the nonzero two-dimensional subspace \(g_0=-g_2\), \(g_1=-g_3\). This proves completeness, not just existence of extremizers.

**5. Time transition and sharp envelope.** For \(0<r<1\), put \(c=(2-r)/D_r>1\), \(A=(1+c)/2>0\), and \(B=(c-1)/2>0\). Then \(\Lambda_r=Ae^{-\alpha_rt}-Be^{-\beta_rt}\). Its derivative at zero is \(-2r<0\); hence \(A\alpha_r>B\beta_r\), and because \(\beta_r>\alpha_r>0\), its derivative remains negative at all positive times. For \(r=1\), the norm is \(e^{-2t}\).

For \(r>1\), note \(2<\alpha_r<\beta_r\), and write
\[
 e^{2t}\Lambda_r'(t)=-2+\frac{r-1}{2D_r}
 \left[\beta_r e^{-(\beta_r-2)t}-\alpha_r e^{-(\alpha_r-2)t}\right].
\]
The square-bracketed function starts at \(2D_r\), decreases through zero, reaches exactly one negative minimum, and increases thereafter toward zero from below. Its derivative is a difference of two exponentials with distinct positive decay rates and therefore has exactly one zero; the derivative at zero is negative. It follows that \(\Lambda_r'(t)<0\) for every \(t>0\) when \(1<r\le3\), whereas for \(r>3\) there is precisely one positive zero of \(\Lambda_r'\), changing sign from positive to negative. The initial derivatives are \(-2r\) for \(r<1\), \(-2\) for \(r=1\), and \(r-3\) for \(r>1\).

Finally, for every finite \(r>1\), the multiplier \((r-1)/(2D_r)\) is strictly below \(1/2\), and both exponential factors in the norm formula lie in \((0,1]\). Consequently \(\Lambda_r(t)<3/2\); for \(r\le1\), \(\Lambda_r(t)\le1\). On the other hand, taking \(r\to\infty\) and \(t=(\log r)/r\) yields \(\alpha_r\to3\), \(\beta_r\sim2r\), \(e^{-2t}\to1\), and \(\frac{r-1}{2D_r}(e^{-\alpha_rt}-e^{-\beta_rt})\to1/2\). This proves the exact, unattained family supremum.

## Verification
The accompanying standalone `verify_cycle.py` independently constructs the full four-by-four vertex generator, verifies the exact edge-gradient intertwining \(-GL_r=B_rG\) with rational arithmetic for ten rational conductance choices, and computes full-state heat kernels by stochastic uniformization rather than by the spectral formula. It exhausts all six vertices of the gradient Lipschitz polytope for each of forty rational parameter/time pairs, comparing the resulting dual norm with the displayed closed form at high precision. Its uniformization truncation is accompanied by an explicit geometric upper bound on the remaining Poisson tail. Direct differentiation of the closed formula gives the first-order coefficients \(-2r\) and \(r-3\); representative exact checks are included in the standalone script. These finite checks are corroboration: the all-parameter statements follow from the analytic argument above.

Run with `python verify_cycle.py` using only the Python standard library.

## Relationship to prior work
Ollivier's transport-curvature framework identifies Wasserstein contraction as the appropriate dual of Lipschitz control for Markov kernels [1]. Chafaï and Joulin develop discrete-gradient semigroup intertwining for birth-death processes [2]. Münch and Wojciechowski prove general weighted-graph curvature/heat-gradient equivalences and discuss combinatorial cycles [3, Theorems 2.6 and 3.8]. Those general principles do not give the explicit all-time one-defect four-cycle norm, the strict maximizing-edge selection, the exact conductance threshold \(r=3\), the extremizer-face classification, or the family envelope \(3/2\) in the inspected statements.

The homogeneous case \(r=1\) is standard: \(C_4\) is the unweighted complete bipartite graph \(K_{2,2}\), for which sharp heat-Lipschitz formulas are already available. Earlier exact heat results for larger unweighted cycles, a weighted four-vertex *path*, and other graph families use different generators or compatibility polytopes; the present weighted **cycle** result does not follow by substituting parameters in those formulas. No priority claim is made beyond the compared accessible material.

## Limitations
The claim is restricted to the four-cycle, one exceptional positive *heat conductance*, three common unit heat conductances, and the **unweighted** graph metric. It does not classify arbitrary four-cycle conductance quadruples, weighted metric lengths, normalized Laplacians, or higher cycles. The sharp bound \(3/2\) is a supremum over this one-defect family, not a universal bound for every finite graph. The listed equality cases concern positive time only. The literature search cannot rule out an unindexed equivalent computation; independent scientific review is not claimed.

## References
[1] Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886, first publicly submitted 2007-01-30, https://arxiv.org/abs/math/0701886.

[2] D. Chafaï and A. Joulin, *Intertwining and commutation relations for birth-death processes*, arXiv:1011.2331, first submitted 2010-11-10, https://arxiv.org/abs/1011.2331.

[3] F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, first submitted 2017-12-04, https://arxiv.org/abs/1712.00875.
