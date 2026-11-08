# Two symmetry-breaking three-cycles at a sharp quadratic nilpotent-map threshold

## Finding
For every real nonzero \(\kappa\), put \(K=\kappa^2\), \(g(t)=t(t-1)\), and consider the three-dimensional polynomial map
\[
F_\kappa(X,Y,Z)=\bigl(\kappa[g(Y)-g(Z)],\ Z,\ K[g(Y)-g(Z)]^2\bigr).
\]
This is the \(a_{12}=1\), \(\nu=0\), \(P_1(t)=\kappa t(t-1)\) specialization of the polynomial conjugate in Castañeda and Rebollo-Perdomo, equation (10). Every primitive period-three orbit has either a repeated value or three pairwise distinct values among its three successive \(Y\)-coordinates.

**Sharp distinct-coordinate theorem.** There are exactly two primitive three-cycles with three pairwise distinct successive \(Y\)-coordinates if \(K>125/12\), and none if \(0<K\le125/12\). For \(K>125/12\), let \(u<v<w\) be the three real roots of
\[
C_K(t)=\left(t-\frac15\right)^2\left(t-\frac45\right)+\frac{1}{3K}.
\]
They satisfy \(0<u<1/5<v<3/5<w<4/5\). The two cycles correspond exactly to the two cyclic orders of these three numbers: \((u,v,w)\) and \((u,w,v)\). The associated starting state for an ordered cyclic triple \((a,b,c)\) is
\[
\bigl(\kappa[g(c)-g(a)],a,b\bigr).
\]
The discriminant and transition polynomial are
\[
\operatorname{disc} C_K=\frac{3(12K-125)}{125K^2},\qquad C_{125/12}(t)=t\left(t-\frac35\right)^2.
\]
Thus the two new oriented cycles coalesce at the sharp threshold with the repeated-coordinate orbit involving \(0\) and \(3/5\).

**Complete real primitive three-cycle count.** Including the repeated-coordinate cycles already accessible through the established scalar criterion, the exact count \(N_3(K)\), modulo cyclic rotation, is
\[
N_3(K)=\begin{cases}
1,&0<K<27/4,\\
2,&K=27/4,\\
3,&27/4<K\le125/12,\\
5,&K>125/12.
\end{cases}
\]
In particular the onset at \(125/12\) increases the count by exactly two; it is not an assertion about attraction, transversality, or the full dynamics outside period three.

## Assumptions and scope
The phase space is \(\mathbb R^3\); \(\kappa\in\mathbb R\setminus\{0\}\); the map is iterated forward. A primitive period-three orbit consists of exactly three distinct states and is identified modulo cyclic time shift, not modulo time reversal. The projected height pair \((Y,Z)\) evolves under \(H_K(Y,Z)=(Z,K[g(Y)-g(Z)]^2)\), and the first coordinate of any periodic state is uniquely determined by the preceding projected state. Thus counting three-cycles of \(H_K\) counts those of \(F_\kappa\). This theorem concerns the polynomial conjugate of a nilpotent-Jacobian family; the displayed conjugate need not itself have pointwise nilpotent Jacobian.

## Proof
Write the projected successive \(Y\)-values on a three-cycle as \((u,v,w)\). Periodicity is equivalent to
\[
u=K[g(v)-g(w)]^2,\qquad v=K[g(w)-g(u)]^2,\qquad w=K[g(u)-g(v)]^2.\tag{1}
\]
The all-equal case of (1) has only \(u=v=w=0\), the fixed point. If any two values coincide, say \(u=v=s\), (1) forces \(w=0\), and then \(s=K[g(s)]^2\). Conversely \((s,s,0)\) is a genuine three-cycle whenever \(s\ne0\) solves this equation. Since \(s=K s^2(s-1)^2\), the nonzero solutions are exactly the positive roots of
\[
K s(s-1)^2=1.\tag{2}
\]
The real function \(s(s-1)^2\) has stationary points at \(s=1/3\) and \(s=1\), with values \(4/27\) and \(0\). Equation (2) has one positive root for \(K<27/4\), two distinct positive roots at equality, and three for \(K>27/4\). These give different orbits.

