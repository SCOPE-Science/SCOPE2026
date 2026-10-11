# Exact finite discrete-base normal forms for modal cover semantics
## Finding

Valliappan's modal cover semantics replaces a binary accessibility relation by a relation
\[
\blacktriangleleft\ \subseteq W\times\mathcal P(W),
\]
so that a modality holds at \(w\) when some modal cover of \(w\) is contained in the truth set of its argument.

On the canonical finite **discrete cover base**, this semantics has four exact normal forms.

Let \(W\) be an \(n\)-element set. Give \(W\) equality as its refinement relation and take the local covering relation to consist only of
\[
w\triangleleft\{w\}.
\]
For any modal covering relation, define its induced set operator
\[
\mu(X)
=
\left\{
w\in W:
\exists\beta\subseteq W\;
\bigl(w\blacktriangleleft\beta\ \text{and}\ \beta\subseteq X\bigr)
\right\}.
\]

Two modal covering relations will be called semantically equivalent when they induce the same operator \(\mu\).

Then the semantic equivalence classes are exactly as follows.

For constructive monotone modal logic CM,
\[
\boxed{
\#\mathrm{CM}(W)=M_n^n,
}
\]
where \(M_n\) is the \(n\)-th Dedekind number, equivalently the number of monotone Boolean functions of \(n\) variables.

For minimal lax logic SL,
\[
\boxed{
\#\mathrm{SL}(W)=3^n.
}
\]
Every operator has the unique form
\[
\mu(X)=T\cup(I\cap X),
\]
where
\[
W=F\sqcup I\sqcup T
\]
is an ordered partition into worlds where the modality is respectively always false, identical to the input, or always true.

For propositional lax logic PLL,
\[
\boxed{
\#\mathrm{PLL}(W)=2^n.
}
\]
Every operator has the unique form
\[
\mu(X)=X\cup C
\]
for a subset
\[
C\subseteq W.
\]

For the box-only logic \(\mathrm{CK}_{\Box}\),
\[
\boxed{
\#\mathrm{CK}_{\Box}(W)=2^{n^2}.
}
\]
Every finite modal-cover operator is exactly a standard Kripke-box operator:
\[
\mu(X)
=
\{w\in W:K_w\subseteq X\}
\]
for a unique family
\[
(K_w)_{w\in W},
\qquad
K_w\subseteq W.
\]

Equivalently, defining
\[
wRv
\quad\Longleftrightarrow\quad
v\in K_w,
\]
gives
\[
\mu(X)
=
\{w:R(w)\subseteq X\}.
\]

Thus, over a finite discrete intuitionistic base, modal cover semantics has a sharp four-way hierarchy:

\[
\mathrm{CM}:
\text{arbitrary monotone set maps},
\]
\[
\mathrm{SL}:
\text{three pointwise behaviors},
\]
\[
\mathrm{PLL}:
\text{adjoin one fixed subset},
\]
\[
\mathrm{CK}_{\Box}:
\text{ordinary Kripke boxes}.
\]

## Assumptions and scope

The discrete cover base is
\[
(W,=,\triangleleft),
\qquad
w\triangleleft\{w\}
\]
and no other local covers.

This is a legitimate cover system under the source definitions. Its localized up-sets are all subsets of \(W\), so its associated Heyting algebra is the Boolean algebra
\[
\mathcal P(W).
\]

The theorem classifies modal covering relations only up to equality of their induced operator
\[
\mu:\mathcal P(W)\to\mathcal P(W).
\]
Raw modal covering relations can contain redundant covers and therefore need not be unique.

The CM, SL, PLL, and \(\mathrm{CK}_{\Box}\) conditions are exactly the modal conditions imposed in the source paper:

- CM uses modal refinement and modal localization;
- SL additionally uses modal inclusion;
- PLL additionally uses modal identity and modal transitivity;
- \(\mathrm{CK}_{\Box}\) additionally uses modal seriality and modal confluence.

The finite hypothesis is needed only for the \(\mathrm{CK}_{\Box}\) least-cover argument and for the finite counts. The CM, SL, and PLL pointwise normal forms remain valid on arbitrary discrete sets if the cardinal enumerations are omitted.

## Proof

On the equality preorder, refinement of subsets reverses ordinary inclusion:
\[
\alpha\preceq\alpha'
\quad\Longleftrightarrow\quad
\alpha'\subseteq\alpha.
\]

Also, because the only local cover of \(w\) is \(\{w\}\),
\[
\langle\triangleleft\rangle X=X.
\]

The usual modal refinement and localization conditions are automatic on this base. Modal refinement is witnessed by the same cover, because the only refinement of a world is itself. Modal localization says that if
\[
w\in\langle\blacktriangleleft\rangle X,
\]
then \(w\) has a modal cover contained in
\[
\langle\triangleleft\rangle X=X,
\]
which is exactly the premise.

