# Exact basin ellipse and geometric escape shells in a quadratic hypergraph benchmark

## Finding

Consider the two-dimensional quadratic map given as Equation (16) in Cui–Zhang–Jardón-Kojakhmetov–Cao (2024):
\[
F(x,y)=(q(x,y),q(x,y)),\qquad q(x,y)=x^2+xy+y^2+\frac{x+y}{10}.
\]
Write \(r=4/15\). Its **entire** real basin of the attracting origin is precisely
\[
\mathcal B=\{(x,y)\in\mathbb R^2:q(x,y)<r\}
=\left\{(x,y):X^2+XY+Y^2<\frac{27}{100},\ X=x+\frac1{30},\ Y=y+\frac1{30}\right\}.
\]
The boundary ellipse consists exactly of points sent in one iteration to the nonzero fixed point \((r,r)\), while every point outside its closure escapes to \((+\infty,+\infty)\). The basin has exact area \(9\sqrt3\pi/50\), which is \(81\sqrt3\pi/128\) times the area of the origin-centered square \(\max(|x|,|y|)<4/15\) certified in the originating work. That square is nonetheless the **largest** origin-centered open sup-norm ball contained in the basin. Every invariant Borel probability measure of \(F\) is a convex combination of the point masses at \((0,0)\) and \((r,r)\).

The full escape-time law from an arbitrary concentric quadratic shell is also explicit. Fix \(H>r\), choose \((x,y)\) uniformly in area from \(\mathcal A_H=\{r<q(x,y)<H\}\), and write \(s=q(x,y)\). After the first iterate the state is \((s,s)\). Define \(N_H=\min\{n\ge1:g^{\circ n}(s)\ge H\}\), where \(g(s)=s/5+3s^2\), and let
\[
h(t)=\frac{\sqrt{1+300t}-1}{30} \quad (t\ge r).
\]
Then, for every integer \(n\ge0\),
\[
\Pr(N_H>n)=\frac{h^{\circ n}(H)-r}{H-r}.
\]
In particular, if \(G\) is geometric on \(\{1,2,\ldots\}\) with \(\Pr(G=k)=(4/9)(5/9)^{k-1}\), then the uniform quantitative thin-shell limit is
\[
d_{\mathrm{TV}}\bigl(\mathcal L(N_H),\mathcal L(G)\bigr)\le\frac{125}{48}\left(H-\frac4{15}\right).
\]
For each fixed \(H>r\), the tail is asymptotic to \(\gamma_H(5/9)^n\), with \(\gamma_H>0\) given explicitly in the proof by a convergent product. These statements concern real discrete iterations, not a continuous-time differential equation.

## Assumptions and scope

The map acts on the **whole** plane \(\mathbb R^2\); no nonnegativity of initial coordinates is required. Iteration is indexed by nonnegative integers. Area is ordinary two-dimensional Lebesgue measure. The shell distribution uses normalized Lebesgue area on the *bounded* set \(\mathcal A_H\), not a stationary measure of \(F\). Total variation uses the convention \(d_{\mathrm{TV}}(P,Q)=\sup_E|P(E)-Q(E)|\). The cutoff \(H>4/15\) is fixed for the exact formula, and tends to \(4/15\) from above for the thin-shell limit. The integer \(N_H\) counts scalar iterations **after** the first planar synchronization. The scientific object is the specific published map, not all polynomial maps on arbitrary hypergraphs.

## Proof

**1. Exact scalar reduction.** Both components of \(F\) are equal. Thus every orbit synchronizes to the diagonal after one iteration, and subsequent iterates are \((g^{\circ n}(q(x,y)),g^{\circ n}(q(x,y)))\), with \(g(s)=s/5+3s^2\). Direct completion of squares gives
\[
q(x,y)=\left(x+\frac1{30}\right)^2+\left(x+\frac1{30}\right)\left(y+\frac1{30}\right)+\left(y+\frac1{30}\right)^2-\frac1{300}.
\]
The quadratic form is positive definite (matrix eigenvalues \(3/2\) and \(1/2\)), so \(q\ge-1/300\) globally.

