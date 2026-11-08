# Extinction-rate singularity transition for randomly switched two-sex quadratic maps

## Finding

Let \(\Delta_2=\{(z,x,y)\in[0,1]^3:z+x+y=1\}\). For each \(r\in(0,1)\) define the quadratic stochastic map
\[
W_r(z,x,y)=(1-2xy,\;2rxy,\;2(1-r)xy).
\]
Fix \(r_0,r_1\in(0,1)\) with \(r_0(1-r_0)\ne r_1(1-r_1)\) and an initial state \((z,x,y)\in\Delta_2\) with \(x,y>0\). At each time choose independently \(\xi_j\in\{0,1\}\), with \(\mathbb P_p(\xi_j=1)=p\), \(0<p<1\), and apply \(W_{r_{\xi_j}}\). Let \(s_n\) be the mass in the two nonempty types after \(n\) steps, and put \(c_i=2r_i(1-r_i)\), \(d_i=-\log c_i>0\) and \(a_1=-\log(2xy)>0\).

The pathwise extinction exponent exists for **every** switching sequence and has the exact representation
\[
L=\lim_{n\to\infty}\frac{-\log s_n}{2^n}
=\frac{a_1+d_0}{2}+\frac{d_1-d_0}{2}
\sum_{j=0}^{\infty}\frac{\xi_j}{2^{j+1}}.
\]
Its convergence has the uniform, deterministic sharp-range estimate
\[
\min(d_0,d_1)\le 2^nL+\log s_n\le \max(d_0,d_1),\qquad n\ge1.
\]
Thus every trajectory undergoes doubly exponential extinction with a positive rate \(L\). The law of \(L\) is a nondegenerate affine image of a dyadic Bernoulli measure. Its support is exactly
\[
I=\left[\frac{a_1+\min(d_0,d_1)}2,\;\frac{a_1+\max(d_0,d_1)}2\right],
\]
and it has no atoms. For unbiased switching \(p=1/2\), \(L\) is uniform on \(I\). For every biased \(p\ne1/2\), its law is singular continuous, with exact Hausdorff dimension
\[
\dim_H\mathcal L_p(L)=\frac{-p\log p-(1-p)\log(1-p)}{\log2}<1.
\]
For any two distinct probabilities \(p\ne q\), the extinction-exponent laws are mutually singular **although they have identical interval support**. Their first two moments are
\[
\mathbb E_pL=\frac{a_1+d_0+(d_1-d_0)p}{2},\qquad
\operatorname{Var}_p(L)=\frac{(d_1-d_0)^2p(1-p)}{12}.
\]

## Assumptions and scope

The Hausdorff dimension of a probability law here means the infimum of the Hausdorff dimensions of Borel sets of full measure; it is not the dimension of its support, which is one. The two reproductive types are numbered 1 and 2; the first coordinate represents an empty-body type. The parameters \(r_0,r_1\) are strictly between zero and one, and their reproductive coefficients \(c_0,c_1\) differ. Switching is independent and identically distributed in time with constant bias \(p\in(0,1)\). The initial state is deterministic and has both reproductive types positive. The result addresses the distribution of the **pathwise logarithmic extinction rate over the independent choices of maps**; it does not concern nonhomogeneous Markov-chain measures constructed from a single operator using several initial states.

These maps belong to the F-stochastic class of Souissi and Mukhamedov (2024), Definition 3.1. Indeed, with \(\varphi(x,y)=(x+y)^2/2\) and \(g(t)=t^2/2\), the nonempty offspring mass is \(2xy\le\varphi(x,y)\), and
\[
\varphi(W_r(z,x,y))=\frac{(2xy)^2}{2}=g(1-(W_r(z,x,y))_0).
\]
The function \(\varphi\) vanishes on the positive quadrant only at the origin; \(g\) is increasing and continuous, and \(g^{\circ n}(t)=2^{-(2^n-1)}t^{2^n}\) tends to zero for every \(t\in[0,1]\), including the endpoint \(t=1\). The maps also have the standard two-sex F-quadratic heredity interpretation: only mixed-type parental pairs can give a nonempty child, and the two nonempty child probabilities sum to one.

## Proof

**1. Exact scalar recurrence.** Given a current state, the total nonempty mass after \(W_r\) is \(2xy\), and its two proportions, conditional on being nonempty, are \(r\) and \(1-r\). In particular \(s_1=2xy>0\) independently of the first switch, whereas the type proportions after step 1 are \((r_{\xi_0},1-r_{\xi_0})\). For each \(n\ge1\), this gives
\[
s_{n+1}=c_{\xi_{n-1}}s_n^2,\qquad
 a_{n+1}=2a_n+d_{\xi_{n-1}},\quad a_n=-\log s_n.
\]
Induction yields
\[
a_n=2^{n-1}a_1+\sum_{j=0}^{n-2}2^{n-2-j}d_{\xi_j},\qquad n\ge1.
\]
Divide by \(2^n\), and sum the uniformly convergent geometric series to obtain the claimed \(L\). Because \(d_i>0\) and \(a_1>0\), its lower endpoint is positive. Multiplying the tail of the infinite sum by \(2^n\) gives
\[
2^n L-a_n=\sum_{j=n-1}^{\infty}2^{n-j-2}d_{\xi_j}.
\]
The coefficients are nonnegative and sum exactly to one, proving the uniform error bounds. Every trajectory satisfies \(s_n=\exp(-2^nL+O(1))\) with a deterministic bounded \(O(1)\) term.

