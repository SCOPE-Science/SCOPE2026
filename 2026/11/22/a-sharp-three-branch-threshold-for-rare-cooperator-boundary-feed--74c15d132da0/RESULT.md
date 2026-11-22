# A sharp three-branch threshold for rare-cooperator boundary feedback

## Finding

In the binary edge-environment evolutionary game of Betz, Fu and Masuda [1], the **regularized all-defector boundary** determines a conditional environmental fraction and a candidate rare-cooperator growth rate from an implicit nonlinear equation. The exact equation can have **one, two, or three distinct solutions**, and the full multiplicity classification is explicit.

Let
\[
 a=2\omega(p_1+q_1),\quad b=1-\omega,\quad
 u=\frac{q_1}{p_1+q_1},\quad v=\frac{q_2}{p_2+q_2},\quad
 h=S_0-S_1,\quad d=S_1-P_1-(P_0-P_1)v.
\]
Set
\[
 c(r)=\frac{au+brv}{a+br},\qquad
 G(r)=\frac{1}{\beta}\log\frac{r}{1-r}-hc(r),\qquad
 K=\beta hab(v-u),\qquad 0<r<1.
\]
For the paper's ordering of environmental transition probabilities, \(0<u<v<1\). Each admissible boundary candidate corresponds one-to-one to a root of \(G(r)=d\); its conditional cross-strategy environment is \(c_2=c(r)\), and its candidate rare-cooperator growth rate is \(b(2r-1)\).

**Complete classification.** If \(h\le0\), or if \(h>0\) and
\[
 \boxed{\beta h b(v-u)\le 4(a+b),}
\]
there is exactly one boundary candidate. Otherwise define
\[
 r_{\pm}=\frac{K-2ab\ \pm\sqrt{K[K-4a(a+b)]}}{2(b^2+K)},
 \qquad 0<r_-<r_+<1.
\]
There are exactly three distinct candidates if and only if
\[
 \boxed{G(r_+)<d<G(r_-).}
\]
At either equality there are two distinct candidates, one double; outside the closed interval there is one. The three-branch regime comprises two attracting and one repelling states of the **auxiliary conditional-environment flow restricted to the regularized boundary**. The result is a classification of the boundary approximation, not a theorem that a finite population has multiple invasion probabilities.

An admissible exact example has two attracting boundary-environment branches predicting **opposite signs** of rare-cooperator linear growth. Take
\[
 \omega=\tfrac15,\quad\beta=40,\quad
 (p_0,p_1,p_2)=(\tfrac45,\tfrac12,\tfrac1{10}),\quad
 (q_0,q_1,q_2)=(\tfrac15,\tfrac25,\tfrac9{10}),
\]
with environmental payoff matrices
\[
 A_0=\begin{pmatrix}5&1\\3&37/57\end{pmatrix},\qquad
 A_1=\begin{pmatrix}3&0\\4&1\end{pmatrix}.
\]
All strict game and environmental-switching inequalities in [1] hold. The three solutions are approximately
\[
 r_1\simeq0.00006855073918,\quad r_2=\tfrac12,\quad
 r_3\simeq0.93855196579.
\]
The first and third branches attract within the regularized boundary's conditional-environment dynamics, whereas the middle one repels. Their transverse candidate cooperator growth rates have signs negative, zero, and positive, respectively. The two opposite signs arise for exactly the same fixed parameters.

## Assumptions and scope

We use the **infinite-population well-mixed regularized boundary approximation** of [1, Eqs. (47)–(55)] for two strategies \(C,D\) and a binary environmental state on each interaction. The updating probability is \(0<\omega<1\), Fermi rationality is \(\beta>0\), and environmental transition probabilities satisfy
\[
 1>p_0>p_1>p_2>0,\qquad 0<q_0<q_1<q_2<1.
\]
The depleted payoff matrix \(A_0\) satisfies \(R_0>T_0\), \(S_0>P_0\); the rich matrix \(A_1\) satisfies \(R_1<T_1\), \(S_1<P_1\). No sign condition is imposed a priori on \(h=S_0-S_1\). All quantities are real and finite. The conditional variables \(c_1,c_2,c_3\in[0,1]\) have the meanings and boundary regularization of [1], not independent physically populated edge types at zero cooperator mass.

