# Short-factor uniqueness makes circular one-deletion shadows asymptotically run-exact

## Finding
Fix an alphabet \(\Sigma\) of \(q\ge2\) labeled symbols and a cyclic word \(w\in\Sigma^n\), with rotation but not reversal or symbol relabeling identified. Let \(\mathcal D_1(w)\) be the set of distinct length-\(n-1\) cyclic words obtained by deleting exactly one position. Let \(r_c(w)\) be the number of cyclic constant-symbol runs, with \(r_c(w)=1\) for a constant word. Say that \(w\) is \(\ell\)-unique if its \(n\) cyclic factors of length \(\ell\), indexed by starting position, are pairwise distinct.

**Deterministic theorem.** For every \(n\ge2\) and \(1\le\ell\le\lfloor n/2\rfloor\),
\[
 w\text{ is }\ell\text{-unique}\quad\Longrightarrow\quad
 |\mathcal D_1(w)|=r_c(w).
\]
In other words, different cyclic runs have different rotation-identified one-deletion descendants whenever every cyclic \(\ell\)-factor is unique.

**Random-source theorem.** Sample \(W\) uniformly from indexed \(q\)-ary words of length \(n\), and put \(D_n=|\mathcal D_1(W)|\). Let \(R_n\) be the number of cyclic edges \((i,i+1)\) at which the letters differ, and let \(R_n^*=\max(1,R_n)\). For every \(\ell\le\lfloor n/2\rfloor\),
\[
 \Pr(D_n\ne R_n^*)\le\binom n2q^{-\ell},\qquad
 d_{\rm TV}(\mathcal L(D_n),\mathcal L(R_n^*))\le\binom n2q^{-\ell}.
\]
The exact probability generating polynomial of \(R_n^*\) is
\[
 \mathbb E[z^{R_n^*}]
 =\frac{(1+(q-1)z)^n+(q-1)(1-z)^n}{q^n}
 +q^{1-n}(z-1).
\]
For fixed \(q\), taking \(\ell=\lceil 5\log_q n\rceil\) at all sufficiently large \(n\) makes the right-hand probability at most \(1/(2n^3)\). Consequently, writing \(p=(q-1)/q\),
\[
 \mathbb E D_n=np+O_q(n^{-2}),\qquad
 \operatorname{Var}(D_n)=np(1-p)+O_q(n^{-1}),\qquad
 \frac{D_n-np}{\sqrt{np(1-p)}}\ \Longrightarrow\ \mathcal N(0,1).
\]
These statements concern the *number of distinct output necklaces*, not their probability masses under uniform-position deletion.

## Assumptions and scope
All source positions are indexed before quotienting by rotation. A cyclic length-\(\ell\) factor starting at \(i\) includes positions \(i,i+1,\ldots,i+\ell-1\pmod n\). A cyclic run is a maximal nonempty arc of equal symbols, with all positions in a constant circle comprising a single run. The empty output at \(n=1\) is not needed. For \(n\ge2\), deletions from any positions in the same cyclic run give the same cyclic output. The alphabet remains fixed while \(n\to\infty\) in the asymptotic assertions.

## Proof
**1. Synchronization by a shared surviving factor.** Let \(w\) be \(\ell\)-unique, \(2\ell\le n\), and assume deletion at positions \(i\) and \(j\) produces the same necklace. Choose a rotation identifying the two length-\(n-1\) outputs, calling it \(y\). Every cyclic length-\(\ell\) factor of \(w\) that does not contain a deleted position survives unchanged as a length-\(\ell\) factor of that output. At most \(\ell\) of the \(n\) original factor starts contain the deleted position, so at least \(n-\ell\) of the \(n-1\) factor starts of \(y\) are *intact* in each deletion presentation. The intact-start sets in \(y\) therefore intersect in at least \(n-2\ell+1\ge1\) positions. Choose a common intact start. The length-\(\ell\) block there comes from original start \(s_i\) in the first presentation and original start \(s_j\) in the second. Because the \(\ell\)-factors of \(w\) are distinct, \(s_i=s_j\pmod n\).

Cut the original cyclic word immediately before this shared start. In both deletion presentations the same surviving length-\(\ell\) factor begins the linearly rooted output, and the same cyclic rotation of the source is used. Therefore the two *linear* one-deletion words are identical, without any remaining rotation. For a fixed linear word, deletion at two different positions gives the same resulting linear word if and only if every letter in the interval between those positions is equal: comparing the two outputs position by position gives \(w_i=w_{i+1}=\cdots=w_j\) after ordering the indices along the cut. Thus the two deleted positions belong to the same cyclic constant-symbol run. Different cyclic runs cannot collide. Since every run contributes exactly one output, \(|\mathcal D_1(w)|=r_c(w)\). The constant case follows directly.

