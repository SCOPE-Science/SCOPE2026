# Exact bounded-range subsequence spectra of two-block periodic words

## Finding

Fix positive integers \(a,b\), put \(L=a+b\), and consider the one-sided infinite binary word
\[
X_{a,b}=(0^a1^b)^\omega.
\]
For each nonempty finite binary pattern \(u=u_1\cdots u_k\), define its **minimum embedding span** \(s_{a,b}(u)\) as the minimum of \(j_k-j_1+1\) over positions \(0\le j_1<\cdots<j_k\) with \(X_{a,b}[j_i]=u_i\). This is the shortest window length containing \(u\) as a subsequence. The minimum exists for every pattern.

**Exact run formula.** Write \(u=c_1^{\ell_1}\cdots c_r^{\ell_r}\) in maximal constant-letter runs. For each run, let \(d_i=a\) when \(c_i=0\), and \(d_i=b\) when \(c_i=1\); uniquely write
\[
\ell_i=q_i d_i+s_i,\qquad q_i\ge0,\quad 1\le s_i\le d_i.
\]
Then
\[
s_{a,b}(u)=\begin{cases}
q_1 L+s_1,&r=1,\\
L\sum_{i=1}^r q_i+s_1+s_r+\sum_{i=2}^{r-1}d_i,&r\ge2.
\end{cases}
\tag{1}
\]

**Exact spectrum generating function.** Define the rational functions
\[
F_d(x,z)=\frac{\sum_{s=1}^{d}(xz)^s}{1-x^d z^L},\qquad
G_d(x,z)=\frac{z^d\sum_{s=1}^{d}x^s}{1-x^d z^L}
\qquad(d\in\{a,b\}).
\]
The bivariate generating function of all nonempty patterns, counted once each by their length and their minimum embedding span, is
\[
H_{a,b}(x,z)=\sum_{u\in\{0,1\}^{+}}x^{|u|}z^{s_{a,b}(u)}
=F_a+F_b+\frac{2F_aF_b+F_a^2G_b+F_b^2G_a}{1-G_aG_b}.
\tag{2}
\]
All functions on the right are evaluated at \((x,z)\). In particular, for every \(k,p\ge1\), the number of distinct length-\(k\) patterns occurring as subsequences in **some** length-\(p\) factor of \(X_{a,b}\) is exactly
\[
\sum_{j=1}^{p}[x^kz^j]H_{a,b}(x,z).
\tag{3}
\]
There are exactly \(2^k\) possible patterns; subtracting (3) gives the number absent from every length-\(p\) factor.

**Sharp full-universality threshold.** Let \(m=\min(a,b)\), \(M=\max(a,b)\), and let \(T_{a,b}(k)=\max_{u\in\{0,1\}^k}s_{a,b}(u)\). For all positive \(k\), the exact answer is
\[
T_{a,b}(k)=\begin{cases}
1+(k-1)L,&m=1,\\
1,&m\ge2,\ k=1,\\
(t-1)L+2,&m\ge2,\ k=2t,\ t\ge1,\\
tL+1,&m=2,\ k=2t+1,\ t\ge1,\\
(t-1)L+M+2,&m\ge3,\ k=2t+1,\ t\ge1.
\end{cases}
\tag{4}
\]
Every binary pattern of length \(k\) occurs in some length-\(p\) factor of \(X_{a,b}\) **if and only if** \(p\ge T_{a,b}(k)\). These are unions over windows; no claim that a single window contains all patterns.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), \(a,b,k,p\) are positive integers, and the host is the one-sided periodic word \(X_{a,b}\). For a pattern of length \(k\), its first and last selected indices determine the span; there is no wraparound restriction and a window may cross arbitrarily many periods. Formula (2) is an identity in formal bivariate power series with coefficients in the nonnegative integers. No random choices or numerical approximations occur in the statements.

## Proof

