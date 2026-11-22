# A single biased site creates a macroscopic last-coverage profile on a cycle

## Finding

Fix an integer \(n\ge3\). On the cycle with vertices \(0,1,\ldots,n-1\), start a discrete-time nearest-neighbor walk at \(0\). At \(0\), let its clockwise step probability be \(p\in(0,1)\); at every other vertex let both directions have probability \(1/2\). Put \(q=1-p\), and let \(L_n\in\{1,\ldots,n-1\}\) be the last newly visited vertex at complete coverage.

For every integer \(1\le k\le n-1\), its **exact tail and mass laws** are

\[
\Pr(L_n\ge k)=\frac{(n-k)p}{(k-1)q+(n-k)p},
\qquad
\Pr(L_n=k)=\frac{(n-1)pq}{D_kD_{k+1}},
\tag{1}
\]
where \(D_k=(k-1)q+(n-k)p\) and \(D_{n}=(n-1)q\). As a consequence, for \(p>1/2\) the masses increase strictly with \(k\), for \(p<1/2\) they decrease strictly, and for \(p=1/2\) they equal \(1/(n-1)\). The law increases strictly in first-order stochastic order with \(p\): for each \(2\le k\le n-1\), \(\Pr(L_n\ge k)\) is a strictly increasing function of \(p\).

The *local* asymmetry remains visible on the *macroscopic* scale. With fixed \(p\in(0,1)\), as \(n\to\infty\),

\[
\frac{L_n}{n-1}\ \Rightarrow\ U_p,
\qquad
\Pr(U_p\le u)=\frac{uq}{(1-u)p+uq},
\qquad
f_p(u)=\frac{pq}{((1-u)p+uq)^2},\quad 0\le u\le1.
\tag{2}
\]

Let \(\mathsf U_{n-1}\) be uniform on \(\{1,\ldots,n-1\}\). The endpoint law has the **nonvanishing total-variation separation**

\[
\boxed{\lim_{n\to\infty}d_{\mathrm{TV}}\bigl(\mathcal L(L_n),\mathsf U_{n-1}\bigr)
=\frac{|\sqrt p-\sqrt q|}{\sqrt p+\sqrt q}.}
\tag{3}
\]

Thus a fixed asymmetry at one vertex—only one of \(n\) transition rules—produces a nonuniform limiting *position* of the last newly discovered site. In contrast, with equal bias applied at every site the last-coverage law is geometric and concentrates near one end at fixed nonzero drift; the one-defect law remains spread over a positive fraction of the cycle.

## Assumptions and scope

The walk has no holding, is time-homogeneous, and takes clockwise and counterclockwise edges modulo \(n\). The transition from \(0\) has probabilities \(p,q\), and every transition from a nonzero vertex has probabilities \(1/2,1/2\). This chain is irreducible for \(0<p<1\), hence its finite-state cover time is finite almost surely. The starting site is the exceptional site, labels are oriented clockwise, and the endpoint is the vertex visited *for the first time* at the cover time. The theorem does not address arbitrarily many defects or a defect whose position varies separately from the start. The limit keeps \(p\) fixed, and the total-variation comparison uses the discrete uniform law rather than a continuous one.

## Proof

**1. The last vertex is determined by a two-point race.** Fix \(2\le k\le n-1\), and denote the first visit to vertex \(j\) by \(\tau_j\). The walk visits only neighboring vertices, and its visited set is always a cyclic arc containing \(0\) before coverage. If it hits \(k-1\) before \(k\), then the clockwise arc \(0,1,\ldots,k-1\) has been visited while \(k\) has not. Every still-unvisited site consequently belongs to \(\{k,\ldots,n-1\}\), so the last newly visited site is at least \(k\). Conversely, if it hits \(k\) before \(k-1\), its first arrival at \(k\) must come through \(n-1,n-2,\ldots,k\); the remaining undiscovered sites lie among \(\{1,\ldots,k-1\}\). The events are exhaustive because visiting either vertex first cannot be simultaneous. Therefore

