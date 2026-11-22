# Exact universal-cycle counts for four-letter words with one nonadjacent repeat

## Finding

Fix an integer \(q\ge4\) and a labeled alphabet \(\Sigma\) with \(q\) symbols. Let \(\mathcal N_q\) consist of all four-letter words containing exactly three distinct symbols in which the repeated symbol is **not** in adjacent positions. Equivalently, the members are precisely
\[
 abac,\qquad abcb,\qquad abca,
\]
with \(a,b,c\) pairwise distinct. Thus \(|\mathcal N_q|=3q(q-1)(q-2)\).

A universal cycle is an oriented circular word whose length-four cyclic windows list every member of \(\mathcal N_q\) once and no other windows. Identify circles only under rotation, not under alphabet relabeling or reversal. Put
\[
 d_+=\frac{q(q-3)}2,\quad d_-=\frac{(q-1)(q-2)}2,\quad
 e=\frac{q(q-1)(q-5)}3+q.
\]
**Theorem.** For every integer \(q\ge4\), universal cycles for \(\mathcal N_q\) exist, and their exact number is
\[
 \boxed{\mathcal U_q=\frac{7^e}{q(q-1)}
 [6(q-1)]^{d_+}[2(4q-5)]^{d_-}
 [2q(q-2)]^{q-1}\bigl((q-3)!\bigr)^{q(q-1)}.}
\]
In particular \(\mathcal U_4=1{,}177{,}583{,}616\) and \(\mathcal U_5=4{,}143{,}132{,}985{,}665{,}169{,}391{,}616{,}000{,}000{,}000\). The length of each cycle is \(3q(q-1)(q-2)\); each alphabet symbol occurs \(3(q-1)(q-2)\) times. For the ternary boundary, the same graph method gives \(12\) circles, a case already included in the broader locally square-free enumeration and not claimed as a novelty here.

## Assumptions and scope

The alphabet is finite, labeled, and has at least four members. Every target window contains precisely one repeated letter and three distinct letters. Adjacent equal letters and all-distinct four-letter windows are **excluded**. No quotient by reversal or alphabet symmetries is taken. Vertex and edge labels below are actual ordered strings, and each edge label occurs exactly once.

## Proof

**1. Directed overlap graph.** For each \(w\in\mathcal N_q\) place one arc from its first three letters to its last three letters. Vertices have exactly two forms: \(A_{ab}=aba\), for \(a\ne b\), and \(B_{abc}=abc\), for pairwise distinct \(a,b,c\). Their multiplicities are \(m=q(q-1)\) and \(n=q(q-1)(q-2)\). Every \(A\)-vertex has incoming/outgoing degree \(q-2\); every \(B\)-vertex has incoming/outgoing degree two. The arcs are exactly
\[
 A_{ab}\longrightarrow B_{bac}\quad(abac),\qquad
 B_{abc}\longrightarrow A_{bc}\quad(abcb),\qquad
 B_{abc}\longrightarrow B_{bca}\quad(abca).
\]
The first arrow is allowed for \(c\notin\{a,b\}\). (Here \(A_{bc}\) denotes the word \(bcb\).)

The graph is strongly connected: on the \(B\)-vertices, the direct third kind of arc cyclically rotates a triple, and the two-step path \(B_{abc}\to A_{bc}\to B_{cba}\) reverses its order. Rotations and reversal give any permutation of the three letters. More generally \(B_{abc}\to A_{bc}\to B_{cbd}\) replaces one chosen letter by any \(d\notin\{b,c\}\). The graph of three-element alphabet subsets linked by one-letter replacements is connected; each \(A\)-vertex is reachable from and reaches a \(B\)-vertex. Balance and connectivity give an Euler circuit, hence a universal cycle.

**2. Full Laplacian determinant reduction.** Let \(L\) be the outgoing graph Laplacian. Use a formal variable \(t\), and set
\[
 s=t+2,\quad D=s^3-1,\quad \beta=q-2,\quad
 \alpha=(t+\beta)D+s^2+s.
\]
Order first the \(A\)-vertices, then the \(B\)-vertices. Write \(U\) for the \(A\to B\) incidence matrix and \(V\) for the \(B\to A\) incidence matrix. On the \(B\)-vertices the direct rotation matrix \(R\) satisfies \(R^3=I\). Consequently the Schur complement of the \(B\)-block \(sI-R\), whose determinant is \(D^{n/3}\), yields
\[
 \det(tI+L)=D^{n/3-m}\det M(t),
\]
where \(M\) acts on arrays \(x=(x_{ab})_{a\ne b}\) by
\[
 (Mx)_{ab}=\alpha x_{ab}-\beta x_{ba}
 -s^2\sum_{c\ne a}x_{ac}-s\sum_{c\ne b}x_{cb}.
\]
Indeed \((sI-R)^{-1}=(s^2I+sR+R^2)/D\), and the three resulting two-step contributions are respectively row-preserving changes \((a,b)\to(a,c)\), column-preserving changes \((a,b)\to(c,b)\), and \(q-2\) copies of the transposition \((a,b)\to(b,a)\). The identity, initially rational in \(t\), extends to the characteristic polynomial.

Decompose the dimension-\(m\) array space into four invariant parts:

* The constants, dimension one, have eigenvalue \(C(t)=(t+\beta)D-\beta(s^2+s+1)\).
* Symmetric arrays with zero row sums, dimension \(d_+=q(q-3)/2\), have eigenvalue \(\alpha-\beta\).
* Antisymmetric arrays with zero row sums, dimension \(d_-=(q-1)(q-2)/2\), have eigenvalue \(\alpha+\beta\).
* Arrays \(x_{ab}=u_a+v_b\) with \(\sum_a u_a=\sum_b v_b=0\), dimension \(2(q-1)\), split into \(q-1\) copies of the two-by-two matrix
  \[
  \begin{pmatrix}
  \alpha-s^2(q-1)&s^2-\beta\\
  s-\beta&\alpha-s(q-1)
  \end{pmatrix}.
  \]
  Denote its determinant by \(\Delta(t)\).

The dimensions sum to \(m\): this is a direct-sum decomposition because the row/column sum constraints have the indicated ranks on the off-diagonal matrix space, and a symmetric (respectively antisymmetric) zero-row array is orthogonal to all additive arrays. Its determinant therefore factors exactly as
\[
 \det(tI+L)=D^{n/3-m} C(t)
 (\alpha-\beta)^{d_+}(\alpha+\beta)^{d_-}
 \Delta(t)^{q-1}.
\]

**3. The rooted-tree factor.** At \(t=0\), \(s=2\), \(D=7\), and \(\alpha=7q-8\). Direct substitution gives
\[
 C(0)=0,\ C'(0)=7(q-1),\quad
 \alpha-\beta=6(q-1),\quad
 \alpha+\beta=2(4q-5),\quad
 \Delta(0)=14q(q-2).
\]
All displayed nonzero factors are positive. The directed matrix-tree theorem applied to this balanced, connected graph gives the number of spanning in-arborescences rooted at **any fixed** vertex as \(\det'(tI+L)|_{t=0}/[q(q-1)^2]\). (The derivative notation means differentiate the determinant as a polynomial in \(t\), then substitute zero.) Therefore
\[
 \tau_q=\frac{7^{n/3-m+1}(q-1)}{q(q-1)^2}
 [6(q-1)]^{d_+}[2(4q-5)]^{d_-}
 [14q(q-2)]^{q-1}.
\]
The Euler circuit count with a fixed distinguished arc is, by the BEST theorem,
\[
 \tau_q\prod_v (\deg^+(v)-1)!
 =\tau_q\bigl((q-3)!\bigr)^{q(q-1)},
\]
because all \(B\)-vertices have degree two. Each Euler circuit uses the distinguished arc exactly once, so fixing it chooses exactly one representative per rotation class. Rearranging factors of seven and two gives the boxed formula, with exponent \(e=q(q-1)(q-5)/3+q\). The exponent is a nonnegative integer for \(q\ge4\). Finally, the target set has exactly \(3(q-1)(q-2)\) words beginning with each symbol, establishing the asserted letter frequencies.

## Verification

Run `python3 verify_arborescences.py`, `python3 verify_tours.py` and `python3 verify_spectral_identity.py`. All use Python's standard library only. The first constructs the overlap graph independently of the determinant reduction, evaluates exact integer Laplacian cofactors for \(q=3,4\), and tests three independent modular cofactors for \(q=5\), matching the product. The second exhaustively lists all twelve ternary circles and independently constructs and verifies a quaternary circle by Hierholzer's method. A third, independent modular checker verifies the complete characteristic-determinant factorization at two alphabet sizes and three nonzero spectral parameters. The quaternary witness is

`010201030130310120121013103132120210212312131232023020302321323032032313`.

The finite checks support the all-alphabet theorem; they do not replace the symbolic proof above.

## Relationship to prior work

Leitner and Godbole study existence of universal cycles for non-bijections and equitable word classes, but not this specific nonadjacent-repeat sublanguage or its exact enumeration. Champlin, Godbole and Tomlinson prove complementary-class existence results for broader word families, not this precise count. Burstein and Kitaev treat *patterns* up to equality-pattern equivalence rather than all explicitly labeled windows of the specified three types. Previously published exact restricted counts for **adjacent** unique repeats concern a disjoint window family, and the locally square-free four-letter count additionally includes all-distinct windows for \(q\ge4\); neither formula implies this count. At \(q=3\) the locally square-free family agrees with this one, explaining the previously known boundary count of twelve. The BEST and directed matrix-tree theorems are established tools; the claimed contribution is the explicit nonadjacent-repeat determinant factorization and all-\(q\) closed enumeration for \(q\ge4\).

## Limitations

The statement is confined to four-letter windows with exactly one nonadjacent repeated symbol, not all locally square-free words, all three-distinct words, or general word lengths. Cycles are counted with labeled symbols and without reversing orientation. There is no independent scientific audit. Although the closest published work and relevant publicly indexed exact formulas have been compared, unindexed historical specializations remain a publication-priority risk.

## References

1. A. Leitner and A. Godbole, *Universal Cycles of Classes of Restricted Words*, arXiv:0808.1309, first public 2008-08-08, https://arxiv.org/abs/0808.1309 (2008 preprint, later revised 2009).
2. M. Champlin, A. Godbole and B. Tomlinson, *Universal Cycles of Complementary Classes*, arXiv:1303.3323, first public 2013-03-14, https://arxiv.org/abs/1303.3323.
3. A. Burstein and S. Kitaev, *On Unavoidable Sets of Word Patterns*, SIAM Journal on Discrete Mathematics 19 (2005), 371–381, https://doi.org/10.1137/S0895480104445678.
4. *Exact enumeration of universal cycles for locally square-free four-letter words*, 2026 public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-enumeration-of-universal-cycles-for-locally-square-free-fo--790ba79860bf.
5. *Exact universal-cycle count for adjacent-double four-letter words*, 2026 public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-universal-cycle-count-for-adjacent-double-four-letter-word--6d6a1bc4c054.
6. Classical directed matrix-tree theorem and BEST theorem for Euler circuits.
