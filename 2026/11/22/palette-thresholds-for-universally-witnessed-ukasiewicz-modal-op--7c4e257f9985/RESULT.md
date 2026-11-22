# Palette thresholds for universally witnessed Łukasiewicz modal operators

## Finding

Let \(W\ne\varnothing\), let \(R:W\times W\to[0,1]\) be a fuzzy accessibility relation, and fix a world \(w\). For a vector \(x\in[0,1]^W\), write
\[
D_w(x)=\sup_{v\in W}\max\{0,R(w,v)+x_v-1\},\qquad
B_w(x)=\inf_{v\in W}\min\{1,1-R(w,v)+x_v\}.
\]
The row has the **finite-positive-cut property** (FPC) if \(\{v:R(w,v)\ge\varepsilon\}\) is finite for every \(\varepsilon>0\). Its distinct positive grades are **reverse well-ordered** (RWO) if every nonempty subset of \(\{R(w,v):R(w,v)>0\}\) has a greatest element.

Fix an atomic truth palette \(S\subseteq[0,1]\) containing \(0,1\). Universal one-step witnessing of \(\Diamond p\), respectively \(\Box p\), means that the displayed supremum, respectively infimum, is attained for **every** map \(p:W\to S\).

**Palette-threshold theorem.**

1. If \(S\) is finite, universal one-step witnessing holds for **both** operators if and only if the row has RWO. The equivalence holds separately for each operator.
2. If \(1\) is approached by values of \(S\) strictly below \(1\), universal one-step witnessing of \(\Diamond p\) holds if and only if FPC holds.
3. If \(0\) is approached by values of \(S\) strictly above \(0\), universal one-step witnessing of \(\Box p\) holds if and only if FPC holds.
4. Under unrestricted real atomic valuations (\(S=[0,1]\)), the two conditions coincide with FPC. If FPC holds at every world, **every modal occurrence in every formula, at arbitrary nesting depth**, has an attained extremum under every valuation.
5. Under the unrestricted real-valued vector domain, FPC at \(w\) is also equivalent to product-topology continuity of each of \(D_w,B_w\), and to uniform approximation by finite-coordinate operators. For every finite \(F\subseteq W\), their *exact* maximum truncation errors are both
\[
 \sup_{v\notin F}R(w,v).
\]

The valuation-palette thresholds are independent: a single infinite row of accessibility grade one can witness the box for every \(p\) from a palette accumulating only at \(1\), while failing the diamond; a palette accumulating only at \(0\) gives the reverse separation. Thus taking arbitrarily fine truth levels can destroy an all-valuations witness guarantee that holds at every fixed finite palette, without changing the frame.

## Assumptions and scope

The carrier \(W\) is any nonempty set, possibly infinite and uncountable. No seriality, reflexivity, symmetry or transitivity assumption is made. All extrema range over **all** worlds, including worlds assigned accessibility grade zero. Consequently the empty-positive-support row has witnessed diamond value zero and box value one. All quantifiers are classical set-theoretic quantifiers; a countably infinite subset is chosen when a positive cut is infinite.

The Łukasiewicz strong conjunction and residuum are \(a\odot b=\max(0,a+b-1)\) and \(a\Rightarrow b=\min(1,1-a+b)\), so \(D_w\) and \(B_w\) are exactly the standard fuzzy Kripke modal clauses. In parts 1–3, an *atomic palette* restricts only the values of the chosen proposition \(p\), not values of arbitrary formulas under propositional combinations. If the finite palette is a finite Łukasiewicz subalgebra, then every modal-free formula also takes values in it, and part 1 applies to all depth-one modal occurrences. The full-palette corollary does not require a restriction on modal depth.

Finite-coordinate truncations \(D_{w,F}\) and \(B_{w,F}\) take, respectively, the supremum and infimum over \(F\), with the conventional empty-domain values \(0\) and \(1\). The topology on \([0,1]^W\) is the product topology; uniform error is measured in the real absolute-value metric over the full cube, not relative error. If \(W\) is finite all statements hold trivially.

## Proof

**The finite-palette equivalence.** Suppose the positive grades have RWO. Given \(p:W\to S\) with finite \(S\), partition \(W\) into the finitely many value fibers \(W_s=\{v:p(v)=s\}\). The positive contributions to the diamond on a nonempty fiber are \(\max(0,r_v+s-1)\), a nondecreasing function of \(r_v=R(w,v)\). If the fiber contains any positive grade, RWO gives a greatest grade and therefore a greatest contribution; otherwise its contributions are all zero. Taking the maximum over finitely many fibers gives an attained global supremum. Similarly, \(\min(1,1-r_v+s)\) is nonincreasing in \(r_v\); on each fiber its infimum is attained at a greatest grade (and equals one if all grades vanish), then the minimum over the finitely many fibers is attained. This proves both sufficient conditions.