### CM

For each world \(w\), let
\[
\mathcal C_w
=
\{\beta\subseteq W:w\blacktriangleleft\beta\}.
\]
Then
\[
w\in\mu(X)
\quad\Longleftrightarrow\quad
\exists\beta\in\mathcal C_w\; \beta\subseteq X.
\]

Hence
\[
\mathcal N_w
=
\{X\subseteq W:w\in\mu(X)\}
\]
is an upset of the Boolean lattice
\[
(\mathcal P(W),\subseteq).
\]

Conversely, every upset \(\mathcal N_w\) is obtained this way by taking
\[
\mathcal C_w=\mathcal N_w.
\]
Indeed, if \(X\in\mathcal N_w\), choose \(\beta=X\); and if some
\[
\beta\in\mathcal N_w
\]
satisfies
\[
\beta\subseteq X,
\]
upward closure gives
\[
X\in\mathcal N_w.
\]

For finite \(W\), every upset has a unique antichain of minimal members. Thus every CM behavior at one world has a unique irredundant family of minimal modal covers.

The number of upsets of the \(n\)-element Boolean lattice is the Dedekind number
\[
M_n.
\]
The choices at distinct worlds are independent, so the number of global operators is
\[
M_n^n.
\]

Equivalently, CM realizes every monotone map
\[
\mathcal P(W)\to\mathcal P(W),
\]
because each output coordinate is an arbitrary monotone Boolean function.

### SL

SL adds modal inclusion:
\[
w\blacktriangleleft\alpha
\quad\Longrightarrow\quad
\{w\}\preceq\alpha.
\]

On the equality preorder,
\[
\{w\}\preceq\alpha
\quad\Longleftrightarrow\quad
\alpha\subseteq\{w\}.
\]

Therefore the only possible modal covers of \(w\) are
\[
\varnothing
\quad\text{and}\quad
\{w\}.
\]

There are three semantically distinct cases.

If there is no modal cover at \(w\), then
\[
w\notin\mu(X)
\]
for every \(X\).

If \(\{w\}\) is a cover but \(\varnothing\) is not, then
\[
w\in\mu(X)
\quad\Longleftrightarrow\quad
w\in X.
\]

If \(\varnothing\) is a modal cover, then
\[
w\in\mu(X)
\]
for every \(X\), independently of whether \(\{w\}\) is also listed.

Thus every world has exactly one of three semantic types:
\[
F,\ I,\ T.
\]
The resulting operator is
\[
\mu(X)=T\cup(I\cap X),
\]
and the ordered partition is recovered uniquely from the operator by evaluating it at
\[
\varnothing,\ \{w\}.
\]

Hence there are
\[
3^n
\]
SL operators.

### PLL

PLL is an SL model satisfying modal identity
\[
w\blacktriangleleft\{w\}
\]
and modal transitivity.

Modal identity eliminates the always-false SL type. Therefore at each world only two semantic behaviors remain:

\[
w\in\mu(X)
\quad\Longleftrightarrow\quad
w\in X,
\]
or
\[
w\in\mu(X)
\quad\text{for all }X.
\]

The possible raw cover families are
\[
\{\{w\}\}
\]
and
\[
\{\varnothing,\{w\}\}.
\]
Both satisfy modal transitivity. For the singleton cover, transitivity reproduces the singleton. For the empty cover, the premise is vacuous and the required union is empty.

Let
\[
C
=
\{w:w\blacktriangleleft\varnothing\}.
\]
Then
\[
\mu(X)=X\cup C.
\]

Conversely every
\[
C\subseteq W
\]
defines a PLL modal covering relation by taking \(\{w\}\) as a cover at every world and adding \(\varnothing\) exactly at the worlds of \(C\).

Thus there are
\[
2^n
\]
PLL operators.

### \(\mathrm{CK}_{\Box}\)

For \(\mathrm{CK}_{\Box}\), modal seriality says that each family
\[
\mathcal C_w
\]
is nonempty.

Modal confluence says that for every
\[
\alpha,\beta\in\mathcal C_w,
\]
there is
\[
\gamma\in\mathcal C_w
\]
with
\[
\alpha\preceq\gamma\succeq\beta.
\]

On the equality preorder this is exactly
\[
\gamma\subseteq\alpha\cap\beta.
\]

Because \(W\) is finite, \(\mathcal P(W)\) is finite, so \(\mathcal C_w\) is finite. Repeated confluence therefore produces a member
\[
\delta\in\mathcal C_w
\]
contained in every modal cover of \(w\).

Put
\[
K_w
=
\bigcap\mathcal C_w.
\]
Then
\[
\delta\subseteq K_w
\]
by construction, while
\[
K_w\subseteq\delta
\]
because \(K_w\) is the intersection of all covers. Hence
\[
K_w=\delta\in\mathcal C_w.
\]

