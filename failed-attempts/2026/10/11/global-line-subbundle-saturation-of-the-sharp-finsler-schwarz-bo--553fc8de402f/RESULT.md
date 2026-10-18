# Global line-subbundle saturation of the sharp Finsler Schwarz bound

## Finding

Fix
\[
n\ge2,\qquad t\ge0,\qquad k\ge2,
\]
with \(k\) an integer. On the unit polydisk
\[
P_n=\{z\in\mathbb C^n:|z_i|<1\},
\]
consider
\[
F_{t,k}^2(z;v)
=
\frac1{1+t}
\left[
\sum_{i=1}^n\frac{|v_i|^2}{(1-|z_i|^2)^2}
+
t\left(
\sum_{i=1}^n\frac{|v_i|^{2k}}{(1-|z_i|^2)^{2k}}
\right)^{1/k}
\right].
\]
The recent source gives the sharp Lu constant
\[
K_{n,t,k}
=
\sqrt{\frac{n+t\,n^{1/k}}{1+t}}
\]
and exhibits the nonautomorphic map
\[
f_0(z_1,\ldots,z_n)=(z_1,\ldots,z_1)
\]
as an equality example at the origin in the direction \(e_1\).

For this same map, the complete equality locus is
\[
F_{t,k}\!\left(f_0(z);df_{0,z}v\right)
=
K_{n,t,k}F_{t,k}(z;v)
\]
if and only if
\[
v\in\mathbb C e_1\setminus\{0\}.
\]

Thus sharp-constant equality is not confined to the single tangent vector displayed in the source. It persists at every base point of \(P_n\) along the constant holomorphic tangent line subbundle
\[
P_n\times\mathbb C e_1.
\]

## Assumptions and scope

The metric \(F_{t,k}\), its curvature extrema, and the sharp Lu constant are exactly those in Example 1 of arXiv:2609.34435v1.

The parameters satisfy
\[
n\ge2,\qquad t\in[0,\infty),\qquad k\in\mathbb N,\quad k\ge2.
\]

The conclusion classifies equality for the particular extremal self-map
\[
f_0(z_1,\ldots,z_n)=(z_1,\ldots,z_1).
\]
It does not classify equality loci for arbitrary holomorphic self-maps of \(P_n\).

The equality here is equality in the sharp Lu estimate with factor
\[
K_{n,t,k}.
\]
It is distinct from the source's unit-factor rigidity condition
\[
F(f(z_0);df\,v)=F(z_0;v)
\]
for every tangent direction at one point.

## Proof

For
\[
(z,v)\in T^{1,0}P_n
\]
define
\[
a_i
=
\frac{|v_i|}{1-|z_i|^2}.
\]
Then
\[
F_{t,k}^2(z;v)
=
\frac{
\sum_{i=1}^n a_i^2
+
t\left(\sum_{i=1}^n a_i^{2k}\right)^{1/k}
}{1+t}.
\]

The map \(f_0\) satisfies
\[
f_0(z)=(z_1,\ldots,z_1)
\]
and
\[
df_{0,z}v=(v_1,\ldots,v_1).
\]
Every coordinate of the image therefore has the same base denominator
\[
1-|z_1|^2
\]
and the same tangent modulus
\[
|v_1|.
\]
Consequently,
\[
\begin{aligned}
F_{t,k}^2\!\left(f_0(z);df_{0,z}v\right)
&=
\frac{
n a_1^2+t(n a_1^{2k})^{1/k}
}{1+t}
\\
&=
\frac{n+t\,n^{1/k}}{1+t}\,a_1^2
\\
&=
K_{n,t,k}^2a_1^2.
\end{aligned}
\]

The sharp Schwarz inequality for this map is therefore an equality exactly when
\[
a_1^2
=
F_{t,k}^2(z;v)
=
\frac{
\sum_i a_i^2
+
t\left(\sum_i a_i^{2k}\right)^{1/k}
}{1+t}.
\]

Now
\[
\sum_i a_i^2\ge a_1^2
\]
and
\[
\left(\sum_i a_i^{2k}\right)^{1/k}\ge a_1^2.
\]

