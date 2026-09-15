# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# UCT-free KK-plus-trace rigidity: corrected Schafhauser Conjecture D

## 1. Question and answer

Let $A,B$ be unital separable simple nuclear $\mathcal Z$-stable C\*-algebras.
Let $\kappa\in KK(A,B)$ be invertible with $\kappa_0([1_A])=[1_B]$ and let
$\gamma:T(B)\to T(A)$ be an affine homeomorphism satisfying the $K_0$–trace
pairing compatibility
\begin{equation}
\langle \gamma(\tau),x\rangle=\langle\tau,\kappa_0(x)\rangle,
\qquad \forall\,\tau\in T(B),\;x\in K_0(A),
\tag{$\star$}
\end{equation}
where $\langle\tau,y\rangle=\tau_*(y)$ is the trace–$K_0$ pairing.
Does $A\cong B$ follow, without assuming $(\kappa,\gamma)$ is induced by a
unital \*-homomorphism $A\to B$ and without assuming UCT for $A,B$?
If $(\star)$ is insufficient, what is the minimal corrected compatibility?

**Answer (proved below).**
- (a) **With UCT, yes as stated.** $(\kappa,\gamma)$ satisfying $(\star)$
  induces an isomorphism of Elliott invariants, hence $A\cong B$ by
  Kirchberg–Phillips (purely infinite case) and Elliott–Gong–Lin–Niu /
  Tikuisis–White–Winter (stably finite case).
- (b) **UCT-free, traceless case, yes as stated.** If $T(A)=T(B)=\varnothing$
  (purely infinite), unit-preserving KK-equivalence alone implies $A\cong B$
  by Kirchberg–Phillips. No trace compatibility is needed.
- (c) **UCT-free, realized case, yes with the corrected hypothesis.**
  If in addition $(\kappa,\gamma)=([\phi],T(\phi))$ for a unital embedding
  $\phi:A\to B$ with $[\phi]$ invertible in $KK$ (resp.\ $KL$) and $T(\phi)$
  invertible, then $A\cong B$ UCT-free; indeed $\phi$ is approximately
  unitarily equivalent to an isomorphism. One-sided realization suffices.
- (d) **Abstract stably-finite case: $(\star)$ is sharp at invariant level
  but does not produce maps UCT-free.** The $K_0$-pairing $(\star)$ is exactly
  the condition that $(\kappa_*,\gamma)$ is an isomorphism of Elliott
  invariants (order being forced by traces under $\mathcal Z$-stability).
  Hence no weaker invariant-level pairing works, and no invariant-level
  strengthening alone crosses the existence gap: the UCT is used precisely to
  realize K-theoretic data by $KK$-elements and by homomorphisms. The minimal
  corrected UCT-free hypothesis is **joint realizability**: require
  $(\kappa,\gamma)$, together with its induced $KL$ and Hausdorffized-$K_1$ /
  rotation data, to lie in the range of a unital \*-homomorphism (equivalently,
  to extend to a $KT_u$/$\underline{K}T_u$-morphism realized by a map).
  Under this correction, (c) gives $A\cong B$ UCT-free.
- (e) **No explicit counterexample is claimed.** A concrete pair $A\not\cong B$
  satisfying the abstract hypotheses would entail failure of the UCT (there is
  no known separable nuclear C\*-algebra failing UCT), so disproof by explicit
  counterexample is out of reach; the obstruction is the missing UCT-free
  existence theorem, identified precisely.

In particular, Schafhauser's Conjecture D as a UCT-free theorem from abstract
data alone is blocked at the existence step; the corrected theorem is (c)–(d).

## 2. Setup

