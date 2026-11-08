# Smooth space-filling cubic-surface pencils over \(\mathbb F_2\): a 56-pencil classification and doubled base transversals

## Finding
Let \(W\) denote the six-dimensional space of homogeneous cubic equations on \(\mathbb P^3_{\mathbb F_2}\) vanishing at all fifteen rational points. A *smooth filling pencil* is a two-dimensional \(\mathbb F_2\)-subspace \(U\subset W\) whose three nonzero equations each define a geometrically smooth cubic surface.

**Theorem.** There are exactly \(56\) smooth filling pencils, forming one orbit under \(\operatorname{PGL}_4(\mathbb F_2)\), with stabilizer of order \(360\). There are \(28\) individual smooth filling cubic equations. The five common rational lines of any pencil partition the fifteen rational points into a line spread, and the map from pencils to spreads is a bijection. No three-dimensional subspace of \(W\) has all its nonzero members smooth.

More precisely, if \(B=V(F,G)\) is the base complete intersection of any such pencil, its reduced geometric support is precisely seven projective lines: the five mutually disjoint \(\mathbb F_2\)-lines of the associated spread and two mutually disjoint \(\mathbb F_4\)-conjugate geometric transversals that each meet all five spread lines. The scheme-theoretic fundamental cycle is
\[
[B]=[L_1]+[L_2]+[L_3]+[L_4]+[L_5]+2[T_\alpha]+2[T_{\alpha^2}],
\]
where \(\alpha^2+\alpha+1=0\). In particular, the base is nonreduced at the generic point of each conjugate transversal even though every rational member of the pencil is smooth. Its reduced support has ten ordinary intersections, incidence graph \(K_{5,2}\), and arithmetic genus \(4\); the complete intersection itself has arithmetic genus \(10\).

The existence and relevance of conjugate skew lines and five transversal lines in cubic-surface constructions is classical, as is the Klein-correspondence relation between line spreads and external lines. The claimed contribution is the complete classification of *all* all-smooth filling pencils, their unique projective orbit and sharp maximality, together with the exact scheme-theoretic base cycle in this extremal family; the older geometric construction and abstract spread correspondence are not claimed as new.

## Assumptions and scope
The ground field is \(k=\mathbb F_2\), and geometric smoothness and reducedness mean after base change to an algebraic closure. An equation is counted up to a nonzero scalar; over \(k\) this does not change its coefficients. All pencils are two-dimensional vector subspaces, not a choice of ordered generators. For \(0\le i<j\le3\), define \(H_{ij}=x_i^2x_j+x_ix_j^2\) and
\[
F_A=\sum_{i<j} a_{ij}H_{ij},\qquad A=(a_{ij})_{0\le i,j\le3},\quad a_{ji}=a_{ij},\quad a_{ii}=0.
\]
All matrix entries are in \(k\). The Pfaffian is
\[
q(A)=a_{01}a_{23}+a_{02}a_{13}+a_{03}a_{12}.
\]
The ordering of six coefficients in both checkers is \((01,02,03,12,13,23)\). One representative pencil is
\[
F=H_{01}+H_{23},\qquad G=H_{01}+H_{03}+H_{12}.
\]

## Proof
**(1) Identification and smoothness.** The vanishing ideal of \(\mathbb P^3(\mathbb F_2)\) is generated in its smallest nonzero degree by the six \(H_{ij}\); equivalently, evaluating a general degree-three form at the fifteen binary projective points gives a fourteen-dimensional image from the twenty-dimensional cubic space with a six-dimensional kernel. More concretely, reducing all monomials against the relations \(x_i^2x_j=x_ix_j^2\), and evaluating the remaining squarefree and pure-cube terms at binary points, proves independence and spanning. Hence \(W\) is the alternating-matrix space. Differentiation gives
\[
\nabla F_A=A(x_0^2,x_1^2,x_2^2,x_3^2)^\mathsf T.
\]
Frobenius squaring is bijective on algebraically closed fields of characteristic two, so this gradient is nowhere zero in projective space precisely when \(A\) is nonsingular. For an alternating \(4\times4\) matrix, \(\det A=q(A)^2\). Thus smoothness is equivalent to \(q(A)=1\).

**(2) Exact census and maximal dimension.** The six-bit enumeration `verify_pencils.py` iterates over all \(63\) nonzero alternating matrices and finds \(28\) with \(q=1\). It forms all unordered triples \(\{A,B,A+B\}\) with three nondegenerate members and obtains exactly \(56\) distinct pencils. The program applies all elementary coordinate transvections (generating the group of order \(20160\)) to the representative \(\{33,13,44\}\), obtains all \(56\), and hence gives stabilizer \(20160/56=360\). An alternating Pfaffian restricted to any three-dimensional vector subspace of \(W\) is a homogeneous quadratic in three variables. By the Chevalley--Warning theorem (or the separate exhaustive eight-point check in the script), it has a nonzero root over \(\mathbb F_2\), so no such three-dimensional subspace is all-smooth.

**(3) Rational spread.** A rational projective line is represented by \(\{u,v,u+v\}\) for two independent nonzero binary four-vectors. Its containment in \(V(F_A)\) is equivalent to \(u^\mathsf T A v=0\), as follows by substituting \(su+tv\). Enumeration of all \(35\) rational lines shows that for each smooth pencil exactly five lines satisfy both alternating equations; they are skew and cover all fifteen nonzero binary four-vectors. The resulting \(56\) spreads are all distinct. This gives the bijection without assuming it from the classical correspondence.

