# A sharp five-column and depth-four cutoff for unary formulas on three-row \(\mathsf{S5}\) grids

## Finding
For each integer \(m\ge1\), let \(G_m\) have worlds \(\{0,1,2\}\times\{1,\ldots,m\}\). Its two reflexive accessibility relations connect, respectively, all worlds in the same row and all worlds in the same column. In ordinary Boolean bimodal logic with **one** propositional letter \(p\), identify formulas when their truth values agree at every world under every Boolean valuation on \(G_m\). The number of distinct pointed modal theories is exactly
\[
N_m=\begin{cases}4,&m=1,\\28,&m=2,\\88,&m=3,\\146,&m=4,\\164,&m\ge5.\end{cases}
\]
The corresponding Boolean algebra of formula-equivalence classes has **exactly** \(2^{N_m}\) elements. The same algebra for the *entire class* \(\{G_m:m\ge1\}\) has \(2^{164}\) elements. Every formula on every such frame is equivalent, simultaneously across this class, to a formula of modal depth at most four; this depth is optimal. The least number of columns realizing every possible pointed theory is **five**, also optimal. For a fixed \(m\), the optimal uniform modal-depth bound is \(\min(m,4)\).

## Assumptions and scope
The language contains Boolean connectives, the constant formulas, \(p\), and two independent normal modal operators \(\Box_h\) and \(\Box_v\), with their Boolean duals \(\Diamond_h\) and \(\Diamond_v\). The horizontal relation is equality of the first coordinate; the vertical relation is equality of the second. Valuations of \(p\) are arbitrary subsets of the frame. The labels of the two modalities are retained (they cannot be interchanged). No counting, hybrid names, diagonal operator, or global modality is present. Formula depth counts nested modal operators, not Boolean operations. An equivalent formula may depend on the original formula but not on the valuation or \(m\).

