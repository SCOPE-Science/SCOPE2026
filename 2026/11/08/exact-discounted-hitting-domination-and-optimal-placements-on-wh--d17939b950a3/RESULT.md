# Exact discounted hitting domination and optimal placements on wheel graphs

## Finding

**Theorem (exact source-set profiles and cardinality optima).** Let \(n\ge4\), let \(W_{n+1}=K_1\vee C_n\) have a distinguished hub \(o\) and individually labelled rim vertices \(0,1,\ldots,n-1\) modulo \(n\), and fix \(0<\lambda<1\). For a nonempty source set \(S\), define \(h_v(S)=\mathbb E_v[\lambda^{T_S}]\) using simple random walk and its first hitting time of \(S\), where \(T_S=0\) for \(v\in S\). Set \(\eta(S)=\min_v h_v(S)\). The following formulas give \(\eta(S)\) for *every* source set, classify every fixed-cardinality maximin placement, and determine \(\delta_{\lambda,\tau}(W_{n+1})=\min\{|S|:\eta(S)\ge\tau\}\) for every \(0<\tau\le1\).

Write
\[
 c=\frac{\lambda}{3-2\lambda},\qquad
 \mu=\operatorname{arcosh}\!\left(\frac3{2\lambda}\right),\qquad
 p_{m,j}=\frac{\cosh(\mu(j-m/2))}{\cosh(\mu m/2)},
\]
for integers \(m\ge2\) and \(1\le j<m\). Let \(q_1=0\), and for \(m\ge2\) put
\[
 q_m=\sum_{j=1}^{m-1}p_{m,j}
 =\coth(\mu/2)\tanh(\mu m/2)-1.
\]
Let \(\psi_1=1\) and, for \(m\ge2\),
\[
 \psi_m=\begin{cases}
 1/\cosh(\mu m/2),&m\text{ even},\\
 \cosh(\mu/2)/\cosh(\mu m/2),&m\text{ odd}.
 \end{cases}
\]
For a source set having \(k\ge1\) rim sources, list the cyclic edge-gaps between consecutive rim sources as \(m_1,\ldots,m_k\ge1\), with \(\sum_i m_i=n\). Put \(M=\max_i m_i\) and \(Q=\sum_i q_{m_i}\). The exact worst-vertex support is
\[
 \eta(S)=\begin{cases}
 c+(1-c)\psi_M,&o\in S,\\
 \min\left\{X,\;cX+(1-cX)\psi_M\right\},&o\notin S,
 \end{cases}
 \qquad
 X=\frac{\lambda(k+Q)}{n-\lambda c(n-k-Q)}.
\]
The hub-only set has \(\eta(\{o\})=c\). Thus these formulas give a necessary-and-sufficient test for every source set at any threshold.

For \(1\le k\le n\), put \(a=\lfloor n/k\rfloor\), \(b=n-ka\), \(L=\lceil n/k\rceil\), and
\[
 Q_{n,k}=(k-b)q_a+bq_{a+1},\quad
 X_{n,k}=\frac{\lambda(k+Q_{n,k})}{n-\lambda c(n-k-Q_{n,k})},
 \quad U_{n,k}=\min\{X_{n,k},\;cX_{n,k}+(1-cX_{n,k})\psi_L\}.
\]
Among all placements with exactly \(k\) rim sources **and no hub**, the maximum of \(\eta(S)\) equals \(U_{n,k}\); the *only* maximizing configurations are the cyclically balanced gaps, namely \(k-b\) gaps of length \(a\) and \(b\) of length \(a+1\). Their exact number on a labelled rim is
\[
 \frac nk\binom{k}{b}.
\]
Among placements with the hub and exactly \(k\ge1\) rim sources, the maximum is
\[
 H_{n,k}=c+(1-c)\psi_L,
\]
and the complete maximizing class consists of configurations whose every rim gap is at most \(L\). The number of these configurations is
\[
 \frac nk[x^n]\left(x+x^2+\cdots+x^L\right)^k.
\]
For \(k=0\), set \(H_{n,0}=c\) (the unique hub-only configuration). In particular, the exact discounted hitting domination number is
\[
 \boxed{\delta_{\lambda,\tau}(W_{n+1})=
 \min\left\{\min_{1\le k\le n\,:\,U_{n,k}\ge\tau}k,\quad
 1+\min_{0\le k\le n\,:\,H_{n,k}\ge\tau}k\right\}.}
\]
Here each minimum is taken over the explicitly indicated finite, nonempty feasible set or is \(+\infty\) if its set is empty. In the hub branch \(\min k=0\) when \(\tau\le c\); otherwise it equals \(\lceil n/L_H\rceil\), where \(L_H\) is the largest integer \(1\le m\le n\) satisfying \(c+(1-c)\psi_m\ge\tau\). This is a finite exact formula involving at most \(n\) rim-cardinality evaluations, rather than an optimization over all subsets.

