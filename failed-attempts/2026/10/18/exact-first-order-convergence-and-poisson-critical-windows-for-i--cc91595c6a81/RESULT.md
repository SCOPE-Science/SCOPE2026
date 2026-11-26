# Exact first-order convergence and Poisson critical windows for independently colored equal-block equivalence relations

## Finding

For each integer \(n\geq 1\), let \(k_n,m_n\) be positive integers with \(k_n\to\infty\) and \(m_n\to\infty\). Form a finite structure \(A_n\) in the vocabulary consisting of equality, an equivalence relation \(E\), and a unary predicate \(P\). Its \(E\)-classes are exactly \(k_n\) labelled blocks, each with \(m_n\) vertices. Independently for every vertex, place it in \(P\) with probability \(1/2\); leave \(E\) deterministic. Define for each fixed integer \(r\geq0\)

\[
\lambda_{n,r}= k_n 2^{-m_n}\binom{m_n}{r},
\]

with the convention that the binomial coefficient vanishes when \(r>m_n\).

The motivating 2025 convergence-law study of random expansions of linear preorders [2] identifies a sufficient superlogarithmic-growth regime, leaving the exact phase boundary for unordered equal-block relations and their rare unary-color defects to be determined.

**Convergence theorem.** The probability of **every** first-order sentence in this vocabulary converges as \(n\to\infty\) if and only if \(\lambda_{n,r}\) converges in the extended half-line \([0,\infty]\) for **every** fixed \(r\geq0\).

**Zero-one criterion.** Under these equivalent convergence conditions, all sentence probabilities tend to either zero or one if and only if each extended limit lies in \(\{0,\infty\}\).

**Complete critical-window trichotomy.** There can be at most one \(r\) with \(\lambda_{n,r}\to\lambda\in(0,\infty)\). If such \(r\) exists, then \(\lambda_{n,s}\to0\) for every fixed \(s<r\) and \(\lambda_{n,s}\to\infty\) for every fixed \(s>r\). The counts of blocks containing exactly \(r\) positive vertices and exactly \(r\) negative vertices jointly converge to two independent Poisson random variables with mean \(\lambda\). All limiting first-order probabilities are finite expressions in their (finitely truncated) joint distribution. Every index \(r\geq0\) and every \(\lambda\in(0,\infty)\) is realized by an explicit sequence.

In particular, the first critical window is the sharp threshold for the sentence saying no equivalence class is monochromatic: if \(k_n2^{-m_n}\to\lambda\in(0,\infty)\), then its probability tends to \(e^{-2\lambda}\).

## Assumptions and scope

The signature is exactly \(\{E,P\}\) with equality. The relation \(E\) is reflexive, symmetric and transitive. Both the number of its classes and their common size diverge; no ordering, class names, numerical counting predicates, or additional random relation is available to formulas. Each unary color is an independent fair Bernoulli choice. Sentences are ordinary first-order sentences of arbitrary but fixed finite quantifier rank. The limit is along the prescribed integer index \(n\), with no unmentioned growth-rate assumptions.

For a structure \(A\) and integer \(q\geq1\), call the **\(q\)-class type** of a class containing \(a\) positive and \(b\) negative vertices the pair \((\min(a,q),\min(b,q))\). Its **\(q\)-profile** counts the number of classes of each type, truncating each count at \(q\). The profile is finite-valued, depending only on \(q\).

## Proof

**1. Uniform finite-rank invariance.** Two finite colored equivalence structures with identical \(q\)-profiles satisfy the same first-order sentences of quantifier rank at most \(q\). This follows from an explicit \(q\)-round Ehrenfeucht–Fraïssé strategy. Duplicator maintains a partial isomorphism between the selected elements and a matching between their represented equivalence classes. When Spoiler enters a previously unused class, Duplicator selects an unused class of the same \(q\)-type. If its multiplicity is below \(q\), exact equality of multiplicities supplies the choice; if it is at least \(q\), fewer than \(q\) classes can have been consumed, so a fresh one remains. When Spoiler selects a further vertex in an already matched class, its color is matched in the partner class. For a color multiplicity smaller than \(q\), the available numbers agree exactly, while if it is at least \(q\), fewer than \(q\) distinct vertices have been played. Equality, equivalence, and color are therefore all preserved. This argument covers repeated element choices and classes containing zero elements of either color. Hence every rank-\(q\) sentence is constant on each \(q\)-profile.

