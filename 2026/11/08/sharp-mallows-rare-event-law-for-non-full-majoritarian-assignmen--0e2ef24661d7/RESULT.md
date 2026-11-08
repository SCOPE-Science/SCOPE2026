# Sharp Mallows rare-event law for non-full majoritarian assignment top cycles

## Finding
Let \(n\ge5\) agents rank the same \(n\) houses independently under Mallows–Kendall preferences with common reference order \((1,\ldots,n)\) and fixed dispersion \(0<q<1\). Write \(T_n\) for the majoritarian assignment top cycle, a subset of the \(n!\) deterministic house assignments. Then
\[
\Pr(|T_n|<n!)\sim C(q)\, n!\left(\frac{1-q}{1-q^n}\right)^nq^{n(n-1)/2},\qquad C(q)=\frac{3q^2+2q+1}{q(1+q)}.
\]
Equivalently, the right side is asymptotic to
\[
C(q)\sqrt{2\pi n}\left(\frac{n(1-q)}e\right)^nq^{n(n-1)/2}.
\]
In the impartial-culture case \(q=1\), where every ranking is uniform and independent, the corresponding sharp law is
\[
\Pr(|T_n|<n!)\sim3\,\frac{n!}{n^n}\sim3\sqrt{2\pi n}\,e^{-n}.
\]
The formula concerns non-full top cycles, not the probability of a popular or Pareto-optimal assignment. It is a distributional consequence of the deterministic structural top-cycle classification of Brandt–Chen–Dong–Lederer–Schlenga.

## Assumptions and scope
For \(n\) agents and \(n\) objects, an assignment is a bijection. Agent \(i\) has a strictly ordered list \(\pi_i\) of the objects. Assignments are compared by the number of agents weakly preferring one to the other; the top cycle is the maximal set under the transitive closure of this weak majority relation, as in the cited paper. Independently for each agent, \(\Pr(\pi_i=\pi)=q^{\operatorname{inv}(\pi)}/Z_n(q)\), where \(Z_n(q)=\prod_{j=1}^n(1-q^j)/(1-q)\) for \(q\ne1\) and \(Z_n(1)=n!\). The order \((1,2,\ldots,n)\) is common. In the asymptotic statement, \(q\) stays fixed as \(n\to\infty\), so it does not cover a moving transition \(q=q_n\).

Set \(A_n(q)=n!((1-q)/(1-q^n))^nq^{n(n-1)/2}\). Define \(F_{\rm top}\) as the union of: all agents having distinct first-ranked objects; and exactly one pair of agents sharing a first-ranked object \(c\), with all other first choices different, while both members of the pair rank the unique unchosen object \(h\) second. Define \(F_{\rm bottom}\) analogously using last and second-to-last ranked objects. Theorem 2 of the cited majoritarian-assignment paper establishes, for \(n\ge5\),
\[
\{|T_n|<n!\}=F_{\rm top}\cup F_{\rm bottom}.
\]
This equivalence is *prior work*, not a new lemma claimed here.

## Proof
**Mallows first and second draws.** Under the stated distribution, the first ranked object is \(c\) with probability \(p_c=a_n q^{c-1}\), where \(a_n=(1-q)/(1-q^n)\). Conditional on this first draw, the next object \(h\ne c\) has probability \(b_nq^{h-1-\mathbf1_{h>c}}\), with \(b_n=(1-q)/(1-q^{n-1})\). This follows directly by factoring inversion weights of the selected element and the remaining permutation. The same sequential sampling rule applies after any fixed number of initial positions.

**Exact exceptional top-event probabilities.** By independence, the probability of distinct top-ranked objects is
\[
\Pr(\text{distinct tops})=\sum_{\sigma\in S_n}\prod_{i=1}^np_{\sigma(i)}=A_n(q).
\]
For the second top-event, choose the colliding pair of agents and a duplicated object \(c\) and the missing object \(h\). The remaining \(n-2\) agents' first choices biject onto the other objects. Multiplying the conditional second-choice probabilities for the pair gives
\[
E_n(q):=\Pr(F_{\rm top}\setminus\{\text{distinct tops}\})
=\frac{A_n(q)b_n^2}{2}
\sum_{\substack{1\le c,h\le n\\c\ne h}}
q^{c+h-2-2\mathbf1_{h>c}}.
\]
The factor \(1/2\) arises because the \(\binom n2(n-2)!\) placements, relative to the \(n!\) distinct-top placements, have ratio \(1/2\). Each summand uses the *actual second position*, rather than an independence approximation. For fixed \(0<q<1\), both finite geometric sums converge, and
\[
\frac{E_n(q)}{A_n(q)}\longrightarrow
\frac{(1-q)^2}{2}\cdot\frac{q^{-1}+q}{(1-q)(1-q^2)}
=\frac{1+q^2}{2q(1+q)}=:c(q).
\]
At \(q=1\), the exact limits are \(A_n(1)=n!/n^n\) and \(E_n(1)/A_n(1)=n/[2(n-1)]\).

