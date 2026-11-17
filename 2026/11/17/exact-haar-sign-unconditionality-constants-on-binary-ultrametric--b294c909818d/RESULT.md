# Exact Haar sign-unconditionality constants on binary ultrametric Lipschitz spaces

## Finding
Let \(d\geq1\) and let \(r_0>r_1>\cdots>r_{d-1}>0\). On the binary leaves \(X_d=\{0,1\}^d\), give distinct leaves \(x,y\) distance \(r_k\) when their first differing coordinate has index \(k\), starting from zero. Let \(T_\varepsilon\) be an independent real sign change of every nonconstant, uniformly normalized Haar coefficient on this binary tree. Its operator norm is measured using the real Lipschitz seminorm, modulo constants. Set \(r_d=0\) and
\[
 F_s=\frac{2s}{3}+\frac59+\frac49\left(-\frac12\right)^s\quad(s\geq0).
\]
Then the **sharp sign-unconditionality constant** is
\[
 \boxed{U_d(r)=\max_{0\leq k<d}\frac1{r_k}\sum_{s=0}^{d-k-1}(r_{k+s}-r_{k+s+1})F_s.}\tag{1}
\]
Equivalently, with an empty sum interpreted as zero,
\[
 \boxed{U_d(r)=1+\max_{0\leq k<d}\frac{2}{3r_k}\sum_{s=2}^{d-k-1}r_{k+s}\left[1-\left(-\frac12\right)^{s-1}\right].}\tag{2}
\]
For each fixed divergence depth \(k\), the corresponding expression inside the maximum is itself the exact sharp amplification over pairs of leaves with that first divergence. Every bound is attained by a sign selection and a Lipschitz function on the finite set.

For geometric radii \(r_k=\rho^k\), \(0<\rho<1\), the maximum is at \(k=0\), and for \(d\geq2\)
\[
 \boxed{U_d(\rho)=1+\frac{2\rho^2}{3}\left[\frac{1-\rho^{d-2}}{1-\rho}+\frac{1-(-\rho/2)^{d-2}}{\rho+2}\right].}\tag{3}
\]
Also \(U_1=1\). The uniform infinite-depth constant is
\[
 \boxed{U_\infty(\rho)=1+\frac{2\rho^2}{(1-\rho)(\rho+2)}.}\tag{4}
\]
In particular, the first deviation from unconditionality one occurs at depth three, and the geometric small-ratio excess is quadratic, \(U_\infty(\rho)-1\sim\rho^2\) as \(\rho\downarrow0\).

For any positive strictly decreasing sequence \(r_k\downarrow0\), equip \(X_\infty=\{0,1\}^{\mathbb N}\) with the corresponding first-disagreement ultrametric. On the closure in Lipschitz seminorm of finite cylinder functions (the real little-Lipschitz space modulo constants), the canonical level-ordered Haar wavelets are unconditional **if and only if**
\[
 \boxed{\sup_{k\geq0}\frac1{r_k}\sum_{s=2}^{\infty}r_{k+s}<\infty,}\tag{5}
\]
which is equivalent to the existence of integers \(L\geq1\) and a number \(0<\theta<1\) such that \(r_{k+L}\leq\theta r_k\) for all \(k\). With infinity permitted, their exact uniform sign bound is
\[
 \boxed{U_\infty(r)=1+\sup_{k\geq0}\frac2{3r_k}\sum_{s=2}^{\infty}r_{k+s}\left[1-\left(-\frac12\right)^{s-1}\right].}\tag{6}
\]

## Assumptions and scope
All values and coefficients are real. For a binary prefix \(v\) of length \(|v|<d\), let \([v]\) be its cylinder and define \(h_v=2^{|v|/2}(\mathbf1_{[v0]}-\mathbf1_{[v1]})\). These form an orthonormal Haar system for uniform counting probability on \(X_d\). The operator is
\[
 T_\varepsilon f=\mathbb Ef+\sum_{|v|<d}\varepsilon_v\langle f,h_v\rangle h_v,
 \qquad \varepsilon_v\in\{-1,1\}.
\]
Changing the constant coefficient is immaterial to the Lipschitz quotient. The seminorm is \(\|f\|_{\mathrm{Lip}}=\max_{x\ne y}|f(x)-f(y)|/d_r(x,y)\). The notation \(\|T_\varepsilon\|_{\mathrm{Lip}}\) means its induced norm on functions modulo constants. For \(X_\infty\), the little-Lipschitz space consists of Lipschitz functions \(f\) with \(\sup_{0<d_r(x,y)\leq r_n}|f(x)-f(y)|/d_r(x,y)\to0\), modulo constants. Its finite-cylinder subspace is dense in this norm, as shown below.

