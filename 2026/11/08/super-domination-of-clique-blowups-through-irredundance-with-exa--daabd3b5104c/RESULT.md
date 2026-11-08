# Super domination of clique blowups through irredundance, with exact cyclic enumerators

## Finding

Let \(G\) be any finite simple graph on \(h\ge1\) vertices, let \(m\ge2\), and let \(H=G[K_m]\) be its lexicographic clique blowup. Write \(\operatorname{Irr}(G)\) for the family of *irredundant* subsets: \(U\subseteq V(G)\) belongs to this family if, for every \(u\in U\), some vertex \(v\in V(G)\) satisfies \(N_G[v]\cap U=\{u\}\). The empty subset is included.

**Exact configuration correspondence.** A vertex subset \(D\subseteq V(H)\) is super dominating if and only if its complement contains at most one vertex in every clique fiber and the indices of fibers containing a complement vertex form an irredundant set of \(G\). Consequently, putting \(I_G(y)=\sum_{U\in\operatorname{Irr}(G)}y^{|U|}\), the polynomial for **all** super dominating sets is
\[
\mathcal S_{G[K_m]}(z)=\sum_{U\in\operatorname{Irr}(G)}m^{|U|}z^{mh-|U|}
=z^{mh}I_G(m/z).
\]
This is understood as a polynomial after cancellation of negative powers. The inclusion-minimal super dominating sets correspond exactly to inclusion-maximal irredundant subsets of \(G\), again with \(m^{|U|}\) lifts per subset. In particular, if \(\operatorname{IR}(G)\) denotes the maximum cardinality of an irredundant subset, then
\[
\gamma_{\mathrm{sp}}(G[K_m])=mh-\operatorname{IR}(G).
\]

For the cyclic blowup \(H_{n,m}=C_n[K_m]\), for all integers \(n\ge3\) and \(m\ge2\), define an \(8\)-state matrix \(T(y)\) indexed by binary triples \(a,b,c\in\{0,1\}\). Its nonzero entries are exactly
\[
T(y)_{(a,b,c),(b,c,d)}=y^d
\quad\text{when }\ (b,c,d)\ne(1,1,1),\quad
(a,b,c,d)\notin\{(1,1,0,1),(1,0,1,1)\}.
\]
(All other entries are zero.) Then the **complete** super-domination polynomial is
\[
\boxed{\mathcal S_{H_{n,m}}(z)=z^{mn}\operatorname{tr}(T(m/z)^n).}
\]
The super domination number is \(mn-\lfloor n/2\rfloor\). The number of super dominating sets of that minimum cardinality is exactly
\[
\boxed{m^{\lfloor n/2\rfloor}
\begin{cases}
6,&n\equiv0\pmod4,\\
2,&n\equiv2\pmod4,\\
n\lfloor(n+3)/4\rfloor,&n\text{ odd}.
\end{cases}}
\]
The underlying cyclic binary patterns and their unweighted irredundance counts have earlier descriptions; the asserted contribution is the general all-configuration correspondence for clique blowups and its weighted super-domination consequences.

## Assumptions and scope

Graphs are finite, simple, undirected, and may have disconnected components or isolated vertices. The blowup replaces each base vertex by a clique of size \(m\), joining all vertices in two fibers precisely when their base vertices are adjacent. The requirement \(m\ge2\) is essential: every fiber with one omitted vertex then retains a selected vertex to serve as a potential witness.

A set \(D\subseteq V(H)\) is super dominating if each omitted vertex \(x\notin D\) has a *selected* witness \(b\in D\) with \(N_H(b)\cap(V(H)\setminus D)=\{x\}\). Its all-set polynomial includes the full set, whose complement is empty. A set is inclusion-minimal when no proper selected subset is super dominating. The number of minimum-cardinality sets is different from the number of all inclusion-minimal sets; the displayed closed count concerns only minimum cardinality.

For \(C_n\) the cycle is a simple cycle of length \(n\ge3\), with positions indexed cyclically; \(C_3=K_3\) is included.

## Proof

**1. At most one omitted vertex per fiber.** Suppose two vertices \(x,x'\) are omitted from the same clique fiber. Every selected neighbor of \(x\) also neighbors \(x'\): outside the fiber their adjacencies coincide, and inside the fiber all other vertices meet both. Hence no selected vertex has exactly \(x\) as an omitted neighbor, contradicting super domination. Thus the omitted set \(W=V(H)\setminus D\) contains at most one vertex from each fiber.