\[
\{L_n\ge k\}=\{\tau_{k-1}<\tau_k\}.
\tag{4}
\]

**2. Harmonic splitting at the defect.** Write \(h_i=\Pr_i(\tau_{k-1}<\tau_k)\). The path between the absorbing vertices \(k\) and \(k-1\), going through \(0\), has the two arms \(k,k+1,\ldots,n-1,0\) and \(0,1,\ldots,k-1\). Except at \(0\), the harmonic equation \(h_i=(h_{i-1}+h_{i+1})/2\) forces the restriction of \(h\) on each arm to be affine. With \(h=h_0\), the neighboring values are

\[
h_1=h+\frac{1-h}{k-1},\qquad
h_{n-1}=h-\frac{h}{n-k}.
\]

The defect equation is \(h=p h_1+q h_{n-1}\), whence

\[
\frac{p(1-h)}{k-1}=\frac{qh}{n-k}
\quad\Longrightarrow\quad
h=\frac{(n-k)p}{(k-1)q+(n-k)p}.
\]

Both denominators are positive because \(2\le k\le n-1\) and \(0<p<1\). For \(k=1\), the tail is identically one, in agreement with the same formula. This proves the first half of (1) for all claimed indices.

**3. Exact masses, strict monotonicities.** Set \(D_k=(k-1)q+(n-k)p\) for \(1\le k\le n\) and \(S_k=(n-k)p/D_k\), taking \(S_n=0\). Then \(\Pr(L_n=k)=S_k-S_{k+1}\). The numerator of this difference is exactly \((n-1)pq\), proving the second half of (1), including the endpoint indices. The consecutive denominators satisfy \(D_{k+1}-D_k=q-p\). Hence \(\Pr(L_n=k)\) is strictly increasing in \(k\) if \(p>q\), strictly decreasing if \(p<q\), and constant when \(p=q\). For \(2\le k\le n-1\), differentiation with \(q=1-p\) yields

\[
\frac{d}{dp}\Pr(L_n\ge k)=
\frac{(k-1)(n-k)}{((k-1)q+(n-k)p)^2}>0,
\]

which establishes the strict stochastic ordering (the \(k=1\) tail is trivially constant).

**4. Scaling limit and its density.** For \(u\in(0,1)\), take \(k=\lceil(n-1)u\rceil\). The exact tail converges to

\[
\Pr(U_p\ge u)=\frac{(1-u)p}{(1-u)p+uq}.
\]

This is continuous and defines the claimed distribution function; differentiating gives the positive density in (2). At the endpoints, the CDF has limits zero and one. This proves weak convergence.

**5. Exact limiting total variation.** Partition \([0,1]\) into \(n-1\) intervals of equal length. On the interval indexed by \(k\), define the step density \(f_{n,p}(u)=(n-1)\Pr(L_n=k)\). By (1), with \(a=(k-1)/(n-1)\) and \(b=k/(n-1)\),

\[
f_{n,p}(u)=\frac{pq}{[p+(q-p)a][p+(q-p)b]}.
\tag{5}
\]

Because \(\min(p,q)>0\), this converges uniformly to \(f_p(u)\). The total-variation distance in (3) equals \(\tfrac12\int_0^1|f_{n,p}(u)-1|\,du\), and therefore tends to \(\tfrac12\int_0^1|f_p(u)-1|\,du\). If \(p=q\), this integral is zero. Otherwise the unique crossing \(f_p(u)=1\) is at

\[
u_*=\frac{\sqrt p}{\sqrt p+\sqrt q},
\qquad
\Pr(U_p\le u_*)=\frac{\sqrt q}{\sqrt p+\sqrt q}.
\]

The area between the CDF of \(U_p\) and the uniform CDF at this single crossing equals the total variation, yielding (3). Every step is an equality or a uniform-limit argument with a positive denominator, completing the proof.

