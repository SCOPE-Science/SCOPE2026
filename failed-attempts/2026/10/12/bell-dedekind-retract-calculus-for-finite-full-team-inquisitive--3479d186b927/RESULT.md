# Bell–Dedekind retract calculus for finite full-team inquisitive and dependence algebras

## Finding
Let \(W\) and \(V\) be finite nonempty sets, and let \(\mathcal I(W)\) be the algebra of all nonempty downward-closed collections of teams \(T\subseteq W\), equipped with its designated core of principal downsets. For the usual inquisitive signature \((\wedge,\vee,\to,\bot)\), and also for the dependence expansion by tensor \(\otimes\), **every core-preserving homomorphism** \(\mathcal I(W)\to\mathcal I(V)\) is uniquely of the form
\[
H_f(A)=\{T\subseteq V:f[T]\in A\},\qquad f:V\longrightarrow W.
\]
Consequently \(|\operatorname{Hom}(\mathcal I(W),\mathcal I(V))|=|W|^{|V|}\) and \(\operatorname{End}(\mathcal I(W))\) is the opposite of the full transformation monoid on \(W\). The extra, concrete conclusion concerns its **retract-image geometry**. For \(|W|=n\ge1\), the collection of retract subalgebras of \(\mathcal I(W)\), ordered by inclusion, is **anti-isomorphic to the partition lattice** \(\Pi_n\). Hence there are exactly \(B_n\) distinct retract subalgebras, with precisely \(\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) retracts of cardinality \(D_k-1\), where \(D_k\) denotes the \(k\)-th Dedekind number (the number of antichains of a \(k\)-point Boolean lattice). All these conclusions are identical in the inquisitive and dependence signatures.

More explicitly, the full endomorphism rank polynomial and retract rank polynomial are
\[
\sum_{h\in\operatorname{End}(\mathcal I(W))}z^{|h[\mathcal I(W)]|}
 =\sum_{k=1}^{n}\binom nk k!\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}z^{D_k-1},
\qquad
\sum_{E\text{ retract of }\mathcal I(W)}z^{|E|}
 =\sum_{k=1}^{n}\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}z^{D_k-1}.
\]
There are \(\sum_{k=1}^n\binom nk k^{n-k}\) idempotent endomorphisms and \(n!\) automorphisms. For \(n=3\), the \(19\)-element algebra has \(27\) endomorphisms, \(10\) idempotent endomorphisms, and \(5\) distinct retract subalgebras; its endomorphism rank polynomial is \(3z^2+18z^5+6z^{19}\). For \(n=4\), the corresponding figures are \(167,256,41,15\), with polynomial \(4z^2+84z^5+144z^{19}+24z^{167}\).

## Assumptions and scope
A team is any subset of a finite nonempty set \(W\). Write \(\downarrow S=\{T\subseteq W:T\subseteq S\}\), and define
\[
\mathcal I(W)=\{A\subseteq\mathcal P(W):\varnothing\in A,\ (S\subseteq T\in A\implies S\in A)\},
\qquad C(W)=\{\downarrow S:S\subseteq W\}.
\]
Here \(\varnothing\) is the empty *team*, and \(A\) is a nonempty downset of teams; the empty family is excluded. The algebra has \(A\wedge B=A\cap B\), \(A\vee B=A\cup B\), \(\bot=\{\varnothing\}\), and
\[
A\to B=\{T\subseteq W:\forall S\subseteq T\ (S\in A\Rightarrow S\in B)\}.
\]
Its dependence expansion additionally has
\[
A\otimes B=\downarrow\{S\cup T:S\in A,\ T\in B\},
\]
where the outer downward arrow means downward closure in the team-inclusion ordering. The designated core \(C(W)\) is a Boolean algebra under its inherited \(\wedge,\to,\bot\); a homomorphism here must map \(C(W)\) into \(C(V)\), in addition to preserving the specified operations. These are the discrete-frame instances of finite, well-connected, core-generated inquisitive/dependence algebras; the theorem does **not** concern arbitrary finite Heyting algebras, arbitrary poset frames, or homomorphisms that disregard the core predicate.

We use \(D_0=2,D_1=3,D_2=6,D_3=20,D_4=168\), so \(|\mathcal I(W)|=D_n-1\). Write \(\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) for a Stirling number of the second kind and \(B_n\) for the Bell number. Partition order uses refinement: \(P\le Q\) means every block of \(P\) lies inside one block of \(Q\).