## Proof
**1. Canonical support compression.** For a valuation, encode column \(j\) by the three-bit word \(c_j\in\{0,1\}^3\) recording the truth of \(p\) in the three rows, and let \(S\subseteq\{0,1\}^3\) be the nonempty set of words actually occurring. Construct the support model \(H_S\) with points \((i,c)\), where \(i\in\{0,1,2\}\) and \(c\in S\), valuation \(p(i,c)=c_i\), horizontal accessibility to all \((i,c')\) for \(c'\in S\), and vertical accessibility to all \((i',c)\) for \(i'\in\{0,1,2\}\). The map \((i,j)\mapsto(i,c_j)\) is a surjective bounded morphism: it preserves atoms, and its images of the full horizontal and vertical successor classes are exactly the corresponding successor classes of \(H_S\). Induction on formulas therefore preserves and reflects truth at the mapped points. Conversely, every nonempty support of size at most \(m\) is realized by an \(m\)-column valuation by repeating selected column words. The possible pointed theories on \(G_m\) are exactly those represented among the \(H_S\) with \(1\le |S|\le\min(m,8)\). This holds for arbitrarily large \(m\) and does not confuse set support with multiplicity-sensitive counting.

**2. A finite depth-type recurrence.** In the disjoint union of all \(255\) nonempty support models \(H_S\), there are exactly \(3\cdot8\cdot2^7=3072\) pointed states. Define the depth-zero type \(\tau_0(w)\) to be the truth bit of \(p\). Recursively let
\[
\tau_{d+1}(w)=\Bigl(\tau_d(w),\ \{\tau_d(u):wR_hu\},\ \{\tau_d(u):wR_vu\}\Bigr).
\]
Equality of these signatures is exactly indistinguishability by formulas of depth at most \(d+1\): the forward implication follows by formula induction. For the reverse implication, characteristic formulas are available inductively. If \(\chi_t\) characterizes depth-\(d\) type \(t\), then for a depth-\((d+1)\) signature consisting of previous type \(t\) and successor-type sets \(A_h,A_v\), take
\[
\chi_t\ \wedge\!\!\bigwedge_{a\in\{h,v\}}\left(\Box_a\bigvee_{s\in A_a}\chi_s\ \wedge\!\!\bigwedge_{s\in A_a}\Diamond_a\chi_s\right).
\]
This formula has precisely that next type on the finite union. The empty-set conventions are the usual Boolean constants, although all current accessibility classes are nonempty. Thus every distinct stable type has an explicit finite-depth defining formula, not merely an abstract bisimulation label.

**3. Exact finite certificate.** The complete recurrence on the 3072 states gives the following type counts. A column \(m\) in the table counts types represented in support models with \(|S|\le m\), and the last column means the cap is eight:

| Depth \(d\) | \(m=1\) | \(m=2\) | \(m=3\) | \(m=4\) | \(m=5\) | \(m\ge8\) |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2 | 2 | 2 | 2 | 2 | 2 |
| 1 | 4 | 8 | 8 | 8 | 8 | 8 |
| 2 | 4 | 28 | 60 | 64 | 64 | 64 |
| 3 | 4 | 28 | 88 | 136 | 140 | 140 |
| 4 | 4 | 28 | 88 | 146 | 164 | 164 |
| 5 | 4 | 28 | 88 | 146 | 164 | 164 |

This is an exhaustive finite integer computation, not extrapolation from samples. The included `checker.py` constructs all nonempty supports and all horizontal/vertical successor classes, forms each signature, verifies that refinement never merges old types, and asserts the exact table including all intermediate caps \(m=1,\ldots,8\). Equality of the depth-four and depth-five partitions in this refining process proves it is a fixed point, so higher depths cannot create any further types. The independent `direct_check.py` runs the recurrence on **every raw Boolean valuation**, without support compression, for \(m=1,2,3,4,5\), checking the corresponding counts (up to \(2^{15}=32768\) labelled valuations). These computations are finite certificates for the displayed table; the reduction and characteristic-formula arguments are proved above for every \(m\).

**4. Algebra, depth and sharpness.** Since every stabilized type has a defining formula, arbitrary unions of the \(N_m\) types are definable by finite disjunctions. Distinct unions differ on a realized pointed state, proving that the formula quotient is the full Boolean powerset algebra on \(N_m\) atoms, hence has \(2^{N_m}\) elements. The table shows that the global stable count \(164\) is already attained for \(m=5\) but not for \(m=4\), and that depth three distinguishes at most \(140\) types globally while depth four distinguishes \(164\). For fixed \(m\), the strict increments at depths \(\min(m,4)\) (and stability thereafter) give the optimal depth claimed. The same characteristic formulas work across all \(G_m\) by the bounded-morphism reduction.

## Verification
Execute `python3 checker.py` and `python3 direct_check.py` from the extracted package. Both are standalone Python-standard-library programs, with no external dependencies. The first prints `THREE_ROW_S5_PROFILE_OK` and all six rows of the exact support-model depth table. The second prints `DIRECT_FRAME_OK` for all five sizes, enumerating \(8,64,512,4096,32768\) entire valuations respectively. For \(m>8\), no additional raw valuations are required because support compression proves that they introduce no new pointed theories. In particular, bounded finite experiments alone are not asserted to prove behavior on unbounded grids; the surjective bounded-morphism lemma provides that bridge.

## Relationship to prior work
Shehtman and Shkatov (2026) investigate semiproducts and products with \(\mathsf{S5}\), and Theorem 4.1 proves qualitative local tabularity of certain finite-depth products using bisimulation games. That theorem neither specifies the one-variable algebra of the class of three-row \(\mathsf{S5}\) grids nor its sharp five-column and depth-four cutoffs. Bezhanishvili and Hodkinson (2003) study the more general \(\mathsf{S5}\)-squared logic, frame extensions, finite axiomatizability, and finite-product representations; the inspected results concern validity and bounded morphic images rather than this explicit formula-algebra count. The present calculation exploits the same standard bisimulation principle but supplies a support-compression proof and a complete, reproducible 3072-state certificate for a natural fixed-factor product family.

## Limitations
The result concerns precisely one Boolean propositional variable and ordinary unlabeled \(\mathsf{S5}\) equivalence modalities on complete rectangular product frames with three rows. It does not supply the counts for additional variables, a fourth row, restricted valuation classes, or enhanced languages with counting or diagonal operators. The exact finite certificate is computational and is made independently replayable; no claim of independent human verification or historical priority is made. An equivalent enumeration in specialist literature not represented by the inspected sources is possible.

## References
- V. Shehtman and D. Shkatov, *Some Prospects for Semiproducts and Products of Modal Logics*, arXiv:2607.17928v1, first public July 20, 2026; Theorem 4.1 and §§2,4,6. https://arxiv.org/abs/2607.17928
- N. Bezhanishvili and I. Hodkinson, *All Normal Extensions of S5-Squared Are Finitely Axiomatizable*, ILLC Preprint PP-2003-25 (2003). https://eprints.illc.uva.nl/id/eprint/109/