**2. Distributional identification.** Put \(U=\sum_{j\ge0}2^{-j-1}\xi_j\). Independence gives the dyadic-cylinder mass
\[
\mathbb P_p\{U\text{ begins with digits }\epsilon_0\ldots\epsilon_{k-1}\}
=p^{\sum_j\epsilon_j}(1-p)^{k-\sum_j\epsilon_j}.
\]
Each exact infinite binary sequence has probability at most \(\max(p,1-p)^k\) for every prefix length \(k\), so \(U\) is nonatomic; dyadic ambiguity has probability zero. Every dyadic interval has positive mass, giving full support \([0,1]\). If \(p=1/2\), each length-\(k\) interval has probability \(2^{-k}\), which determines Lebesgue measure. Taking an affine image gives the stated support, nonatomicity and uniform law for \(L\).

**3. Biased singularity and exact dimension.** Let \(E_p\) be the set of nondyadic reals whose binary digits have limiting frequency \(p\) of ones. By the strong law of large numbers, \(\mathbb P_p(U\in E_p)=1\). Under Lebesgue measure the digit frequency is \(1/2\) almost everywhere; for \(p\ne1/2\) the measures are singular. For \(p\ne q\), the sets \(E_p,E_q\) are disjoint, yielding mutual singularity. The measures have no atoms, hence biased laws are singular continuous.

For completeness, let \(h(p)=-p\log p-(1-p)\log(1-p)\). The mass of the dyadic cylinder containing a typical \(U\), of length \(2^{-k}\), is
\[
\exp\bigl[-k h(p)+o(k)\bigr].
\]
For every \(\varepsilon>0\), a subset of positive measure has, uniformly for all sufficiently large \(k\), cylinder masses at most \(\exp[-k(h(p)-\varepsilon)]\); an interval of size at most \(2^{-k}\) meets at most two such dyadic cells, giving a Frostman lower bound on the Hausdorff dimension of every positive-measure subset of the typical set. Any full-measure set intersects such a subset in positive measure, so the lower bound holds for the Hausdorff dimension of the law. Conversely, all sufficiently typical words of length \(k\) occur in at most \(\exp[k(h(p)+\varepsilon)]\) dyadic intervals and carry mass tending to one. Covering their eventual typical set gives an upper Hausdorff bound. Letting \(\varepsilon\downarrow0\) yields the exact dimension \(h(p)/\log2\); affine similarity does not change dimension.

**4. Moments.** Independence implies \(\mathbb E_pU=p\) and \(\operatorname{Var}_p(U)=p(1-p)\sum_{j\ge0}2^{-2j-2}=p(1-p)/3\). Apply the affine relation for \(L\).

## Verification

The standalone script `verify.py` performs exact-rational tests of the map and recurrence, including both switch symbols, direct finite-step composition and the closed recurrence for each binary word through length six. It checks positivity, simplex preservation and the F-stochastic inequalities on a rational grid, tests finite-length Bernoulli-cylinder normalization, and independently checks the exponential-tail bound in high precision. It also verifies the stated moment identities algebraically. Run using `python3 verify.py` with the standard Python library; success prints `ALL CHECKS PASSED`. These finite checks are diagnostic, not proofs of asymptotic or dimension claims, which are established above.

## Relationship to prior work

Souissi and Mukhamedov (2024), DOI 10.1007/s44198-024-00172-6, introduce the relevant F-stochastic class, prove convergence to the empty-body fixed point and construct associated nonhomogeneous Markov chains. Jamilov et al. (2024), DOI 10.1002/mma.10191, study the same broad class, including absolute continuity and singularity of **associated nonhomogeneous Markov path measures**. Jamilov et al. (2023), DOI 10.1016/j.heliyon.2023.e17913, analyze deterministic and randomly selected F-quadratic sexual-system operators and almost-sure extinction. Those results do not themselves give the complete law of the random **double-exponential extinction exponent** for the concrete, independently switched two-sex family above. The dyadic Bernoulli measure, Shannon entropy, digit-frequency strong law and their general dimension theory are classical and not claimed as new. The claim is the exact connection from a natural quadratic stochastic switching model to these laws, with its precise rate and finite-time bounds.

## Limitations

The result does not cover zero initial mass in either reproductive type, identical offspring contraction coefficients, dependent or nonstationary switching, or more than two reproductive offspring types. It gives no central limit theorem for fluctuating environmental bias and no quantitative finite-sample estimator of the bias. Novelty assessment is based on inspected accessible literature and searches, not an exhaustive publication-priority certificate. Independent validation has not been performed.

## References

1. A. Souissi and F. Mukhamedov, *Nonlinear Stochastic Operators and Associated Inhomogeneous Entangled Quantum Markov Chains*, Journal of Nonlinear Mathematical Physics 31, 11 (2024), first public February 26, 2024, DOI 10.1007/s44198-024-00172-6. Full text: https://link.springer.com/article/10.1007/s44198-024-00172-6.
2. U. Jamilov, F. Mukhamedov, F. Mukhamedova and A. Souissi, *Dynamics of nonlinear stochastic operators and associated Markov measures*, Mathematical Methods in the Applied Sciences 47 (2024), 13300–13312, first public May 16, 2024, DOI 10.1002/mma.10191. Full text: https://onlinelibrary.wiley.com/doi/full/10.1002/mma.10191.
3. U. Jamilov, F. Mukhamedov and F. Mukhamedova, *Discrete time model of sexual systems*, Heliyon 9 (2023), e17913, first public July 7, 2023, DOI 10.1016/j.heliyon.2023.e17913. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC10362173/.
4. Standard background: the strong law for Bernoulli digits, dyadic cylinder coding, and the entropy formula for biased Bernoulli measures under the doubling map.
