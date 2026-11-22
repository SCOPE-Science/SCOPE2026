# Mixed Poisson first cyclic labels and a critical moment spectrum in uniform random mappings

## Finding

Let \(f_n:[n]\to[n]\) be uniform among all \(n^n\) maps, let \(\mathcal C_n\) denote the vertices lying on directed cycles of its functional digraph, and let \(M_n=\min\mathcal C_n\). The rescaled point process of cyclic labels
\[
\Xi_n=\sum_{v\in\mathcal C_n}\delta_{v/\sqrt n}
\]
converges vaguely in distribution on \([0,\infty)\) to a Cox process that, given a Rayleigh random variable \(R\) with density \(r\exp(-r^2/2)\) for \(r>0\), is a homogeneous Poisson process of rate \(R\). In particular, for every \(t\ge0\),
\[
\lim_{n\to\infty}\Pr\{M_n>t\sqrt n\}
= S(t):=\int_0^\infty r\exp(-r^2/2-tr)\,dr
=1-t\exp(t^2/2)\int_t^\infty \exp(-u^2/2)\,du.
\]
The limiting survival probability satisfies \(S(t)\sim t^{-2}\) as \(t\to\infty\). The weak limit has a critical second-moment divergence and rare-event-dominated higher moments:
\[
\lim_{n\to\infty}\frac{\mathbb E M_n}{\sqrt n}=\sqrt{\frac\pi2},\qquad
\operatorname{Var}(M_n)=n\log n+O(n),
\]
where the variance estimate has leading coefficient exactly one, and for every fixed integer \(s\ge3\),
\[
\lim_{n\to\infty}\frac{\mathbb E[M_n^s]}{n^{s-1}}
=\frac{s}{(s-1)(s-2)}.
\]
These are claims about a *fixed, naturally labeled* uniform random mapping, not independent random selection of vertices.

## Assumptions and scope

For every integer \(n\ge1\), each vertex \(i\in[n]=\{1,\dots,n\}\) independently chooses a uniformly random image \(f_n(i)\in[n]\). A vertex is cyclic precisely when some positive iterate returns to it. Let \(K_n=|\mathcal C_n|\ge1\). The order in \(M_n\) refers to fixed numerical labels, not distance along an orbit. Convergence of \(\Xi_n\) means convergence of its counting measures on each bounded label interval in the vague topology. The limits for \(s\) hold separately for each fixed integer \(s\ge3\); they are not uniform in the order of the moment.

## Proof

**1. Exact cyclic-core distribution and conditional label law.** The number of maps with cyclic set exactly a specified \(k\)-set \(A\) is \(k!\,k n^{n-k-1}\) for \(k<n\): choose a permutation on \(A\) and a rooted forest directed from the other vertices into \(A\). The same formula gives \(n!\) when \(k=n\), since \(k n^{n-k-1}=1\) in that case. Summing over \(\binom nk\) sets and dividing by \(n^n\) gives
\[
\Pr\{K_n=k\}=p_{n,k}
=\frac{k}{n}\,Q_{n,k},\qquad
Q_{n,k}:=\prod_{j=0}^{k-1}\left(1-\frac jn\right),\quad 1\le k\le n.
\]
By label exchangeability, conditional on \(K_n=k\), the cyclic set is a uniform \(k\)-subset of \([n]\). Thus for integers \(0\le m\le n\),
\[
\Pr\{M_n>m\mid K_n=k\}
=\frac{\binom{n-m}{k}}{\binom nk},
\]
with the convention that the numerator is zero when \(k>n-m\). The corresponding conditional mass is \(\Pr\{M_n=m\mid K_n=k\}=\binom{n-m}{k-1}/\binom nk\) for \(1\le m\le n-k+1\).

**2. Rayleigh core and Cox process.** For \(k\) of order \(\sqrt n\),
\[
\log Q_{n,k}=-\frac{k(k-1)}{2n}+O(k^3/n^2),
\]
while \(Q_{n,k}\le\exp[-k(k-1)/(2n)]\) for all \(k\). Consequently \(K_n/\sqrt n\Rightarrow R\), with Rayleigh density \(r\exp(-r^2/2)\). To prove the joint point-process assertion, condition on \(K_n=k\), take pairwise disjoint bounded half-open intervals \(I_1,\dots,I_d\subset[0,\infty)\), and let \(N_j\) count cyclic labels \(v\) with \(v/\sqrt n\in I_j\). If \(m_j\) is the number of such labels in \([n]\), then for fixed nonnegative integers \(\ell_j\), with \(\ell=\sum_j\ell_j\),
\[
\mathbb E\left[\prod_j (N_j)_{\ell_j}\mid K_n=k\right]
=\frac{(k)_\ell}{(n)_\ell}\prod_j(m_j)_{\ell_j}.
\]
For \(k/\sqrt n\to r>0\), this tends to \(r^\ell\prod_j|I_j|^{\ell_j}\), the factorial moments of independent Poisson variables with rates \(r|I_j|\). Tightness follows because the expected count on a fixed bounded interval is \(O(1)\), uniformly in \(n\), by \(\mathbb E K_n=O(\sqrt n)\). The conditional binomial/hypergeometric factorial generating functions give the corresponding Laplace convergence, and the Rayleigh mixture gives \(\Xi_n\Rightarrow\Xi\). For \(M_n\), either the first-arrival distribution of \(\Xi\) or the exact hypergeometric tail gives \(S(t)=\mathbb E\exp(-tR)\). Integration by parts yields the displayed integral identity. Substituting \(u=tr\) shows \(t^2S(t)\to\int_0^\infty u e^{-u}\,du=1\).

