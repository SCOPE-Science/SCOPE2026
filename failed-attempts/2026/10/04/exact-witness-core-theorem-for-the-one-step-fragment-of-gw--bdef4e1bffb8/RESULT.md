# Exact witness-core theorem for the one-step fragment of GW
## Finding

Ferrari, Fiorentini, Giardini, and Rodriguez define the Gödel modal logic GW over **witnessed** fuzzy Kripke models. At a world \(w\), the modal values are

\[
e(w,\Box\alpha)
=
\inf_{u\in W}
\bigl(R(w,u)\to e(u,\alpha)\bigr),
\]

and

\[
e(w,\Diamond\alpha)
=
\sup_{u\in W}
\min\bigl(R(w,u),e(u,\alpha)\bigr),
\]

with Gödel implication

\[
a\to b=
\begin{cases}
1,&a\le b,\\
b,&a>b.
\end{cases}
\]

Witnessedness says that these extrema are attained.

For modal depth one, this immediately supports an exact finite-core theorem.

Let \(\Delta\) be a finite set of formulas of modal depth at most one and fix a root \(w\). For every distinct modal subformula \(\chi\in\mathsf{MSub}(\Delta)\), its scope is propositional. Define the root witness sets

\[
E_{\Box\alpha}
=
\left\{
u\in W:
R(w,u)\to e(u,\alpha)=e(w,\Box\alpha)
\right\},
\]

and

\[
E_{\Diamond\alpha}
=
\left\{
u\in W:
\min(R(w,u),e(u,\alpha))=e(w,\Diamond\alpha)
\right\}.
\]

Every such set is nonempty.

Now let

\[
S\subseteq W
\]

be finite with \(w\in S\), and restrict the model to \(S\) without changing the accessibility or atomic values between retained worlds.

Then

\[
\boxed{
\mathfrak M\!\upharpoonright S
\text{ preserves every modal-subformula value at }w
\iff
S\cap E_\chi\ne\varnothing
\text{ for every }\chi\in\mathsf{MSub}(\Delta).
}
\]

Thus the minimum size of a finite induced root-preserving core is **exactly** the rooted transversal number of the finite witness hypergraph

\[
\mathcal H_w(\Delta)
=
\left(
W,
\{E_\chi:\chi\in\mathsf{MSub}(\Delta)\}
\right).
\]

If

\[
m=|\mathsf{MSub}(\Delta)|,
\]

then choosing one witness from every hyperedge, together with the root, gives

\[
\boxed{
|S|\le m+1.
}
\]

Because the scopes are propositional, their values at retained worlds are unaffected by restriction. Once all modal-subformula values at the root are preserved, every formula in \(\Delta\) has exactly the same root truth value.

The universal bound is sharp. For every

\[
m\ge1,
\]

there is a finite crisp witnessed model and a depth-one formula with exactly \(m\) distinct modal subformulas for which every value-preserving induced root core has exactly

\[
m+1
\]

worlds.

## Assumptions and scope

The semantics are the witnessed Gödel modal semantics of the primary source.

The result concerns a **fixed root** and a **finite family of formulas of modal depth at most one**.

The induced restriction keeps:

\[
R_S(x,y)=R(x,y)
\]

for retained worlds \(x,y\in S\), and keeps every atomic valuation on \(S\).

No closure under generated successors is imposed; this is an induced semantic core, not a generated submodel in the classical modal-logic sense.

The theorem deliberately stops at modal depth one. If a modal operator occurs inside the scope of another modal operator, restricting the model can change the value of that inner scope at a retained witness world. The simple witness-hypergraph criterion therefore no longer suffices without recursive bookkeeping.

The empty modal-subformula case has minimum core size \(1\): the root alone.

## Proof

Fix a witnessed model

\[
\mathfrak M=(W,R,e),
\]

a root \(w\in W\), and a finite set \(\Delta\) of modal-depth-one formulas.

Let

\[
\chi=\Box\alpha
\]

be a modal subformula of \(\Delta\). Since \(\Delta\) has modal depth at most one, \(\alpha\) is propositional.

For each \(u\in W\), put

\[
q_u=R(w,u)\to e(u,\alpha).
\]

Write

\[
q=e(w,\Box\alpha)=\inf_{u\in W}q_u.
\]

Witnessedness gives at least one \(u\) with

\[
q_u=q,
\]

so \(E_{\Box\alpha}\ne\varnothing\).

Now restrict to a finite \(S\ni w\). Because \(\alpha\) is propositional, its value at every retained world is unchanged. Hence

\[
e_S(w,\Box\alpha)
=
\min_{u\in S}q_u.
\]

Since \(q\) is the infimum over all of \(W\),

\[
q\le q_u
\]

for every \(u\). Therefore

\[
e_S(w,\Box\alpha)=q
\]

if and only if one of the retained \(q_u\)'s actually equals \(q\), which is equivalent to

\[
S\cap E_{\Box\alpha}\ne\varnothing.
\]

The diamond case is dual. Put

\[
r_u=\min(R(w,u),e(u,\alpha))
\]

and

\[
r=e(w,\Diamond\alpha)=\sup_{u\in W}r_u.
\]

Witnessedness gives a world attaining \(r\). In the finite restriction,

\[
e_S(w,\Diamond\alpha)
=
\max_{u\in S}r_u.
\]

Since every \(r_u\le r\), equality with the original value holds if and only if \(S\) retains at least one world from

\[
E_{\Diamond\alpha}.
\]

Applying these equivalences independently to every distinct modal subformula proves

