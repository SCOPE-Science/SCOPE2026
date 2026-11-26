# A cubic-root optimal three-stage unmasking law at the ordered Ising edge

## Finding and definitions

Let a stationary symmetric binary Markov chain on \(\mathbb Z\) have one-step correlation \(\lambda\in(0,1)\), switch probability \(r/2=(1-\lambda)/2\), and correlation length \(\xi=(-\log\lambda)^{-1}\). Assign sites independently to rounds 1, 2 and 3 with probabilities \(p,(1-p)q,(1-p)(1-q)\) for \((p,q)\in[0,1]^2\). Let \(P_L\) be the path law of the **exact joint sampler** on the first \(L\) sites, and \(Q_L\) the path law of the **parallel factorized sampler**. The exact sampler draws each assigned block from the source conditional law given earlier rounds. The parallel sampler draws its sites independently from the exact single-site marginals given the earlier values. Round assignments are included in the path. Define \(B_3=\lim_{L\to\infty}D_{\rm KL}(P_L\Vert Q_L)/L\), taking this limit at fixed \(\lambda,p,q\). The direction of this divergence is exact-to-factorized, not its reverse.

As \(\lambda\uparrow1\), every global minimizer satisfies
\[
p_*\sim (2\log 2)^{-2/3}\xi^{-2/3},\qquad
q_*\sim (2\log 2)^{-1/3}\xi^{-1/3},\qquad
\min B_3\sim 3(\log 2/4)^{1/3}\xi^{-2/3}.
\]
Here \(q_*\) is the conditional second-stage reveal probability among remaining sites; the cumulative second-stage density is asymptotic to it. All logarithms are natural.

## Proof

Write \(h(x)=-x\log x-(1-x)\log(1-x)\) with the continuous conventions, \(a_k=h((1-\lambda^k)/2)\), and \(c_0=\log 2\). By the entropy chain rule and Markov property, the entropy of a spin conditional on revealed neighbors at distances \(k,\ell\) is \(a_k+a_\ell-a_{k+\ell}\), averaged over the boundary values. It is \(a_k\) with just one neighbor and \(c_0\) with neither. For independent geometric variables \(K,K'\) on \(\{1,2,\ldots\}\) of parameter \(u\in(0,1]\), set \(F_r(u)=2\mathbb E a_K-\mathbb E a_{K+K'}\) and \(F_r(0)=c_0\). This is the conditional entropy with previous reveal density \(u\). At fixed \(r>0\) it is continuous on \([0,1]\), also at zero since \(a_k\to c_0\). At positive reveal density the sum over sites of the probability a side has no boundary in the finite interval is bounded by \(2/u\), so the per-site end correction tends to zero; at zero density the entropy is exactly \(c_0\).

Under \(P_L\) the entire spin configuration has the source law independently of the reveal assignments. The mask probabilities cancel in the likelihood ratio. The exact log spin likelihood has expectation \(-c_0-(L-1)a_1\), and the factorized log likelihood contributes the negative sum of the single-site conditional entropies. With \(s=p+(1-p)q\), this gives
\[
B_3=p c_0+(1-p)qF_r(p)+(1-p)(1-q)F_r(s)-a_1.
\tag{1}
\]
Continuity gives existence of a minimum on the square.