## Proof
**1. An exact transport identity.** Embed the finite ultrametric as leaves of a rooted metric binary tree. The edges leading to vertices at depth \(t\), for \(1\leq t\leq d\), have length \(b_t=(r_{t-1}-r_t)/2\), with \(r_d=0\). The length of the path between two leaves first diverging at \(k\) is \(2\sum_{t=k+1}^d b_t=r_k\). For a signed leaf measure \(\mu\) with total mass zero, the Kantorovich--Rubinstein norm is exactly
\[
 \|\mu\|_{\mathrm{KR}}=\sum_{t=1}^d b_t\sum_{|v|=t}|\mu([v])|.\tag{7}
\]
Indeed, for every edge its lower subtree carries the signed total mass \(\mu([v])\), giving the upper bound by telescoping Lipschitz gradients. Conversely, prescribe a gradient of the maximizing sign independently on every edge. Its leaf restriction is 1-Lipschitz for the tree metric and achieves the upper bound. This is the finite-tree transport identity compatible with the general tree-space framework.

**2. Duality reduces the problem to leaf pairs.** The Lipschitz norm is determined by normalized differences \(\delta_x-\delta_y\). For each fixed \(\varepsilon\), since the Haar transform is symmetric in uniform counting measure, its adjoint sends this molecule to the signed difference of its two kernel rows. Hence
\[
 \|T_\varepsilon\|_{\mathrm{Lip}}=
 \max_{x\ne y}\frac{\|T_\varepsilon^*(\delta_x-\delta_y)\|_{\mathrm{KR}}}{d_r(x,y)}.\tag{8}
\]
This is finite-dimensional duality; the suprema are maxima.

**3. Signed row masses obey a scalar Bellman equation.** In a normalized binary Haar kernel row, a subtree of current mass \(m\in[-1,1]\) splits under its node sign \(e\in\{-1,1\}\) into the followed child of mass \((m+e)/2\) and its sibling of mass \((m-e)/2\). Let \(W_s(m)\) be the greatest total absolute mass at level \(s\) below this subtree when all signs along the followed path are free. The other child subtrees carry constant density for that row and require no further choices. Therefore
\[
 W_0(m)=|m|,\qquad
 W_s(m)=\max_{e=\pm1}\left\{\frac{|m-e|}{2}+W_{s-1}\left(\frac{m+e}{2}\right)\right\}.\tag{9}
\]
Induction gives \(W_s(m)=A_s+B_s|m|\) for \(|m|\leq1\), where
\[
 A_0=0,\ B_0=1,\qquad
 A_s=A_{s-1}+\frac{1+B_{s-1}}2,\quad
 B_s=\frac{1-B_{s-1}}2.
\]
The maximizing choice for nonzero \(m\) opposes its sign, except for possible ties at the final stage. Solving these scalar recurrences gives
\[
 B_s=\frac13+\frac23\left(-\frac12\right)^s,
 \quad A_s=\frac{2s}{3}+\frac29\left[1-\left(-\frac12\right)^s\right].
\]
In particular \(W_s(1)=F_s\), and the greedy signs optimize **all descendant levels simultaneously**. This row identity is not, by itself, the novelty asserted here: it is the previously established sharp signed \(L^\infty\) Haar row formula.

**4. Two disjoint rows after the first divergence.** Fix distinct leaves \(x,y\), first diverging at level \(k\). Their signed kernel rows have identical masses above their last common ancestor. At depth \(k+1\), the kernel-row difference has masses \(+e\) and \(-e\) on the two child cylinders of that ancestor, for the sign \(e\) at that node. In each child cylinder, all subsequent nonconstant terms come from the unique evaluation leaf belonging to it. By step 3, at depth \(t=k+1+s\), the sum of absolute masses of the kernel-row difference is at most \(2F_s\). The signs in the two disjoint child branches can be selected independently; the nested greedy patterns in step 3 attain equality simultaneously for **every** \(s\geq0\). Thus the exact best value for a pair first diverging at \(k\), by (7), is
\[
 \frac1{r_k}\sum_{t=k+1}^d\frac{r_{t-1}-r_t}2\,2F_{t-k-1},
\]
which is the \(k\)-term in (1). Maximizing over \(k\) proves (1), with actual finite-dimensional norming functions supplied by the edge-gradient construction in step 1.

**5. Positive tail formula and geometric specialization.** We have \(F_0=F_1=1\), and for \(s\geq2\)
\[
 F_s-F_{s-1}=\frac23\left[1-\left(-\frac12\right)^{s-1}\right].\tag{10}
\]
Summation by parts in (1), using \(r_d=0\), gives (2). Every summand in (2) is positive; hence with geometric radii the longest available suffix is optimal (\(k=0\)). Summing the two geometric series gives (3). Its limit is (4), including the stated small-ratio asymptotics.

