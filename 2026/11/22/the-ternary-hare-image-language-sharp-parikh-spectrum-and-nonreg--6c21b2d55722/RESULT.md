# The ternary hare image language: sharp Parikh spectrum and nonregular rational growth

## Finding
Let \(h\) be the one-pass Defant–Kravitz **hare** stack-sorting map on the ordered ternary alphabet \(\{0,1,2\}\). For a binary word \(u\), let \(d_{10}(u)\) denote the number of occurrences of the *contiguous* factor `10`, including overlapping occurrences (none actually overlap one another). Then the complete language of outputs is
\[
\mathcal H=h(\{0,1,2\}^*)=\{u2^c:u\in\{0,1\}^*,\ c\ge d_{10}(u)\}.
\]
For all nonnegative integers \(a,b,c\), the image of the words with exactly \(a\) zeros, \(b\) ones and \(c\) twos has cardinality
\[
H_{a,b,c}=\sum_{j=0}^{\min(a,b,c)}\binom{a}{j}\binom{b}{j}.
\]
It includes every possible binary prefix of content \((a,b)\) if and only if \(c\ge\min(a,b)\), and this cutoff is sharp. The unbounded language \(\mathcal H\) is deterministic one-counter and nonregular. Its complete multivariate enumerator and its ordinary length enumerator are
\[
\sum_{a,b,c\ge0}H_{a,b,c}x^ay^bz^c=\frac1{(1-z)((1-x)(1-y)-xyz)},
\]
\[
\sum_{n\ge0}\lvert\mathcal H\cap\{0,1,2\}^n\rvert t^n=\frac1{(1-t)(1-2t+t^2-t^3)}.
\]
Consequently the number of distinct length-\(n\) outputs is asymptotic to \(K\lambda^n\), where \(\lambda=1.754877666246\ldots\) is the largest real root of \(\lambda^3-2\lambda^2+\lambda-1=0\) and \(K=2.223851198\ldots\).

## Assumptions and scope
All words are finite, including the empty word, over the fixed totally ordered alphabet \(0<1<2\). The hare map is defined recursively: if \(m\) is the greatest symbol appearing in a nonempty word and \(w=A_0mA_1m\cdots mA_k\) with no \(m\) in the blocks, then \(h(w)=h(A_0)h(A_1)\cdots h(A_k)m^k\); also \(h(\varepsilon)=\varepsilon\). The input content is fixed when calculating \(H_{a,b,c}\). The output language claim allows all contents and lengths. The word `10` is a *contiguous* substring, not a scattered subsequence. The variables in generating functions are commuting formal indeterminates.

## Proof
**1. Binary blocks.** For every binary input \(v\), the recursion gives \(h(v)=0^{\lvert v\rvert_0}1^{\lvert v\rvert_1}\). If \(w=A_0 2 A_1 2\cdots2 A_c\), the full ternary recursion therefore yields
\[
h(w)=\bigl(0^{a_0}1^{b_0}\bigr)\cdots\bigl(0^{a_c}1^{b_c}\bigr)2^c,
\]
where \(a_i,b_i\) are the contents of \(A_i\). Hence any binary output prefix is a concatenation of \(c+1\) weakly increasing binary blocks. An occurrence of `10` cannot lie inside any one such block, so the number of descents is at most \(c\).

**2. Converse.** Any binary word \(u\) with precisely \(d=d_{10}(u)\) occurrences of `10` has a canonical decomposition into \(d+1\) consecutive weakly increasing blocks, obtained by cutting immediately between each `1` and succeeding `0`. If \(d\le c\), subdivide these blocks (allow empty blocks) into exactly \(c+1\) weakly increasing blocks; for example, insert \(c-d\) empty blocks. Place a `2` between successive blocks. The resulting ternary input has hare image \(u2^c\). Thus the stated necessary condition is also sufficient, for every content including zeros.

