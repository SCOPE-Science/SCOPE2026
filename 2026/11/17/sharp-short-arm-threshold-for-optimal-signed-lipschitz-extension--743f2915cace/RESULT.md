# Sharp short-arm threshold for optimal signed Lipschitz extensions of star-leaf metrics

## Finding

For every integer \(m\ge3\), real \(0<t\le1\), and real \(R\ge1\), consider a star whose \(m\) long leaf edges have length \(1\) and whose remaining short leaf edge has length \(t\). Retain only the leaves as a metric space \(X=\{x_1,\ldots,x_m,z\}\), so that \(d(x_i,x_j)=2\) for \(i\ne j\) and \(d(x_i,z)=1+t\). Adjoin a point \(o\) at distance \(R\) from each leaf. This gives a metric because \(\operatorname{diam}X=2\le2R\) and all pairwise leaf distances are at most \(2R\).

Set
\[
t_c=\frac{m-2}{m},\qquad
T_m(t)=\begin{cases}
1+t,&0<t\le t_c,\\
\dfrac{m(1+t)^2}{2(mt+1)},&t_c\le t\le1.
\end{cases}
\]
The branches agree at the boundary. The exact optimal real-linear simultaneous scalar Lipschitz extension norm is
\[
\inf_E\|E\|=\max\left\{1,\frac{T_m(t)}R\right\}.
\]

Every extension operator acts at the new point through an affine signed coefficient vector,
\[
(Ef)(o)=\sum_{i=1}^m w_i f(x_i)+s f(z),\qquad \sum_{i=1}^m w_i+s=1.
\]
For \(1\le R\le T_m(t)\), **all** optimal vectors are as follows:

* If \(0<t<t_c\), the unique minimizer is \(w_i=0\), \(s=1\) (evaluation at the short leaf).
* If \(t=t_c\), the complete minimizer set is the nondegenerate line segment \(w_i=(1-s)/m\), \(0\le s\le1\).
* If \(t_c<t\le1\), the unique minimizer is
\[
w_i=\frac{1+t}{2(mt+1)},\qquad s=\frac{mt-m+2}{2(mt+1)}.
\]

Thus the minimax center is unique on either side of a sharp arm-length threshold, but a full interval of optimizers occurs exactly at equality. Importantly, this classification allows **arbitrary signed coefficients** at the outset and proves positivity of every minimizer in the stated regime. For \(R>T_m(t)\), all minimizers are precisely the vectors satisfying the explicit inequalities \(\Phi_j\le R\) below; this set is a full-dimensional compact convex polytope of affine dimension \(m\) in its affine coefficient hyperplane.

For illustration, with \(m=4\) and \(R=1\), the transition occurs at \(t=1/2\). The optimal norms at \(t=1/4,1/2,3/4\) are respectively \(5/4,3/2,49/32\). Their optimal coefficient sets are, respectively, short-leaf evaluation, a line segment, and the unique vector with long coefficients \(7/32\) and short coefficient \(1/8\).

## Assumptions and scope

Functions and coefficients are real; \(\operatorname{Lip}(X)\) is equipped with the Lipschitz seminorm and constants are preserved. Equivalently, one may pass to Lipschitz functions vanishing at a fixed leaf. Every bounded linear extension operator on this finite one-point extension has the stated affine signed coefficient representation. The old distances are a leaf submetric of the weighted star, while the new attachment is equidistant and need not be the original star hub. The case \(t=1\) is a known equilateral endpoint, included only for continuity and checking.

For the vector \(u=(w_1,\ldots,w_m,s)\), let \(a_i=1\) for long leaves and \(a_z=t\). For each leaf \(j\), write
\[
\Phi_j(u)=a_j|1-u_j|+\sum_{k\ne j}a_k|u_k|.
\]
The exact operator norm is
\[
\|E_u\|=\max\left\{1,\frac{\max_j\Phi_j(u)}R\right\}.
\]
In particular, the operator-norm claim for all \(R\ge1\) follows from the signed minimax identity \(\inf_{\sum u_j=1}\max_j\Phi_j(u)=T_m(t)\).

## Proof

**1. Exact dual norm on the leaf metric.** For any real leaf masses \(\mu_j\) with total mass zero, the Kantorovich--Rubinstein norm is
\[
\left\|\sum_j\mu_j\delta_j\right\|_{\mathcal F(X)}=\sum_j a_j|\mu_j|.
\]
Indeed every \(1\)-Lipschitz scalar potential on the leaves extends to the star hub by choosing a real number in the intersecting intervals \([f(j)-a_j,f(j)+a_j]\). Conversely, arbitrary hub-centered leaf values in \([-a_j,a_j]\) restrict to \(1\)-Lipschitz leaf potentials. The zero-mass pairing eliminates the common hub value, so the supremum is the displayed weighted absolute sum. Apply this identity to \(\delta_j-\sum_k u_k\delta_k\) to obtain \(\Phi_j(u)\). Preserving old leaf distances gives the additional mandatory operator norm lower bound \(1\).

**2. Candidate values.** Put \(A=\sum_ka_k|u_k|\). When \(u_j\in[0,1]\) for every coordinate, \(\Phi_j=A+a_j(1-2u_j)\). For \(t\le t_c\), taking \(u_z=1\) and all long coordinates zero gives \(\max_j\Phi_j=1+t\). For \(t>t_c\), put
\[
q=\frac{1+t}{2(mt+1)},\qquad
s=\frac{mt-m+2}{2(mt+1)}.
\]
Then \(mq+s=1\), all coordinates are strictly between zero and one, and the \(m+1\) values \(\Phi_j\) coincide with \(T_m(t)=m(1+t)^2/[2(mt+1)]\). The formulas agree at \(t=t_c\).

