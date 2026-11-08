# A ternary double-Poisson threshold for shattering by coordinate-equality predicates

## Finding

**Theorem (three alphabet regimes).** Fix an integer \(q\ge2\) and a real \(c\). For each positive integer \(m\), sample independent uniform words \(X_1,\ldots,X_m\) from the categorical product \([q]^{d_m}\), and form the **positive coordinate-equality concept class**
\[
\mathcal H_{q,d}=\bigl\{H_{i,a}=\{x\in[q]^d:x_i=a\}:1\le i\le d,\ a\in[q]\bigr\}.
\]
There are no added complement concepts, no constant concepts, and no learned leaf-label reversals. For the binary alphabet set
\[
 d_m=\left\lfloor 2^{m-1}\bigl(\log(2^{m-1})+c\bigr)\right\rfloor.
\]
For each fixed alphabet size \(q\ge3\), instead set
\[
 d_m=\left\lfloor\frac{q^{m-1}}{q-1}(\log m+c)\right\rfloor.
\]
Then
\[
\lim_{m\to\infty}\Pr\bigl(\{X_1,\ldots,X_m\}\text{ is shattered by }\mathcal H_{q,d_m}\bigr)
=\begin{cases}
\exp(-e^{-c}),&q=2,\\
\exp(-e^{-c}-\tfrac12e^{-2c}),&q=3,\\
\exp(-e^{-c}),&q\ge4.
\end{cases}
\]
The limit is unchanged under uniform sampling of distinct words. In the ternary case, the numbers of unrealized traces of sizes \(m-1\) and \(m-2\) converge jointly to independent Poisson variables of respective means \(e^{-c}\) and \(\tfrac12e^{-2c}\). Simultaneously, with probability tending to one, all other trace sizes occur.

**Finite extremal comparison.** For every integer \(q\ge2\) and \(d\ge1\),
\[
 \operatorname{VCdim}(\mathcal H_{q,d})=1+\lfloor\log_2d\rfloor.
\]
The novel asymptotic conclusion is a statement about uniformly random supports, not simply the worst-case VC dimension.

## Assumptions and scope

For a labeled \(m\)-tuple \(\mathbf X\), a trace is a set \(T\subseteq[m]\) of indices whose samples belong to a single concept. A tuple is shattered if all \(2^m\) traces occur. This is equivalent to shattering its underlying set when the samples are pairwise distinct. A repeated sample cannot be shattered. Logarithms are natural; \(q\) and \(c\) are fixed as \(m\to\infty\). The integer dimensions above are nonnegative for all sufficiently large \(m\). In each coordinate the vector of \(m\) symbol-values is an independent uniform member of \([q]^m\).

The expression \(\mathcal H_{q,d}\) is the unlabeled positive-literal family: for \(q\ge3\), it is **not** a family of all categorical binary splits, and for \(q=2\) it contains only the two fibers of each coordinate. This normalization matters for the exact threshold.

## Proof

**1. Trace-covering equivalence.** A coordinate partitions \([m]\) into at most \(q\) fibers, one per symbol. The family shatters if and only if every nonempty subset occurs as one of these fibers and the empty subset occurs somewhere. In particular, a constant column realizes both the full subset and an empty fiber because \(q\ge2\). Thus realizing every nonempty subset automatically realizes the empty subset as well. For a fixed target \(T\) of size \(m-j\), with \(1\le j\le m-1\), the events that its fiber has symbol \(a\in[q]\) are disjoint: all positions of \(T\) must have symbol \(a\), and all \(j\) outside positions must have a different symbol. Hence a single column realizes \(T\) with exact probability
\[
 p_j=q\cdot q^{-(m-j)}\left(\frac{q-1}{q}\right)^j
 =\frac{(q-1)^j}{q^{m-1}}.
\]
For \(T=[m]\), the probability is \(p_0=q^{1-m}\), corresponding to a constant column.

**2. Binary case.** When \(q=2\), a coordinate realizes the pair \(\{T,[m]\setminus T\}\) of complementary fibers, even when one is empty. Every binary column selects uniformly one of exactly \(M=2^{m-1}\) unordered complementary pairs. Different coordinates select independent pairs. Thus shattering is *exactly* the classical coupon-collector event of observing all \(M\) coupons after \(d_m=\lfloor M(\log M+c)\rfloor\) draws. For any fixed \(r\), the \(r\)-th factorial moment of the number of missing pairs is
\[
 (M)_r(1-r/M)^{d_m}\longrightarrow e^{-rc},
\]
so the number missing converges to \(\mathrm{Poisson}(e^{-c})\), giving the first limit.

