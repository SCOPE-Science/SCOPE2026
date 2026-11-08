# Exact formula algebra and sharp depth two for reachability on Alexandrov stars

## Finding

For every integer \(m\geq1\), let \(X_m=\{r,\ell_1,\ldots,\ell_m\}\) carry the Alexandrov topology of the partial order \(r<\ell_i\), with distinct leaves incomparable. In the Boolean propositional language with \(k\geq0\) variables, Cantor-derivative modality \(d\), and the binary topological path-reachability modality \(\gamma\), identify formulas that have identical truth sets under every valuation on this **one fixed space** \(X_m\).

Set \(Q=2^k\) and
\[
N_{k,m}=Q\sum_{j=1}^{\min(m,Q)}\binom{Q}{j}(j+1).
\]
Then the number of equivalence classes of formulas is exactly \(2^{N_{k,m}}\). Every formula is equivalent on \(X_m\) to one of modal depth at most **two**, where each occurrence of \(d\) or \(\gamma\) adds one to the maximum modal depth of its arguments. When \(k\geq1\) and \(m\geq2\), this bound is sharp: some formulas have no equivalent of depth at most one.

As soon as \(m\geq Q\), the number stabilizes at
\[
2^{Q(2^Q-1+Q2^{Q-1})},
\]
and \(m=Q\) is the least uniform stabilization point when \(Q\geq2\). Examples: for \(k=0\), there are four classes for every \(m\geq1\); for \(k=1\), there are \(256\) classes when \(m=1\), and \(2^{14}=16384\) when \(m\geq2\). For \(k=2\) the exponents \(N_{2,m}\) for \(m=1,2,3\) and \(m\geq4\) are respectively \(32,104,168,188\).

## Assumptions and scope

Open subsets are upper sets in the indicated order. Atomic propositions have **arbitrary** truth subsets of \(X_m\); there is no persistence restriction. Boolean connectives are classical. For \(A\subseteq X_m\), define the Cantor derivative \(d(A)\) as the set of points whose every open neighborhood contains a point of \(A\) different from itself. Thus \(d(A)=\{r\}\) if \(A\) contains a leaf and \(d(A)=\varnothing\) otherwise.

For \(A,B\subseteq X_m\), \(x\in\gamma(A,B)\) means that a continuous \(\pi:[0,1]\to X_m\) exists with \(\pi(0)=x\), \(\pi((0,1))\subseteq A\), and \(\pi(1)\in B\). This is the path-reachability convention used by Gagarin and Fernández-Duque (2026). Write \(E(C)=\gamma(X_m,C)\). Since the space is path connected, \(E(C)\) equals \(X_m\) if \(C\neq\varnothing\) and equals the empty set otherwise. Put \(R=d(X_m)=\{r\}\) and \(L=X_m\setminus R\).

An atomic **type** is a truth assignment to the \(k\) variables, so there are \(Q\) types. For a valuation, let \(b\) be the type at the root and \(S\) the nonempty set of types realized by the leaves. At a pointed leaf also record its own type \(a\in S\); at the pointed root use a distinguished root symbol \(*\). Repetitions of a leaf type are deliberately discarded. The theorem concerns semantic equivalence on \(X_m\), not equivalence valid over all topological spaces.

## Proof

**1. Exact binary-reachability rule.** A continuous path in a finite Alexandrov space with all intermediate values in \(A\) can be replaced by a finite up-down comparability path whose interior vertices lie in \(A\) (Bezhanishvili et al., 2024, Lemma 3.6). Equivalently, it meets one comparability component \(C\) of the induced order on \(A\), with interior witnesses above both endpoints: \(x\leq a\) and \(y\leq a'\) for some \(a,a'\in C\), where \(y\in B\) is the endpoint. Conversely these witnesses and a comparability walk inside \(C\) concatenate into a continuous path, allowing endpoint jumps along the specialization order. For the rooted star this gives exactly
\[
\begin{aligned}
r\in\gamma(A,B)&\iff ((r\in B\ \land\ A\ne\varnothing)\ \lor\ (A\cap B\cap L\ne\varnothing)),\\
\ell\in\gamma(A,B)&\iff \ell\in A\ \land\ [\ell\in B\ \lor\ r\in B\ \lor\ (r\in A\ \land\ A\cap B\cap L\ne\varnothing)]
\end{aligned}
\]
for each leaf \(\ell\). To see the first line directly, the path through any chosen leaf in \(A\) can start and end at the root; a terminal leaf must itself be in \(A\). For the second, the singleton open neighborhood of \(\ell\) forces \(\ell\in A\). The path can end at the root, remain at \(\ell\), or travel from \(\ell\) through an \(A\)-root to an \(A\cap B\)-leaf. These are all possibilities.

In logical notation the rule also eliminates the general binary \(\gamma\) in favor of the global existence abbreviation \(E\), the root marker \(R=d\top\), and Boolean operations. The right-hand conditions depend only on root truth, local leaf truth, and existence of some leaf satisfying the indicated Boolean combination.

**2. Semantic support invariance.** We claim that the truth of every formula at a point is determined by its profile \((b,S,*)\) or \((b,S,a)\) above. This is immediate for atomic propositions and Boolean connectives. If the claim holds for \(\varphi\), then \(d\varphi\) is always false on leaves and is true at the root just when one of the types in \(S\) makes \(\varphi\) true at a leaf. For \(\gamma(\varphi,\psi)\), the two displayed path rules involve only the same profile information and the existence of a type in \(S\) satisfying both \(\varphi\) and \(\psi\). Induction therefore proves the claim, including for arbitrarily nested modalities. In particular no formula counts repetitions of an atomic type among the leaves.

