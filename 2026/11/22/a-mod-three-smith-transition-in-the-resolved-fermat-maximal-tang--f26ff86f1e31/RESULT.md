# A mod-three Smith transition in the resolved Fermat maximal-tangent boundary

## Finding
For every integer \(d\ge3\), let \(F_d\subset\mathbb P^2_{\mathbb C}\) be the smooth Fermat curve \(X^d+Y^d+Z^d=0\). Let \(B_d\) be its reduced divisor of all \(3d\) maximal-contact tangent lines, namely
\[
B_d:\ (X^d+Y^d)(Y^d+Z^d)(Z^d+X^d)=0.
\]
Blow up the three coordinate vertices and let \(D_d\) be the union of the \(3d\) strict transforms and the three reduced exceptional curves. Then \(D_d\) is a stable nodal curve with \(3d+3\) rational components, \(3d^2+3d\) nodes, and arithmetic genus \(3d^2-2\).

Write \(m=2d+1\) and \(C_r=\mathbb Z/r\mathbb Z\). The critical group of its dual graph \(\Gamma_d\) has the **complete integral invariant-factor decomposition**
\[
K(\Gamma_d)\cong
\begin{cases}
C_m^{\,3d-5}\oplus C_{d^2m}\oplus C_{3d^2m},&3\nmid m,\\
C_3\oplus C_m^{\,3d-5}\oplus C_{d^2m}^{\,2},&3\mid m.
\end{cases}
\]
In particular, \(3\mid m\) exactly when \(d\equiv1\pmod3\): this changes the number of nontrivial invariant factors, while preserving the universal spanning-tree order
\[
|K(\Gamma_d)|=3d^4(2d+1)^{3d-3}.
\]
For example, \(d=4\) gives \(C_3\oplus C_9^7\oplus C_{144}^2\), whereas \(d=5\) gives \(C_{11}^{10}\oplus C_{275}\oplus C_{825}\).

For any proper regular split semistable curve model whose reduced special fiber is \(D_d\), with every node of thickness one, the geometric component group of the Néron model of the generic Jacobian has the same abstract finite group. This is a conditional interpretation, not an assertion that any particular preassigned family realizes the fiber.

## Assumptions and scope
All geometry is over \(\mathbb C\); the integral graph statement is independent of any arithmetic form. An ordinary graph edge records each transverse node of \(D_d\), not intersections before resolving the coordinate vertices. An attached exceptional vertex has degree \(d\); each strict line vertex has degree \(2d+1\). The critical group is the finite cokernel of any reduced integral Laplacian of the connected graph (one vertex deleted). Exponents in the displayed direct sums are multiplicities, and \(C_1\) factors are omitted.

## Proof
**1. Geometric incidence.** The Hessian determinant of \(X^d+Y^d+Z^d\) is a nonzero scalar multiple of \((XYZ)^{d-2}\). Hence all flexes lie on the three coordinate axes, where there are exactly \(d\) distinct points per axis. The tangent at a point with \(Z=0\) and \(X^d+Y^d=0\) has intersection multiplicity \(d\), so is one linear factor of \(X^d+Y^d\); similarly for the other two axes. These are all the maximal-contact tangents. Each of the three sets of \(d\) lines forms a pencil centered at one coordinate vertex.

A triple intersection of lines taken from the three different pencils would yield nonzero \(\alpha,\beta,\gamma\) with \(\alpha^d=\beta^d=\gamma^d=-1\) and \(\alpha\beta\gamma=1\), contradicting \((\alpha\beta\gamma)^d=-1\). Consequently there are exactly \(3d^2\) distinct ordinary double intersections across different pencils, and the only other singularities are three ordinary \(d\)-fold vertices. Blowing up these vertices separates each pencil and creates \(d\) transverse strict-line/exceptional intersections. The dual graph is the complete tripartite graph on three sets of \(d\) line vertices, augmented by three *separate* hub vertices, one connected to every line in its own set and to no others. Therefore its vertex and edge counts are \(3d+3\) and \(3d^2+3d\). It is connected, and its first Betti number, hence the arithmetic genus of the all-rational-component nodal curve, is \(E-V+1=3d^2-2\). Every component has at least three special points for \(d\ge3\), so the curve is stable.

