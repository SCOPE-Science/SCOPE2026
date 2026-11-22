# A quarter-power leaf-transition law for Kemeny-optimal helm walks

## Finding

Let \(H_n\), for an integer \(n\ge5\), be the helm formed from a wheel with \(n\) rim vertices by adjoining one private leaf to each rim vertex. Among all symmetric, nonnegative, irreducible stochastic matrices supported on the edges and diagonal of \(H_n\), define the zero-target Kemeny objective
\[
\mathcal K(P)=\sum_{j=2}^{2n+1}(1-\lambda_j(P))^{-1}.
\]
There is a unique global minimizer. For all sufficiently large \(n\), it has a common hub--rim probability \(a_n=1/n\), a common rim--rim probability \(b_n=(1-1/n-c_n)/2\), and a common rim--leaf probability \(c_n\), where \(c_n\) is the unique root in \((0,1-1/n)\) of
\[
\frac{A_n}{c_n^2}
=2\sum_{k=1}^{n-1}
\frac{t_k}{\{1/n+(1-1/n-c_n)t_k\}^2},\qquad
A_n=n-1+\frac{n+1}{2n+1},\quad t_k=1-\cos\frac{2\pi k}{n}.
\]
The hub and rim vertices have zero holding probability, and the private leaves have holding probability \(1-c_n\). The sharp asymptotic allocation and optimum are
\[
 c_n\sim2^{1/4}n^{-1/4},\qquad
 \mathcal K(P_n^*)=\sqrt2\,n^{3/2}+2^{3/4}n^{5/4}+o(n^{5/4}).
\]
The maximum-degree symmetric random walk, which puts probability \(1/n\) on every permitted edge and makes up each row with holding, satisfies
\[
\mathcal K(P_n^{\mathrm{md}})\sim
\left(1+\frac2{\sqrt5}\right)n^2,
\qquad
\frac{\mathcal K(P_n^{\mathrm{md}})}{\mathcal K(P_n^*)}
\sim\frac{1+2/\sqrt5}{\sqrt2}\sqrt n.
\]
The theorem concerns the zero-target convention; adding the alternative unit recurrence term changes all objective values by one but not any optimizer or the stated leading terms.

## Assumptions and scope

Each undirected edge may independently receive any nonnegative symmetric transition probability. The diagonal entries are the remaining nonnegative row masses, and the positive-weight edge support must connect all \(2n+1\) vertices. No orbit symmetry is imposed. There are no imposed positive lower bounds on the permitted edges. The assertion \(a_n=1/n\) is eventual, not a claimed explicit small-size cutoff; global uniqueness holds for every \(n\ge5\). All asymptotic statements hold along integers \(n\to\infty\).

## Proof

**1. Strict global convexity.** Write \(L=I-P\), \(N=2n+1\), and \(Q=\mathbf1\mathbf1^{\mathsf T}/N\). On connected supports, \(L+Q\) is positive definite and
\[
\mathcal K(P)=\operatorname{tr}((L+Q)^{-1})-1.
\]
For any nonzero symmetric perturbation \(D\), the second derivative of inverse trace is \(2\operatorname{tr}(G^{-1}DG^{-1}DG^{-1})>0\), where \(G=L+Q\). Distinct edge-weight vectors produce distinct Laplacians, so the objective is strictly convex in all edge weights. It diverges toward a disconnected support. Thus a global unique minimizer exists, and invariance under the dihedral action on \(H_n\) forces one probability on each of the three edge orbits.