## Verification

The standalone `checker.py` uses exact rational arithmetic in two independently formulated finite-state computations: an absorbing Dirichlet linear system for the first-hitting race, and a full visited-mask Markov system that tracks the identity of the last newly visited vertex without using the two-point reduction. For \(3\le n\le21\), five rational biases were checked against the exact tail and mass laws; for \(3\le n\le7\), twenty full-cover Markov systems were checked. The recorded execution completed **3330 exact assertions**. The checks verify algebra and model interpretation for the sampled finite cases, not the universal result, which follows from the analytic proof above.

Reproduce using `python3 checker.py` in the same directory; no external packages or online data are needed. The recorded JSON output is `verification_output.json`.

## Relationship to prior work

Idnani and Salem (arXiv:2610.15115v1, first posted October 10, 2026) study final discovery for cycles with spatially homogeneous constant bias and with deterministic *time-dependent*, spatially homogeneous bias. Their constant-bias terminal law is geometric. Here the bias is *spatially localized at one site* and persists across revisits; even at fixed nonzero bias, the endpoint has a continuum-scale law and a nonzero total-variation separation from uniform. The available abstract does not cover this setting; the full source was not accessible for a definitive full-text comparison. Neither the connected-arc property nor ordinary one-dimensional gambler's ruin is claimed to be new.

Buchanan, Horn and Rombach (Discrete Mathematics Letters 11 (2023), 96–98) classify directed *unweighted* graphs with uniform terminal distributions when walks choose uniformly among outgoing neighbors; this cannot yield the nonuniform weighted transition law at a single site. The published conductance-cycle result *Cover-endpoint tomography of conductance cycles: exact law and inverse rigidity* treats reversible walks: its edge parameters must satisfy zero affinity around the ring. Our transition probabilities have multiplicative clockwise/counterclockwise affinity \(p/q\ne1\) for \(p\ne1/2\), so the reversible formulas cannot be specialized to (1)–(3). Another published result, *A parity-resolved last-coverage law for alternating zero-drift walks on cycles*, uses a **time-alternating** common bias rather than one exceptional spatial transition rule. Its parity-split distribution does not imply this smooth macroscopic profile.

## Limitations

The defect is exactly at the starting vertex, all other sites are unbiased, and \(p\) is held fixed for asymptotics. The result does not derive the joint law with cover time or cover times themselves, nor does it cover multiple defects or arbitrary spatial biases. The main calculation uses classical harmonic techniques; the asserted advance is the exact one-defect distribution and its global scale/total-variation consequence, not the underlying technique. Prior priority remains subject to the inaccessible full text of the 2026 motivating paper and any unindexed nonreversible spatial-disorder work. No independent proof review has been undertaken.

## References

1. K. Idnani and J. Salem, *Last-Coverage Probabilities of Random Walks on Cycle Graphs for Symmetric, Biased, and Time-Dependent Walks*, arXiv:2610.15115v1 (first posted October 10, 2026). https://arxiv.org/abs/2610.15115
2. C. Buchanan, P. Horn and P. Rombach, *On the last new vertex visited by a random walk in a directed graph*, Discrete Mathematics Letters 11 (2023), 96–98. https://www.dmlett.com/archive/v11/DML23_v11_pp96-98.pdf
3. *Cover-endpoint tomography of conductance cycles: exact law and inverse rigidity*, published mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cover-endpoint-tomography-of-conductance-cycles-exact-law-and-in--93e0815cb503
4. *A parity-resolved last-coverage law for alternating zero-drift walks on cycles*, published mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-parity-resolved-last-coverage-law-for-alternating-zero-drift-w--bd1a2327f361
5. L. Lovász and P. Winkler, *A note on the last new vertex visited by a random walk*, Journal of Graph Theory 17 (1993), 593–596. https://doi.org/10.1002/jgt.3190170505
