# Critical deletion noise for the longest empty arc of a uniform circular sample

## Finding

Let \(U_1,\ldots,U_n\) be independent uniform locations on a circle of circumference one, with \(n\ge2\). Independently delete each location with probability \(\varepsilon_n\). Write \(M_n\) for the largest original consecutive-point gap and \(\widetilde M_n\) for the largest consecutive-survivor gap. On the event that no location survives, set \(\widetilde M_n=1\); this convention is asymptotically irrelevant in the regimes below.

Assume \(\varepsilon_n\log n\to\tau\in[0,\infty)\). With \(X_n=nM_n-\log n\) and \(Y_n=n\widetilde M_n-\log n\), for every real \(x,y\),

\[
\Pr(X_n\le x,\ Y_n\le y)\longrightarrow
\exp\!\left[-e^{-\min(x,y)}-(e^\tau-1)e^{-y}\right].
\]

Equivalently, in the limit, the original extreme-gap process is Poisson with tail intensity \(e^{-x}\); new gaps created by deletion form an independent Poisson process with tail intensity \((e^\tau-1)e^{-x}\), and the thinned maximum is the maximum over both processes. Consequently,

\[
\Pr(\widetilde M_n=M_n)\longrightarrow e^{-\tau}.
\]

The perturbation threshold is \(\varepsilon_n\asymp1/\log n\). More precisely, if \(\varepsilon_n\to0\) and \(\varepsilon_n\log n\to\infty\), then \(\Pr(\widetilde M_n=M_n)\to0\).

There is also a finite-sample identity. Let \(C_{n,k}(t)\) be the number of retained gaps longer than \(t\in[0,1)\) that consist of exactly \(k\) consecutive original gaps. For \(1\le k<n\), with \(q_n=1-\varepsilon_n\),

\[
\mathbb E C_{n,k}(t)
=nq_n^2\varepsilon_n^{k-1}\Pr\{\operatorname{Beta}(k,n-k)>t\}.
\]

## Assumptions and scope

The original locations are iid uniform and continuous. Deletions are independent of one another and of all original locations; in particular they are not optimized or chosen in response to observed gaps. All maxima are arc lengths, not chord lengths. The joint limit concerns fixed real thresholds and the fixed \(n\) binomial sample model, not an independently resampled point cloud. The Poisson processes describe exceedance heights on the real line; each has infinitely many points far below any fixed threshold, but a finite number above every real threshold. The case \(\tau=0\) is included. The additional high-noise conclusion requires \(\varepsilon_n\to0\).

## Proof

**1. Exponential representation and finite mean.** Enumerate the original circle gaps cyclically. Their joint law is

\[
(G_1,\ldots,G_n)\stackrel d=
(E_1/S_n,\ldots,E_n/S_n),\qquad
S_n=\sum_{i=1}^n E_i,
\]

with independent \(E_i\sim\operatorname{Exp}(1)\), independent of the deletion marks. A consecutive sum of \(k\) coordinates has the \(\operatorname{Beta}(k,n-k)\) distribution for \(1\le k<n\). A specified run of \(k\) original gaps becomes exactly one retained gap when its two endpoint vertices are retained and all \(k-1\) intervening vertices are deleted, an event of probability \(q_n^2\varepsilon_n^{k-1}\). Summing over \(n\) possible cyclic starts gives the stated exact expectation. The exceptional case of one surviving point has probability \(nq_n\varepsilon_n^{n-1}\).

**2. Marked rare blocks on the exponential scale.** Let \(Z_{n,k}(u)\) count retained gaps consisting of exactly \(k\) consecutive exponential variables whose *unnormalized* sum exceeds \(u\). For fixed \(k<n\), independence of marks and increments yields

\[
\mathbb E Z_{n,k}(u)
=nq_n^2\varepsilon_n^{k-1}
 e^{-u}\sum_{j=0}^{k-1}\frac{u^j}{j!}.
\]

Put \(u=\log n+x\). For each fixed positive integer \(k\), and \(\varepsilon_n\log n\to\tau<\infty\),

\[
\mathbb E Z_{n,k}(\log n+x)
\longrightarrow
\frac{\tau^{k-1}}{(k-1)!}e^{-x}.
\]

Here \(\tau^0=1\), including at \(\tau=0\). To prove the joint Poisson convergence for any finite collection of block lengths and threshold intervals, expand mixed factorial moments of their marked exceedance counts. Two different complete retained blocks cannot share any original exponential gap: overlapping interiors would demand that a common vertex be simultaneously retained and deleted. For an ordered \(r\)-tuple of prescribed blocks whose gap sets and endpoint marks are separated, all constraints and exponential sums are independent. Their aggregate contribution tends to the product of the above intensities. Tuples with neighboring blocks share only a retained endpoint; for fixed block lengths there are \(O(n^{r-1})\) such tuples, and their joint exceedance probability is \(O(n^{-r})\), since their exponential sums use disjoint increments and the joint mark probability differs from the independent-block product by at most a bounded factor \(q_n^{-1}\). These exceptional tuples contribute \(o(1)\). Repeating the argument with disjoint threshold intervals proves convergence of the marked processes for every finite set of lengths to independent Poisson processes, the process for length \(k\) having tail intensity \(\tau^{k-1}e^{-x}/(k-1)!\).

**3. Uniform control of long deletion runs.** For \(q_n>0\), the geometric mixture identity is

\[
\sum_{k\ge1}q_n^2\varepsilon_n^{k-1}
\Pr\{\operatorname{Gamma}(k,1)>u\}
=q_ne^{-q_nu},\qquad u\ge0.
\]