**2. Distribution of finite-rank profiles.** Fix \(q\). Eventually \(m_n>2q\). Consequently the possible class types are exactly the \(2q\) exceptional types \((r,q)\) and \((q,r)\) for \(0\leq r<q\), together with the generic type \((q,q)\). A given exceptional type has probability

\[
p_{n,r}=2^{-m_n}\binom{m_n}{r}.
\]

Across distinct equivalence classes, the types are independent. The count of any exceptional type has binomial marginal distribution with \(k_n\) trials and expected value \(\lambda_{n,r}\). If this mean tends to zero, the count tends to zero in probability by Markov's inequality. If it tends to infinity, its variance is at most its mean, so its count tends to infinity in probability by Chebyshev's inequality. If it tends to a finite positive \(\lambda\), the count tends in law to \(\mathrm{Poisson}(\lambda)\): here \(p_{n,r}\to0\) because \(m_n\to\infty\), and the binomial probability-generating function converges. For several exceptional types with finite means, their joint generating function is

\[
\left(1+\sum_i p_{n,i}(z_i-1)\right)^{k_n}\longrightarrow
\exp\left(\sum_i\lambda_i(z_i-1)\right),
\]

so their limiting counts are independent Poisson variables. Types with diverging means have truncated count \(q\) with probability tending to one; types with vanishing means have truncated count zero. Finally, the generic class probability tends to one since all finitely many exceptional probabilities tend to zero. As \(k_n\to\infty\), its truncated count tends to \(q\) in probability. Hence if all the extended means converge, each finite \(q\)-profile converges in distribution. By Step 1, the probability of every rank-\(q\) sentence converges. This proves the sufficient direction of the convergence criterion.

**3. Necessity from defining rare classes.** For each fixed \(r\geq0\), ordinary first-order logic expresses the sentence \(\chi_r\) asserting that **some** equivalence class contains exactly \(r\) vertices satisfying \(P\): select a representative and \(r\) pairwise distinct positive vertices in that class and assert universally that these are all its positive vertices. At \(r=0\) assert that some class has no positive vertex. Consequently

\[
\mathbb{P}(A_n\models\chi_r)=1-(1-p_{n,r})^{k_n}.
\]

Since \(p_{n,r}\to0\), we have \(-\log(1-p_{n,r})/p_{n,r}\to1\). The displayed sentence probability therefore converges if and only if \(\lambda_{n,r}=k_np_{n,r}\) converges in \([0,\infty]\): indeed the map \(t\mapsto1-e^{-t}\) is a homeomorphism from the extended half-line onto \([0,1]\), and the logarithmic correction is asymptotically one (for sufficiently large \(n\)). Thus, if every sentence probability converges, every extended mean converges.

**4. Zero-one law and uniqueness of critical level.** If all the extended means converge to zero or infinity, the finite-profile limiting law in Step 2 is concentrated at a single profile for every \(q\). Therefore every sentence has a zero-or-one limiting probability. Conversely, if some mean tends to \(\lambda\in(0,\infty)\), the sentence \(\chi_r\) has limiting probability \(1-e^{-\lambda}\in(0,1)\).

For fixed \(s,r\geq0\), the exact ratio of the means, whenever its denominator is nonzero, is

\[
\frac{\lambda_{n,s}}{\lambda_{n,r}}=\frac{\binom{m_n}{s}}{\binom{m_n}{r}}.
\]

