# Exact recurrent conjugacy between elementary Rules 18 and 126, with unequal attraction basins

## Finding
For every integer \(n\ge1\), consider synchronous elementary binary cellular automata Rule 18 and Rule 126 on the indexed cyclic ring \(X_n=\{0,1\}^{\mathbb Z/n\mathbb Z}\), with the same periodic-neighborhood convention even at sizes one and two. Let \(S_n\) and \(T_n\) denote their respective global update maps. Their **entire recurrent subsystems** are canonically conjugate by the cyclic domain-wall map
\[
 D_n(x)_i=x_i\oplus x_{i+1}.
\]
The conjugacy intertwines both **temporal evolution and spatial rotation**. Consequently, for *every* pair of integers \(n,t\ge1\),
\[
 \boxed{\#\operatorname{Fix}(S_n^t)=\#\operatorname{Fix}(T_n^t),}
\]
and their numbers of primitive temporal orbits at **every** period coincide. More strongly, for every spatial rotation \(\sigma^r\),
\[
\boxed{\#\{x\in X_n:T_n^t x=x,\ \sigma^r x=x\}
=\#\{w\in X_n:S_n^t w=w,\ \sigma^r w=w\}.}
\]
Thus all joint temporal/spatial stabilizers and their complete finite-ring spatial-period spectra agree.

The correspondence is *not* an identification of attraction basins. For a temporal orbit \(\mathcal O\) of Rule 18, let \(\widetilde{\mathcal O}\) be the corresponding Rule 126 orbit. Put \(E_n=\{w\in X_n:\sum_i w_i\equiv0\pmod2\}\) and write \(\mathcal B_S(\mathcal O)\) for the full basin of an orbit under Rule 18. Then the exact **basin transfer law** is
\[
 \boxed{\#\mathcal B_T(\widetilde{\mathcal O})
 =2\#\bigl(\mathcal B_S(\mathcal O)\cap E_n\bigr).}
\]
For example, at circumference four, both maps have one fixed point and two primitive two-cycles, but the Rule 18 basin sizes are \(12,2,2\), whereas those of Rule 126 are \(8,4,4\), matched by the recurrent conjugacy. The one-step image sizes are respectively seven and six. In fact the full-state maps are not conjugate for any \(n\ge2\); at \(n=1\) they coincide as constant-zero maps.

## Assumptions and scope
For \(a,b,c\in\{0,1\}\), Rule 18 outputs one exactly for the neighborhoods `001` and `100`; Rule 126 outputs one exactly when the three neighborhood bits are not all equal, i.e. for all triples other than `000` and `111`. The site indexed by \(i\) reads its left neighbor \(i-1\), itself \(i\) and right neighbor \(i+1\) synchronously. The two positions coincide at short rings according to cyclic indexing. Temporal periodicity means literal return of the indexed word, *not* return modulo spatial rotation. The recurrent set \(\mathcal R_F\) of a map on a finite state space is the union of its periodic orbits; a basin includes its recurrent orbit and all transient initial conditions eventually entering it. Distinct spatial shifts are not quotiented out unless explicitly stated.

## Proof
**1. Explicit factorization.** Define a second local map \(H_n:X_n\to X_n\) by
\[
 H_n(w)_i=w_{i-1}\lor w_i.
\]
Direct Boolean calculation gives
\[
\begin{aligned}
 (H_nD_nx)_i&=(x_{i-1}\oplus x_i)\lor(x_i\oplus x_{i+1})=(T_nx)_i,\\
 (D_nH_nw)_i&=(w_{i-1}\lor w_i)\oplus(w_i\lor w_{i+1})\\
 &=(1-w_i)(w_{i-1}\oplus w_{i+1})=(S_nw)_i.
\end{aligned}
\]
The second equality follows by separating the cases \(w_i=0\) and \(w_i=1\). Therefore
\[
 \boxed{T_n=H_nD_n,\qquad S_n=D_nH_n,\qquad D_nT_n=S_nD_n.}
\]
All identities are valid for every finite circumference, including repeated neighborhood coordinates. The supplied eight-neighborhood verifier independently checks the truth tables.

**2. Periodic-core bijection, with a constructive inverse.** For each integer \(t\ge1\), induction on the factorization yields \(T_n^t=H_nS_n^{t-1}D_n\). If \(T_n^t x=x\), then \(S_n^t D_nx=D_nT_n^tx=D_nx\). Conversely, take any \(w\in\operatorname{Fix}(S_n^t)\) and put
\[
 x=H_nS_n^{t-1}w.
\]
Then \(D_nx=S_n^tw=w\) and
\[
 T_n^t x=H_nS_n^{t-1}D_nx=H_nS_n^{t-1}w=x.
\]
Finally, for \(x\in\operatorname{Fix}(T_n^t)\), the same identity shows that this inverse sends \(D_nx\) back to \(x\). Therefore \(D_n\) restricts to a **bijection** between the two \(t\)-fold fixed sets for every \(t\). It also maps each temporal successor to the corresponding successor. Taking the union over \(t\), \(D_n\) conjugates the two recurrent permutations. In particular least periods and every temporal cycle count agree, without any extrapolation from finite tests.

**3. Spatial equivariance.** Both \(D_n\) and \(H_n\) commute with cyclic spatial rotation \(\sigma\). Hence the inverse on recurrent sets is also rotation-equivariant. The bijection therefore restricts to each intersection \(\operatorname{Fix}(T_n^t)\cap\operatorname{Fix}(\sigma^r)\), proving the joint fixed-point identity and preserving all combined spatial-temporal symmetries. Möbius inversion of the identical fixed-iterate counts yields equality of all primitive temporal-orbit populations.

**4. Entire attraction-basin correspondence.** The image of \(D_n\) is precisely the even-parity subspace \(E_n\): telescoping the cyclic XOR differences proves even parity, and any even-parity \(w\) can be integrated from an arbitrary first bit, giving exactly two complementary preimages. For any initial state \(x\), all its later states satisfy \(D_nT_n^k x=S_n^kD_nx\). Since both finite-state systems eventually enter a periodic orbit and the recurrent conjugacy is bijective, \(x\) enters \(\widetilde{\mathcal O}\) if and only if \(D_nx\) enters \(\mathcal O\). Thus the Rule 126 basin is exactly \(D_n^{-1}(\mathcal B_S(\mathcal O)\cap E_n)\). Every fiber there has two elements. The basin formula follows for each orbit separately; no claim of equal basin sizes is made.

**5. Full-state obstruction and the four-site example.** A Rule 18 site equal to one must update to zero, so the only fixed point is \(0^n\). Rule 126 has the same unique fixed point by Step 2. The only one-step Rule 126 preimages of \(0^n\) are the two constant words, since each local triple must be constant. When \(n\ge2\), Rule 18 also sends each word with one zero and all other entries one to \(0^n\): the zero has two agreeing neighbors and every one updates to zero. These words are distinct from the constant words. The indegrees of the unique fixed points differ, which rules out a full-state conjugacy for \(n\ge2\). For \(n=1\), every neighborhood consists of three copies of the same bit, so the two maps coincide. Direct enumeration of all sixteen configurations at \(n=4\) gives a Rule 18 fixed-point basin of size twelve and two two-cycle basins of size two; Rule 126 has a fixed-point basin of size eight and two two-cycle basins of size four. Their one-step image sizes are seven and six, respectively.

## Verification
`verification/structural_check.py` builds the original Wolfram truth tables, both auxiliary maps and both functional graphs, checks the factorization on every binary configuration through circumference sixteen, and verifies recurrent-cycle correspondence and parity-sliced basin sizes individually. Its recorded final line is `STRUCTURAL_OK`. `verification/direct_orbit_check.py` uses different bitwise formulas and a different functional-graph traversal to compare the full temporal-orbit multisets through circumference fifteen; it also verifies the circumference-four basin contrast and the two primitive eleven-cycles at circumference eleven. Its recorded final line is `DIRECT_ORBIT_OK`. Both programs use only the Python standard library. The all-circumference theorem follows from the explicit algebraic identity, not from these bounded computations.

## Relationship to prior work
Wolfram's 1983 analysis already relates the long-time statistical behavior of Rules 18, 122, 126 and 146 by transformations. Stricker's 2023 classification reports the same maximum cycle-length envelope for that four-rule group at selected circumferences. Equality of maxima does not imply equality of cycle counts, temporal-spatial stabilizers or basins; Rule 122 and Rule 146 are **not** included in the present conjugacy. Earlier exact Rule 18 period-two and odd-eleven results, and exact Rule 126 period-four results, determine selected temporal invariants; they do not supply a universal identification of all temporal periods of the two rules. The 2010 Rule 126 analysis studies particular de Bruijn cycles, finite-ring basins and memory-enriched dynamics, whereas the present claim concerns the two original, memory-free automata and an exact structural relation. Sabrié and Törmä study long-term limit sets of Rule 18 on bi-infinite lattices, which differ from this finite-ring periodic-core claim. The abstract algebraic principle behind the factorization \(HD\) and \(DH\) is standard; the precise identification of these two elementary rules and its spatiotemporal and basin consequences are the contribution here.

## Limitations
The conjugacy concerns **periodic points of finite cyclic rings**, not an arbitrary infinite-lattice topological conjugacy or equality of attraction-basin measures. The parity-slice basin formula is exact but does not by itself evaluate all Rule 18 basin sizes. The general \(HD/DH\) principle is classical. Historical discussions of Rule 18/126 transformations leave open priority of the specific factorization; the bounded comparisons do not rule out earlier equivalent formulations.

## References
1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644; first published July 1, 1983. https://doi.org/10.1103/RevModPhys.55.601 ; lawful author-hosted text https://content.wolfram.com/sw-publications/2020/08/statistical-mechanics-cellular-automata.pdf.
2. G. J. Martínez, A. Adamatzky, J. C. Seck-Tuoh-Mora, R. Alonso-Sanz, *How to make dull cellular automata complex by adding memory: Rule 126 case study*, Complexity **15** (2010), 34–49. https://doi.org/10.1002/cplx.20311 ; preprint https://arxiv.org/abs/1212.0124.
3. H.-P. Stricker, *Classification of Elementary Cellular Automata Based on Their Limit Cycle Lengths in Z/k*, Complex Systems **32** (2023), 229–251, especially Section 3.4.2. https://doi.org/10.25088/ComplexSystems.32.3.229 ; https://content.wolfram.com/sites/13/2024/01/32-3-1.pdf.
4. H. Sabrié and I. Törmä, *Limit dynamics of elementary cellular automaton 18*, arXiv:2308.12744, first posted August 24, 2023. https://arxiv.org/abs/2308.12744.
5. *Exact temporal two-orbit census and spatial zeta for elementary cellular automaton 18*. https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-exact-temporal-two-orbit-census-and-spatial-zeta-for-elementary--752b17859ec3.
6. *A sharp forty-nine-site gap and two entropy scales in Rule 126 periodic dynamics*. https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-a-sharp-forty-nine-site-gap-and-two-entropy-scales-in-rule-126-p--57fee525ae70.
7. *The first odd temporal clock of elementary Rule 18: a universal nine-step exclusion and an eleven-site onset*. https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-the-first-odd-temporal-clock-of-elementary-rule-18-a-universal-n--08ff8406f062.
