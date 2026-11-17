# Sharp half-size stabilization of alternating modal possibility on finite frames

## Finding

For every integer \(n\ge1\), consider any finite nonempty directed Kripke frame \(F=(W,R)\) with \(|W|=n\). Put \(\alpha_0=\top\) and \(\alpha_{k+1}=\Box\Diamond\alpha_k\). In ordinary basic modal semantics, the truth sets of this iteration stabilize no later than

\[
\alpha_{\lfloor n/2\rfloor}\equiv_F\alpha_{\lfloor n/2\rfloor+1}
\]

and therefore all subsequent truth sets are identical. This is sharp for every \(n\ge2\): an appropriate directed path, possibly with one isolated vertex, has a world first failing at step \(\lfloor n/2\rfloor\). Equivalently, the smallest finite Kripke frame separating consecutive iterations \(\alpha_k\) and \(\alpha_{k+1}\) has exactly \(2k+2\) worlds for every \(k\ge0\).

The structural assertion is stronger than the size bound: if a world first becomes false at stage \(t\ge1\), the frame contains a **simple directed path of \(2t\) distinct worlds ending at a dead end**, with an alternating rank pattern described below. This path need not be induced; additional edges are permitted.

## Assumptions and scope

The relation \(R\subseteq W\times W\) is completely arbitrary: it may have loops, cycles, branching, and dead ends. The set \(W\) is nonempty and finite for the stabilization and minimum-size statements. No propositional letters or valuation choices occur in these formulas. All assertions concern satisfaction at individual worlds; equivalence over a frame means agreement at every world. Define \(R(x)=\{y\in W:xRy\}\). The semantics of \(\Box\) and \(\Diamond\) use universal and existential quantification respectively over \(R(x)\), with an empty universal condition true and an empty existential condition false.

Set \(B_0=\varnothing\) and \(B_k=\{x:x\not\models\alpha_k\}\) for \(k\ge1\). For a world \(x\), its **first-failure rank** \(r(x)\) is the least positive integer \(t\) such that \(x\in B_t\), or \(\infty\) if no such integer exists. The same rank construction is meaningful on arbitrary (even infinite) frames, although the finite stabilization bound uses \(|W|<\infty\).

## Proof

**Step 1: exact monotone recurrence.** By the modal truth clauses,

\[
B_{t+1}=\bigl\{x:\exists y\in R(x)\text{ such that }R(y)\subseteq B_t\bigr\}.
\]

The operator on the right is monotone in its set argument. Since \(B_0=\varnothing\), induction gives \(B_0\subseteq B_1\subseteq B_2\subseteq\cdots\). Thus the first-failure ranks are well-defined and a world, once false, never becomes true again.

**Step 2: rank-infinity witness lemma.** We prove by induction on \(t\ge1\): if \(r(x)=t\), there exists \(y\in R(x)\) such that \(r(y)=\infty\) and

\[
\max\bigl(\{r(z):z\in R(y)\}\cup\{0\}\bigr)=t-1.
\]

The maximum is taken over **finite** ranks; the assertion includes that every member of \(R(y)\) has a finite rank at most \(t-1\). For \(t=1\), the recurrence provides a successor \(y\) with \(R(y)=\varnothing\). Such a dead end has rank \(\infty\), and the maximum is zero.

Suppose \(t\ge2\) and the assertion is proved for all positive ranks below \(t\). From \(x\in B_t\setminus B_{t-1}\), choose \(y\in R(x)\) with \(R(y)\subseteq B_{t-1}\). If \(R(y)\subseteq B_{t-2}\) then \(x\in B_{t-1}\), a contradiction. Thus every successor \(z\) of \(y\) has finite rank at most \(t-1\), and some successor has rank exactly \(t-1\). By induction, **each** such \(z\) has a successor with infinite rank. Hence for no finite \(s\ge1\) does any \(z\in R(y)\) satisfy \(R(z)\subseteq B_{s-1}\). The recurrence therefore excludes \(y\) from every \(B_s\): \(r(y)=\infty\). This proves the lemma. The argument also covers the case of a relation with loops because no acyclicity was assumed.

**Step 3: extracting distinct worlds.** Suppose \(r(x_t)=t\). For \(j=t,t-1,\ldots,1\), apply the lemma to the rank-\(j\) world \(x_j\) and select an infinite-rank successor \(y_j\). For \(j\ge2\), select \(x_{j-1}\in R(y_j)\) of rank \(j-1\). At \(j=1\), \(y_1\) is a dead end. This produces directed edges