As \(m_n\to\infty\), this ratio tends to zero for \(s<r\), and to infinity for \(s>r\). Thus a finite positive limiting mean can occur at only one level, with the asserted behavior below and above it. For sufficiently large \(n\), the events 'exactly \(r\) positive vertices' and 'exactly \(r\) negative vertices' in a class are disjoint, and have equal probability \(p_{n,r}\). Their joint count generating function is

\[
\bigl(1+p_{n,r}(z-1)+p_{n,r}(w-1)\bigr)^{k_n},
\]

which tends to \(\exp(\lambda(z-1)+\lambda(w-1))\). Thus the two counts converge jointly to independent \(\mathrm{Poisson}(\lambda)\) variables. The finite-profile reduction from Steps 1–2 gives every sentence's limit by summing the event's indicator against finitely truncated Poisson weights. Explicitly, let \(m_n=n\) and

\[
k_n=\max\left(1,\left\lfloor\lambda\frac{2^n}{\binom{n}{r}}\right\rfloor\right).
\]

Then \(k_n\to\infty\) and \(\lambda_{n,r}\to\lambda\), proving attainability. At \(r=0\), monochromatic classes consist of two disjoint rare types with the same limiting mean \(\lambda\). The probability that both rare counts vanish tends to \(e^{-2\lambda}\). This completes the proof.

## Verification

A self-contained executable `check.py` constructs finite colored equivalence structures, independently plays the full two-sided Ehrenfeucht–Fraïssé game, and checks that matching truncated profiles imply winning Duplicator strategies on bounded samples. It also checks exact binomial class-event probabilities against their Poisson approximation with explicit numerical error bounds. The checker returned `COLORED_EQUIVALENCE_VERIFY_OK EF=246 probability=36`. The proof above, not finite enumeration or numerical convergence, establishes every unbounded assertion.

## Relationship to prior work

Koponen and Karlsson [2] give a zero-one law for suitably rapidly growing classes of **linear preorders** under broader expansion distributions, with class sizes faster than every logarithm and below some polynomial; that sufficient result does not state the present critical \(m_n\)-versus-\(k_n\) classification. Their full paper was not available for complete comparison. A later October 2026 source by Koponen [1], especially Example 2.12 and Remark 2.15, highlights base-structure conditions relevant to random expansions, while its main results concern finite model properties and closure-based limit theories, not this exact random equal-block criterion. Dawar, Grädel and Hoelzel [3] study random expansions of repeated products of a fixed finite structure, not the moving-size equivalence classes and rare colored blocks here. The Ehrenfeucht–Fraïssé game [4] and elementary binomial-to-Poisson asymptotics are established tools; the claimed contribution is their exact combination into a necessary-and-sufficient first-order convergence and zero-one criterion for this natural random expansion family.

## Limitations

This is a theorem for a single independently fair unary predicate, uniformly equal class sizes, and diverging numbers of classes **and** class sizes. It makes no claim about unequal block sizes, additional random relations, non-half color biases varying with \(n\), monadic second-order logic, or formulas with counting quantifiers. The novelty comparison is bounded by accessible literature, especially the unavailable full text of [2]; lack of a search hit does not prove priority. No independent scientific audit has been performed.

## References

[1] V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (first publicly posted 2026-10-12), https://arxiv.org/html/2610.16163v1.

[2] V. Koponen and E. Karlsson, *Convergence Laws for Expansions of Linear Preorders*, WoLLIC 2025, pp. 101–118, first online 2025-08-01, DOI:10.1007/978-3-031-99536-1_7, https://link.springer.com/chapter/10.1007/978-3-031-99536-1_7.

[3] A. Dawar, E. Grädel and M. Hoelzel, *Convergence and Nonconvergence Laws for Random Expansions of Product Structures* (2020), https://api.repository.cam.ac.uk/server/api/core/bitstreams/07815c3c-7f3e-4cdc-8e5e-afb88dd574e6/content.

[4] Standard Ehrenfeucht–Fraïssé game characterization of first-order quantifier rank.