**2. Complete orbit classification and boundary.** The scalar fixed-point equation is
\[
g(s)-s=s(3s-4/5),
\]
with precisely the fixed points \(0\) and \(r=4/15\). For \(-1/300\le s<0\), \(g(s)=s(1/5+3s)\) lies strictly between \(s\) and zero; iteration increases to zero. For \(0<s<r\), the positive sequence \(g^{\circ n}(s)\) strictly decreases to zero. For \(s>r\), it strictly increases; if bounded it would converge to a fixed point larger than \(r\), which does not exist, so it tends to \(+\infty\). At \(s=r\) it stays at \(r\). The point \(s=0\) is fixed. Since every first-step scalar belongs to \([-1/300,\infty)\), the claimed global trichotomy follows. At the nonzero fixed point, the Jacobian is \(\left(\begin{smallmatrix}9/10&9/10\\9/10&9/10\end{smallmatrix}\right)\) with eigenvalues \(9/5\) and \(0\). Every boundary point is mapped onto this fixed point in one step.

The only recurrent points of \(F\) are its two fixed points. Indeed, all other trajectories either converge to a different point or escape. By the Poincaré recurrence theorem applied to an invariant probability measure, almost every point is recurrent; therefore every invariant Borel probability is supported on these two fixed points. Both Dirac masses are invariant, proving the full classification.

**3. Elliptic area and optimal certified box.** Level sets \(q<t\) with \(t>-1/300\) are ellipses with centered quadratic form matrix \(\left(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\right)\), determinant \(3/4\). Their area is
\[
\operatorname{area}\{q<t\}=\frac{2\pi}{\sqrt3}\left(t+\frac1{300}\right).
\]
At \(t=4/15\) this equals \(9\sqrt3\pi/50\). The square \(\max(|x|,|y|)<r\) has area \((2r)^2=64/225\); their ratio is \(81\sqrt3\pi/128\). The convex function \(q\) attains its maximum over \([-r,r]^2\) at a corner, and the largest corner value is \(q(r,r)=r\); therefore the open square is contained in the open ellipse. Any larger origin-centered sup-norm ball contains \((r,r)\), which is not in the origin's basin. This proves sharpness **within the box family**, without claiming that the square equals the global basin.

**4. Exact shell law.** The area formula in Step 3 implies that the value \(s=q(x,y)\) is exactly uniform on \((r,H)\) under normalized area on \(\mathcal A_H\). The increasing function \(g\) maps \([r,\infty)\) bijectively onto itself, with inverse \(h(t)=(\sqrt{1+300t}-1)/30\). For every \(n\ge0\), \(g^{\circ n}(s)<H\) is equivalent to \(s<h^{\circ n}(H)\). Hence
\[
\Pr(N_H>n)=\frac{h^{\circ n}(H)-r}{H-r},\qquad
\Pr(N_H=n)=\frac{h^{\circ(n-1)}(H)-h^{\circ n}(H)}{H-r}\quad (n\ge1).
\]
The unnormalized area of the corresponding exact-time shell is \(2\pi(h^{\circ(n-1)}(H)-h^{\circ n}(H))/\sqrt3\).

**5. Sharp tail and thin-shell total-variation bound.** Put \(\delta_n=h^{\circ n}(H)-r>0\), \(\delta_0=H-r\), and \(\lambda=5/9\). Since \(g(r+d)=r+(9/5)d+3d^2\), inversion yields
\[
\delta_n=\frac95\delta_{n+1}+3\delta_{n+1}^2,\quad
\delta_{n+1}=\frac{\lambda\delta_n}{1+(5/3)\delta_{n+1}},\quad 0<\delta_n\le\lambda^n\delta_0.
\]
Thus
\[
\frac{\delta_n}{\delta_0}=\lambda^n\prod_{j=1}^n\left(1+\frac53\delta_j\right)^{-1}.
\]
Because \(\sum_{j\ge1}\delta_j\le\delta_0\lambda/(1-\lambda)<\infty\), the product converges to
\[
\gamma_H=\prod_{j=1}^{\infty}\left(1+\frac53\delta_j\right)^{-1}\in(0,1).
\]
Its tail-product error is \(O_H(\lambda^n)\), proving \(\Pr(N_H>n)=\gamma_H\lambda^n(1+O_H(\lambda^n))\).