**2. Exact spectrum and feasible reduction.** Denote these probabilities by \(a\) (hub--rim), \(b\) (rim--rim), and \(c\) (rim--leaf). Feasibility requires
\[
0<a\le1/n,\quad c>0,\quad b\ge0,\quad a+2b+c\le1.
\]
For each nonzero rim Fourier mode, the Laplacian has a \(2\times2\) block
\[
\begin{pmatrix}a+2bt_k+c&-c\\-c&c\end{pmatrix},
\]
whose inverse-eigenvalue sum is \(1/c+2/(a+2bt_k)\). The hub, uniform-rim and uniform-leaf quotient has two nonzero eigenvalues with sum \((n+1)a+2c\) and product \((2n+1)ac\). Consequently, with \(B_n=2/(2n+1)\),
\[
\mathcal K_n(a,b,c)=\frac{A_n}{c}+\frac{B_n}{a}
+2\sum_{k=1}^{n-1}\frac1{a+2bt_k}.
\]
Increasing \(b\) at fixed \(a,c\) strictly reduces this expression. Hence every optimum has \(2b=1-a-c\) and no rim holding. Put \(w=1-a-c\); then the exact remaining convex objective is
\[
F_n(a,c)=\frac{A_n}{c}+\frac{B_n}{a}
+2\sum_{k=1}^{n-1}\frac1{a+w t_k}.
\]

**3. The cyclic resolvent.** For \(a,w>0\), set \(\Delta=\sqrt{a(a+2w)}\) and \(\rho=(a+w-\Delta)/w\). Finite Fourier summation, or the geometric-series expansion of the Poisson kernel, gives
\[
S_n(a,w):=\sum_{k=1}^{n-1}\frac1{a+w t_k}
=\frac n\Delta\frac{1+\rho^n}{1-\rho^n}-\frac1a.
\]
When \(a=\sigma/n\) and \(w\) tends to a positive constant, uniformly for \(\sigma\) in any compact subset of \((0,1]\),
\[
2S_n(a,w)=\sqrt{\frac2{\sigma w}}\,n^{3/2}+O(n),
\]
and its derivative with respect to \(w\), at \(a=1/n\), is
\[
-2\sum_{k=1}^{n-1}\frac{t_k}{(1/n+w t_k)^2}
=-\frac1{\sqrt2}w^{-3/2}n^{3/2}(1+o(1)).
\]
The error statements follow by differentiating the displayed exact formula: \(\rho^n\) and its derivatives are exponentially small in \(\sqrt n\) when \(w\) is bounded away from zero.

**4. Localization.** A feasible trial with \(a=1/n\) and \(c=n^{-1/4}\) gives \(\mathcal K\le\sqrt2\,n^{3/2}+O(n^{5/4})\). Because \(a\le1/n\) and \(w\le1-c\), any minimizer with \(c\ge\varepsilon>0\) satisfies
\[
F_n(a,c)\ge 2\sum_{k=1}^{n-1}\frac1{1/n+(1-\varepsilon)t_k}
=\sqrt{\frac2{1-\varepsilon}}\,n^{3/2}+O(n),
\]
contradicting the trial for large \(n\). Thus \(c_n\to0\). Similarly, if \(na\le1-\varepsilon\), compare with the sum having denominator \((1-\varepsilon)/n+t_k\); it follows that \(na_n\to1\).

**5. Eventual exact hub saturation.** In fact, for all sufficiently large \(n\), \(a_n=1/n\), not merely asymptotically. At fixed \(c\le1/4\), differentiate the last sum in \(F_n\) with respect to \(a\) along \(w=1-a-c\). Its derivative is
\[
-\sum_{k=1}^{n-1}\frac{1-t_k}{(a+w t_k)^2}.
\]
For \(k\le\lfloor\sqrt n/8\rfloor\), one has \(t_k\le\pi^2/(32n)\); the positive contributions to the sum inside the minus sign are bounded below by a fixed positive multiple of \(n^{5/2}\). Negative contributions (which require \(t_k>1\)) are at most \(4n\) in absolute value, since \(w\ge1-1/n-1/4\ge1/2\). Thus the derivative of the last sum is strictly negative uniformly over \(0<a\le1/n\) and \(c\le1/4\), for all sufficiently large \(n\). The other \(a\)-dependent term \(B_n/a\) is also strictly decreasing. Since the global optimizer has \(c_n\to0\), it must attain the boundary \(a_n=1/n\). This is a comparison within the original feasible stochastic domain, not an imposed hub-symmetry constraint.