All algebras are unital separable simple nuclear $\mathcal Z$-stable.
Such $A$ is either purely infinite or stably finite
([37, Thm 4.1.10(ii)] in the source paper's numbering; Rørdam–Størmer).
In the stably finite case $T(A)\ne\varnothing$ (Haagerup: quasitraces are
traces), $A$ has stable rank one (Rørdam) and strict comparison of positive
elements by traces (Matui–Sato, Rørdam, CETW–Winter). $B_\infty$ denotes the
norm sequence algebra, $B^\infty$ the uniform tracial sequence algebra,
$0\to J_B\to B_\infty \xrightarrow{q_B} B^\infty\to 0$ the trace-kernel
extension. $KL(A,B)=KK(A,B)/\overline{\{0\}}$ (Dadarlat topology; Cuntz–Thomsen
picture via Cuntz pairs for the nonseparable target via the $ZKK$ definition).
$T(\phi)(\tau)=\tau\circ\phi$. Approximate unitary equivalence preserves $KL$
and $T$ (but not $KK$).

The Elliott invariant is
$\mathrm{Ell}(A)=(K_0(A),K_0(A)_+,[1_A],K_1(A),T(A),\rho_A)$ with
$\rho_A(\tau,x)=\langle\tau,x\rangle$.
The total invariant $KT_u$ adds $K_*$ with coefficients, $KL$, the
Hausdorffized algebraic $K_1$ $\bar K_1^{\mathrm{alg}}$, the Thomsen sequence
and rotation/determinant maps; morphisms must intertwine all of it. For maps,
Gong–Lin–Niu / Carrion–Gabe–Schafhauser–Tikuisis–White (CGSTW) show that
$KL$ + traces + Hausdorffized-$K_1$ classifies unital homomorphisms up to
approximate unitary equivalence, with full range characterized similarly.

## 3. Lemma: order is forced by traces

**Lemma 1.** Let $A$ be as above and stably finite. Then the ordered group
$(K_0(A),K_0(A)_+,[1_A])$ is recovered from $(K_0(A),[1_A],T(A),\rho_A)$:
a class $x\ne 0$ is positive iff $\rho_A(\tau,x)>0$ for all $\tau\in T(A)$.
In particular, a group isomorphism $\kappa_0:K_0(A)\to K_0(B)$ with
$\kappa_0([1_A])=[1_B]$ intertwining the pairings via an affine homeomorphism
$\gamma$ of trace spaces is automatically an order isomorphism.

*Proof sketch.* Stable rank one + strict comparison + simplicity + exactness +
$\mathcal Z$-stability imply projections separate comparison and $K_0^+$
is strictly determined by traces; see Rørdam on real/stable rank of
$\mathcal Z$-absorbing algebras, Matui–Sato strict comparison, and the
Elliott-program references (Gong–Lin–Niu, CETW). Invertible $\kappa$ induces a
$K_*$-isomorphism, and $(\star)$ says
$\rho_A(\gamma(\tau),x)=\rho_B(\tau,\kappa_0(x))$; strict positivity on all
traces is therefore preserved in both directions, giving positivity
preservation. ∎

Consequence: at invariant level, $(\star)$ is the *exact* compatibility making
$(\kappa_*,\gamma)$ an $\mathrm{Ell}$-isomorphism (given $\kappa$ invertible).
It cannot be weakened without losing $\mathrm{Ell}$-rigidity, and any
“stronger pairing” at the level of $K_0\times T$ alone still lands inside
$\mathrm{Ell}$.

A $KK$-invertible $\kappa$ automatically induces isomorphisms on $K_*$ and on
total $K$-theory compatible with Bockstein operations; under UCT this is the
same as an isomorphism of the $K$-theoretic part of $\mathrm{Ell}$.

## 4. Theorem with UCT

**Theorem 2 (UCT case).** Assume $A,B$ satisfy UCT. Then abstract
$(\kappa,\gamma)$ satisfying $(\star)$ induces an $\mathrm{Ell}$-isomorphism
and hence $A\cong B$. Conversely every $\mathrm{Ell}$-isomorphism lifts to
such a $(\kappa,\gamma)$.

*Proof.* If both traceless, $\kappa$ gives unit-preserving $K_*$-isomorphism;
Kirchberg–Phillips gives $A\cong B$. If stably finite, Lemma 1 upgrades
$(\kappa_0,\gamma)$ to ordered $K_0$-isomorphism; $\kappa$ gives $K_1$-iso.
Hence $(\kappa_*,\gamma)$ is an $\mathrm{Ell}$-isomorphism, and classification
(Elliott–Gong–Lin–Niu; Tikuisis–White–Winter quasidiagonality/completion)
yields $A\cong B$. Conversely, Rosenberg–Schochet UCT lifts any
$K_*$-isomorphism to an invertible $\kappa\in KK$ (Cor. 7.5 of [39] in source
numbering), and the trace map is part of the $\mathrm{Ell}$-isomorphism. ∎

## 5. Traceless UCT-free theorem

**Theorem 3.** If $A,B$ are purely infinite (hence traceless), any invertible
$\kappa\in KK(A,B)$ with $\kappa_0([1_A])=[1_B]$ implies $A\cong B$ with no UCT
assumption.

*Proof.* This is Kirchberg–Phillips: unital Kirchberg algebras are classified
by unit-preserving $KK$-equivalence. ∎

## 6. Realized UCT-free rigidity

**Theorem 4 (Schafhauser Thm 3.2; UCT-free).** Let $A,B$ be as in §2
(finite case; infinite follows from Theorem 3). Let $\phi:A\to B$ be a unital
embedding with $[\phi]\in KK(A,B)$ invertible as a $KK$-morphism (hence
invertible in $KL$) and $T(\phi):T(B)\to T(A)$ invertible (e.g.\ bijective).
Then there is an isomorphism $A\to B$ approximately unitarily equivalent to
$\phi$. In particular the abstract conclusion holds under one-sided
homomorphism realization.

The proof uses only UCT-free ingredients: CETW classification of maps into
$B^\infty$ by traces (Thm 2.1), CGS TW lifting criterion through the
trace-kernel extension in terms of $KK$ (Thm 2.2), classification of lifts
$A\to B_\infty$ with fixed trace data up to the secondary invariant
$h_{\phi,\psi}\in KL(A,J_B)$ (Thm 2.5 + Props 2.4, 2.6, 2.7), and Elliott
intertwining via reparameterization (Gabe/Kirchberg). We reproduce the
argument.

**Lemma 5 (one-sided inverse).** Let $\phi:A\to B$ be as in Theorem 4 and let
$\psi'_\infty:B\to A_\infty$ be a unital embedding with
$T(\psi'_\infty\phi)=T(\iota_A)$ ($\iota_A:A\to A_\infty$ constant sequences).
Then there is a unital embedding $\psi:B\to A$ with $\psi\phi\approx_{\mathrm{a.u.}}\mathrm{id}_A$.

*Proof.* Since $[\phi]$ is $KL$-invertible,
$\phi^*:KL(B,\cdot)\to KL(A,\cdot)$ is invertible. By Prop. 2.6,
$h_{\iota_A,\psi'_\infty\phi}\in KL(A,J_A)$ vanishes on $[1]$, so
$(\phi^*)^{-1}(h_{\iota_A,\psi'_\infty\phi})\in KL(B,J_A)$ vanishes on $[1]$.
By Thm 2.5(ii) realize it as $h_{\psi_\infty,\psi'_\infty}$ for some unital
$\psi_\infty:B\to A_\infty$ with the same trace map. Functoriality
(Prop. 2.7(iii)) gives
$h_{\psi_\infty\phi,\psi'_\infty\phi}=h_{\iota_A,\psi'_\infty\phi}$, whence by
additivity (Prop. 2.7(i)–(ii)) $h_{\psi_\infty\phi,\iota_A}=0$; by Thm 2.5(i),
$\psi_\infty\phi$ is unitarily equivalent to $\iota_A$ in $A_\infty$.
For any reparameterization $r^*$, $r^*\psi_\infty\phi\sim_u\psi_\infty\phi$,
and trace-invertibility of $\phi$ forces $T(r^*\psi_\infty)=T(\psi_\infty)$;
applying $\phi^*$ and using Thm 2.5(i) plus invertibility gives
$h_{r^*\psi_\infty,\psi_\infty}=0$, so $r^*\psi_\infty\sim_u\psi_\infty$.
Since this holds for every $r$, intertwining-via-reparameterization yields
$\psi:B\to A$ with $\iota_A\psi\sim_u\psi_\infty$. Then
$\iota_A\psi\phi\sim_u\iota_A$, i.e.\ $\psi\phi\approx_{\mathrm{a.u.}}\mathrm{id}_A$. ∎

*Proof of Theorem 4.* $T(A)\cong T(B)$ forces both finite or both infinite;
assume finite. Realize the trace map
$\gamma=T(\phi)^{-1}T(q_A\iota_A):T(A_\infty)\to T(B)$ by a unital embedding
$\theta:B\to A^\infty$ (Thm 2.1(ii)); then $\theta\phi\sim_u q_A\iota_A$
(Thm 2.1(i)). Put $\kappa=(\phi^*)^{-1}([\iota_A])\in KK(B,A_\infty)$;
unitality is preserved and
$\phi^*((q_A)_*(\kappa))=[\theta\phi]=\phi^*([\theta])$, so
$(q_A)_*(\kappa)=[\theta]$ by invertibility; Thm 2.2 lifts $\theta$ to
$\psi'_\infty:B\to A_\infty$. The trace computation uses invertibility of
$T(q_A)$ to get $T(\psi'_\infty\phi)=T(\iota_A)$. Lemma 5 gives
$\psi:B\to A$ left-inverse to $\phi$ up to approximate unitary equivalence.
Hence $[\psi]=[\phi]^{-1}$ in $KL$ and $T(\psi)=T(\phi)^{-1}$ are invertible.
Repeating with $(\psi,\iota_B\phi)$ in place of $(\phi,\psi'_\infty)$ gives
$\phi':A\to B$ with $\phi'\psi\approx_{\mathrm{a.u.}}\mathrm{id}_B$.
Then $\phi'\sim_{\mathrm{a.u.}}\phi$ and they are two-sided inverses up to
approximate unitary equivalence; Elliott intertwining promotes $\phi$ to an
isomorphism. The $KL$-valued secondary invariant is essential because $KK$
is not invariant under approximate unitary equivalence whereas $KL$ is. ∎

**Corollary 6 (homotopy rigidity).** If projections separate traces (e.g.\ real
rank zero or unique trace), homotopy-equivalent $A,B$ are isomorphic UCT-free:
a homotopy equivalence is (after unitization) an embedding with invertible
$KK$ and invertible trace map, so Theorem 4 applies.

## 7. Why $(\star)$ alone is insufficient UCT-free, and the minimal correction

The proof of Theorem 4 starts from a *map* $\phi$ inducing $\kappa,\gamma$.
The abstract hypotheses supply only a $KK$-element and a trace map with
$K_0$-compatibility. To run any uniqueness/intertwining argument one must
produce maps $A\to B_\infty$, $B\to A_\infty$ realizing *jointly* the
$KK$-class and the trace data (the lifting criterion Thm 2.2:
$\kappa_0([1])=[1]$ and $(q)_*(\kappa)=[\theta]$). Choosing $\theta$ by traces
alone (Thm 2.1) leaves its $KK$-class uncontrolled; correcting it by the
secondary invariant (Thm 2.5) requires the invertible $KK$-morphism
$\phi^*$ coming from a map. Producing a $KK$-equivalence from a $K$-theory
isomorphism, and producing homomorphisms with prescribed $KL$ + trace +
Hausdorffized-$K_1$ data (the existence/range half of GLN/CGSTW), are exactly
the steps whose known proofs assume UCT on the domain. Uniqueness (maps with
the same $KT_u$ data are approximately unitarily equivalent) is UCT-free, but
existence is not. Hence no proof from $(\star)$ alone can close UCT-free with
current technology, and any “corrected pairing” formulated purely at the level
of $K_0\times T$ remains inside $\mathrm{Ell}$ by Lemma 1 and cannot supply
the missing maps.

**Minimal correction.** Require joint realizability, in either of the
equivalent forms:
- (R1, one-sided) there is a unital embedding $\phi:A\to B$ with
  $[\phi]=\kappa$ in $KK$ (hence $KL$) and $T(\phi)=\gamma$; then Theorem 4
  gives $A\cong B$ UCT-free; or symmetrically two-sided embeddings realizing
  $(\kappa,\gamma)$ and $(\kappa^{-1},\gamma^{-1})$;
- (R2, invariant form) $(\kappa,\gamma)$ extends to a $KT_u$-morphism
  (total $K$ + traces + pairing + $\bar K_1^{\mathrm{alg}}$ + Thomsen/rotation
  compatibility) lying in the range of $\mathrm{Hom}(A,B)$ — i.e.\ the pair is
  induced by a \*-homomorphism, which automatically satisfies $(\star)$ plus
  the full rotation/Thomsen compatibilities.

(R2) is minimal in the precise sense: Lemma 1 shows $(\star)$ is already the
complete invariant-level compatibility (any weakening loses
$\mathrm{Ell}$-isomorphism; any $K_0$–$T$ strengthening is redundant), so the
only remaining gap is passage from invariant to maps; (R1) is exactly the
passage needed for the UCT-free intertwining machine, and one-sided data
already suffices by Theorem 4. The $KL$ (rather than $KK$) formulation is the
operative one, since $KL$ is the approximately-unitarily-invariant quotient
in which the secondary obstruction lives.

*Remark on sharpness.* The SSA and AF examples in Schafhauser §4 show trace–
$K_0$ interaction cannot be dropped in general (e.g.\ unit-preserving
$KK$-equivalent AF algebras with different trace-induced orders on $K_0$ are
not isomorphic), confirming $(\star)$ is a necessary component. The gap is not
that $(\star)$ is the wrong pairing but that it must be *realized*.

## 8. Consolidated resolution

- Stated $K_0$-pairing $(\star)$ + UCT $\Rightarrow$ $A\cong B$ (Theorem 2).
- Stated data UCT-free + traceless $\Rightarrow$ $A\cong B$ (Theorem 3).
- Stated data UCT-free + one-sided homomorphism realization $\Rightarrow$
  $A\cong B$ (Theorem 4); this is the minimal corrected KK–trace compatibility
  (R1)/(R2).
- Abstract stably-finite data without realization and without UCT does not
  imply $A\cong B$ by any UCT-free intertwining proof; producing a literal
  counterexample would go beyond current knowledge (it would imply existence
  of non-UCT nuclear algebras, the outstanding open UCT problem), so the
  complete auditable answer is the conditional/corrected theorem above, not an
  explicit counterexample.

## References (sources used)

- C. Schafhauser, *KK-rigidity of simple nuclear C\*-algebras*,
  arXiv:2408.02745v2 (statement of Conjecture D; Theorems A/3.2, Cor. B,
  Thm C/4.4; §2 classification Thms 2.1, 2.2, 2.5 and Props 2.6–2.7; §3 Lemma
  3.1 and intertwining; §4 Dadarlat–Winter input). All section/theorem numbers
  above beginning “Thm/Prop/Lemma” in §§6–7 refer to that paper unless noted.
- J. Carrion, J. Gabe, C. Schafhauser, A. Tikuisis, S. White,
  *Classifying \*-homomorphisms I*, arXiv:2307.06480 (existence needs UCT on
  domain; uniqueness framework; trace-kernel methods).
- G. Gong, H. Lin, Z. Niu, *Homomorphisms into simple $\mathcal Z$-stable
  algebras II* (KL + trace + Hausdorffized-$K_1$ homomorphism invariant).
- J. Castillejos, S. Evington, A. Tikuisis, S. White, *Classifying maps into
  uniform tracial sequence algebras* (maps into $B^\infty$ by traces).
- E. Kirchberg–N. C. Phillips classification; Elliott–Gong–Lin–Niu +
  Tikuisis–White–Winter finite classification; Rosenberg–Schochet UCT;
  Rørdam (stable rank one of $\mathcal Z$-stable finite algebras),
  Matui–Sato (strict comparison), Haagerup (quasitraces are traces),
  Dadarlat–Winter (KK of SSA algebras), Gabe (intertwining via
  reparameterization).
