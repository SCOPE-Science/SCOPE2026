# A sharp congruence-locality dichotomy for a Klarner affine orbit

## Finding

Let \(S\) be the least subset of \(\mathbb Z_{\ge0}\) containing \(0\) and stable under
\[
A(x)=2x,\qquad B(x)=3x+2,\qquad C(x)=6x+3.
\]
For any positive integer \(m\), write \(S_m\) for the image of \(S\) in \(\mathbb Z/m\mathbb Z\). The following is an exact classification, including composite moduli:
\[
\boxed{S_m=\mathbb Z/m\mathbb Z\quad\Longleftrightarrow\quad 6\nmid m.}
\]
Consequently \(S\) represents every residue class modulo every prime power, although \(S\) never represents the residue \(1\pmod6\). In particular, its image is dense in each individual ring of \(p\)-adic integers, but not in the full profinite completion of \(\mathbb Z\).

## Assumptions and scope

All three maps act on nonnegative integers. The empty word in the generators is allowed, and hence \(0\in S\). Closure means forward application only, not use of integer inverses. For a modulus \(m\), the finite forward orbit of the residue \(0\) under the induced maps is exactly \(S_m\). The statement includes \(m=1\), for which the unique residue is attained. No density claim for \(S\) in the ordinary integers is made.

## Proof

**1. The unit case.** Suppose \(\gcd(m,6)=1\). The maps \(A\) and \(B\) are permutations of \(\mathbb Z/m\mathbb Z\). In a finite permutation group, the inverse of each generator is a positive power of that generator; therefore inverses and their products can be realized by forward words in \(A\) and \(B\) modulo \(m\). Calculate
\[
(A\circ B)(x)=6x+4,\qquad (B\circ A)(x)=6x+2.
\]
Their linear coefficient is the same unit \(6\). Thus the forward transformation semigroup contains
\[
(A\circ B)\circ(B\circ A)^{-1}:x\longmapsto x+2.
\]
Since \(m\) is odd, translation by \(2\) cycles through every residue class. Its iterates from \(0\) belong to \(S_m\). Hence \(S_m\) is the whole ring whenever \(\gcd(m,6)=1\).

**2. A twofold lifting rule.** Suppose \(3\nmid m\) and \(S_m=\mathbb Z/m\mathbb Z\). To establish surjectivity modulo \(2m\), fix an even residue \(2t\pmod{2m}\) with \(t\pmod m\) arbitrary. Choose \(x\in S\) with \(x\equiv t\pmod m\). Then \(A(x)\equiv 2t\pmod{2m}\). To obtain any odd residue \(2t+3\pmod{2m}\), choose \(x\in S\) with \(3x\equiv t\pmod m\), possible because \(3\) is a unit modulo \(m\). Now \(C(x)\equiv 2t+3\pmod{2m}\). Thus
\[
3\nmid m,\quad S_m=\mathbb Z/m\mathbb Z
\quad\Longrightarrow\quad S_{2m}=\mathbb Z/(2m)\mathbb Z.
\]

**3. A threefold lifting rule.** Suppose \(2\nmid m\) and \(S_m=\mathbb Z/m\mathbb Z\). Every residue modulo \(3m\) has a unique representation \(3t+r\), with \(t\pmod m\) and \(r\in\{0,1,2\}\). The three forward maps
\[
C(x)=3(2x+1),\quad (A\circ B)(x)=3(2x+1)+1,\quad B(x)=3x+2
\]
reach all three classes \(r=0,1,2\): for the first two, \(2x+1\) ranges over all residues modulo \(m\), since \(2\) is a unit; for the third, \(x\) ranges over all residues. Hence
\[
2\nmid m,\quad S_m=\mathbb Z/m\mathbb Z
\quad\Longrightarrow\quad S_{3m}=\mathbb Z/(3m)\mathbb Z.
\]

**4. All permitted moduli.** If \(6\nmid m\), either \(3\nmid m\) or \(2\nmid m\). In the first case write \(m=2^a u\) with \(\gcd(u,6)=1\), and apply Step 1 followed by the twofold lifting rule \(a\) times. In the second case write \(m=3^b u\) with \(\gcd(u,6)=1\), and apply Step 1 followed by the threefold lifting rule \(b\) times. This proves the forward implication for all positive \(m\).

**5. Sharp obstruction.** In the initial orbit \(0\not\equiv1\pmod6\). For any integer input, \(A(x)\) is even, \(B(x)\equiv2\pmod3\), and \(C(x)\equiv3\pmod6\). None of these outputs is \(1\pmod6\). Induction on word length gives \(1\notin S_6\). If \(6\mid m\), a residue of \(S_m\) congruent to \(1\pmod6\) would reduce to an element of \(S_6\), a contradiction. Thus \(S_m\) cannot be all residues for any multiple of six. This proves the reverse implication. \(\square\)

## Verification

The accompanying standalone Python program `verify.py` forms the complete reachable residue graph modulo each \(m\) from \(1\) to \(2000\), with no numeric upper-bound heuristics. For all \(2000\) tested moduli, it checks full reachability exactly when \(6\nmid m\), and confirms the class \(1\pmod6\) is absent whenever \(6\mid m\). Examples of counts are \(|S_6|=5\), \(|S_{12}|=10\), \(|S_{18}|=14\), and \(|S_{36}|=26\). These finite checks corroborate, but do not substitute for, the unconditional proof for every positive modulus.

## Relationship to prior work

Shamazov and Talambutsa [1, Section 4.1] identify exactly the affine family \(2x\), \(3x+2\), \(6x+3\) through the Klarner tuple \((0,2,3)\), and discuss longstanding open questions concerning the ordinary asymptotic density of its integer orbit. Their Theorems 2 and 4 concern growth bounds; their Theorem 6 gives positive density under an exact covering of integer progressions, a condition they say is unavailable for distinct slopes \(2,3,6\). These statements do not imply the above if-and-only-if modular-surjectivity classification. The classical Klarner and Rado work [2] introduces recursively generated arithmetic sets, but is not represented here as having been exhaustively reexamined. The new conclusion is finite-congruence reachability, not a solution to the ordinary density problem.

## Limitations

The theorem determines which moduli have full support, but not the exact number or structure of reachable residues when \(6\mid m\). It does not calculate asymptotic counting density, guarantee long arithmetic progressions within \(S\), or solve the classical orbit-density question. General affine semigroup methods could potentially imply the conclusion without explicitly stating this particular classification; such implicit prior coverage is an originality risk requiring independent literature review.

## References

[1] K. F. Shamazov and A. L. Talambutsa, *On orbit sets generated by semigroups of one-dimensional affine functions*, arXiv:2507.06875v1 (first posted July 9, 2025), https://arxiv.org/html/2507.06875v1 . Relevant material: Introduction and Sections 3–4, including the tuple \((0,2,3)\), growth bounds, and exact covering conditions.

[2] D. A. Klarner and R. Rado, *Arithmetic properties of certain recursively defined sets*, Pacific Journal of Mathematics **53** (1974), 445–463. Historical reference cited by [1]; not used as an unverified proof premise.
