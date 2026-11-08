# Poisson critical window for distinctive representation in random approval elections

## Finding

Let \(n\ge k\ge2\) and \(m\ge k\) be integers. Independently for each voter and candidate, draw an approval with probability \(p\in(0,1)\). A committee \(W\) of \(k\) candidates has **distinctive representation (DR)** when it satisfies justified representation (JR) and each elected candidate has exactly \(q=\lceil n/k\rceil\) approving voters, as in [1]. Write \(T\) for the number of DR committees and \(Z\) for the number of candidates with exactly \(q\) approvals. Set

\[
b=\binom nq p^q(1-p)^{n-q},\qquad
\tau=\Pr\{\operatorname{Bin}(n-q,p)\ge q\},
\]

where \(\tau=0\) if \(q>n-q\). **The finite coupling inequality** is

\[
Z\sim\operatorname{Bin}(m,b),\qquad
\Pr\!\left\{T\ne\binom Zk\right\}\le m(m-1)b\tau.
\tag{1}
\]

In particular, except on the explicitly bounded exceptional event, *every* size-\(k\) selection from the exactly-quota candidates is a DR committee. Thus on this event the seemingly difficult DR existence, construction, and counting tasks reduce to checking column sums.

For the following limiting law, fix \(k\ge2\), let \(n\to\infty\), and assume

\[
\frac{m_n}{\sqrt n}\longrightarrow c\in[0,\infty),\qquad
p_n=\frac1k+\frac\beta{\sqrt n}+o(n^{-1/2}),
\qquad \beta\in\mathbb R.
\]

Define

\[
\mu=\frac{ck}{\sqrt{2\pi(k-1)}}
\exp\!\left(-\frac{k^2\beta^2}{2(k-1)}\right).
\]

If \(P_\mu\sim\operatorname{Poisson}(\mu)\), then the **entire number-of-DR-committees law** converges:

\[
\boxed{\quad T\ \xrightarrow{d}\ \binom{P_\mu}{k},\qquad
\Pr(T>0)\longrightarrow1-e^{-\mu}\sum_{j=0}^{k-1}\frac{\mu^j}{j!}.\quad}
\tag{2}
\]

The convergence concerns the finite integer-valued count, not only its mean. The convention is \(\binom jk=0\) when \(j<k\). In the same \(p_n=1/k+O(n^{-1/2})\) window, if \(m_n\) grows polynomially and \(m_n/\sqrt n\to\infty\), DR exists with probability tending to one, whereas \(m_n/\sqrt n\to0\) implies nonexistence with probability tending to one. For any fixed \(p\in(0,1)\setminus\{1/k\}\) and polynomially many candidates, DR is absent with probability tending to one.

## Assumptions and scope

The approval entries are mutually independent, with common approval probability; \(k\) is fixed only in the limiting results, while (1) holds for every finite \(n\ge k\ge2\), \(m\ge k\), and \(p\in(0,1)\). An election's JR condition uses the Hare quota: each group of at least \(n/k\) voters who all approve a common candidate must contain at least one voter approving some member of \(W\). No candidate-support nesting, impartial-culture ranking model, or voter normalization is assumed. The number of candidates is permitted to grow with \(n\). Finite formulas require no integrality assumption on \(n/k\).

## Proof

**Step 1: an exact uncovered-voter test.** For candidate \(c\), let \(S_c\subseteq[n]\) be its supporter set. For a committee \(W\), let \(U(W)=[n]\setminus\bigcup_{c\in W}S_c\). The definition of JR is equivalent to

\[
W\text{ satisfies JR}\quad\Longleftrightarrow\quad
|U(W)\cap S_d|<q\ \text{for every candidate }d.
\tag{3}
\]

Indeed, if the right side fails, any \(q\) voters in \(U(W)\cap S_d\) form an unrepresented cohesive group. Conversely, a cohesive group without any represented voter is contained in \(U(W)\), and its shared approved candidate \(d\) witnesses the failure of the right side.

**Step 2: a pairwise obstruction is the only possible exceptional cause.** Call a candidate *quota-sized* when \(|S_c|=q\). Let \(E\) denote the event that no ordered distinct pair \((c,d)\) satisfies

\[
|S_c|=q\quad\text{and}\quad |S_d\setminus S_c|\ge q.
\tag{4}
\]

On \(E\), choose any \(k\) quota-sized candidates as \(W\). For every elected \(c\), \(U(W)\subseteq[n]\setminus S_c\). Hence \(|S_d\cap U(W)|\le|S_d\setminus S_c|<q\) for all \(d\ne c\), while the inequality for \(d=c\) is automatic. By (3), \(W\) is JR. The DR definition also forces every selected candidate to be quota-sized, so on \(E\) the DR committees are **exactly** the \(k\)-subsets of those \(Z\) candidates. This proves the asserted identity on \(E\).

Each approval column is an independent \(n\)-trial Bernoulli vector, whence \(Z\sim\operatorname{Bin}(m,b)\). For distinct \(c,d\), conditional on \(|S_c|=q\), the number \(|S_d\setminus S_c|\) is \(\operatorname{Bin}(n-q,p)\), independently of the particular support of \(c\). Thus each ordered obstruction (4) has probability \(b\tau\). A union bound over \(m(m-1)\) pairs gives (1). It also proves a coupling in total variation between the laws of \(T\) and \(\binom Zk\), with the same error bound.

