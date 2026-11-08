# A persistent crossing-covariance footprint of rare non-simple isolated chords

## Finding

Let \(\mathcal D_n\) be uniformly distributed over all perfect matchings of \(2n\) labeled points in cyclic order, for integer \(n\ge2\). Let \(C_n\) denote the number of unordered crossing pairs of chords, \(I_n\) the number of chords with **no** crossings (isolated vertices of the intersection graph), and \(S_n\) the number of simple chords joining consecutive cyclic endpoints. For nonnegative integers \(a,b\), write \((2a-1)!!=1\cdot3\cdots(2a-1)\), with \((-1)!!=1\), and put

\[
q_{n,a}=\frac{(2a-1)!!\,(2n-2a-3)!!}{(2n-1)!!},\qquad 0\le a\le n-1.
\]

Then the following exact, strictly negative mixed covariance holds for every \(n\ge2\):

\[
\boxed{\operatorname{Cov}(C_n,I_n)=-\frac n3\sum_{a=0}^{n-1}q_{n,a}\bigl(n-1+a(n-1-a)\bigr)<0.}
\]

Its finite-size asymptotic expansion has three explicit terms:

\[
\boxed{\operatorname{Cov}(C_n,I_n)=-\frac n3-\frac16-\frac{5}{6n}+O(n^{-2}).}
\]

The distinction from **simple** chords survives in the unscaled covariance. For \(R_n=I_n-S_n\), the number of isolated chords whose endpoints are *not* consecutive, the exact formula restricts to \(1\le a\le n-2\), and, for \(n\ge3\),

\[
\boxed{\operatorname{Cov}(C_n,R_n)=-\frac13-\frac{11}{12n}+O(n^{-2})\qquad(n\to\infty).}
\]

For every finite \(n\ge3\), the exact covariance with \(R_n\) is strictly negative. In particular, although \(R_n\to0\) in \(L^2\), its covariance with total crossings tends to the **nonzero** value \(-1/3\). This is the main rare-event effect: discarding non-simple isolated chords leaves first-order asymptotics unchanged, but changes the constant term of a global covariance.

Furthermore \(\operatorname{Var}(I_n)\to1\), and consequently the correlation has the sharp decay law

\[
\boxed{\lim_{n\to\infty}\sqrt n\,\operatorname{Corr}(C_n,I_n)=-\sqrt5.}
\]

The theorem concerns one mixed dependence problem: the full isolated-chord/crossing covariance and its explicit rare-non-simple contribution. The leading simple-chord/crossing covariance and its Gaussian–Poisson limit were previously established and are not claimed as new.

## Assumptions and scope

Each of the \((2n-1)!!\) pairings is equally likely. A crossing occurs when distinct chords with endpoints \(i<j\) and \(k<\ell\) alternate cyclically. An isolated chord has degree zero in the intersection graph, whether or not its endpoints are consecutive. A *simple chord* means a chord joining two consecutive cyclic endpoints, and \(S_n\) counts such chords. All limits are taken along integer \(n\to\infty\); no conditioning on crossing count, growing geometric model, or joint distributional limit is asserted.

## Proof

**1. The isolation decomposition.** Fix a potential chord \(c\). If its endpoints cut the other endpoints into arcs containing \(2a\) and \(2b\) points, then \(a+b=n-1\). The event \(E_c\) that \(c\) occurs and has no crossing means that the \(2a\) endpoints on one side match among themselves, and independently the \(2b\) on the other side match among themselves. Hence

\[
\Pr(E_c)=\frac{(2a-1)!!(2b-1)!!}{(2n-1)!!}=q_{n,a}.
\]

Conditioned on \(E_c\), each arc carries a *uniform* independent matching. The entire crossing count is therefore distributed as the sum of independent crossing counts on \(a\) and \(b\) chords. In particular, using the established or directly double-countable expectation \(\mathbb E[C_m]=m(m-1)/6\),

\[
\mathbb E[C_n\mid E_c]-\mathbb E[C_n]
=\frac{a(a-1)+b(b-1)-n(n-1)}6
=-\frac{ab+n-1}{3}.
\]

Writing \(I_n=\sum_c\mathbf1_{E_c}\) over all potential chords gives

\[
\operatorname{Cov}(C_n,I_n)
=\sum_c\Pr(E_c)\bigl(\mathbb E[C_n\mid E_c]-\mathbb E[C_n]\bigr).
\]

For each \(a\in\{0,\ldots,n-1\}\), there are \(2n\) clockwise oriented arcs between two potential endpoints having exactly \(2a\) intervening endpoints. Every unoriented potential chord appears exactly twice as \(a\) runs over this range. Thus the sum over chords equals \(n\) times the sum over \(a\), proving the boxed exact formula. Every summand is strictly positive before the leading minus sign for \(n\ge2\), proving strict negativity without a large-\(n\) assumption.

**2. Sharp expansion.** The weights are symmetric in \(a\) and \(n-1-a\) and obey

\[
\frac{q_{n,a+1}}{q_{n,a}}=\frac{2a+1}{2n-2a-3}.
\]

On the first quarter of the range this ratio is bounded by \(1/2\) for all sufficiently large \(n\); by symmetry and unimodality, the central range is exponentially smaller than the initial tail. In particular, for any fixed \(r\), the weighted remainder over \(r\le a\le n-1-r\) is bounded by a constant times \(n q_{n,r}\), where \(q_{n,r}=O(n^{-r-1})\). After the factor \(n/3\) in the covariance, the terms with \(a\ge3\) and \(n-1-a\ge3\) contribute \(O(n^{-2})\).

For sufficiently large \(n\), the contributions from the two ends \(a=0,n-1\), then \(a=1,n-2\), then \(a=2,n-3\), are respectively

