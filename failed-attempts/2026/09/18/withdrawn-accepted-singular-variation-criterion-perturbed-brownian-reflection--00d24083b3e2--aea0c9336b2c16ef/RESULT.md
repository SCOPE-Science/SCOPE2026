# Singular-variation criterion for subcritical perturbed Brownian reflection

## Statement

Let \(B\) be a standard Brownian motion, \(x\ge 0\), \(\nu<1/2\), and let
\(b:[0,\infty)\to\mathbb R\) be deterministic, continuous, locally of finite
variation, with \(b(0)=0\). Consider
\[
W_t=(1-\nu)x+B_t+\nu M_t(W)+\frac12L_t^0(W-b),
\qquad W_t\ge b(t),
\tag{1}
\]
where \(M_t(W)=\sup_{0\le s\le t}W_s\).

Set \(\bar\nu=1-\nu\), \(\nu^*=\nu/\bar\nu\), and
\[
R=\begin{pmatrix}1&\nu^*\\-1&1\end{pmatrix}.
\]
Because \(\rho(|I-R|)=\sqrt{|\nu^*|}<1\), the orthant Skorokhod problem with
driver
\[
f_t=\binom{x+B_t-b(t)}{-B_t}
\]
has a unique adapted continuous solution \((X,Y,K,V)\). Define \(W=X+b\).
Then
\[
\frac{V_t}{\bar\nu}=M_t(W)-x
\]
and hence
\[
W_t=(1-\nu)x+B_t+\nu M_t(W)+K_t,\qquad W_t\ge b(t),
\tag{2}
\]
with \(K\) increasing only on \(\{W=b\}\).

The following identity describes exactly when this Skorokhod regulator is the
boundary local time required in (1).

### Theorem 1 (local-time defect identity)

Let
\[
A_t:=\int_0^t {\bf 1}_{\{W_s=b(s)\}}\,db(s),\qquad
J_t:=\int_0^t {\bf 1}_{\{W_s=b(s)\}}\,dM_s(W).
\]
Then, almost surely for every \(t\ge0\),
\[
\boxed{\;
K_t-\frac12L_t^0(W-b)=A_t-\nu J_t.
\;}
\tag{3}
\]

