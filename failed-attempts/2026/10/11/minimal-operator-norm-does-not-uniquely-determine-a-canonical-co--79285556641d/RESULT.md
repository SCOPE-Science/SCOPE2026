# Minimal operator norm does not uniquely determine a canonical controlled \(K\)-\(g\)-dual

## Finding
Proposition 3.7 of Hosseinnezhad asserts that every controlled \(K\)-\(g\)-frame has a unique controlled dual \(K\)-\(g\)-Bessel sequence whose synthesis operator has minimal norm among all controlled duals.

The uniqueness assertion is false even with identity controls and in dimension two.

Let
\[
H=\mathbb C^2,
\qquad
C=C'=I,
\qquad
K=
\begin{pmatrix}
1&0\\
0&1/2
\end{pmatrix}.
\]
Take three scalar coefficient spaces and the frame vectors
\[
f_1=e_1,
\qquad
f_2=\frac1{\sqrt2}e_2,
\qquad
f_3=\frac1{\sqrt2}e_2.
\]
Equivalently,
\[
\Lambda_jx=\langle x,f_j\rangle.
\]
The synthesis operator is
\[
T_\Lambda(c_1,c_2,c_3)
=
\left(c_1,\frac{c_2+c_3}{\sqrt2}\right).
\]
Since
\[
T_\Lambda T_\Lambda^*=I,
\]
the family is an ordinary Parseval frame. In particular,
\[
\|K^*x\|^2\le
\sum_{j=1}^3\|\Lambda_jx\|^2
=
\|x\|^2,
\]
so it is an \(I\)-controlled \(K\)-\(g\)-frame.

For each real \(c\), define
\[
V_c(x_1,x_2)
=
\left(
x_1,
\frac{1/2+c}{\sqrt2}x_2,
\frac{1/2-c}{\sqrt2}x_2
\right).
\]
Then
\[
T_\Lambda V_c
=
\begin{pmatrix}
1&0\\
0&1/2
\end{pmatrix}
=
K.
\]
Thus \(V_c\) is the analysis operator of a controlled dual \(K\)-\(g\)-Bessel sequence.

Direct multiplication gives
\[
V_c^*V_c
=
\begin{pmatrix}
1&0\\
0&1/4+c^2
\end{pmatrix}.
\]
Therefore
\[
\|V_c\|=1
\]
for every
\[
|c|\le\frac{\sqrt3}{2}.
\]
All of these duals have globally minimal operator norm, because any solution \(V\) of
\[
T_\Lambda V=K
\]
satisfies
\[
1=\|K\|
\le
\|T_\Lambda\|\,\|V\|
=
\|V\|.
\]
Hence there is a continuum of distinct minimum-norm duals.

The unique object supplied by Douglas factorization is the reduced solution, not the unique solution determined solely by operator-norm minimization.

## Assumptions and scope
The example lies entirely inside the source's setting. The controls are the identity, the coefficient spaces are one-dimensional, and the original family is a redundant ordinary Parseval frame.

No singular \(K\) is used:
\[
K=
\operatorname{diag}(1,1/2)
\]
is invertible. Thus the nonuniqueness is caused by redundancy of the synthesis operator together with slack below its top singular direction, not by a kernel of \(K\).

The finding concerns uniqueness under the global operator norm. It does not deny existence or uniqueness of the Douglas reduced solution.

## Proof
The frame vectors give
\[
T_\Lambda^*(x_1,x_2)
=
\left(
x_1,
\frac{x_2}{\sqrt2},
\frac{x_2}{\sqrt2}
\right),
\]
so
\[
T_\Lambda T_\Lambda^*=I.
\]
Consequently
\[
\|T_\Lambda\|=1.
\]

For the family \(V_c\),
\[
T_\Lambda V_c(x_1,x_2)
=
\left(
x_1,
\frac{(1/2+c)+(1/2-c)}2x_2
\right)
=
(x_1,x_2/2)
=
K(x_1,x_2).
\]
Thus every \(V_c\) satisfies the dual reconstruction identity.