**3. Signed global lower bound for \(t\le t_c\).** Give the \(m\) long leaves dual weights \(\lambda_i=1/m\) and the short leaf weight \(\lambda_z=0\). Since the maximum dominates this weighted average,
\[
\max_j\Phi_j(u)\ge G(u):=\sum_j a_j\bigl[\lambda_j|1-u_j|+(1-\lambda_j)|u_j|\bigr].
\]
For a long coordinate \(v\), the convex function \(m^{-1}|1-v|+(1-m^{-1})|v|\) has subgradient interval \([-1,1-2/m]\) at zero. Because \(0<t\le t_c=1-2/m\), it is at least \(1/m+tv\). Also \(t|s|\ge ts\). Therefore every signed vector of total mass one satisfies
\[
G(u)\ge1+t\sum_{i=1}^m w_i+ts=1+t.
\]
If \(t<t_c\), equality in this supporting-line inequality forces every long coefficient to vanish, and hence \(s=1\). When \(t=t_c\), equality permits precisely long coefficients in \([0,1]\) and \(s\ge0\). Since all long dual weights are positive, equality in \(\max_j\Phi_j\ge G\) also requires all long \(\Phi_i\) to be equal to the common optimum. Their formula \(A+1-2w_i\) then forces \(w_1=\cdots=w_m=(1-s)/m\), with \(0\le s\le1\). Every such vector attains the bound, proving the exact segment.

**4. Signed global lower bound and uniqueness for \(t>t_c\).** Choose dual weights equal to the positive candidate coefficients: \(\lambda_i=q\), \(\lambda_z=s\). Define
\[
c=\frac{(m-1)t}{mt+1}.
\]
For each long coordinate the slope of \(a_i[\lambda_i|1-v|+(1-\lambda_i)|v|]\) on \(0<v<1\) is \(1-2q=c\); for the short coordinate it is \(t(1-2s)=c\). As all dual weights lie strictly in \((0,1)\), the corresponding convex functions have this common supporting slope, with equality only for \(v\in[0,1]\). Summing their affine supports and using \(\sum_j u_j=1\) gives \(G(u)\ge G(u^*)=T_m(t)\), hence \(\max_j\Phi_j(u)\ge T_m(t)\). Any minimizer must have every coordinate in \([0,1]\); because every \(\lambda_j>0\), it must also have \(\Phi_j(u)=T_m(t)\) for every leaf. Equal long-leaf equations force \(w_1=\cdots=w_m=(1-s)/m\), and the short-versus-long equation is
\[
(t_c-t)+2\left(t+\frac1m\right)s=0.
\]
Its unique solution is the displayed \(s\), establishing uniqueness even among signed coefficients.

**5. Attachment-radius transition.** For any \(R\ge1\), the norm formula in Step 1 converts the established minimax value into \(\max\{1,T_m(t)/R\}\). If \(R\le T_m(t)\), minimizing the operator norm is equivalent to attaining the minimax value, so Steps 3--4 give the complete optimizer set. For \(R>T_m(t)\), optimality is equivalent to \(\Phi_j(u)\le R\) for all \(j\). Each inequality defines a closed polyhedral region; their intersection with the mass-one hyperplane is bounded because for one fixed \(j\), \(\Phi_j\le R\) bounds all coordinates in weighted absolute value. The displayed minimax vector has all \(\Phi_j\le T_m(t)<R\), so a relative open neighborhood is feasible, proving affine dimension \(m\). This completes all cases.

## Verification

The accompanying `checker.py` independently solves the unrestricted signed-coefficient linear program over auxiliary absolute-value variables for \(73\) rational profiles, with \(3\le m\le9\). It checks the exact rational formula, candidate coefficients, and coordinatewise uniqueness away from the threshold; at equality it checks the two segment endpoints and rules out asymmetric long coefficients by optimization over the optimal face. A second formulation solves the original metric Lipschitz-potential dual linear program and compares it to the star absolute-sum identity. Both checks finish successfully. These experiments are finite corroboration, not a proof of the all-parameter assertion.

Reproduce with `python checker.py` in a Python environment with NumPy and SciPy installed. The exact rational formulas and analytical dual certificates are given above and do not depend on these libraries.

## Relationship to prior work

Basso's work on absolute Lipschitz extendability and projection constants (arXiv:2104.14238, especially Lemma 2.6, Lemma 4.1 and Section 5) proves the equilateral star-center case and provides general finite-dimensional projection/linear-programming theory. At \(t=1\) and \(R=1\), our constant \(2m/(m+1)\) agrees with that classical result; **this endpoint constant is not claimed as new**. Bruè--Di Marino--Stra (arXiv:1801.07533) develop general extension operators through probability-valued random projections but do not specify the sharp one-short-arm minimax transition or all signed equality cases. The distinctive assertion here concerns \(0<t<1\): precise breakpoint \(t_c\), a short-leaf-only optimal regime, uniqueness away from a critical optimizer segment, and the attachment-radius transition.

## Limitations

This is a complete statement only for a star-leaf metric with exactly one shortened arm and \(m\) equal long arms, and for **scalar real-linear** extensions to a single equidistant added point. It does not assert an exact formula for multiple shortened arms, nonlinear or arbitrary Banach-valued extension operators, nor all weighted stars. The sharp minimax value for \(R> T_m(t)\) is established, but the fine facial and signed-coefficient structure of that full-dimensional norm-one polytope is not classified beyond its defining inequalities. A potentially equivalent earlier formulation in weighted \(\ell_1\)-simplex Chebyshev-center or transport literature remains a historical-priority risk.

## References

1. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238, first submitted 29 April 2021. https://arxiv.org/abs/2104.14238
2. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projections*, arXiv:1801.07533, first submitted 23 January 2018. https://arxiv.org/abs/1801.07533
