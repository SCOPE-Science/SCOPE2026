# Global selection on the singular four-species cycle and its sharp entropy window

## Finding

Consider the four-species competitive Lotka–Volterra flow
\[
\begin{aligned}
\dot u&=u(1-u-a v),\\
\dot v&=v(1-v-a w),\\
\dot w&=w(1-w-(1-\varepsilon)a u-\varepsilon a z),\\
\dot z&=z(1-z-a u),
\end{aligned}
\]
with \(a>1\) and the critical participation weight
\[
\varepsilon=\frac{a^2-a+1}{a^3}.
\]
Let \(\rho=1.574743073887\ldots\) denote the unique real zero of
\[
p(a)=a^3-a^2+a-3.
\]
For every \(1<a<\rho\) and **every** initial condition \((u_0,v_0,w_0,z_0)\in(0,\infty)^4\), the forward solution exists globally and converges exponentially in time to exactly one interior equilibrium. Writing \(c=(1+a)^{-1}\) and
\[
q=\left(-\frac1a,\frac1{a^2},-\frac1{a^3},1\right),
\]
the limit is \(c(1,1,1,1)+s_*q\), with \(-c<s_*<ac\). It is characterized uniquely by
\[
\begin{split}
H(c(1,1,1,1)+s_*q)&=H(u_0,v_0,w_0,z_0),\\
H(u,v,w,z)&=-\log u+a\log v-a^2\log w+(a^2-a+1)\log z.
\end{split}
\]
In particular, every strictly positive trajectory in this parameter range persists uniformly away from extinction and admits no non-equilibrium recurrent limit set.

There is also a sharp, structural certificate theorem. Put
\[
C_a=\begin{pmatrix}
1&a&0&0\\0&1&a&0\\a(1-\varepsilon)&0&1&a\varepsilon\\a&0&0&1
\end{pmatrix}.
\]
There **exists** a strictly positive diagonal matrix \(D\) satisfying the matrix inequality
\[
DC_a+C_a^{\mathsf T}D\succeq0
\]
if and only if \(1<a\le\rho\). Whenever such \(D\) exists, it is unique up to a positive scalar multiple and equals
\[
D_a=\operatorname{diag}(a,a^3,a^5,a^2-a+1)
\]
up to scaling. The threshold \(\rho\) is sharp for this diagonal relative-entropy method; it is **not** asserted to be a threshold for global convergence of the underlying flow.

## Assumptions and scope

The state space is the strictly positive orthant and time is continuous. The only variable coefficient is \(a>1\), with \(\varepsilon\) fixed to the singular curve stated above; indeed \(0<\varepsilon<1\). The global convergence and exponential-rate conclusions are proved for the open interval \(1<a<\rho\). The certificate classification holds for the entire range \(a>1\), including its endpoint at \(a=\rho\). A rate constant may depend on \(a\) and the positive initial condition; no uniform rate is claimed as \(a\uparrow\rho\) or as initial coordinates approach zero.

## Proof

**1. Equilibrium kernel and conserved level.** Write \(x=(u,v,w,z)^{\mathsf T}\) and \(\mathbf 1=(1,1,1,1)^{\mathsf T}\). The flow is
\[
\dot x=\operatorname{diag}(x)(\mathbf 1-C_a x).
\]
Direct multiplication gives \(C_a\mathbf 1=(1+a)\mathbf 1\), \(C_a q=0\), and
\[
\ell^{\mathsf T}C_a=0,\quad
\ell=(-1,a,-a^2,a^2-a+1)^{\mathsf T},\quad
\ell^{\mathsf T}\mathbf1=0.
\]
The leading \(3\times3\) minor of \(C_a\) equals \(a(a^2-a+1)>0\), while \(C_aq=0\); hence the rank is three, and all interior equilibria are precisely
\[
L=\{c\mathbf1+sq:-c<s<ac\}.
\]
Moreover, \(H(x)=\ell^{\mathsf T}\log x\) obeys
\(\dot H=\ell^{\mathsf T}(\mathbf1-C_a x)=0\). Both the equilibrium line and a conserved monomial on it were identified in the source work; they are used here, not claimed as independent discoveries.

