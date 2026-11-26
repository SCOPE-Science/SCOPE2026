# Frequent-factor counts of sparse binary words: exact extrema and an atomic-continuous limit law

## Finding

For a finite word \(w\), let \(\operatorname{occ}_w(u)\) count starting positions of \(u\) in \(w\), including overlaps. Let \(\Phi(w)\) count the distinct nonempty contiguous factors \(u\) with \(\operatorname{occ}_w(u)>|u|\). For a binary word with exactly two ones, write \(w=0^{g_1}1\,0^{g_2}1\,0^{g_3}\) and \(N=g_1+g_2+g_3=|w|-2\). Then, with \(z_+=\max(z,0)\),
\[
 \Phi(w)=1+\sum_{j=1}^N\mathbf 1_{\{\sum_{i=1}^3(g_i-j+1)_+>j\}}.
\]
The sum is over the three indexed gaps, even if two or more have equal length. For every \(N\ge0\), the exact extrema over these words are
\[
 \min\Phi=1+\left\lfloor\frac{N+2}{4}\right\rfloor,\qquad
 \max\Phi=1+\left\lfloor\frac N2\right\rfloor.
\]
Balanced gaps attain the minimum, and putting all zeros in one gap attains the maximum.

Let \(W_n\) be uniform on binary words of length \(n\) with exactly two ones. Then \(\Phi(W_n)/n\) converges in law to a random variable \(Y\) supported on \([1/4,1/2]\), with distribution function
\[
 F_Y(t)=\begin{cases}
 0&t<1/4,\\
 33t^2-12t+1&1/4\le t\le 1/3,\\
 -12t^2+12t-2&1/3<t\le 1/2,\\
 1&t>1/2.
 \end{cases}
\]
In particular there is one atom, of mass \(1/16\) at \(1/4\). The absolutely continuous density is \(66t-12\) on \((1/4,1/3)\), \(12-24t\) on \((1/3,1/2)\), and zero elsewhere. The first two moments and variance of \(\Phi(W_n)/n\) converge respectively to
\[
 \mathbb E Y=\frac{187}{576},\qquad \mathbb E Y^2=\frac{1499}{13824},\qquad \operatorname{Var}(Y)=\frac{1007}{331776}.
\]

## Assumptions and scope

Factors are linear, not cyclic, and counted by spelling, not by position. The frequency threshold is strict. The finite formulas include \(n=2\), and the limit is through integer lengths with the two one-positions uniformly chosen without replacement.

## Proof

**1. Complete factor classification.** An occurrence of a factor with at least one one must align its first one with one of the two marked positions. Thus there are at most two occurrences, which cannot exceed the length unless the factor is the single letter \(1\), which always qualifies. Any remaining factor is \(0^j\), with precisely \(\sum_{i=1}^3(g_i-j+1)_+\) occurrences. This quantity is nonincreasing in \(j\), so the qualifying powers form an initial segment and the displayed formula follows.

**2. Exact extrema.** The zero-factor occurrence count is at least \(N-3(j-1)\); every positive integer \(j\) with \(4j<N+3\) therefore qualifies. For gaps differing by at most one, write \(N=3q+r\) with \(0\le r\le2\). The count is exactly \(N-3(j-1)\) through \(j=q+1\), and zero beyond. The largest positive integer with \(4j<N+3\), taking zero if there is none, is \(\lfloor(N+2)/4\rfloor\), which is at most \(q+1\). At the other extreme the count is at most \((N-j+1)_+\): if some gaps contribute, their total length is at most \(N\) and at least one subtraction of \(j-1\) is made. For \((N,0,0)\) this bound is attained for all \(j\); the strict threshold is then equivalent to \(j\le\lfloor N/2\rfloor\). Including \(1\) gives both extrema.

**3. Limiting root.** For \(N>0\) let \(x_i=g_i/N\). On the unit simplex, define \(T(x)\) by \(\sum_i(x_i-T(x))_+=T(x)\). The left side minus the right is continuous, decreases at least at unit rate, and has a unique positive root. Perturbing \(x\) changes the function by at most the \(\ell_1\) perturbation, proving continuity of \(T\). The discrete sign test for \(0^j\) uses \(x_i-j/N+1/N\) in place of \(x_i-j/N\) in the positive part. This increases the left side by at most \(3/N\), so the corresponding root increases by at most \(3/N\); the grid cutoff under the strict inequality is within \(1/N\) of that root (the discrete root is at most 1). Counting \(1\) adds \(1/N\), giving \(|\Phi(w)/N-T(x)|\le5/N\). Replacing \(N\) by \(n=N+2\) preserves the uniform approximation as \(N\to\infty\). The uniform grid of gap compositions converges by Riemann sums to normalized area on the simplex, so \(Y=T(X)\) for a uniform simplex point \(X\).

**4. Distribution.** The sum of the positive parts is the maximum of the subset sums of the signed terms. Consequently, for \(t\ge0\), \(T(x)\le t\) holds precisely when each subset \(A\) satisfies \(\sum_{i\in A}x_i\le (|A|+1)t\). For the whole triple this requires \(t\ge1/4\), for pairs it requires \(x_i\ge1-3t\) for all \(i\), and for singletons it requires \(x_i\le2t\) for all \(i\). On \([1/4,1/3]\), translate each coordinate by \(-(1-3t)\). The remaining simplex has total \(9t-2\), and the forbidden corner above \(2t\) in any original coordinate leaves a simplex of total \(4t-1\) after translation. Two forbidden corners cannot overlap, since the remaining total would be \(-t\). Area scales quadratically, giving \((9t-2)^2-3(4t-1)^2=33t^2-12t+1\). For \(1/3\le t\le 1/2\) only the upper bounds matter; the three disjoint caps have relative area \((1-2t)^2\) each. For \(t\ge1/2\) all constraints hold. This gives the stated distribution, including its endpoint jump.

**5. Moments.** Integration against the atom and the two density pieces gives total mass one and the displayed rational moments. The normalized finite counts are bounded by 1, so weak convergence gives convergence of both moments and hence of variance.

## Verification

The accompanying standard-library `verify.py` enumerates literal factor multiplicities for all 1140 gap triples with \(0\le N\le17\), comparing the exact indexed-gap formula and both extrema. It checks the normalized cutoff against the root model at several larger sizes and integrates the density with exact rational arithmetic. `output.txt` records the original checker output. The analytic proof, not these finite checks, proves the unbounded statements.

## Relationship to prior work and limitations

Bals, Charalampopoulos, Lachish, Pissis, and Verbeek, *Text Indexing: From Reporting to Counting* (ESA 2026, Article 68, [DOI](https://doi.org/10.4230/LIPIcs.ESA.2026.68), arXiv:2607.24043), study the general frequency-versus-length statistic and its unrestricted extremal bound. *Fixed-binary asymptotic sharpness of the frequent-factor bound* (record 18eac5e211b6) addresses a dense worst-case regime. *Minimal absent factors of two-marker binary words: exact counts and a limit law* (record e744971e8c41) counts a different, absence-based invariant of the same sparse family. The scope here is fixed weight two; neither other weight regimes nor a full finite-length probability mass function are claimed. Unindexed equivalent prior work remains possible.
