# Uniform renewal enumeration of window-injective subsequence-universal words

## Finding

Fix integers \(q>d\ge 2\) and a labeled alphabet \(\Sigma\) of \(q\) letters. A word is **window-injective of radius \(d\)** when every \(d+1\) consecutive positions carry pairwise distinct letters; equivalently, equal letters are always separated by at least \(d+1\) positions. Let \(a_{q,d}(n,k)\) be the number of such words of length \(n\ge0\) whose full-alphabet scattered-subsequence universality index is exactly \(k\ge0\). Put \(r=q-d\), define \((q)_{\underline j}=q!/(q-j)!\), and set

\[
 B_r(z)=\frac{r!z^r}{\prod_{h=0}^{r-1}(1-hz)},\quad
 H_r(z)=\sum_{t=0}^{r-1}\frac{r!z^t}{(r-t)!\prod_{h=0}^{t}(1-hz)},\quad
 P_{r,d}(z)=\sum_{j=0}^{d-1}(rz)^j.
\]

The exact bivariate generating function, with \(z\) marking total length and \(u\) marking the universality index, is

\[
 \boxed{\sum_{n,k\ge0}a_{q,d}(n,k)z^nu^k
 =\sum_{j=0}^{d-1}(q)_{\underline j}z^j
 +(q)_{\underline d}z^d
 \frac{H_r(z)+uB_r(z)P_{r,d}(z)}{1-u(rz)^dB_r(z)}.}
\]

In particular, radius \(d=2\) and alphabet size \(q=4\) give the fully evaluated expression

\[
 \boxed{\sum_{n,k\ge0}a_{4,2}(n,k)z^nu^k
 =\frac{1+3z+8z^2+12z^3+16uz^4+16uz^5}{1-z-8uz^4}.}
\]

For each \(k\ge1\), the minimum possible length of a \(k\)-universal window-injective word is \(qk\), and the exact number achieving the minimum is

\[
 \boxed{a_{q,d}(qk,k)=q!\bigl(r^d r!\bigr)^{k-1}.}
\]

There is an exact rigidity transition. If \(r=1\), every admissible length-\(n\) word has index \(\lfloor n/q\rfloor\). If \(r\ge2\), the pair \((n,k)\) is attainable by an admissible word exactly when \(n\ge qk\).

For uniform random admissible words of length \(n\), write \(K_n\) for the index. With harmonic sums \(\mathsf H_r=\sum_{j=1}^r j^{-1}\) and \(\mathsf H_r^{(2)}=\sum_{j=1}^r j^{-2}\), put

\[
 \mu=d+r\mathsf H_r,\qquad \sigma^2=r^2\mathsf H_r^{(2)}-r\mathsf H_r.
\]

Under the natural infinite uniform extension process (each new symbol chosen uniformly among the \(r\) letters different from the previous \(d\)), we have \(K_n/n\to1/\mu\) almost surely. For \(r\ge2\),

\[
 \boxed{\frac{K_n-n/\mu}{\sqrt n}\ \Longrightarrow\
 \mathcal N\!\left(0,\frac{\sigma^2}{\mu^3}\right).}
\]

For \(r=1\), the index is deterministic as stated above and no nondegenerate Gaussian limit is claimed.

## Assumptions and scope

All counts use **labeled** letters and the full fixed alphabet \(\Sigma\), even for words omitting some letters. The empty word is included once with index zero. The radius applies to all pairs of positions at positive distance at most \(d\), not merely equal adjacent positions. The bounds are the strict integer constraints \(q>d\ge2\), \(n,k\ge0\). A scattered subsequence has increasing, not necessarily consecutive, positions. A word of index \(k\) contains all length-\(k\) words over \(\Sigma\) as subsequences but does not contain every length-\(k+1\) word.

For the random assertion, the law on admissible words of length \(n\ge d\) is uniform: there are \((q)_{\underline d}r^{n-d}\) words, since the first \(d\) positions are mutually distinct and each subsequent position has exactly \(r\) permitted colors. The probability statement concerns the stationary-rule infinite extension, not independent uniform letters.