Conversely, if RWO fails, choose a nonempty set \(T\) of positive row grades with no greatest element, and put \(t=\sup T>0\). Assign \(p(v)=1\) precisely when \(R(w,v)\in T\), and \(p(v)=0\) otherwise. The diamond contributions are exactly grades in \(T\), together with zeros, so their supremum \(t\) is not attained. For the box instead put \(p(v)=0\) on those worlds and \(1\) on the others; its contributions are \(1-r_v\) for \(r_v\in T\) and \(1\) otherwise, with unattained infimum \(1-t\). Only the two truth values \(0,1\) are used. Thus either universal witnessing property forces RWO.

**Positive cuts suffice for all truth degrees.** If FPC holds, fix any \(x\in[0,1]^W\) and let \(d=D_w(x)\). If \(d=0\), every contribution is zero and the supremum is attained since \(W\ne\varnothing\). If \(d>0\), choose \(\varepsilon=d/2\). Every contribution larger than \(\varepsilon\) comes from a vertex with \(r_v\ge\varepsilon\), of which there are finitely many. The supremum therefore equals their maximum and is attained. The identity
\[
 B_w(x)=1-D_w(\mathbf1-x)
\]
follows term by term from the Łukasiewicz operations. It proves box attainment for every vector as well. The argument does not assume that the vector originates from an atom: substituting the evaluation vector of *any* modal subformula proves the arbitrary-depth corollary when FPC holds at every world.

**An accumulating upper palette forces finite cuts.** Suppose some \(C_\varepsilon=\{v:r_v\ge\varepsilon\}\) is infinite for \(\varepsilon>0\), and that \(S\) contains grades strictly below \(1\) arbitrarily close to \(1\). Choose distinct \(v_j\in C_\varepsilon\) with \(r_{v_j}\to t\in[\varepsilon,1]\), possible by sequential compactness of \([0,1]\). For each \(j\), choose \(s_j\in S\) with \(0<\delta_j=1-s_j<1/j\). Passing to a subsequence and selecting distinct terms sufficiently far along it, we may ensure \(|r_{v_j}-t|<\delta_j/2\). Assign \(p(v_j)=s_j\) and \(p(v)=0\) elsewhere. For all sufficiently large \(j\), the contributions are
\[
 \max(0,r_{v_j}-\delta_j),
\]
strictly below \(t\) and converging to \(t\). For the finitely many initial terms, select each \(v_j\) close enough to \(t\) so the same strict inequality holds; all other contributions are zero. Thus the supremum \(t\) is not attained. This contradicts universal diamond witnessing, proving the necessity of FPC. No monotonicity of the row grades was assumed. The box characterization for a palette accumulating at zero follows by substituting \(1-p\), whose palette \(1-S\) accumulates at one, in the displayed duality. This proves parts 2–4.

**Product topology and sharp error.** For finite \(F\), let \(a=D_{w,F}(x)\) and \(b=\sup_{v\notin F}\max(0,r_v+x_v-1)\). Then \(D_w(x)=\max(a,b)\), whence \(0\le D_w(x)-D_{w,F}(x)\le\sup_{v\notin F}r_v\). Equality is realized by setting \(x_v=0\) on \(F\) and \(x_v=1\) elsewhere. Hence the exact worst-case error equals the omitted-grade supremum. The duality proves the identical error for \(B_{w,F}(x)-B_w(x)\), realized by reversing these input values. The FPC property is equivalent to making the omitted-grade supremum arbitrarily small after retaining finitely many coordinates; thus it is equivalent to uniform finite approximation. Every finite-coordinate operator is product-topology continuous, so uniform approximation implies continuity. Conversely, if some positive cut is infinite, every basic product neighborhood of the all-zero vector leaves an unconstrained coordinate with \(r_v\ge\varepsilon\); switching that coordinate to one changes the diamond from zero to at least \(\varepsilon\). The diamond is discontinuous at zero. The duality similarly makes the box discontinuous at the all-one vector. This completes part 5.

**Sharp palette separations.** Take \(W=\{o\}\cup\{v_j:j\ge2\}\), assign \(R(o,v_j)=1\), and let all other edges have grade zero. The row at \(o\) has RWO, but fails FPC. For \(S_+=\{0,1\}\cup\{1-1/j:j\ge2\}\), every nonempty subset of \(S_+\) has a minimum, so \(\Box p\) always has a witness; yet assigning \(p(v_j)=1-1/j\) makes \(\Diamond p\) have unattained value one. For \(S_-=\{0,1\}\cup\{1/j:j\ge2\}\), every nonempty subset has a maximum, so \(\Diamond p\) always has a witness, while \(p(v_j)=1/j\) makes \(\Box p\) have unattained value zero. By contrast, replacing the root grades by \(R(o,v_j)=1/j\) gives an infinite positive-support row with FPC; all modal extrema in the resulting frame are witnessed under arbitrary real valuations, including at every nesting depth.

