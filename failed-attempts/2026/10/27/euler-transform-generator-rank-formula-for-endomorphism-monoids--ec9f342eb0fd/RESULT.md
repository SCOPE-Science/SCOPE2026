# Euler-transform generator-rank formula for endomorphism monoids of full transformation semigroups

## Finding
Let \(\mathcal T_n\) be the full transformation semigroup on \(n\) points, and let \(m(n)\) be the minimum cardinality of a generating set of \(\operatorname{End}(\mathcal T_n)\). For formal power series with integer coefficients put
\[
A(z)=\frac{z}{1-z},\quad P(z)=\prod_{j\ge1}(1-z^j)^{-1},\quad Q(z)=\prod_{j\ge2}(1-z^j)^{-\lfloor j/2\rfloor}.
\]
For \(H(z)\in z\mathbb Z[[z]]\) define its multiset Euler transform
\[
\mathcal M(H)(z)=\prod_{j\ge1}(1-z^j)^{-[z^j]H(z)}.
\]
Write
\[
G=\mathcal M(APQ),\qquad G_0=\mathcal M(AP),\qquad G_{\mathrm{ess}}=\mathcal M(A(1+A)).
\]
**Theorem.** For every integer \(n\ge5\), the rank-three singular-endomorphism conjugacy-orbit count is \(r_3(n)=[z^n](G-G_0)\), the *essential* rank-two orbit count is \(r_2(n)=[z^n](G_{\mathrm{ess}}-P)\), and
\[
\boxed{m(n)=3+[z^n]\bigl(G-G_0+G_{\mathrm{ess}}-P\bigr).}
\]
For \(n=5,6,7,8,9,10,11,12\), the resulting exact minimum generating-set sizes are \(35,86,207,503,1206,2880,6808,15996\), respectively.

## Assumptions and scope
All transformations are total maps of a finite nonempty set to itself; multiplication means composition. The rank \(m(n)\) refers to the **endomorphism monoid** of \(\mathcal T_n\), not to the transformation semigroup \(\mathcal T_n\) itself and not to the image size of an endomorphism. Results concern \(n\ge5\); sizes \(n\le4\) have exceptional monoid structures and are explicitly excluded.

The published structural theorem of Gould, Grau and Johnson [1, Theorem 2.1] identifies each singular endomorphism uniquely with a permissible pair \((t,e)\) of transformations satisfying \(t^3=t\) and \(te=et=e^2=e\); conjugation by the unit group agrees with simultaneous relabeling of \((t,e)\). Here an endomorphism with an involutive two-cycle in \(t\) has image rank three; one with \(t^2=t\ne e\) has image rank two; and \(t=e\) gives rank one. The published rank-reduction theorem [1, Proposition 4.2] states \(m(n)=3+r_3(n)+r_2(n)\), where essential rank-two means not constructible from endomorphisms of strictly greater image rank. These existing structural statements are inputs, not new claims.

## Proof
**1. Counting all permissible pairs and rank-three pairs.** From \(t^3=t\), every connected component of the functional digraph of \(t\) is either a fixed point carrying zero or more incoming leaves, or a directed two-cycle carrying a nonnegative number of incoming leaves at each of its two vertices. The first species has one isomorphism type in each positive size, with generating function \(A(z)\). A two-cycle component of size \(j\ge2\) is specified, up to swapping its two cycle vertices, by a nonnegative unordered pair of leaf multiplicities summing to \(j-2\); there are \(\lfloor j/2\rfloor\) types, yielding the multiset factor \(Q(z)\).

The relation \(et=e\) forces \(\operatorname{im}e\subseteq\operatorname{Fix}(t)\), and \(te=e\) forces \(e\) to be constant on each connected component of the functional digraph of \(t\). Since \(e^2=e\), each fiber of \(e\) has exactly one distinguished \(t\)-fixed-root component whose root is its image under \(e\); all remaining \(t\)-components in that fiber are unrestricted. Thus each fiber is uniquely specified by a distinguished fixed-root star, a multiset of further fixed-root stars, and a multiset of two-cycle components. Its isomorphism-type generating function is \(APQ\). A permissible pair is an unordered multiset of such \(e\)-fibers, giving \(G=\mathcal M(APQ)\). Excluding all two-cycle components changes this to \(G_0=\mathcal M(AP)\), so subtracting counts precisely the rank-three pairs. Because conjugacy is simultaneous relabeling, \(r_3(n)=[z^n](G-G_0)\).

