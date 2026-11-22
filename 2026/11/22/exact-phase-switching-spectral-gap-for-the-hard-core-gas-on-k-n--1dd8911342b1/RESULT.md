# Exact phase-switching spectral gap for the hard-core gas on \(K_{n,n}\)

## Finding

Let \(n\ge1\) and \(\lambda>0\). In the continuous-time hard-core birth–death dynamics on the balanced complete bipartite graph \(K_{n,n}\), each allowed vacant vertex independently becomes occupied at rate \(\lambda\), and each occupied vertex becomes vacant at rate \(1\). The spectral gap \(g_n(\lambda)\) of the negative generator is the **unique** root \(a\in(0,1+\lambda)\) of

\[
\frac1a=\sum_{j=1}^n\frac{\binom nj\lambda^j}{j(1+\lambda)-a}.
\]

This is the exact relaxation rate of the entire \(2^{n+1}-1\)-state hard-core chain, not merely of an occupancy-count approximation. Moreover,

\[
1=g_1(\lambda)>g_2(\lambda)>g_3(\lambda)>\cdots>0,
\]

and, for every **fixed** \(\lambda>0\),

\[
g_n(\lambda)=\frac{n\lambda}{(1+\lambda)^n}
\left[1-\frac{1}{\lambda n}-\frac{1+\lambda}{\lambda^2n^2}
+O_\lambda(n^{-3})\right] \quad(n\to\infty).
\]

In particular, the exponential metastable relaxation scale has the sharp prefactor \(n\lambda\), and the first two algebraic relative corrections are explicit. For example, \(g_2(\lambda)=(3+\lambda-\sqrt{(3+\lambda)^2-8})/2\).

## Assumptions and scope

The graph has two labeled classes, each of size \(n\), and every cross edge is present. A legal configuration is an independent set, hence consists entirely of occupied left vertices, entirely of occupied right vertices, or is empty. The rates are specified **per vertex**, so a side with \(k\) occupied sites has total birth rate \((n-k)\lambda\) and death rate \(k\). No division by \(2n\) or by \(1+\lambda\) is made. The reversible stationary probability of configuration \(I\) is proportional to \(\lambda^{|I|}\), with partition function \(2(1+\lambda)^n-1\). The spectral gap means the smallest strictly positive eigenvalue of \(-L\), where \(L\) is this continuous-time generator. All claims hold for all integers \(n\ge1\) and all real \(\lambda>0\). The asymptotic expansion keeps \(\lambda\) fixed.

## Proof

**Two glued hypercubes.** Denote the empty configuration by \(\varnothing\). Each nonempty configuration is a nonempty subset of exactly one of the two vertex classes. Thus the state graph comprises two copies of the \(n\)-dimensional binary-flip Markov chain glued only at \(\varnothing\). On one unglued copy, let \(Q_n\) be the generator of \(n\) independent binary sites with birth rate \(\lambda\) and death rate \(1\), and let \(Q_n^D\) be its principal submatrix obtained by removing the empty state. Write \(A_n=-Q_n^D\), a positive definite irreducible killed-generator matrix in its reversible similarity form; its smallest eigenvalue \(\alpha_n\) is simple and has a strictly positive eigenvector.

**The full gap equals the killed gap.** The exchange of the two vertex classes commutes with \(L\). On its antisymmetric subspace, the value at \(\varnothing\) is zero and the negative generator is \(A_n\); hence \(\alpha_n\) occurs in the full spectrum. On the symmetric subspace, deleting the single coordinate \(\varnothing\) from the reversible symmetric representation of \(-L\) produces precisely the symmetric similarity of \(A_n\): the doubled stationary masses for nonempty states cancel in the internal similarity transform. Cauchy interlacing therefore makes the second eigenvalue in the symmetric sector at least \(\alpha_n\), while its first eigenvalue is zero. Every antisymmetric eigenvalue is at least \(\alpha_n\). Therefore \(g_n=\alpha_n\), with no omitted nonoccupancy modes.

**Scalar root equation.** Put \(b=1+\lambda\). The unglued independent-site chain has eigenvalues \(0,-b,-2b,\ldots,-nb\). Starting at \(\varnothing\), its return probability at time \(t\) is

\[
P_t(\varnothing,\varnothing)=b^{-n}(1+\lambda e^{-bt})^n.
\]

The resolvent diagonal of \(-Q_n-aI\) at \(\varnothing\) is, by its spectral expansion,

\[
R(a)=b^{-n}\left[-\frac1a+
\sum_{j=1}^{n}\frac{\binom nj\lambda^j}{jb-a}\right].
\]