**Step 1: optimal embedding through runs.** The source has one zero block of length \(a\) and one one block of length \(b\) in each period. For fixed initial selected position, greedily selecting the earliest available occurrence of each next letter never makes any later selection impossible or later than a nongreedy embedding. For a one-run pattern \(c^\ell\), the optimal start is the first position of a block of \(c\); if \(\ell=qd+s\) with \(1\le s\le d\), the final selected position is \(qL+s-1\) after the start, giving \(qL+s\).

For at least two pattern runs, suppose the first run has length \(q_1d_1+s_1\). A best embedding begins with the last \(s_1\) positions of a source block of \(c_1\): the last selected position of that pattern run then coincides with the end of a source block after \(q_1\) periods, and the opposite symbol starts immediately afterward. Starting earlier within a source block only increases the distance to the next opposite block; starting later makes an additional whole source block necessary. Each internal run starts at the first position of a block of its letter, traverses \(q_i\) full periods, and uses the last \(s_i\) positions of a later block; the next opposite letter starts exactly \(q_iL+d_i\) positions after the first selected position of that run. The final run, starting at its source-block beginning, needs \(q_rL+s_r\) selected-span units. Adding these distances proves (1), with the \(s_1\) contribution from the initial run, \(d_i\) for each internal run, and \(s_r\) for the final run. Since the period is repeated without end, the optimal initial phase is always available in the one-sided source.

**Step 2: rational enumerator.** For a run of symbol with source capacity \(d\), the pair \((\ell,qd+s)\) contributes \(x^{qd+s}z^{qL+s}\) at an endpoint, summed by \(F_d\). An internal run contributes \(x^{qd+s}z^{qL+d}\), summed by \(G_d\). Single-run patterns contribute \(F_a+F_b\). For even run counts at least two, alternating runs contribute \(2F_aF_b\sum_{j\ge0}(G_aG_b)^j\). For odd run counts at least three, they contribute \((F_a^2G_b+F_b^2G_a)\sum_{j\ge0}(G_aG_b)^j\). These disjoint cases exhaust the unique maximal-run decomposition of every nonempty pattern. Summing the geometric series proves (2); the definition of span proves (3).

**Step 3: sharp threshold for patterns of at least two runs.** Assume \(a,b\ge2\), let \(R\ge2\) be the number of pattern runs, put \(Q=\sum_iq_i\), \(Y=s_1+s_R\), and define
\[
D=\sum_{i=1}^{R}q_i(d_i-2)+\sum_{i=2}^{R-1}(s_i-1)\ge0.
\]
By the decomposition of every run, \(k=2Q+Y+(R-2)+D\). By (1),
\[
s_{a,b}(u)=LQ+Y+\sum_{i=2}^{R-1}d_i.
\]
If \(R\) is even, the internal capacities occur in balanced pairs, giving \(\sum_{i=2}^{R-1}d_i=(R-2)L/2\). Consequently
\[
s_{a,b}(u)=\frac L2 k-\left(\frac L2-1\right)Y-\frac L2D
\le\frac L2(k-2)+2.
\tag{5}
\]
If \(R\) is odd, the internal capacities have one extra copy of the capacity \(d_*\) of the letter opposite to the initial letter. Therefore
\[
s_{a,b}(u)=\frac L2(k-3)+2+d_*
-\left(\frac L2-1\right)(Y-2)-\frac L2D.
\tag{6}
\]
For odd \(k\), equations (5) and (6), together with \(d_*\le M\) and \(M\ge L/2\), give \(s_{a,b}(u)\le (k-3)L/2+M+2\). For even \(k\), (5) gives \(s_{a,b}(u)\le(k-2)L/2+2\). To cover (6) with even \(k\) and odd \(R\), observe that \(k-R=2Q+(Y-2)+D\) is odd; thus \((Y-2)+D\ge1\). The last two nonpositive terms of (6) then subtract at least \(L/2-1\), and \(d_*\le L-1\) gives the same even-length bound. Alternating patterns attain the relevant bounds: for even \(k\), either alternating start works; for odd \(k\), choose its endpoints to be the letter whose **opposite** source block has length \(M\). Thus these are the exact maxima among all patterns with at least two runs.

