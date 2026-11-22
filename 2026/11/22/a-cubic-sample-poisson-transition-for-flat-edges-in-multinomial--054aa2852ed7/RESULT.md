# A cubic-sample Poisson transition for flat edges in multinomial histograms

## Finding
Let \(n\to\infty\) and let \(N=N_n\) be a deterministic positive integer sequence with \(\lambda_n=N_n/n\to\infty\). Sample the ordered histogram
\[
(X_1,\ldots,X_n)\sim\operatorname{Mult}(N_n;1/n,\ldots,1/n).
\]
A *flat edge* is an adjacent pair of bins with exactly equal counts. Define the counting measure and total number of flat edges by
\[
\Xi_n=\sum_{j=1}^{n-1}\mathbf1_{\{X_j=X_{j+1}\}}\delta_{j/n},
\qquad T_n=\Xi_n([0,1]).
\]
For every fixed \(c\in(0,\infty)\), if \(N_n/n^3\to c\), then
\[
\boxed{\Xi_n\ \Rightarrow\ \operatorname{PPP}\left(\frac{dx}{\sqrt{4\pi c}}\right),\qquad
T_n\ \Rightarrow\ \operatorname{Pois}\left(\frac{1}{\sqrt{4\pi c}}\right).}
\]
In particular, the limiting probability of *no* flat edge is
\[
\boxed{\Pr(T_n=0)\longrightarrow \exp\left(-\frac1{\sqrt{4\pi c}}\right).}
\]
The threshold is two-sided. If \(N_n/n^3\to\infty\) then \(\Pr(T_n=0)\to1\). If \(N_n/n^3\to0\) while \(N_n/n\to\infty\), then \(T_n/\mathbb ET_n\to1\) in probability and \(\Pr(T_n=0)\to0\). Uniformly across these diverging-load regimes,
\[
\boxed{\mathbb ET_n\sim\frac{n-1}{\sqrt{4\pi\lambda_n}}\sim
\frac1{2\sqrt\pi}\sqrt{\frac{n^3}{N_n}}.}
\]
These assertions are for a **fixed-total multinomial sample**, not an independently Poissonized histogram.

A useful stronger local statement describes clustering. For a fixed positive integer \(k\), let \(J\subseteq\{1,\ldots,n-1\}\) have \(|J|=k\). Break \(J\) into its maximal runs of consecutive edges, of lengths \(L_1,\ldots,L_b\) with \(\sum_h L_h=k\). Then, uniformly over all such \(J\),
\[
\boxed{\Pr\left(X_j=X_{j+1}\ \text{for every }j\in J\right)
=\frac{1+o(1)}{(2\pi\lambda_n)^{k/2}\sqrt{\prod_{h=1}^{b}(L_h+1)}}.}
\tag{1}
\]
The \(o(1)\) depends on \(k\) and the sequence \(\lambda_n\), but not on the selected edge positions. In particular, \(k\) pairwise non-neighboring edges have asymptotic joint probability \((4\pi\lambda_n)^{-k/2}\), whereas two neighboring edges have probability asymptotic to \((2\pi\lambda_n\sqrt3)^{-1}\).

## Assumptions and scope
The bin count \(n\) grows to infinity; the number of samples \(N_n\) is fixed rather than Poisson, each sample falls independently and uniformly in the \(n\) ordered bins, and \(\lambda_n=N_n/n\to\infty\). There are \(n-1\) **noncyclic** adjacent edges. The point process lives on the compact unit interval; its limiting intensity is Lebesgue measure multiplied by the displayed positive constant. All asymptotic statements refer to joint growth of \(n\) and \(N_n\) under the specified scaling. No analogous claim is made for nonuniform probabilities or cyclic edge conventions.

