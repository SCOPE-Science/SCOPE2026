# Boundary-stress directional derivatives and a metric kink criterion for isoperimetric uniqueness

## Statement

Let \((M^{n+1},g)\) be a closed connected smooth Riemannian manifold, \(n\ge 1\), and fix
\[
0<m<\operatorname{Vol}_g(M).
\]
Write
\[
I_g(m)=\inf\{P_g(E):\operatorname{Vol}_g(E)=m\}
\]
for the isoperimetric profile and \(\mathcal I(g,m)\) for its minimizing finite-perimeter sets. Let \(\mathscr X_g^\infty\) be the smooth, \(g\)-self-adjoint, trace-free endomorphism fields. For \(A\in\mathscr X_g^\infty\), set
\[
g_{t,A}=g e^{tA}.
\]
The volume form is independent of \(t\).

For a finite-perimeter set \(E\), let
\[
\mathsf T_E=\frac12\left(\nu_E^\flat\otimes\nu_E^\flat-\frac1{n+1}g\right)\mu_E
\]
be its trace-free boundary stress, and write \(\langle\mathsf T_E,A\rangle\) for its pairing with \(A\).

### Theorem 1: Hadamard directional formula

For every \(A\in\mathscr X_g^\infty\),
\[
\boxed{
\left.\frac{d}{dt}\right|_{t=0+} I_{g e^{tA}}(m)
=-\max_{E\in\mathcal I(g,m)}\langle\mathsf T_E,A\rangle
}
\]
and
\[
\boxed{
\left.\frac{d}{dt}\right|_{t=0-} I_{g e^{tA}}(m)
=-\min_{E\in\mathcal I(g,m)}\langle\mathsf T_E,A\rangle.
}
\]
The right derivative is Hadamard-stable with respect to the direction: if \(t_j\downarrow0\) and \(A_j\to A\) smoothly, then
\[
\frac{I_{g e^{t_jA_j}}(m)-I_g(m)}{t_j}
\longrightarrow
-\max_{E\in\mathcal I(g,m)}\langle\mathsf T_E,A\rangle.
\]
No regularity or nondegeneracy assumption on the isoperimetric boundary is required.

Equivalently, if
\[
\mathcal S(g,m)=\{\mathsf T_E:E\in\mathcal I(g,m)\},
\]
then the full one-sided first-order metric response is the negative support function of the stress set:
\[
D_+I_g(m;A)=-h_{\mathcal S(g,m)}(A).
\]
Thus the directional derivative data determine the weak-* closed convex hull of the boundary stresses.

### Theorem 2: differentiability is equivalent to uniqueness up to complement

Define on the volume-form-preserving Ebin slice
\[
J(A)=I_{g e^A}(m),\qquad A\in\mathscr X_g^\infty.
\]
The following are equivalent:

1. every two members of \(\mathcal I(g,m)\) agree modulo null sets up to complementation;
2. for every \(A\in\mathscr X_g^\infty\), the function \(t\mapsto I_{g e^{tA}}(m)\) is two-sided differentiable at \(0\);
3. \(J\) is Gâteaux differentiable at \(0\).

When these conditions hold and \(E\in\mathcal I(g,m)\),
\[
\boxed{DJ(0)[A]=-\langle\mathsf T_E,A\rangle.}
\]
If \(2m\ne\operatorname{Vol}_g(M)\), the conditions are equivalent to ordinary uniqueness of the isoperimetric region. If \(2m=\operatorname{Vol}_g(M)\), they are equivalent to having exactly the complementary pair \(E,E^c\).

Conversely, if \(E,F\in\mathcal I(g,m)\) are not complementary, then there is a smooth trace-free direction \(A\) for which the profile has a strict metric kink,
\[
D_-I_g(m;A)-D_+I_g(m;A)
=
\max_{G\in\mathcal I(g,m)}\langle\mathsf T_G,A\rangle
-
\min_{G\in\mathcal I(g,m)}\langle\mathsf T_G,A\rangle
>0.
\]

### Global sensitivity bound

For every \(A\in\mathscr X_g^\infty\),
\[
\boxed{
e^{-\|A\|_{0,g}/2}I_g(m)
\le I_{g e^A}(m)
\le e^{\|A\|_{0,g}/2}I_g(m),
}
\]
hence
\[
\boxed{
\left|\log I_{g e^A}(m)-\log I_g(m)\right|
\le\frac12\|A\|_{0,g}.
}
\]

## Proof

Gongping Niu proved for every fixed finite-perimeter set \(E\) and every \(A\in\mathscr X_g^\infty\) that
\[
P_{g e^{tA}}(E)
=P_g(E)-t\langle\mathsf T_E,A\rangle+R_t(E),
\]
with
\[
|R_t(E)|\le \frac14t^2\|A\|_{0,g}^2e^{|t|\|A\|_{0,g}/2}P_g(E).
\]
He also proved compactness of isoperimetric regions under smooth metric convergence, strict \(BV_g\) convergence of minimizing subsequences, weak-* continuity of \(\mathsf T_E\) under that strict convergence, and the separation theorem
\[
\mathsf T_E=\mathsf T_F
\iff
F=E\ \text{or}\ E^c\quad\text{modulo null sets}.
\]
These facts are the input.

