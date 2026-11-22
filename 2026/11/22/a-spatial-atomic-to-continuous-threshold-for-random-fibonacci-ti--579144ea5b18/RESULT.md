# A spatial atomic-to-continuous threshold for random Fibonacci tiling coverage

## Finding
Consider the fair, cyclic random Fibonacci tiling of Amit, Gebre, Housholder, Khan, Miller, Upton and Yau in any fixed dimension \(d\ge2\). Choose a coordinate \(r\), and let \(w_j=F^{(d)}_{d-1+r+jd}\) be its successive positive-face extension lengths. Write \(W_m=\sum_{j=0}^{m-1}w_j\), with \(W_0=0\), and let \(D_m\) be an **independent uniform lattice distance** on the first-feasible annulus
\[
\{W_{m-1}+1,\ldots,W_m\},\qquad m\ge1.
\]
For a fixed distance \(\delta\), put
\[
K_m(\delta)=\Pr\!\left(\sum_{j=0}^{m-1}B_jw_j<\delta\right),\qquad B_j\ \text{iid Bernoulli}\left(\frac12\right),
\]
and define the random *conditional failure probability* \(K_m=K_m(D_m)\). The randomness of \(K_m\) is solely the uniformly selected target; the fair tiling flips have already been averaged out. This is the chance that the target is not covered in the selected coordinate by its earliest feasible update.

**Exact finite-scale law.** Put \(g_j=w_j-\sum_{i<j}w_i>0\). For each \(m\ge1\), the entire distribution is
\[
\Pr(K_m=\tfrac12)=\frac{g_{m-1}}{w_{m-1}},
\qquad
\Pr\!\left(K_m=\tfrac12+\frac{t}{2^m}\right)
=\frac{g_{\nu_2(t)}}{w_{m-1}}
\quad(1\le t<2^{m-1}),
\]
where \(\nu_2(t)\) is the number of trailing zero digits in the binary expansion of the positive integer \(t\). There are no other values.

**Limiting spatial law.** Let \(\rho_d>1\) be the positive root of \(x^d-x^{d-1}-1=0\), put \(Q_d=\rho_d^d>2\), and \(\gamma_d=(Q_d-2)/(Q_d-1)=2-\rho_d\). Then \(K_m\) converges **in total variation** to a purely atomic probability law \(\mathcal L_d\) with
\[
\mathcal L_d\{\tfrac12\}=\gamma_d,
\qquad
\mathcal L_d\!\left\{\tfrac12+\frac{2i+1}{2^{j+1}}\right\}
=\gamma_dQ_d^{-j},\quad j\ge1,\quad0\le i<2^{j-1}.
\]
Its atoms are dense in \([1/2,1]\), but neither endpoint \(1\) nor any nondyadic number carries positive mass. It is independent of the coordinate \(r\). The largest atom has mass \(2-\rho_d\) at \(1/2\). The exact mean and its limit are
\[
\mathbb E K_m=\frac12+\frac{W_{m-1}}{4w_{m-1}},
\qquad
\lim_{m\to\infty}\mathbb EK_m=\frac12+\frac{\rho_d-1}{4}.
\]

**Universal doubling boundary.** The exact finite histogram and its limiting conclusion extend to *any* positive strictly superincreasing integer sequence \((w_j)_{j\ge0}\) with \(w_{j+1}/w_j\to Q\in[2,\infty)\). For \(Q>2\), the same purely atomic law holds with \(\gamma=(Q-2)/(Q-1)\) and atom weights \(\gamma Q^{-j}\). At the sharp boundary \(Q=2\), instead,
\[
K_m\ \Longrightarrow\ \operatorname{Uniform}([1/2,1]),
\]
in ordinary weak convergence (not total variation). Hence the doubling ratio separates a spatially *purely atomic* regime from a *continuous uniform* regime.

## Assumptions and scope
The deterministic order-\(d\) Fibonacci numbers satisfy \(F^{(d)}_0=\cdots=F^{(d)}_{d-1}=1\) and \(F^{(d)}_n=F^{(d)}_{n-1}+F^{(d)}_{n-d}\) for \(n\ge d\). At move \(r+1+jd\), the tiling independently extends on either face of coordinate \(r\) with equal probability; thus the distance extended toward a fixed exterior target is the sum of its Bernoulli-selected coordinate weights. A target at positive-face distance \(\delta\) may be taken at lattice coordinate \(a_r=1+\delta\), with every other coordinate inside the initial cube. Since \(w_j>W_j\), the annulus \(W_{m-1}<\delta\le W_m\) is precisely the set of distances for which \(m\) is the least feasible number of coordinate updates. We additionally sample \(D_m\) uniformly from that annulus, independently of the tiling, to measure the spatial distribution of conditional failure probabilities.