## Proof

**1. The greedy-arch criterion.** Scan a word from left to right, closing an arch at the first occurrence of the last previously unseen alphabet letter, then resetting the set of seen letters. Let \(m\) arches close, followed by a remainder missing at least one letter. Taking the \(j\)-th desired subsequence symbol from the \(j\)-th arch proves \(m\)-universality. Conversely, if \(c_j\) is the unique finishing letter of arch \(j\) (unseen earlier in that arch) and \(a\) is absent from the remainder, \(c_1c_2\cdots c_ma\) is not a subsequence: the first \(c_j\) obtainable after the previous finishing letter is the end of arch \(j\). Hence the index is exactly the number of completed greedy arches, including when \(m=0\).

**2. A scalar state after the first \(d\) positions of each arch.** If a scan restarts after a completed arch, the previous \(d\) letters are distinct but are *unseen* for the new arch. For each of the next \(d\) positions, none of the already seen letters of the new arch can be chosen: each remains within the last \(d\) positions. Exactly \(r\) allowed letters are available at every such step, and all these choices add a new letter. After these \(d\) positions, the last \(d\) letters all belong to the new arch. The same condition holds in the first arch after its initial \(d\) mutually distinct positions.

If the current arch has \(s\) distinct seen letters with \(d\le s<q\), then precisely \(s-d\) of the \(r\) permitted next letters are already seen and precisely \(q-s\) are new. Thus a repeat leaves \(s\) unchanged, while a new letter changes \(s\) to \(s+1\) (or completes the arch if \(s+1=q\)). These counts are independent of the identities and order of earlier letters.

**3. Exact generating function.** Starting in state \(s=d\), a residence at state \(s=d+t\), followed by the next new letter, has length enumerator \((r-t)z/(1-tz)\). Consequently the enumerator of complete arches after the first \(d\) new letters is \(B_r(z)\), and the enumerator of all partial suffixes with no completion is \(H_r(z)\). Both statements follow by multiplying the geometric series for repeat steps at successive seen-cardinality states.

Let \(G(z,u)\) enumerate continuations starting at the state where the current incomplete arch has exactly \(d\) seen letters and the last \(d\) positions are those letters. A continuation either remains incomplete, contributing \(H_r(z)\), or completes this arch, contributing \(uB_r(z)\), then makes \(j<d\) forced-new steps and stops (\(r^jz^j\) possibilities), or makes all \(d\) forced-new steps and continues in state \(G\) (\((rz)^dG\) possibilities). Therefore

\[
 G=H_r+uB_r\bigl(P_{r,d}+(rz)^dG\bigr),\qquad
 G=\frac{H_r+uB_rP_{r,d}}{1-u(rz)^dB_r}.
\]

Before the first such state, an admissible word either ends at length \(j<d\), contributing \((q)_{\underline j}z^j\), or has \(d\) pairwise distinct initial letters, contributing \((q)_{\underline d}z^dG\). This proves the displayed generating function as an identity of formal power series. Direct simplification at \((q,d)=(4,2)\) gives the stated rational example.

**4. Minimum length, multiplicity, and attainability.** Each of the \(q\) distinct letters must occur at least \(k\) times in a \(k\)-universal word; thus its length is at least \(qk\). Equality forces the word to be a concatenation of \(k\) permutations of the alphabet, one per greedy arch, and such concatenations are \(k\)-universal. The first permutation has \(q!\) choices. After any complete permutation, for each of the first \(d\) positions of the next permutation exactly \(r\) possibilities avoid the preceding \(d\) letters; all are distinct within the next permutation. Its remaining \(r\) letters can then be ordered in \(r!\) ways. This gives \(q!(r^dr!)^{k-1}\) and constructs every boundary case.

