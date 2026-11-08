# Three-valued Łukasiewicz-transitive frames: a preorder–upset classification and exact census

## Finding
Let \(W\) be a labelled nonempty finite set, \(|W|=n\), and let \(R:W\times W\to\{0,\tfrac12,1\}\). Call \(R\) a *Łukasiewicz fuzzy preorder* when \(R(x,x)=1\) and
\[
\max(0,R(x,y)+R(y,z)-1)\le R(x,z)\qquad(x,y,z\in W).
\]
Put \(P=\{(x,y):R(x,y)=1\}\) and \(H=\{(x,y):R(x,y)\ge\tfrac12\}\). The following is an exact classification, with converse and unique recovery:

**Classification.** Such \(R\) correspond bijectively to pairs \((P,H)\) satisfying
\[
P\text{ is a preorder},\qquad P\subseteq H,\qquad P\circ H\subseteq H,\qquad H\circ P\subseteq H.
\]
Given \(P\), collapse its mutual-comparability classes to a finite poset \(Q\). Then compatible \(H\) are in bijection with upsets of the induced subposet
\[
D_Q=\{(a,b)\in Q^{\mathrm{op}}\times Q:a\not\le_Q b\}.
\]
Here the product order is \((a,b)\preceq(c,d)\) exactly when \(c\le_Q a\) and \(b\le_Q d\). The degree-one edges are precisely the order pairs of \(Q\); a chosen upset adds degree-one-half edges outside that order. Choices are independent of the sizes of the collapsed classes.

For each integer \(k\ge1\), let \(\mathcal P_k\) be the collection of partial orders on a fixed labelled \(k\)-point set, let \(u(D)\) denote the number of upsets of finite poset \(D\), and set
\[
T_k=\sum_{Q\in\mathcal P_k}u(D_Q).
\]
The **exact count of labelled \(n\)-world ternary Łukasiewicz fuzzy preorders**, for every positive integer \(n\), is
\[
\boxed{A_n=\sum_{k=1}^n {n\brace k}T_k},
\]
where \({n\brace k}\) is a Stirling number of the second kind. Equivalently, as a formal exponential generating series,
\[
\sum_{n\ge1}A_n\frac{z^n}{n!}=\sum_{k\ge1}T_k\frac{(e^z-1)^k}{k!}.
\]
Direct evaluation gives
\[
(T_1,T_2,T_3,T_4)=(1,8,256,27434),\qquad
(A_1,A_2,A_3,A_4)=(1,9,281,29027).
\]

**Catalan boundary.** If the degree-one core \(P\) is a *total preorder* with exactly \(k\) equivalence classes, then exactly
\[
C_k=\frac{1}{k+1}\binom{2k}{k}
\]
ternary Łukasiewicz fuzzy preorders have that fixed core. Thus the total number among the labelled \(n\)-world frames whose degree-one core is total is exactly
\[
\boxed{\sum_{k=1}^{n}k!{n\brace k}C_k}.
\]
At the opposite extreme, if the core is equality, the number is \(2^{n(n-1)}\). These are structural subfamilies, not extra restrictions in the general census.

## Assumptions and scope
All objects are finite, nonempty, and labelled. The middle grade is exactly \(1/2\), the Łukasiewicz strong conjunction is \(a\odot b=\max(0,a+b-1)\), and reflexivity means grade one on every diagonal entry. We count distinct accessibility matrices, not matrices modulo permutations and not arbitrary-valued \([0,1]\) matrices. A preorder means reflexive and transitive; its quotient by \(x\sim y\iff xPy\wedge yPx\) is a partial order.

A relation product \(S\circ T\) consists of pairs \((x,z)\) for which some \(y\) satisfies \(xSy\) and \(yTz\). A set \(U\) of a poset is an *upset* if \(p\in U\) and \(p\le q\) imply \(q\in U\).

## Proof
**1. Two threshold relations suffice.** Writing \(\Delta_W=\{(x,x):x\in W\}\) for the diagonal, reflexivity gives \(\Delta_W\subseteq P\subseteq H\). In the three-element chain the only positive products \(a\odot b\) are \(1\odot1=1\) and \(1\odot\tfrac12=\tfrac12\odot1=\tfrac12\). Thus transitivity of \(R\) says exactly that the composition of two \(P\)-edges is in \(P\), and that a \(P\)-edge followed or preceded by an \(H\)-edge is in \(H\). Two half-grade edges impose no condition since their strong conjunction is zero. This proves the displayed equivalence, both directions. Since a pair's membership in \(P,H\) determines its value among zero, half and one, the correspondence is injective.

**2. Passage to a poset.** For \(P\) a preorder, put \(x\sim y\iff xPy\) and \(yPx\), and write \(Q=W/{\sim}\). The two action conditions imply that \(H\) is constant on each ordered pair of \(P\)-equivalence classes: if \(xHy\), replacing either endpoint by an equivalent endpoint preserves membership, using \(P\circ H\subseteq H\) and \(H\circ P\subseteq H\). Consequently \(H\) descends to a relation \(\bar H\subseteq Q^2\) containing the order \(\le_Q\). The two action conditions become
\[
a'\le_Q a,\ a\bar H b,\ b\le_Q b'\ \Longrightarrow\ a'\bar H b'.\]
This is precisely upward closure in \(Q^{\mathrm{op}}\times Q\). The order-pair set \(\{(a,b):a\le_Q b\}\) is already an upset in that product. Therefore deleting these mandatory order pairs gives a bijection between allowable \(\bar H\) and upsets \(U\) of the induced complement \(D_Q\): take \(\bar H=\le_Q\cup U\). Conversely any such \(U\) yields an upward-closed \(\bar H\) and hence a unique \(H\) and a unique \(R\). This also proves independence from equivalence-class sizes.