The universal extension requires only integer weights \(w_j>\sum_{i<j}w_i\), positivity, and a finite asymptotic successive ratio \(Q\ge2\). The limit \(Q=2\) is allowed; no regularity beyond the ratio limit is assumed. All random variables, indices, and measures are defined in this document.

## Proof
**Step 1: the sorted subset sums and an exact histogram.** For \(m\ge1\), let \(N=2^{m-1}\). The \(N\) subset sums of the lower weights \(w_0,\dots,w_{m-2}\), in strictly increasing order, are \(s_0=0<s_1<\cdots<s_{N-1}=W_{m-1}\). Strict superincreasingness says that their order is the binary order of the corresponding length-\((m-1)\) bit strings. For any \(\delta\in\{W_{m-1}+1,\dots,W_m\}\), every lower-half placement word (top bit zero) fails to cover, contributing \(N\) failing words out of \(2N\). A top-bit-one word fails exactly if its lower sum is less than \(\delta-w_{m-1}\). If \(\delta\le w_{m-1}\), there are no such additional words, and the number of possible distances is exactly \(g_{m-1}=w_{m-1}-W_{m-1}\). Otherwise, for \(1\le t<N\), precisely \(t\) lower sums are less than the integer \(\delta-w_{m-1}\) when
\[
s_{t-1}<\delta-w_{m-1}\le s_t,
\]
which accounts for exactly \(s_t-s_{t-1}\) integer distances. When incrementing binary rank from \(t-1\) to \(t\), the trailing \(\nu_2(t)\) ones flip to zero and the next bit flips to one. Therefore
\[
s_t-s_{t-1}=w_{\nu_2(t)}-\sum_{i<\nu_2(t)}w_i=g_{\nu_2(t)}.
\]
Since the annulus has exactly \(w_{m-1}\) lattice distances, division by this length yields the finite histogram, including the case \(m=1\). As a consistency check, its masses sum to one, since the gaps between consecutive lower subset sums telescope to \(W_{m-1}\).

**Step 2: asymptotic weights and the atomic phase.** If \(w_{j+1}/w_j\to Q>1\), then for each fixed integer \(h\ge0\), \(w_{n-h}/w_n\to Q^{-h}\). A geometric domination of the backward ratios yields
\[
\frac{W_n}{w_n}\longrightarrow\sum_{h\ge1}Q^{-h}=\frac1{Q-1},\qquad
\frac{g_n}{w_n}\longrightarrow1-\frac1{Q-1}=\frac{Q-2}{Q-1}.
\]
For \(Q>2\), the mass at \(1/2\) tends to \(\gamma\). A dyadic number \(1/2+(2i+1)/2^{j+1}\), with fixed \(j\ge1\) and \(0\le i<2^{j-1}\), is represented at finite level \(m\ge j+1\) by \(t=(2i+1)2^{m-j-1}\), so its probability is \(g_{m-j-1}/w_{m-1}\to\gamma Q^{-j}\). The proposed limit has total mass
\[
\gamma+\sum_{j=1}^{\infty}2^{j-1}\gamma Q^{-j}
=\gamma\left(1+\frac1{Q-2}\right)=1.
\]
All finite distributions are supported on the same countable set of dyadic numbers, so pointwise convergence of their masses to a probability mass function of total mass one implies convergence in total variation (discrete Scheffé lemma). The claimed dense atomic support follows from the dyadic fractions with odd numerators.

**Step 3: the sharp continuous boundary.** Assume now \(Q=2\). Couple the reversed lower bits to iid Bernoulli variables \((B_j)_{j\ge1}\), and write
\[
X_m=\sum_{j=1}^{m-1}B_j\frac{w_{m-1-j}}{w_{m-1}}.
\]
For each fixed \(j\), the weight ratio tends to \(2^{-j}\). Because the successive ratios are eventually bounded below by some constant greater than one, the tails of these reversed coefficient sums are uniformly geometrically small. Hence \(X_m\) converges in distribution to \(X=\sum_{j\ge1}B_j2^{-j}\), which is uniform on \([0,1]\). Since this limit has a continuous distribution function, the CDFs \(F_m(x)=\Pr(X_m<x)\) converge uniformly in \(x\) to the clipped identity \(F(x)=\max(0,\min(x,1))\).