For \(r=1\), every new letter is forced once \(d=q-1\) earlier letters are given; all admissible words repeat a permutation cyclically and each arch has length \(q\). For \(r\ge2\), after any \(k\) complete permutation arches, append \(t=n-qk\) letters without completing a further arch. When \(t\le d\), choose \(t\) distinct new letters. When \(t\ge d+1\), introduce \(d+1\le q-1\) distinct letters, then cycle among those \(d+1\) letters in their existing order. Every window of length \(d+1\) remains injective, and the incomplete arch never sees all \(q\) letters. The same construction from an empty starting word proves the \(k=0\) case.

**5. Renewal limit.** Under uniform admissible random sampling, after the initial \(d\) distinct letters there are always \(r\) equiprobable permitted choices. At seen-cardinality \(s=d+t\), the probability of discovering a new letter is \((r-t)/r\). The waiting time before each next new letter is therefore geometric on \(\{1,2,\ldots\}\); conditional on any previous history its parameter depends only on \(t\), so successive waiting times and successive inter-arch lengths are independent. Every completed arch is followed by \(d\) forced-new steps. The inter-completion length \(L\), including these steps, has the law

\[
 L\ \overset{\mathrm d}{=}\ d+\sum_{j=1}^r G_j,
 \qquad \Pr(G_j=t)=\left(1-\frac{j}{r}\right)^{t-1}\frac{j}{r}
 \quad (t\ge1),
\]

where the \(G_j\) are independent. This also holds for the initial arch. Hence \(\mathbb E L=d+r\mathsf H_r=\mu\) and \(\operatorname{Var}L=r^2\mathsf H_r^{(2)}-r\mathsf H_r=\sigma^2\). The number of completed arches before position \(n\) is precisely the renewal count. The ordinary renewal strong law and renewal central limit theorem imply the two stated limits. For \(r=1\), \(L=q\) almost surely and the index is deterministic.

## Verification

Run `python3 verify.py` with standard-library Python. The script computes the displayed rational series by exact integral formal-power-series operations, compares it coefficientwise against a separate weighted-state dynamic program for every \(3\le q\le8\), \(2\le d<q\), through length \(32\), and compares seven parameter pairs against literal enumeration of admissible labeled words. It also checks all minimum-length coefficients in that finite range, rigidity when \(q=d+1\), and the \((4,2)\) denominator identity through length \(60\). The successful run reported:

`VERIFY_OK q=3..8 d=2..q-1 n<=32 finite_cells=1732 literal_instances=44223 quaternary_identity_n<=60`

These finite calculations check the algebra and boundary cases; they do not replace the all-parameter proof above. No external proof assistant or independent review is claimed.

## Relationship to prior work

Barker et al. (2020) introduced/scoped scattered-factor universality and supplied the greedy arch criterion. Adamson (2023) gave unrestricted word-counting algorithms, and Adamson et al. (2023) gave general counting algorithms for regular-language restrictions. The present result extracts a uniform closed form for the whole nontrivial radius range \(2\le d<q\) and an explicit independent-renewal law. Generic fixed-automaton algorithms do not themselves state this evaluated two-parameter generating function, the minimum-word counts, or the Gaussian limit. The radius-one adjacency-distinct subfamily has separately been enumerated; the present claims are restricted to radius at least two and are not deductions of the radius-one distribution. A yet-unidentified equivalent enumeration or dependent coupon-collector treatment remains possible.

## Limitations

The restriction is over a labeled finite alphabet, with complete windows of length \(d+1\); no claims are made for arbitrary graph coloring constraints, variable alphabet size growing with \(n\), or nonuniform random transitions. The Gaussian law requires fixed \(q,d\), \(r\ge2\); no uniform rate of convergence or finite-size error bound is asserted. The originality comparison is based on inspected identified sources, not on a proof that no equivalent publication exists. Independent scientific validation has not been performed.

## References

- L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1 (first posted 2020-03-10), https://arxiv.org/html/2003.04629v1.
- D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1 (first posted 2023-04-10), https://arxiv.org/html/2304.04583v1.
- D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1 (first posted 2023-11-17), https://arxiv.org/html/2311.10658v1.
