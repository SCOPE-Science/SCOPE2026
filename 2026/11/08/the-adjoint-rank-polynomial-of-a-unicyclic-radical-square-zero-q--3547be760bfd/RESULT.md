# The adjoint-rank polynomial of a unicyclic radical-square-zero quiver algebra detects cycle length

## Finding
Let \(q\) be any prime power. Let \(Q\) be an orientation of a finite, connected, simple unicyclic graph \(G\) with \(n\) vertices and a unique cycle of length \(c\), where \(3\le c\le n\). Write \(J\) for the arrow ideal of the path algebra and \(A=\mathbb F_qQ/J^2\). For \(a\in A\), set \(\operatorname{ad}_a(b)=ab-ba\), and define its rank enumerator
\[
R_{Q,q}(z)=\sum_{a\in A}z^{\operatorname{rank}_{\mathbb F_q}(\operatorname{ad}_a)}.
\]
Then
\[
\boxed{R_{Q,q}(z)=\bigl(1+(q^2-1)z\bigr)^{n-c}\Bigl[\bigl(1+(q^2-1)z\bigr)^c+(q-1)(1-z)^c+q(q-1)^c(z^{c-1}-z^c)\Bigr].}
\]
Every rank from \(0\) through \(n\) occurs. Moreover,
\[
[z^0]R_{Q,q}=q,\qquad\deg R_{Q,q}=n,\qquad[z^1]R_{Q,q}=q(q-1)\bigl((q+1)n-qc\bigr).
\]
Consequently the **polynomial itself** recovers \(q\), \(n\), and \(c\). Conversely these three data determine the entire polynomial: the ranks are unchanged by every edge reversal or rearrangement of the trees attached to the unique cycle. The centralizer of \(a\) has dimension \(2n-\operatorname{rank}(\operatorname{ad}_a)\), so this is simultaneously the complete centralizer-dimension spectrum.

## Assumptions and scope
The underlying undirected graph is simple and connected with precisely one cycle, and each undirected edge carries exactly one oriented arrow. Its \(n\) vertices and \(n\) arrows give the basis of \(A\), so \(\dim_{\mathbb F_q}A=2n\). Every path of length two is zero in the quotient, even when the quiver contains an oriented cycle. All finite fields, including characteristic two, are covered. We count elements in the specified algebra, not isomorphism classes of centralizer subalgebras.

## Proof
Write an element as \(a=\sum_{v\in V(G)}s_ve_v+\sum_{e\in E(G)}t_ea_e\), with \(s_v,t_e\in\mathbb F_q\). For an oriented edge \(e\colon i\to j\), let \(\delta_e=s_i-s_j\). The defining multiplication yields
\[
[a,\sum_v u_ve_v+\sum_e w_ea_e]
 =\sum_{e:i\to j}\bigl(\delta_e w_e+t_e(u_j-u_i)\bigr)a_e.
\]
In the commutator matrix, each row indexed by an edge with \(\delta_e\ne0\) has a pivot in its own arrow-coordinate column. Eliminating these rows leaves the signed incidence rows indexed by
\[
S=\{e:\delta_e=0,\ t_e\ne0\}.
\]
Thus the rank is the number of edges with \(\delta_e\ne0\) plus the row rank of the incidence matrix of \(S\). Incidence matrices of loopless graphs have rank \(|V|-\kappa(S)\) over every field, where \(\kappa(S)\) is the number of components after including the isolated vertices. Since \(G\) is unicyclic, \(\operatorname{rank}B_S=|S|-1\) precisely when \(S\) contains the entire unique cycle, and equals \(|S|\) otherwise. Hence
\[
\operatorname{rank}(\operatorname{ad}_a)
=\#\{e:(\delta_e,t_e)\ne(0,0)\}
-\mathbf1_{\{\delta_e=0,\ t_e\ne0\ \text{for every cycle edge}\}}.
\tag{1}
\]
The map from vertex labels \((s_v)\) to edge differences \((\delta_e)\) has a one-dimensional kernel. Choose a coherent direction around the unique cycle and change the signs of some \(\delta_e\) to match it. Its image consists of all edge labels obeying the *single* cycle equation \(\sum_{e\in C}\delta_e=0\); differences on the \(n-c\) bridges are independent. Each permitted difference vector has exactly \(q\) vertex-label preimages.