The squared norm of \(V_cx\) is
\[
\|V_cx\|^2
=
|x_1|^2+
\left(\frac14+c^2\right)|x_2|^2.
\]
Hence
\[
\|V_c\|^2
=
\max\left\{1,\frac14+c^2\right\}.
\]
It follows that
\[
\|V_c\|=1
\]
throughout the interval
\[
|c|\le\frac{\sqrt3}{2}.
\]

For any dual analysis operator \(V\),
\[
K=T_\Lambda V,
\]
and therefore
\[
1=\|K\|\le\|T_\Lambda\|\,\|V\|=\|V\|.
\]
Thus no dual can have norm below \(1\), proving that every \(V_c\) in the displayed interval is a global minimizer.

Finally,
\[
N(T_\Lambda)
=
\operatorname{span}\{(0,1,-1)\}.
\]
The member
\[
V_0=T_\Lambda^*K
\]
has range in
\[
R(T_\Lambda^*)=N(T_\Lambda)^\perp.
\]
For every \(c\),
\[
(V_c-V_0)(x_1,x_2)
=
\frac{cx_2}{\sqrt2}(0,1,-1),
\]
so every nonzero \(c\) adds a synthesis-kernel component. This explains why Douglas' reduced solution is unique while norm minimizers are not.

## Verification
The source was inspected at its controlled-dual definition, Douglas-factorization lemma, Theorem 3.6, Proposition 3.7 and its complete proof, and the later parametrization and canonical-dual characterization.

Proposition 3.7 explicitly claims uniqueness among all controlled duals satisfying the minimal synthesis-operator norm inequality. Its proof selects the Douglas reduced factor and proves that its norm is minimal, but does not prove that another solution cannot have the same norm.

The source's own Douglas lemma records additional conditions accompanying the unique reduced factor. The example above retains the minimum norm while changing only the synthesis-kernel component, so it distinguishes precisely between reduced-solution uniqueness and norm-minimizer uniqueness.

The calculations are exact finite-dimensional identities; no numerical experiment or finite search is used.

## Relationship to prior work
The operator-norm uniqueness assertion predates the controlled \(K\)-\(g\)-frame formulation. Xiang's 2019 paper states that Guo's canonical dual \(K\)-Bessel sequence is unique among duals whose analysis operator attains the minimum norm and builds later characterizations on that terminology. Li and Li's 2020 work likewise cites existence and uniqueness of a canonical \(K\)-dual Bessel sequence defined through minimal analysis-operator norm.

Those papers establish that the issue is inherited from the operator-theoretic canonical-dual convention rather than caused by the control operators. The present controlled \(K\)-\(g\)-frame proposition is nevertheless a distinct theorem with the same overstrong uniqueness conclusion.

The correct operator-theoretic uniqueness is the Douglas reduced solution: add the reduced-range condition
\[
R(V)\subseteq\overline{R(T_\Lambda^*)}.
\]
In the example this singles out \(V_0\) from the continuum of minimum-norm duals.

## Limitations
The result corrects the uniqueness clause of Proposition 3.7. It does not invalidate the existence of a minimum-norm dual or the later formulas that specifically identify the reduced canonical dual.

The example proves nonuniqueness for operator norm. It does not claim nonuniqueness for every stricter optimization criterion, such as pointwise coefficient-norm minimization.

A nonindexed erratum or informal correction may contain the same observation.

## References
1. H. Hosseinnezhad, *Dual and canonical dual of controlled \(K\)-\(g\)-frames in Hilbert spaces*, Turkish Journal of Mathematics 44(4) (2020), 1181--1196, DOI 10.3906/mat-2002-113.
2. Z.-Q. Xiang, *Some Properties of Canonical Dual \(K\)-Bessel Sequences for Parseval \(K\)-Frames*, Journal of Function Spaces (2019), Article 9862369, DOI 10.1155/2019/9862369.
3. Y.-Z. Li and Y.-N. Li, *The \(K\)-dual Bessel generators for unitary groups of Hilbert spaces*, Journal of Mathematical Analysis and Applications 482(1) (2020), Article 123548, DOI 10.1016/j.jmaa.2019.123548.
4. R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proceedings of the American Mathematical Society 17 (1966), 413--415.
