# An opinion-connectivity threshold and subcritical symmetry breaking in a two-community higher-order SIS model

## Finding

In an admissible two-community instance of the higher-order SIS--opinion model of Samadi, Caiza, Gracy and Paré, stronger *opinion exchange* destabilizes a synchronous endemic equilibrium even though both communities have identical parameters and their pairwise disease contacts remain unchanged. The loss of stability occurs at the exact weight \(w_*=1/2\), and the symmetry-breaking bifurcation is **subcritical**: two nearby unequal-prevalence equilibria exist on the *stable* side of this boundary but each is unstable.

More precisely, let \(x_i\) denote the infected fraction of community \(i\), let \(y_i=o_i+1/2\) be its shifted opinion, and let \(j=3-i\), for \(i=1,2\). For every \(w\geq0\), consider
\[
\dot x_i=-\left(\frac25+3y_i\right)x_i+(1-x_i)\left(\frac{x_j}{10}+6x_i^2\right),\qquad
\dot y_i=x_i-y_i+w(y_j-y_i).
\tag{1}
\]
On \([0,1]^4\), the healthy equilibrium is locally exponentially stable for all \(w\geq0\). The synchronous endemic equilibrium
\[
E=\left(\frac13,\frac13,\frac13,\frac13\right)
\]
(where coordinates are \((x_1,x_2,y_1,y_2)\)) is locally exponentially stable in the *full four-dimensional system* exactly when \(0\leq w<1/2\). It is a hyperbolic saddle when \(w>1/2\), and it is nonlinearly unstable at \(w=1/2\). Its stability restricted to the synchronous two-dimensional invariant set, however, holds for **all** \(w\geq0\).

There is \(\varepsilon>0\) such that for \(1/2-\varepsilon<w<1/2\), precisely two additional equilibria lie sufficiently near \(E\), exchanged by swapping communities, and both have a positive real eigenvalue. No such nearby unequal equilibria occur for \(1/2<w<1/2+\varepsilon\). Setting \(v=(x_1-x_2)/2\), these branches satisfy
\[
\frac{x_1+x_2}{2}=\frac13-\frac{42}{11}v^2+O(v^4),\qquad
w=\frac12-\frac{246}{11}v^2+O(v^4),\qquad
\frac{y_1-y_2}{2}=\frac{v}{1+2w}.
\tag{2}
\]
In particular, the amplitude of infection disagreement grows like \(\sqrt{(11/246)(1/2-w)}\) as the threshold is approached from below. The transition is a nondegenerate subcritical pitchfork, not an exchange of stability with newly attracting unequal equilibria.

## Assumptions and scope

Equation (1) is a specialized instance of the published higher-order susceptible--infected--susceptible epidemic--opinion model. The infection-contact matrix has \(a_{12}=a_{21}=1\) and other entries zero. The only nonzero quadratic-contact entries are \(b_{111}=b_{222}=1\). The pairwise transmission rate and its minimum are both \(1/10\); the quadratic transmission rate and its minimum are both \(6\). The minimum removal rate is \(2/5\), and the maximum removal rate is \(17/5\), giving the effective removal rate \(2/5+3y_i\). The undirected opinion graph consists of a single edge of weight \(w\). All requirements of nonnegative contacts, symmetric unsigned opinion adjacency and ordered rates are satisfied.

The complete published opinion vector field is piecewise smooth because its signed Laplacian depends on the signs of \(o_i\). At \(E\), \(o_1=o_2=-1/6\), so both opinions are strictly negative in a neighborhood; here the signed Laplacian reduces exactly to the unsigned Laplacian and (1) is the original system. All stability and bifurcation claims are local to this smooth region. The assertion about the healthy equilibrium is likewise local to the region where both original opinions remain negative.

The source's next-generation upper ratio for pairwise transmission is \((1/10)/(2/5)=1/4<1\). Therefore the healthy state is locally stable, and higher-order transmission permits a separate stable endemic state when \(w<1/2\), yielding full-state local bistability. No claims of global convergence or attracting asymmetric branches are made.

## Proof

