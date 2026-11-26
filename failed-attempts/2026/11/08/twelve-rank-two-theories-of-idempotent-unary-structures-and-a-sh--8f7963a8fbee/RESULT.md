# Twelve rank-two theories of idempotent unary structures and a sharp seven-point reduction

## Finding

For every nonempty structure \(M=(X,f)\) with a single total unary function satisfying \(f(f(x))=f(x)\) for all \(x\), the complete first-order theory of quantifier rank at most two belongs to **exactly twelve classes**. This includes infinite models. Every class has a finite representative on at most seven elements, and seven is optimal. The theorem also provides an exact labelled finite-model counting series for every class.

## Assumptions and scope

The signature contains equality and one unary function symbol \(f\), with no constants, other predicates, or extra functions. The universe is nonempty. Quantifier rank means ordinary first-order nesting depth of quantifiers, without counting operators; there is no bound on Boolean formula size. A component of an idempotent function is a fiber \(f^{-1}(r)\) of a fixed point \(f(r)=r\). It is a rooted star: one root and zero, one, or at least two nonroot points. Put \(S\) for existence of a one-point component, \(D\) for existence of a two-point component, and \(L\) for existence of a component of size at least three. Put \(M_2\) for existence of at least two nonsingleton components, and \(N_2\) for existence of at least two points.

The twelve possible patterns are: when no nonsingleton component exists, the two alternatives \(N_2=0\) and \(N_2=1\); with exactly one nonsingleton component, its size category is \(D\) or \(L\), independently with \(S=0\) or \(S=1\); with at least two nonsingleton components, their size categories are only \(D\), only \(L\), or both, independently with \(S=0\) or \(S=1\). Representative component-size multisets, respectively, are

\[
(1),\ (1,1);\quad (2),\ (1,2),\ (3),\ (1,3);\quad (2,2),\ (1,2,2),\ (3,3),\ (1,3,3),\ (2,3),\ (1,2,3).
\]

## Proof

**1. The five tests have rank at most two.** The properties \(S,D,L,M_2,N_2\) are expressed, respectively, by the following sentences (the implications are object-language material implications):

\[
\begin{aligned}
S&:\ \exists x\,[f(x)=x\wedge\forall y(f(y)=x\Rightarrow y=x)],\\
D&:\ \exists x\,[f(x)\ne x\wedge\forall y((f(y)=f(x)\wedge y\ne f(x))\Rightarrow y=x)],\\
L&:\ \exists x\exists y\,[x\ne y\wedge f(x)=f(y)\wedge f(x)\ne x\wedge f(y)\ne y],\\
M_2&:\ \exists x\exists y\,[f(x)\ne x\wedge f(y)\ne y\wedge f(x)\ne f(y)],\\
N_2&:\ \exists x\exists y\,(x\ne y).
\end{aligned}
\]

Thus distinct admissible patterns cannot agree at rank two. The combinatorics of rooted-star decompositions yields exactly the twelve patterns listed above.

**2. There are no additional rank-two distinctions.** For two selected elements \(x,y\), every atomic formula is an equality between terms in \(\{x,y,f(x),f(y)\}\), because \(f^2=f\). Fix an element \(x\). If \(x\) is a root, the possible complete atomic two-element types as \(y\) varies consist of \(y=x\), a leaf in its own component (when one exists), a root of another component (when one exists), and a leaf in another component (when one exists). If \(x\) is a leaf, the types consist of \(y=x\), its own root, a distinct sibling leaf (when its component has at least three points), a root of another component, and a leaf in another component. The relevant existence conditions depend only on the twelve-pattern data.

Consequently, for two structures with the same pattern, every element on either side can be matched with an element on the other side that has the same unary atomic type and the same *set* of attainable complete atomic pair types. Duplicator uses these matches on the first move and matches the required atomic pair type on the second move. This is a winning two-round Ehrenfeucht–Fraïssé strategy, valid also for infinite universes. Hence the structures satisfy the same first-order sentences of rank at most two.

**3. Sharp finite representatives.** The displayed twelve multisets realize all patterns; each has sum at most seven. A pattern with a singleton component and two components of size at least three requires at least \(1+3+3=7\) elements. Therefore the uniform bound seven is minimal.

**4. Exact labelled counts.** A component of size \(j\ge1\) on a given labelled set has exactly \(j\) choices for its fixed-point root. Its exponential generating-function contribution is \(jz^j/j!=z^j/(j-1)!\). Thus singleton, doubleton, and large-component EGFs are

\[
A(z)=z,\qquad B(z)=z^2,\qquad C(z)=z(e^z-1-z).
\]

The exponential formula for finite labelled sets of independent components yields the two all-singleton class EGFs \(A\) and \(e^A-1-A\). With exactly one nonsingleton component, one chooses either \(B\) or \(C\) and either zero singleton components (factor \(1\)) or at least one (factor \(e^A-1\)). For at least two nonsingleton components, the options are two or more doubletons and no large components (\(e^B-1-B\)), two or more large components and no doubletons (\(e^C-1-C\)), or at least one of each (\((e^B-1)(e^C-1)\)); again multiply independently by \(1\) or \(e^A-1\). This gives exactly the twelve EGFs claimed. The coefficient rule \(n![z^n]\) gives the precise labelled counts.

## Verification

The standalone `checker.py` gives two independent finite checks. First it enumerates every nonempty multiset of rooted-star component sizes through total size thirty, constructs the complete atomic two-variable pair-type profile for each, and verifies that precisely the same twelve equivalence classes arise from the five tests. It checks all minimum representatives and the sharp seven-element bound. Second it enumerates **all** 49,023 labelled idempotent unary maps of sizes one through eight, checking that each indicator profile determines its complete two-round type. The total labelled-component formula and all twelve classwise exponential generating functions are verified through size twelve. Run `python3 checker.py` with the standard library; expected success prefix is `RANK_TWO_IDEMPOTENT_CLASSIFICATION_OK`.

The full result, including arbitrarily large and infinite structures, follows from the two-round back-and-forth argument, not from finite enumeration. The checker does not attempt an exhaustive list of all infinite models or higher-rank formulas.

## Relationship to prior work

Kuželka (2026, arXiv:2608.30580v1) studies first-order model counting with unary function symbols, establishing complexity results and reductions between labelled and unlabelled counting. That paper motivates a bounded-quantifier-rank invariant for particularly simple unary functions. The present theorem is a complete rank-two elementary-equivalence classification for idempotent unary functions, together with a sharp representative bound and exact classwise EGFs. The paper's abstract is accessible, but its complete text was not accessible in this investigation; absence of overlap in that full text is **not** asserted.

The general Ehrenfeucht–Fraïssé game principle and the labelled exponential formula are standard tools, not claimed as new. The novelty claim is restricted to the explicit twelve-pattern classification, sharp seven-point cutoff, and its classwise counting refinement. A separate published study of generic unrestricted unary-function type spaces concerns existentially closed infinite functions, not the idempotent height-one class or rank-two enumeration.

## Limitations

The classification is restricted to rank at most two and to total idempotent unary functions without added symbols. The exact EGFs count labelled **finite** models; infinite models are included in the logical classification only. An earlier equivalent statement may exist in specialist finite-model-theory literature, and the motivating paper was not inspected in full. The mathematical review is not an independent audit.

## References

- O. Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580v1 (first submitted 2026-08-31), https://arxiv.org/abs/2608.30580.
- B. Courcelle, *On first-order definable operations on relational structures*, arXiv:2605.31260 (2026), https://arxiv.org/abs/2605.31260. (General context; no claim of full-text inspection.)
