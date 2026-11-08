# A sharp inverse-logarithmic physical-clock excursion tail at the critical Fibonacci bimodal map

## Finding

At the critical geometric parameter \(\lambda=1/2\) of the piecewise-linear Fibonacci bimodal interval map of Ji and Ma, begin with normalized Lebesgue measure on **one** of its four level-five monotonicity intervals. The induced dynamics makes an excursion through levels at least five before first landing at level four. The resulting excursion, measured in iterations of the **original map**, has a sharp tail:

\[
\boxed{\lim_{T\to\infty}(\log T)\,\mathbb P(R>T)=\log\varphi},\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]

The number \(\tau\) of induced steps and the maximum excursion height \(H\) have the exact, independently useful laws

\[
\mathbb P(\tau=n)=\frac{2}{4^n}\,\frac1n\binom{2n-2}{n-1},\quad
\mathbb P(\tau>n)=\frac{\binom{2n}{n}}{4^n},\qquad n\ge1,
\]

and

\[
\mathbb P(H\ge h)=\frac1{h+1}\quad(h\ge2),\qquad \mathbb P(H\ge1)=1.
\]

Thus the induced-step return tail is asymptotic to \(1/\sqrt{\pi n}\), whereas the same excursion in original-map time has a much heavier, inverse-logarithmic tail. In particular \(\mathbb E[R^q]=\infty\) for every real \(q>0\). The sharp leading constant uses the golden-ratio growth of Fibonacci inducing times; it is not inferred from induced-step recurrence alone.

## Assumptions and scope

Let \(f_\lambda:[-1,1]\to[-1,1]\) be the *specific geometrically scaled, piecewise-linear Fibonacci bimodal map* constructed in Ji and Ma, Section 4 (2023), and let \(F_\lambda\) be the induced Markov map of their Section 2.4. Their branch partition contains four types at each high level \(j\): \(W_j,\widehat W_j,V_j,\widehat V_j\). The following established defining properties of this inducing scheme are used, and no assertion is made about arbitrary maps with Fibonacci combinatorics.

For every \(j\ge3\), each branch of level \(j\) is mapped affinely onto one specified family of branches of all levels \(i\ge j-1\) (the target family varies with \(j\bmod12\)); each target branch has length \(\varepsilon_i=(1-\lambda)\lambda^{i+1}/4\). The induced map equals \(f_\lambda^{S_{j-1}}\) on every branch of level \(j\ge2\), where \(S_0=1\), \(S_1=2\), and \(S_{j+1}=S_j+S_{j-1}\). These facts are the branch-image formula in Fact 2.2 and the roof/length formulas of Ji–Ma, pp. 8412–8413 and 8418–8419.

Fix \(\lambda=1/2\), and let \(x\) be distributed according to Lebesgue probability normalized on \(W_5\) (or, identically, any single branch of the four level-five types). The finitely many branch endpoints are null and may be omitted. Let \(J_t\) be the level index of \(F_{1/2}^t(x)\). Define

\[
\tau=\inf\{t\ge1:J_t=4\},\qquad
H=\max_{0\le t<\tau}(J_t-4),\qquad
R=\sum_{t=0}^{\tau-1}S_{J_t-1}.
\]

The quantity \(R\) counts original-map iterations **up to the induced stopping time**, not necessarily the first original-map visit to the level-four set during an unfinished inducing block. This distinction is essential. The stopping time is finite almost surely, so all three variables are well defined almost surely.

## Proof

**1. Exact high-level Markov chain.** From the image description and geometric lengths, conditional normalized Lebesgue measure on a branch of level \(j\ge5\) gives

\[
\mathbb P(J_{t+1}=j-1+k\mid J_t=j,\text{past branch itinerary})
=\frac{\varepsilon_{j-1+k}}{\sum_{i\ge j-1}\varepsilon_i}
=(1-\lambda)\lambda^k,\qquad k=0,1,\dots.
\]

Each restricted induced branch is affine, so conditional Lebesgue measure on a successive partition cylinder maps to normalized Lebesgue measure on the next branch. Consequently the stated transition law is valid jointly at all steps before landing on level four. Set \(X_t=J_t-4\); then \(X_0=1\), and while \(X_t\ge1\),

\[
X_{t+1}=X_t+G_t-1,\qquad \mathbb P(G_t=k)=2^{-(k+1)},\quad k\ge0,
\]

with independent increments. The chain cannot jump below zero before first hitting it.

**2. Exact first-passage probabilities.** The random walk is skip-free downward. If \(U(z)=\mathbb E[z^\tau]\), decomposing the first jump into \(G_0\) independent unit-descents gives, for \(0\le z<1\),

\[
U(z)=z\sum_{k\ge0}2^{-(k+1)}U(z)^k=\frac z{2-U(z)}.
\]

The solution with \(U(0)=0\) is \(U(z)=1-\sqrt{1-z}\). Its coefficients give the stated Catalan formula, with total mass \(U(1-)=1\). The tail generating function is