**Synchronous equilibria.** On \(x_1=x_2=y_1=y_2=s\), the nonzero infected-equilibrium condition becomes
\[
0=-\left(\frac25+3s\right)+(1-s)\left(\frac1{10}+6s\right)
=-6\left(s-\frac3{20}\right)\left(s-\frac13\right).
\]
Thus both \(s=3/20\) and \(s=1/3\) are exact positive synchronous equilibria for every \(w\geq0\). At \(s=1/3\), their original opinion coordinates are strictly negative. Exchange of the two community labels is a symmetry of (1).

**Four-dimensional spectrum.** Linearize at \(E\) and separate synchronous perturbations \((\delta x_1=\delta x_2,\delta y_1=\delta y_2)\) from antisynchronous perturbations \((\delta x_1=-\delta x_2,\delta y_1=-\delta y_2)\). The corresponding blocks are
\[
J_+=\begin{pmatrix}19/30&-1\\1&-1\end{pmatrix},\qquad
J_-(w)=\begin{pmatrix}1/2&-1\\1&-(1+2w)\end{pmatrix}.
\]
Their traces and determinants are
\[
\operatorname{tr}J_+=-\frac{11}{30},\quad \det J_+=\frac{11}{30},\qquad
\operatorname{tr}J_-=-\left(\frac12+2w\right),\quad \det J_-=\frac12-w.
\]
The synchronous block is Hurwitz for every \(w\). For \(w\geq0\), the antisynchronous block is Hurwitz exactly if \(w<1/2\); it has one positive and one negative real eigenvalue if \(w>1/2\). At \(w=1/2\), it has eigenvalues \(0,-3/2\); the synchronous eigenvalues still have strictly negative real parts.

At the healthy equilibrium \((0,0,0,0)\), the infection eigenvalues are \(-3/10,-1/2\), and opinion eigenvalues are \(-1,-(1+2w)\). Thus it remains locally exponentially stable.

**Critical nonlinear instability.** Introduce the mean/deviation coordinates
\[
 x_1=\frac13+u+v,\quad x_2=\frac13+u-v,\quad
 y_1=\frac13+z+h,\quad y_2=\frac13+z-h.
\]
The transformed exact equations for the infection coordinates are
\[
\begin{aligned}
\dot u&=\frac{19}{30}u-z-\frac1{10}u^2-3uz-6u^3-18uv^2+\frac1{10}v^2-3hv,\\
\dot v&=\frac12v-h-3hu-18u^2v-6v^3-3zv,
\end{aligned}
\]
while \(\dot z=u-z\) and \(\dot h=v-(1+2w)h\). At \(w=1/2\), three eigenvalues have negative real parts and the remaining simple eigenvalue is zero. Invariance and label-exchange symmetry give a local one-dimensional center manifold parametrized by \(v\), with
\[
u=-\frac{42}{11}v^2+O(v^4),\quad
z=-\frac{42}{11}v^2+O(v^4),\quad
h=\frac12v-\frac{41}{11}v^3+O(v^5).
\]
For clarity, substituting \(u=z=av^2+O(v^4)\), \(h=v/2+cv^3+O(v^5)\), and \(\dot v=bv^3+O(v^5)\) into the invariance equations gives \(-11a/30-7/5=0\), \(c=-b/4\), and \(b=-c-9a/2-6\). Hence \(a=-42/11\), \(b=164/11\), and \(c=-41/11\). The reduced flow is therefore
\[
\dot v=\frac{164}{11}v^3+O(v^5),
\]
so the critical equilibrium repels along its center direction and is nonlinearly unstable.

**Unequal equilibrium branches and their stability.** At any equilibrium sufficiently near \(E\), the opinion equations imply \(z=u\) and \(h=v/(1+2w)\). The infection equations are then equivalent to \(S(u,v^2,w)=0\) and \(vD(u,v^2,w)=0\), where
\[
\begin{aligned}
S(u,t,w)&=-\frac{11}{30}u-\frac{31}{10}u^2-6u^3-18ut+\left(\frac1{10}-\frac3{1+2w}\right)t,\\
D(u,t,w)&=\frac{2w-1}{2(1+2w)}-3u\left(1+\frac1{1+2w}\right)-18u^2-6t.
\end{aligned}
\]
At \((u,t,w)=(0,0,1/2)\), the derivative of \((S,D)\) with respect to \((u,w)\) has matrix
\[
\begin{pmatrix}-11/30&0\\-9/2&1/2\end{pmatrix},
\]
which is invertible. The analytic implicit-function theorem therefore gives one and only one local curve of nonsynchronous equilibria parametrized by \(t=v^2\geq0\), with \(u'(0)=-42/11\) and \(w'(0)=-246/11\). This proves (2), existence of exactly two label-exchanged branches for each nearby \(w<1/2\), and their absence on the opposite side.

