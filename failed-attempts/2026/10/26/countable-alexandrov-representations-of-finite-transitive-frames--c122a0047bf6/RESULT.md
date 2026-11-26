# Countable Alexandrov representations of finite transitive frames by \(\omega\)-accumulation

## Finding

Let \(F=(W,R)\) be a nonempty finite binary frame. On a topological space \(X\), write
\[
\omega_X(A)=\{x\in X:\text{every open neighbourhood }U\ni x\text{ has infinite intersection with }A\}.
\]
Call \(F\) *\(\omega\)-representable* if there are a space \(X\), a surjection \(\pi:X\to W\), and, for **every** \(B\subseteq W\), the identity
\[
\omega_X(\pi^{-1}B)=\pi^{-1}(R^{-1}B),\qquad
R^{-1}B=\{w\in W:\exists v\in B\;(wRv)\}.
\tag{1}
\]
All Boolean operations are automatically preserved by inverse image, so (1) is an embedding of the entire complex modal algebra \(\mathcal P(W)\) into \(\mathcal P(X)\).

**Exact representation boundary.** The frame \(F\) is \(\omega\)-representable if and only if \(R\) is transitive. Whenever it is representable, \(X\) can be chosen countable, \(T_0\), and Alexandrov. Such a representation with \(X\) additionally \(\omega\)-scattered exists if and only if \(R\) is transitive and irreflexive. When \(R\ne\varnothing\), cardinality \(\aleph_0\) is the least possible cardinality of any representing \(X\); when \(R=\varnothing\), a finite discrete representation exists.

**Single-space consequence.** There is one countable \(T_0\) Alexandrov space whose complete validity logic under \(\Diamond A:=\omega_X(A)\) is exactly \(\mathsf{K4}\). There is another single countable \(T_0\) Alexandrov space, moreover \(\omega\)-scattered, whose complete validity logic is exactly \(\mathsf{GL}\). No finite topological space can have either exact validity logic under this modality.

## Assumptions and scope

We work in ordinary classical set theory, with countable choice available. Finite frames are nonempty, but their accessibility relations need not be reflexive or serial. Transitivity means \(R\circ R\subseteq R\). Irreflexivity means \(w\not Rw\) for every \(w\). All valuations in the derived modal logic on the constructed spaces are arbitrary subsets, not merely inverse images of frame valuations. Formula transport along (1), in contrast, concerns precisely inverse-image valuations, which suffice to reflect every countermodel. \(\mathsf{K4}\) is the normal modal logic of transitive frames; \(\mathsf{GL}\) is the normal provability logic of finite transitive irreflexive frames. A space is \(\omega\)-scattered when it has no nonempty closed set \(P\) with \(P\subseteq\omega_X(P)\).

An Alexandrov space has arbitrary intersections of opens open. On a poset, its upper-set topology has least neighbourhood \(\uparrow x=\{y:x\le y\}\). The \(T_0\) property holds because the underlying order is antisymmetric. The term *representation* does **not** claim that \(\pi\) is a topological quotient, or that (1) holds for arbitrary nonsaturated subsets of \(X\).

## Proof

**Step 1: universal necessary conditions.** For every topological space and every \(A\subseteq X\), the set \(\omega_X(A)\) is closed. Indeed, if every neighbourhood of \(x\) meets \(\omega_X(A)\), then every such neighbourhood \(U\) contains a point \(y\in\omega_X(A)\). Because \(U\) itself is an open neighbourhood of \(y\), \(U\cap A\) is infinite. Furthermore \(\omega_X\) is monotone and
\[
\omega_X(\omega_X(A))\subseteq\omega_X(A).
\tag{2}
\]
For (2), a neighbourhood meeting \(\omega_X(A)\) even once already contains infinitely many points of \(A\); a fortiori this is true when it meets \(\omega_X(A)\) infinitely.

Suppose (1) holds. Because \(\pi\) is surjective, inverse image is injective. Applying (2) to \(\pi^{-1}(B)\) and using (1) twice gives \(R^{-1}(R^{-1}B)\subseteq R^{-1}B\) for all \(B\subseteq W\). Taking singleton \(B\) shows \(R\circ R\subseteq R\). Thus \(R\) is transitive.

If \(X\) is \(\omega\)-scattered, then \(R\) also has no loop. For otherwise choose \(wRw\) and put \(A=\pi^{-1}\{w\}\). Equation (1) gives the nonempty inclusion \(A\subseteq\omega_X(A)\). Monotonicity gives \(\omega_X(A)\subseteq\omega_X(\omega_X(A))\). Thus \(P=\omega_X(A)\) is nonempty, closed and satisfies \(P\subseteq\omega_X(P)\), contradicting \(\omega\)-scatteredness. Finally, if \(X\) is finite, \(\omega_X\) is identically empty. For \(R\ne\varnothing\), a singleton target of an edge has nonempty inverse image under \(R^{-1}\), so (1) is impossible on finite \(X\).