If \(db=b'_a(t)\,dt+db_s\) is the Lebesgue decomposition of the Stieltjes
measure of \(b\), the absolutely continuous part contributes neither to \(A\)
nor to \(J\). More explicitly,
\[
A_t=\int_0^t{\bf 1}_{\{W_s=b(s)\}}\,db_s(s),
\qquad
J_t=\int_0^t{\bf 1}_{\{M_s(W)=b(s)\}}\,db_s(s).
\tag{4}
\]
Thus the discrepancy between the Skorokhod regulator and half the local time
is carried entirely by the singular variation of the boundary.

### Corollary 2 (all locally absolutely continuous boundaries)

If \(b\) is locally absolutely continuous, then
\[
K_t=\frac12L_t^0(W-b)\qquad\text{for all }t\ge0
\]
almost surely. Consequently, for every \(x\ge0\) and every \(\nu<1/2\),
equation (1) has a unique strong solution.

No Brownian-scale modulus condition on the upward increments of \(b\) is
needed in this subcritical regime.

### Corollary 3 (exact criterion for increasing boundaries)

Suppose in addition that \(b\) is nondecreasing. For the unique orthant
Skorokhod candidate \(W\),
\[
\boxed{\;
\text{(1) has a solution}
\iff
\int_0^t{\bf 1}_{\{W_s=b(s)\}}\,db(s)=0
\quad\text{for every }t\ge0.
\;}
\tag{5}
\]
When (5) holds, the solution is automatically pathwise unique.

Since the absolutely continuous part of \(db\) never charges the contact set,
(5) is equivalently a condition only on the singular Stieltjes component of
an increasing boundary.

## Proof

The orthant Skorokhod reduction is the one used for the subcritical regime in
Wang (2026). Adding the two coordinates in
\[
\binom{X}{Y}
=
\binom{x+B-b}{-B}
+
R\binom{K}{V}
\]
gives
\[
Y_t=x-W_t+\frac{V_t}{\bar\nu}.
\]
Because \(V/\bar\nu\) is continuous, increasing, starts from zero, and
increases only when \(Y=0\), the one-dimensional Skorokhod lemma yields
\[
\frac{V_t}{\bar\nu}
=
\sup_{0\le s\le t}(W_s-x)^+
=
M_t(W)-x.
\]
This proves (2).

Put \(X=W-b\ge0\). Its local martingale part is \(B\), so
\(\langle X\rangle_t=t\). The occupation-density formula therefore gives
\[
\int_0^t{\bf 1}_{\{X_s=0\}}\,ds=0,
\qquad
\int_0^t{\bf 1}_{\{X_s=0\}}\,dB_s=0.
\tag{6}
\]
From (2),
\[
dX=dB+\nu\,dM+dK-db.
\]
Tanaka's formula for the nonnegative semimartingale \(X=X^+\), together with
the support property of \(dK\), gives
\[
\frac12L_t^0(X)
=
\int_0^t{\bf 1}_{\{X_s=0\}}\,dX_s
=
\nu J_t+K_t-A_t,
\]
which is (3).

It remains to identify which part of \(db\) can enter \(A\) and \(J\).
Equation (6) implies that the contact set \(\{X=0\}\) has Lebesgue measure
zero. Hence the absolutely continuous part \(b'_a(t)\,dt\) contributes
nothing to \(A\).

Now let \(F=M(W)-b\). Since \(M\ge W\ge b\), \(F\ge0\); moreover \(F\) is
continuous and locally of finite variation. The finite-variation version of
Tanaka's formula gives
\[
{\bf 1}_{\{F=0\}}\,dF=0,
\]
and hence
\[
{\bf 1}_{\{F=0\}}\,dM
=
{\bf 1}_{\{F=0\}}\,db.
\tag{7}
\]
The measure \(dM\) is carried by \(\{W=M\}\). On this support, if \(X=0\),
then \(M=W=b\), so \(F=0\). Conversely \(F=0\) implies
\(M=b\), and \(M\ge W\ge b\) forces \(W=b\). Therefore
\[
J_t
=
\int_0^t{\bf 1}_{\{F_s=0\}}\,db(s).
\]
Again \(\{F=0\}\subseteq\{X=0\}\) has zero Lebesgue measure, so only \(db_s\)
contributes. This proves (4). If \(b\) is locally absolutely continuous then
\(db_s=0\), so (3) gives \(K=L^0(X)/2\), proving existence in Corollary 2.
Any solution of (1) induces a solution of the same orthant Skorokhod problem,
so uniqueness of that Skorokhod problem gives pathwise uniqueness.

Finally suppose \(b\) is nondecreasing. Then \(A_t,J_t\ge0\), and (7) gives
\(0\le J_t\le A_t\). Equation (1) is satisfied exactly when
\(K=L^0(X)/2\), equivalently \(A_t=\nu J_t\) for all \(t\). If
\(\nu<0\), nonnegativity immediately forces \(A_t=J_t=0\). If
\(0\le\nu<1/2\), then
\[
A_t=\nu J_t\le \nu A_t
\]
again forces \(A_t=0\). The converse is immediate because \(A_t=0\) implies
\(J_t=0\). This proves (5).

## Consequence: Hölder exponent alone does not classify solvability

For every \(\alpha\in(0,1/2]\), define the increasing boundary
\[
b_\alpha(t)=\min\{t^\alpha,1\}.
\]
It is globally \(\alpha\)-Hölder, has total variation one, and is absolutely
continuous. Hence, for every \(\nu<1/2\), (1) has a unique strong solution
with boundary \(b_\alpha\).

Yet \(b_\alpha\) fails Wang's condition
\[
\omega^+_{b,T}(h)=o(\sqrt h)
\]
at the origin whenever \(\alpha\le1/2\): for \(\alpha<1/2\),
\(b_\alpha(h)/\sqrt h=h^{\alpha-1/2}\to\infty\), while for
\(\alpha=1/2\) the ratio equals one. In particular, the critical boundary
\(b(t)=\min\{\sqrt t,1\}\) is solvable throughout the subcritical
\(\nu<1/2\) regime although it lies outside the stated positive theorem.

For every \(\alpha\in(0,1/2)\), Wang (2026) also constructs an increasing,
globally \(\alpha\)-Hölder boundary of total variation one whose Stieltjes
measure is singular and for which no solution starting from zero exists for
any \(\nu<1\). Thus, already for fixed \(\alpha<1/2\), the same Hölder
regularity and the same total variation admit both solvable and nonsolvable
boundaries. The distinction is not the Hölder exponent by itself; in the
subcritical orthant regime it is the singular boundary variation seen by the
contact set.

## Relation to prior work

Wang (2026) introduced the time-dependent-boundary problem above. Its main
positive result assumes the Brownian-scale condition
\(\omega^+_{b,T}(h)=o(\sqrt h)\); its negative result constructs singular
\(\alpha\)-Hölder counterexamples for \(\alpha<1/2\). The same paper gives
the orthant Skorokhod reduction for \(\nu<1/2\), proves a no-\(db\)-charge
property for any genuine solution with increasing boundary, and identifies
the regulator with local time under its modulus condition.

The classical orthant result that \(\rho(|I-R|)<1\) yields a unique
Skorokhod solution is due to the reflected-Brownian/Skorokhod literature,
including Williams (1995); Bass and Burdzy (2025) describe the same
subcritical criterion while studying the critical case. Doney and Zhang
(2005) establish existence and uniqueness for perturbed Skorokhod equations
with a fixed reflecting level.

The contribution here is the exact defect identity (3), its localization to
the singular Stieltjes component (4), the resulting if-and-only-if
contact-measure criterion (5) for increasing boundaries in the
\(\nu<1/2\) regime, and the consequent removal of the Brownian-scale modulus
condition for all locally absolutely continuous boundaries.

## Limitations

The sufficient absolute-continuity result is proved only in the subcritical
regime \(\nu<1/2\), where the associated orthant Skorokhod problem has a
unique solution for every continuous driver. For \(\nu\ge1/2\), existence
and uniqueness of the regulator problem itself require additional analysis,
so (3) alone does not extend the corollary to that range.

For a general singular boundary, criterion (5) is path-dependent: it reduces
solvability to whether the unique Skorokhod candidate's contact set is
charged by \(db\), but it does not give a deterministic condition on \(b\)
alone. No claim is made that absolute continuity is necessary. At the
critical Hölder exponent \(1/2\), the result supplies explicit solvable
boundaries but does not classify all \(1/2\)-Hölder boundaries.

## References

1. C. Wang, *Perturbed Brownian motion reflected at a time-dependent
   boundary*, arXiv:2609.20491 (2026).
   https://arxiv.org/abs/2609.20491
2. R. J. Williams, *Semimartingale reflecting Brownian motions in the
   orthant*, in *Stochastic Networks*, IMA Vol. Math. Appl. 71, 125--137
   (1995), DOI: 10.1007/978-1-4757-2418-9_7.
3. R. F. Bass and K. Burdzy, *Uniqueness for the Skorokhod problem in an
   orthant: critical cases*, Electronic Journal of Probability 30 (2025);
   arXiv:2407.05140.
4. R. A. Doney and T. Zhang, *Perturbed Skorohod equations and perturbed
   reflected diffusion processes*, Ann. Inst. H. Poincaré Probab. Statist.
   41 (2005), 107--121, DOI: 10.1016/j.anihpb.2004.03.005.