**3. Exact labelled census.** For a fixed partition of \(W\) into \(k\) nonempty blocks, choices of preorder cores \(P\) correspond to partial orders \(Q\) on those \(k\) blocks. For each choice exactly \(u(D_Q)\) compatible half supports exist by Step 2. Summing gives \(T_k\), independent of which partition was selected. There are \({n\brace k}\) such partitions. Summing over \(k\) proves \(A_n\), without overcounting since \(P\) is uniquely read from each \(R\). The generating function is the standard set-partition substitution \(\sum_{n\ge k}{n\brace k}z^n/n!=(e^z-1)^k/k!\).

**4. The Catalan case.** Suppose \(Q\) is the \(k\)-element chain \(1<\cdots<k\). The complement \(D_Q\) comprises pairs \((i,j)\) with \(1\le j<i\le k\), and its order is \((i,j)\preceq(i',j')\) precisely when \(i'\le i\) and \(j\le j'\). Changing coordinates to \((s,t)=(k+1-i,j)\) identifies it with the staircase poset of cells \(s,t\ge1\), \(s+t\le k\), ordered coordinatewise. Downsets of this staircase are in bijection with Dyck paths of semilength \(k\): trace the boundary of the selected cells and the fixed diagonal in the \(k\)-by-\(k\) grid. Hence \(u(D_Q)=C_k\), using complementation to exchange upsets with downsets. There are \(k!\) ways to order \(k\) fixed unordered blocks; summing over the partitions gives the total-core formula. For \(P\) equality, \(D_Q\) is a discrete poset of \(n(n-1)\) ordered off-diagonal pairs, so it has \(2^{n(n-1)}\) upsets.

## Verification
The accompanying `newcheck.py` is a standalone Python 3 checker using only the standard library. It independently enumerates all \(3^{n(n-1)}\) candidate labelled matrices for \(1\le n\le4\) and compares the original Łukasiewicz inequalities with the proposed \((P,H)\) criteria, entry by entry. The resulting counts are \(1,9,281,29027\). Separately it enumerates every labelled poset for \(k\le4\), counts the upsets of its induced \(D_Q\), obtains \(T_k=1,8,256,27434\), and recovers all four matrix counts from the Stirling transform. The Catalan specialization is checked for chain sizes \(1\) through \(7\). This finite verification supports but does not replace the general bijective argument.

## Relationship to prior work
Khan, Martins, Madeira and Zaman (2026, arXiv:2610.40809) define reflexive Łukasiewicz-transitive fuzzy Kripke relations and develop their topological interpretation; their full available fifteen-page paper was inspected, including the definition and representation propositions. It does not supply a classification or count of ternary-valued relations. This finding adopts their established frame definition, but makes no new claim to Łukasiewicz algebraic semantics or the Kripke/topological correspondence.

Boixader and Recasens (2015) give a broader theory of generating and representing fuzzy \(T\)-preorders, but their inspected article does not state this exact three-grade preorder–upset census or Catalan fixed-core multiplicity. Pfeiffer (2004) counts ordinary crisp transitive relations; the present relation is not crisp and has nontransitive half-support in general. Prior finite-grid three-world enumeration yields \(281\) at three levels, already known in the available mathematical records; that number here is a verification point, **not a novelty claim**. The contribution is the arbitrary-size classification, Stirling–poset formula, four-world value and Catalan total-core family. Earlier max–min transitive-fuzzy counts concern a different t-norm: there, every nonzero level-cut is transitive, whereas here half-grade edges can compose to zero. See also the distinctions discussed in the associated review.

## Limitations
The series expression is an exact finite-poset summation, not an elementary closed form or efficient asymptotic estimate for arbitrary \(n\). Exact evaluation through four worlds is computationally checked; larger counts are specified by the proved finite formula but not numerically tabulated here. The classification assumes precisely three equally spaced Łukasiewicz truth values. It does not treat other grid sizes, arbitrary fuzzy degrees, isomorphism classes, or general fuzzy-topological structures not induced by the stated frames. Equivalence in different fuzzy-relation terminology may exist; the literature comparison is finite and cannot certify worldwide novelty. No independent audit was performed.

## References
1. M. A. Khan, M. A. Martins, A. Madeira, B. Zaman, *On Łukasiewicz Topological Semantics*, arXiv:2610.40809, first submitted 29 October 2026, EPTCS 455 (2026), pp. 62–76. https://arxiv.cnoctave.top/pdf/2610.40809
2. D. Boixader and J. Recasens, *Generation and Characterization of Fuzzy T-preorders*, Applied Artificial Intelligence 29 (2015), pp. 514–530. https://doi.org/10.1080/08839514.2015.1026663
3. G. Pfeiffer, *Counting Transitive Relations*, Journal of Integer Sequences 7 (2004), Article 04.3.2. https://cs.uwaterloo.ca/journals/JIS/VOL7/Pfeiffer/pfeiffer6.html
