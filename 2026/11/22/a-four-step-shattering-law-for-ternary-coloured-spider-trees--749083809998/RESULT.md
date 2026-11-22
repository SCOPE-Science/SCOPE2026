# A four-step shattering law for ternary-coloured spider trees

## Finding
Let \(S(a,b,c)\) denote the finite tree consisting of one hub and three internally disjoint paths of positive edge lengths \(a,b,c\), measured from the hub. Take **all** proper maps from its vertices to three named colours, and test a colouring by individual Boolean vertex–colour equality queries. Write \(V(a,b,c)\) for the VC dimension of this Boolean concept family.

**Four-step stability theorem.** For all positive integers \(a,b,c\) and each arm length at least four in the displayed identity,
\[
V(a+4,b,c)=V(a,b,c)+3\qquad(a\ge4),
\]
with the analogous identities in the other arms. No large-length or genericity qualification is needed. A finite exact, all-parameter formula for \(V(a,b,c)\) is given below by a twenty-state recurrence. In particular, on the equal-arm spider, for **every** integer \(m\ge1\),
\[
\boxed{V(m,m,m)=1+\left\lceil\frac{9m}{4}\right\rceil.}
\]
For example the dimensions at equal arm lengths \(m=1,2,3,4,5,6,7,8\) are \(4,6,8,10,13,15,17,19\). This concerns ordinary static VC shattering, not the online learning dimension.

## Assumptions and scope
The tree is simple, with all three arm lengths positive. A proper colouring assigns one of the **named** colours \(1,2,3\) to each vertex, with adjacent vertices differently coloured. The query \((v,t)\) outputs one precisely when vertex \(v\) has colour \(t\). Shattering means realization of every binary labeling of a fixed set of queries by possibly different proper colourings. A shattered query set cannot contain two different colour queries at the same vertex, so we represent each vertex by a *mark*: \(0\) when unqueried, or \(t\in\{1,2,3\}\) for a query about colour \(t\). The number of nonzero marks is the number of queries. No symmetry quotient is taken on colours or vertices.

Masks are integers from \(0\) through \(7\), with bit \(t-1\) indicating the availability of colour \(t\). For a nonzero mask \(M\), define
\[
J(M)=\begin{cases}7\mathbin{\mathrm{xor}}M,&M\text{ is a singleton},\\7,&M\text{ contains at least two colours}.\end{cases}
\]
Here `xor` is bitwise exclusive-or. Thus \(J(M)\) is exactly the set of colours allowable at a new predecessor adjacent to a vertex whose possible colours are \(M\).

A *signature* \(F\) is a nonempty set of nonzero masks. It lists the allowed terminal-vertex colour sets arising from **every** choice of binary answers on the marked part of an arm. Define transitions by processing arm vertices from leaf to hub:
\[
T_0(F)=\{J(M):M\in F\},
\]
\[
T_t(F)=\{J(M)\cap\{t\},\ J(M)\setminus\{t\}:M\in F\}\quad(t=1,2,3).
\]
All masks in these formulas are interpreted as colour sets. If any resulting mask is empty, the transition is *invalid*: that arm has a binary answer pattern impossible to realize. Otherwise repeated identical masks are merged.

Let \(D_0(\{7\})=0\), with all other signatures initially infeasible (weight \(-\infty\)). For \(\ell\ge0\), let
\[
D_{\ell+1}(G)=\max_{\substack{F,t\in\{0,1,2,3\}\\T_t(F)=G\text{ valid}}}\bigl(D_\ell(F)+\mathbf1_{t\ne0}\bigr).
\]
This is an exact max-plus recurrence: \(D_\ell(F)\) is the largest number of selected vertices achievable by a length-\(\ell\) arm with signature \(F\). No unbounded state search is required.

