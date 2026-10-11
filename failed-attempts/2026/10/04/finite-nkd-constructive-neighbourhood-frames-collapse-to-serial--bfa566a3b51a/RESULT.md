# Finite NKD constructive neighbourhood frames collapse to serial relational cores
## Finding

Let
\[
F=(W,\le,N)
\]
be a constructive neighbourhood frame with finite, nonempty \(W\). Assume that, for every \(w\in W\),

1. \(N(w)\ne\varnothing\);
2. \(N(w)\) is closed under binary intersections;
3. \(U\cap V\ne\varnothing\) for all \(U,V\in N(w)\).

These are the structural conditions used by Dalmonte and de Groot for the modal principles \(N\), \(K\), and \(D\), respectively.

Define the **core neighbourhood**
\[
C_w=\bigcap N(w).
\]
Then \(C_w\) is a nonempty member of \(N(w)\). If
\[
N_{\mathrm c}(w)=\{C_w\},
\]
then for every valuation \(V\), every formula \(\varphi\), and every \(w\in W\),
\[
(W,\le,N,V),w\Vdash\varphi
\quad\Longleftrightarrow\quad
(W,\le,N_{\mathrm c},V),w\Vdash\varphi.
\]

Equivalently, define a binary relation \(R\) by
\[
wRu\quad\Longleftrightarrow\quad u\in C_w.
\]
The relation is serial, and the two modal clauses reduce exactly to
\[
w\Vdash\Box\varphi
\quad\Longleftrightarrow\quad
\forall v\ge w\ \forall u\,(vRu\Rightarrow u\Vdash\varphi),
\]
and
\[
w\Vdash\Diamond\varphi
\quad\Longleftrightarrow\quad
\forall v\ge w\ \exists u\,(vRu\ \text{and}\ u\Vdash\varphi).
\]

Conversely, every serial relation \(R\) on \(W\) determines a principal constructive neighbourhood frame by
\[
N_R(w)=\{R(w)\},
\]
and this frame satisfies the same three structural conditions. Hence, on a fixed labelled \(m\)-world set, the canonical principal cores are in bijection with serial relations and number exactly
\[
(2^m-1)^m.
\]

The finite hypothesis is sharp for this collapse. Let \(W=\mathbb N\) with the equality preorder and, at every world, let
\[
N(w)=\bigl\{\{k,k+1,k+2,\ldots\}:k\in\mathbb N\bigr\}.
\]
This family is nonempty, binary-intersection closed, and pairwise intersecting, but has no least member and total intersection \(\varnothing\). No singleton neighbourhood family can preserve its \(\Box\)-semantics for all valuations.

## Assumptions and scope

The forcing clauses are exactly the constructive neighbourhood clauses of Dalmonte and de Groot:
\[
w\Vdash\Box\varphi
\]
iff for every \(v\ge w\) there exists \(a\in N(v)\) such that every \(u\in a\) forces \(\varphi\), while
\[
w\Vdash\Diamond\varphi
\]
iff for every \(v\ge w\) and every \(a\in N(v)\), some \(u\in a\) forces \(\varphi\).

The theorem concerns frames satisfying the **structural sufficient conditions** associated with \(N\), \(K\), and \(D\). It does not claim that every finite frame that happens to validate those formulas must satisfy these structural conditions.

No antisymmetry assumption is needed: \(\le\) may be any preorder. The \(N\)-condition already makes the frame continual, because every world has a nonempty neighbourhood family.

The count \((2^m-1)^m\) counts labelled canonical principal-core assignments, equivalently labelled serial relations. It does not assert that all such relations have pairwise distinct sets of valid modal formulas.

## Proof

Fix \(w\in W\). Since \(W\) is finite, \(\mathcal P(W)\) is finite, so the nonempty family \(N(w)\subseteq\mathcal P(W)\) is finite. Write
\[
N(w)=\{U_1,\ldots,U_r\}.
\]
Binary-intersection closure implies inductively that
\[
U_1\cap\cdots\cap U_j\in N(w)
\]
for every \(1\le j\le r\). The pairwise-intersection condition applied to
\[
U_1\cap\cdots\cap U_{r-1}
\]
and \(U_r\) shows that
\[
C_w=U_1\cap\cdots\cap U_r\ne\varnothing.
\]
Thus \(C_w\in N(w)\), \(C_w\ne\varnothing\), and \(C_w\subseteq a\) for every \(a\in N(w)\).

Let \(A\subseteq W\). The local existential neighbourhood test satisfies
\[
(\exists a\in N(w))\ a\subseteq A
\quad\Longleftrightarrow\quad
C_w\subseteq A.
\]
The forward implication holds because \(C_w\subseteq a\); the reverse implication holds by choosing \(a=C_w\).

