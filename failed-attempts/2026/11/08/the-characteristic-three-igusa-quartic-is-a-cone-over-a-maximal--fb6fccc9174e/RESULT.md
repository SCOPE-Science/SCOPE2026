# The characteristic-three Igusa quartic is a cone over a maximal fifteen-nodal K3 model

## Finding
Let \(k=\overline{\mathbb F}_3\), let \(H\subset k^6\) be the five-dimensional subspace defined by \(\sum_{i=1}^6x_i=0\), and let \(X\subset\mathbb P(H)\) be the characteristic-three Igusa quartic, given by
\[
F(x)=\left(\sum_{i=1}^6x_i^2\right)^2-4\sum_{i=1}^6x_i^4=0.
\]
Then \(X\) is the projective cone with vertex \(v=[1:1:1:1:1:1]\) over a geometrically irreducible quartic surface \(B\subset\mathbb P^3\). The surface \(B\) has exactly fifteen singular points, all \(\mathbb F_3\)-rational ordinary double points, in bijection with the fifteen partitions of six labels into three unordered pairs. The singular locus of \(X\) is exactly the union of the fifteen lines joining the vertex to these nodes.

Let \(Y\to B\) be the minimal resolution. It is a smooth K3 surface over \(\mathbb F_3\); every exceptional curve is a split conic (hence isomorphic to \(\mathbb P^1\) over \(\mathbb F_3\)). The characteristic polynomial of geometric Frobenius on \(H^2_{\mathrm{\acute et}}(Y_{\overline{\mathbb F}_3},\mathbb Q_\ell)\), for \(\ell\ne3\), is
\[
(T-3)^{21}(T+3).
\]
In particular, over \(\mathbb F_9\) the surface \(Y\) meets the upper Weil bound for K3 surfaces. For each integer \(n\ge1\), writing \(q=3^n\), the exact point counts are
\[
\begin{aligned}
\#Y(\mathbb F_q)&=1+q^2+q\bigl(21+(-1)^n\bigr),\\
\#B(\mathbb F_q)&=1+q^2+q\bigl(6+(-1)^n\bigr),\\
\#X(\mathbb F_q)&=1+q+q^3+q^2\bigl(6+(-1)^n\bigr).
\end{aligned}
\]
Their Hasse–Weil zeta functions are respectively
\[
\begin{aligned}
Z(Y,T)&=\frac{1}{(1-T)(1-9T)(1-3T)^{21}(1+3T)},\\
Z(B,T)&=\frac{1}{(1-T)(1-9T)(1-3T)^6(1+3T)},\\
Z(X,T)&=\frac{1}{(1-T)(1-3T)(1-27T)(1-9T)^6(1+9T)}.
\end{aligned}
\]

## Assumptions and scope
Everything is considered in characteristic three. The singularity, irreducibility, and normalization claims hold after extension to the algebraic closure. Point counts and Frobenius actions refer to the explicitly defined models over \(\mathbb F_3\). A concrete base surface \(B\) is obtained by choosing the slice \(x_6=0\), with \(x_5=-x_1-x_2-x_3-x_4\). In this slice its homogeneous quartic equation is \(G=\left(\sum_{i=1}^5 x_i^2\right)^2-\sum_{i=1}^5x_i^4\). The fifteen ordinary double points are distinguished by partitions into three equal two-element classes corresponding to the values \(0,1,-1\) of the six coordinates, modulo simultaneous translation and nonzero scaling.

## Proof
**Cone structure.** Put \(\mathbf1=(1,1,1,1,1,1)\). In characteristic three, \(\mathbf1\in H\). For every scalar \(a\) and \(x\in H\), one has \(\sum (x_i+a)^2=\sum x_i^2\), because \(2a\sum x_i+6a^2=0\); also \(\sum(x_i+a)^4=\sum x_i^4\), since the only possibly nonzero mixed terms are multiples of \(\sum x_i^3=(\sum x_i)^3=0\) and \(\sum x_i=0\), while \(6a^4=0\). Thus \(F(x+a\mathbf1)=F(x)\). Since \(H=\langle\mathbf1\rangle\oplus\{x\in H:x_6=0\}\), this is a genuine projective cone over \(B\).

**Complete singular set.** Set \(s=\sum x_i^2\). In characteristic three the partial derivatives in the ambient six-space are \(\partial_iF=sx_i-x_i^3\). The gradient of the restriction to \(H\) vanishes exactly when all these six quantities agree. Subtraction of the equations for two indices gives
\[
(x_i-x_j)\bigl(s-(x_i-x_j)^2\bigr)=0.
\]
If \(s=0\), all six coordinates agree (the cone vertex). Otherwise, choose \(r\) with \(r^2=s\); all coordinates take the form \(a+rt_i\) with \(t_i\in\mathbb F_3\). The conditions \(\sum x_i=0\) and \(s=\sum x_i^2\) become \(\sum t_i=0\) and \(\sum t_i^2=1\) in \(\mathbb F_3\). Their only six-element multiset solution is \(\{0,0,1,1,-1,-1\}\). Conversely, these multisets yield singular points and satisfy \(F=0\). Modulo translation and nonzero scaling of the three values, there are precisely \(6!/(2!^3\,3!)=15\) partitions into unordered pairs. Each defines exactly one line through the vertex of \(X\) and one point in the chosen base slice.

