# Exact third-cumulant sign transitions in finite hard-core paths

## Finding
Let \(P_n\) be the open path with vertices \(1,\ldots,n\), \(n\ge3\). In the equilibrium hard-core lattice gas with common fugacity \(z>0\), denote occupation indicators by \(X_v\) and their distinct-site connected three-point function by \(K_{i,j,k}(z)=\mathbb E[(X_i-p_i)(X_j-p_j)(X_k-p_k)]\), where \(p_v=\mathbb E[X_v]\) and \(1\le i<j<k\le n\).

For every such triple,
\[
\operatorname{sgn}K_{i,j,k}(z)=(-1)^{k-i}\operatorname{sgn}(1-2p_j(z)).
\]
Define the exceptional internal-site set
\[
E_n=\begin{cases}
\{j:2\le j\le n-1,\ j\text{ odd}\},&n\text{ odd},\\
\{j:2\le j\le n-1,\ (j\text{ odd and }2j<n)\text{ or }(j\text{ even and }2j>n+2)\},&n\text{ even}.
\end{cases}
\]
If \(j\notin E_n\), then \(p_j(z)<1/2\) at every finite positive fugacity. If \(j\in E_n\), exactly one finite \(z_{n,j}>0\) satisfies \(p_j(z_{n,j})=1/2\), with a simple, transversal crossing from \(p_j<1/2\) to \(p_j>1/2\). Thus the corresponding three-point function reverses sign **exactly once**; all others have a strict constant sign. The threshold is the unique positive solution of
\[
z I_{j-2}(z)I_{n-j-1}(z)=I_{j-1}(z)I_{n-j}(z),
\]
where \(I_0=1\), \(I_1=1+z\), and \(I_t=I_{t-1}+zI_{t-2}\) for \(t\ge2\). The number of triples with a reversal is exactly
\[
\sum_{j\in E_n}(j-1)(n-j).
\]
The smallest path admitting any triple-correlation sign reversal has **five vertices**. On \(P_5\), all triples with middle site \(j=3\) reverse at the unique positive root of \(z^3-2z^2-3z-1=0\), between \(3\) and \(4\).

## Assumptions and scope
The configuration space consists of independent vertex sets of the finite path, each weighted by \(z^{\text{number of occupied vertices}}\), with no interaction beyond nearest-neighbor exclusion. All sites have identical strictly positive fugacity; the path has free/open boundary conditions. All three observables use **distinct** sites. A sign reversal means a change of sign through a finite positive fugacity; no thermodynamic limit or thermodynamic phase transition is claimed.

## Proof
**1. Markov separation and sign factorization.** The finite-path Gibbs law is a binary inhomogeneous Markov chain along the path. For each \(t<n\), there is \(0<a_t<1\) such that \(\mathbb E[X_{t+1}\mid X_t]=a_t(1-X_t)\): occupation of \(t\) forbids occupation of \(t+1\), while either state is possible after an empty site. Iterating conditional expectations gives \(\operatorname{sgn}\operatorname{Cov}(X_u,X_v)=(-1)^{v-u}\) for \(u<v\), with no vanishing covariances.

The two segments on either side of \(j\) are independent conditional on \(X_j\). Because conditional means of Bernoulli variables are affine in their conditioning Bernoulli variable, for \(i<j<k\) one obtains the **exact** identity
\[
K_{i,j,k}=\frac{\operatorname{Cov}(X_i,X_j)\operatorname{Cov}(X_j,X_k)}{p_j(1-p_j)}(1-2p_j).
\]
Here \(0<p_j<1\), so the prefactor has sign \((-1)^{k-i}\). This proves the first displayed sign formula.

**2. One-site odds.** Let \(I_t(z)\) be the hard-core partition polynomial for a \(t\)-site path. Counting configurations according to occupation of site \(j\) gives
\[
p_j=\frac{zI_{j-2}I_{n-j-1}}{I_n},\qquad
\frac{p_j}{1-p_j}=\frac{zI_{j-2}I_{n-j-1}}{I_{j-1}I_{n-j}}.
\]
Set \(x=(\sqrt{1+4z}-1)/(\sqrt{1+4z}+1)\in(0,1)\), so \(z=x/(1-x)^2\), and put \(b=n-j+1\). The characteristic-root solution of the path recurrence yields
\[
R_j(x):=\frac{p_j}{1-p_j}=x\frac{(1-(-x)^j)(1-(-x)^b)}{(1-(-x)^{j+1})(1-(-x)^{b+1})}.
\]
It suffices to classify the roots of \(R_j(x)=1\).