At the all-defector regularized boundary, \(x=0\), the environmental variable \(c_3\) has limiting equilibrium \(v\). With \(c_3=v\), the conditional \(C\)-\(D\) environment obeys the scalar auxiliary ODE
\[
 \dot c_2=a(u-c_2)+b\rho(c_2)(v-c_2),\qquad
 \rho(c_2)=\frac{1}{1+e^{-\beta(d+hc_2)}}.
\]
This ODE is an exact restriction of the **regularized** equations, not an exact description of rare mutants in the finite stochastic network. The full boundary includes a further stable \(c_1\) direction and a stable \(c_3\) direction; the transversal cooperator fraction is governed at first order by \(\lambda_{\rm inv}=b(2\rho-1)\), as derived in [1].

## Proof

**Step 1: reduction and admissibility.** The strict ordering of transition probabilities implies
\[
 u=\frac{q_1}{p_1+q_1}<\frac{q_2}{p_2+q_2}=v,
\]
because \(q_1p_2<q_2p_1\). At an auxiliary equilibrium, \((a+b\rho)c_2=au+b\rho v\); hence \(c_2=c(\rho)\in(u,v)\subset(0,1)\). Conversely every \(r\in(0,1)\) with \(G(r)=d\) gives \(c_2=c(r)\), \(c_3=v\), and a unique \(c_1\in(0,1)\) from [1, Eq. (51)]. Thus there are no missing admissible candidate solutions. Logit inversion gives the scalar identity \(G(r)=d\).