The hub is not always present in an optimal solution. At \(n=4\), \(\lambda=1/2\), and \(\tau=1/3\), the optimum is exactly two sources, and its **only** two placements are the opposite rim pairs \(\{0,2\}\) and \(\{1,3\}\); neither uses the hub.

## Assumptions and scope

Graphs are finite, unweighted, simple, undirected, with rim size \(n\ge4\). The walk moves uniformly among neighbors. The discount satisfies \(0<\lambda<1\), the requested uniform support floor \(0<\tau\le1\), and hitting time is zero at any initially selected source. A source has support one. Only nonempty source sets are considered. All counts distinguish labelled rim vertices and do not quotient out rotations. A rim gap is the number of *rim edges* from one selected rim vertex to the next in cyclic order; for a lone rim source its gap is \(n\).

## Proof

**Pinned-equilibrium reduction.** First-step conditioning gives the unique solution to \(h_v=1\) for \(v\in S\) and \(h_v=\lambda\deg(v)^{-1}\sum_{w\sim v}h_w\) otherwise. Uniqueness follows from the strict contraction factor \(\lambda<1\) on the unpinned coordinates. For a rim interval between consecutive pinned rim sources let \(x\) denote hub support. Every interior rim coordinate satisfies
\[
 y_j=\frac\lambda3(y_{j-1}+y_{j+1}+x),\qquad y_0=y_m=1.
\]
The constant particular solution is \(cx\), since \(c=\lambda/(3-2\lambda)\). With \(\cosh\mu=3/(2\lambda)\), the unique two-ended homogeneous solution is
\[
 y_j=cx+(1-cx)p_{m,j}.
\]
This is also valid on a one-edge gap, where no interior coordinate occurs.

The sequence \(p_{m,j}\) is symmetric about the gap midpoint and decreases from each endpoint toward the midpoint. Its minimum over the interior is \(\psi_m\) when \(m\ge2\), and with no interior vertices \(\psi_1=1\). The hyperbolic geometric sum gives
\[
 \sum_{j=1}^{m-1}p_{m,j}
 =\frac{\sinh((m-1)\mu/2)}{\sinh(\mu/2)\cosh(m\mu/2)}
 =\coth(\mu/2)\tanh(m\mu/2)-1=q_m.
\]
The minimum of the non-source rim coordinates thus occurs at the midpoint(s) of a longest source-to-source gap, because \(\psi_m\) strictly decreases with integer \(m\ge1\). The strict decrease follows directly from the displayed hyperbolic formulas, checking the even-to-odd and odd-to-even steps.

**Hub selected.** Now \(x=1\), giving \(\eta(S)=c+(1-c)\psi_M\) for any set containing rim sources; the special hub-only case gives the constant solution \(h_v=c\) on the rim. Consequently minimizing the largest gap maximizes worst support, and the least attainable largest gap with \(k\) rim sources is \(L=\lceil n/k\rceil\). Every configuration attaining this largest gap (and no others) is optimal. To count them, root a cyclic sequence of \(k\) gaps at a chosen source: there are \([x^n](x+\cdots+x^L)^k\) rooted gap sequences and \(n\) choices for the root, while each labelled source set is rooted \(k\) ways. This proves the exact counting formula.

**Hub not selected.** Sum the rim supports. The \(k\) pinned rim vertices contribute \(k\). Summing interiors of all gaps gives the total \(k+Q+cx(n-k-Q)\). The hub first-step equation is
\[
 x=\frac\lambda n\bigl(k+Q+cx(n-k-Q)\bigr).
\]
Its unique solution is \(X\) as displayed, because the denominator is at least \(n(1-\lambda c)>0\). Comparing the hub coordinate to the minimum rim coordinate gives \(\eta(S)=\min\{X,cX+(1-cX)\psi_M\}\), as claimed.

**Strict balancing of hub-free placements.** The gap-sum function \(m\mapsto q_m=\coth(\mu/2)\tanh(\mu m/2)-1\) is *strictly concave* on positive integers. Whenever two gaps differ by at least two, transfer one edge from the longer gap to the shorter one. Their total remains unchanged, their contribution to \(Q\) strictly increases, and the largest gap \(M\) does not increase. For fixed \(n,k\),
\[
 \frac{dX}{dQ}=\frac{\lambda n(1-\lambda c)}{[n-\lambda c(n-k-Q)]^2}>0.
\]
Both the hub coordinate \(X\) and the worst rim coordinate \(cX+(1-cX)\psi_M\) strictly increase under the transfer: the latter is strictly increasing in \(X\) whenever \(M>1\), and nondecreasing in \(\psi_M\). A transfer is possible only when \(M\ge3\). Thus \(\eta(S)\) increases strictly. Iterating terminates exactly when gaps differ by at most one, proving both optimality and exclusivity of balanced patterns. Their \(Q\) is \(Q_{n,k}\), giving \(U_{n,k}\).