\[
-\frac{2n(n-1)}{3(2n-1)},\qquad
-\frac{2n}{3(2n-1)},\qquad
-\frac{2n(3n-7)}{(2n-1)(2n-3)(2n-5)}.
\]

The sum of the first two equals \(-2n^2/[3(2n-1)]\), with expansion \(-n/3-1/6-1/(12n)+O(n^{-2})\); the third equals \(-3/(4n)+O(n^{-2})\). Their sum proves \(-n/3-1/6-5/(6n)+O(n^{-2})\). Omitting the simple-chord terms \(a=0,n-1\), the same calculation gives \(\operatorname{Cov}(C_n,R_n)=-1/3-11/(12n)+O(n^{-2})\); the exact remaining sum is strictly negative for \(n\ge3\).

**3. Variance of isolated-chord count.** Every simple chord is isolated. Let \(R_n=I_n-S_n\). From the same isolation count,

\[
\mathbb E[R_n]=n\sum_{a=1}^{n-2}q_{n,a}=O(n^{-1}),
\]

where the tail estimate above applies. For a uniform diagram of \(m\) chords, \(\mathbb E[I_m]\le2\) for all \(m\ge1\): for \(m\ge2\) put \(M=m-1\), use

\[
\frac{q_{m,a}}{q_{m,0}}=\frac{\binom M a}{\binom{2M}{2a}}
\le \binom M a^{-1},
\]

and sum, noting \(\sum_{a=0}^{M}\binom M a^{-1}\le3\) and \(3m/(2m-1)\le2\). The case \(m=1\) is immediate. Given an isolated chord, its two independently matched arcs contain an expected total of at most four other isolated chords. Summing over all potential non-simple isolated chords therefore yields

\[
\mathbb E[R_n I_n]\le5\mathbb E[R_n]=O(n^{-1}),
\qquad \mathbb E[R_n^2]\le\mathbb E[R_n I_n]=O(n^{-1}).
\]

Thus \(R_n\to0\) in \(L^2\). Counting the \(2n\) cyclically adjacent pairs gives

\[
\mathbb E[S_n]=\frac{2n}{2n-1},\quad
\mathbb E[(S_n)_2]=\frac{2n}{2n-1},\quad
\operatorname{Var}(S_n)=\frac{4n(n-1)}{(2n-1)^2}\to1.
\]

The second factorial moment uses exactly \(n(2n-3)\) unordered pairs of disjoint adjacent endpoint pairs, each both present with probability \(1/[(2n-1)(2n-3)]\). Cauchy–Schwarz and \(R_n\to0\) in \(L^2\) show \(\operatorname{Var}(I_n)\to1\).

**4. Correlation.** The classical exact crossing variance is

\[
\operatorname{Var}(C_n)=\frac{n(n-1)(n+3)}{45}
\]

(Flajolet–Noy, Theorem 3(i), also checked independently for small \(n\)). Combining it with the established covariance and isolated-count variance gives

\[
\sqrt n\,\frac{\operatorname{Cov}(C_n,I_n)}{\sqrt{\operatorname{Var}(C_n)\operatorname{Var}(I_n)}}
\longrightarrow -\frac{\sqrt{45}}{3}=-\sqrt5.
\]

## Verification

The standalone standard-library script `verify.py` enumerates all pairings with \(2n\) endpoints for \(2\le n\le7\), compares exact rational covariances, verifies the established crossing variance and the isolated-chord expectation, and checks conditional crossing distributions for every possible arc split with \(2\le n\le5\). It also checks the exact ratio of isolation weights and the rational asymptotic diagnostics. The script produced **1,304 passing assertions**. Exhaustive finite checks support the identities but are not used in place of the infinite proofs above.

Run with `python3 verify.py` from the directory containing these two files.

## Relationship to prior work

Flajolet and Noy's March 2000 report proves the marginal component-count limit and exact crossing moments (sections 1–2). Acan's January 2015 work studies the degree distribution of a marked chord and monolithic diagrams (sections 2–3). Paguyo's 2021 preprint, subsequently revised, obtains separate quantitative marginal limit theorems for crossings and *simple* chords (Theorems 1.1–1.2). None of the inspected relevant statements supplies the exact mixed covariance with **all** isolated chords, the three-term expansion or the sharp correlation constant. An earlier finite joint enumerator of **simple** chords and crossings also gives their covariance \(-2n(n-1)/[3(2n-1)]\) and a Gaussian–Poisson asymptotic independence limit; those are not part of the new claim. The present all-isolated-chord result is not obtained by replacing a name: non-simple isolated chords have vanishing count in \(L^2\) but retain covariance \(-1/3\) with crossings. The conditional splitting identity proves this persistence, which does not follow from the earlier simple-chord enumerator.

## Limitations

This mathematical derivation has not undergone independent audit. A stronger or implicit joint generating-function treatment in older chord-diagram literature may already cover the formula; literature searches cannot establish priority conclusively. A joint normal–Poisson independence theorem is not proved or claimed. The \(O(n^{-2})\) bound concerns covariance alone, not rates for the correlation limit or joint distributional convergence. Computations were exact over finite ranges only.

## References

1. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report RR-3914, March 2000, https://algo.inria.fr/flajolet/Publications/FlNo00.pdf . Sections 1–2; Theorem 3 for crossing moments.
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, first posted January 7, 2015, https://arxiv.org/abs/1501.01489 . Sections 2–3 on marked-chord degree and monoliths.
3. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, initially posted April 2, 2021; subsequent revision in 2023, https://arxiv.org/abs/2104.01134 . Theorems 1.1–1.2 on separate crossing and simple-chord marginal limits.
