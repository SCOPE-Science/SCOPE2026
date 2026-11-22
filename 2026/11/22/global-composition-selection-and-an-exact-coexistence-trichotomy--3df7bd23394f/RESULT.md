# Global composition selection and an exact coexistence trichotomy in ratio-dependent intraguild predation

## Finding

In the three-species ratio-dependent intraguild-predation system of Chan and Wu [1], suppose both consumers have identical basal-resource saturation and uptake rates and identical basal-resource conversion gains. Then the **weighted consumer composition evolves autonomously**, regardless of resource abundance and total consumer density. This scalar law gives an exact, global criterion for attraction to an interior composition, exclusion in weighted composition, or neutral preservation of the initial composition. Under the additional natural constraints \(0<c<1\) and \(E\ge a\), every positive coexistence equilibrium is explicitly classified: there is at most one when \(e_3\ne a_3\), and it is locally asymptotically stable exactly when \(e_3>a_3\); at \(e_3=a_3\), any positive equilibria form a normally attracting continuum. No positive coexistence equilibrium undergoes a Hopf bifurcation within this symmetric-gain family.

## Assumptions and scope

Work in dimensionless time, with \(x,y,z>0\) representing basal resource, intraguild prey, and intraguild predator. The precise model is

\[
\begin{aligned}
\dot x&=x(1-x)-\frac{c_1mxy}{a_1x+my+z}-\frac{c_2xz}{a_2x+my+z},\\
\dot y&=y\left(\frac{e_1c_1mx}{a_1x+my+z}-\frac{c_3z}{a_3y+z}-d_1\right),\\
\dot z&=z\left(\frac{e_2c_2x}{a_2x+my+z}+\frac{e_3c_3y}{a_3y+z}-d_2\right).
\end{aligned}
\]

All named parameters are strictly positive, with \(m>0\). Assume the **matched basal-feeding regime**

\[
c_1=c_2=c,\quad a_1=a_2=a,\quad e_1m=e_2=E,\quad 0<c<1,\quad E\ge a.
\]

This is not an assumption of identical organisms: intraguild consumption, conversion \(e_3\), saturation \(a_3\), and mortalities \(d_1,d_2\) remain distinct. Define the weighted consumer fraction, weighted consumer/resource ratio, mortality difference and intraguild denominator:

\[
v=\frac{my}{my+z},\qquad w=\frac{my+z}{x},\qquad \Delta=\frac{d_2-d_1}{c_3},\qquad D(v)=m+(a_3-m)v.
\]

The coordinate transformation is a smooth bijection on the strictly positive octant, with inverse \(y=vwx/m\), \(z=(1-v)wx\). The result concerns exact deterministic dynamics of this model. A limit \(v\to0\) or \(v\to1\) is a **relative-composition** statement, not by itself a claim of absolute species extinction or survival.

## Proof

**1. Autonomous selection law.** Logarithmic differentiation of \(my\) and \(z\) gives \(\dot v=v(1-v)(\dot y/y-\dot z/z)\). The matched basal gains cancel, leaving

\[
\boxed{\dot v=c_3v(1-v)\left[\Delta-\frac{m+(e_3-m)v}{m+(a_3-m)v}\right].}
\]

Set \(G(v)=[m+(e_3-m)v]/D(v)\). Then \(G(0)=1\), \(G(1)=e_3/a_3\), and

\[
G'(v)=\frac{m(e_3-a_3)}{D(v)^2}.
\]

Consequently, if \(e_3>a_3\), an interior composition fixed point exists exactly for \(1<\Delta<e_3/a_3\), and **every** trajectory with \(0<v(0)<1\) converges monotonically to it (unless already there). If \(e_3<a_3\), it exists exactly for \(e_3/a_3<\Delta<1\), is repelling, and the global basins are \(v(0)<v_*\Rightarrow v(t)\to0\) and \(v(0)>v_*\Rightarrow v(t)\to1\). The unique interior root in either case is

\[
\boxed{v_* =\frac{m(\Delta-1)}{e_3-m-\Delta(a_3-m)}.}
\]

Outside these strict inequalities there is no interior root, so the sign of the scalar vector field selects an endpoint (possibly with a nonhyperbolic endpoint at equality). If \(e_3=a_3\), the frequency obeys \(\dot v=c_3(\Delta-1)v(1-v)\): it is constant for every strictly positive trajectory exactly when \(d_2-d_1=c_3\); otherwise it approaches the endpoint selected by the sign of \(\Delta-1\). These conclusions hold for all positive initial abundances, independently of whether the other two population coordinates converge.

**2. Existence and reconstruction of positive equilibria.** With

\[
g(v)=\frac{c_3m(1-v)}{D(v)},\qquad L(v)=d_1+g(v),
\]

the matched-resource system in \((x,v,w)\) has

\[
A=1-x-\frac{cw}{a+w},\quad
B=\frac{Ec}{a+w}-g(v)-d_1,\quad
C=\frac{Ec}{a+w}+\frac{e_3c_3v}{D(v)}-d_2,
\]

and \(\dot x=xA\), \(\dot v=v(1-v)(B-C)\), \(\dot w=w[vB+(1-v)C-A]\). An interior equilibrium requires \(A=B=C=0\). When \(e_3\ne a_3\), it is therefore unique if and only if the stated interior-root condition holds **and** \(L(v_*)<Ec/a\). Its explicit coordinates are

\[
\boxed{
 w_*=\frac{Ec}{L(v_*)}-a,\quad
 x_*=1-\frac{cw_*}{a+w_*},\quad
 y_*=\frac{v_*w_*x_*}{m},\quad
 z_*=(1-v_*)w_*x_*.
}
\]