The simple critical eigenvalue on the synchronous branch has derivative \(2/3\) with respect to \(w\). Hence, on a parameter-dependent center manifold, the odd scalar flow has expansion
\[
\dot v=\frac23\left(w-\frac12\right)v+\frac{164}{11}v^3+
O\!\left(\left|w-\frac12\right|^2|v|+\left|w-\frac12\right||v|^3+|v|^5\right).
\]
The positive cubic coefficient and negative equilibrium-branch slope imply that each nonzero branch has a positive eigenvalue \(\frac43(1/2-w)+O((1/2-w)^2)\). The three complementary eigenvalues retain negative real parts by continuity. Thus the bifurcation is subcritical and the unequal states are unstable.

## Verification

The included `verify.py` independently reconstructs the original four equations using exact rational coefficients, checks the synchronous roots, both full Jacobian blocks, the healthy spectrum, the equilibrium-reduction identities, the implicit-function branch derivatives, and the center-manifold cubic coefficient using symbolic algebra. Run `python verify.py` with Python 3 and SymPy installed. All statements involving infinitely many \(w\) and sufficiently close equilibria follow from the analytic arguments above, not from numerical sampling.

## Relationship to prior work

Samadi, Caiza, Gracy and Paré (2026), arXiv:2608.31032, introduce precisely the higher-order SIS--opinion field specialized here. Their Section IV-A proves coexistence and stability *relative to the synchronous invariant set*; they explicitly distinguish this from stability under unsynchronized perturbations. Their paper supplies the general Jacobian in Section III but does not present this sharp full-state threshold or the subcritical two-community branches. These formulas specialize the already-known model and standard \(\mathbb Z_2\)-equivariant center-manifold ideas, not a new general bifurcation theory.

She, Liu, Sundaram and Paré (2021/2022) study networked SIS with cooperative and antagonistic opinions but not this quadratic source-to-self exposure. Kiss, Iacopini, Simon and Georgiou (2023) investigate higher-order SIS contagion without the same coupled opinion feedback. Prior general epidemic equilibrium atlases and equivariant pitchfork theorems neither by themselves specify these four-dimensional coefficients nor yield the exact \(w=1/2\) transition. Exact duplication in unindexed work cannot be ruled out.

## Limitations

The threshold is proved for the displayed two-community subfamily, not for all parameter choices or networks. The result concerns local stability and local equilibrium branches, not their global basins or globally persistent asymmetric states. It does not imply that tighter opinion coupling always destabilizes epidemics. At \(w=1/2\), instability is nonlinear and cannot be inferred from the zero eigenvalue alone. At either opinion switching surface \(o_i=0\), the full model may not be smooth; the proof takes place away from both surfaces. Independent external validation has not been performed.

## References

1. S. Samadi, J. I. Caiza, S. Gracy, and P. E. Paré, *A Networked SIS Epidemic–Opinion Model with Higher-Order Interactions*, arXiv:2608.31032 (first public version 31 August 2026). https://arxiv.org/abs/2608.31032 ; full HTML https://arxiv.org/html/2608.31032 .
2. B. She, J. Liu, S. Sundaram, and P. E. Paré, *On a Network SIS Epidemic Model with Cooperative and Antagonistic Opinion Dynamics*, arXiv:2102.12834 (2021); IEEE Transactions on Control of Network Systems (2022). https://arxiv.org/abs/2102.12834 .
3. I. Z. Kiss, I. Iacopini, P. L. Simon, and N. Georgiou, *Insights from exact social contagion dynamics on networks with higher-order structures*, Journal of Complex Networks 11 (2023), cnad044. https://doi.org/10.1093/comnet/cnad044 .
4. M. Golubitsky, I. Stewart, and D. G. Schaeffer, *Singularities and Groups in Bifurcation Theory*, Volume II, Springer (1988). https://doi.org/10.1007/978-1-4612-4574-2 .
