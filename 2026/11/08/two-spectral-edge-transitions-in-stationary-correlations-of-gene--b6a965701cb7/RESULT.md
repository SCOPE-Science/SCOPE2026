# Two spectral-edge transitions in stationary correlations of generalized heterochaos baker maps

## Finding
For each integer \(m\ge2\) and \(0<a<1/m\), consider the generalized heterochaos baker map \(F_{m,a}\) defined below with stationary two-dimensional Lebesgue probability. Let \(Y_n\) be its center coordinate and set \(C_n=\operatorname{Cov}(Y_0,Y_n)\). Put \(p=ma\), \(q=1-ma\), and
\[
r(z)=\frac{1-\sqrt{1-4pqz^2}}{2pz},\qquad R=\frac{1}{2\sqrt{pq}},\qquad \lambda_e=2\sqrt{pq}.
\]
The branch of the square root takes value \(1\) at \(z=0\), and \(r(0)=0\). Then the **exact covariance generating function** is
\[
\boxed{\sum_{n\ge0} C_n z^n=\frac{1}{12\,[1-r(z)/m]\,[1-az-pzr(z)]}.}
\]
In particular, this determines every stationary correlation coefficient by formal expansion, even at the neutral-center parameter \(a=1/(2m)\).

There are **two spectral-edge thresholds**
\[
a_-=\frac{1}{m(m^2+1)},\qquad a_+=\frac{m}{m^2+1}=\frac1m-a_-.
\]
Write \(\lambda_L=m^{-1}+(m^2-1)a\) and \(\lambda_H=m-(m^2-1)a\). As \(n\to\infty\), the exact asymptotic alternatives are:

- If \(0<a<a_-\), then
\[
 C_n\sim \frac{1-m(m^2+1)a}{12(1-2ma)}\,\lambda_L^n.
\]
- If \(a=a_-\) or \(a=a_+\), then
\[
 C_n\sim\frac{\lambda_e^n}{6(1-m^{-2})\sqrt{2\pi n}}.
\]
- If \(a_-<a<a_+\), set \(s=\sqrt{q/p}\), \(A_+=1-s/m\), \(B_+=(1-2aR)/2\), \(A_-=1+s/m\), and \(B_-=(1+2aR)/2\). Define
\[
 K_+=\frac1{12\sqrt{2\pi}A_+B_+}\left(\frac{s}{mA_+}+\frac1{2B_+}\right),\qquad
 K_-=\frac1{12\sqrt{2\pi}A_-B_-}\left(\frac1{2B_-}-\frac{s}{mA_-}\right).
\]
Both constants are strictly positive, and
\[
 \boxed{C_n=\lambda_e^n n^{-3/2}\bigl[K_++(-1)^nK_-+O_{m,a}(n^{-1})\bigr].}
\]
- If \(a_+<a<1/m\), then
\[
 C_n\sim \frac{m[a-m(1-ma)]}{12(2ma-1)}\,\lambda_H^n.
\]
The spectral-edge transitions at \(a_-\) and \(a_+\) differ from the zero-Lyapunov transition at \(a=1/(2m)\), which lies strictly between them. There the stationary center coordinate has an explicit positive, parity-dependent \(n^{-3/2}\) leading coefficient. The statements concern this observable, not universal mixing rates for arbitrary functions.

## Assumptions and scope
Let \((X,Y)\in[0,1]^2\), with \(m\ge2\) integer and \(0<a<1/m\). The expanding base map is
\[
 \tau_a(x)=\begin{cases}(x-(i-1)a)/a,&(i-1)a\le x<ia,\;1\le i\le m,\\(x-ma)/(1-ma),&ma\le x\le1.\end{cases}
\]
Define \(F_{m,a}(x,y)=(\tau_a(x),T(x,y))\), where
\[
 T(x,y)=\begin{cases}(y+i-1)/m,&(i-1)a\le x<ia,\;1\le i\le m,\\my\bmod1,&ma\le x\le1.\end{cases}
\]
The standard half-open convention on branch boundaries is immaterial to Lebesgue correlations. The full-map definition is the generalized two-dimensional heterochaos baker family. Two-dimensional Lebesgue probability is invariant; indeed the expanding base branches have probabilities \(a,\ldots,a,q\), and their center-coordinate images preserve the uniform marginal in aggregate. All covariance expectations refer to this invariant probability, for every integer \(n\ge0\). The same center-coordinate result holds for the three-dimensional Lebesgue-preserving extension because the stable coordinate does not enter the center dynamics.

