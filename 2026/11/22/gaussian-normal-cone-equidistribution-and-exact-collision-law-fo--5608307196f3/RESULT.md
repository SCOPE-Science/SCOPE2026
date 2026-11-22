# Gaussian normal-cone equidistribution and exact collision law for clique fractional stable-set polytopes

## Finding
For each integer \(n\ge3\), consider the full-dimensional Euclidean fractional stable-set polytope of the clique:
\[
F_n=\{x\in\mathbb R_{\ge0}^{n}: x_i+x_j\le 1\quad(1\le i<j\le n)\}.
\]
Let \(G\sim N(0,I_n)\), and let \(V_n\) denote the almost-surely unique vertex maximizing \(G\cdot x\) over \(F_n\). Define independent half-normal variables \(H_i=|Z_i|\), where the \(Z_i\) are independent standard Gaussians; for every integer \(k\ge3\), put
\[
q_k=\Pr\!\left(2\max_{1\le j\le k} H_j<\sum_{j=1}^k H_j\right),
\qquad
\alpha_n=\Pr\!\left(Z_1>\sum_{j=2}^n (Z_j)_+\right).
\]
Here \((t)_+=\max(t,0)\). The vertices comprise the origin, all standard basis vectors, and the half-support vectors \(h_S=\frac12\mathbf1_S\) with \(S\subseteq[n]\) and \(|S|\ge3\). Their **exact Gaussian normal-cone probabilities** are
\[
\boxed{\Pr(V_n=0)=2^{-n},\quad \Pr(V_n=e_i)=\alpha_n,\quad
\Pr(V_n=h_S)=2^{-n}q_{|S|}.}
\tag{1}
\]
In particular, for independent Gaussian directions and exposed vertices \(V_n,V_n'\), the coincidence probability is exactly
\[
\boxed{C_n:=\Pr(V_n=V_n')=4^{-n}\!\left(1+\sum_{k=3}^{n}\binom nk q_k^2\right)+n\alpha_n^2.}
\tag{2}
\]
Writing \(\Phi\) for the standard Gaussian distribution function, let
\[
\rho=2e^{1/2}\Phi(-1)=0.523156\ldots,\qquad
m=\frac12+e^2\Phi(-2)=0.668102\ldots.
\]
For all integer \(n\ge3\), these constants control explicit exponential errors, and the collision probability has the **sharp asymptotic leading constant**
\[
\boxed{C_n=2^{-n}\bigl(1+O(n(0.9)^n)\bigr).}
\tag{3}
\]
Let \(U_n\) be uniform on the \(2^n-1-n-\binom n2\) half-support vertices \(\{h_S:|S|\ge3\}\). In total variation,
\[
\boxed{d_{\mathrm{TV}}(\mathcal L(V_n),\mathcal L(U_n))=O(nm^n).}
\tag{4}
\]
Condition on the two independent directions exposing the same vertex. Set \(K_n=|S|\) if their common vertex is \(h_S\), and \(K_n=0\) if it is an integral vertex. Then
\[
d_{\mathrm{TV}}\bigl(\mathcal L(K_n\mid V_n=V_n'),\operatorname{Bin}(n,1/2)\bigr)
=O(n(0.9)^n),
\]
so \((K_n-n/2)/(\sqrt n/2)\) converges in distribution to a standard normal. The asymptotic law is about *Gaussian random exposing directions*, not uniformly chosen vertices or points of the body.

## Assumptions and scope
The metric is the standard Euclidean metric on the displayed coordinate realization of \(F_n\). Gaussian directions are equivalent to uniform spherical directions because multiplying a nonzero direction by a positive scalar does not change the exposed face. Normal-cone boundary ties occur with probability zero. A support set is an arbitrary subset of \([n]\), and all asymptotic statements use integer \(n\to\infty\). The normal-cone angle probabilities in (1) hold at every finite integer \(n\ge3\). The half-support vectors are vertices because their tight pairwise inequalities on any three support indices, together with the other support pair equations and the zero coordinates, uniquely determine the vector. No additional vertices exist: at any feasible vertex, a connected component of tight pair equations not anchored by a zero coordinate must contain an odd cycle and hence be identically one-half; components without an odd cycle admit a nonzero alternating perturbation; an integral vertex can have at most one unit coordinate. The same classification is given by the half-integral odd-cycle-support criterion in Hamano--Hibi--Ohsugi, Lemma 2.2.

## Proof
**1. The objective maximum is explicit.** Fix a direction \(g\in\mathbb R^n\) without zero coordinates or ties among the finitely many vertex scores, and let \(S=\{i:g_i>0\}\). The largest score among all half-support vertices is no larger than \(\frac12\sum_{i\in S}g_i\), attained by \(h_S\) whenever \(|S|\ge3\). The largest score among the singleton vertices is \(\max_i g_i\), and the origin scores zero. If \(S\) is empty the origin wins; if \(S\) has at most two elements then \(\frac12\sum_{i\in S}g_i\le\max_i g_i\), so a singleton wins. If \(|S|\ge3\), the half-support vertex \(h_S\) wins exactly when \(\sum_{i\in S}g_i>2\max_i g_i\). The unique singleton \(e_i\) wins exactly when \(g_i>\sum_{j\ne i}(g_j)_+\), since this inequality is equivalent to its score exceeding the best half-support score, including when \(|S|\le2\). These cases exhaust all directions up to probability-zero boundaries.

**2. Exact angles and collision identity.** Independent Gaussian signs are independent fair coins and independent of the absolute coordinate values. Conditional on a specified positive support \(S\) of size \(k\ge3\), its positive coordinate values are independent half-normal variables. Thus \(\Pr(V_n=h_S)=2^{-n}q_k\). The all-negative sign orthant has probability \(2^{-n}\), proving the origin formula. By exchangeability and the singleton criterion in Step 1, every \(e_i\) has angle probability \(\alpha_n\). This proves (1); in particular all angles sum to one. For two independent objectives, the matching-vertex event is the disjoint union of matching at each possible vertex, hence its probability is the sum of squared normal-cone probabilities. Grouping half-support vectors by size proves (2) exactly.

**3. Two exponential estimates.** For \(k\ge3\), if \(q_k<1\) then at least one half-normal component exceeds or equals the sum of all others. A union bound and Markov's inequality yield
\[
1-q_k\le k\Pr\!\left(H_1\ge\sum_{j=2}^k H_j\right)
\le k\mathbb E[e^{H_1}]\bigl(\mathbb E[e^{-H_1}]\bigr)^{k-1}
=k A\rho^{k-1},
\tag{5}
\]
where \(A=2e^{1/2}\Phi(1)\) and \(\rho=2e^{1/2}\Phi(-1)<1\). For the singleton exposure probability, again by Markov's inequality,
\[
\alpha_n=\Pr\!\left(Z_1>\sum_{j=2}^n(Z_j)_+\right)
\le \mathbb E\left[e^{2Z_1-2\sum_{j=2}^n(Z_j)_+}\right]
=e^2m^{n-1},
\tag{6}
\]
where \(m=\mathbb E[e^{-2(Z_1)_+}]=\frac12+e^2\Phi(-2)<1\). The exponential moments follow by completing the Gaussian square. Direct substitution gives \((1+\rho)/2<0.9\) and \(2m^2<0.9\).

**4. The sharp collision law.** Since \(1-q_k^2\le2(1-q_k)\), the binomial theorem and (5) give
\[
\begin{aligned}
0\le 2^n-\sum_{k=3}^{n}\binom nkq_k^2
&\le \sum_{k=0}^2\binom nk+2 A\sum_{k=3}^{n}\binom nk k\rho^{k-1}\\
&\le1+n+\binom n2+2An(1+\rho)^{n-1}.
\end{aligned}
\tag{7}
\]
Divide (2) by \(2^{-n}\). The term involving half-support vertices differs from one by at most (7) divided by \(2^n\). The origin correction is \(2^{-n}\); (6) bounds the singleton correction by \(n e^4 2^n m^{2(n-1)}\). The strict inequalities following (6) prove (3), with a constant independent of integer \(n\ge3\).

**5. Uniformity and conditional support sizes.** Couple the exposed vertex with the sign support \(S\) of its Gaussian direction. The latter is an exactly uniform subset of \([n]\). The coupling outputs \(h_S\) whenever \(|S|\ge3\) and the half-support vector wins. By the first part of the theorem, the probability of failure is \(\Pr(V_n\text{ integral})=2^{-n}+n\alpha_n\). Conditioning a uniform subset to have at least three elements changes its distribution in total variation by \(2^{-n}(1+n+\binom n2)\). The coupling inequality and (6) prove (4).

Given collision at a half-support vertex \(h_S\), that support has probability proportional to \(q_{|S|}^2\). By (2) and (7), total collision probability is \(2^{-n}(1+O(n(0.9)^n))\) and the total variation distance from the uniform-subset law, including the exceptional integral collision mass, is bounded by the sum of the relative error in (7), the relative integral collision mass, and the normalization error. Each is \(O(n(0.9)^n)\). Applying the support-cardinality map contracts total variation, proving the conditional binomial approximation. The classical binomial central limit theorem proves the displayed normal limit. All bounds hold independently of finite-sample experiments.

## Verification
The standalone `verify.py` uses independent linear programming against the defining halfspaces for 1,500 Gaussian objectives in dimensions three through eight, compares the complete explicitly constructed vertex lists with active-constraint ranks and exact objective maxima, and checks the three-support Gaussian inequality against a large Monte Carlo sample. It additionally examines the three vertex classes at dimensions six, ten and sixteen. Run `python3 verify.py` with Python, NumPy and SciPy. The expected final marker is `CLIQUE_GRAPH_POLYTOPE_CHECK_PASS`. The experiments corroborate small cases but do not establish any infinite-dimensional or asymptotic statement; Steps 1--5 are the proof.

## Relationship to prior work
Liu (2024) studies the same graph polytope \(P(K_n)\) and proves an Ehrhart-theoretic conjecture; the evaluated Gaussian normal-cone spectrum and vertex collisions are different geometric statistics. Hamano, Hibi and Ohsugi (2016) characterize the half-integral graph-polytope vertices and establish Ehrhart properties; their vertex criterion is used explicitly in the proof, not claimed as new. The published result *Complete-graph fractional stable-set polytopes have a sharp seven-dimensional sphere transition* gives the exact same polytope's smallest enclosing Euclidean ball and its contact vertices. A minimum enclosing sphere is a worst-case vertex-distance statistic and does not imply the random-objective argmax probabilities in (1), their squared sum in (2), or the asymptotic uniformity (3)--(4). Related published angular-spectrum results concern different polytopes, including symmetric edge/root polytopes and graphical zonotopes. The reduction from graph-polytope vertices to Gaussian signs and half-normal dominance, and its sharp collision asymptotic, are the contributions asserted here.

## Limitations
The theorem uses only the clique graph and the standard Euclidean realization. It treats Gaussian/spherical exposing objectives rather than uniform points in the polytope, and gives no result for general graphs or arbitrary affine changes of coordinates. The quantities \(q_k\) and \(\alpha_n\) are explicitly defined finite-dimensional half-normal/Gaussian probabilities, not claimed as elementary rational numbers. The displayed exponential errors need not be optimal. General probability inequalities and the binomial central limit theorem are classical; novelty is asserted for their evaluated application to this exact polyhedral normal fan. Unindexed equivalent formulations remain possible. Independent mathematical audit has not been performed.

## References
1. F. Liu, *Proof of a conjecture on graph polytope*, arXiv:2409.11970v1, first publicly posted 2024-09-18. https://arxiv.org/abs/2409.11970
2. G. Hamano, T. Hibi and H. Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, arXiv:1603.09613v1, first publicly posted 2016-03-31. https://arxiv.org/abs/1603.09613
3. *Complete-graph fractional stable-set polytopes have a sharp seven-dimensional sphere transition*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-graph-fractional-stable-set-polytopes-have-a-sharp-seve--66ee64a01479
4. *Exact normal-cone angular spectrum under a deleted graph matching*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-normal-cone-angular-spectrum-under-a-deleted-graph-matchin--606a499d846d