It remains to classify cycles with \(u,v,w\) pairwise distinct. Define \(S=u+v+w\), \(q=uv+uw+vw\), \(r=uvw\), \(Q=S^2-2q\), and residuals \(R_u=u-K[g(v)-g(w)]^2\), with \(R_v,R_w\) obtained cyclically. The factorization
\[
R_u-R_v=(u-v)\bigl[1+K(u+v-1)\{g(u)+g(v)-2g(w)\}\bigr]
\]
and its cyclic partners, together with \(R_u=R_v=R_w=0\), imply that each \(t\in\{u,v,w\}\) is a root of
\[
H(t)=(S-1-t)(Q-S-3t^2+3t)+K^{-1}.
\]
As \(H\) has leading coefficient \(3\), and the three roots are distinct, \(H(t)=3(t-u)(t-v)(t-w)\). Comparing coefficients of \(t\) and the constants gives
\[
q=-S^2+4S-3,\qquad r=-(S-1)^2(S-2)-\frac{1}{3K}.\tag{3}
\]
For completeness, the elementary symmetric identity
\[
\sum_{\rm cyc}[g(v)-g(w)]^2
=2S^4-4S^3-8S^2q+2S^2+14Sq+12Sr+2q^2-6q-18r
\]
turns the sum of (1), after inserting (3), into \(0=5S-6\). Hence \(S=6/5\), \(q=9/25\), and \(r=4/125-1/(3K)\). Thus \(u,v,w\) are precisely the three roots of \(C_K\).

Conversely, suppose \(C_K\) has three distinct real roots \(u,v,w\). Vieta's formulas give \(S=6/5\) and \(q=9/25\). Given any one root \(u\), the other two obey
\[
(v-w)^2=(6/5-u)^2-4\bigl[9/25-u(6/5-u)\bigr]=3u(4/5-u),
\]
while \(g(v)-g(w)=(v-w)(v+w-1)=(v-w)(1/5-u)\). Since \(C_K(u)=0\) states \(3K(4/5-u)(u-1/5)^2=1\), it follows that \(K[g(v)-g(w)]^2=u\). The same argument proves the other equations (1), for **any ordering** of the roots. Six permutations divide into exactly two cyclic-rotation classes, giving two distinct primitive three-cycles, and no others of the distinct-coordinate type.

A direct cubic discriminant calculation gives \(\operatorname{disc} C_K=3(12K-125)/(125K^2)\). For \(K\le125/12\), there cannot be three distinct real roots. For \(K>125/12\), \(C_K\) changes signs successively at \(0,1/5,3/5,4/5\), with signs negative, positive, negative, positive. Therefore its three roots lie in the three claimed disjoint positive intervals. At equality the factorization is \(t(t-3/5)^2\): its repeated-root triple is one of the already counted solutions (2), and no extra primitive cycle appears. Adding the repeated-coordinate count proves the displayed complete census.

## Verification
Run \(\texttt{python CHECK.py}\) with Python 3 and SymPy. The checker verifies exactly, by rational symbolic identities, the residual factorization, the coefficient and symmetric-sum reductions, the cubic discriminant and threshold factorization, the converse identity, and the repeated-coordinate stationary-point thresholds. Four parameter examples with both orientations provide additional non-probative numerical consistency checks. All tests passed on the packaged source. The proof above, not finite root sampling, establishes the all-parameter statement.

## Relationship to prior work
Castañeda and Rebollo-Perdomo [1, Theorem 1.1 and §3] prove existence of a primitive three-cycle in the general nilpotent-Jacobian setting, construct repeated-coordinate cycles through a scalar equation, and calculate a multiplier for such a cycle. Their concluding §5 expressly raises the possibility of uniqueness. Chamberland [2, Theorem 3.1] proves existence through a similar repeated-coordinate construction in an earlier special family. Neither theorem implies that this particular fixed quadratic family develops exactly two additional oppositely ordered cycles at \(K=125/12\). General geometric constraints on distinct-coordinate three-cycles and known repeated-coordinate scalar analyses do not by themselves specify the sharp fixed-parameter cubic, its discriminant, or the complete census. The genuinely additional part here is the necessity-and-sufficiency classification of **all** distinct-coordinate cycles for fixed \(\kappa\), including their sharp onset.

## Limitations
Only primitive real period-three cycles are classified. No nonlinear stability, basin measure, higher-period orbit count, or global bifurcation claim is made. The parameter threshold is exact for this particular quadratic defining polynomial, not for arbitrary polynomials in the originating family. Priority remains subject to equivalent derivations in unindexed literature and subsequent journal versions. No independent audit has been performed.

## References
[1] Á. Castañeda and S. Rebollo-Perdomo, *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields*, arXiv:2209.06986v1, first posted 2022-09-15. https://arxiv.org/abs/2209.06986 ; see §3, equation (10), and §5.

[2] M. Chamberland, *Dynamics of Maps with Nilpotent Jacobians*, author preprint dated 2005-05-17; *Journal of Difference Equations and Applications* **12** (2006), 49–56. https://chamberland.math.grinnell.edu/papers/nilpotent.pdf ; see Theorem 3.1 and §4.
