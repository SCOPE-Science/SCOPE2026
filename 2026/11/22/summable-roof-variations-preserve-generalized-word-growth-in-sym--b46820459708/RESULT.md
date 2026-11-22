# Summable roof variations preserve generalized word-growth in symbolic suspensions
## Finding
Let \(A\) be a finite alphabet and \(\Lambda\subseteq A^{\mathbb Z}\) a nonempty two-sided subshift. Let \(p(n)=|\{x_{[0,n-1]}:x\in\Lambda\}|\). For \(k\ge0\), put
\[
\operatorname{var}_k(r)=\sup\{|r(x)-r(y)|:x_{[-k,k]}=y_{[-k,k]}\}.
\]
If a positive roof \(r:\Lambda\to(0,\infty)\) has \(\sum_{k\ge0}\operatorname{var}_k(r)<\infty\), the suspension time map \(f_t=\Phi_r^t\), for each fixed \(t\ne0\), satisfies two-sided orbit-complexity comparisons with the base word complexity. More precisely, for some \(\varepsilon_0,c>0\) and all large \(n\),
\[
\operatorname{sep}_{f_t}(n,\varepsilon_0)\ge p(\lfloor cn\rfloor),
\]
while for each \(\varepsilon>0\), some \(C_\varepsilon>0\) and \(C>0\) satisfy
\[
\operatorname{span}_{f_t}(n,\varepsilon)\le C_\varepsilon p(\lceil Cn\rceil).
\]
Consequently, if \(\sup_{n\ge1}p(2n)/p(n)<\infty\), the generalized-entropy growth class of every nonzero time map is exactly
\[
\boxed{o(f_t)=\llbracket p(n)\rrbracket.}
\]
The result includes positive Hölder and more general summable-variation roofs of genuinely infinite symbolic range; no roof cohomology, minimality, or mixing hypothesis is required.

## Assumptions and scope
The suspension is
\[
M_r=\{(x,s):x\in\Lambda,\ 0\le s\le r(x)\}/((x,r(x))\sim(\sigma x,0)),
\]
with the induced unit-speed continuous flow. Use any compatible metric on its compact space. Its \(n\)-sample Bowen metric for \(f_t\) is \(d_n(z,w)=\max_{0\le j<n}d(f_t^jz,f_t^jw)\). The spanning and separated numbers are the minimum cardinality of an \((n,\varepsilon)\)-spanning family and maximum cardinality of an \((n,\varepsilon)\)-separated family respectively. Changing a compatible metric does not change the resulting order of growth. The notation \(\llbracket a(n)\rrbracket\) means comparison up to positive multiplicative constants for all sufficiently large \(n\). Put \(m=\min r>0\), \(M=\max r<\infty\), and \(V_K=\sum_{j\ge K}\operatorname{var}_j(r)\to0\). No differentiability or finite-memory assumption is used.

## Proof
**1. Uniform roof drift for long matching blocks.** Suppose \(x,y\) agree at every coordinate in \([-K,N+K]\). For each \(0\le j\le N\), their shifts \(\sigma^j x,\sigma^j y\) agree on the central radius \(K+\min(j,N-j)\). Consequently, for every \(0\le h\le N\),
\[
\left|\sum_{j=0}^{h-1}r(\sigma^jx)-\sum_{j=0}^{h-1}r(\sigma^jy)\right|
\le\sum_{j=0}^{N}\operatorname{var}_{K+\min(j,N-j)}(r)\le2V_K.
\tag{1}
\]
This is uniform in \(N,h,x,y\). In particular, if \(K\) is large, a pair with the same long block has nearly synchronous crossings of corresponding roof sections throughout that block.

**2. Upper spanning bound.** Fix a small desired metric scale \(\varepsilon\). Compactness of the quotient suspension and positivity of \(m\) give a uniform local-flow-box scale \(\delta>0\) and a finite symbolic radius \(J\): if two representatives' base sequences agree on \([-J,J]\), their physical heights differ by less than \(\delta\), and their roof-section indices are identical (or differ by one only while both points are within \(\delta\) of the corresponding glued boundary), then the quotient points are \(\varepsilon\)-close. Choose \(K\ge J+2\) with \(2V_K<\delta/4\) and \(\operatorname{var}_K(r)<\delta/4\). For a continuous-time observation interval \([0,T]\), take \(N=\lceil T/m\rceil+2\). For every admitted block on \([-K-J,N+K+J]\), choose one representative \(x^w\). Quantize the initial normalized height \(s/r(x)\in[0,1]\) using a fixed mesh smaller than \(\delta/(4M)\). For any point \([x,s]\), choose its block representative and closest normalized height. The initial physical-height error is smaller than \(\delta/2\), including the small roof-value difference. By (1), all corresponding section-crossing times up to \(T\) differ by less than \(\delta\). At each physical time up to \(T\), either both points are in the same section slab with base words agreeing at radius \(J\), or they lie within \(\delta\) of the same quotient seam; in both cases they are \(\varepsilon\)-close. There are at most \(C_\varepsilon p(N+2K+2J+1)\) representatives. Since \(p(N+B)\le |A|^B p(N)\) for each fixed \(B\), this is at most \(C'_\varepsilon p(\lceil T/m\rceil+2)\). It spans the sampled orbit at times \(0,t,\ldots,(n-1)t\) when \(T=|t|n\), yielding the upper assertion (for positive \(t\); reverse coordinates for negative \(t\)).

