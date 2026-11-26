# A Gaussian-smoothed logarithmic spike in two-order one-point type spectra

## Finding
Let \(\mathcal R\) be the countable homogeneous structure of two independent linear orders. For each \(n\ge1\), let a finite, individually named \(n\)-point parameter structure be chosen uniformly from the \(n!\) possible permutations. Let \(H_{\pi,n}(k)\) count complete nonalgebraic singleton types whose insertion reverses the relative order of precisely \(k\) named parameters between the two orders. Write \(M_{n,k}=\mathbb E_\pi H_{\pi,n}(k)\), for \(0\le k\le n\).

The claim is the local asymptotic at the logarithmic singularity of the known macroscopic degree law. For every fixed real \(s\), set \(k_n=\lfloor n/2+s\sqrt n\rfloor\), defined within \(\{0,\ldots,n\}\) for all sufficiently large \(n\). With \(Z\sim N(0,1)\),
\[
 \frac{M_{n,k_n}}{n+1}-\frac12\log n
 \longrightarrow -\mathbb E\log|Z+2s|.
\]
In particular, with Euler's constant \(\gamma\),
\[
 M_{n,\lfloor n/2\rfloor}=(n+1)\left(\frac12\log n+\frac{\gamma+\log2}{2}+o(1)\right).
\]
For comparison, away from the singularity, if \(k_n/n\to t\in(0,1)\setminus\{1/2\}\), the same finite representation immediately gives
\[
 M_{n,k_n}/(n+1)\to -\log|1-2t|.
\]
Thus the expected **exact-degree** type spectrum has an order-\(n\log n\) central peak, with a nonconstant Gaussian-smoothed profile on the \(\sqrt n\) window, whereas its bulk coefficients are order \(n\). This is a statement about expectation over parameter permutations, not concentration of any single realized histogram.

## Assumptions and scope
A named \(n\)-point two-order structure is represented by \(\pi\in S_n\), where the first order is \(1<\cdots<n\) and the second ranks element \(a\) at \(\pi(a)\). An injective, nonparameter one-point type is uniquely specified by two insertion gap indices \((i,j)\in\{0,\ldots,n\}^2\): exactly \(i\) named elements are earlier in the first order and \(j\) are earlier in the second. Every such pair extends in the homogeneous two-order structure. Define
\[
 A_\pi(i,j)=|\{a\le i:\pi(a)\le j\}|,
 \qquad d_\pi(i,j)=i+j-2A_\pi(i,j),
\]
and \(H_{\pi,n}(k)=|\{(i,j):d_\pi(i,j)=k\}|\). The statistic counts named elements that lie on opposite sides of the new element in the two orders, equivalently its degree in the induced permutation inversion graph on adding the element.

## Proof
**1. Exact insertion law.** Take \(n+1\) independent points with independent continuous uniform coordinates in the unit square; designate one point as new. Their two coordinate rankings define a uniform permutation, and the restriction to the old \(n\) points gives a uniform \(\pi\). The ranks of the designated point in the two orders are independent uniform insertion gaps \((i,j)\), independent of \(\pi\). Conditional on its coordinates \((U,V)=(u,v)\), each old point disagrees with it in exactly one of the two orders independently with probability
\[
 p(u,v)=u(1-v)+(1-u)v=u+v-2uv.
\]
Hence the disagreement count \(D\) conditional on \((U,V)\) is \(\operatorname{Bin}(n,p(U,V))\), and \(\Pr(D=k)=M_{n,k}/(n+1)^2\). This conditional-binomial law is an immediate specialization of the independent-point permutation model and inversion kernel in [1, §§2.3–2.4, Eq. (2.8)], after distinguishing one vertex and translating degrees to types.

**2. Finite representation used in the proof.** Corollary 2.2 of [1] gives the mixing density \(f(p)=-\log|1-2p|\); it also follows by writing \(1-2p(U,V)=(1-2U)(1-2V)\), a product of independent uniform variables on \([-1,1]\). Conditioning on \(p\) in Step 1 and normalizing a beta integral give, for \(B_{n,k}\sim\operatorname{Beta}(k+1,n-k+1)\),
\[
 M_{n,k}=(n+1)\mathbb E[-\log|1-2B_{n,k}|]
 =(n+1)^2\binom nk\int_0^1 p^k(1-p)^{n-k}[-\log|1-2p|] \,dp.
\]
This convergent exact formula is used as a direct consequence of prior ingredients, not as a separate originality claim.

For an explicit rational certificate, set \(c_r=[x^r](1+x)^k(1-x)^{n-k}\). With \(x=2p-1\), use parity and \(\int_0^1 x^{2r}(-\log x)\,dx=1/(2r+1)^2\) to obtain
\[
 M_{n,k}=\frac{(n+1)^2\binom nk}{2^n}
 \sum_{r=0}^{\lfloor n/2\rfloor}\frac{c_{2r}}{(2r+1)^2}.
\]
This also proves rationality. Reflection \(p\mapsto1-p\) proves symmetry in \(k\), and summing the binomial probabilities proves the total.

