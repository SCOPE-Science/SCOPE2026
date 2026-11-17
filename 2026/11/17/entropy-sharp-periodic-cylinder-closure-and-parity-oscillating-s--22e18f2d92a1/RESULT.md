# Entropy-sharp periodic-cylinder closure and parity-oscillating short-period counts

## Finding

A uniform admissible word in a finite irreducible positive-entropy vertex shift typically needs a periodic orbit of period close to the word length. The excess of the word length over its shortest periodic realization has a two-sided exponential tail with rate **exactly** the shift entropy. This produces a sharp change in exponential moments at the entropy, even when the adjacency graph is irreducible but nonmixing. The *number* of strictly shorter periods has an exact finite matrix formula and can exhibit genuine parity oscillation when the graph has period two.

Let \(B\) be a finite irreducible \(0\)-\(1\) matrix, let \(\lambda=\rho(B)>1\), and let \(d\) be its graph period. Write \(\mathcal W_n\) for its allowed vertex words of length \(n\), and draw \(W_n\) uniformly from \(\mathcal W_n\). For an allowed word \(w\), define \(\eta_n(w)\) as the least period of any one-sided **periodic** sequence beginning with \(w\). Put \(Z_n=(n-\eta_n(W_n))_+\). Then there exist positive constants \(c,C,L\), depending only on \(B\), such that for every sufficiently large integer \(n\) and every integer \(1\le k\le n-L\),

\[
c\lambda^{-k}\leq\Pr(Z_n\ge k)\leq C\lambda^{-k}.
\]

With \(h=\log\lambda\), for each fixed \(t\ge0\),

\[
\mathbb E[e^{tZ_n}]=
\begin{cases}
\Theta(1),&0\le t<h,\\
\Theta(n),&t=h,\\
\Theta(e^{(t-h)n}),&t>h.
\end{cases}
\]

The constants implicit in these bounds can depend on \(B\) and \(t\). In particular, \(\mathbb E\eta_n=n+O(1)\) and \(\mathrm{Var}(\eta_n)=O(1)\).

For each word define \(R_n(w)\) as the number of integers \(p\) with \(1\le p<n\) for which a periodic sequence of period dividing \(p\) begins with \(w\). Then the following **exact** identity holds for all \(n\ge2\):

\[
\mathbb E R_n=\frac{\sum_{p=1}^{n-1}\operatorname{tr}(B^p)}{\mathbf 1^{\mathsf T}B^{n-1}\mathbf 1}.
\]

Put \(c_r=\lim_{m\to\infty}\lambda^{-(dm+r)}\mathbf1^{\mathsf T}B^{dm+r}\mathbf1\), where \(0\le r<d\). Each constant exists and is strictly positive. For each residue \(r\),

\[
\lim_{m\to\infty}\mathbb E R_{dm+r+1}
=\frac{d\lambda^{-r}}{c_r(1-\lambda^{-d})}.
\]

Two concrete consequences are useful. The three-symbol, no-consecutive-equal-letters shift has \(B=J_3-I_3\), \(\lambda=2\), and

\[
\mathbb E R_n=\frac{2^n-3+(-1)^{n-1}}{3\,2^{n-1}}\longrightarrow\frac23.
\]

For its deficit, the tail has the explicit bounds, for \(1\le k\le n-2\),

\[
\frac{2^{n-k}+2(-1)^{n-k}}{3\,2^{n-1}}
\le\Pr(Z_n\ge k)\le
\frac{2^{n-k+1}-3+(-1)^{n-k}}{3\,2^{n-1}}.
\]

For the complete bipartite shift whose two vertex classes have sizes two and three, the spectral radius is \(\sqrt6\) and the graph period is two. There,

\[
\lim_{m\to\infty}\mathbb E R_{2m+1}=\frac{12}{25},
\qquad
\lim_{m\to\infty}\mathbb E R_{2m}=\frac15.
\]

## Assumptions and scope