**3. Nonbinary near-full traces.** Let \(q\ge3\), \(h=q-1\) and \(K=q^{m-1}/h\). At \(d_m=\lfloor K(\log m+c)\rfloor\), the absence probability of a specified trace \(T\) with \(j\) omitted points is
\[
 (1-p_j)^{d_m}=\exp\bigl(-h^{j-1}(\log m+c)+o(1)\bigr)
\]
for each fixed \(j\ge1\), because \(d_mp_j=h^{j-1}(\log m+c)+o(1)\) and \(d_mp_j^2=o(1)\). For fixed integers \(r,s\ge0\) and \(m\ge5\), any two distinct target sets of sizes \(m-1\) or \(m-2\) intersect, so a single coordinate cannot realize two of them as different fibers. A column therefore hits exactly one among any fixed selection of \(r\) targets of size \(m-1\) and \(s\) targets of size \(m-2\), or hits none, with total hit probability \(rp_1+sp_2\).

Let \(Z_1,Z_2\) count the absent target sets of those two respective sizes. The exact joint factorial moment is
\[
 \mathbb E\bigl[(Z_1)_r(Z_2)_s\bigr]
 =(m)_r\left(\binom m2\right)_s
 (1-rp_1-sp_2)^{d_m}.
\]
The last factor equals \(\exp(-(r+hs)(\log m+c)+o(1))\), so for \(q=3\), \(h=2\),
\[
 \mathbb E\bigl[(Z_1)_r(Z_2)_s\bigr]
 \longrightarrow (e^{-c})^r\bigl(\tfrac12e^{-2c}\bigr)^s.
\]
These are the joint factorial moments of independent Poisson variables. Tightness and the factorial-moment characterization give joint convergence and
\[
 \Pr(Z_1=Z_2=0)\longrightarrow\exp(-e^{-c}-\tfrac12e^{-2c}).
\]
For \(q\ge4\), \(h\ge3\); the same one-family computation yields \(Z_1\Rightarrow\mathrm{Poisson}(e^{-c})\), but \(\mathbb E Z_2\sim\frac12m^{2-h}e^{-hc}\to0\).

**4. No additional missing traces.** The probability that the full set \([m]\) is absent is at most
\[
 (1-q^{1-m})^{d_m}\le \exp(-d_mq^{1-m})
 =m^{-1/h}e^{-c/h+o(1)}\longrightarrow0.
\]
For any other \(j\in\{1,\ldots,m-1\}\), the union bound gives
\[
 \Pr(\exists\text{ missing trace omitting }j\text{ points})
 \le\binom mj\exp(-d_mp_j).
\]
To make this bound **uniform in the omitted-set size**, note that the floor in \(d_m\) gives, for every \(1\le j\le m-1\),
\[
 d_mp_j\ge h^{j-1}(\log m+c)-p_j\ge h^{j-1}(\log m+c)-1.
\]
Hence the union-bound summand is at most \(e\binom mj\exp[-h^{j-1}(\log m+c)]\). Put \(a_j=m^j\exp[-h^{j-1}(\log m+c)]\); then for each integer \(j\ge1\),
\[
 \frac{a_{j+1}}{a_j}=m\exp[-h^{j-1}(h-1)(\log m+c)].
\]
For \(q=3\), thus \(h=2\), all \(j\ge3\) satisfy \(a_{j+1}/a_j\le m\exp[-4(\log m+c)]\le m^{-2}\) for all sufficiently large \(m\). The initial term \(a_3=m^3\exp[-4(\log m+c)]=O(m^{-1})\), so the complete tail is \(o(1)\). When \(q\ge4\), \(h\ge3\), all \(j\ge2\) satisfy \(a_{j+1}/a_j\le m\exp[-6(\log m+c)]\le m^{-2}\) eventually, while \(a_2=m^2\exp[-h(\log m+c)]=O(m^{2-h})=o(1)\). This covers even \(j\) growing with \(m\), not just fixed omitted-set size. Thus only the counted near-full missing families affect the limit.