**Step 2: an explicit countable partially ordered representation.** Assume \(R\) transitive. Put \(w\sim v\) exactly when \(w=v\), or both \(wRv\) and \(vRw\). This is an equivalence relation. Let \(\mathcal C=W/{\sim}\) be its finite set of clusters. Call cluster \(C\) reflexive if \(wRw\) for a (hence every) \(w\in C\). Any cluster of size greater than one is reflexive. For distinct clusters put \(C\prec D\) if \(wRv\) for (equivalently, every) \(w\in C,v\in D\). Transitivity makes \(\prec\) a strict partial order.

Take \(X_F=W\times\mathbb N\), with \(\mathbb N=\{0,1,2,\ldots\}\), and define
\[
(w,i)\le(v,j)\quad\Longleftrightarrow\quad
(w,i)=(v,j)\ \text{or}\ [w]\prec[v]\ \text{or}\
\bigl([w]=[v]\text{ is reflexive and }i<j\bigr).
\tag{3}
\]
This is a partial order: asymmetry within a cluster comes from strictly increasing integer indices, and distinct clusters can move only upward in the strict partial order \(\prec\). The mixed cases preserve transitivity. Equip \(X_F\) with its upper-set topology. It is countable, \(T_0\), and Alexandrov. Let \(\pi(w,i)=w\).

Fix \((w,i)\) and \(B\subseteq W\). The intersection \(\uparrow(w,i)\cap\pi^{-1}(B)\) consists of at most its single point \((w,i)\), plus all copies of worlds belonging to strictly higher clusters that lie in \(B\), plus (when \([w]\) is reflexive) all copies \((v,j)\) with \(v\in B\cap[w]\) and \(j>i\). It is infinite exactly if
\[
\exists v\in B\bigl([w]\prec[v]\ \text{or}\ ([w]=[v]\text{ is reflexive})\bigr),
\]
which is equivalent to \(\exists v\in B\;(wRv)\). Since the principal upset is the smallest neighbourhood, this proves (1) for every \(B\), with no restrictions on its cardinality. Thus every finite transitive frame admits a representation.

**Step 3: exact scattered boundary.** For an arbitrary poset with its upper-set topology, it is \(\omega\)-scattered if and only if there is no infinite strictly increasing chain. In one direction, a chain \(x_0<x_1<\cdots\) gives \(A=\{x_n:n\in\mathbb N\}\subseteq\omega_X(A)\). Therefore \(P=\omega_X(A)\) is a nonempty closed \(\omega\)-perfect set by monotonicity. Conversely, if \(P\) is a nonempty closed \(\omega\)-perfect set, each \(x\in P\) has infinitely many points of \(P\) above it, so one can recursively choose \(x_0<x_1<\cdots\) inside \(P\). This uses countable dependent choice only.

If \(R\) is irreflexive, each cluster is a singleton without the within-cluster comparabilities in (3). An ascending chain in \(X_F\) would project onto a strictly increasing chain of distinct clusters, impossible in the finite set \(\mathcal C\). Hence \(X_F\) is \(\omega\)-scattered. This proves both sufficiency directions and, with Step 1, the two exact representation boundaries. When \(R=\varnothing\), one may instead take \(X=W\) with the discrete topology and \(\pi\) the identity.

**Step 4: preservation of all modal formulas.** Given any Kripke valuation \(V\) on \(F\), use \(\widehat V(p)=\pi^{-1}(V(p))\). The Boolean connectives commute with inverse image, and (1) supplies the induction step for \(\Diamond\). Therefore, for every modal formula \(\varphi\),
\[
\llbracket\varphi\rrbracket_{(X_F,\widehat V),\omega}
=\pi^{-1}\bigl(\llbracket\varphi\rrbracket_{(F,V),R}\bigr).
\tag{4}
\]
In particular, every finite transitive frame countermodel lifts to the \(\omega\)-semantics on a countable \(T_0\) Alexandrov space. The same holds in the \(\omega\)-scattered class for finite irreflexive transitive counterframes.

**Step 5: single countable completeness spaces.** Take one representative of each isomorphism type of nonempty finite transitive frames and form the topological disjoint union \(X_{\mathsf{K4}}\) of their spaces (3). Similarly, take the disjoint union \(X_{\mathsf{GL}}\) over all finite transitive irreflexive frames. Both are countable, \(T_0\), Alexandrov spaces; the latter is \(\omega\)-scattered, because a strictly increasing chain cannot leave its component. The \(\omega\)-operator acts componentwise, since components are open. Standard finite-frame completeness of \(\mathsf{K4}\) and \(\mathsf{GL}\), together with (4), shows that any non-theorem fails on the corresponding single space. Soundness on the corresponding spaces follows from universal \(\mathsf{K4}\) soundness and \(\mathsf{GL}\) soundness on \(\omega\)-scattered spaces (Montacute, Theorems 6.16 and 6.18). Hence their exact validity logics are \(\mathsf{K4}\) and \(\mathsf{GL}\), respectively.