## Proof
**1. An incidence-matrix local limit theorem with a fixed number of flat-edge constraints.** Fix \(k\) and \(J=\{j_1,\ldots,j_k\}\). Let \(B=B_J\) be the \(k\times n\) signed edge-incidence matrix with row \(e_{j_r+1}^{\mathsf T}-e_{j_r}^{\mathsf T}\). Then \(BX=0\) is precisely the event in (1). For one uniformly placed ball, the increment of \(BX\) is a column of \(B\), and its characteristic function is
\[
\phi_{n,J}(t)=\frac1n\sum_{v=1}^n\exp\bigl(i(B^{\mathsf T}t)_v\bigr),\qquad t\in[-\pi,\pi]^k.
\]
The \(N_n\) ball increments are iid. Fourier inversion on \(\mathbb Z^k\) gives the exact identity
\[
\Pr(BX=0)=\frac1{(2\pi)^k}\int_{[-\pi,\pi]^k}\phi_{n,J}(t)^{N_n}\,dt.\tag{2}
\]
Write \(A_J=BB^{\mathsf T}\). Distinct rows are linearly independent, and
\[
(A_J)_{rs}=\begin{cases}2,&r=s,\\-1,&|j_r-j_s|=1,\\0,&\text{otherwise}.\end{cases}
\]
The matrix is block diagonal along the consecutive-edge runs. Its block of length \(L\) is the path tridiagonal matrix \(\operatorname{tridiag}(-1,2,-1)\). The determinant recurrence \(d_L=2d_{L-1}-d_{L-2}\), with \(d_0=1,d_1=2\), gives
\[
\det A_J=\prod_{h=1}^b(L_h+1)>0.\tag{3}
\]
There are at most \(2k\) nonzero columns of \(B\), and \(\sum_v (B^{\mathsf T}t)_v=0\). With \(t=s/\sqrt{\lambda_n}\), Taylor expansion gives, for each fixed \(s\),
\[
N_n\log\phi_{n,J}(s/\sqrt{\lambda_n})
=-\tfrac12s^{\mathsf T}A_Js
+O_k\bigl(\|s\|^3/\sqrt{\lambda_n}+\|s\|^4/(n\lambda_n)\bigr).\tag{4}
\]
Here and below, the bounds can be chosen independently of the placement of \(J\), because for fixed \(k\) only finitely many run patterns occur.

**2. Global Fourier bound; no hidden lattice peaks.** Put \(a_v=(B^{\mathsf T}t)_v\), and let \(S\) be the support of these nonzero column forms. The identity
\[
1-|\phi_{n,J}(t)|^2=\frac1{n^2}\sum_{u<v}|e^{ia_u}-e^{ia_v}|^2
\]
gives, since at least \(n-2k\) coordinates have \(a_v=0\),
\[
1-|\phi_{n,J}(t)|^2\ge\frac{n-2k}{n^2}\sum_{v\in S}|e^{ia_v}-1|^2.
\]
For each consecutive-edge run, the endpoint column forms are the first and last edge variables (with signs), while the interior column forms are successive differences of edge variables. Therefore all phases \(a_v\) can be multiples of \(2\pi\) only if all \(t_r\) are multiples of \(2\pi\). The sole such point in the torus fundamental domain is the origin. Near the origin, the sum on the right is \(t^{\mathsf T}A_Jt+O_k(\|t\|^4)\). Its ratio to \(\|t\|^2\) is bounded away from zero globally on the compact fundamental domain by continuity and positive definiteness. Thus, for all large \(n\), with \(c_k>0\) independent of \(n\) and \(J\),
\[
|\phi_{n,J}(t)|^{N_n}\le\exp(-c_k\lambda_n\|t\|^2).\tag{5}
\]
At opposite faces of the chosen cube, the same torus statement applies by periodicity. This also rules out any lattice-period multiplicity in (2).

Use the substitution \(t=s/\sqrt{\lambda_n}\) in (2). Equations (4)--(5) and dominated convergence, together with the standard Gaussian integral, now yield uniformly over selected \(J\),
\[
\begin{aligned}
\Pr(BX=0)
&=(1+o(1))(2\pi)^{-k}\lambda_n^{-k/2}
\int_{\mathbb R^k}e^{-s^{\mathsf T}A_Js/2}\,ds\\
&=\frac{1+o(1)}{(2\pi\lambda_n)^{k/2}\sqrt{\det A_J}}.
\end{aligned}
\]
Equation (3) proves (1).

**3. The spatial Poisson process at cubic sample size.** Suppose \(N_n/n^3\to c\in(0,\infty)\), equivalently \(\lambda_n/n^2\to c\). For fixed \(k\), any ordered \(k\)-tuple of pairwise non-neighboring distinct edge indices has joint probability
\[
(4\pi\lambda_n)^{-k/2}(1+o(1))=n^{-k}(4\pi c)^{-k/2}(1+o(1)).
\]
Among \(O(n^k)\) ordered distinct edge tuples, only \(O_k(n^{k-1})\) contain at least one pair of neighboring indices. The uniform local estimate (1) bounds each such exceptional probability by \(O_k(\lambda_n^{-k/2})=O_k(n^{-k})\), so their total contribution to factorial moments vanishes. For any finite collection of disjoint intervals with endpoints in \([0,1]\), their mixed falling-factorial moments thus converge to those of independent Poisson variables, each with mean its interval length divided by \(\sqrt{4\pi c}\). The multivariate factorial-moment method identifies the limit. Bounded expected total mass ensures tightness of the finite counting measures on \([0,1]\), and the interval-count characterization yields the asserted Poisson point-process limit. Taking the whole interval gives the one-dimensional Poisson law, including the zero-count probability.

