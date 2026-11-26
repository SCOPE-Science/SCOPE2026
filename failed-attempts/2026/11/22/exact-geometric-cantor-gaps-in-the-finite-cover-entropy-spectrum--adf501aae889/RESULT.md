# Exact geometric Cantor gaps in the finite-cover entropy spectrum of Sturmian gap shifts

## Finding
Fix any irrational \(0<\alpha<1\), and define its lower mechanical word
\[
s_j=\lfloor(j+1)\alpha\rfloor-\lfloor j\alpha\rfloor\in\{0,1\},\qquad j\ge0.
\]
Let \(X_\alpha\subseteq\{0,1\}^{\mathbb Z}\) be the bilateral binary gap shift in which a word \(10^j1\) occurs only if \(s_j=1\). Let \(Y_N\) denote the canonical length-\((N+1)\) finite-type cover of \(X_\alpha\), with entropies \(h_N\) and \(h\), respectively. Let \(\lambda\in(1,2)\) be the unique root of
\[
\sum_{j\ge0}s_j\lambda^{-(j+1)}=1,
\qquad r=\lambda^{-1},\qquad
T=\sum_{j\ge0}(j+1)s_jr^{j+1}>0.
\]
Then the entropy excess has a uniform asymptotic for all positive integers \(N\):
\[
\boxed{\lambda^{N+1}(h_N-h)=\frac1T\sum_{j\ge0}(1-s_{N+j})r^j+O_\alpha(Nr^N).}
\]
The complete subsequential accumulation set \(K_\alpha\) on the left is an **uncountable compact perfect nowhere-dense set of Hausdorff dimension zero**. Its convex hull has length exactly \(1/T\). The bounded connected components of its complement *inside that convex hull* comprise exactly **one open interval for each integer \(n\ge1\)**, of length
\[
\boxed{\ell_n=\frac{(1-r)r^{n-1}}T.}
\]
Thus \(K_\alpha\) has zero Lebesgue measure and its complete geometric sequence of complementary interval lengths is explicit. In addition, the finite-type covers have the exact plateau law
\[
\boxed{Y_N=Y_{N+1}\quad\Longleftrightarrow\quad s_N=1.}
\]
At every other step their topological entropies strictly decrease.

## Assumptions and scope
All shifts are two-sided over \(\{0,1\}\). A *zero-run length* \(j\) means the number of zeros between successive symbols \(1\), so the corresponding return distance is \(j+1\). The gap shift is the closure of bi-infinite concatenations of permitted return blocks; equivalently a binary configuration is legal precisely when every factor \(10^j1\) has \(s_j=1\). One-sided zero tails and the all-zero point are included. The canonical length-\((N+1)\) cover has all its length-\((N+1)\) words from \(X_\alpha\), and \(N\ge1\). The error term is for fixed irrational \(\alpha\); it is not asserted to be uniform in the slope. The cluster set includes all finite subsequential limits as \(N\to\infty\), with no dependence on a chosen subsequence. All entropy uses natural logarithms. The phase interval is \([0,1)\) with its natural circular endpoints.

## Proof
**1. Exact canonical cover.** The minimal forbidden blocks of the original gap shift are precisely \(10^j1\) for those \(j\ge0\) with \(s_j=0\): permitted finite gaps may be concatenated arbitrarily, and any finite prefix or suffix can be completed using arbitrarily long permitted gaps. The block \(10^j1\) has length \(j+2\), so the length-\((N+1)\) cover forbids it exactly when \(j<N\). Thus \(Y_N\) is the cofinite gap shift with permitted zero-run lengths
\[
\{j<N:s_j=1\}\ \cup\ \{N,N+1,\ldots\}.
\]
The standard renewal return equation for a binary gap shift gives \(h=\log\lambda\), and \(h_N=\log\lambda_N\), where \(\lambda_N>1\) uniquely solves
\[
\sum_{j<N}s_j\lambda_N^{-(j+1)}+
\frac{\lambda_N^{-(N+1)}}{1-\lambda_N^{-1}}=1.
\]
The mechanical word has infinitely many ones and zeros and is not eventually periodic; hence the defining series has a unique root strictly between \(1\) and \(2\). The finite covers have a finite irreducible aperiodic renewal-graph presentation, and their roots tend downward to \(\lambda\). The renewal-root identity is standard background, not a new theorem.