Every coordinate is strictly positive: \(L>0\), \(w_*>0\), and \(x_*>1-c>0\). Conversely these formulas solve all three equilibrium equations, establishing necessity and sufficiency. At \(e_3=a_3\), the condition \(d_2-d_1=c_3\) is necessary, and every \(v\in(0,1)\) with \(L(v)<Ec/a\) yields an equilibrium via the same formulas. These admissible \(v\)'s form either the empty set or a nonempty open interval, since \(g(v)\) is strictly decreasing. Thus any positive equilibria form an explicit continuous curve, not isolated points.

**3. Full local spectrum.** At every positive equilibrium, the Jacobian in \((x,v,w)\) has entries

\[
J=\begin{pmatrix}
-x_*&0&-x_*ca/(a+w_*)^2\\
0&\lambda_v&0\\
w_*&* &-w_*c(E-a)/(a+w_*)^2
\end{pmatrix},
\quad
\lambda_v=\frac{c_3m v_*(1-v_*)(a_3-e_3)}{D(v_*)^2}.
\]

Here \(*\) is a finite derivative irrelevant to the characteristic polynomial. The two remaining eigenvalues are the roots of

\[
\lambda^2+T\lambda+Q=0,\quad
T=x_*+\frac{w_*c(E-a)}{(a+w_*)^2}>0,\quad
Q=\frac{x_*w_*cE}{(a+w_*)^2}>0.
\]

They have negative real parts. For \(e_3>a_3\), \(\lambda_v<0\), giving local asymptotic stability. For \(e_3<a_3\), \(\lambda_v>0\), giving instability with one positive real eigenvalue. For \(e_3=a_3\), \(\lambda_v=0\), the zero eigenvalue is tangent to the equilibrium curve, while the other two are strictly stable: the curve is locally normally attracting at each of its interior points. This exact spectral factorization rules out a Hopf crossing at a positive equilibrium in the stipulated parameter regime; it **does not** exclude other global periodic phenomena far from an equilibrium.

**4. Exact witnesses.** With \(m=1\), \(c=a=1/2\), \(E=2\), \(c_3=1\), two choices give the same positive equilibrium \((x_*,y_*,z_*)=(3/4,3/16,3/16)\). For \((a_3,e_3,d_1,d_2)=(1,2,1/2,2)\), its Jacobian characteristic polynomial is \((\lambda+1/4)(\lambda^2+9\lambda/8+3/8)\), hence strict local stability. For \((a_3,e_3,d_1,d_2)=(2,1,2/3,4/3)\), it is \((\lambda-1/9)(\lambda^2+9\lambda/8+3/8)\), hence a saddle. In the neutral case \((a_3,e_3,d_1,d_2)=(1,1,1/2,3/2)\), every \(v\in(0,1)\) yields a positive equilibrium. These three examples demonstrate nonempty regimes; they are not the proof of the general classification.

## Verification

`checker.py` uses exact SymPy rational algebra to independently reconstruct the three original differential equations, derive the autonomous composition identity, check the derivative and monotonicity of the scalar response, and verify the full Jacobian characteristic polynomials and equilibrium residuals for the stable and saddle exact witnesses. It also checks the neutral continuum symbolically. Run `python checker.py` with Python 3 and SymPy installed. The infinite-family conclusions follow from the algebra and scalar comparison argument above; finite computations alone do not establish them.

## Relationship to prior work

Chan and Wu [1] introduce the original ratio-dependent intraguild predation model, prove general extinction and equilibrium-branch results, and already derive the composition coordinate and transformed equations (their Section 5). **The coordinate and general transformation are prior work.** The contribution here is the explicit matched-basal-gain reduction in which composition becomes autonomous globally, together with its complete basin and equilibrium-stability trichotomy, the normally attracting coexistence continuum and the rigorous absence of positive-equilibrium Hopf crossings under \(E\ge a\).

Hsu, Hwang and Kuang [2] analyze a ratio-dependent one-prey two-competitor model without the intraguild transfer terms in [1]; their degenerate coexistence continuum is an important precedent, but their equations do not supply this exact intraguild frequency law. Other ecological symmetry and neutral-selection principles provide useful context, not a proof for the specified model.

## Limitations

The matched-feeding equalities and \(0<c<1\), \(E\ge a\) are genuine restrictions; the original asymmetric model may show Hopf bifurcations and chaos [1]. Relative weighted consumer frequency is not an absolute survival probability or a guarantee that the basal resource persists. Local stability and normal attraction are not claimed to imply global convergence of all abundances; global attraction is claimed **only for the autonomous frequency**. No finite-sample estimation theory, noise robustness, or independent scientific audit is claimed. Broader historical literature may contain equivalent specialized results not identified by the performed searches.

## References

[1] Tzu-Hsuan Chan and Chang-Hong Wu, *Extinction and the global structure of positive equilibria in a ratio-dependent intraguild predation model*, arXiv:2610.23995v1, publicly posted 15 October 2026, https://arxiv.org/html/2610.23995v1, particularly Sections 2, 5 and 6; primary MSC2020 92D25.

[2] Sze-Bi Hsu, Tzy-Wei Hwang and Yang Kuang, *Rich dynamics of a ratio-dependent one-prey two-predators model*, Journal of Mathematical Biology 43 (2001), 377–396, https://doi.org/10.1007/s002850100100, particularly the competitive-predator equations and coexistence section.