**Step 4: comparison with constant patterns.** The larger span among the two constant patterns of length \(k\) belongs to the symbol with shorter source-block length \(m\), and equals \(qL+r\), where \(q=\lfloor(k-1)/m\rfloor\), \(r=k-qm\). For \(m=1\) it equals \(1+(k-1)L\). Every pattern has span at most that value, since, after its first selected letter, each next desired letter is available within at most \(L\) additional source positions. For \(m=2\), substitution into the constant-pattern formula gives \((t-1)L+2\) at \(k=2t\) and \(tL+1\) at \(k=2t+1\); the odd value exceeds the alternating bound by exactly one. For \(m\ge3\), the constant-pattern value never exceeds the alternating bound: for even \(k=2t\), \(q\le t-1\); if equality holds then \(r\le2\), otherwise the spare full period exceeds the remaining \(r\le m\). For odd \(k=2t+1\), \(q\le t-1\) and \(r\le m\le M\), giving the claimed comparison. The case \(k=1\) is immediate. Combining the constant and mixed cases establishes all of (4), including attainability.

## Verification

The accompanying dependency-free Python program `periodic_span_verify.py` constructs an independent reference span by enumerating all source phases and greedily embedding every binary pattern, rather than using (1) to generate the reference answer. Running `python3 periodic_span_verify.py` passed 36,792 exact-span comparisons for \(1\le a,b\le6\), \(1\le k\le9\), 324 sharp-threshold comparisons, and 667 independently expanded generating-function coefficient comparisons for \(1\le a,b\le4\), \(1\le k\le7\), with coefficient mass totals \(2^k\). Those computations test boundaries and arithmetic, while the argument above proves every parameter value.

For example, \(a=2,b=3,k=3\) gives the exact shortest-span histogram \(\{3:5,4:1,5:1,6:1\}\), so every length-three pattern appears in some source window of length six, but not all appear by length five. When \(a=b=1\), (2) simplifies to \(2xz/(1-xz-xz^2)\), encoding the elementary count \(2\binom{k-1}{p-k}\) for span \(p\) (with out-of-range binomial coefficients zero).

## Relationship to prior work

Kosche, Koß, Manea and Pak introduced and studied bounded-range subsequence matching and analysis, including general hardness and algorithms (first publicly available 2022-07-19). Their problem definition is used here, but their theorems do not give (1), (2), or (4) for two-block periodic words. Adamson and colleagues later studied counts of absent unrestricted subsequences under a fixed universality index; that is a different enumeration and does not enforce a bounded window. Menon and Singh studied counts of indexed occurrences of patterns as subsequences of finite words, which is also distinct from the minimum-span distribution of distinct patterns in a fixed periodic host. Generic automaton algorithms can of course compute individual finite cases but do not supply the explicit all-parameter rational spectrum and sharp formula here. Bibliographic searches cannot establish uniqueness against unindexed work.

## Limitations

The result concerns the specific canonical two-block periodic source and subsequences with **one** overall window-length constraint. It neither settles bounded-range matching complexity for arbitrary hosts nor describes gap-by-gap constraints, nonbinary alphabets, or occurrence multiplicities. The generating function counts each distinct pattern once, rather than counting multiple embeddings. The same-model correctness, originality and value review does not constitute independent verification; novelty remains provisional until a separate literature audit.

## References

1. M. Kosche, T. Koß, F. Manea and V. Pak, *Subsequences in Bounded Ranges: Matching and Analysis Problems*, arXiv:2207.09201, first posted 2022-07-19. https://arxiv.org/abs/2207.09201
2. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn and M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599, first posted 2024-07-26. https://arxiv.org/abs/2407.18599
3. K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870, first posted 2023-06-13. https://arxiv.org/abs/2306.07870