**6. Infinite Cantor limit and unconditionality.** Let \(P_n\) be conditional expectation onto cylinders of depth \(n\). Coupling the same tail below two different depth-\(n\) prefixes shows \(\|P_n\|_{\mathrm{Lip}}\leq1\). For a little-Lipschitz function \(f\), set \(\omega_n=\sup_{0<d_r(x,y)\leq r_n}|f(x)-f(y)|/d_r(x,y)\to0\). Within one depth-\(n\) cylinder, \(f-P_nf\) has Lipschitz constant at most \(\omega_n\); between different cylinders its difference quotient is at most \(2\omega_n\). Thus \(P_nf\to f\) in Lipschitz seminorm, proving cylinder density. For a partial sum that cuts through one Haar level, the selected same-level wavelets form a function constant on each child cylinder, of magnitude at most \(r_n\|f\|_{\mathrm{Lip}}/2\); its Lipschitz norm is at most \(\|f\|_{\mathrm{Lip}}\). Hence any fixed level ordering gives uniformly bounded initial partial-sum operators (at most two), and the Haar system is a Schauder basis of the little-Lipschitz quotient.

The finite-depth sign norms are exactly (2); their increasing supremum over finite cylinder subspaces equals (6), with infinity permitted. By (10), the positive factors multiplying \(r_{k+s}\) for \(s\geq2\) lie between \(1/2\) and \(1\), so uniform boundedness is equivalent to (5). If \(B=\sup_k\sum_{s\geq2}r_{k+s}/r_k<\infty\), monotonicity implies \(Lr_{k+L+1}\leq\sum_{s=2}^{L+1}r_{k+s}\leq Br_k\); choosing \(L>2B\) gives a uniform fixed-step contraction. Conversely, if \(r_{k+L}\leq\theta r_k\), partition the tail into blocks of length \(L\) to bound the normalized sum uniformly by \(L/(1-\theta)\). This proves the iff claim and the sharp infinite constants.

## Verification
The standalone `check_ultrametric_haar.py` performs exact rational calculations. It independently reconstructs finite Haar kernel rows and their signed tree-flow transportation norms, then exhausts all sign choices and distinct leaf pairs for three different depth-three radius profiles and a depth-two profile. For each divergence depth it compares the actual maximum with (1), not merely the overall maximum. Separately it enumerates all binary path sign configurations through depth eight to check \(F_s\). The exact observed diagnostics are reproduced by running `python check_ultrametric_haar.py` with Python 3. No finite test is used in place of the analytical proof for arbitrary depth or the infinite Cantor case.

## Relationship to prior work
Godard's tree-metric free-space theory supports the transportation representation (7), but it does not give the Haar multiplier profile (1) or the radius-dependent unconditionality criterion (5). Cúth and Doucha established monotone Schauder bases and \(\ell_1\)-isomorphism for free spaces over separable ultrametrics; their construction is not this precise binary Haar basis or its sharp Lipschitz sign constants. General Haar-martingale inequalities, including Osękowski's sharp inequalities for other target norms, do not imply (1). A previously established signed Haar row identity gives the \(F_s\) term; **the present claim is the exact integration of those rows against ultrametric transport levels, the full arbitrary-radius profile, and its scale-dependent unconditionality theorem**. Previously obtained exact constants for nearest-predecessor bases on *comb* ultrametrics concern a different metric and basis; their qualitative block-decay criterion alone does not imply the weighted formula for balanced binary trees. Likewise, coordinate-truncation projections for *weighted Hamming* Cantor metrics have a different norm and metric structure.

## Limitations
The finite formula is specific to uniform binary Haar systems with distance determined only by first divergence level; it does not address asymmetric branching probabilities, nonbinary trees, arbitrary pruned trees or arbitrary ultrametrics. The infinite assertion concerns the separable little-Lipschitz quotient, not the generally larger full Lipschitz space, in which finite cylinders need not be dense in norm. The bound is for independent **sign** changes, not 0/1 suppression or general bounded coefficients. Only a self-review has been carried out; priority relative to incompletely indexed older Haar multiplier and ultrametric literature remains an acknowledged bibliographic risk.

## References
- A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178v1, first public 2009-04-21, especially Section 3. https://arxiv.org/abs/0904.3178
- M. Cúth and M. Doucha, *Lipschitz-free spaces over ultrametric spaces*, arXiv:1411.2434v1, first public 2014-11-10, particularly the retractional-basis results. https://arxiv.org/abs/1411.2434
- A. Osękowski, *Sharp Inequalities for the Haar System and Fourier Multipliers*, 2013, for comparison of different Haar-operator norms. https://doi.org/10.1155/2013/646012