For any finite topological \(X\), \(\omega_X(X)=\varnothing\), so \(\neg\Diamond\top\) is valid on \(X\). This formula fails in a one-world reflexive transitive Kripke frame and also in a two-world strict transitive Kripke chain, so it belongs to neither \(\mathsf{K4}\) nor \(\mathsf{GL}\). Therefore no finite space realizes either exact logic, and countability is sharp.

## Verification

The accompanying `checker.py` enumerates all \(4180\) transitive labelled binary relations on nonempty sets of sizes one through four. For every relation, it constructs the clusters and verifies that the finite truncation of (3) is a partial order. It independently counts \(\uparrow(w,i)\cap\pi^{-1}(B)\) for every \(B\subseteq W\) with two truncation sizes and compares the counts against the exact affine formula
\[
\mathbf 1_{w\in B}+(N-i-1)\mathbf 1_{[w]\text{ reflexive}}|B\cap[w]|+N\sum_{D\succ[w]}|B\cap D|,
\quad i=1,\ N\in\{3,5\}.
\]
The positive coefficient of \(N\) is equivalent to \(w\in R^{-1}(B)\). The checker independently verifies this equivalence and the irreflexive no-within-cluster condition. Execution returned `ALL_CHECKS_OK transitive_frames= 4180 counting_and_modal_checks= 779484`. Finite tests do not prove the universal claim; Steps 1–5 are its proof. The checks do not assert exhaustive testing of arbitrary topologies or infinite set theory.

## Relationship to prior work

Montacute, *Halo Semantics for Modal Logic* (arXiv:2606.31885v1, June 30, 2026), identifies the nonstandard halo modality with the topological \(\omega\)-accumulation operator and proves \(\mathsf{K4}\) completeness over infinite spaces and \(\mathsf{GL}\) completeness over infinite \(\omega\)-scattered spaces. Its proofs transfer from finite Kripke frames using metrizable \(T_1\) spaces and derivative maps. The present result instead classifies exactly which **individual finite frames** embed by inverse images into \(\omega\)-algebras, constructs countable \(T_0\) Alexandrov witnesses explicitly, and realizes each logic on a **single** countable space. Neither the general-class completeness statements nor the ordinary Alexandrov/interior correspondence alone yield this exact representation characterization.

Baltag, Bezhanishvili, Özgün and Smets, *A Topological Approach to Full Belief* (2018/2019), Section 2.2.2, establishes the classical equivalence between reflexive-transitive Kripke frames and Alexandrov spaces for the **interior** modality. Here the modality is instead infinitude of successors in each neighbourhood, and the representable frames need only be transitive, possibly irreflexive. The mechanisms are distinct. A published finding on the countable indiscrete halo space studies \(\mathsf{KD45}\) and the failure of pointwise Kripke representation of the full \(\omega\)-operator; the present result claims only preservation on the saturated subalgebra, and does not conflict with that phenomenon.

## Limitations

This is a finite-frame representation theorem: no analogous exact characterization is claimed for infinite source relations. The constructed space is countable and generally not Hausdorff. The map \(\pi\) is used only through inverse image; (1) is not asserted on arbitrary valuations on \(X_F\), nor is it a Kripke correspondence for the full power-set algebra of that space. The exact single-space logics rely on the established finite-frame completeness theorems and established topological soundness; those metatheorems are not re-proved here. Priority relative to unindexed older work on Alexandrov derivative logics remains subject to independent scholarly review.

## References

1. Yoàv Montacute, *Halo Semantics for Modal Logic*, arXiv:2606.31885v1 (first public June 30, 2026), especially Sections 6.1–6.3, Theorems 6.4, 6.16 and 6.18. https://arxiv.org/html/2606.31885
2. Alexandru Baltag, Nick Bezhanishvili, Aybüke Özgün, Sonja Smets, *A Topological Approach to Full Belief*, *Journal of Philosophical Logic* 48 (2019), 205–244; online May 23, 2018, especially Section 2.2.2. https://doi.org/10.1007/s10992-018-9463-4
3. Patrick Blackburn, Maarten de Rijke, Yde Venema, *Modal Logic*, Cambridge University Press (2001), standard finite transitive-frame completeness and provability-logic references (background, not an assertion of the present representation).
