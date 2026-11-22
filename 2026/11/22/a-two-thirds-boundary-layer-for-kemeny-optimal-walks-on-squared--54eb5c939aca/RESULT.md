# A two-thirds boundary layer for Kemeny-optimal walks on squared cycles

## Finding

For every integer \(n\geq5\), let \(G_n=C_n^2\) be the graph on the residues modulo \(n\), with edges between vertices differing by \(\pm1\) or \(\pm2\). Among **all** irreducible, symmetric, entrywise-nonnegative row-stochastic matrices \(P\) supported on these edges and the diagonal, there is a unique minimizer of the zero-target Kemeny sum
\[
K(P)=\sum_{j=2}^n\frac{1}{1-\lambda_j(P)}.
\]
The minimizer has zero diagonal, and its probabilities at distances one and two are respectively
\[
a_n=\frac{\varepsilon_n}{2},\qquad b_n=\frac{1-\varepsilon_n}{2},
\]
where \(\varepsilon_n\in(0,1)\) is the unique zero of
\[
\sum_{k=1}^{n-1}
\frac{B_k-A_k}{\bigl(\varepsilon A_k+(1-\varepsilon)B_k\bigr)^2}=0,
\quad A_k=1-\cos\frac{2\pi k}{n},\quad B_k=1-\cos\frac{4\pi k}{n}.
\]
As \(n\to\infty\),
\[
\boxed{\varepsilon_n\sim 4^{2/3}n^{-2/3}},\qquad
\boxed{K(P_n^*)=\frac{n^2}{24}+\frac{3}{8\,4^{1/3}}n^{4/3}+o(n^{4/3})}.
\]
In particular \(a_n\sim 2^{1/3}n^{-2/3}\), and \(b_n\to1/2\). The optimal Kemeny sum has limiting ratio \(1/4\) to the pure one-hop walk's sum and \(5/8\) to the equal-edge walk's sum. This is a singular design limit: the dominant two-hop channel alone is disconnected for even \(n\), and for odd \(n\) it is connected but still nonoptimal at every finite \(n\).

## Assumptions and scope

The graph is simple and undirected; \(n\ge5\) guarantees distinct distance-one and distance-two edge orbits. Admissible entries may be zero but the resulting walk must be irreducible. Every vertex has the same stationary probability \(1/n\); arbitrary independent symmetric edge probabilities and vertex holding probabilities are allowed. The sum excludes the stationary eigenvalue and is defined even for periodic chains. The more common first-passage Kemeny convention including an extra return contribution differs by a constant \(1\) and has the same optimizer.

## Proof

**1. Unrestricted uniqueness and orbit reduction.** On the mean-zero subspace \(\mathbf1^\perp\), put \(L(P)=I-P\). Connectedness makes \(L\) positive definite there. Its inverse-trace is strictly convex: for every nonzero symmetric perturbation \(H\),
\[
\frac{d^2}{dt^2}\operatorname{tr}(L+tH)^{-1}\bigg|_{t=0}
=2\operatorname{tr}(L^{-1}HL^{-1}HL^{-1})>0.
\]
For the strict inequality, conjugate \(H\) by \(L^{-1/2}\): the expression is the trace of a nonzero positive-semidefinite square multiplied by a positive-definite matrix. The map from feasible off-diagonal weights to \(L\) is injective, so a minimizer, if attained, is unique. Existence follows from compactness after extending the objective by \(+\infty\) on disconnected matrices (the inverse trace diverges near loss of connectivity).

Cyclic averaging of an arbitrary admissible \(P\) preserves its constraints and cannot increase the convex objective; strictness forces the unique optimizer to be invariant under the rotations. Thus all distance-one edges have a common probability \(a\), and all distance-two edges a common probability \(b\). The row constraint is \(2a+2b\le1\). If the inequality were strict, increasing both positive orbit weights slightly while reducing holding would increase \(L\) strictly on mean-zero vectors and lower its inverse trace. The same argument handles a boundary with one positive orbit weight. Hence every optimum saturates \(a+b=1/2\) and has no holding. Set \(\varepsilon=2a\) and \(1-\varepsilon=2b\).

