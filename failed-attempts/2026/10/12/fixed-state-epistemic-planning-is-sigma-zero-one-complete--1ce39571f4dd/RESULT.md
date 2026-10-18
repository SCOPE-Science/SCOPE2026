# Fixed-state epistemic planning is Sigma-zero-one complete
## Finding

Fix the one-agent epistemic planning setting based on modal logic \(K\).

Let
\[
\mathsf{Prp}_\ast=
\{0,1,a,b,\mathrm{root},\mathrm{stg1},
\mathrm{empty},\mathrm{end},\mathrm{ntF},\mathrm{lp}\}.
\]

Let \(s_\ast\) be the finite pointed Kripke model used as the initial epistemic state in Section 3 of Achilleos's reduction, and fix the goal
\[
\Phi_\ast
=
K\neg\mathrm{empty}
\wedge
K(\mathrm{tail}\wedge\neg\mathrm{failed}),
\]
where the abbreviations \(\mathrm{tail}\) and \(\mathrm{failed}\) are the fixed modal-depth-one formulas of that construction.

Consider the following restricted plan-existence problem.

The initial epistemic state is always \(s_\ast\).

The agent set is always the singleton agent of modal logic \(K\).

The proposition vocabulary is always \(\mathsf{Prp}_\ast\).

The goal is always \(\Phi_\ast\).

The only input is a finite set of epistemic actions over that fixed vocabulary, every action having no postconditions and every event precondition having modal depth at most \(1\).

Then
\[
\boxed{
\text{this restricted plan-existence problem is }\Sigma^0_1\text{-complete}.
}
\]

Equivalently, it is recursively enumerable complete under computable many-one reductions.

Thus the undecidability does not require the initial epistemic state or the goal to carry instance information. In the reduction, all input dependence is concentrated in the finite action library.

## Assumptions and scope

An epistemic action is a finite pointed event model with preconditions as in Achilleos. No postconditions are present, so valuations are inherited under product update.

A plan is a finite sequence of input actions whose successive product updates are all defined and whose final pointed model satisfies the fixed goal \(\Phi_\ast\).

Modal depth at most \(1\) means that event preconditions contain no nested epistemic modalities.

The classification
\[
\Sigma^0_1
\]
is with respect to standard effective encodings of finite event models and finite action sets.

The source reduces the binary Post correspondence problem. We use the standard fact that PCP is recursively enumerable complete. Restricting PCP to a binary alphabet preserves this completeness: encode any finite alphabet by a computable injective prefix code over \(\{0,1\}\); the induced morphism preserves and reflects equality of concatenations.

## Proof

### The source reduction already fixes the state, vocabulary, and goal

Take a binary PCP instance
\[
B=
\{(a_i,b_i):1\le i\le n\},
\qquad
a_i,b_i\in\{0,1\}^\ast.
\]

In Section 3 of Achilleos's paper, the proposition set is fixed once and for all as
\[
\mathsf{Prp}_\ast=
\{0,1,a,b,\mathrm{root},\mathrm{stg1},
\mathrm{empty},\mathrm{end},\mathrm{ntF},\mathrm{lp}\}.
\]

The initial epistemic state \(s_\ast\) is then defined solely from this fixed vocabulary. Its worlds, accessibility relation, valuation, and designated world do not depend on the PCP instance \(B\).

The reduction later fixes the goal
\[
\Phi_\ast
=
K\neg\mathrm{empty}
\wedge
K(\mathrm{tail}\wedge\neg\mathrm{failed}).
\]
Again, no symbol in this goal depends on \(B\).

All instance dependence is confined to the actions
\[
\mathrm{add}_i,
\]
whose event chains encode the two words \(a_i,b_i\).

The complete action set is
\[
\mathrm{Act}_B
=
\{\mathrm{add}_i:1\le i\le n\}
\cup
\{\mathrm{nxt\_stg},\mathrm{rmv}_0,\mathrm{rmv}_1\}.
\]

The three verification-stage actions
\[
\mathrm{nxt\_stg},\mathrm{rmv}_0,\mathrm{rmv}_1
\]
are fixed independently of \(B\).

Every action has no postconditions, and every event precondition has modal depth at most \(1\).

Achilleos's Theorem 3.19 proves
\[
B\text{ has a PCP match}
\quad\Longleftrightarrow\quad
(s_\ast,\mathrm{Act}_B,\Phi_\ast)
\text{ has a plan}.
\]

Therefore binary PCP computably many-one reduces to the restricted problem.

### Binary PCP is \(\Sigma^0_1\)-complete

PCP is recursively enumerable complete.