**3. Bulk.** If \(k/n\to t\in(0,1)\), the beta law concentrates at \(t\) with variance \(O(1/n)\). For \(t\ne1/2\), take a fixed closed neighborhood of \(1/2\) disjoint from \(t\). The beta density there is at most its maximum \(O(\sqrt n)\) times \(e^{-cn}\) for some \(c>0\): the exponent divided by \(n\) is \((k/n)\log p+(1-k/n)\log(1-p)\), whose maximum is strictly higher at \(p=k/n\) than on that neighborhood. The logarithm is integrable there and bounded off that neighborhood. This gives the bulk limit.

**4. Central window and the constant.** With \(k_n=\lfloor n/2+s\sqrt n\rfloor\), write \(Y_n=\sqrt n(2B_{n,k_n}-1)\). The beta central limit theorem, obtained for instance by expressing beta variables as ratios of independent gamma variables with shapes \(k_n+1\) and \(n-k_n+1\), gives \(Y_n\Rightarrow Z+2s\). Stirling's estimate for the beta density at its mode gives a uniform bound for the densities of \(Y_n\) when \(s\) is fixed and \(n\) is large. Furthermore \(\sup_n\mathbb E Y_n^2<\infty\). The bounded density controls the negative-log singularity: uniformly, the expected contribution from \(|Y_n|<\delta\) is at most \(C\delta(1+|\log\delta|)\). The second-moment bound controls the positive-log tails beyond \(R\), tending to zero as \(R\to\infty\). Therefore \(\{\log|Y_n|\}\) is uniformly integrable, and
\[
 \mathbb E\log|Y_n|\longrightarrow\mathbb E\log|Z+2s|.
\]
The identity \(-\log|1-2B_{n,k_n}|=\frac12\log n-\log|Y_n|\) proves the critical window. Finally \(\mathbb E\log|Z|=\frac12[\psi(1/2)+\log2]=-(\gamma+\log2)/2\), since \(Z^2\sim\chi_1^2\). Taking \(s=0\) proves the exact constant.

## Verification
The supplied, standard-library-only `verify.py` compares three genuinely distinct finite expressions: a direct enumeration of all permutations and two-gap insertions, an exact hypergeometric overlap sum, and the independently derived rational logarithmic-integral formula. All three agree at every \(k\) for \(1\le n\le6\); the latter two agree at every \(k\) for \(7\le n\le12\), with all coefficient sums and palindromicity tested. Central exact examples are \(M_{6,3}=176/15\), \(M_{8,4}=563/35\), \(M_{10,5}=6508/315\), and \(M_{12,6}=88069/3465\). A finite checker does not establish the infinite asymptotic claims, whose proof uses the beta central limit theorem and uniform integrability.

## Relationship to prior work
Bhattacharya and Mukherjee [1] use the independent-point permutation representation and inversion kernel in §§2.3–2.4 and give the logarithmic density in Corollary 2.2. Together these already imply the exact degree probability of a uniformly chosen vertex by conditioning on its coordinates. The degree-to-type translation and finite beta and rational formulas above are explicit calculations from those inputs, not asserted as new. The contribution is the fixed-offset \(\sqrt n\)-window asymptotic for exact degree probabilities, including its Gaussian-log profile and constant term. The global weak limit does not give this local asymptotic, and Theorem 3.4 in [1] instead concerns the weak limit of the rescaled degree of the vertex at a fixed middle first-order rank. Here the vertex ranges over all ranks and the result concerns one exact integer degree at a time. Hoppen et al. [2] supply the permutation-limit framework. Historical priority remains provisional.

## Limitations
The expectation is over uniformly sampled parameter permutations; there is no claimed almost-sure or high-probability concentration of an individual type histogram. The critical limit is pointwise for each fixed \(s\), not uniform in an expanding window, and the bulk result excludes the endpoint regimes and \(t=1/2\). The statement concerns singleton types with both linear orders named, not reducts or higher tuple arities. No independent mathematical audit has been performed.

## References
1. B. B. Bhattacharya and S. Mukherjee, *Degree Sequence of Random Permutation Graphs*, arXiv:1503.03582, initially public 2015-03-12, https://arxiv.org/abs/1503.03582 ; full journal text https://sites.stat.columbia.edu/sumitm/perm_deg.pdf, especially Corollary 2.2 and Section 3.2.
2. C. Hoppen, Y. Kohayakawa, C. G. Moreira, B. Ráth and R. M. Sampaio, *Limits of Permutation Sequences*, arXiv:1103.5844, https://arxiv.org/abs/1103.5844.