**6. Quarter-power scale and objective.** With \(a=1/n\), strict convexity gives uniqueness of the one-variable minimizer. The derivative tends to \(-\infty\) as \(c\downarrow0\), while at \(c=1-1/n\) its left limit is \(-A_n/(1-1/n)^2+2n^3>0\) for \(n\ge5\), using \(\sum_{k=1}^{n-1}t_k=n\). Thus there is exactly one interior root, given by the stationary equation in the Finding. The derivative-resolvent estimate from step 3, together with \(c_n\to0\), yields
\[
\frac{A_n}{c_n^2}=\frac1{\sqrt2}n^{3/2}(1+o(1)),
\quad A_n\sim n,
\]
and hence \(c_n\sim2^{1/4}n^{-1/4}\). Expanding the exact resolvent at \(w=1-1/n-c_n\) yields
\[
2S_n(1/n,w)=\sqrt2\,n^{3/2}
+\frac1{\sqrt2}c_n n^{3/2}+o(n^{5/4}).
\]
The other leading term is \(A_n/c_n\sim2^{-1/4}n^{5/4}\). Their coefficients add to \(2^{3/4}\); \(B_n/a_n=O(1)\), while the \(-2n\) from the resolvent is \(o(n^{5/4})\).

**7. Maximum-degree comparison.** With \(a=b=c=1/n\), the exact formula becomes
\[
\mathcal K_n^{\mathrm{md}}=n(A_n+B_n)+2n\sum_{k=1}^{n-1}\frac1{3-2\cos(2\pi k/n)}.
\]
The Riemann sum converges to \(1/\sqrt5\) after division by \(n\), because \((2\pi)^{-1}\int_0^{2\pi}(3-2\cos\theta)^{-1}\,d\theta=1/\sqrt5\). This proves the stated divergence in the comparator-to-optimum ratio.

## Verification

The accompanying standalone `verify.py` directly assembles each helm Laplacian and compares its eigenvalue inverse trace with the independent orbit formula for numerous positive edge configurations. It also solves the finite scalar stationarity equation and tests local feasible perturbations, the maximum-degree benchmark, and the two asymptotic scalings. One completed run reported **389 passing finite assertions**. These diagnostics do not certify the infinite statements, which follow from the displayed convexity, Fourier and asymptotic arguments. Run `OPENBLAS_NUM_THREADS=1 python verify.py` with NumPy and SciPy installed.

## Relationship to prior work

Hunter (2012) gives the foundational Kemeny identities, including the distinction between the ordinary and modified convention. Patel, Agharkar and Bullo (2015) establish general convex and semidefinite design formulations for reversible Kemeny minimization, but do not give the helm-family allocation or asymptotic law. A more recent general reversible-chain numerical optimization study also does not state this helm result. Earlier specific network solutions for bare wheels and leaf coronas address distinct edge sets: the helm combines a saturating hub with \(n\) private leaves and its quarter-power rate is not a consequence of either formula without a new analysis. The finite cyclic resolvent is a standard identity; novelty is not claimed for that identity or the convexity framework.

## Limitations

The proof establishes exact hub saturation only for all sufficiently large rim sizes, without a best explicit cutoff. It does not assert a formula for the interior optimum at every small \(n\) beyond uniqueness and the two-variable convex reduction. Published-source discovery is not proof of priority; an unindexed helm-specific optimization result could preempt originality. Only self-review and finite reproducibility checks have been performed; independent audit is absent. The optimality applies to symmetric stochastic walks with uniform stationary distribution, not arbitrary nonreversible chains or degree-biased graph walks.

## References

1. J. J. Hunter, *The Role of Kemeny's Constant in Properties of Markov Chains* (arXiv:1208.4716v1, publicly posted 2012-08-23), https://arxiv.org/abs/1208.4716.
2. R. Patel, P. Agharkar and F. Bullo, *Robotic Surveillance and Markov Chains With Minimal Weighted Kemeny Constant*, IEEE Transactions on Automatic Control 60 (2015), 3156–3167, https://doi.org/10.1109/TAC.2015.2426317; openly accessible manuscript https://motion.me.ucsb.edu/pdf/2014b-pab.pdf.
3. F. Durastante, M. Gnazzo and B. Meini, *Kemeny's constant minimization for reversible Markov chains via structure-preserving perturbations* (2026), https://doi.org/10.1007/s10543-026-01152-6.
4. *Helm Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/HelmGraph.html (graph definition only; not cited for the optimization).