**Ordinary nodes.** At a singular representative \(x=a\mathbf1+rt\), the Hessian bilinear form of \(F\) on \(H\) equals, up to the nonzero scalar \(r^2\),
\[
(u,w)\longmapsto\sum_{i=1}^6u_iw_i-\left(\sum_{i=1}^6t_i u_i\right)\left(\sum_{i=1}^6t_i w_i\right).
\]
Its radical is exactly \(\langle\mathbf1,t\rangle\): the inclusion is immediate from \(\sum t_i=0\), \(\sum t_i^2=1\), while the reverse inclusion follows because the orthogonal complement of \(H\) under the ambient dot product is \(\langle\mathbf1\rangle\). Quotienting by the vertex direction and projective scaling leaves a nondegenerate three-dimensional quadratic tangent form at each singular point of \(B\). As the characteristic is not two, these are ordinary quadratic double points. There are no further singular points. A reducible projective quartic surface in \(\mathbb P^3\) would have a positive-dimensional intersection of its components, hence a positive-dimensional singular set; this contradicts the fifteen isolated nodes. Therefore \(B\) is geometrically irreducible. A normal quartic with only rational double points has minimal crepant resolution a K3 surface. The fifteen exceptional curves are smooth conics over \(\mathbb F_3\), and every smooth conic over a finite field has a rational point, hence is a split \(\mathbb P^1\).

**Exact Frobenius spectrum.** Exhaustive evaluation of the explicit four-variable polynomial over the projective spaces \(\mathbb P^3(\mathbb F_3)\) and \(\mathbb P^3(\mathbb F_9)\), by the attached finite-field verifier, gives \(\#B(\mathbb F_3)=25\) and \(\#B(\mathbb F_9)=145\). Replacing the fifteen rational nodes by split exceptional lines gives \(\#Y(\mathbb F_3)=25+15\cdot3=70\) and \(\#Y(\mathbb F_9)=145+15\cdot9=280\). The K3 Betti numbers are \(b_0=b_4=1\), \(b_2=22\), and \(b_1=b_3=0\). Deligne's bounds give absolute value \(3\) for each of the twenty-two complex-conjugate Frobenius eigenvalues \(\alpha_j\) on \(H^2\). The Lefschetz trace formula at the second power gives \(\sum\alpha_j^2=280-1-81=198=22\cdot9\), saturating the triangle inequality. Thus every \(\alpha_j^2=9\); the first-power trace \(70-1-9=60\) then forces twenty-one eigenvalues \(+3\) and one eigenvalue \(-3\). The formulas for every extension and the zeta functions follow. Finally, every \(\mathbb F_q\)-point of the projective cone lies either at its vertex or on one of the \(q\) points above an \(\mathbb F_q\)-point of \(B\), giving \(\#X=1+q\#B\).

## Verification
Run `python3 verify_igusa3.py` using an ordinary Python interpreter. The script uses the explicit model of \(\mathbb F_9=\mathbb F_3[\theta]/(\theta^2+1)\), enumerates every projective point in the base \(\mathbb P^3\) and cone \(\mathbb P^4\) over both fields, checks the fifteen nodes, and verifies Hessian rank three at each node in both characteristics. Its output is reproduced in `verify_output.txt`. The two base point counts are exhaustive finite calculations; the universal formulas are proved by the geometric argument and Frobenius eigenvalue bound, not extrapolation. No external algebra system is required.

## Relationship to prior work
The Igusa quartic and its classical fifteen singular lines are known over characteristic zero, including Kondō's explicit equation and boundary arrangement. Dolgachev studies complex fifteen-nodal quartic surfaces arising as hyperplane sections of the Igusa quartic. Rams and Schütt study smooth supersingular quartic K3 models in characteristic three; Kondō and Shimada study the Fermat quartic K3 surface of Artin invariant one. These results supply context and tools but do not imply the characteristic-three collapse of the Igusa quartic into a cone, the explicit fifteen-node base with its finite-field models, or its complete Frobenius spectrum merely by specialization. The classical fifteen-line property itself is not claimed as a discovery.

## Limitations
Historical priority is provisional: an unindexed treatment of the characteristic-three Igusa quartic or a modular interpretation of this precise special fiber may already imply the result. The argument does not determine the Artin invariant of \(Y\), the automorphism group of the resolution, or a canonical identification with another supersingular quartic K3. The exact counts use exhaustive tests over only \(\mathbb F_3\) and \(\mathbb F_9\); the passage to every extension uses Deligne's theorem and the K3 cohomological trace formula. No independent scientific validation has been performed.

## References
- Shigeyuki Kondō, *Igusa quartic and Borcherds products*, arXiv:1406.2394 (first public 2014-06-10), https://arxiv.org/abs/1406.2394.
- Igor Dolgachev, *15-nodal quartic surfaces I*, arXiv:1906.12295 (2019), https://arxiv.org/abs/1906.12295.
- Sławomir Rams and Matthias Schütt, *112 lines on smooth quartic surfaces (characteristic 3)*, arXiv:1409.7485 (2014), https://arxiv.org/abs/1409.7485.
- Shigeyuki Kondō and Ichiro Shimada, *The automorphism group of a supersingular K3 surface with Artin invariant 1 in characteristic 3*, arXiv:1205.6520 (first public 2012-05-29), https://arxiv.org/abs/1205.6520.
