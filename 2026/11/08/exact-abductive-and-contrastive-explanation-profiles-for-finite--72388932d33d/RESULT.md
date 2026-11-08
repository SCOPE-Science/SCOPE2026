# Exact abductive and contrastive explanation profiles for finite-trace persistence

## Finding

Fix an integer \(n\ge1\). Let \(w=w_0w_1\cdots w_{n-1}\in\{0,1\}^n\) be a finite trace of the single proposition \(p\). Consider the persistence formula
\[
\varphi=\mathsf G(p\rightarrow\mathsf X_{w}p),
\]
where \(\mathsf X_w\) is weak next and is true at the final time. Thus \(w\models\varphi\) exactly when \(w\) is nondecreasing, or equivalently \(w=0^a1^{n-a}\) for a unique \(0\le a\le n\).

A set of positions is an **abductive explanation** (AXp) when fixing those entries to their values in \(w\) forces the same compliance classification for every length-\(n\) completion and no proper subset does so. A set is a **contrastive explanation** (CXp) when allowing changes only at its positions permits a trace with the opposite classification, and no proper subset permits this.

**Violating traces.** If \(w\not\models\varphi\), the AXps are exactly the two-point sets
\[
\{i,j\}\quad(0\le i<j<n,\ w_i=1,\ w_j=0).
\]
For each cut \(0\le c\le n\), put
\[
D_c(w)=\{i<c:w_i=1\}\cup\{i\ge c:w_i=0\}.
\]
The CXps are exactly the sets \(D_c(w)\) with
\[
 c=0\text{ and }w_0=1,\quad
 c=n\text{ and }w_{n-1}=0,\quad\text{or}\quad
 0<c<n\text{ and }(w_{c-1},w_c)=(0,1).
\]
Writing \(\operatorname{inv}_{10}(w)\) for its number of ordered inverted pairs and \(d(w)\) for its number of adjacent descents \(10\), this gives
\[
\#\operatorname{AXp}(w)=\operatorname{inv}_{10}(w),\qquad
\#\operatorname{CXp}(w)=d(w)+1.
\]
For each integer \(1\le d\le\lfloor n/2\rfloor\), the exact number of **violating** binary words with \(d+1\) CXps is
\[
\boxed{\binom{n+1}{2d+1}}.
\]
Among violating words, the largest possible AXp count is \(\lfloor n^2/4\rfloor\), and the largest possible CXp count is \(\lfloor n/2\rfloor+1\). Both bounds are attained.

**Satisfying traces.** If \(w=0^a1^{n-a}\), then every case has exactly \(n-1\) CXps. For \(0<a<n\), they are the singleton positions \(\{i\}\) with \(i<a-1\) or \(i>a\), together with \(\{a-1,a\}\). Its two AXps consist of all positions except \(a-1\), and all positions except \(a\). For the constant zero word, the CXps are \(\{i\}\) for \(0\le i<n-1\), and the sole AXp fixes the first \(n-1\) positions. For the constant one word, the CXps are \(\{i\}\) for \(1\le i<n\), and the sole AXp fixes the last \(n-1\) positions. When \(n=1\), the single AXp is the empty set and there are no CXps.

There are \(2^n-n-1\) violating words. Across all length-\(n\) words the total number of AXps arising from violating words is
\[
\binom n2 2^{n-2}\quad(n\ge2).
\]
The total number of CXps arising from violating words is
\[
(2^n-n-1)+(n-1)2^{n-2}\quad(n\ge2).
\]

## Assumptions and scope

Trace length is fixed and positive. Only one proposition is present; its value at each position is independently changeable when unlocked. Explanations are inclusion-minimal sets of **time-indexed original literals**, equivalently subsets of positions, not necessarily minimum-cardinality sets and not explanations allowing inserted or deleted time steps. Both compliant and violating traces are covered by comparing completions with the trace's actual Boolean outcome. The weak-next convention is essential: a strong-next implication at the final time has a different satisfying language. The counting formulas concern words with their positions distinguished, not isomorphism types or a probability law on traces.

## Proof

**1. Temporal semantics.** Each nonfinal occurrence of \(p\) requires \(p\) at the next instant, so a word satisfies \(\varphi\) if and only if it contains no adjacent \(10\). The absence of \(10\) is equivalent to the existence of a cut \(c\) giving \(0^c1^{n-c}\).

**2. AXps of violating words.** Fix a set \(S\) of original bits. A nondecreasing completion exists if and only if no pair of fixed bits has the form \(1\) at an earlier position and \(0\) at a later position. Indeed, any such pair excludes every nondecreasing completion. Conversely, in the absence of such a pair, choose a cut after every fixed zero and before every fixed one; this is possible because all fixed zeros precede all fixed ones, and it gives a compatible nondecreasing word. Therefore \(S\) forces a violation exactly when it contains an inverted pair. Inclusion-minimal such \(S\) are precisely the displayed two-element inverted pairs.