**2. Integral Laplacian reduction.** Label line vertices \(x_{a,i}\) with \(a\in\{1,2,3\}\) and \(1\le i\le d\), and hubs \(e_a\). Delete the row and column of \(e_3\) in the Laplacian. Thus, in its additive cokernel, the line relation is
\[
m x_{a,i}-\sum_{b\ne a}\sum_{j=1}^d x_{b,j}-e_a=0,
\]
where \(e_3=0\), and the remaining hub relations are \(d e_a-\sum_jx_{a,j}=0\) for \(a=1,2\). Put \(y_a=x_{a,d}\), \(u_{a,i}=x_{a,i}-y_a\) for \(1\le i<d\), \(t_a=\sum_{i<d}u_{a,i}\), and \(f_a=e_a-y_a\) for \(a=1,2\). Subtracting each group's base-line relation from its remaining line relations gives \(m u_{a,i}=0\). Since the row vector of coefficients defining \(t_a\) is primitive, it is part of a unimodular basis of the \(d-1\) variables \(u_{a,i}\). The \(3(d-2)\) complementary difference generators split off as independent \(C_m\) factors.

The remaining relations, after eliminating \(f_1,f_2\) using unit coefficients in the first two base-line equations, are
\[
\begin{aligned}
m t_a&=0\quad(a=1,2,3),\\
-t_1-dt_2-dt_3+d^2(2y_1-y_2-y_3)&=0,\\
-dt_1-t_2-dt_3+d^2(-y_1+2y_2-y_3)&=0,\\
-t_1-t_2-dy_1-dy_2+my_3&=0.
\end{aligned}
\]
Set \(r_1=y_1-y_3\), \(r_2=y_2-y_3\). In the last equation the coefficient of \(y_3\) is \(m-2d=1\), so eliminating \(y_3\) is another integral unimodular operation. The residual five-generator presentation, with generators ordered \((t_1,t_2,t_3,r_1,r_2)\), is the exact square matrix
\[
M_d=\begin{pmatrix}
m&0&0&0&0\\0&m&0&0&0\\0&0&m&0&0\\
-1&-d&-d&2d^2&-d^2\\
-d&-1&-d&-d^2&2d^2
\end{pmatrix}.
\]
Thus \(K(\Gamma_d)\cong C_m^{3(d-2)}\oplus\operatorname{coker}(M_d)\) **integrally**, not merely after tensoring with \(\mathbb Q\). Its residual determinant is \(3d^4m^3\), so the full group order is \(3d^4m^{3d-3}\).

**3. All prime-local invariant factors.** We have \(\gcd(d,m)=1\). For a prime \(p\mid d\), the first three diagonal relations of \(M_d\) are units over \(\mathbb Z_p\), so they eliminate the \(t_a\). The residual \(2\)-by-\(2\) block is \(d^2\begin{psmallmatrix}2&-1\\-1&2\end{psmallmatrix}\), whose integral Smith form is \(\operatorname{diag}(d^2,3d^2)\). This gives the complete \(p\)-primary part for such primes.

For a prime \(p\mid m\), \(d\) is a \(p\)-adic unit. If \(p\ne3\), the last two columns of the last two rows form an invertible block of determinant \(3d^4\). Eliminating \(r_1,r_2\) leaves three independent cyclic factors of order \(p^{v_p(m)}\). If \(p=3\), then \(d\equiv1\pmod3\); subtracting the final two relations gives
\[
3d^2(r_1-r_2)+(d-1)(t_1-t_2)=0.
\]
The other linear combination of these relations eliminates one of the \(r_a\) with a \(3\)-adic unit coefficient. Since \(3\mid(d-1)\), replacing the remaining difference generator by \(d^2(r_1-r_2)+(d-1)(t_1-t_2)/3\) is a \(\mathbb Z_3\)-unimodular change. The residual relation becomes exactly three times that new generator, independently of the three \(m\)-torsion generators. Hence the \(3\)-primary residual group is \(C_{3^{v_3(m)}}^3\oplus C_3\).