**3. Lower separated bound.** We record the standard flow-box crossing argument explicitly. The global section \(S=\{[x,0]:x\in\Lambda\}\) is homeomorphic to \(\Lambda\). Choose \(0<\delta<m/8\). The map \((x,u)\mapsto\Phi_r^u[x,0]\) is a flow box for \(|u|<2\delta\). Compactness, disjointness of the clopen central-symbol cylinders in \(S\), and uniform continuity imply the existence of \(\varepsilon_0>0\) such that two orbits beginning on \(S\) and remaining \(\varepsilon_0\)-close at all matching physical times have corresponding section crossings within \(\delta\) of each other, with the same central symbol. Indeed, at a crossing of either orbit the other is then in the same flow box; its nearest crossing is within \(\delta\), and its central symbol agrees. Since crossings of either orbit are separated by at least \(m>8\delta\), this correspondence is order-preserving, cannot skip or duplicate a crossing, and starts at crossing index zero. Thus the initial symbolic itineraries agree at least through every crossing occurring before \(T-2\delta\) if the orbits stay close on \([0,T]\). Each roof interval lasts at most \(M\). Hence, for \(N=\lfloor (T-2\delta)/M\rfloor-1\), choosing one section point \([x^w,0]\) for each distinct admitted length-\(N\) word gives \(p(N)\) continuous-time \((T,\varepsilon_0)\)-separated points.

For the discrete time map, uniform continuity of \(\Phi_r^u\) on the compact suspension, uniformly over \(0\le u\le|t|\), gives \(\varepsilon_1>0\) such that if sampled orbits are \(\varepsilon_1\)-close at times \(j|t|\), then they remain \(\varepsilon_0\)-close between samples. Therefore the same representative set is \((n,\varepsilon_1)\)-separated for \(f_t\), with \(T=(n-1)|t|\). This proves the lower bound with any sufficiently small \(c<|t|/M\).

**4. Bounded doubling.** If \(D=\sup_n p(2n)/p(n)<\infty\), monotonicity and iterated doubling show \(p(\lfloor cn\rfloor)\asymp p(n)\asymp p(\lceil Cn\rceil)\) for every fixed \(c,C>0\). The two previous estimates force the generalized-entropy class of \(f_t\) to equal \(\llbracket p(n)\rrbracket\). The negative-time case follows by applying the same proof to the reversed base shift and roof (which has the same \(p(n)\) and variations).

## Verification
The key inequality (1) is a finite double-tail count: each variation radius \(K+\ell\) occurs at most twice, independent of the matched block length. This count verifies the only nonstandard quantitative input and is not extrapolated from sample sizes. The global-section crossing argument needs only continuous positive roofs and the compact flow-box geometry; it supplies the lower bound independent of the summable-variation condition. Upper spanning uses precisely the small cumulative drift from (1). As a sanity example, the Fibonacci/Sturmian subshift has \(p(n)=n+1\); for the infinite-range positive roof
\[
r(x)=2+\sum_{j=1}^{\infty}4^{-j}x_{-j}x_j,
\]
we have \(\operatorname{var}_k(r)\le\sum_{j>k}4^{-j}=4^{-k}/3\), so all its nonzero suspension time maps have generalized entropy \(\llbracket n\rrbracket\). This example is not asserted to be noncohomologous to a locally constant roof. No finite experiment is invoked as a proof.

## Relationship to prior work
Corrêa and Lacerda (arXiv:2611.13420v1, public November 10, 2026) prove the constant-roof suspension formula in Theorem C and explicitly ask in Remark 5.8/Section 7.4 whether bounded doubling suffices for arbitrary continuous variable roofs. Their argument requires synchronized section crossings. The present proof gives the missing uniform drift control under summable cylinder variations, so it treats infinite-range roofs; it does not answer the arbitrary-continuous case.

The previously established locally constant roof result provides a finite-memory case, where equal long words give literally identical interior return times. It does not imply the summable-variation case by uniform approximation, since a uniformly small per-step roof error can accumulate linearly in observation time. The independent Dini-roof result on full-shift suspensions, described in the cited published-finding corpus record, proves a local product-structure criterion, not a comparison of Bowen covering growth to subshift word complexity; it also concerns a positive-entropy full shift, whose exponential word growth lacks bounded doubling. The present statement follows a different growth-invariant question. Classical Bowen--Walters flow-box geometry is acknowledged; the new point is its uniform combination with the block-variation bound and generalized entropy.

## Limitations
The roof is required to have summable centered cylinder variations. The theorem does not settle the case of arbitrary continuous roofs, nor establish necessity or an optimal regularity threshold. It does not address flow mixing or local product structure. No independent mathematical audit is claimed. Older results phrased as slow-entropy invariance under regular time changes could potentially subsume this theorem; the inspected sources and database comparisons did not establish such an implication.

## References
1. H. Corrêa and G. Lacerda, *Minimal dynamics with polynomial and intermediate complexity*, arXiv:2611.13420v1, first public 2026-11-10; Theorem C, Proposition 5.3, Remark 5.8, Section 7.4 (full HTML inspected at https://arxiv.org/html/2611.13420).
2. X. Wen, *Local Product Structure of Expansive Flows with Shadowing Property*, arXiv:2608.26561v1, first public 2026-08-27; classical Bowen--Walters roof geometry and regularity setting as discussed in the related published Dini-roof result.
3. R. Bowen and P. Walters, *Expansive one-parameter flows*, J. Differential Equations 12 (1972), 180–193, for the standard flow-box suspension framework.
4. *Dini roofs retain local product structure for full-shift suspensions*, public published-finding corpus finding 2026/10/11/SCOPE-dini-roofs-retain-local-product-structure-for-full-shift-suspens--5a62f6726832; RESULT.md read in full for statement-level comparison.