**The bottom event and its intersection.** Reversing positions and simultaneously relabeling objects by \(j\mapsto n+1-j\) preserves the inversion count, hence preserves the joint distribution and exchanges \(F_{\rm top}\) and \(F_{\rm bottom}\). Consequently \(\Pr(F_{\rm bottom})=A_n+E_n\). It remains to show \(\Pr(F_{\rm top}\cap F_{\rm bottom})=o(A_n)\).

Condition on any elementary specification making \(F_{\rm top}\) true: the first-ranked object of each agent and, for the unique colliding pair if present, its second-ranked objects. The unexposed ranking suffixes are still independent Mallows sequential draws on the respective remaining ordered object sets. For every agent, at most two leading positions are fixed. For the last-ranked object to lie among the \(\lfloor n/2\rfloor\) smallest labels, its conditional probability is at most \(p_n^*=nq^{\lfloor n/2\rfloor-2}\): among at least \(n-2\) surviving labels, each of these small objects has at least \(\lfloor n/2\rfloor-2\) larger ones, so its final-position probability is at most the indicated geometric weight. Under \(F_{\rm bottom}\), all but at most one house appear as distinct bottom-ranked objects; thus at least \(k=\lfloor n/2\rfloor-1\) agents must have bottom choices in the smaller half. Conditional independence and a union bound give
\[
\Pr(F_{\rm bottom}\mid\text{elementary }F_{\rm top}\text{ specification})
\le 2^n\bigl(nq^{\lfloor n/2\rfloor-2}\bigr)^{\lfloor n/2\rfloor-1}
=\exp(-\Omega_q(n^2)).
\]
This uniform bound is valid for sufficiently large \(n\). Averaging the specifications proves \(\Pr(F_{\rm top}\cap F_{\rm bottom})=o(\Pr(F_{\rm top}))=o(A_n)\), since \(E_n/A_n\) has a finite limit for fixed positive \(q\). Thus inclusion-exclusion gives \(\Pr(|T_n|<n!)=2(A_n+E_n)(1+o(1))\), yielding \(2(1+c(q))=(3q^2+2q+1)/(q(1+q))\). Stirling's formula yields the equivalent expression.

At \(q=1\), condition instead on the same top-event specifications. Every unexposed suffix is uniform, with length at least \(n-2\). The probability of any particular set of distinct bottom labels for all but one agent is at most \((n-2)^{-n}\) up to a bounded factor, so a union bound over choices of the unchosen bottom label and colliding pair shows \(\Pr(F_{\rm bottom}\mid F_{\rm top})\le O(n^C)n!/n^n=o(1)\) for some fixed \(C\). Together with the exact uniform values of \(A_n\) and \(E_n\), this proves the factor \(3\).

## Verification
The included dependency-free Python file `checker.py` independently enumerates Mallows permutations and their ordered first/second selections using exact fractions. It matches both finite-event formulas in sixteen combinations of market sizes \(3\le n\le6\) and rational dispersions, including the uniform limit, and checks the limiting coefficient at three rational dispersions and the impartial-culture identities through \(n=15\). Enumeration at \(n<5\) checks the probabilistic identities, **not** the top-cycle classification (which is invoked only for \(n\ge5\)). The independent implementation is separate from the algebraic derivation, while the infinite asymptotic conclusion relies on the proof.

## Relationship to prior work
Brandt, Chen, Dong, Lederer and Schlenga, *Majoritarian Assignment Rules* (arXiv:2602.14816v1, February 16, 2026), Theorem 2 and Appendix B, give the deterministic top-cycle classification used as a premise; they do not derive these Mallows or impartial-culture rare-event probabilities or the sharp prefactors. He, Müller and Verstraaten, *Cycles in Mallows random permutations* (2023), Section 2, records Mallows normalization, geometric sampling, and reversal symmetry, but studies cycle counts of individual random permutations rather than the majority top cycle of assignments over independent agent rankings. The present contribution is the *joint extreme-ranking probability calculation and sharp probability law* for the distinct majoritarian top-cycle object; it is not a new deterministic classification of top cycles.

## Limitations
The result requires independent rankings with a common Mallows center and fixed dispersion \(q\in(0,1)\), or the separate uniform case. It does not treat the scaling window \(q\to1\), heterogeneous reference orders, correlated agents, other majority notions, or exact finite-\(n\) joint top/bottom event probabilities. The first- and second-choice formulas depend on strict rankings and equal numbers of agents and houses. The top-cycle classification is external prior mathematics. No claim of exhaustive priority over inaccessible or unindexed literature is made; independent scientific validation has not occurred.

## References
1. F. Brandt, H. Chen, C. Dong, P. Lederer, and A. Schlenga, *Majoritarian Assignment Rules*, arXiv:2602.14816v1, February 16, 2026, Theorem 2 and Appendix B. https://arxiv.org/pdf/2602.14816
2. J. He, T. Müller, and T. W. Verstraaten, *Cycles in Mallows random permutations*, Random Structures & Algorithms 63 (2023), 1054–1099, Section 2. https://doi.org/10.1002/rsa.21169