For any three signatures \(F_1,F_2,F_3\), define the hub test \(H(F_1,F_2,F_3,t)\) to mean that for **every** triple \(M_i\in F_i\), the intersection \(K=J(M_1)\cap J(M_2)\cap J(M_3)\) is nonempty and, when \(t\ne0\), both \(t\in K\) and \(K\setminus\{t\}\ne\varnothing\). Then the following expression is an exact all-parameter formula:
\[
V(a,b,c)=\max_{\substack{F_1,F_2,F_3,t\\H(F_1,F_2,F_3,t)}}\left[D_a(F_1)+D_b(F_2)+D_c(F_3)+\mathbf1_{t\ne0}\right].
\]
The maximum ranges over feasible signatures and \(t\in\{0,1,2,3\}\). For any arm of length at least four, there are exactly twenty possible signatures.

## Proof
**1. Exact arm semantics.** For each binary label string on an arm's selected queries, the set of possible colours at the terminal vertex is a mask. Adding a vertex adjacent to that terminal transforms the old allowable mask \(M\) into \(J(M)\). An unselected new vertex admits all of \(J(M)\). If the new vertex is tested for colour \(t\), the positive answer gives \(J(M)\cap\{t\}\) and the negative answer gives \(J(M)\setminus\{t\}\). These are independent choices for each previous label string, so the family of all possible masks evolves by precisely \(T_t\). An empty member certifies a forbidden trace and can never be repaired by adding more vertices. Induction from the empty arm (signature \(\{7\}\)) proves the recurrence and the exact meaning of \(D_\ell\).

**2. Exact hub semantics.** Once the label strings on three disjoint arms are chosen independently, the corresponding feasible hub colours are \(J(M_1),J(M_2),J(M_3)\). A global proper colouring exists exactly when their intersection is nonempty. If the hub itself is queried, its positive answer requires its target colour in every intersection and its negative answer requires a different one in every intersection. This is exactly the test \(H\). Conversely any colour in the relevant intersection provides compatible colourings of all three arms, since those arms have no edges between them. Optimizing the number of queries over the three independent arm signatures proves the finite exact formula for every \(a,b,c\ge1\).

**3. The finite four-step certificate.** Applying the four elementary transitions to the initial signature gives nineteen feasible signatures at length three and exactly twenty at length four. The following exhaustive table lists **all twenty** feasible signatures at length four, their optimum weights at lengths four and eight, and their four successor states. A sequence such as `1,2,3,4` denotes a set of four colour masks, not an ordered path. A dash denotes an invalid selected transition. Indexing is zero-based.

| ID | Signature masks | \(D_4\) | \(D_8\) | Successors for marks 0, 1, 2, 3 |
|---:|---|---:|---:|---|
| 0 | 1,2,3,4 | 3 | 6 | 12, –, –, – |
| 1 | 1,2,4,5 | 3 | 6 | 12, –, –, – |
| 2 | 1,2,4,6 | 3 | 6 | 12, –, –, – |
| 3 | 1,2,5 | 3 | 6 | 16, –, –, 0 |
| 4 | 1,2,6 | 3 | 6 | 16, –, –, 0 |
| 5 | 1,3,4 | 3 | 6 | 14, –, 1, – |
| 6 | 1,4,6 | 3 | 6 | 14, –, 1, – |
| 7 | 1,6 | 3 | 6 | 18, –, 9, 8 |
| 8 | 2,3,4 | 3 | 6 | 13, 2, –, – |
| 9 | 2,4,5 | 3 | 6 | 13, 2, –, – |
| 10 | 2,5 | 3 | 6 | 17, 6, –, 5 |
| 11 | 3,4 | 3 | 6 | 15, 4, 3, – |
| 12 | 3,5,6,7 | 3 | 6 | 19, 7, 10, 11 |
| 13 | 3,5,7 | 2 | 5 | 19, 7, 10, 11 |
| 14 | 3,6,7 | 2 | 5 | 19, 7, 10, 11 |
| 15 | 3,7 | 2 | 5 | 19, 7, 10, 11 |
| 16 | 5,6,7 | 2 | 5 | 19, 7, 10, 11 |
| 17 | 5,7 | 2 | 5 | 19, 7, 10, 11 |
| 18 | 6,7 | 2 | 5 | 19, 7, 10, 11 |
| 19 | 7 | 2 | 5 | 19, 7, 10, 11 |