**Step 2: count all roots.** Define
\[
 F(r)=\log\frac{r}{1-r}-\beta[d+hc(r)].
\]
We have \(F(0+)=-\infty\), \(F(1-)=+\infty\). Direct differentiation gives
\[
 F'(r)=\frac{(a+br)^2-Kr(1-r)}{r(1-r)(a+br)^2}.
\]
For \(h\le0\), \(K\le0\), so \(F'>0\). If \(h>0\), the sign numerator is the quadratic
\[
 Q(r)=a^2+(2ab-K)r+(b^2+K)r^2.
\]
Its discriminant is exactly \(K[K-4a(a+b)]\). Alternatively, the function \((a+br)^2/[r(1-r)]\) on \((0,1)\) attains its unique minimum \(4a(a+b)\) at \(r=a/(2a+b)\). Thus \(F\) is strictly increasing when \(K\le4a(a+b)\), including equality (where \(F'\) vanishes at only one point).

When \(K>4a(a+b)\), the two distinct critical points are precisely \(r_-<r_+\) displayed above, and lie in \((0,1)\). The derivative is positive on \((0,r_-)\cup(r_+,1)\) and negative on \((r_-,r_+)\). Hence \(G\) increases, then decreases, then increases, with a strict local maximum \(G(r_-)\) and minimum \(G(r_+)\). Counting intersections of the horizontal line \(G=d\) proves the exact one/two/three classification, including the two tangencies. Rewriting \(K>4a(a+b)\) yields \(\beta hb(v-u)>4(a+b)\).

**Step 3: auxiliary stability.** At a scalar equilibrium, the derivative of the boundary conditional-environment vector field is
\[
 \frac{\partial\dot c_2}{\partial c_2}
 =-(a+br)+b\beta h r(1-r)(v-c(r))
 =-(a+br)r(1-r)F'(r),
\]
where \(v-c(r)=a(v-u)/(a+br)\) was used. Thus the two outer simple roots have negative auxiliary eigenvalue and the middle root positive eigenvalue. The other two conditional-environment directions have eigenvalues \(-2\omega(p_0+q_0)-2br\) and \(-2\omega(p_2+q_2)\), both negative. These statements concern attraction **tangent to the regularized boundary**. The transverse candidate invasion eigenvalue remains \(b(2r-1)\) and must be checked independently.

**Step 4: exact three-branch witness.** For the rational parameters displayed in the Finding,
\[
 a=\tfrac9{25},\quad b=\tfrac45,\quad u=\tfrac49,\quad
 v=\tfrac9{10},\quad h=1,\quad d=-\tfrac{13}{19},
 \quad K=\tfrac{656}{125}>\tfrac{1044}{625}=4a(a+b).
\]
Moreover
\[
 c(\tfrac12)=\tfrac{13}{19},\qquad
 F(\tfrac12)=0,\qquad F'(\tfrac12)=-\tfrac{1836}{361}<0.
\]
Since \(F\) starts negative and ends positive and has at most three distinct zeros, a negative derivative at the exact central zero forces precisely one additional root on either side of \(1/2\). Their auxiliary derivatives are negative; the central derivative is positive. Since \(b>0\), the transverse growth signs are respectively negative, zero, positive. This proves the existence of opposite invasion verdicts among attracting **boundary candidates**, without using approximate root values. At the central candidate the exact auxiliary eigenvalue is \(459/475>0\).

## Verification

The standalone standard-library checker `verify.py` recomputes the exact rational parameter inequalities, fold threshold, central fixed point, derivative, and central auxiliary eigenvalue. It additionally bisects the two outer roots numerically and verifies their environmental and transverse eigenvalue signs. Run from the directory containing the file:

```text
python3 verify.py
```

The infinite root count is proved analytically in Steps 1–2; the finite numerical bisections are illustrations and checks, not certificates of a global count. No external numerical dataset is required.

## Relationship to prior work

Betz, Fu and Masuda [1, Eqs. (51)–(55)] derive the rare-cooperator scalar implicit system and explicitly allow for the possibility of multiple solutions, without giving a sharp condition or an admissible three-solution witness. The fixed-point equations, Fermi updating, and candidate growth rate are theirs. The present result classifies their **same implicit system** and exhibits conflicting candidate invasion signs. Their numerical findings on full-population bistability, interior equilibria, and oscillations are different claims, neither implied by nor used here.

Betz, Fu and Masuda [2] analyze a continuous environmental-feedback replicator model on two communities; their equilibrium and stability results do not provide the binary conditional-edge rare-invader fold test above. Su, McAvoy, Wang and Nowak [3] derive weak-selection conditions for games whose interaction states change; their fixation comparisons do not assert the present finite-selection-strength regularized-boundary solution count. Ito and Yamamichi [4] classify continuous resource-feedback game regimes, which likewise does not directly supply this exact scalar conditional-environment threshold.

## Limitations

The statement is **not** a proof that actual rare cooperators in a finite network have three invasion probabilities, or that two physical invasion outcomes coexist from the same populated all-defector state. As [1] emphasizes, the boundary conditional fractions are auxiliary variables when the associated edge type is absent; establishing a rigorous selection of boundary branches in the original finite-population model remains unproved. The theorem does not describe the finite stochastic process, global four-dimensional basins, or fixation probabilities. Tangent double roots are nonhyperbolic in the auxiliary direction. No claim of historical uniqueness follows from the searches alone; independent scientific validation and a broader literature audit remain to be done.

## References

[1] K. Betz, F. Fu, and N. Masuda, *Evolutionary games on networks with negative edge-based environmental feedback*, arXiv:2611.11029v1 (first public version, 2026-11-08), https://arxiv.org/abs/2611.11029 . Full preprint inspected, especially Eqs. (35)–(55), boundary caveats and concluding discussion.

[2] K. Betz, F. Fu, and N. Masuda, *Evolutionary Game Dynamics with Environmental Feedback in a Network with Two Communities*, Bulletin of Mathematical Biology 86, 84 (2024), https://doi.org/10.1007/s11538-024-01310-3 . Open-access HTML inspected, especially model and analytical framework.

[3] Q. Su, A. McAvoy, L. Wang, and M. A. Nowak, *Evolutionary dynamics with game transitions*, Proceedings of the National Academy of Sciences 116, 25398–25404 (2019), https://doi.org/10.1073/pnas.1908936116 . Public abstract and model description checked.

[4] H. Ito and M. Yamamichi, *A complete classification of evolutionary games with environmental feedback*, PNAS Nexus 3, pgae455 (2024), https://doi.org/10.1093/pnasnexus/pgae455 . Public article summary and discussion checked; full mathematical exposition was not accessible in this review.