To remove any dependence on alphabet size, let
\[
\Sigma=\{\sigma_1,\ldots,\sigma_m\}
\]
be a finite alphabet and define, for example,
\[
c(\sigma_i)=1^i0.
\]

Extend \(c\) to words by concatenation.

The set
\[
\{1^i0:1\le i\le m\}
\]
is prefix-free, so
\[
c(u)=c(v)
\quad\Longleftrightarrow\quad
u=v.
\]

Applying \(c\) to both coordinates of every PCP pair preserves and reflects matches. Hence binary PCP is also \(\Sigma^0_1\)-complete.

It follows from the source reduction that the restricted planning problem is \(\Sigma^0_1\)-hard.

### The restricted problem is recursively enumerable

Given a finite input action set, enumerate all finite words over that set:
\[
\epsilon,\quad
A_1,\quad
A_1A_2,\quad
\ldots
\]

For each candidate sequence, compute successive product updates starting from the fixed finite state \(s_\ast\).

Each update is effective because both the current epistemic state and the chosen event model are finite, and satisfaction of every depth-one precondition is decidable by direct finite model checking.

If at some step the designated event's precondition fails, reject that candidate sequence.

Otherwise compute the final finite pointed model and decide whether it satisfies the fixed modal formula
\[
\Phi_\ast.
\]

If a plan exists, this enumeration eventually finds one. Therefore the restricted plan-existence problem lies in
\[
\Sigma^0_1.
\]

Combining upper and lower bounds gives
\[
\boxed{
\Sigma^0_1\text{-completeness}.
}
\]

## Verification

Three points were checked directly in the primary PDF.

First, the source defines the proposition set
\[
\{0,1,a,b,\mathrm{root},\mathrm{stg1},
\mathrm{empty},\mathrm{end},\mathrm{ntF},\mathrm{lp}\}
\]
before introducing the PCP-dependent action models, and the displayed initial state \(s_I\) is defined entirely from those fixed symbols.

Second, the reduction closes with
\[
\mathrm{Act}
=
\{\mathrm{add}_i,\mathrm{nxt\_stg},\mathrm{rmv}_{bt}:
1\le i\le n,\ bt\in\{0,1\}\}
\]
and the fixed goal
\[
\Phi_G
=
K\neg\mathrm{empty}\wedge
K(\mathrm{tail}\wedge\neg\mathrm{failed}).
\]

Third, Theorem 3.19 states the exact equivalence between a PCP match and existence of a plan for that task.

The source also states and uses throughout that the construction has no postconditions and preconditions of modal depth at most \(1\).

The \(\Sigma^0_1\) upper bound is independent of the reduction: finite plans can be enumerated and each finite product-update computation can be checked effectively.

## Relationship to prior work

Achilleos proves undecidability for plan existence with modal-depth-one preconditions and no postconditions, including the single-agent \(K\) case. The paper does not isolate the stronger parameter statement that, in its Section 3 reduction, the initial epistemic state and goal are constants and only the finite action set varies. It also states undecidability rather than the exact \(\Sigma^0_1\)-completeness classification.

Lê Cong, Pinchinat, and Schwarzentruber previously obtained a complementary small undecidable class over two-agent \(S5\): their action repertoire and goal are fixed, while only the initial knowledge state is input-dependent. Their paper explicitly highlights that division of input dependence.

The present result identifies the dual concentration in Achilleos's new depth-one/no-postcondition regime: here the initial state and goal can both be fixed, and all PCP information is carried by the action library.

Targeted searches for fixed-initial-state epistemic planning, fixed-goal single-agent \(K\) planning, and the phrase “only the action set varies” did not locate this formulation.

## Limitations

The number and sizes of the input actions are not bounded by a constant. In particular, there is one action
\[
\mathrm{add}_i
\]
for each PCP pair, and its finite event structure depends on the lengths of \(a_i\) and \(b_i\).

The result concerns the unrestricted \(K\)-frame semantics for one agent. It does not apply to the single-agent negative-introspection cases that the source proves decidable.

No claim is made that ten propositions are necessary or minimal.

The theorem fixes the initial state and goal but not the action repertoire; the 2018 small-instance result explores the complementary regime in which the action repertoire is fixed and the initial state varies.

## References

[1] Antonis Achilleos, “An Undecidability Proof for the Plan Existence Problem,” arXiv:2604.22736, first posted 24 April 2026.

[2] Sébastien Lê Cong, Sophie Pinchinat, and François Schwarzentruber, “Small Undecidable Problems in Epistemic Planning,” *Proceedings of IJCAI 2018*, 4780–4786. DOI:10.24963/ijcai.2018/664.

[3] Emil L. Post, “A variant of a recursively unsolvable problem,” *Bulletin of the American Mathematical Society* 52 (1946), 264–268.