This table is a finite arithmetic certificate, not a finite-sample extrapolation: the successor columns prove closure of the twenty-state set for **all later lengths**, and the displayed \(D_8\) column is obtained by applying those very transitions four times to \(D_4\). Every state satisfies \(D_8(F)=D_4(F)+3\). The max-plus transition is translation-equivariant, so induction gives
\[
D_{\ell+4}(F)=D_\ell(F)+3\qquad(\ell\ge4)
\]
for all twenty states. The exact hub formula is also translation-equivariant, hence adding four vertices on any arm already of length at least four increases the global optimum by **exactly three**, proving the four-step stability theorem.

**4. Equal-arm closed form.** The exact hub formula applied to arms of length \(1,2,3,4,5,6,7\) gives respectively \(4,6,8,10,13,15,17\). Each value is reproduced by direct feasible-signature optimization from the recurrence; the executable certificate includes the entire finite calculation. These seven initial values agree with \(1+\lceil 9m/4\rceil\). For \(m\ge4\), simultaneously extending all three arms by four adds \(9\) to VC dimension. Since the displayed expression also increases by nine under this operation, induction on \(m\) establishes the claimed formula for **all** positive integers.

## Verification
The standalone `spider_vc_certificate.py` uses integer bitmask arithmetic only, builds every feasible arm signature and exact max-plus weight, lists all twenty states and their transitions, and checks the critical equality \(D_8=D_4+3\). The file `spider_vc_verification_output.txt` is its complete captured stdout. It also **independently** enumerates actual proper three-colourings for every three-arm spider with a total of at most six arm edges, comparing all 58,624 marked-query assignments against the arm-signature criterion. Finally it recomputes the equal-arm dimensions at lengths one through twelve and several asymmetric four-step identities. The exact infinite theorem is justified by the proved recurrences and the finite certificate identity, not by extrapolating those tests.

Run with the standard-library command `python3 spider_vc_certificate.py` in the directory containing the supplied files. The only inputs are the displayed definitions; there are no external datasets, solvers, random seeds, or network dependencies.

## Relationship to prior work
Walker's *Tree Dimension and the Sauer–Shelah Dichotomy* (first posted March 23, 2022) treats general VC and Littlestone shattering and provides the learning-theoretic framework, but not proper-colouring spider values. Blanca, Chen, Štefankovič and Vigoda (2017) investigate inference of an unknown graph from randomly sampled proper colourings, rather than the VC dimension of one-hot vertex–colour equality concepts on a specified tree. Earlier work on **paths** gives the three-colour dimension \(n-\lfloor n/4\rfloor\), but an arm-extension identity at a common degree-three hub does not follow from the path statement. Earlier finite-tree work isolates the six-selected-vertex obstruction on the seven-vertex \((3,2,1)\) spider and explicitly leaves all larger trees unclassified. That local obstruction gives a necessary condition but neither proves nor yields the universal arm-periodicity and balanced-spider formula here. The present work preserves those earlier conclusions and claims no novelty for them.

## Limitations
The result is restricted to ordinary proper **three**-colourings of three-arm trees with vertex–colour equality tests. The twenty-state construction computes the exact VC dimension for every asymmetric triple of positive lengths; a single elementary closed expression is given only for equal arms. There is no claim about other palettes, arbitrary trees, or the Littlestone dimension. The finite table is an explicit proof certificate; independent mathematical audit and exhaustive historical-priority verification have not been performed. Related results indexed under alternate terminology could affect originality.

## References
1. Roland Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first posted March 23, 2022, https://arxiv.org/abs/2203.12211.
2. Antonio Blanca, Zongchen Chen, Daniel Štefankovič and Eric Vigoda, *Structure Learning of H-colorings*, arXiv:1708.05118, first posted August 17, 2017, https://arxiv.org/abs/1708.05118.
3. *A sharp three-colour palette threshold for VC and online shattering of path colourings* (2026), available as a publicly indexed mathematical result.
4. *The first branching obstruction to three-colouring shattering on trees* (2026), available as a publicly indexed mathematical result.