**Step 3: critical probability and the vanishing JR obstruction.** Put \(p_0=1/k\) and \(\sigma^2=p_0(1-p_0)=(k-1)/k^2\). Since \(q=np_0+O(1)\), the local binomial central limit theorem for the stated \(p_n\) yields

\[
\sqrt n\,b_n\longrightarrow
\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{\beta^2}{2\sigma^2}\right).
\tag{5}
\]

Furthermore,

\[
\frac{q-(n-q)p_n}{n}\longrightarrow\frac1{k^2}>0.
\]

Hoeffding's inequality, or the equivalent binomial Chernoff inequality, therefore gives \(\tau_n\le e^{-a_kn}\) for a constant \(a_k>0\) once \(n\) is sufficiently large. This statement also covers the case where the tail is identically zero. Consequently, for polynomial \(m_n\), the right side of (1) is \(o(1)\).

**Step 4: Poisson limit and the two off-critical regimes.** When \(m_n/\sqrt n\to c\), (5) gives \(m_nb_n\to\mu\) and \(b_n\to0\). The binomial rare-event limit yields \(Z_n\Rightarrow P_\mu\), and (1) transfers the complete discrete law of \(\binom{Z_n}k\) to \(T_n\), proving (2). When \(m_n/\sqrt n\to\infty\) at polynomial scale, \(m_nb_n\to\infty\) and \(\Pr(Z_n\ge k)\to1\); (1) transfers this to DR existence. When \(m_n/\sqrt n\to0\), Markov's inequality yields \(\Pr(Z_n\ge k)\to0\). Finally, for fixed \(p\ne1/k\), standard binomial large-deviation bounds give \(b_n\le e^{-a n}\) for some \(a>0\); therefore polynomial \(m_n\) has no quota-sized candidates with high probability. This establishes all regimes.

## Verification

The standalone `checker.py` implements both the compact JR criterion (3) and a separate literal enumeration of cohesive voter groups. It exhausts \(365{,}056\) labeled approval matrices over five parameter triples, confirms the finite coupling implication and bound, and independently checks the literal and compact definitions on \(4{,}608\) matrices. A separately weighted enumeration at approval probability \(1/3\) verifies an exact rational probability comparison. Local binomial masses are checked against (5) at increasing sample sizes, and numerical values of the limiting Poisson formula are checked for several fixed \(k\) and \(\beta\). These finite checks are corroboration only; the infinite-\(n\) result follows from the displayed analytic argument.

## Relationship to prior work

Chingoma, Grossi, Lindeboom, and Maly [1] introduced DR and proved the general decision problem NP-complete, motivating an analysis of its behavior on natural random election profiles. Their deterministic definitions, optimization results, and experiments do not provide the finite coupling (1) or full count law (2). Aziz and collaborators [2] introduced JR itself. Han, Tao, Xia, Zhang, and Zhou [3] analyzed the **different** axiom of average justified representation (AJR) in the Bernoulli approval model with fixed \(m\) and \(k\); their phase diagram does not imply this exact-quota DR result with growing \(m\). Existing deterministic characterizations of DR under laminar supporter sets do not apply to the typically crossing random supporter sets here; random SJR/SSJR results impose different axioms. The local binomial and Poisson approximations used in Step 3–4 are classical ingredients, not claimed as new probability theorems. The additional mathematical statement is the JR-validity coupling for all quota-selected committees and its complete DR-count phase transition.

## Limitations

The asymptotic theorem requires homogeneous independent approval entries and fixed committee size. It is not a worst-case algorithm for NP-complete DR and does not describe correlated-voter, growing-\(k\), or exponentially large candidate pools. The bound in (1) may be numerically loose for small electorates. The full-count limit is weak convergence, not convergence of every moment. Publication priority requires independent comparison against any unindexed or newly appearing equivalent random-election results; no such identity is asserted from a failed search alone. The scientific analysis has not received independent audit.

## References

[1] J. Chingoma, D. Grossi, F. Lindeboom, and J. Maly, *Diverse Representation in Approval-Based Committee Voting*, arXiv:2609.29332 (first posted 2026-09-24; inspected 2026-10-28 revision), https://arxiv.org/abs/2609.29332 and https://arxiv.org/html/2609.29332v2, especially Definition 25, Theorem 28, Sections 6–8, and Appendix D.

[2] H. Aziz, M. Brill, V. Conitzer, E. Elkind, R. Freeman, and T. Walsh, *Justified Representation in Approval-Based Committee Voting*, arXiv:1407.8269, https://arxiv.org/abs/1407.8269.

[3] Q. Han, B. Tao, L. Xia, C. Zhang, and H. Zhou, *Likelihood of the Existence of Average Justified Representation*, arXiv:2510.18718 (2025-10-21), https://arxiv.org/abs/2510.18718, notably Definition 2.1, Theorem 2.2 and the final discussion.