**3. Exact Parikh count.** A binary word with \(a\) zeros, \(b\) ones and \(d\) descents has a unique run decomposition
\[
0^{x_0}1^{y_1}0^{x_1}\cdots1^{y_d}0^{x_d}1^{y_{d+1}},
\]
where \(x_0,y_{d+1}\ge0\), \(x_i\ge1\) for \(1\le i\le d\), and \(y_i\ge1\) for \(1\le i\le d\). Stars and bars gives \(\binom{a}{d}\) choices for the zero-run vector and \(\binom{b}{d}\) for the one-run vector (including \(d=0\)). Summing over \(d\le c\) proves the displayed formula. The maximum possible descent count for fixed content is \(\min(a,b)\), achieved by alternating as much as possible, proving the exact saturation threshold.

**4. Language class.** A deterministic counter automaton scans the binary prefix, remembering its previous bit and incrementing a counter at every `10`. At the first `2` it enters a terminal-symbol-only phase and decrements the counter for each `2` while positive; further twos are allowed. It accepts precisely when the counter is zero at the end, proving deterministic one-counter recognizability. For nonregularity, the words \((10)^j\) are pairwise Myhill–Nerode distinguishable: for \(i<j\), appending \(2^i\) makes \((10)^i2^i\) belong to \(\mathcal H\) but \((10)^j2^i\) not belong. Hence no finite automaton recognizes \(\mathcal H\).

**5. Generating functions and asymptotic.** For fixed \(d\), standard binomial generating functions give
\[
\sum_{a\ge d}\binom{a}{d} x^a=\frac{x^d}{(1-x)^{d+1}},\quad
\sum_{b\ge d}\binom{b}{d} y^b=\frac{y^d}{(1-y)^{d+1}},\quad
\sum_{c\ge d}z^c=\frac{z^d}{1-z}.
\]
Multiply and sum the geometric series over \(d\ge0\). This yields \(1/((1-z)((1-x)(1-y)-xyz))\). Set \(x=y=z=t\) for the ordinary series. The polynomial \(g(t)=1-2t+t^2-t^3\) has strictly negative derivative \(g'(t)=-2+2t-3t^2<0\) on the real axis, so its one real zero \(r=0.569840290998\ldots\) is simple and positive. The other two zeros form a complex-conjugate pair, whose product is \(1/r\) by Vieta, hence both have modulus \(\sqrt{1/r}>r\). The additional pole at \(t=1\) is also farther away. The simple pole at \(r\) therefore gives \(\lambda=1/r\) and \(K=-1/(r(1-r)g'(r))\) as claimed.

## Verification
Run `python3 verify_exhaustive.py` and `python3 verify_independent.py` using only the Python standard library. The first enumerates all ternary source and candidate output words through length ten and compares both their exact image sets and all fixed-content counts. The second independently counts accepted words by a direct counter-state dynamic program through length 39, comparing the binomial-sum formula and the coefficient recurrence \(h_n=3h_{n-1}-3h_{n-2}+2h_{n-3}-h_{n-4}\) (for \(n\ge4\)). Representative image counts at lengths zero through ten are \(1,3,6,11,20,36,64,113,199,350,615\). These finite checks support, but do not replace, the all-length proof above.

## Relationship to prior work
Defant and Kravitz introduced the hare/tortoise recursions and proved a general hook-configuration formula for the number of preimages of an individual output word. Campbell and Rampersad introduced stack-sorting complexity on factors of automatic sequences; their published treatment focuses on the binary alphabet and the tortoise operation. A separately established ternary *tortoise* image classification concerns a different map, so its language and counting formula do not entail the hare-image theorem here. The contribution here is an explicit all-content, all-length classification of one-pass ternary **hare** images, its one-counter/nonregular boundary, and its rational growth series; no independent priority guarantee is asserted.

## Limitations
The result treats the fixed three-symbol ordered alphabet and exactly one hare application. It does not characterize larger alphabets, iterated hare-image languages, or the complete preimage-fiber distribution for individual outputs. The existence of a general older algorithm for individual fertilities leaves the possibility of an equivalent earlier specialization; literature search cannot rule out unindexed results. This is a self-contained mathematical proof with finite checks, not an independently validated theorem.

## References
1. C. Defant and N. Kravitz, *Stack-sorting for Words*, arXiv:1809.09158, initially public 24 September 2018; especially Definition 1.1 and Theorem 3.2. https://arxiv.org/abs/1809.09158
2. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, initially public 28 April 2026; especially Sections 2–3. https://arxiv.org/abs/2604.25811