Fix \(t_j\downarrow0\) and \(A_j\to A\) smoothly. Since \(\mathcal I(g,m)\) is compact and the stress pairing is continuous on it, choose \(E_*\in\mathcal I(g,m)\) maximizing \(\langle\mathsf T_E,A\rangle\). Using \(E_*\) as a competitor for \(g e^{t_jA_j}\) gives
\[
\limsup_j\frac{I_{g e^{t_jA_j}}(m)-I_g(m)}{t_j}
\le -\langle\mathsf T_{E_*},A\rangle.
\]

For the reverse inequality, choose
\[
E_j\in\mathcal I(g e^{t_jA_j},m).
\]
After passing to a subsequence, Niu's compactness result gives strict \(BV_g\) convergence \(E_j\to E\) for some \(E\in\mathcal I(g,m)\). The fixed-set expansion, now applied with \(A_j\), gives
\[
I_{g e^{t_jA_j}}(m)
=P_g(E_j)-t_j\langle\mathsf T_{E_j},A_j\rangle+R_j.
\]
Because \(P_g(E_j)\ge I_g(m)\),
\[
\frac{I_{g e^{t_jA_j}}(m)-I_g(m)}{t_j}
\ge -\langle\mathsf T_{E_j},A_j\rangle+\frac{R_j}{t_j}.
\]
The perimeters \(P_g(E_j)\) stay bounded, \(A_j\) stays bounded in \(C^0\), and the explicit remainder estimate gives \(R_j/t_j\to0\). Moreover
\[
\langle\mathsf T_{E_j},A_j\rangle
-\langle\mathsf T_{E_j},A\rangle\to0
\]
by the uniform perimeter bound and \(\|A_j-A\|_0\to0\), while weak-* stress convergence gives
\[
\langle\mathsf T_{E_j},A\rangle\to\langle\mathsf T_E,A\rangle.
\]
Hence every subsequential lower limit is at least
\[
-\langle\mathsf T_E,A\rangle
\ge -\max_{F\in\mathcal I(g,m)}\langle\mathsf T_F,A\rangle.
\]
This matches the upper bound and proves the Hadamard right-derivative formula. Applying it to \(-A\) and replacing \(t\) by \(-t\) gives the left-derivative formula.

The two one-sided derivatives agree for every \(A\) exactly when
\[
\langle\mathsf T_E,A\rangle
\]
is independent of \(E\in\mathcal I(g,m)\) for every smooth trace-free \(A\). Smooth trace-free fields separate trace-free tensor-valued Radon measures, so all minimizing stresses must coincide. Niu's stress-rigidity proposition then says all minimizers are equal up to complement. The converse is immediate because complementation leaves \(\mathsf T_E\) unchanged. The common derivative is linear in \(A\), giving the Gâteaux statement. If noncomplementary minimizers exist, their stresses differ and a smooth trace-free field separates them, giving a strict kink.

Finally, Niu's exact perimeter identity
\[
P_{g e^A}(E)=\int_{\partial^*E}|e^{-A/2}\nu_E|_g\,d\mu_E
\]
implies
\[
e^{-\|A\|_0/2}P_g(E)
\le P_{g e^A}(E)
\le e^{\|A\|_0/2}P_g(E).
\]
The volume form is unchanged, so taking the infimum over the same volume-\(m\) admissible sets proves the global sensitivity bound.

## Relation to recent work

Niu's 17 September 2026 preprint proves generic uniqueness of isoperimetric regions in arbitrary dimension, including the singular-boundary setting. Its variational mechanism introduces the trace-free boundary stress, gives the fixed-set perimeter expansion above, and shows that a generic perturbation selects a unique minimizing stress. The preprint does not state the derivative of the optimized value \(I_g(m)\) with respect to the metric, nor the equivalence between differentiability of that value and uniqueness up to complement.

The abstract envelope-theorem principle for optimized values is classical; for example Milgrom--Segal (2002) treat value-function derivatives for arbitrary choice sets. The contribution here is the geometric specialization with an exact boundary-stress support formula, including Hadamard stability, finite-perimeter compactness, singular boundaries, and the converse metric-kink characterization through Niu's stress rigidity.

A direct corollary of Niu's generic uniqueness theorem and Theorem 2 is that, for each fixed volume fraction \(s\in(0,1)\), a generic smooth metric \(g\) is a Gâteaux differentiability point of
\[
A\longmapsto I_{g e^A}\!\left(s\operatorname{Vol}_g(M)\right)
\]
at \(A=0\) along trace-free directions. This remains true at \(s=1/2\), where the generic complementary pair has a common stress.

## Limitations

The derivative formula is restricted to the volume-form-preserving trace-free Ebin slice. For a general metric variation, the volume constraint itself moves and additional terms are required. Only first-order sensitivity is established; no second-order formula or quantitative convergence rate for minimizing regions is claimed. Gâteaux differentiability is not promoted here to Fréchet differentiability. The motivating preprint is very recent, so unindexed parallel work remains a residual originality risk.

## References

1. Gongping Niu, *Generic Uniqueness of Isoperimetric Regions in Arbitrary Dimension*, arXiv:2609.20790v1, 17 September 2026. https://arxiv.org/abs/2609.20790
2. Paul Milgrom and Ilya Segal, *Envelope Theorems for Arbitrary Choice Sets*, Econometrica 70 (2002), 583--601. https://doi.org/10.1111/1468-0262.00296