Likewise, the local universal hitting test satisfies
\[
(\forall a\in N(w))\ a\cap A\ne\varnothing
\quad\Longleftrightarrow\quad
C_w\cap A\ne\varnothing.
\]
The forward implication uses \(C_w\in N(w)\). For the reverse implication, any point of \(C_w\cap A\) belongs to every \(a\in N(w)\).

Now induct on formulas. Atomic formulas and intuitionistic connectives are unchanged because the preorder and valuation are unchanged. At a modal step, apply the two displayed local equivalences at every \(v\ge w\), with \(A\) equal to the truth set of the induction hypothesis. This proves truth preservation for both \(\Box\) and \(\Diamond\).

Defining \(vRu\) iff \(u\in C_v\) gives the displayed relational clauses immediately. Seriality follows from \(C_v\ne\varnothing\). Conversely, if \(R\) is serial, then each singleton family \(\{R(v)\}\) is nonempty, binary-intersection closed, and pairwise intersecting.

On a labelled \(m\)-world set, each world independently chooses one nonempty successor set, giving \(2^m-1\) choices at each of \(m\) worlds and therefore
\[
(2^m-1)^m
\]
principal cores.

For the infinite boundary example, every two tails meet and the intersection of two tails is again a tail, but their total intersection is empty. If a singleton core \(\{C\}\) had the same \(\Box\)-test, then every tail \(T_k\) would satisfy \(C\subseteq T_k\). Hence
\[
C\subseteq\bigcap_kT_k=\varnothing,
\]
so \(C=\varnothing\). But the singleton family \(\{\varnothing\}\) makes \(\Box\bot\) true, whereas the tail family does not. Thus no principal replacement preserves the semantics.

## Verification

The proof reduces the modal semantics to two exact set-theoretic equivalences at each world.

The bundled checker exhaustively enumerates every neighbourhood family on carrier sizes \(1\) through \(4\). Whenever a family is nonempty, binary-intersection closed, and pairwise intersecting, it verifies that the total intersection is nonempty, belongs to the family, and gives exactly the same existential-subset and universal-hitting tests on every subset of the carrier. It also confirms that every nonempty subset occurs as the core of a principal admissible family.

The computation is only a consistency check for small carriers. The theorem for all finite carriers follows from the finite-intersection proof above, and the infinite counterexample is proved symbolically rather than by enumeration.

## Relationship to prior work

Dalmonte and de Groot introduce the constructive neighbourhood semantics used here and study the extensions of intuitionistic monotone modal logic by \(N\), \(P\), \(T\), \(D\), and \(K\). Their Lemma 2.4 associates \(N\) with nonempty neighbourhood families, \(D\) with pairwise nonempty intersections, and \(K\) with binary-intersection closure. They also explicitly include \(\mathrm{IM}\oplus N\oplus K\oplus D\) among the systems treated by their semantic and proof-theoretic framework.

The paper does not state the finite principal-core collapse, the serial relational reduction of both modal clauses, the \((2^m-1)^m\) canonical-core census, or the tail-family obstruction showing why the same reduction fails on infinite carriers. Its canonical semantics remains genuinely neighbourhood-based.

Classical normal neighbourhood semantics has a well-known relationship with relational semantics when neighbourhood systems are principal filters. That background makes the set-theoretic mechanism natural, but it does not by itself give the present two-modality constructive forcing equivalence, where \(\Box\) uses an existential neighbourhood witness, \(\Diamond\) uses a universal hitting condition, and both clauses quantify over all intuitionistic future worlds.

## Limitations

The result is a finite-frame semantic reduction, not a finite-model-property theorem for \(\mathrm{IM}\oplus N\oplus K\oplus D\). It does not show that every non-theorem has a finite countermodel.

The principal-core count is a count of canonical serial relations before quotienting by modal equivalence or world isomorphism. Different cores may validate the same formulas.

Finiteness cannot simply be dropped: binary-intersection closure guarantees only finite intersections, and an infinite neighbourhood family can have no least member.

## References

[1] Tiziano Dalmonte and Jim de Groot, “Intuitionistic Monotone Modal Logic: Proof Theory and Semantics,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 278–298. arXiv:2606.31870. DOI:10.4204/EPTCS.447.16.

[2] Jim de Groot, “Intuitionistic monotone modal logic via translation,” *Journal of Logic and Computation* 36(4) (2026), exag017. arXiv:2507.13746. DOI:10.1093/logcom/exag017.