**(4) The geometric base cycle.** By the orbit computation it suffices to treat the representative \(F=H_{01}+H_{23}\) and \(G=H_{01}+H_{03}+H_{12}\). Its five binary spread lines are spanned respectively by bit-pairs
\[
(1,4),\quad(2,8),\quad(3,12),\quad(6,11),\quad(7,9),
\]
where a bit-mask represents a coordinate vector with bit zero corresponding to \(x_0\). Set \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). The two additional lines are
\[
T_t=\{[u:v:tu:tv]:[u:v]\in\mathbb P^1\},\qquad t\in\{\alpha,\alpha^2\}.
\]
Substitute \((x_0,x_1,x_2,x_3)=(u,v,tu,tv)\). Both cubics vanish identically since \(t^3=1\) and \(1+t+t^2=0\). These lines are skew to each other; each has exactly one point in common with each of the five binary spread lines; and the resulting ten crossings are distinct. Direct evaluation gives the gradient dependence \(\nabla F=t^2\nabla G\) along \(T_t\). Thus the generic multiplicity of the local complete intersection along each \(T_t\) is at least two: otherwise its generic reduced smooth line would have Jacobian rank two. In contrast, at every binary rational point the two gradients are independent (neither is zero, and equality would contradict invertibility of \(A+B\)), so each binary line has generic multiplicity one.

The two cubics are distinct smooth irreducible surfaces; their intersection is a pure one-dimensional Cohen--Macaulay complete intersection of degree \(3\cdot3=9\), with no embedded associated points. The five binary lines contribute degree five, and the two doubled transversals contribute at least four more. Bézout degree therefore forces equality: there is no other geometric component and the multiplicities along the seven listed lines are exactly \(1,1,1,1,1,2,2\). This also justifies the complete reduced support over the algebraic closure without extrapolating merely from the \(\mathbb F_4\) search. The reduced support is a nodal union with seven rational-line components over the algebraic closure and ten transverse crossings, so \(p_a(B_{\mathrm{red}})=10-7+1=4\). The adjunction formula for a \((3,3)\) complete-intersection curve in projective three-space gives \(p_a(B)=1+9(3+3-4)/2=10\).

## Verification
Run from the directory containing the scripts:

```sh
python3 verify_pencils.py
python3 verify_base_cycle.py
```

Expected terminal checks are `FROBENIUS_CUBIC_PENCILS_PASS 28 56 56 56 360 35` and `FROBENIUS_CUBIC_BASE_PASS 5 2 7 85 357 9 4 10`. The first is a complete binary enumeration of pencils and rational spreads. The second independently uses exact arithmetic in \(\mathbb F_4\), enumerates all \(357\) rational lines over that extension, checks seven common lines and the gradient dependence, and checks the degree budget. The proof of no additional geometric components uses complete-intersection degree, not the limited extension-field enumeration. The scripts use only the Python standard library.

## Relationship to prior work
Asgarli--Ghioca (2022), first publicly available 2022-03-14, study finite-field pencils all of whose ground-field members are smooth; their even-characteristic surface constructions concern quadrics, not the exact classification here. Asgarli--Duan--Lai (2022), Proposition 4.5, describe smooth Frobenius-nonclassical hypersurfaces of degree \(q+1\) by nondegenerate alternating forms; this is close background for the individual cubic equations and is not claimed anew. Havlicek--Riesinger (2017) explain the classical bijection between Klein-quadric external lines and regular spreads; the abstract external-line/spread correspondence is not new. Swinnerton--Dyer (2010) explicitly constructs cubic surfaces using five rational transversals to two conjugate skew lines; the seven-line incidence pattern is therefore not claimed new either. The inspected sources do not state the complete \(56\)-pencil all-smooth classification with its stabilizer and maximality, nor the exact multiplicity-two base-cycle assertion for every such pencil. The seven-line support is nevertheless very close to the older construction, and priority of the combined statement requires expert historical review.

## Limitations
The result concerns only \(\mathbb F_2\)-rational members of the pencil; over the algebraic closure, the pencil can contain singular members. It does not classify arbitrary cubic-surface pencils or spread-like structures over larger fields. The symbolic local algebra of the nonreduced ribbon structure beyond the fundamental cycle is not classified. The association with known seven-line configurations and known external-line spread theory creates a substantive residual risk that the present finite classification is implicit in earlier literature. Independent mathematical and historical-priority audits have not been performed.

## References
1. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first posted 2022-03-14, https://arxiv.org/abs/2203.07169.
2. S. Asgarli, L. Duan, K.-W. Lai, *Frobenius nonclassical hypersurfaces*, arXiv:2207.11981, first posted 2022-07-25, https://arxiv.org/abs/2207.11981.
3. H. Havlicek and R. Riesinger, *Pencilled regular parallelisms*, arXiv:1705.07276, first posted 2017-05-20, https://arxiv.org/abs/1705.07276.
4. H. P. F. Swinnerton--Dyer, *Cubic surfaces over finite fields*, Math. Proc. Camb. Phil. Soc. 149 (2010), 385--388; first online 2010-07-07, DOI 10.1017/S0305004110000320.