\[
x_t\to y_t\to x_{t-1}\to y_{t-1}\to\cdots\to x_1\to y_1.
\]

All \(x_j\) are distinct because their first-failure ranks differ. No \(y_j\) equals an \(x_i\) because \(r(y_j)=\infty\). The \(y_j\) are mutually distinct because the maximum first-failure rank over their successors, with zero for the empty set, equals \(j-1\) and is different for different \(j\). Therefore all \(2t\) displayed worlds are distinct; the path is simple and terminates at a dead end. The length is \(2t-1\) edges.

**Step 4: stabilization bound.** A world that newly enters \(B_t\) must have rank \(t\), requiring at least \(2t\) distinct worlds by Step 3. Hence if \(n<2t\), then \(B_t=B_{t-1}\). For \(t=\lfloor n/2\rfloor+1\), this inequality holds. Thus \(B_{\lfloor n/2\rfloor+1}=B_{\lfloor n/2\rfloor}\), and all subsequent sets are equal by deterministic iteration. The case \(n=1\) is included: \(B_0=B_1=\varnothing\).

**Step 5: sharpness and separation.** For any \(t\ge1\), consider the directed path on \(2t\) worlds

\[
w_0\to w_1\to\cdots\to w_{2t-1},
\]

with no edges other than those displayed and \(w_{2t-1}\) a dead end. Direct induction on the remaining distance \(d\) shows that a path world first fails at stage \(j\) precisely when \(d=2j-1\); even-distance vertices never fail. In particular, \(r(w_0)=t\), so \(\alpha_{t-1}\) is true and \(\alpha_t\) false at \(w_0\). Step 3 excludes any smaller separating frame. Setting \(t=k+1\) yields the exact minimum \(2k+2\). To attain the stabilization index on any odd \(n=2t+1\), add one isolated world to the \(2t\)-world path; for even \(n\), use the path alone.

## Verification

The self-contained `checker.py` enumerates every directed relation (loops allowed) on each set of one through four worlds, totalling **66,066 frames**. It computes the bad-set iteration and checks that every finite first-failure rank is at most half the frame size and yields an actual distinct-vertex witness path with the specified ranks. It additionally tests **10,000** reproducibly sampled frames on five through eight worlds and checks the path extremizers for all \(1\le t\le30\) (sizes two through sixty). Running `python3 checker.py` prints `ALTERNATING_MODAL_HALF_SIZE_OK`. These finite tests do **not** establish the general theorem; Steps 1–5 give an all-size proof.

## Relationship to prior work

Alpay and Basaran [1, Section 7, Proposition 5, Lemma 2 and Table 3] introduced a family of alternating possibility/necessity semantic-mirage examples. Their Lemma 2 supplies, for every \(k\ge1\), a separating **upper-bound path** on \(2k+2\) worlds. Their exhaustive and SAT analyses prove that size is **minimal only for \(k=1,2,3\)**. They expressly distinguish the path construction from an all-parameter minimality proof. That path construction and those three finite results are prior work, not new claims here. The present all-rank witness lemma proves the converse lower bound for arbitrary frames and every \(k\), giving an exact bound and finite-stage stabilization theorem without SAT certificates.

General modal fixed-point iteration and monotone approximants are standard [2]; such background gives finite convergence but does not by itself specify the sharp half-size cutoff for this particular two-step operator. No assertion is made that the source's finite examples or the general construction of modal approximants are novel.

## Limitations

The sharp bound is specifically for iterations of \(\Box\Diamond\) starting from \(\top\) over a **single arbitrary relation**. It does not assert a comparable bound for arbitrary modal words, arbitrary initial subsets, distinct relations for the two modalities, or all fixed-point algorithms. The required path is not necessarily induced, and existence of such a path alone does not force failure rank \(t\) when other edges exist. Infinite frames may have unbounded ranks and need not stabilize at any finite stage. Bibliographic priority against all older specialist treatments of alternating reachability ranks is not established; no independent audit has been performed.

## References

[1] F. Alpay and B. Basaran, *GPU-Accelerated Search and Certification of Bounded Indistinguishability in Finite Kripke Semantics*, arXiv:2606.15437v1 (first publicly posted 2026-06-13). https://arxiv.org/abs/2606.15437. Especially Proposition 5, Lemma 2, Table 3, and the discussion of the limits of bounded minimality in Section 7.

[2] *Modal Logic: A Contemporary View*, Internet Encyclopedia of Philosophy, section on modal \(\mu\)-calculus and monotone approximants. https://iep.utm.edu/modal-lo/.