\[
\sum_{n\ge0}\mathbb P(\tau>n)z^n=\frac{1-U(z)}{1-z}=(1-z)^{-1/2}.
\]

Hence the central-binomial tail is exact; Stirling's formula yields \(\mathbb P(\tau>n)\sim(\pi n)^{-1/2}\).

**3. Exact height distribution.** For an integer \(h\ge2\), stop \(X_t\) on hitting zero or first reaching at least \(h\). Until then \(1\le X_t\le h-1\), and at every step there is probability at least \(2^{-(h-1)}\) of absorption within \(h-1\) consecutive downward steps. Thus the stopping time has finite expectation. Because \(\mathbb E(G_t-1)=0\) and the increments are integrable, the stopped walk has expectation \(1\). At the upper crossing, the geometric overshoot above \(h\) has conditional mean one by memorylessness, regardless of the pre-crossing level. At the lower crossing, the position is zero. Therefore

\[
1=\mathbb E[X_{\rm stop}]=(h+1)\,\mathbb P(H\ge h),
\]

proving the height identity. The event \(H\ge1\) is certain because \(X_0=1\).

**4. Converting inducing time to original-map time.** Fibonacci growth provides constants \(0<c<C<\infty\) satisfying \(c\varphi^j\le S_{j-1}\le C\varphi^j\) for every \(j\ge5\). Since every visited level is at most \(H+4\), and the top level is visited at least once,

\[
c\varphi^H\le R\le C\tau\varphi^H
\]

upon modifying the constants by a fixed factor \(\varphi^4\). For each \(\eta\in(0,1)\) and large \(T\), take integers \(h_+=\lceil(1+\eta)\log T/\log\varphi\rceil\), \(h_-=\lfloor(1-\eta)\log T/\log\varphi\rfloor\). The two roof bounds yield

\[
\frac1{h_++1}\le\mathbb P(R>T)
\le\frac1{h_-+1}+\mathbb P\!\left(\tau>c_\eta T^\eta\right)
=\frac1{h_-+1}+O_\eta(T^{-\eta/2}).
\]

Multiplying by \(\log T\), then letting \(T\to\infty\) and \(\eta\downarrow0\), proves the claimed constant \(\log\varphi\). Finally the tail integral for any positive moment diverges because \(\mathbb P(R>T)\sim(\log\varphi)/\log T\).

## Verification

The companion `checker.py` uses exact rational dynamic programming for the Catalan first-passage probabilities, exact rational finite-barrier linear systems for the height identity, and supporting numerical tests for Stirling and Fibonacci estimates. Run with `python3 checker.py` from the directory containing this document. The program passes 83 finite checks. These do not replace the infinite-level martingale argument or the analytical tail sandwich.

## Relationship to prior work

Ji and Ma [1] construct the exact bimodal map and its Markov inducing scheme, including the geometric branch lengths, Fibonacci return schedule, and qualitative recurrence/dissipativity transition at \(\lambda=1/2\). These inputs are credited. The assessed result adds the exact excursion-step and height distributions **and** the original-clock inverse-logarithmic tail with its sharp constant. The distinction between inducing steps and original-map iterations is not addressed by the quoted transition result.

Bruin and Todd [2,3] analyze thermodynamic and recurrence phenomena for related infinitely branched and Fibonacci **unimodal** systems. Their model families and primary statements do not give this bimodal, critical, original-clock excursion distribution. Ma [4] studies absolutely continuous invariant measures for a different smooth cubic Fibonacci-like family. Published and indexed mathematical statements may nevertheless contain an equivalent specialization or a stronger general theorem; this is the principal residual priority risk.

## Limitations

This theorem concerns one critical parameter and an induced excursion starting from normalized Lebesgue on a specified high-level branch. It is not a claim of a universal return-time law for all bimodal maps, of a mixing-rate asymptotic, or of an original-map *first-hit* distribution. The result is analytically proved conditional on the explicitly cited, independently inspected branch/roof construction of [1]. Finite checks are supportive only. Publication-priority originality has not been independently audited.

## References

[1] H. Ji and W. Ma, “Phase transition for piecewise linear fibonacci bimodal map,” *AIMS Mathematics* **8** (2023), 8403–8430, published 2023-02-03. DOI: 10.3934/math.2023424. https://www.aimspress.com/aimspress-data/math/2023/4/PDF/math-08-04-424.pdf

[2] H. Bruin and M. Todd, “Transience and thermodynamic formalism for infinitely branched interval maps,” arXiv:1104.5452, https://arxiv.org/pdf/1104.5452.

[3] H. Bruin and M. Todd, “Wild attractors and thermodynamic formalism,” arXiv:1202.1770, https://arxiv.org/pdf/1202.1770.

[4] W. Ma, “Invariant measure for cubic Fibonacci-like polynomials,” *JUSTC* **54** (2024), article 0802. DOI: 10.52396/JUSTC-2023-0036. https://justc.ustc.edu.cn/en/article/pdf/preview/10.52396/JUSTC-2023-0036.pdf.