**2. Exact scalar problem and interior support.** Fourier diagonalization gives the nonzero Laplacian eigenvalues
\[
D_k(\varepsilon)=\varepsilon A_k+(1-\varepsilon)B_k,
\qquad k=1,\ldots,n-1.
\]
Thus \(F_n(\varepsilon)=\sum_{k=1}^{n-1}D_k(\varepsilon)^{-1}\), with
\[
F_n''(\varepsilon)=2\sum_{k=1}^{n-1}
\frac{(A_k-B_k)^2}{D_k(\varepsilon)^3}>0
\]
throughout its finite domain. At \(\varepsilon=1\), elementary trigonometric sums yield
\[
F_n'(1)=\sum_{k=1}^{n-1}\frac{B_k-A_k}{A_k^2}
=\frac{(n-1)(n-3)}2>0.
\]
At \(\varepsilon=0\), the graph is disconnected if \(n\) is even. If \(n\) is odd, multiplication by two permutes the nonzero residues, so \(F_n(0)=F_n(1)=(n^2-1)/6\); strict convexity implies \(F_n(1/2)<F_n(0)\). Either way neither boundary minimizes. Consequently the unique interior optimum is characterized by \(F_n'(\varepsilon_n)=0\) as stated.

**3. Exact finite-size trigonometric resolvent.** Write \(A=4-3\varepsilon\), \(\Delta=\sqrt{\varepsilon A}\), and
\[
r=\frac{2(1-\varepsilon)}{2-\varepsilon+\Delta}\in(0,1).
\]
From \(D_k=2\sin^2(\pi k/n)[A-4(1-\varepsilon)\sin^2(\pi k/n)]\) and partial fractions,
\[
F_n(\varepsilon)=\frac{n^2-1}{6A}
+\frac{2(1-\varepsilon)}{A}
\left[\frac{n}{\Delta}\frac{1+(-r)^n}{1-(-r)^n}-\frac1A\right].\tag{1}
\]
For completeness: \(\sum_{k=1}^{n-1}\csc^2(\pi k/n)=(n^2-1)/3\), obtainable by differentiating the cotangent multiplication identity. The remaining denominator equals \(2-\varepsilon+2(1-\varepsilon)\cos(2\pi k/n)\). Its reciprocal has Fourier series
\[
\frac1{\Delta}\left(1+2\sum_{j\ge1}(-r)^j\cos(j\theta)\right).
\]
Summing this series over the \(n\) equally spaced angles kills all nonmultiples of \(n\); subtracting the \(k=0\) term \(1/A\) yields (1). This derivation proves (1) for both parities without a numerical approximation.

**4. Boundary-layer and sharp coefficient.** Evaluate (1) at the admissible comparison \(\varepsilon=n^{-2/3}\). Since \(-\log r\sim\sqrt\varepsilon\), the factor involving \((-r)^n\) tends exponentially to \(1\); consequently
\[
F_n(\varepsilon_n)\le\frac{n^2}{24}+O(n^{4/3}).\tag{2}
\]
The first summand of (1) bounds \(F_n\) from below, proving \(\varepsilon_n=O(n^{-2/3})\). Moreover \(n\sqrt{\varepsilon_n}\to\infty\): otherwise a subsequence would have \(\varepsilon_n\le C/n^2\), and a Fourier mode nearest \(\pi\) would contribute at least \(c_C n^2\) to the second, nonnegative summand in (1), contradicting (2). (Equivalently use the original Fourier sum together with the first summand lower bound.) Hence \((-r)^n\to0\). In (1), the second summand is now asymptotic to \(n/(4\sqrt{\varepsilon_n})\), up to a uniformly bounded subtractive term, and (2) forces \(\varepsilon_n\ge c n^{-2/3}\) for some \(c>0\).

Therefore \(x_n=n^{2/3}\varepsilon_n\) stays in a compact subset of \((0,\infty)\). Uniformly on such compact sets, substituting \(\varepsilon=x n^{-2/3}\) into (1) gives
\[
F_n(xn^{-2/3})=\frac{n^2}{24}
+n^{4/3}\left(\frac{x}{32}+\frac1{4\sqrt x}\right)+o(n^{4/3}).\tag{3}
\]
The strictly convex limiting function in parentheses has its unique minimum where \(x^{3/2}=4\), hence \(x=4^{2/3}\). Compactness and uniqueness of that minimum imply convergence of \(x_n\) and yield both boxed asymptotics. Inserting the optimizer gives the correction \(3/(8\,4^{1/3})\).

Finally the simple one-hop walk has sum \((n^2-1)/6\), and the four-neighbor equal-edge walk has \(\varepsilon=1/2\); (1) yields \(F_n(1/2)\sim n^2/15\). Thus the indicated limiting ratios are \((1/24)/(1/6)=1/4\) and \((1/24)/(1/15)=5/8\).

## Verification

Run `python3 verify.py` using Python 3.9 or later; only the standard library is required. The checker evaluates the Fourier sum and independent closed form on finite sample sizes, verifies strict derivative signs and numerical root optimality, computes the discrete transition matrix and an independent Gaussian-elimination inverse-trace for small \(n\), and checks the predicted asymptotic constants at increasing \(n\). These finite tests are diagnostics; the infinite-family result and asymptotics follow from the proof above.

## Relationship to prior work

Boyd, Diaconis, Parrilo and Xiao's graph-symmetry optimization analyzes fastest mixing using the second-largest eigenvalue modulus, not the Kemeny objective. Patel, Agharkar and Bullo established a general convex optimization and semidefinite formulation for reversible Kemeny design, but did not give the squared-cycle trace minimizer or its singular large-cycle scaling in the inspected results. Ghosh, Boyd and Saberi give a general effective-resistance conductance-design framework; it does not determine the finite squared-cycle Kemeny optimizer or the boundary layer. Doi and collaborators give an exact mean-hitting-time formula for the *simple random walk* on the same squared-cycle graph, whose four edge probabilities are fixed at \(1/4\). Two later results on the same squared-cycle family optimize *worst-case spectral mixing* (SLEM), assigning one-hop probabilities of order \(n^{-2}\); their objectives and optimizers are not the present trace-inverse result. Formula (1), unrestricted uniqueness for this objective, and the \(n^{-2/3}\) law are the specific claims here, not novelty of Fourier diagonalization or symmetry reduction.

## Limitations

The result concerns symmetric stochastic matrices (uniform stationary distribution), the standard unweighted edge-support graph, and two available jump lengths. It does not imply the same exponent for nonreversible walks, priced edges, or multiple longer jumps. The formula uses the zero-target Kemeny convention. No claim of independent mathematical validation is made. A published equivalent not surfaced in the inspected literature remains a priority risk; database nonmatches are not proof of uniqueness of publication.

## References

1. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (public September 6, 2007), https://arxiv.org/abs/0709.0955.
2. R. Patel, P. Agharkar and F. Bullo, *Robotic Surveillance and Markov Chains With Minimal Weighted Kemeny Constant*, IEEE Transactions on Automatic Control 60(12), 3156–3167 (2015), https://doi.org/10.1109/TAC.2015.2426317; author manuscript https://motion.me.ucsb.edu/pdf/2014b-pab.pdf.
3. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, https://www.stat.berkeley.edu/~aldous/206-RWG/RWGpapers/ghosh_boyd.pdf.
4. Y. Doi et al., *On the Average Hitting Times of the Squares of Cycles*, Discrete Applied Mathematics 313 (2022), 18–28, arXiv:2110.12614, https://arxiv.org/abs/2110.12614.
5. *Exact Fastest Symmetric Mixing on Two-Hop Cyclic Networks*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-fastest-symmetric-mixing-on-two-hop-cyclic-networks--68c871d2f31e (different objective, SLEM).
6. *Exact Fastest Mixing on the Second Power of Every Finite Cycle*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-fastest-mixing-on-the-second-power-of-every-finite-cycle--1e4c2afd1cba (different objective, SLEM).