**5. Without replacement.** For \(m\) independent samples, the collision probability is at most \(\binom m2q^{-d_m}\to0\). Conditional on no collisions the distribution is exactly uniform sampling without replacement, so the probabilities in the theorem differ by \(o(1)\).

**6. Deterministic VC dimension.** Fix any hypothetical shattered \(m\)-point support. Give a nonempty subset \(T\) weight \(1\) if \(|T|>m/2\), weight \(1/2\) if \(|T|=m/2\), and weight \(0\) otherwise. Every coordinate's disjoint symbol fibers have total weight at most \(1\), whereas the sum of weights over all \(2^m\) subsets is \(2^{m-1}\). Hence shattering requires \(d\ge2^{m-1}\). Conversely, assign one binary-valued coordinate to each unordered complementary pair \(\{T,T^c\}\), using two symbols of \([q]\); its two fibers realize that entire pair. The resulting \(m\) words are distinct for \(m\ge2\), and the constant-pair column realizes empty and full traces. Thus \(d=2^{m-1}\) suffices, and increasing \(d\) preserves shattering. This proves \(\operatorname{VCdim}=1+\lfloor\log_2d\rfloor\) (including \(m=1\)).

## Verification

The accompanying standalone script `verify_stumps.py` tests the trace-covering characterization using two independent exact algorithms: dynamic programming over achievable trace masks and direct enumeration of every coordinate array. Twelve small parameter triples were checked (including ternary dimension four and four-symbol samples). It also independently evaluates the exact finite-size probability that all asymptotically critical near-full targets are present by inclusion–exclusion, and evaluates a union-bound control for the other targets for several small \(m\). The exact results are recorded in `verification_output.txt`. They corroborate the proof but do not replace the all-\(m\) factorial-moment and uniform union-bound arguments.

## Relationship to prior work

Leboeuf, LeBlanc and Marchand (2022, arXiv:2210.10781v1, Section 5.3 and Theorem 10) study the unitary comparison split on nominal features and bound worst-case two-partitioning functions for decision stumps. Their hypothesis rules allow signed reversals, and their result concerns worst-case attainable partitions rather than the probability that a uniformly random support is shattered by the uncomplemented positive-fiber class. It supplies the natural source setting but not the ternary two-Poisson law. Their earlier 2020 work treats real-valued feature partitions.

Godbole, Pinella and Zhuang (2013, arXiv:1301.6371v1) study random shattering thresholds for systems of words and covering arrays. Their sampled objects and quantified requirement involve covering all patterns in fixed coordinate sets, rather than covering all \(2^m\) subsets of \(m\) random sample rows as a single coordinate-symbol fiber. Neither their event nor their probabilistic scale implies the ternary double-Poisson result through the inspected statements. The relationship invites further comparison under covering-array dualities.

## Limitations

The alphabet size \(q\) is fixed: simultaneous growth of \(q\) with \(m\) is not proved. This theorem concerns precisely the positive coordinate-equality family, not richer classifiers, generalized thresholds, conjunctions, learned stump labels, or arbitrary distributions on words. The asymptotic assertions do not give a finite-sample sharp error constant. The joint factorial-moment argument counts near-full subsets; only the separate uniform union bound proves that these suffice. Literature comparisons were limited to available sources and do not establish absolute historical priority. No independent mathematical audit is claimed.

## References

1. J.-S. Leboeuf, F. LeBlanc, and M. Marchand, *Generalization Properties of Decision Trees on Real-valued and Categorical Features*, arXiv:2210.10781v1, first public 2022-10-18. Section 5.3 and Theorem 10. https://arxiv.org/abs/2210.10781
2. A. P. Godbole, S. Pinella, and Y. Zhuang, *Shattering Thresholds for Random Systems of Sets, Words, and Permutations*, arXiv:1301.6371v1, first public 2013-01-27. https://arxiv.org/abs/1301.6371
3. J.-S. Leboeuf, F. LeBlanc, and M. Marchand, *Decision trees as partitioning machines to characterize their generalization properties*, arXiv:2010.07374v1, first public 2020-10-14. https://arxiv.org/abs/2010.07374