\[
\mathfrak M\!\upharpoonright S
\text{ preserves all root modal-subformula values}
\iff
S
\text{ is a rooted transversal of }
\mathcal H_w(\Delta).
\]

Because the hypergraph has only finitely many hyperedges and each is nonempty, a finite rooted transversal exists: choose one world from every edge and adjoin \(w\). Thus the exact minimum is the rooted transversal number and is at most

\[
m+1.
\]

Finally, every formula in \(\Delta\) is obtained at the root by applying Gödel propositional operations to atomic root values and the values of its modal subformulas. The atomic root values are unchanged, and the modal-subformula values are unchanged by construction. A structural induction on formulas therefore gives

\[
e_S(w,\varphi)=e(w,\varphi)
\]

for every \(\varphi\in\Delta\).

### Sharpness

Fix

\[
m\ge1.
\]

Take worlds

\[
W=\{w,u_1,\ldots,u_m\}.
\]

Use a crisp accessibility relation with

\[
R(w,u_i)=1
\]

for every \(i\), and

\[
R(w,w)=0.
\]

All accessibility values not needed for the argument may be set to \(0\).

Introduce atoms \(p_1,\ldots,p_m\) with

\[
e(u_i,p_i)=1,
\]

and with \(p_i\) equal to \(0\) at every other world.

Then

\[
e(w,\Diamond p_i)=1,
\]

and the unique witness world for that value is \(u_i\). Hence

\[
E_{\Diamond p_i}=\{u_i\}.
\]

Consider

\[
\Phi_m
=
\bigwedge_{i=1}^{m}\Diamond p_i.
\]

Its value at \(w\) is \(1\).

If an induced restriction containing \(w\) omits some \(u_i\), then in that restriction

\[
e_S(w,\Diamond p_i)=0,
\]

so

\[
e_S(w,\Phi_m)=0.
\]

Therefore every induced root-preserving submodel in which \(\Phi_m\) keeps value \(1\) must contain all \(m\) witness worlds as well as \(w\). Exactly \(m+1\) worlds are necessary and sufficient.

## Verification

The bundled checker uses the finite Gödel truth-value set

\[
\left\{0,\frac12,1\right\}.
\]

For carriers with one, two, and three worlds, it exhaustively enumerates root accessibility vectors and modal one-step value profiles.

For every pair of modal specifications, independently chosen as box or diamond, it computes:

1. the original extremal modal values;
2. their exact witness sets;
3. every subset containing the root;
4. the modal values after restriction.

It verifies in every case that simultaneous value preservation is equivalent to hitting all witness sets.

This finite replay tests both box and diamond behavior, overlapping witness sets, singleton witness sets, witness sets containing the root, and non-crisp intermediate truth values.

The checker separately constructs the sharp crisp family for

\[
1\le m\le12
\]

and verifies that each \(\Diamond p_i\) has a singleton witness set, that the full conjunction has root value \(1\), and that omitting any witness makes the conjunction value \(0\).

The script prints `VERIFY_OK`.

## Relationship to prior work

Ferrari--Fiorentini--Giardini--Rodriguez introduce GW over witnessed Gödel modal models and prove completeness and a finite-model property. Their proof-search construction creates worlds intended to witness modal assignments and derives a general finite countermodel-size bound from recursive modal decomposition.

The checked full text does not formulate an induced-submodel theorem for a pre-existing witnessed model, does not isolate the modal-depth-one fragment, and does not characterize the **minimum** preserving core by a transversal invariant.

The 2025 witnessed-crisp predecessor develops the same broad proof-theoretic program for crisp accessibility and likewise establishes finite-model behavior, but the checked material does not contain the present one-step witness-core characterization.

Related fuzzy-modal literature on depth-bounded bisimulation studies finite-depth behavioral equivalence through fuzzy relations. That is a different object: it does not identify minimum induced root cores by the sets that attain witnessed extrema.

The present result therefore sharpens the one-step situation in an instance-sensitive way. Instead of merely asserting that a small model exists, it identifies exactly which retained worlds matter for the root: one must hit every extremal witness set, and nothing else is required.

## Limitations

The result is only for modal depth at most one. Nested modalities require recursively preserving the values of modal scopes at retained witness worlds.

The theorem preserves values at one designated root, not necessarily at every retained world.

The hypergraph transversal problem can itself be combinatorially hard for a large explicitly represented witness family; the theorem is a structural characterization, not an efficient optimization algorithm.

The sharp family is crisp, showing that allowing fuzzy accessibility cannot improve the universal worst-case bound.

A conceptually similar one-step minimization statement may exist under coalgebraic, neighborhood, or fuzzy-modal terminology not recovered by the checked literature searches. This is retained as a literature risk.

## References

[1] Mauro Ferrari, Camillo Fiorentini, Paolo Giardini, and Ricardo Oscar Rodriguez, “A Gödel Modal Logic Over Witnessed Models,” arXiv:2606.31906, first posted 30 June 2026; *Electronic Proceedings in Theoretical Computer Science* 447 (2026). DOI:10.4204/EPTCS.447.20.

[2] Mauro Ferrari, Camillo Fiorentini, and Ricardo Oscar Rodriguez, “A Gödel Modal Logic over Witnessed Crisp Models,” in *Automated Reasoning with Analytic Tableaux and Related Methods*, 2025. DOI:10.1007/978-3-032-06085-3_8.

[3] Linh Anh Nguyen, “Depth-Bounded Fuzzy Bisimulation,” *International Journal of General Systems* 53 (2024), 215–236. DOI:10.1080/03081079.2023.2296248.