## Proof
**1. The core forces a unique world map.** For \(U,S\subseteq W\), the inherited core operations satisfy
\[
\downarrow U\wedge\downarrow S=\downarrow(U\cap S),\qquad
(\downarrow U)\to(\downarrow S)=\downarrow((W\setminus U)\cup S).
\]
Thus a core-preserving inquisitive homomorphism \(h\) restricts to a homomorphism of finite Boolean algebras \(\mathcal P(W)\to\mathcal P(V)\), since the Boolean join and complement are definable using implication and bottom in the core. Each such Boolean homomorphism is uniquely inverse image along a total function \(f:V\to W\). Hence \(h(\downarrow S)=\downarrow f^{-1}[S]\). Every \(A\in\mathcal I(W)\) is a finite union of its principal downsets: \(A=\bigcup_{S\in A}\downarrow S\). Preservation of \(\vee\) forces
\[
h(A)=\bigcup_{S\in A}\downarrow f^{-1}[S]
   =\{T\subseteq V:f[T]\in A\}=H_f(A).
\]
The middle equality follows because \(T\subseteq f^{-1}[S]\) is equivalent to \(f[T]\subseteq S\), and \(A\) is downward closed. Therefore there are no other maps.

**2. All induced maps preserve every operation.** Direct inverse image under \(T\mapsto f[T]\) preserves arbitrary unions, intersections, and \(\bot\). For implication, the key finite lifting fact is
\[
\{f[R]:R\subseteq T\}=\mathcal P(f[T]);
\]
every subset of \(f[T]\) can be realized by selecting representatives from the appropriate fibers inside \(T\). It follows that \(f[T]\in A\to B\) if and only if \(T\in H_f(A)\to H_f(B)\). For tensor, if \(f[T]\subseteq S\cup U\) for \(S\in A,U\in B\), take \(T_1=\{t\in T:f(t)\in S\}\) and \(T_2=\{t\in T:f(t)\in U\}\). Then \(T=T_1\cup T_2\), \(f[T_1]\in A\), and \(f[T_2]\in B\); the converse follows from images of unions. Hence \(H_f(A\otimes B)=H_f(A)\otimes H_f(B)\). Core preservation is \(H_f(\downarrow S)=\downarrow f^{-1}[S]\).

**3. Endomorphism monoid and ranks.** For endomorphisms, \(H_f\circ H_g=H_{g\circ f}\), so the monoid is anti-isomorphic to the full transformation monoid \(W^W\). A map \(f\) with exactly \(k\) image points factors through its \(k\)-block kernel quotient. Its induced algebra map has the same image as the injective embedding of the full-team algebra on that \(k\)-point quotient. Thus the image is isomorphic to \(\mathcal I(\{1,\ldots,k\})\), with \(D_k-1\) elements. There are \(\binom nk k!\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) transformations of rank \(k\), proving the endomorphism rank polynomial.

**4. Image inclusions encode precisely kernel refinements.** For a partition \(P\in\Pi_n\), let \(E_P\) be the endomorphism image \(H_f[\mathcal I(W)]\) of any \(f:W\to W\) with \(\ker f=P\). This is well-defined because the induced \(H_f(A)\) depends on \(f\) only through which partition blocks a team meets, up to an injective relabeling of those blocks. Its core elements are exactly the principal families \(\downarrow U\) for \(U\) a union of \(P\)-blocks. Indeed \(H_f(\downarrow S)=\downarrow f^{-1}[S]\) gives all such principal families, and if \(H_f(A)=\downarrow U\), then membership of singleton teams depends only on the \(f\)-value, forcing \(U\) to be a union of fibers. This recovers \(P\) intrinsically from \(E_P\), so distinct partitions have distinct images.

If \(P\) refines \(Q\), any downset depending only on \(Q\)-blocks also depends only on \(P\)-blocks, giving \(E_Q\subseteq E_P\). Conversely, if \(E_Q\subseteq E_P\), then \(C(W)\cap E_Q\subseteq C(W)\cap E_P\); every \(Q\)-block is therefore a union of \(P\)-blocks, so \(P\) refines \(Q\). This proves the order-reversing bijection \(\Pi_n\to\{E_P\}\).