## Proof
**1. The stationary center-coordinate transition.** Under Lebesgue initialization, the successive labels of the full branches of \(\tau_a\) are independent, with probabilities \(a\) for each of the \(m\) short branches and \(q=1-ma\) for the long branch. Because each later base label is independent of the preceding labels and the initial center coordinate, the process \((Y_n)_{n\ge0}\) has the Markov Koopman operator
\[
 (Ph)(y)=a\sum_{i=0}^{m-1}h((y+i)/m)+q\,h(my\bmod1).
\]
Lebesgue measure on the center coordinate is stationary. Put \(h_k(y)=\{m^ky\}-1/2\), \(k\ge0\), so \(h_0(y)=y-1/2\) except at a null boundary. Direct substitution yields the exact identities
\[
 Ph_0=ah_0+qh_1,\qquad Ph_k=ma\,h_{k-1}+q\,h_{k+1}\quad(k\ge1).
\]
In addition, direct integration over the \(m^k\) monotonicity intervals gives
\[
 \int_0^1h_0(y)h_k(y)\,dy=\frac{1}{12m^k}.
\]
This is the critical nonstandard reduction: although the original dynamical system has a nonuniformly hyperbolic center, its complete stationary coordinate covariance reduces to a weighted nearest-neighbor walk with a distinguished boundary.

**2. Exact resolvent.** Expand \((I-zP)^{-1}h_0=\sum_{k\ge0}u_k(z)h_k\) initially as formal power series in \(z\). Each coefficient at a fixed order has finite support. Let \(r(z)\) be the zero-constant-term solution of \(r=qz+pzr^2\), where \(p=ma\). The coefficient recursion from Step 1 is
\[
 u_0=1+az\,u_0+pz\,u_1,\qquad u_k=qz\,u_{k-1}+pz\,u_{k+1}\quad(k\ge1).
\]
The unique formal solution is
\[
 u_k=\frac{r^k}{1-az-pzr}\quad(k\ge0).
\]
Taking the inner product with \(h_0\) and summing the geometric series of weights \(m^{-k}\) proves the generating function in the Finding section. This derivation is formal and therefore valid coefficientwise without a priori convergence assumptions.

**3. Singularities and sharp transitions.** The algebraic root has only square-root branch points \(z=\pm R\), where \(R=(2\sqrt{pq})^{-1}\), and satisfies \(r(R)=s=\sqrt{q/p}\) and \(r(-R)=-s\). Its first positive denominator can have an interior simple zero only at \(r(z)=m\), yielding the pole \(z_L=m/[1+(m^2-1)ma]\), and this zero lies on the physical small-root sheet precisely when \(0<a<a_-\). Its second denominator can have an interior simple zero only at \(z_H=1/[a+mq]\), and this zero lies on the small-root sheet precisely when \(a>a_+\). The two critical coincidences of these poles with \(+R\) occur at \(a=a_-\) and \(a=a_+\), respectively. For \(a_-<a<a_+\), neither positive pole is present on the physical sheet.

The covariance coefficients are nonnegative by the positive-coefficient walk expansion in Step 2. Hence a nonreal singularity of smaller modulus than a positive singularity is impossible by Pringsheim's theorem. At the positive poles, uniqueness on their modulus circle follows from strict triangle inequalities for the relevant positive-coefficient series: \(r(z)\) has positive odd powers, and the second denominator contains nonzero terms in both degrees one and two. At a branch edge, the only singularities on the circle are \(\pm R\).