Finally, if \(p\nmid dm\), the first three relations eliminate \(t_a\), and the remaining determinant is a \(p\)-adic unit unless \(p=3\). At \(p=3\) with \(3\nmid m\), the same elimination leaves \(d^2\begin{psmallmatrix}2&-1\\-1&2\end{psmallmatrix}\), including the possibility \(3\mid d\) already covered above. Combining the prime-primary factors yields, when \(3\nmid m\), \(\operatorname{coker}(M_d)\cong C_m\oplus C_{d^2m}\oplus C_{3d^2m}\); when \(3\mid m\), it gives \(\operatorname{coker}(M_d)\cong C_3\oplus C_m\oplus C_{d^2m}^2\). Adding the previously split \(C_m^{3(d-2)}\) establishes both displayed formulas. The factors are ordered by divisibility, so they are complete invariant factors.

## Verification
The bundled independent-arithmetic script `verify.py` reconstructs the graph from its edges, computes the rooted integral Laplacian, computes its Smith factors, computes \(M_d\), and compares both against the theorem for \(d\in\{3,4,5,6,7,8,9,10,11,12\}\). The direct integral-relation proof above covers **all integers \(d\ge3\)**; the finite tests provide error detection only and are not used to infer the infinite theorem. Run `python verify.py` after installing the dependency in `requirements.txt`. The matrix \(M_d\) is given explicitly so that all computations can be reproduced without geometrical black boxes.

## Relationship to prior work
Oka's study of Fermat flexes and dual curves, Pambianco's characterization of Fermat-curve symmetry, and Dimca–Ilardi–Pokora–Sticlaru's Theorem 1.7 all provide classical or modern geometric foundations for this tangent arrangement. Merta–Zieliński's Lemma 2.1 explicitly confirms the \(d=4\) line-intersection census. None of those inspected source passages computes a reduced-Laplacian Smith form for the blowup boundary. Jacobson–Niedermaier–Reiner classify critical groups of **complete multipartite graphs**, which cover the graph obtained by discarding the three exceptional hubs; this is a genuinely different graph, since the hubs contribute new edges and nontrivial \(d^2\) and residue-three invariant factors. The present proof gives a direct integral presentation for the full resolved graph rather than asserting novelty from unmatched wording. Earlier unindexed calculations or general graph extensions remain a possible priority risk.

## Limitations
This is a complex-geometric statement, not a uniform characteristic-\(p\) theorem. The Néron interpretation assumes a regular split semistable family with unit node thicknesses; arbitrary thicknesses change the component-group presentation. The theorem does not compute the Picard group of the blown-up surface, the Jacobian of the smooth Fermat curve, or the full arithmetic Galois action on the stable boundary. The exact provenance of an older historical formula, if any, has not been independently settled.

## References
1. M. Oka, *On Fermat curves and maximal nodal curves*, Michigan Math. J. **53** (2005), 459–477, DOI: 10.1307/MMJ/1123090779.
2. F. Pambianco, *The Fermat curve \(x^n+y^n+z^n\): the most symmetric non-singular algebraic plane curve*, arXiv:1004.2603, first version 2010-04-15, https://arxiv.org/abs/1004.2603.
3. A. Dimca, G. Ilardi, P. Pokora and G. Sticlaru, *Construction of Free Curves by Adding Lines to a Given Curve*, Results Math. **79** (2024), online 2023-11-09, https://doi.org/10.1007/s00025-023-02036-9, especially Theorem 1.7.
4. Ł. Merta and M. Zieliński, *On quartics with the maximal number of maximal tangency lines*, Period. Math. Hung. **91** (2025), 309–319, https://doi.org/10.1007/s10998-025-00648-y, especially Lemma 2.1.
5. B. Jacobson, A. Niedermaier and V. Reiner, *Critical groups for complete multipartite graphs and Cartesian products of complete graphs*, J. Graph Theory **44** (2003), 231–250, https://doi.org/10.1002/jgt.10139.
6. D. J. Lorenzini, *A finite group attached to the Laplacian of a graph*, Discrete Math. **91** (1991), 277–282, on integral graph component groups.
7. A. Amini, M. Baker, E. Brugallé and J. Rabinoff, *Lifting harmonic morphisms I: metrized complexes and Berkovich skeleta*, Theorem 8.2 (Raynaud) for the semistable Jacobian component group, https://www.math.ens.psl.eu/~amini/Publications/hmmcI.pdf.