To count balanced patterns, there are \(\binom kb\) ordered gap words with \(b\) long gaps, and the same source-rooting count gives \(n\binom kb/k\) distinct labelled rim subsets. This quotient is an integer by the combinatorial interpretation. Taking the better of each possible hub-state/cardinality optimum proves the formula for \(\delta_{\lambda,\tau}\). When \(\tau>c\), monotonicity of \(\psi_m\) gives the explicit hub-branch cutoff \(L_H\) and its required number of rim sources.

**Sharp hub-exclusion example.** At \(n=4\) and \(\lambda=1/2\), \(c=1/4\). Opposite rim pairs have gaps \(2,2\), hub support \(8/23\), and minimum rim support \(9/23\), so they meet \(\tau=1/3\). Adjacent pairs have gaps \(1,3\) and hub support \(6/19<1/3\), so do not. Hub-plus-one-rim placements have minimum support \(5/17<1/3\), the hub alone has \(1/4\), and every singleton rim placement also fails the threshold. Hence the only optimal sets are the two opposite pairs.

## Verification

The included standalone script `verify.py` independently constructs the original wheel and solves the unpinned equilibrium linear equations for every nonempty source set on each wheel with \(4\le n\le8\) at \(\lambda\in\{1/5,1/2,4/5\}\). It compares these directly computed minima with the closed source-set formula, then checks each hub-state/cardinality maximin and its exact optimizer count. Its final checks enumerate the exceptional five-vertex wheel example with rational arithmetic.

To replay: `python3 verify.py` (requires Python 3 and NumPy). The recorded output was:

```text
DIRECT_EQUILIBRIUM_OK 2961 source_sets
BALANCED_MAXIMIN_AND_OPTIMIZER_COUNTS_OK 105 cardinality_cases
EXACT_HUB_FREE_OPTIMUM_OK 2 configurations
VERIFY_OK
```

The exhaustive finite computations corroborate, but do not substitute for, the proof of the infinite family. The claimed parameter range is established by the elementary recurrence and concavity arguments, not by numerical extrapolation.

## Relationship to prior work

Allagan, Pereyra, and Massey introduced discounted hitting domination for general graphs, proved the pinned-equilibrium and first-hitting interpretation, established complexity and approximation relationships, and gave exact algorithms for spiders; their paper's Section 5 contains the related degree-two path gap potential. The present theorem uses that *existing* probabilistic framework and elementary linear-recurrence method, but a wheel has a degree-three rim and a non-source hub that couples all source gaps through an unknown global coordinate. The exact wheel maximin classification, balanced-gap optimality for all real discount parameters, optimizer counts, and hub-free optimum are not supplied by those known general statements or the investigated spider and star results.

Guo and coauthors study group hitting-probability queries and target-set proximity, which provide a related interpretation but not this exact minimum-cardinality worst-vertex wheel covering classification. Previously published results for other graph families or directed cycles do not imply the claimed wheel recurrence, and search alone cannot establish absolute historical uniqueness. The result's contribution is the full wheel-specific solution, not the prior definition of the support potential, its general monotonicity, or the generic use of hyperbolic gap solutions.

## Limitations

The theorem assumes uniform simple random walk, homogeneous \(0<\lambda<1\), a wheel with at least four rim vertices, and the stated support-floor formulation. It does not determine analogous optima for weighted wheels, directed walks, nonuniform fidelity or general cones. The counting results concern *fixed-cardinality maximin* placements, not the number of all threshold-feasible supersets at every parameter pair. Relative priority is qualified by incomplete indexing and uninspected related literature; no independent mathematical audit has been performed.

## References

1. J. D. Allagan, K. Pereyra, and W. A. Massey, *Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms*, arXiv:2609.31535v1, first publicly submitted 2026-09-25. https://arxiv.org/abs/2609.31535
2. Q. Guo et al., *Efficient Algorithms for Group Hitting Probability Queries on Large Graphs*, IEEE Transactions on Knowledge and Data Engineering, DOI 10.1109/TKDE.2023.3349164. https://doi.org/10.1109/TKDE.2023.3349164
3. *Random-walk domination in large graphs: problem definitions and fast solutions*, arXiv:1302.4546. https://arxiv.org/abs/1302.4546