**2. Uniform normalized entropy difference.** Put \(f(u)=\sum_{j\ge0}s_j e^{-(j+1)u}\) and \(f_N(u)=\sum_{j<N}s_j e^{-(j+1)u}+\sum_{j\ge N}e^{-(j+1)u}\). These have \(f(h)=f_N(h_N)=1\), and
\[
f_N(h)-1=r^{N+1}\sum_{j\ge0}(1-s_{N+j})r^j.
\]
The last tail is bounded above by \(1/(1-r)\), independent of \(N\); it is nonnegative. Also \(f'(h)=-T\), \(f_N'(h)=-T+O_\alpha(Nr^N)\), and the second derivatives are uniformly bounded on a fixed neighborhood of \(h>0\). The implicit-root mean-value estimate first yields \(h_N-h=O_\alpha(r^{N+1})\). Expanding \(f_N(h_N)=1\) at \(h\), and then multiplying by \(r^{-(N+1)}\), gives the displayed uniform asymptotic with an \(O_\alpha(Nr^N)\) remainder. This is an analytic statement for every \(N\), not a conclusion extrapolated from finite computations.

**3. Rotation phases and ordered jumps.** For \(\theta\in[0,1)\), write
\[
s_j(\theta)=\lfloor\theta+(j+1)\alpha\rfloor-
\lfloor\theta+j\alpha\rfloor,\qquad
G(\theta)=\sum_{j\ge0}s_j(\theta)r^j.
\]
Since \(\{N\alpha\}\) is dense in the circle, and \(s_{N+j}=s_j(\{N\alpha\})\), the asymptotic implies
\[
K_\alpha=\overline{\left\{\frac{1/(1-r)-G(\{N\alpha\})}{T}:N\ge1\right\}}.
\]
At a phase \(0<\theta<1\), each \(s_j(\theta)\) is locally constant except where \(\theta=\{-n\alpha\}\) for some \(n\ge1\). At the particular phase \(\theta_n=\{-n\alpha\}\), only \(s_{n-1}\) and \(s_n\) change: from \((0,1)\) immediately left to \((1,0)\) immediately right. Accordingly \(G\) jumps upward by exactly \((1-r)r^{n-1}\). These phases are distinct and dense.

For \(0\le\theta<\eta<1\), a telescoping identity gives for every \(m\ge1\)
\[
\sum_{j=0}^{m-1}\bigl(s_j(\eta)-s_j(\theta)\bigr)
=\lfloor\eta+m\alpha\rfloor-\lfloor\theta+m\alpha\rfloor
\in\{0,1\}.
\]
Summation by parts now gives
\[
G(\eta)-G(\theta)=
(1-r)\sum_{m\ge1}r^{m-1}
\bigl(\lfloor\eta+m\alpha\rfloor-\lfloor\theta+m\alpha\rfloor\bigr)>0.
\]
The strict inequality uses the density of \(\{-m\alpha\}\), ensuring at least one (indeed infinitely many) positive summands. Thus \(G\) is strictly increasing, and its jumps remove pairwise disjoint open intervals from the closure of its range. At the endpoints, \(s_j(1-)=s_j(0)\) for every \(j\ge1\), whereas \(s_0(1-)=1\) and \(s_0(0)=0\); therefore \(G(1-)-G(0)=1\). The full convex hull of its closure has length one.

**4. Complete complementary-interval census.** The sum of all its distinct positive jump widths is
\[
\sum_{n\ge1}(1-r)r^{n-1}=1=G(1-)-G(0).
\]
Every jump produces an omitted open interval: no value of the strictly increasing function (including either one-sided limit) can lie strictly between its left and right limits. The listed disjoint gaps therefore exhaust the convex hull up to a set of Lebesgue measure zero; there cannot be any additional complementary open interval of positive length, because the total of the listed widths already equals the hull length. The orbit \(\{\{N\alpha\}:N\ge1\}\) is dense on both sides of every phase, so its discounted-digit images have precisely the same closure as the full two-sided one-sided-limit range of \(G\). Reflection by \(1/(1-r)\) and division by \(T\) preserve the gap census apart from the scaling factor \(1/T\), yielding exactly the lengths \(\ell_n\) and hull length \(1/T\) claimed.

The resulting set is compact and has empty interior by the dense jump locations. It has no isolated points: every phase, including either side of a jump, is approached by distinct phases, and strict monotonicity gives distinct nearby values. It is therefore a perfect nowhere-dense compact set and is uncountable. For any \(m\ge1\), the mechanical words \(s_0(\theta)\cdots s_{m-1}(\theta)\), allowing both one-sided versions at discontinuities, have exactly \(m+1\) distinct possibilities (the standard Sturmian factor complexity). All values with the same length-\(m\) prefix lie in an interval of diameter at most \(r^m/(1-r)\). Consequently \(K_\alpha\) can be covered by \(m+1\) intervals of diameter at most \(r^m/[T(1-r)]\). For every \(\delta>0\), their total \(\delta\)-power length tends to zero as \(m\to\infty\); hence \(\dim_HK_\alpha=0\).

**5. Exact plateaus.** The only new minimal forbidden word when passing from \(Y_N\) to \(Y_{N+1}\) is \(10^N1\). If \(s_N=1\), there is no new restriction and both systems coincide. If \(s_N=0\), the periodic point \((10^N)^{\mathbb Z}\) belongs to \(Y_N\) but not to \(Y_{N+1}\). The finite-type system \(Y_N\) has an irreducible presentation; a proper subshift of an irreducible finite-type shift has strictly smaller entropy. This proves both the exact equality stages and the strict decrease elsewhere.