**2. Characterizing essential rank-two pairs.** Suppose \(t^2=t\ne e\) and \(te=et=e^2=e\). A permissible lift \((u,e)\) with \(u^3=u\), \(u^2=t\), and at least one two-cycle exists **if and only if** some fiber of \(e\) contains two distinct \(t\)-fixed points other than its distinguished \(e\)-fixed root.

For necessity, every two-cycle of \(u\) consists of two distinct \(t=u^2\)-fixed points. Neither belongs to \(\operatorname{im}e\), because \(ue=e\) forces all image points of \(e\) to be fixed by \(u\). Moreover \(eu=e\) forces the two to have the same \(e\)-image. Conversely, given such two points, define \(u\) by interchanging them, fixing all other \(t\)-fixed points, and setting \(u(x)=u(t(x))\) for \(x\notin\operatorname{im}t\). Then \(u^2=t\), \(u^3=u\), and \(ue=eu=e\), so \((u,e)\) is a rank-three permissible pair.

The singular multiplication classification in [1, Corollary 2.6 and Proposition 4.2] implies that a rank-two pair belongs to a nonessential orbit exactly when it arises as \((u^2,e)\) from such a rank-three pair. For the sufficient direction an even-type rank-three left factor exists for every \(n\ge5\): take a permutation interchanging two disjoint pairs and fixing a fifth point, and the constant idempotent onto that fifth point. Its product with the endomorphism represented by \((u,e)\) has pair \((u^2,e)\). Conversely the multiplication table shows that rank-three products yielding rank two have this form; rank-two and rank-one factors cannot generate an essential rank-two orbit.

Consequently an essential rank-two pair is exactly an idempotent \(t\) whose every \(e\)-fiber contains at most one additional \(t\)-fixed-root star beyond the distinguished root star. Each fiber therefore has generating function \(A(1+A)\), and their unordered multisets have generating function \(G_{\mathrm{ess}}=\mathcal M(A(1+A))\). Among them, pairs with \(t=e\) have exactly one fixed-root star per fiber and correspond to integer partitions, enumerated by \(P(z)\). Removing these rank-one pairs gives \(r_2(n)=[z^n](G_{\mathrm{ess}}-P)\).

**3. Rank formula.** Substitute these two independently established orbit counts into the known minimal-generator theorem \(m(n)=3+r_3(n)+r_2(n)\) for \(n\ge5\). Formal products are well-defined because each coefficient depends only on finitely many factors. This proves the displayed formula.

## Verification
The bundled standalone Python 3 file `checker.py` builds all permissible pairs directly for \(2\le n\le5\), obtains conjugacy classes by full symmetric-group relabeling, and independently tests which rank-two pairs have a rank-three square-root lift. For \(n=5\), it finds \(r_3(5)=15\) and \(r_2(5)=17\), agreeing with \(m(5)=35\). A separate exact-integer Euler-transform implementation computes the coefficients for \(5\le n\le12\); its output is `checker_output.txt`. The explicit general proof, rather than finite enumeration, establishes all \(n\ge5\).

## Relationship to prior work
Gould, Grau and Johnson [1] classified these endomorphisms, proved the essential-orbit rank formula, and described the relevant colored functional digraphs; they left an explicit computational direction to determine \(r_2(n)\) and \(r_3(n)\). The new steps here are the pointed-fiber Euler decompositions and the square-root criterion selecting essential rank-two orbits, which together turn their structural formula into an exact generating-function expression. Grau's dissertation [2, Chapter IV] independently emphasizes the remaining description of essential rank-two orbits without stating the generating formula. Classical integer-partition and Euler-transform identities are counting ingredients and are not claimed as discoveries.

## Limitations
This is an exact formal generating-function solution, not a closed elementary expression or an asymptotic estimate for \(m(n)\). Coefficients for \(n\le4\) are outside scope because of exceptional endomorphisms. No independent mathematical audit has been performed. Although the identified primary works were materially compared and a published-record search was made, an unindexed equivalent enumeration remains a possible priority risk.

## References
[1] V. Gould, A. Grau, and M. Johnson, *The Structure of End(\(\mathcal T_n\))* (2023 preprint), arXiv:2307.11596v1, https://arxiv.org/abs/2307.11596. Particularly Theorem 2.1, Corollary 2.6, Proposition 4.2, and Section 8.

[2] A. Grau, *Aspects of endomorphism monoids of certain algebras*, doctoral dissertation, University of York, August 2023, https://etheses.whiterose.ac.uk/id/eprint/33804/1/GRAU-Aspects_of_endomorphism_monoids_of_certain_algebras.pdf, especially Chapter IV.