So \(K_w\) is the least modal cover of \(w\).

It follows that
\[
w\in\mu(X)
\]
iff some cover of \(w\) is contained in \(X\), which holds iff the least cover satisfies
\[
K_w\subseteq X.
\]

Thus
\[
\mu(X)
=
\{w:K_w\subseteq X\}.
\]

Conversely, any family
\[
(K_w)_{w\in W}
\]
defines a valid \(\mathrm{CK}_{\Box}\) modal covering relation by taking the single modal cover \(K_w\) at \(w\). Seriality and confluence are immediate.

There are
\[
2^n
\]
choices for each \(K_w\), independently for \(n\) worlds, so there are exactly
\[
2^{n^2}
\]
operators.

The family \((K_w)\) is equivalent to an arbitrary binary relation
\[
R\subseteq W\times W,
\]
with
\[
R(w)=K_w.
\]
Therefore finite discrete-base \(\mathrm{CK}_{\Box}\) modal cover semantics collapses exactly to ordinary Kripke-box semantics.

## Verification

The bundled checker performs independent finite replays.

For
\[
1\le n\le4,
\]
it enumerates every antichain of
\[
\mathcal P(W)
\]
and obtains the Dedekind counts
\[
3,\ 6,\ 20,\ 168.
\]

For
\[
1\le n\le3,
\]
it enumerates every raw family of modal covers at one world. It computes the induced semantic upset and verifies that the number of distinct CM behaviors is exactly
\[
M_n.
\]

For every world in those carriers, it checks that modal inclusion leaves exactly three SL behaviors and modal identity leaves exactly two PLL behaviors.

For \(\mathrm{CK}_{\Box}\), the checker enumerates every nonempty raw cover family through
\[
n=3,
\]
filters by modal confluence, proves computationally that the total intersection is itself a cover, and verifies that the induced operator is determined exactly by this least cover. The number of distinct local behaviors is
\[
2^n.
\]

The global counts then follow from independence of the world coordinates.

The script prints `VERIFY_OK`.

## Relationship to prior work

Valliappan introduces modal cover semantics in 2026 as a constructive generalization of relational cover semantics. The primary paper explicitly defines the modal-cover operator
\[
\langle\blacktriangleleft\rangle X
=
\{w:\exists\alpha\; w\blacktriangleleft\alpha\subseteq X\},
\]
shows that CM yields arbitrary monotone modal Heyting operators, adds modal inclusion for SL, modal identity and transitivity for PLL, and modal seriality and confluence for \(\mathrm{CK}_{\Box}\).

The checked full text does not specialize the framework to a finite discrete cover base. It contains no Dedekind-number enumeration, no three-state SL normal form, no fixed-subset PLL normal form, and no least-cover or Kripke-collapse theorem for finite \(\mathrm{CK}_{\Box}\) modal covers.

The CM count uses the classical identification of the Dedekind number \(M_n\) with the number of monotone Boolean functions, equivalently antichains of the Boolean lattice. That enumerative fact is background. The new content is the exact reduction of finite discrete modal-cover semantics to those objects, together with the simultaneous normal forms for the three stronger modal systems.

The \(\mathrm{CK}_{\Box}\) collapse is consistent with the standard fact that finite-meet-preserving normal operators on a finite powerset algebra admit relational representations. Here it is proved directly from the source's modal seriality and confluence conditions, producing the least cover explicitly.

Targeted searches for discrete modal-cover systems, Dedekind counts, finite CM/SL/PLL classifications, and finite \(\mathrm{CK}_{\Box}\) least-cover collapses did not locate an equivalent result.

## Limitations

The theorem concerns the discrete local cover base. Nontrivial refinement or local-cover structure can couple worlds and invalidate the pointwise classifications.

The exact CM count uses labelled worlds. Quotienting by permutations of \(W\) would produce a different, substantially harder enumeration.

The \(\mathrm{CK}_{\Box}\) least-cover theorem uses finiteness. Infinite downward-directed families of covers need not contain their total intersection.

The result classifies induced modal operators, not raw modal covering relations. Redundant cover families are intentionally identified.

No complexity theorem for satisfiability or proof search is claimed.

## References

[1] Nachiappan Valliappan, “Cover Semantics for Intuitionistic Modalities,” arXiv:2607.11352, first posted 13 July 2026; MFPS 2026 preliminary proceedings.

[2] Matthew Jenssen, Will Perkins, and Aditya Potukuchi, “On Dedekind's problem, a sparse version of Sperner's theorem, and antichains of a given size in the Boolean lattice,” *Journal of the London Mathematical Society* 114 (2026), e70624. DOI:10.1112/jlms.70624.

[3] Robert Goldblatt, “Cover semantics for quantified lax logic,” *Journal of Logic and Computation* 21(6) (2011), 1035–1063. DOI:10.1093/logcom/exq029.