**2. Exact entropy matrix.** Define
\[
D_a=\operatorname{diag}(a,a^3,a^5,a^2-a+1),\qquad
S_a=\frac{D_aC_a+C_a^{\mathsf T}D_a}{2}.
\]
Then \(D_aq=\ell\), so \(S_aq=0\). The upper-left \(3\times3\) principal matrix \(B_a\) has leading principal minors
\[
\Delta_1=a,\qquad \Delta_2=\frac{3a^4}{4},\qquad
\Delta_3=\frac{a^{10}(a^2-a+1)(3-a^3+a^2-a)}4.
\]
Since \(p'(a)=3a^2-2a+1>0\), \(B_a\) is positive definite exactly for \(1<a<\rho\), and positive semidefinite of rank two at \(a=\rho\). Because \(S_aq=0\) with fourth component \(q_4=1\), the full \(S_a\) is positive semidefinite with kernel \(\mathbb Rq\) exactly when \(1<a<\rho\). At equality its kernel has dimension two.

**3. Sharpness among all positive diagonal scalings.** Let \(\widetilde D>0\) be diagonal and assume \(\widetilde S=(\widetilde DC_a+C_a^{\mathsf T}\widetilde D)/2\succeq0\). Since \(C_aq=0\), one has \(q^{\mathsf T}\widetilde S q=0\). For a positive semidefinite symmetric matrix this forces \(\widetilde S q=0\), hence \(C_a^{\mathsf T}\widetilde Dq=0\). The left kernel of \(C_a\) is \(\mathbb R\ell\); as each entry of \(q\) and corresponding entry of \(\ell\) have the same sign, \(\widetilde Dq=\kappa\ell\) for some \(\kappa>0\). Therefore \(\widetilde D=\kappa D_a\). The displayed determinant \(\Delta_3\) is negative for \(a>\rho\), excluding positive semidefiniteness. This proves both uniqueness and the sharp certificate cutoff.

**4. Global convergence.** Fix the strictly positive equilibrium \(\bar x=c\mathbf1\) and consider the proper relative entropy
\[
V_{\bar x}(x)=\sum_{i=1}^4 (D_a)_{ii}\left[x_i-\bar x_i-\bar x_i\log\left(\frac{x_i}{\bar x_i}\right)\right].
\]
For \(1<a<\rho\) and every positive solution,
\[
\dot V_{\bar x}=-(x-\bar x)^{\mathsf T}S_a(x-\bar x)\le0.
\]
The positive sublevel sets of \(V_{\bar x}\) are compact subsets of \((0,\infty)^4\), because every scalar summand diverges at both zero and infinity. Thus all positive solutions exist for all forward times and remain in a compact subset of the positive orthant. For \(1<a<\rho\), equality in \(\dot V_{\bar x}=0\) holds precisely when \(x-\bar x\in\mathbb Rq\), which is exactly the equilibrium line \(L\). LaSalle's invariance argument therefore places every omega-limit set inside \(L\).

Along \(L\), the conserved level is strictly increasing:
\[
\frac{d}{ds}H(c\mathbf1+sq)
=\sum_{i=1}^4\frac{(D_a)_{ii}q_i^2}{c+sq_i}>0.
\]
It tends to \(-\infty\) as \(s\downarrow-c\), where the fourth coordinate vanishes, and to \(+\infty\) as \(s\uparrow ac\), where the first coordinate vanishes. Consequently each level of \(H\) meets \(L\) in exactly one point \(x_*\). Every omega-limit set is this singleton, proving convergence for each strictly positive initial state.

**5. Exponential rate for each orbit.** The conserved level \(H=H(x_*)\) is transverse to the equilibrium line at \(x_*\), because \(\nabla H(x_*)\cdot q>0\). On this level, sufficiently close to \(x_*\), the orthogonal projection of \(x-x_*\) to \(q^\perp\) bounds its full norm below up to a fixed positive constant. Since \(S_a\) is positive definite on \(q^\perp\), the entropy \(V_{x_*}\), defined by replacing \(\bar x\) with \(x_*\), satisfies \(\dot V_{x_*}\le-\gamma V_{x_*}\) near \(x_*\), for some \(\gamma>0\). The already proved convergence eventually enters this neighborhood; local quadratic bounds on \(V_{x_*}\) then give \(\|x(t)-x_*\|\le M e^{-\gamma'(t-t_0)}\) for sufficiently large \(t\), with positive constants depending on the orbit.

## Verification

The standalone `verify.py` evaluates the exact kernel, left-kernel, conservation, diagonal multiplier and minor identities symbolically, locates \(\rho\) numerically and checks representative spectra on either side. Four positive initial conditions were integrated for different parameter choices below \(\rho\), with predicted conserved-level equilibria obtained independently by scalar root finding. The largest observed final-state discrepancy was below \(10^{-11}\), while conservation residuals were below \(5\cdot10^{-12}\). These finite calculations are reproducibility tests, not substitutes for the proofs of global convergence or optimality of the certificate.

## Relationship to prior work

Murdie, Abrams, Bayliss and Volpert [1] introduced precisely this parity-transition four-species model. Their Section 3 and Appendix D identify the singular coexistence line and a conserved quantity and discuss local stability with shift. These ingredients are prior work. The present result gives a separate all-positive-initial-condition global theorem on an explicit nontrivial parameter interval, a proof of exponential selection to a uniquely determined point on the line, and the exact cutoff and uniqueness of all positive diagonal entropy multipliers. Their reported local stability and shift discussion does not itself supply these global bounds or the sharp entropy-multiplier classification.

General Volterra–Lyapunov diagonal-stability and relative-entropy techniques are classical; see [2]. Their standard strict-definiteness theorems do not directly handle the singular coexistence continuum: here the symmetric matrix necessarily has a neutral direction and requires the explicit rank-deficient calculation and a conserved transverse level. The result neither asserts that this general technique is new nor claims dynamics become unstable when its diagonal certificate fails.

## Limitations

At \(a=\rho\) the entropy matrix has a two-dimensional kernel; the argument above does not establish global convergence or exponential selection there. For \(a>\rho\), failure of every diagonal certificate of the stated form says nothing by itself about convergence or coexistence. The theorem assumes all four initial species are present; it does not classify boundary initial data or perturbations of the singular participation weight. No claim is made about stochastic models, spatial diffusion, or a complete bifurcation diagram. Historical priority is assessed only against accessible literature and indexed findings; independent verification is not yet available.

## References

[1] T. M. Murdie, D. M. Abrams, A. Bayliss, V. A. Volpert, *Effect of Parity in Cyclically Competing Communities*, arXiv:2609.28833 (first submitted 2026-09-23), https://arxiv.org/abs/2609.28833 .

[2] W. E. Hong and R. L. Pego, *Exclusion and multiplicity for stable communities in Lotka–Volterra systems*, arXiv:2102.00611 (first submitted 2021-02-01), https://arxiv.org/abs/2102.00611 . The source discusses standard Volterra–Lyapunov matrix criteria and relative-entropy attraction arguments.