On a bridge, the pair \((\delta_e,t_e)\) has one zero choice and \(q^2-1\) nonzero choices, contributing \(1+(q^2-1)z\). On the cycle, fix a set of \(r\) positions at which \((\delta_e,t_e)\ne(0,0)\). With the cycle sum constrained to zero, the number of assignments on those positions is
\[
\frac{(q^2-1)^r+(q-1)(-1)^r}{q}.
\tag{2}
\]
To verify (2), apply additive-character orthogonality to the sum of the first coordinates. For the trivial character each nonzero pair contributes \(q^2-1\); for every nontrivial character its sum over the nonzero pairs is \(-1\), because the \(\delta=0\) term contributes \(q-1\) and the \(\delta\ne0\) terms contribute \(-q\). There are \(q-1\) such characters.

Multiplying (2) by the \(q\) constant vertex-label choices, choosing the \(r\) positions, and summing produces \(\bigl(1+(q^2-1)z\bigr)^c+(q-1)(1-z)^c\). There is one exceptional event in (1): every cycle difference is zero and every cycle radical coefficient is nonzero. It has \(q(q-1)^c\) assignments to the cycle variables, and the true rank is one less than the number of supported pairs. Replacing \(z^c\) by \(z^{c-1}\) in exactly those cases gives the displayed correction. Multiplying the independent bridge factors proves the polynomial formula.

The constant term is \(q\) and direct coefficient extraction yields the asserted linear coefficient. Every rank \(0\le r<n\) is realized by setting all vertex labels equal and choosing exactly \(r\) nonzero arrow coefficients on edges that omit at least one cycle edge. Rank \(n\) occurs by choosing two nonzero cycle differences with total sum zero and making all arrow coefficients nonzero: the exceptional cycle event is then absent. Thus the polynomial has degree \(n\), with all coefficients through that degree positive. Finally its constant term gives \(q\), its degree gives \(n\), and its linear coefficient determines \(c\).

## Verification
The included standalone program `verify.py` builds each algebra's multiplication table from primitive vertex idempotents and arrows, computes every commutator matrix directly from products, and performs Gaussian elimination over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\). It tests 13 quivers with \(3\le n\le5\), including multiple orientations, different branch attachments, pure cycles, and characteristic-two extension-field arithmetic. All 13 complete enumerations match the claimed coefficients and recover \(q\), \(n\), and \(c\) from rank-zero and rank-one counts. Run `python verify.py`; the expected last line is `VERIFY_OK_UNICYCLIC 13`.

These exhaustive checks are finite sanity checks, not a proof for unbounded \(n\) or all prime powers. The preceding incidence and additive-character arguments establish those universal cases.

## Relationship to prior work
Jonsson studies left, right, and two-sided bimodule cells for radical-square-zero cyclic Nakayama algebras. This establishes the cyclic-algebra setting but does not enumerate inner-derivation ranks or element-centralizer dimensions over finite fields. Sánchez-Flores studies outer derivations and first Hochschild cohomology for monomial algebras, including the familiar incidence-differential rank \(n-1\) in the connected case; this is distinct from the distribution of the rank of \(\operatorname{ad}_a\) as \(a\) varies. Commuting-pair probabilities provide a single weighted sum \(q^{-2n}R_{Q,q}(q^{-1})\), not the entire coefficient distribution. No originality is claimed for signed incidence-rank identities, additive-character orthogonality, or that weighted-average specialization.

## Limitations
The result does not handle graphs with two or more independent cycles, loops, or parallel arrows, and does not reconstruct the tree attachment pattern or individual centralizer subalgebras. It is a labeled-element count, not a classification up to algebra automorphism. Broader enumeration identities could imply the polynomial; publication-priority assessment is necessarily provisional.

## References
1. Helena Jonsson, *Cell Structure of Bimodules over Radical Square Zero Nakayama Algebras*, arXiv:1804.07082, first public version 2018-04-19. https://arxiv.org/abs/1804.07082
2. Selene Sánchez-Flores, *On the semisimplicity of the outer derivations of monomial algebras*, arXiv:1004.2820, 2010. https://arxiv.org/abs/1004.2820