The cofactor identity gives \(R(a)=\det(-Q_n^D-aI)/\det(-Q_n-aI)\) for \(0<a<b\). Since \(R'(a)>0\), \(R(a)\to-\infty\) at \(0+\), and \(R(a)\to+\infty\) at \(b-\), there is exactly one zero \(\alpha_n\in(0,b)\). Interlacing of the principal submatrix with the full independent-site generator places its smallest eigenvalue there; the zero is the claimed eigenvalue and yields the equation. The \(n=1\) equation gives \(g_1=1\).

**Strict size descent.** Take the strictly positive Dirichlet ground eigenfunction on the nonempty subsets of \(n\) sites, extending it by zero at the empty subset. On \(n+1\) sites, let the trial function ignore the final site. Its Dirichlet quadratic form and squared \(L^2\) norm are each multiplied by the same factor \(1+\lambda\), so its Rayleigh quotient remains \(\alpha_n\). But the trial function vanishes at the legal nonempty singleton consisting solely of the new site. As the principal Dirichlet eigenfunction on \(n+1\) sites is strictly positive everywhere, equality in the variational bound is impossible. Hence \(\alpha_{n+1}<\alpha_n\).

**Large-size expansion.** Write \(p=\lambda/(1+\lambda)\) and let \(X_n\sim\operatorname{Bin}(n,p)\). At \(a=0\), the positive sum on the right of the root equation is

\[
S_n(0)=(1+\lambda)^{n-1}\mathbb E[X_n^{-1};X_n\ge1].
\]

Taylor expansion about \(np\), with an exponentially small binomial-tail remainder, gives

\[
\mathbb E[X_n^{-1};X_n\ge1]=\frac{1}{np}
\left[1+\frac{1-p}{np}+
\frac{(1-p)(2-p)}{n^2p^2}+O_p(n^{-3})\right].
\]

The scalar root equation bounds \(\alpha_n\le S_n(0)^{-1}\), and expanding its denominators shows \(\alpha_n=S_n(0)^{-1}[1+O_\lambda((1+\lambda)^{-n})]\); a weaker polynomial-times-exponential error suffices. Inverting the displayed binomial expansion produces the claimed coefficients \(-1/\lambda\) and \(-(1+\lambda)/\lambda^2\). This completes the proof.

## Verification

Two standalone scripts accompany this text. `CHECK_EXACT.py` checks the rational cofactor determinant identity for the killed birth–death count matrices at 108 rational test inputs, including three distinct positive activities. `CHECK_DENSE.py` builds the full, labeled hard-core generator and compares its smallest nonzero reversible eigenvalue with the unique scalar root for 21 parameter choices (part sizes one through seven and three activities). It also checks exact small-size values and strict finite size descent. The latter script requires NumPy and SciPy. These finite checks corroborate the algebra but do not replace the all-size proof above.

## Relationship to prior work

Galvin and Tetali's *Slow mixing of Glauber dynamics for the hard-core model on regular bipartite graphs* (first published online on 12 December 2005; an earlier technical report identifies only January 2004) proves exponential lower bounds under expansion and degree-size hypotheses. Its Theorem 1.1 requires the total graph order to be at least the squared degree; that hypothesis does not hold for the balanced complete bipartite graphs of large order studied here. No exact all-size spectral equation, sharp prefactor, or strict size descent is asserted in its inspected introduction, theorem, or subsequent proof. Den Hollander, Nardi, and Taati (2017), Example 4.1, explicitly analyze hard-core dynamics on a complete bipartite graph and give an exact effective-resistance reduction and a high-activity asymptotic for the mean *crossing time*, with \(\lambda\to\infty\) at fixed graph size. Their inspected example does not state a spectral-gap equation or fixed-activity, growing-graph expansion. The earlier Ehrenfest-urn fluctuation literature studies return and first-passage behavior of a single hypercube; our use of that spectrum is classical, while the **full hard-core chain's symmetric/antisymmetric gluing and its exact relaxation gap** form the claim. These comparisons do not certify historical uniqueness.

## Limitations

This theorem concerns the equal-size complete bipartite host, symmetric activity between classes, and the specified continuous-time rates. It does not provide total-variation mixing-time cutoff, prove a claim for incomplete bipartite graphs, treat unequal activities, or give asymptotics when activity varies with size. An equivalent result may occur implicitly in older absorbing-urn spectral literature; one highly relevant 1991 article was not available in full text for comparison. No independent external validation has been performed.

## References

1. D. Galvin and P. Tetali, *Slow mixing of Glauber dynamics for the hard-core model on regular bipartite graphs*, Random Structures & Algorithms 28 (2006), 427–443, first online 2005-12-12, DOI: 10.1002/rsa.20094. Author-accessible version: https://arxiv.org/pdf/1206.3165.
2. N. H. Bingham, *Fluctuation Theory for the Ehrenfest urn*, Advances in Applied Probability 23 (1991), 598–611, DOI: 10.2307/1427624 (abstract inspected; full article not available for comparison).
3. F. den Hollander, F. R. Nardi and S. Taati, *Metastability of hard-core dynamics on bipartite graphs*, arXiv:1710.10232, Example 4.1 (available PDF: https://arxiv.org/pdf/1710.10232).
4. P. Diaconis and D. Stroock, *Geometric bounds for eigenvalues of Markov chains*, Annals of Applied Probability 1 (1991), 36–61 (background on reversible-chain spectral bounds).