Independently choose \(D_m\) uniformly from the first-feasible annulus and let \(U_m=(D_m-w_{m-1})/w_{m-1}\). Since \(W_{m-1}/w_{m-1}\to1\), the variables \(U_m\) converge to uniform \([0,1]\). The same top-bit split as in Step 1 gives the exact identity \(K_m=1/2+F_m(U_m)/2\). Uniform CDF convergence and the continuous mapping theorem imply \(K_m\Rightarrow1/2+U/2\) for \(U\) uniform on \([0,1]\), proving the continuous boundary law.

**Step 4: specialization and the mean.** For the cyclic Fibonacci tiling, the recurrence and simple dominant root imply \(w_{j+1}/w_j\to Q_d=\rho_d^d\). The root equation gives \(Q_d-1=\rho_d^{d-1}=1/(\rho_d-1)>1\), so \(Q_d>2\) and \(\gamma_d=(Q_d-2)/(Q_d-1)=2-\rho_d\). The general atomic conclusion applies for every coordinate. For the exact expectation, average the top-bit-one failure indicator over uniformly chosen \(\delta\). For any fixed lower sum \(s\), the number of distances satisfying \(s<\delta-w_{m-1}\) is \(W_{m-1}-s\); because the uniform lower subset sum has mean \(W_{m-1}/2\), this yields \(\mathbb E K_m=1/2+W_{m-1}/(4w_{m-1})\). Its limit follows from Step 2.

## Verification
The accompanying self-contained Python 3 script `check.py` uses exact integer enumeration and `fractions.Fraction` to compare the complete finite histogram with direct enumeration of random tiling placement words for multiple dimensions, coordinates and small update depths, and checks the exact mean. It also checks special geometric-weight cases and numerical predictions for fixed-depth limiting atom masses. Run `python3 check.py` from the directory containing `check.py`. A successful replay prints `PASS cumulative 845`. The finite checks only test particular instances; the universal limit and sharp boundary are proved in the preceding argument, not by computation.

## Relationship to prior work
Amit et al. [1] introduce the fair random Fibonacci tiling, prove superincreasing binary ordering of coordinate subset sums (Theorem 3.1), and compute the exact fixed-target first-feasible failure parameter and geometric delay (Theorem 3.4). Their result concerns a chosen fixed lattice target; it does **not** give the distribution of that failure parameter when the target itself is sampled uniformly from the feasibility annulus. Their moment and fixed-target asymptotic formulas (Sections 4–5) do not give the countably atomic law, its spatial weights, or the universal doubling boundary.

The published note [2] classifies all subsequential **laws of centered covering times** across arbitrarily chosen target sequences, including attainable failure parameters. It does not supply the **spatial frequencies** with which parameters occur under uniform lattice target sampling; attainability of each parameter is distinct from the exact histogram and limiting spatial probability measure. Standard Cantor functions and binary expansions [3] underpin the interpretation, and are not presented as novel here. The new contribution is the full target-averaged finite histogram and its atomic-to-continuous ratio classification, not the pre-existing superincreasing ordering or classical Bernoulli expansion.

## Limitations
Only fair independent placement decisions are considered. The spatial law uses a **single coordinate** and a uniformly sampled target **within one first-feasible annulus**, not uniform sampling in an expanding Euclidean ball, nonuniform target sampling, or the full multi-coordinate covering time. The doubling-boundary result applies to arbitrary superincreasing integer sequences, but the cyclic Fibonacci weights always lie strictly on the atomic side. There is no claim that Cantor distributions themselves or binary-carry identities are new. Full historical priority is not established beyond the searches and sources identified in the accompanying review. No external independent verification has occurred.

## References
[1] Y. Amit, A. Gebre, C. Housholder, J. Khan, S. Miller, E. Upton, C. Yau, *Random Fibonacci Tilings*, arXiv:2611.08317v1, first publicly posted 2026-11-05, https://arxiv.org/html/2611.08317v1 .

[2] *Complete subsequential covering-time laws for random Fibonacci tilings*, published mathematical record, 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-complete-subsequential-covering-time-laws-for-random-fibonacci-t--e2af1a5dfd9a/RESULT.md .

[3] *Cantor distribution*, background mathematical description, https://en.wikipedia.org/wiki/Cantor_distribution .