A vertex word \(w_0\cdots w_{n-1}\) is admissible iff \(B_{w_i,w_{i+1}}=1\) for \(0\le i<n-1\). The one-sided symbolic shift consists of all infinite paths in this graph. Graph irreducibility means any vertex can reach any other by a directed path; no aperiodicity or primitivity is assumed. Positive entropy \(\lambda>1\) excludes directed permutation cycles. Each strictly shorter *closing period* \(p\) is a positive integer for which an infinite \(p\)-periodic admissible path begins with \(w\), whether or not its least period equals \(p\). Consequently \(R_n\) counts qualifying integers, not distinct periodic orbits. The statistical distribution is uniform over finite allowed words, not necessarily the stationary Markov distribution at finite \(n\).

## Proof

**Step 1: periodic closure and word counts.** Irreducibility gives a uniform finite upper bound on the length of a directed positive-length path from any terminal vertex to any initial vertex. Joining that path to a length-\(n\) word produces a periodic admissible path of period at most \(n+K\), for a graph-dependent integer \(K\). In particular, \(\eta_n\) is finite and \(\eta_n-n\) is bounded above. If \(p<n\), a word beginning a \(p\)-periodic admissible path is uniquely determined by the first \(p\) symbols of that path. Conversely, every path fixed by the \(p\)-th shift iterate has an admissible length-\(n\) prefix, and distinct such infinite paths have distinct length-\(n\) prefixes because \(p<n\). Hence the exact count of length-\(n\) words admitting the closing period \(p\) is \(\operatorname{tr}(B^p)\). Summation proves the identity for \(\mathbb E R_n\).