**3. Odd path lengths.** When \(n\) is odd, \(j\) and \(b\) have the same parity. If they are even, both ratios \((1-x^t)/(1+x^{t+1})\) are less than \(1\), so \(R_j(x)<x<1\). If they are odd, both \((1+x^t)/(1-x^{t+1})\) increase strictly with \(x\); therefore \(R_j\) increases strictly from \(0\) to \(+\infty\) and crosses \(1\) exactly once, transversally.

**4. Even path lengths.** Reflection \(j\mapsto n+1-j\) permits taking \(j\) odd, so \(b\) is even. Expansion of the numerator of \(R_j-1\), whose denominator is strictly positive, gives
\[
(1-x)\left[-(1+x^{n+2})+2\sum_{t=j+1}^{b}x^t\right]
\]
when \(b>j\); if \(b\le j\) the unexpanded expression is negative. For \(b>j\), the critical ratio is
\[
S_{j,b}(x)=\frac{2\sum_{t=j+1}^{b}x^t}{1+x^{n+2}}.
\]
The interval \(j+1,\ldots,b\) is invariant under \(t\mapsto n+2-t\). Writing \(x=e^{-u}\), each paired summand has the form
\[
\frac{x^t+x^{n+2-t}}{1+x^{n+2}}=
\frac{\cosh((\frac{n+2}{2}-t)u)}{\cosh(\frac{n+2}{2}u)},
\]
which increases strictly as \(x\) increases, since \(0\le|\frac{n+2}{2}-t|<\frac{n+2}{2}\). A possible midpoint summand is also strictly increasing. Hence \(S_{j,b}\) increases strictly from \(0\) to \(b-j\). It crosses \(1\) exactly once if \(b-j>1\), and never reaches \(1\) at finite \(x\) otherwise. The condition \(b-j>1\) is \(2j<n\); reflection gives the even-site alternative \(2j>n+2\). Strict monotonicity gives transversal crossings.

**5. Counting and sharp minimum.** Each admissible middle site \(j\) is shared by exactly \((j-1)(n-j)\) ordered triples \(i<j<k\), proving the count. No internal site is exceptional for \(n=3\) or \(4\); at \(n=5\) the internal site \(3\) is exceptional. Direct recurrence gives the polynomial displayed above. The proof is for every finite \(n\), not just the checked instances.

## Verification
The standalone Python 3 program `check.py` uses exact rational arithmetic and independently enumerates legal configurations on paths of lengths \(3\) through \(10\). It checks 1,650 three-point moment-factorization identities and pair covariance signs for five positive fugacities, and independently checks 306 rational characteristic-root odds identities for lengths up to \(14\). It also brackets the five-site threshold between \(3\) and \(4\). Run `python check.py` in the directory containing this file and the script. These finite exact checks are supporting consistency tests, not substitutes for the all-length proof.

## Relationship to prior work
The hard-core partition-function framework and graph deletion identities are classical; see Scott and Sokal (2003). The site-wise one-dimensional Markov factorization is standard and is not claimed as an independent discovery. The contribution assessed here is the **all-length parity-and-position classification**, simple uniqueness of every possible positive-fugacity third-cumulant transition, and the sharp five-site minimum in the uniform open-chain model. Cheong and Henley (2009) study quantum ground-state correlations in a different Hamiltonian setting. Tanaka, Morita and Hiroike (1986) consider direct and total two-point correlations at fixed half density with longer-range interactions. Unindexed earlier analyses might subsume the classification; historical priority is not independently certified.

## Limitations
The classification does not cover periodic chains, arbitrary inhomogeneous activities, canonical fixed-particle laws, fourth and higher cumulants, or finite-size scaling of the thresholds. The formula for the number of reversing triples counts triples, not distinct fugacity thresholds. The proof concerns equilibrium occupation cumulants, not relaxation dynamics.

## References
- A. D. Scott and A. D. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma*, arXiv:cond-mat/0309352v1, first public 2003-09-15. https://arxiv.org/abs/cond-mat/0309352
- S.-A. Cheong and C. L. Henley, *Exact ground states and correlation functions of chain and ladder models of interacting hardcore bosons or spinless fermions*, arXiv:0907.4228v1, first public 2009-07-24. https://arxiv.org/abs/0907.4228
- K. Tanaka, T. Morita and K. Hiroike, *Correlation Functions of a One-Dimensional Lattice Gas with Interactions Up to Third-Nearest Neighbors*, Progress of Theoretical Physics Supplement 87 (1986), 214–228. https://doi.org/10.1143/PTPS.87.214