For \(0<a<a_-\), a simple residue calculation at \(z_L\) gives the coefficient \([1-m(m^2+1)a]/[12(1-2ma)]\). For \(a>a_+\), the residue at \(z_H\) equals \(m[a-mq]/[12(2ma-1)]\). At either critical value \(a=a_\pm\), the corresponding pole merges with \(+R\) and produces the expansion
\[
 \sum_{n\ge0}C_nz^n\sim\frac{1}{6(1-m^{-2})\sqrt2}(1-z/R)^{-1/2}.
\]
Standard binomial coefficient asymptotics yield the stated \(n^{-1/2}\) amplitude. In the intermediate regime, expand the two analytic factors at \(\pm R\) in powers of \(\sqrt{1-z^2/R^2}\). Their first nonanalytic terms give \(K_+\) and \(K_-\) above and the remaining nonanalytic terms are \(O((1\mp z/R)^{3/2})\). Singularity transfer then yields the error \(O(\lambda_e^n n^{-5/2})\). Positivity of \(K_-\) follows, for example, from
\[
 \frac1{2B_-}-\frac{s}{mA_-}=\frac{m-1/m}{(m+s)(1+2aR)}>0.
\]
This completes all parameter regimes, including their boundaries.

## Verification
The enclosed standalone verifier builds the exact rational walk recursion independently of the formal power-series resolvent and compares the first 29 coefficients for multiple rational parameters and several dimensions. It also compares long finite sequences to the predicted pole and branch-edge asymptotics. An additional direct simulation of the original two-dimensional map at \(m=2,a=1/3\) matched its first six covariance values within sampling tolerance. These are finite cross-checks, not substitutes for the formal resolvent proof or singularity analysis.

## Relationship to prior work
Takahasi and Yamamoto introduced the generalized heterochaos baker families and investigated their entropy-maximizing invariant measures (arXiv:2209.04905, first public 2022-09-11). Saiki, Takahasi and Yorke introduced the original special map and established heterochaos and ergodicity (arXiv:1811.01009, first public 2018). Takahasi later proved exponential mixing away from the neutral-center parameter and mixing of all orders (arXiv:2307.08119, 2023), without exact observable-specific covariance rates. Takahasi and Tsujii proved the sharp \(n^{-3/2}\) correlation exponent for arbitrary Hölder observables in the neutral-center case (arXiv:2408.16618, 2024). That latter result already covers the **order of polynomial decay** at neutrality, which is not claimed as new here; the claims here are the complete explicit generating function, coefficient-level constants, parity correction, and two off-neutral spectral transitions. In particular the off-neutral pole/branch thresholds are not the Lyapunov-neutral threshold.

## Limitations
The result is specific to the centered center-coordinate observable and its stationary two-time covariance. It does not identify a sharp decay rate for every Hölder observable, establish a new central limit theorem, or classify all invariant measures. The underlying weighted-walk method is related to the transfer-operator analysis of Takahasi and Tsujii; an algebraically equivalent closed resolvent in unindexed literature remains a priority risk. At the critical parameters the displayed asymptotics are leading-order equivalences, not uniform joint limits as the parameter also approaches a transition. The exact covariance is a Lebesgue-stationary statement, not a pointwise orbit assertion.

## References
- H. Takahasi and K. Yamamoto, *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for the breakdown of entropy approachability*, arXiv:2209.04905 (submitted 2022-09-11 UTC), https://arxiv.org/abs/2209.04905.
- Y. Saiki, H. Takahasi and J. A. Yorke, *Piecewise linear maps with heterogeneous chaos*, arXiv:1811.01009, https://arxiv.org/abs/1811.01009.
- H. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119 (2023), https://arxiv.org/abs/2307.08119.
- H. Takahasi and M. Tsujii, *Polynomial rate of mixing for the heterochaos baker maps with mostly neutral center*, arXiv:2408.16618 (2024), https://arxiv.org/abs/2408.16618.