**3. Exact factorial moments of the least label.** Let \(x^{\overline s}:=\prod_{j=0}^{s-1}(x+j)\). From the conditional mass and the hockey-stick/Vandermonde identity (or the ordinary negative-hypergeometric waiting-time law), for every integer \(s\ge1\),
\[
\mathbb E[M_n^{\overline s}\mid K_n=k]
=s!\frac{(n+1)^{\overline s}}{(k+1)^{\overline s}},
\]
where all denominators are positive. Hence the exact, unconditional identity
\[
\mathbb E[M_n^{\overline s}]
=\frac{s!(n+1)^{\overline s}}n
\sum_{k=1}^{n}\frac{k Q_{n,k}}{(k+1)^{\overline s}}.
\tag{1}
\]
This formula remains exact for \(s>n\) and also at \(n=1\).

**4. First and critical second moments.** For \(s=1\), equation (1), \(Q_{n,k}\le e^{-k(k-1)/(2n)}\), and Riemann summation imply
\[
\frac{\mathbb E M_n}{\sqrt n}
\longrightarrow\int_0^\infty e^{-r^2/2}\,dr
=\sqrt{\pi/2}.
\]
For \(s=2\), write
\[
H_n=\sum_{k=1}^n\frac{kQ_{n,k}}{(k+1)(k+2)}.
\]
For \(k\le\lfloor\sqrt n\rfloor\), use \(0\le1-Q_{n,k}\le k(k-1)/(2n)\); replacing \(Q_{n,k}\) by one changes that partial sum by \(O(1)\), and the sum without \(Q\) equals \(\frac12\log n+O(1)\). For \(k>\sqrt n\), the exponential bound and comparison with \(\int_1^\infty e^{-u^2/3}du/u\) make the remaining sum \(O(1)\). Thus \(H_n=\frac12\log n+O(1)\). Equation (1) gives
\[
\mathbb E[M_n(M_n+1)]
=\frac{2(n+1)(n+2)}n H_n
=n\log n+O(n).
\]
Subtracting \(\mathbb E M_n=O(\sqrt n)\) shows \(\mathbb E M_n^2=n\log n+O(n)\), and subtracting \((\mathbb E M_n)^2=O(n)\) gives the claimed variance.

**5. All higher fixed moments.** For any integer \(s\ge3\), the summand \(kQ_{n,k}/(k+1)^{\overline s}\) is dominated by \(k/(k+1)^{\overline s}=O(k^{1-s})\), which is summable. For each fixed \(k\), \(Q_{n,k}\to1\). Dominated convergence in (1) therefore gives
\[
\lim_{n\to\infty}\frac{\mathbb E[M_n^{\overline s}]}{n^{s-1}}
=s!\sum_{k\ge1}\frac{k}{(k+1)^{\overline s}}
=s\int_0^1\frac{t}{(1-t)^2}(1-t)^{s-1}dt
=\frac{s}{(s-1)(s-2)}.
\]
The middle equality follows from \(\frac{s!}{(k+1)^{\overline s}}=s\int_0^1t^k(1-t)^{s-1}dt\) and \(\sum_{k\ge1}kt^k=t/(1-t)^2\). Since \(M_n^{\overline s}=M_n^s+\sum_{j<s}c_{s,j}M_n^j\), with fixed coefficients, and the lower moments are \(O(n\log n)\) for \(j=2\), \(O(\sqrt n)\) for \(j=1\), and \(O(n^{j-1})\) for \(j\ge3\), the same asymptotic holds for ordinary \(s\)-th moments. This proves every assertion.

## Verification

Execute `python3 check.py` using Python 3 and its standard library. The script exhaustively enumerates all self-maps for \(1\le n\le6\) and checks the cyclic-core distribution, every conditional minimum tail, and rising moments of orders one through five using exact rational arithmetic. It also computes numerical moment ratios through \(n=100000\). It reported 244 passing exact finite assertions. The numerical checks are sanity checks, not a proof of any infinite-population result; all limits above follow from the analytic arguments.

## Relationship to prior work

The classical cyclic-core distribution and Rayleigh law are not claimed to be new; random mapping statistics are developed by Flajolet and Odlyzko, and cyclic-core conditioning is treated by Hansen and Jaworski. Conditional uniformity of labeled cyclic sets follows from symmetry. The contribution here is the **first-label Cox limit together with the sharp non-uniform-integrability and all-fixed-integer-moment phase transition** for that specific label statistic. In particular, the \(n\log n\) variance and order \(n^{s-1}\) higher moments are not implied by convergence in distribution of \(K_n/\sqrt n\) alone. Comparisons with the accessible cited full text and research abstracts did not locate this combined statement, but do not establish absolute publication priority.

## Limitations

The result is restricted to uniform independent-image mappings and natural numerical vertex labels; relabeling the realization randomly changes the realized minimum but not its distribution. Convergence of point processes is weak, not total variation. The moment statement fixes integer order before letting \(n\) increase. No explicit error term is established for the Cox limit or for higher-moment ratios. The \(s=2\) limiting distribution has an infinite second moment, so one cannot infer the finite-size variance by naive moment convergence. Some historically relevant preprints and older books were not available in full text; priority is conditional on the stated comparisons and requires independent historical review.

## References

1. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, EUROCRYPT 1989 proceedings, 1990. DOI: https://doi.org/10.1007/3-540-46885-4_34.
2. J. C. Hansen and J. Jaworski, *Random mappings with exchangeable in-degrees*, Random Structures & Algorithms 33 (2008), 105–126; first publicly posted by publisher on 2007-09-04. https://doi.org/10.1002/rsa.20187.
3. J. C. Hansen and J. Jaworski, *Random mappings with a given number of cyclical points*, Ars Combinatoria 94 (2010), 341–359. https://combinatorialpress.com/article/ars/Volume%20094/volume-94-paper-34.pdf.