**Step 2: two-sided tails.** Set \(A_n=\lvert\mathcal W_n\rvert=\mathbf1^{\mathsf T}B^{n-1}\mathbf1\). Perron–Frobenius theory for an irreducible (possibly imprimitive) matrix yields graph-dependent constants \(a,A>0\) for which \(a\lambda^n\le A_n\le A\lambda^n\) for all \(n\ge1\), after harmless changes to the constants. Its periodic point counts satisfy \(\operatorname{tr}(B^p)\le A'\lambda^p\) for every \(p\ge1\). Every realization of \(Z_n\ge k\) admits some closing period \(p\le n-k\). A union bound therefore gives

\[
\Pr(Z_n\ge k)\le\frac1{A_n}\sum_{p=1}^{n-k}\operatorname{tr}(B^p)\le C\lambda^{-k}.
\]

The peripheral spectrum is the simple \(d\)-cycle of eigenvalues \(\lambda e^{2\pi i j/d}\), hence \(\operatorname{tr}(B^{dm})=d\lambda^{dm}+O(\theta^{dm})\) for some \(\theta<\lambda\). For \(n-k\) sufficiently large, choose \(p=d\lfloor(n-k)/d\rfloor\). This is an admissible periodic length, with \(n-k-d<p\le n-k\), and \(\operatorname{tr}(B^p)\ge a'\lambda^p\). Its distinct length-\(n\) prefixes alone show \(\Pr(Z_n\ge k)\ge c\lambda^{-k}\), uniformly on \(1\le k\le n-L\).

**Step 3: the sharp exponential moment threshold.** For every nonnegative integer random variable bounded by \(n-1\),

\[
\mathbb E[e^{tZ_n}]=1+(e^t-1)\sum_{k=1}^{n-1}e^{t(k-1)}\Pr(Z_n\ge k).
\]

The upper tail bound reduces the sum to a geometric sum of \(e^{(t-h)k}\). The lower bound applies to every \(k\le n-L\), and establishes matching orders, including a linear number of comparable terms at \(t=h\). At \(t=0\) the moment equals one exactly. Also \(\eta_n=n-Z_n\) whenever \(Z_n>0\), while on \(Z_n=0\) the graph-dependent closing overhead is bounded. The exponential tail of \(Z_n\) gives bounded moments of every fixed order for \(\eta_n-n\), including the asserted expectation and variance bounds.

**Step 4: lattice limits for the number of closing periods.** For \(0\le r<d\), the cyclic Perron–Frobenius decomposition gives \(A_{dm+r+1}\sim c_r\lambda^{dm+r}\), with \(c_r>0\). Only multiples of \(d\) support closed graph walks. Moreover \(\operatorname{tr}(B^{dj})\sim d\lambda^{dj}\). Summing the resulting geometric sequence through \(p=d m\), then dividing by \(A_{dm+r+1}\), gives

\[
\lim_{m\to\infty}\mathbb E R_{dm+r+1}=
\frac{d\lambda^{-r}}{c_r(1-\lambda^{-d})}.
\]

**Step 5: exact model calculations.** For \(B=J_3-I_3\), the eigenvalues are \(2,-1,-1\); therefore \(A_n=3\,2^{n-1}\) and \(\operatorname{tr}(B^p)=2^p+2(-1)^p\). Summing traces gives the stated exact mean. To bound the deficit tail, retain only period \(p=n-k\) for the lower bound and sum all traces \(1\le p\le n-k\) for the upper bound.

For the complete \(K_{2,3}\) bipartite adjacency, the nonzero eigenvalues are \(\sqrt6\) and \(-\sqrt6\). Thus \(\operatorname{tr}(B^{2j})=2\cdot6^j\) and odd traces vanish. Allowed word counts are \(A_{2m+1}=5\cdot6^m\) and \(A_{2m}=2\cdot6^m\). Inserting these into the exact mean identity yields limits \(12/25\) and \(1/5\), respectively.

## Verification

The standalone Python 3 checker in `checks/verify.py` enumerates all admissible words and their shortest strictly shorter closing periods for the three-color, golden-mean, and bipartite matrices. It checks each finite tail against the sum of periodic point traces and the particular trace contribution, confirms the three-color spectral counts, and prints representative subcritical, critical, and supercritical exponential moments. It is finite verification of identities and sample cases, not the infinite asymptotic proof; Steps 1–5 above provide the latter.

## Relationship to prior work

Krishnaswami and Rameshan (first public version June 24, 2026) propose a three-symbol no-repeat finite-type model of chaotic coincidence *codes* for a three-rotor flow and compute its word complexity. Their Section 6 leaves broader word statistics and the identification of physical periodic words as distinct questions. Our conclusion is explicitly **only** about the abstract finite-type shift; it does **not** identify its periodic symbolic sequences with physical three-rotor periodic trajectories.

Holub and Shallit examine longest borders and least periods for unrestricted words over a uniform alphabet, including their bounded mean offset. Their full-alphabet model does not provide the graph-dependent, possibly imprimitive periodic-cycle counts and their parity limits established here, nor the entropy-critical moment classification in this statement. Allen, Baker, and Bárány address almost-sure dynamical recurrence to cylinders under Gibbs measures, with distinct observables and quantifiers. The arguments here use periodic closed paths and uniform finite admissible words, not recurrence times of an evolving random infinite path. Standard Perron–Frobenius spectral theory underlies the proof and is not claimed as new.

## Limitations

The comparison with the literature is not an independence or priority certificate. Unindexed work on Markov-constrained word borders and periodic specification may already entail parts of the theorem. Constants in the general two-sided bounds are not evaluated optimally, and no limiting law for the full deficit distribution is asserted. The graph must be finite, irreducible, and have positive entropy. The special three-rotor adjacency graph was motivated by a conjectural symbolic approximation of chaotic trajectories; no inference about real physical periodic orbits is drawn. Self-review is not independent verification.

## References

1. G. S. Krishnaswami and A. Rameshan, *Symbol sequences from three-rotor coincidences and their word-complexity*, arXiv:2606.25766v1 (first posted June 24, 2026), especially Section 6, https://arxiv.org/abs/2606.25766.
2. Š. Holub and J. Shallit, *Periods and Borders of Random Words*, STACS 2016, LIPIcs 47, article 44, DOI:10.4230/LIPIcs.STACS.2016.44, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2016.44.
3. D. Allen, S. Baker, and B. Bárány, *Recurrence rates for shifts of finite type*, arXiv:2209.01919v1 (2022), https://arxiv.org/abs/2209.01919.