If
\[
t=0,
\]
equality is equivalent to
\[
\sum_i a_i^2=a_1^2,
\]
which holds exactly when
\[
a_i=0
\qquad(i\ge2).
\]

If
\[
t>0,
\]
the right side is a positive weighted average of two quantities, each at least \(a_1^2\). It equals \(a_1^2\) exactly when both quantities equal \(a_1^2\), again equivalent to
\[
a_i=0
\qquad(i\ge2).
\]

Because every denominator
\[
1-|z_i|^2
\]
is strictly positive, this condition is exactly
\[
v_2=\cdots=v_n=0.
\]
Thus the nonzero equality directions are precisely
\[
\mathbb C e_1\setminus\{0\}
\]
at every \(z\in P_n\).

Finally, \(f_0(P_n)\) lies in the diagonal analytic disk
\[
\{(w,\ldots,w):w\in\mathbb D\},
\]
so \(f_0\) is not surjective for \(n\ge2\) and hence is not an automorphism.

## Verification

The primary preprint was inspected at Theorem 1.8, Theorem 4.1, Theorem 4.4, and the full polydisk equality example in Section 5. Its PDF gives the exact formula for \(F_{t,k}\), the curvature quotient
\[
\frac{K_1}{K_2}
=
\frac{n+t\,n^{1/k}}{1+t},
\]
and the map
\[
f_0(z)=(z_1,\ldots,z_1).
\]
The source checks equality at
\[
z_0=0,\qquad v_0=e_1.
\]

The earlier unit-polydisk Schwarz paper was inspected in full at its sharp Schwarz theorem, its formula for \(F_{t,k}\), and its Example 4.7. It gives the same sharp constant but does not identify the map \(f_0\) or a global equality locus.

The present equality classification is an exact substitution into the metric formula. No numerical experiment or asymptotic argument is used.

## Relationship to prior work

Lin and Zhong established the invariant Kähler--Berwald Schwarz inequality on unit polydisks and computed the sharp constant for the family \(F_{t,k}\). Their 2023 paper records the sharp constant but does not provide the global equality set considered here.

He and Zhong's 2026 paper makes optimality explicit for arbitrary bounded symmetric domains and, for the polydisk family, exhibits
\[
f_0(z)=(z_1,\ldots,z_1)
\]
with equality at the single tangent pair
\[
(0,e_1).
\]
The source uses this to show that equality at one tangent pair in the sharp Lu estimate does not imply automorphy.

The present calculation determines the entire equality locus of that extremal map and shows a stronger persistence phenomenon: the same nonautomorphism attains the sharp factor at every point along a holomorphic tangent line subbundle.

Targeted searches under the source identifier, polydisk Lu equality, the explicit map \(f_0\), and line-field saturation did not locate an implication-equivalent statement.

## Limitations

The result classifies equality only for the specific rank-one map \(f_0\); other extremal self-maps may have different equality sets.

It does not classify all self-maps attaining the Lu constant.

The finding concerns the sharp factor
\[
K_{n,t,k}
=
\sqrt{\frac{n+t\,n^{1/k}}{1+t}},
\]
which is greater than one for \(n\ge2\). It therefore does not weaken or contradict the source's separate rigidity statement formulated with unit factor in every tangent direction.

## References

1. Y. He and C. Zhong, *Schwarz lemma on bounded symmetric domains endowed with holomorphic invariant Kähler--Berwald metrics*, arXiv:2609.34435v1, 2026.
2. S. Lin and C. Zhong, *Characterization of Holomorphic Invariant Strongly Pseudoconvex Complex Finsler Metrics on Unit Polydisks*, Journal of Geometric Analysis 33 (2023), Article 343, DOI: 10.1007/s12220-023-01397-5.
3. C. Zhong, *De Rham decomposition theorem for strongly convex Kähler--Berwald manifolds*, Results in Mathematics 78 (2023), Article 47, DOI: 10.1007/s00025-022-01797-z.