**5. Every endomorphic image is a retract.** Given partition \(P\), choose one representative in each block and define \(e:W\to W\) to send all points of that block to its representative. Then \(e^2=e\) and \(\ker(e)=P\). Consequently \(H_e\) is idempotent, and \(E_P=H_e[\mathcal I(W)]\) is a retract subalgebra. Conversely every retract image is the image of its idempotent retraction, necessarily some \(H_f\), so every retract is some \(E_P\). There are \(B_n\) such images, with \(\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) of size \(D_k-1\). Idempotent functions on an \(n\)-point set with \(k\) fixed points are counted by \(\binom nk k^{n-k}\), proving the idempotent formula. The bijections are the \(n!\) automorphisms.

## Verification
The standalone file `verify_team.py` enumerates the nonempty Boolean-lattice downsets for \(1\le n\le4\), independently evaluates implication and tensor, and reconstructs every map \(H_f\). It operation-checks all \(56\) cross-size maps for source and target set sizes through \(3\), exhaustively screens all \(5^5=3125\) set maps on the smallest nontrivial \(5\)-element algebra for core-preserving operations, and evaluates all \(n^n\) endomorphisms and their distinct image posets through \(n=4\). It returns `VERIFY_OK 58536 assertions; 56 constructed cross-size homomorphisms; 3125 scalar set maps screened`. The general theorem rests on the preceding proof, not on extrapolating finite checks.

## Relationship to prior work
Quadrellaro's *On Intermediate Inquisitive and Dependence Logics: An Algebraic Study* (first publicly posted April 2, 2021) establishes the finite downset-core representation (Section 4, especially Propositions 4.4–4.10), an abstract categorical equivalence (Theorem 4.11), and the corresponding dependence framework. Those representation and duality results are **prior art**, not claimed as discoveries here. In particular, the world-function normal form can be viewed as the discrete-frame specialization of that duality; the general transformation monoid and elementary Bell/Stirling/Dedekind number formulas are known objects. The proposed additional classification is the concrete internal **partition-indexed lattice of retract subalgebras**, with its precise Dedekind-cardinality rank grading, and the simultaneous explicit operation-level identification for both signatures. The cited primary text contains no treatment of retracts, endomorphism spectra, Bell numbers, partition lattices, or Dedekind-graded image subalgebras. The earlier inquisitive-extension construction of Bezhanishvili–Grilletti–Holliday (2019) supplies foundational algebraic semantics. The accessible full text of Bezhanishvili–Grilletti–Quadrellaro (2020 preprint) studies DNA-logics, algebraic varieties, and the inquisitive hierarchy; it does not classify these endomorphic images. Neither comparison is a substitute for the present source’s strong categorical duality. The entire result is elementary relative to that substantial prior structure, and no priority claim can eliminate the possibility of uncatalogued folklore or an unindexed calculation.

## Limitations
The theorem applies to finite nonempty **discrete-frame**, **core-preserving** inquisitive/dependence algebras only; forgetting the designated core can admit more homomorphisms, so the formulas cannot be asserted for plain Heyting endomorphisms. The equivalence with the duality paper has been checked in its finite representation setting, but formal independent peer review of the new retract classification has not been performed. The finite verifier covers the enumerated sizes; the proof supplies the arbitrary finite case. The originality comparison is not an exhaustive search of unpublished notes, theses, or every possible categorical folklore formulation.

## References
- D. E. Quadrellaro, *On Intermediate Inquisitive and Dependence Logics: An Algebraic Study*, arXiv:2104.00981 (initial version 2021-04-02), *Annals of Pure and Applied Logic* **173** (2022), 103143, DOI:10.1016/j.apal.2022.103143. Primary source: https://arxiv.org/pdf/2104.00981 .
- N. Bezhanishvili, G. Grilletti, W. H. Holliday, *Algebraic and Topological Semantics for Inquisitive Logic via Choice-Free Duality*, WoLLIC 2019, Lecture Notes in Computer Science **11541**, 35–52, DOI:10.1007/978-3-662-59533-6_3.
- N. Bezhanishvili, G. Grilletti, D. E. Quadrellaro, *An Algebraic Approach to Inquisitive and DNA-Logics*, ILLC Preprint PP-2020-10, deposited 2020-05-01, https://eprints.illc.uva.nl/id/eprint/1739/1/Paper.pdf ; subsequently *Review of Symbolic Logic* **15** (2022), 950–990.
- Standard combinatorial sequences: Dedekind numbers, Stirling numbers of the second kind, and Bell numbers; their well-established enumerative meanings are used, not claimed as new.