It follows by inserting the Erlang tail and interchanging nonnegative sums. The finite-circle expected number of retained blocks with at least \(K+1\) exponential gaps and sum above \(u\) is bounded by the infinite-mixture expectation after removing the first \(K\) terms, apart from the single-survivor event. Therefore for \(u=\log n+x\), its limiting upper bound is

\[
e^{-x}\left(e^\tau-\sum_{j=0}^{K-1}\frac{\tau^j}{j!}\right),
\]

which tends to zero as \(K\to\infty\). Markov's inequality permits the passage from fixed-length Poisson processes to their full union. The retained-gap extremal process thus has tail intensity \(e^\tau e^{-x}\), with its length-one and length-at-least-two portions asymptotically independent and of respective tail intensities \(e^{-x}\) and \((e^\tau-1)e^{-x}\).

**4. Identification of the original extreme process.** The unnormalized original gaps are iid exponential, so their extreme point process has tail intensity \(e^{-x}\). A given original extreme gap survives as a length-one retained block exactly when both endpoints are retained. The expected number of original gaps exceeding \(\log n+x\) that fail this condition is

\[
n(1-q_n^2)e^{-(\log n+x)}=(1-q_n^2)e^{-x}\longrightarrow0.
\]

Thus the original extreme process and the retained length-one extreme process have the same asymptotic points above every finite threshold. The new length-at-least-two process is independent in the limit by the mixed factorial-moment calculation. The joint maximum formula follows: both maxima are below \(x\) and \(y\) exactly when the common extreme process has no point above \(\min(x,y)\) and the new process has no point above \(y\).

**5. Return to arc lengths and stability.** Chebyshev's inequality for the exponential sum shows \((n/S_n-1)\log n\to0\) in probability. The original and thinned unnormalized maxima are both \(\log n+O_{\Pr}(1)\), from their extreme-process limits. Hence multiplication by \(n/S_n\) changes both centered maxima by \(o_{\Pr}(1)\), proving the displayed joint limit for circular arc lengths.

With probability at least \(1-2\varepsilon_n\), both endpoints of the uniquely longest original gap survive. On that event it remains a retained gap, and the longest arc remains exactly unchanged if no newly merged gap exceeds it. The limiting common and new extreme processes are independent, with respective tail intensities \(e^{-x}\) and \((e^\tau-1)e^{-x}\), so the probability that their top point comes from the common process is

\[
\int_{-\infty}^\infty e^{-x}\exp(-e^\tau e^{-x})\,dx=e^{-\tau}.
\]

No ties occur with positive probability. This proves the exact-equality limit. Finally, if \(\varepsilon_n\to0\) but \(\varepsilon_n\log n\to\infty\), condition on the binomial number \(R_n\) of survivors. Given \(R_n=r\), their positions are iid uniform and the classical maximal-spacing theorem gives \(r\widetilde M_n-\log r=O_{\Pr}(1)\). Since \(R_n/n=q_n+O_{\Pr}(n^{-1/2})\),

\[
n\widetilde M_n-\log n
=\frac{\varepsilon_n}{q_n}\log n+O_{\Pr}(1)
\longrightarrow\infty,
\]

whereas \(nM_n-\log n=O_{\Pr}(1)\). The maximum therefore changes with probability tending to one.

## Verification

The accompanying `checker.py` uses only the Python 3 standard library. It exhaustively enumerates retention masks for \(3\le n\le9\) at three rational deletion probabilities, checking the exact finite block-count identities and the exceptional single-survivor contribution (156 exact assertions including rational Laplace-mixture checks). It also reports three illustrative, deterministic-seed Monte Carlo quantities at \(n=5000\), \(\tau=0.7\); their finite-size discrepancies are not used as proofs. Run `python3 checker.py` in the directory containing this file and the checker.

## Relationship to prior work

Schlemm (2014, arXiv:1405.6114) proves the one-sample Gumbel limit for the longest uniform circular gap and provides finite moments. Mijatović and Vysotsky (2015, arXiv:1508.00944) prove fixed-order \(k\)-spacing Gumbel limits using exponential representations and stationary-sequence extremes. Neither statement gives a jointly coupled thinned/original maximum or a deletion-noise threshold. Nehring (2014, arXiv:1407.1700) examines the splitting characterization of Poisson point processes, a different structural fact that does not specify extreme-gap overlap in fixed-cardinality samples. The present calculation combines a deletion-run mark with simultaneous extremes and a summable geometric-gamma mixture. It does not assert novelty of the classical one-sample Gumbel law, exponential representation, or Poisson thinning.

## Limitations

The result does not treat adversarially deleted points, nonuniform location densities, a fixed nonvanishing deletion fraction in the joint-window normalization, or higher-dimensional empty regions. The convergence in the theorem is weak convergence of the two maximum statistics; no quantitative total-variation rate is claimed. Historical priority for a potentially more general extreme-process coupling theorem remains unverified by independent review.

## References

1. E. Schlemm, *Limiting distribution of the maximal distance between random points on a circle: A moments approach*, arXiv:1405.6114, first submitted 23 May 2014. https://arxiv.org/abs/1405.6114
2. A. Mijatović and V. Vysotsky, *On the weak limit law of the maximal uniform k-spacing*, arXiv:1508.00944, first submitted 5 August 2015. https://arxiv.org/abs/1508.00944
3. B. Nehring, *A Characterization of the Poisson Process revisited*, arXiv:1407.1700, first submitted 7 July 2014. https://arxiv.org/abs/1407.1700