**2. Exact witness translation.** Let \(U\subseteq V(G)\) index the fibers with one omitted vertex each. Because \(m\ge2\), every fiber has a selected vertex. For any selected vertex \(b\) in the fiber indexed by \(v\), its omitted neighbors comprise precisely the unique omitted vertices in fibers whose indices lie in \(N_G[v]\cap U\). This includes the possible omitted vertex in the same fiber, because the fiber is a clique; it also includes omitted vertices in adjacent fibers and excludes all others. Therefore an omitted vertex in fiber \(u\) has a selected witness precisely when some \(v\in V(G)\) satisfies \(N_G[v]\cap U=\{u\}\). Requiring this for every \(u\in U\) is exactly irredundance. Choices of the omitted vertex are independent among fibers, giving \(m^{|U|}\) distinct lifts. This proves the correspondence and all-set polynomial.

**3. Minimality and the scalar parameter.** Irredundance is hereditary: if \(U'\subseteq U\) and \(U\) is irredundant, any private closed-neighborhood witness for a member of \(U'\) remains private in \(U'\). If an irredundant set \(U\) can be extended, omitting an additional vertex from the new fiber gives a strictly smaller super dominating set. Conversely, any strict reduction of a super dominating set either omits a second vertex in an already used fiber (impossible by Step 1) or extends \(U\). Thus inclusion-minimal super dominating sets correspond exactly to maximal irredundant supports. The smallest selected set corresponds to a largest irredundant support, proving the scalar identity.

**4. Cyclic irredundance words.** Encode \(U\subseteq V(C_n)\) as a cyclic binary word \((w_0,\dots,w_{n-1})\), with \(w_i=1\) iff the \(i\)th base vertex lies in \(U\). Its closed neighborhood consists of itself and its two cyclic neighbors. A run of three consecutive ones leaves its middle vertex without a private closed-neighborhood witness. A run of two ones followed after a single zero by another one produces the forbidden factor \(1101\); the reflection gives \(1011\). Conversely, if none of the cyclic factors \(111,1101,1011\) occurs, every one-run has length one or two. A singleton one has itself as a private witness; each endpoint of a two-run has an outward zero neighbor whose own two neighbors are not in the support, so that outward vertex is private. Hence \(U\) is irredundant exactly when those three cyclic factors are avoided.

**5. Transfer trace.** A transition \((a,b,c)\to(b,c,d)\) appends \(d\) and rules out a newly completed forbidden factor. Assign weight \(y^d\). A closed walk of length \(n\) in the triple-state graph is in bijection with a labeled cyclic word of length \(n\); reading the appended symbols reconstructs every position, including period-dividing words exactly once per labeled word. The product of weights is \(y^{\#\text{ones}}\). Thus \(\operatorname{tr}(T(y)^n)=\sum_{U\in\operatorname{Irr}(C_n)}y^{|U|}\), also for the boundary case \(n=3\) by cyclic reading. Substitute the all-set correspondence to obtain the polynomial.

**6. Maximum support size.** In a nonempty admissible cyclic word, every run of ones is of length one or two; a two-run is followed by at least two zeros, while a singleton run is followed by at least one zero. Assign the zeros immediately following each run to that run. This gives at least as many zeros as ones, so \(|U|\le\lfloor n/2\rfloor\). A maximum independent set on the cycle, encoded by separated singleton ones, attains \(\lfloor n/2\rfloor\); thus this is the maximum irredundance size and gives \(\gamma_{\mathrm{sp}}\).

**7. Number of maximum supports, even order.** Let \(n=2k\). A maximum word has \(k\) ones and \(k\) zeros. If there are no two-runs, all ones and zeros alternate, giving two labeled words. If a two-run occurs, the consecutive zero-run following it must have length at least two. Because the preceding two-run also requires two zeros before it, equality between the total number of ones and zeros forces every one-run to be a two-run, every zero-run to have length two, and the cyclic word to be \(1100\) repeated. This occurs only when \(4\mid n\) and gives four further rotations. Thus the even-order counts are two or six, as stated.

**8. Number of maximum supports, odd order.** Let \(n=2k+1\), so a maximum word has \(k\) ones and \(k+1\) zeros. Let \(q\) be the number of two-runs and \(p=k-2q\) the number of singleton runs; then there are \(r=p+q=k-q\) zero-gaps between runs. At least one zero is needed per gap, leaving \(q+1\) extra zeros. If \(q=0\), the one extra zero can appear in precisely one gap; there are \(n\) labeled words. If \(q\ge1\) and \(p>0\), the gaps incident to two-runs demand at least \(q+1\) extra zeros, with equality precisely when all two-runs form one contiguous cyclic block of runs. Each choice of \(q\), \(1\le q\le\lfloor(k-1)/2\rfloor\), then yields exactly \(n\) labeled words: the first two-run after the singleton-run block distinguishes the starting position, and all gap sizes are forced. Finally, if \(p=0\) (possible only when \(k\) is even), all runs have length two and all \(q=k/2\) gaps have length at least two. There is exactly one extra zero, hence again exactly \(n\) words, distinguished by its position. Summing gives \(n(\lfloor k/2\rfloor+1)=n\lfloor(n+3)/4\rfloor\) labeled maximum words. Each such support has \(m^k\) lifts, completing the minimum-set count.

## Verification

The companion `verification_check.py` uses two independent definitions: super domination as an open-neighborhood private-witness test in the expanded graph, and irredundance as a closed-neighborhood private-witness test in the base graph. It examines all labeled simple graphs on at most four vertices (with the indicated small fiber sizes), every selection in their clique blowups, every cyclic base word of lengths \(3\) through \(17\), and direct clique-blowup subsets for selected small cycles. Transfer and minimum-number formulas are checked separately. Run `python3 verification_check.py` from the directory containing this file.

The exact verifier output is recorded in `VERIFICATION.md`; the file-level hashes in the enclosing package establish the tested artifact identity. The infinite identities are proved above; finite checks are corroboration only.

## Relationship to prior work

Dettlaff, Lemańska, Rodríguez-Velázquez, and Zuazua, arXiv:1703.06034 (first public version March 17, 2017), study the **minimum super-domination number** of lexicographic products. Their Lemmas 7–8 and Theorem 12 give fiber bounds and general inequalities; their cycle/path propositions handle extremal values in other product regimes. They do not state the all-configuration bijection with irredundant supports or the full weighted all-superdominating polynomial for clique fibers. The present scalar equality is a consequence of the stronger correspondence, not a claim that lexicographic super-domination itself is new.

Ghanbari, Jäger, and Lehtilä, arXiv:2209.01795 (first public version September 5, 2022), count **minimum** super dominating sets in several graph classes, notably ordinary paths and cycles; the inspected enumeration concerns the original graphs, not complete clique blowups.

The older OEIS records A286954, A291044, and A290493 already give **maximal irredundant subsets** of ordinary cycles, their cardinality tables, and total irredundant-set counts. In particular, A286954 explicitly records the cyclic forbidden factors for maximal irredundant subsets, including the three factors above, and the known upper irredundance number. Accordingly these base-cycle facts and numerical tables are not independently claimed as novel. The claim here is the exact general cross-parameter configuration correspondence and its complete super-domination polynomial on clique blowups. The transfer matrix provides an explicit reproducible weighted specialization.

## Limitations

No independent mathematical audit or external priority certification has been performed. Relevant earlier product lemmas and the known cycle irredundance tables make some corollaries straightforward once the new correspondence is available. The novelty judgment is limited to the specific complete configuration-level statement and exact weighted blowup translation; an equivalent formulation in unindexed literature remains possible. The cycle enumerator is not an independent discovery of the old base-cycle counting sequences. The proof assumes genuine clique fibers of size at least two and does not claim the same correspondence for arbitrary second factors. There is no claim about general algorithms being efficient for arbitrary base graphs, nor about computational enumeration establishing infinite statements.

## References

1. M. Dettlaff, M. Lemańska, J. A. Rodríguez-Velázquez, R. Zuazua, *On the super domination number of lexicographic product graphs*, arXiv:1703.06034, initial public version 2017-03-17. https://arxiv.org/abs/1703.06034
2. N. Ghanbari, G. Jäger, T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795, initial public version 2022-09-05. https://arxiv.org/abs/2209.01795
3. OEIS A286954, *Number of maximal irredundant sets in the n-cycle graph*, entry and notes by E. W. Weisstein and A. Howroyd, 2017. https://oeis.org/A286954
4. OEIS A291044, *Number of maximal irredundant sets of size k in the n-cycle graph*, A. Howroyd, 2017. https://oeis.org/A291044
5. OEIS A290493, *Number of irredundant sets in the n-cycle graph*, E. W. Weisstein, 2017. https://oeis.org/A290493
6. B. Bollobás and E. J. Cockayne, *Graph-theoretic parameters concerning domination, independence, and irredundance*, Journal of Graph Theory 3 (1979), 241–249. DOI 10.1002/jgt.3190030306.