For a finite-time bound valid simultaneously for all \(n\), use \(1-\prod_j(1+a_j)^{-1}\le\sum_j a_j\) for positive \(a_j\):
\[
0\le\lambda^n-\Pr(N_H>n)
\le\lambda^n\frac53\sum_{j=1}^n\delta_j
\le \frac{25}{12}(H-r)\lambda^n.
\]
If \(S_n\) and \(S_n^*\) are the respective survival tails of \(N_H\) and \(G\), then \(S_0=S_0^*=1\) and the total-variation distance is at most \(\sum_{n\ge1}|S_n-S_n^*|\) (obtained by differencing tails to recover probability masses). The geometric sum gives
\[
d_{\mathrm{TV}}\le\frac{25}{12}(H-r)\frac{\lambda}{1-\lambda}
=\frac{125}{48}(H-r).
\]
This also bounds \(\left|\mathbb E N_H-9/4\right|\) by the same quantity, using the tail-sum formula for expectations. No finite simulation is used as a proof of any infinite statement.

## Verification

The accompanying executable `check_exact_basin.py` uses symbolic rational arithmetic to check the centered quadratic form, scalar reduction, fixed points, inverse branch, repelling multiplier, area ratio and expansion at the boundary, plus illustrative high-precision inverse iterates. Run `python check_exact_basin.py` with SymPy installed; the expected success line is `EXACT_QUADRATIC_BASIN_AND_ESCAPE_IDENTITIES_OK`. The complete global and probabilistic conclusions are proved above; the finite checks are not substituted for those proofs.

## Relationship to prior work

The source of the map is Equation (16) and Figure 2 of Cui, Zhang, Jardón-Kojakhmetov and Cao, *On discrete-time polynomial dynamical systems on hypergraphs* (arXiv:2403.03416, initial public version March 6, 2024; IEEE Control Systems Letters 8 (2024), 1078–1083). That paper proves the conservative square \(\max(|x|,|y|)<4/15\) is in the origin's attraction basin, and plots numerical examples. Its inspected sections V–VII do not identify the exact ellipse, classify all real initial states and invariant probabilities, or compute exact first-exit shells and their geometric scaling. The square itself is retained, not contradicted; it is optimal among origin-centered sup-norm balls but not as a global basin.

Can Chen, *On the Stability of Multilinear Dynamical Systems* (arXiv:2105.01041, initial public May 3, 2021) gives general tensor spectral stability criteria for homogeneous multilinear systems, not this nonhomogeneous quadratic benchmark's exact global basin or area-sampled exit statistics. Other general one-dimensional results on quadratic iterates supply techniques but do not automatically give the planar level-set geometry and the shell sampling law for this concrete example.

## Limitations

Only this displayed two-state real polynomial map is classified; no claim of a new general basin theorem for arbitrary tensor polynomial systems is made. The residence-time law uses a specified quadratic-area shell and a specified synchronized-state threshold; it is not an invariant physical measure, and its geometric limit depends on this sampling convention. The coefficient \(125/48\) is a rigorous total-variation upper bound, not claimed optimal. The proof's scalar reduction is elementary and is essential to its applicability; no hidden higher-dimensional robustness is implied. Novelty assessment is bounded by accessible indexed results and inspected primary texts; an unindexed equivalent computation may exist. Independent audit has not been performed.

## References

1. S. Cui, G. Zhang, H. Jardón-Kojakhmetov, and M. Cao, *On discrete-time polynomial dynamical systems on hypergraphs*, arXiv:2403.03416, first submitted 2024-03-06, IEEE Control Systems Letters 8 (2024), 1078–1083, DOI 10.1109/LCSYS.2024.3406597. Primary full text: https://arxiv.org/pdf/2403.03416 .
2. C. Chen, *On the Stability of Multilinear Dynamical Systems*, arXiv:2105.01041, first submitted 2021-05-03. https://arxiv.org/pdf/2105.01041 .