**3. CXps of violating words.** Every satisfying alternative is \(u^{(c)}=0^c1^{n-c}\) for some cut \(c\). Its differing positions from \(w\) are exactly \(D_c(w)\). A set of unlocked positions admits some satisfying completion precisely if it contains some \(D_c(w)\). CXps are thus the inclusion-minimal members of this cut family. For \(c<e\), the only differing membership coordinates between \(D_c\) and \(D_e\) are the positions in \([c,e)\), and
\[
D_e\subseteq D_c\iff w_c=\cdots=w_{e-1}=0,\qquad
D_c\subseteq D_e\iff w_c=\cdots=w_{e-1}=1.
\]
Hence \(D_c\) is inclusion-minimal precisely when \(c=0\) or the preceding symbol is \(0\), **and** \(c=n\) or the following symbol is \(1\). This gives the three boundary/rise cases displayed in the finding. A binary word has
\[
\#(01)-\#(10)=w_{n-1}-w_0.
\]
It follows that \(1_{w_0=1}+\#(01)+1_{w_{n-1}=0}=1+\#(10)\), proving the CXp count formula for violating words.

**4. Compliant words.** For a nondecreasing word \(0^a1^{n-a}\), changing a single early zero with a later zero left fixed creates a \(10\), as does changing a single late one with an earlier one left fixed. At the unique boundary in a mixed word, flipping the two boundary bits from \(01\) to \(10\) is necessary and sufficient if no other position is altered. These are exactly the displayed singleton and boundary-pair CXps; other possible flips contain one of these sets. For the constant words, only the indicated singletons work. The AXps follow either by directly testing which original literals must be fixed to forbid every such intervention or by minimal hitting-set duality: the mixed-word CXp family consists of compulsory singleton positions and the pair \(\{a-1,a\}\), yielding exactly the two all-but-one AXps; constant words have one AXp made of all compulsory positions. For \(n=1\), every word satisfies, so locking no position suffices and no contrastive intervention exists.

**5. Spectrum and extrema.** Append \(0\) before \(w\) and \(1\) after it. If \(w\) has exactly \(d\) descents \(10\), this padded word has exactly \(d\) descents and \(d+1\) rises \(01\), hence \(2d+1\) alternating transition locations among its \(n+1\) successive gaps. Choosing those gaps uniquely determines \(w\), proving \(\binom{n+1}{2d+1}\). A violating word has \(d\ge1\), and \(d\le\lfloor n/2\rfloor\), with equality for an alternating word starting in \(1\). If a word has \(a\) ones and \(b\) zeros, then its inversion count is at most \(ab\le\lfloor n^2/4\rfloor\), with equality for \(1^a0^b\) at balanced \(a,b\). Finally each ordered pair of positions \(i<j\) is an inversion in exactly \(2^{n-2}\) of the \(2^n\) words, and each adjacent pair is a descent in exactly \(2^{n-2}\) words. Sum these indicators, using the count \(2^n-(n+1)\) of violating words, to obtain both aggregate identities.

## Verification

The accompanying standalone `checker.py` directly enumerates every subset of locked/unlocked positions and every binary completion, independently of the closed formulas, and compares the resulting minimal explanation families against the formulas above for every word of lengths \(1\) through \(8\) (\(510\) words in total). It separately verifies the exact descent-count distribution and the total number of violating words. Running `python checker.py` produces `ALL_CHECKS_OK`. This is a finite consistency check; the all-length result rests on the preceding mathematical proof.

## Relationship to prior work

Fionda, Ielo and Ricca (arXiv:2610.35169, first public date 2026-10-26) define locked-literal AXps and unlocked-literal CXps for finite-trace temporal logic and prove their hitting-set duality. Their Section on experiments exhibits \(2^N\) CXps for a conjunction of independently named weak-next response clauses. Those definitions and the duality are prior art. Their inspected discussion does not give the present single-proposition persistence classification, the inversion and descent formulas, or the exact binomial explanation-count spectrum. Reusing one proposition across successive time steps causes shared obligations rather than independent choice pairs; it collapses the number of CXps on **violating** traces from potentially exponential to at most linear.

A related earlier exact explanation theorem for a two-proposition until formula studies different time-indexed constraints and geometric joint distributions, so neither statement implies the other under a semantic identification. Classical combinatorics already counts binary words by transitions, and classical graph terminology describes minimal vertex covers; these are credited as components of the argument, not claimed as new. The claimed contribution is their complete, direct application to AXps/CXps of this specific temporal formula, including both outcome classes and the exact finite spectrum.

## Limitations

The formulas do not extend as stated to multiple independent propositions, arbitrary temporal formulas, strong next at the terminal position, or variable-length interventions. They make no general complexity claim for temporal explanation enumeration; they show a tractable structural family. The novelty comparison is limited to inspected available primary text and search results; a more general earlier result about minimal implicants or nested graph covers could subsume portions of the theorem.

## References

- V. Fionda, A. Ielo and F. Ricca, *Formal Explanations for Linear Temporal Logic over Finite Traces*, arXiv:2610.35169, version first submitted 2026-10-26, https://arxiv.org/abs/2610.35169.
- J. Ignatiev et al., *From Contrastive to Abductive Explanations and Back Again* (2020), cited in Fionda--Ielo--Ricca for general minimal hitting-set duality.