**4. Both sides of the transition.** The \(k=1\) instance of (1) gives, writing \(p_n=\Pr(X_1=X_2)\),
\[
p_n\sim(4\pi\lambda_n)^{-1/2},\qquad
\mathbb ET_n=(n-1)p_n.\tag{6}
\]
If \(N_n/n^3\to\infty\) then \(\mathbb ET_n\to0\), hence \(\Pr(T_n>0)\le\mathbb ET_n\to0\).

If \(N_n/n^3\to0\) while \(\lambda_n\to\infty\), then \(np_n\to\infty\). Two adjacent flat-edge indicators have joint probability \(O(\lambda_n^{-1})\) by the \(k=2\) run of length two, while two indicators separated by at least one intervening edge have joint probability \(p_n^2(1+o(1))\) *uniformly* by the \(k=2\) disjoint-run estimate. Consequently,
\[
\operatorname{Var}(T_n)
=O(np_n+n/\lambda_n)+o(n^2/\lambda_n),
\]
whereas \((\mathbb ET_n)^2\asymp n^2/\lambda_n\to\infty\). Dividing gives \(\operatorname{Var}(T_n)/(\mathbb ET_n)^2\to0\); Chebyshev's inequality establishes the concentration and disappearance of the no-flat-edge event. This proves all assertions.

## Verification
The standalone Python 3 script `verify.py` performs 345 exact or explicitly numerical consistency assertions. It independently enumerates small multinomial configurations with exact integer multiplicities; checks the formulas for a single flat edge, a neighboring pair of flat edges and a disjoint pair; verifies the path-incidence determinant \(\prod(L_h+1)\) on many subsets using an independent permutation formula; and evaluates the critical one-edge normalization at several increasing bin counts with a stable binomial-mixture calculation. The resulting absolute errors from the expected normalization \(2\sqrt\pi\,n\Pr(X_1=X_2)\to1\) decrease across the tested sizes. The script needs only the Python standard library; run `python3 verify.py` from its directory. The infinite-dimensional and asymptotic claims are proved by the Fourier and factorial-moment arguments above, not by these finite checks.

For reference, the exact finite-sample one-edge formula independently used in the script is
\[
\Pr(X_1=X_2)=\frac1{n^N}\sum_{r=0}^{\lfloor N/2\rfloor}
\binom N{2r}\binom{2r}r(n-2)^{N-2r}.
\]

## Relationship to prior work
Banić and Elezović's recent series on discrete total variation under the multinomial concerns the statistic \(\sum_j|X_{j+1}-X_j|\), its moments, and fixed-bin or iterated asymptotics, with a separate analysis of nonuniform sampling laws. Their Part 4 manuscript, first publicly submitted November 6, 2026, explicitly distinguishes fixed-dimensional limits from later limits in the number of bins. It does not state the zero-gradient *count*, a cubic simultaneous-growth threshold, or a spatial Poisson process of flat edges. Their Part 1 gives the exact expected sum of *absolute* adjacent contrasts rather than the probability a contrast is *zero*.

The earlier published result *Conditioning removes a leading variance term from multinomial histogram roughness* treats the fixed-positive-load variance of the sum of absolute adjacent contrasts. It is not an asymptotic for the rare event \(X_j=X_{j+1}\) as occupancy load diverges. Eaton, Godbole and Sinclair analyze ties in occupancy-type competition, but the examined results concern other score comparisons rather than this fixed-total high-load adjacent-bin point process. The local Fourier method here is closely related to standard lattice local-limit theory and Poisson rare-event theory, and similar abstractions might establish the result implicitly; no assertion of exhaustive novelty across all such theorems is made.

## Limitations
The statement requires diverging load \(N_n/n\to\infty\) and uniform bin probabilities. It does not address the low-load occupancy regimes, nonuniform histograms, arbitrary adjacency graphs, or finite-sample error rates for the point-process approximation. The checker is corroborating finite evidence only. The global literature comparison cannot exclude an equivalent statement hidden in unindexed or inaccessible probability literature, and there has been no independent mathematical audit.

## References
1. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 4: variance under a general distribution*, arXiv:2611.09592v1, publicly submitted 2026-11-06, https://arxiv.org/abs/2611.09592.
2. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 1: expectation under the uniform null*, arXiv:2610.13366, publicly submitted 2026-10-09, https://arxiv.org/abs/2610.13366.
3. *Conditioning removes a leading variance term from multinomial histogram roughness*, published 2026-10-18, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-conditioning-removes-a-leading-variance-term-from-multinomial-hi--e29f4fd136bb/RESULT.md.
4. J. Eaton, A. Godbole and B. Sinclair, *Competition between Discrete Random Variables, with Applications to Occupancy Problems*, arXiv:0806.1007, https://arxiv.org/abs/0806.1007.