**2. A birthday bound for distinct cyclic factors.** Fix distinct cyclic starts \(a,b\) and let \(d=b-a\pmod n\). The event that the length-\(\ell\) factors coincide imposes the \(\ell\) equalities \(W_{a+t}=W_{a+d+t}\) for \(0\le t<\ell\), with subscripts modulo \(n\). Represent these constraints by undirected edges \(x\leftrightarrow x+d\) on the \(n\) source positions, one edge for each \(x\in\{a,\ldots,a+\ell-1\}\). In the full \(d\)-shift graph every component is a cycle whose vertices form a residue class modulo \(g=\gcd(n,d)\). A constraint-edge cycle would require all \(n/g\) vertices of such a component to lie among \(\ell\) consecutive starts. But these vertices are spaced \(g\) apart, and any cyclic interval containing all of them has at least \(n-g+1>n/2\) consecutive positions because \(g\le n/2\). This is impossible for \(\ell\le n/2\). The constraint graph is a forest with exactly \(\ell\) edges. Independence of the \(n\) uniform letters therefore gives probability exactly \(q^{-\ell}\) for this factor equality. The union bound over \(\binom n2\) start pairs shows that \(W\) fails \(\ell\)-uniqueness with probability at most \(\binom n2 q^{-\ell}\). Applying step 1 proves the coupling and total variation bounds.

**3. The exact run law.** For \(r=0\) there are exactly \(q\) constant indexed words. For \(r\ge1\), choosing the \(r\) edges where the symbol changes and assigning symbols to the resulting \(r\) cyclic runs is equivalent to properly coloring a cycle of \(r\) vertices with \(q\) symbols. Its chromatic polynomial is \((q-1)^r+(q-1)(-1)^r\), including the zero value for \(r=1\). Thus the number of indexed sources having exactly \(r\) unequal cyclic edges is
\[
 \binom nr\big((q-1)^r+(q-1)(-1)^r\big).
\]
Summing with the constant-word term yields the stated polynomial, with \(q^{1-n}(z-1)\) moving the atom of \(R_n=0\) to \(R_n^*=1\).

**4. Moments and Gaussian law.** The \(n\) cyclic change indicators have mean \(p\) and, for \(n\ge3\), are pairwise independent: two distinct edges of a cycle form a forest, and uniform independent vertex labels give independent nonzero-difference events on forest edges. Consequently \(\mathbb E R_n=np\) and \(\operatorname{Var}(R_n)=np(1-p)\). The first \(n-1\) change indicators, lying on a path, are mutually independent Bernoulli\((p)\); the cyclic sum differs from their sum by at most one. The classical binomial central limit theorem therefore gives a standard normal limit for \(R_n\) and \(R_n^*\). For fixed \(q\) and sufficiently large \(n\), \(\ell=\lceil5\log_q n\rceil\le n/2\) and the exceptional coupling probability is at most \(1/(2n^3)\). Since \(1\le D_n,R_n^*\le n\), the differences of their first and second moments are \(O_q(n^{-2})\) and \(O_q(n^{-1})\), respectively; the variance comparison follows after accounting for the mean, and the total-variation approximation transfers the central limit theorem. \(\square\)

## Verification
Run the self-contained Python 3 file `verify.py` in the same directory. It constructs all rotation-identified one-deletion outputs literally, tests every eligible distinct-factor implication for all binary words through length 14, ternary words through length 8 and quaternary words through length 6, checks the exact cyclic transition polynomial at these lengths, and independently enumerates the pairwise factor-equality probabilities through length 8. All tests return `VERIFY_OK`. The finite enumeration corroborates, but does not replace, the all-length arguments.

## Relationship to prior work
Classical linear deletion-channel theory gives exactly the ordinary number of runs as the one-deletion descendant count (Sloane, 2002, Section 5); Liron and Langberg (2012, Sections I–II) study linear descendants and run-extremal words. Published work on the largest circular one-deletion shadow addresses the sharp *maximum*, and its arbitrary necklace examples can exhibit collisions between different cyclic runs. A separately established de Bruijn-cycle result gives run-exact deletion shadows for that highly structured source class through unique fixed factors. The present theorem instead supplies a general **short-factor uniqueness criterion for every source**, plus a full explicit random-source output-count comparison in total variation for every fixed alphabet. The linear-word statements, circular maximum, and special de Bruijn source do not imply the random cyclic law without a separate synchronization argument. Circular trace reconstruction literature concerns recovering an unknown source from random deletion traces, not this support-count distribution of exactly one deletion.

## Limitations
The source is sampled uniformly over indexed words and then interpreted cyclically; this is not a uniform distribution over necklaces (whose orbit sizes differ), although periodic sources have exponentially small mass under the indexed model. Deletion positions can have different probabilities of producing a particular distinct output. The bound is conservative and asymptotic once a logarithmic factor length fits within half the circumference; it does not give a sharp finite-length collision probability, an exact finite-length shadow-size histogram, or multi-deletion laws. Earlier non-indexed work on cyclic deletion posets or unique-factor synchronization may contain equivalent statements; priority remains subject to independent review.

## References
1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, first public arXiv version 2002-07-22, https://arxiv.org/html/math/0207197v1, especially Section 5.
2. Y. Liron and M. Langberg, *A characterization of the number of subsequences obtained via the deletion channel*, first public arXiv version 2012-02-08, https://arxiv.org/html/1202.1644v1, Sections I–II.
3. *Sharp one-deletion outdegree of binary necklaces*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-one-deletion-outdegree-of-binary-necklaces--2341722fce11/RESULT.md; compares an extremal circular support question.
4. A. Burudgunte, P. Valiant and H. Wang, *New Bounds for Circular Trace Reconstruction*, first public arXiv version 2025-12-02, https://arxiv.org/html/2512.02412v1, Sections 1–2.