**3. Every profile is definable at depth two.** For each atomic type \(c\), let \(P_c\) be the conjunction of its \(k\) defining literals (when \(k=0\), this is \(\top\)). The formula \(E(L\land P_c)\) is true everywhere exactly when the leaf type \(c\) occurs. Hence a Boolean conjunction of these formulas and their negations defines each possible leaf support \(S\). At the root, \(P_b\) tests the root's own type; at any point \(E(R\land P_b)\) globally tests it. To define a pointed root profile, conjoin the support test with \(R\land P_b\). To define a pointed leaf profile \((b,S,a)\), conjoin the support test with \(L\land P_a\land E(R\land P_b)\). Every such formula has modal depth at most two. Every formally admissible profile is realized: choose one leaf of each type in \(S\), fill the remaining \(m-|S|\) leaves with any type already present, and give the root type \(b\).

Thus profiles are both the **complete** semantic indistinguishability classes and individually definable. Their total number is \(N_{k,m}\): choose one of \(Q\) root types; choose a nonempty support of size \(j\leq m\), in \(\binom Qj\) ways; then choose one root-point kind or one of the \(j\) possible leaf-point kinds. Every subset of this finite collection is definable by a disjunction of its defining formulas. Conversely any formula determines such a subset. Therefore the Boolean algebra of formula-equivalence classes has exactly \(2^{N_{k,m}}\) elements, with depth-two representatives.

**4. Sharpness of the depth bound.** Suppose \(k\geq1\), \(m\geq2\), and fix a variable \(p\), assigning any other variables false. Compare valuations at the same distinguished leaf \(\ell_1\): both make \(p\) false at \(\ell_1\) and true at the root; in the first all leaves make \(p\) false, whereas in the second \(\ell_2\) makes \(p\) true and all other leaves make it false. Every propositional formula at the distinguished leaf agrees between the two. Every depth-one derivative formula \(d\alpha\), for propositional \(\alpha\), is false at that leaf. For a depth-one \(\gamma(\alpha,\beta)\), the leaf path rule above also agrees: its possible terms \(\beta(\ell_1)\) and \(\beta(r)\) already control any newly introduced \(\alpha\land\beta\)-leaf of the same type as the root; if \(\alpha\land\beta\) holds there, \(\beta(r)\) is already true. Arbitrary Boolean combinations preserve agreement. Yet the depth-two formula \(E(L\land p)=\gamma(\top,\neg d\top\land p)\) is false at the first distinguished leaf and true at the second. Hence depth one does not suffice.

**5. Sharp leaf-count stabilization.** The coordinate formula adds the strictly positive term \(Q\binom Qm(m+1)\) when \(1\leq m\leq Q\), so the exponent increases strictly up to \(m=Q\). Beyond this every nonempty support is already realizable and the exponent stays at \(Q[(2^Q-1)+Q2^{Q-1}]\).

## Verification

The standalone Python 3 file `checker.py` is self-contained. Running `python checker.py` returns the exact prefix `ALEXANDROV_STAR_GAMMA_ALGEBRA_OK`. It checks \(5456\) pairs \((A,B)\) over stars with one through five leaves, comparing the displayed closed path rule to two independently programmed finite-space reachability procedures. It also enumerates the pointed valuation profiles for \(k=0,1,2\) and \(m=1,2,3,4\); checks explicit depth-two characteristic tests on small parameter cases; and tests the depth-one lower-bound examples for two through four leaves. These experiments corroborate the stated identities but do not replace the general structural proof above. The latter covers all integers \(k\ge0\) and \(m\ge1\).

## Relationship to prior work

The syntax and topological path meaning of \(\gamma\) follow Gagarin and Fernández-Duque (2026), whose main theorems concern axiomatization, completeness, and decidability over broad classes of spaces. The 2024 Bezhanishvili–Bussi–Ciancia–Fernández-Duque–Gabelaia paper establishes the finite Alexandrov up-down path criterion used as a premise above (Lemma 3.6) and explicitly observes the definability of a componentwise global modality from reachability. Those facts are not claimed as new. The proposed new result is the **complete exact fixed-star formula algebra** with arbitrary variable count, the sharp depth-two limit, and the precise stabilization threshold. A 2026 dynamic polyhedral extension concerns temporal homeomorphisms and likewise supplies no checked formula-algebra count for these fixed stars. Targeted searches did not locate a covering published classification; this is a literature-limited priority conclusion, not a uniqueness certificate.

## Limitations

The result uses arbitrary Boolean valuations and the stated Cantor derivative, not persistent intuitionistic valuations or the interior-only version of reachability logic. It applies to each fixed finite rooted star, not arbitrary finite posets, dynamic temporal extensions, or infinite branching. The primitive-language depth-two bound is sharp only under the specified nontrivial parameter conditions. The use of familiar path and global modalities does not imply that the exact enumeration is historically unprecedented; independent priority and mathematical audits have not occurred.

## References

- A. Gagarin and D. Fernández-Duque, *Topological Logics of Path-Reachability*, arXiv:2606.31874 (first submitted 2026-06-30), especially Section 2 (semantics).
- N. Bezhanishvili, L. Bussi, V. Ciancia, D. Fernández-Duque and D. Gabelaia, *Logics of Polyhedral Reachability*, arXiv:2406.16056 (first submitted 2024-06-23), especially Section 3.2, Lemma 3.6, and the componentwise global modality observation in the later logic discussion.
- N. Bezhanishvili, L. Bussi, V. Ciancia, D. Fernández-Duque and D. Gabelaia, *Dynamic Polyhedral Logic*, arXiv:2608.25691 (first submitted 2026-08-26), for the distinct spatio-temporal extension.