## Verification

Run `python3 checker.py` (Python standard library only). The script uses exact fractions and checks 66,900 finite vectors and 1,110 row/truncation configurations (including every input vector at each configuration), tests both Łukasiewicz modal operators against their duality, verifies the exact truncation errors, and tests six finite prefixes of each nonattainment example. Its expected output is `VERIFY_OK checked_vectors=66900 checked_truncations=1110 prefixes=6`.

Finite exhaustive checks validate the arithmetic identities and small instances, not the infinite nonattainment statements or product-topology assertions. Those follow from the proofs above. The verifier needs no network, solver, or files besides `checker.py`.

## Relationship to prior work

Khan, Martins, Madeira and Zaman (2026) provide the Łukasiewicz fuzzy Kripke and topological semantics used here, but the inspected manuscript develops their equivalence and modal axioms rather than rowwise universal witness conditions. Vidal (2022) treats global consequence, finite/witnessed models, and undecidability in many-valued modal logic; the exact palette-specific row conditions are not stated in the inspected text. Bou, Cerami and Esteva (2011) handle finite-valued Łukasiewicz modal logic with finite-model analysis, not witness guarantees on arbitrary infinite frames.

The most directly analogous published results concern **Gödel**, not Łukasiewicz, modal operators: *A vanishing-at-infinity criterion for universally witnessed Gödel possibility* (2026) obtains the positive-cut/continuity/truncation characterization for Gödel max-min possibility, but its necessity clause instead requires finite positive support. *Boolean-input Gödel witnessability: an exact one-step criterion and a depth-two obstruction* (2026) gives RWO for Boolean-input Gödel possibility and a depth-two obstruction. These precedents cover the abstract mathematical pattern of the endpoint arguments, and no novelty is claimed for generic finite-max or tail-error principles. The candidate difference is the **Łukasiewicz dual necessity/possibility and the opposite one-sided truth-palette accumulation thresholds**, with exact separations on one common fixed frame. The checked literature does not appear to state that joint criterion; this is a best-knowledge claim, not a priority guarantee.

## Limitations

This is an all-valuations, fixed-frame statement, not an axiomatization, a decidability result, a complexity bound, or a criterion for particular individual valuations. Parts 1–3 concern atomic one-step modalities unless the palette is a subalgebra closed under the propositional connectives. The theorem does not classify every possible infinite palette lacking endpoint accumulation, and no claim is made about non-Łukasiewicz t-norms or finite-support approximations in other topologies. Infinite-world arguments use classical countable selection. Older equivalents in fuzzy relational equations, possibility theory, or generalized sup-convolution could subsume some or all operator statements, although no such exact palette theorem was found in inspected sources. Independent assessment of mathematical correctness or priority has not been performed.

## References

1. M. A. Khan, M. A. Martins, A. Madeira, and B. Zaman, *On Łukasiewicz Topological Semantics*, arXiv:2610.40809, first publicly posted 2026-10-29, https://arxiv.org/abs/2610.40809 . Full 15-page manuscript inspected.
2. A. Vidal, *Undecidability and Non-Axiomatizability of Modal Many-Valued Logics*, *Journal of Symbolic Logic*, https://doi.org/10.1017/jsl.2022.32 . Accessible primary article inspected.
3. F. Bou, M. Cerami, and F. Esteva, *Finite-Valued Łukasiewicz Modal Logic Is PSPACE-Complete* (2011), IJCAI proceedings, https://www.ijcai.org/Proceedings/11/Papers/085.pdf . Accessible proceedings text inspected.
4. *A vanishing-at-infinity criterion for universally witnessed Gödel possibility* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-vanishing-at-infinity-criterion-for-universally-witnessed-g-de--5aa5ef858bfd . Full RESULT.md inspected.
5. *Boolean-input Gödel witnessability: an exact one-step criterion and a depth-two obstruction* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-boolean-input-g-del-witnessability-an-exact-one-step-criterion-a--15bde642c362 . Full RESULT.md inspected.
6. G. Hansoul and B. Teheux, *Completeness results for many-valued Łukasiewicz modal systems and relational semantics*, https://arxiv.org/abs/math/0612542 . Abstract consulted as earlier logical context, not claimed to be a complete full-text exclusion.