## Verification
The standalone standard-library file `check.py` was executed after writing the proof. It independently compared the cutoff gap-language rule against the definition that **every visible window of length at most \(N+1\)** belongs to the original gap shift in 18,414 finite binary word/cutoff comparisons, verified 23 plateau witnesses, compared 18 geometric phase jumps with high-precision discounted mechanical digits, checked the unit hull/jump-sum identity, and checked the normalized entropy asymptotic numerically at eight cover lengths. All assertions passed. These computations are diagnostic checks of formulas and indexing, not infinite proofs.

For \(\alpha=(\sqrt5-1)/2\), numerical evaluation gives \(\lambda\approx1.4569740225048505\), \(T\approx3.985988427074893\), convex-hull length \(1/T\approx0.2508788016561923\), and first complementary interval length \((1-r)/T\approx0.0786871237120119\). The theorem applies to every irrational slope, with no bounded-type hypothesis.

## Relationship to prior work
Coles, Cyr, Kra and Pavlov (2026) define canonical finite-type approximations and investigate entropy stability and qualitative entropy-decay conditions. Their results do not supply an exact entropy-tail expansion or a geometric Cantor gap census for a Sturmian-indexed gap set. Classical S-gap renewal work (Ahmadi Dastjerdi–Jangjoo; Climenhaga's expository derivation) supplies the entropy equation, which is used rather than claimed new. Bugeaud and Laurent study the number-theoretic continued fractions of numbers with Sturmian digit expansions; that is a different invariant, though it motivates caution about whether the discounted mechanical-word jump structure is independently known.

The published result *A countable entropy-phase spectrum in finite-type covers of geometric gap shifts* concerns sparse power-of-base return distances and has a **countable**, one-limit-point cluster set, with no Sturmian rotation or Cantor complement census. The published *Periodic zeta rationality versus Sturmian nonsoficity in decorated gap shifts* concerns three-symbol words with Sturmian **blocks between markers** (an arbitrary gap set), not a binary gap shift whose **allowed gap lengths form a Sturmian index set**; it classifies periodic zeta functions rather than canonical-cover errors. A separate published Fibonacci Sturmian *language*-cover theorem treats entropy converging to zero, not positive-entropy binary gap shifts. A general normalized renewal-tail formula, by itself, would not imply the strictly ordered geometric jump census here.

## Limitations
The claim classifies a binary gap system whose *indicator of allowed zero-run lengths* is the fixed lower mechanical Sturmian word, not every Sturmian decoration and not arbitrary gap sets. The normalization requires the root \(\lambda\) and finite positive constant \(T\) associated to that indicator. It does not claim uniform error constants as the irrational slope varies, a finite-dimensional Markov presentation of the original shift, or a characterization of all maximal-entropy measures. The renewal-root and Sturmian-factor-complexity inputs are classical. A potential equivalent gap-spectrum statement in older Sturmian digit-expansion or renewal literature cannot be excluded conclusively from current bibliographic searches; independent audit and historical-priority verification remain outstanding.

## References
1. Solly Coles, Van Cyr, Bryna Kra and Ronnie Pavlov, *Stable covers of subshifts*, arXiv:2602.04097v1, first public 2026-02-04; https://arxiv.org/abs/2602.04097 (especially finite-type covers and entropy stability).
2. D. Ahmadi Dastjerdi and S. Jangjoo, *Computations on Sofic S-gap Shifts*, arXiv:1108.3414; https://arxiv.org/abs/1108.3414 (S-gap renewal background).
3. Vaughn Climenhaga, *Entropy of S-gap shifts*, 2014-09-08; https://vaughnclimenhaga.wordpress.com/2014/09/08/entropy-of-s-gap-shifts/ (explicit renewal-root derivation).
4. Yann Bugeaud and Michel Laurent, *Combinatorial structure of Sturmian words and continued fraction expansions of Sturmian numbers*, arXiv:2104.09239v1, 2021-04-19; https://arxiv.org/abs/2104.09239 (adjacent Sturmian digit-expansion literature).
5. *A countable entropy-phase spectrum in finite-type covers of geometric gap shifts*, published research record, 2026-10-18; https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-countable-entropy-phase-spectrum-in-finite-type-covers-of-geom--1fd88ee11f52.
6. *Periodic zeta rationality versus Sturmian nonsoficity in decorated gap shifts*, published research record, 2026-10-25; https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-periodic-zeta-rationality-versus-sturmian-nonsoficity-in-decorat--0881e8e9b148.
7. *A Fibonacci entropy staircase and its full scaled accumulation interval*, published research record, 2026-10-11; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-fibonacci-entropy-staircase-and-its-full-scaled-accumulation-i--be7c0c99809f.