For \(r,u\downarrow0\) and \(r/u\to0\), we claim \(F_r(u)\sim r/(2u)\). Put \(\mu=-\log\lambda\), \(\phi(z)=h((1-e^{-z})/2)\), and \(b=\mu/u\). The expansion at zero is \(\phi(z)=(z/2)(1-\log(z/2))+O(z^2(1+|\log z|))\). The variables \(uK,u(K+K')\) have uniformly exponentially bounded tails. For either variable \(Y\), on \(bY\le1\) the expected remainder is \(O(b^2(1+|\log b|))\) by bounded moments of \(Y^2(1+|\log Y|)\); the tail \(bY>1\) is exponentially small, including the leading term there. Linear terms cancel by \(\mathbb E(K+K')=2\mathbb E K\), leaving \(b/2\) times the difference of the corresponding \(Y\log Y\) moments. Geometric convergence and uniform integrability give the difference \(\mathbb E[(E+E')\log(E+E')]-2\mathbb E[E\log E]=1\) for independent unit exponentials (by the gamma recurrence). This proves the claim. If \(r/u\to t>0\) finite instead, the limit is \(\mathbb E[\phi(tE)+\phi(tE')-\phi(t(E+E'))]>0\), by strict concavity of \(\phi\) and \(\phi(0)=0\). If \(r/u\to\infty\), the limit is \(c_0\) by geometric scaling and bounded convergence. Consequently, whenever \(r,u\downarrow0\) and \(F_r(u)\to0\), necessarily \(r/u\to0\); zero-density terms cannot occur on such a subsequence.

Set \(C=(2c_0)^{-2/3}\), \(D=(2c_0)^{-1/3}\). The trial \(p=Cr^{2/3},q=Dr^{1/3}\) has cost \(O(r^{2/3})\) by (1), since \(a_1=O(r\log(1/r))=o(r^{2/3})\). At every minimizer the three nonnegative entropy summands in (1) are thus individually \(O(r^{2/3})\). In particular \(p=O(r^{2/3})\). If \(q\) were bounded below along a subsequence, \(F_r(p)=O(r^{2/3})\) would force \(r/p\to0\) and then \(F_r(p)\gtrsim r^{1/3}\), a contradiction. Thus \(q\to0\), so the last summand forces \(F_r(s)=O(r^{2/3})\), \(r/s\to0\), and \(s\gtrsim r^{1/3}\). Therefore \(q\gtrsim r^{1/3}\) and \(q\gg p\). The middle summand gives \(F_r(p)=O(r^{1/3})\), hence \(r/p\to0\) and \(p\gtrsim qr^{1/3}\). Together these yield \(p\asymp r^{2/3}\), \(q\asymp r^{1/3}\) for every minimizer, with uniform upper and lower bounds.

For \(p=cr^{2/3},q=dr^{1/3}\) on compact positive ranges, \(B_3/r^{2/3}\to c c_0+d/(2c)+1/(2d)\) uniformly by the sequential asymptotic just proved. The product of its three positive terms is \(c_0/4\); equality in AM–GM requires \(d^2=c\) and \(d=2c^2 c_0\), giving uniquely \((C,D)\). By compactness, every subsequential limit of scaled exact minimizers equals this pair. The trial attains the limit and \(r\xi\to1\), proving the stated constants.

## Verification

The accompanying `verify_three_round.py` computes the expected log likelihood ratio with the source (exact-sampler) weights, as required by this definition. It compares finite path sums to finite-chain entropy formulas and numerically checks the asymptotic constants; the proof of the infinite-volume and strong-order limits is analytic.

## Comparison and limitations

Baule, *Masked diffusion as random sequential adsorption*, arXiv:2611.07845v1, §§I–II and IV, supplies exact finite-round identities for this objective, and §V treats many rounds at fixed source. The three-round global optimization in the singular strong-order limit uses a separate geometric-gap asymptotic and compactness for all minimizers. Broader information-profile and discretization formulations appear in Lavenant and Zanella (arXiv:2510.25544) and Wainwright (arXiv:2608.13520). The subsequent all-fixed-round corpus result, *Universal fixed-round geometric unmasking law in a strongly correlated Ising chain*, explicitly cites this three-round claim and contains it as its \(m=3\) specialization. The present proof uses the direct nearest-neighbor single-site entropy instead of its positive pair-information series. No priority assertion beyond the examined work is made.

The result concerns paths with Bernoulli reveal assignments and exact single-site conditionals; it is not a result for final-output KL, adaptive masking, or a finite chain in a simultaneous strong-order limit. No assertion is made here about uniqueness at finite correlation, or uniformity in the number of rounds.
