# General-calculus translations compose, and rule translation is strictly functorial
## Finding

Let \\(\\mathbf{M}\\), \\(\\mathbf{L}\\), and \\(\\mathbf{K}\\) be arbitrary calculi on sets \\(S\\), \\(T\\), and \\(U\\). Following Fellin's sequent-level framework, let \\(f=(\\ell,\\rho)\\) consist of maps \\(\\ell,\\rho:S^*\\to T^*\\), and let \\(g=(p,q)\\) consist of maps \\(p,q:T^*\\to U^*\\). Define their componentwise composite by
\\[
g\\circ f=(p\\circ\\ell,q\\circ\\rho).
\\]
For every rule schema \\(r\\), one has the literal identity
\\[
(r_f)_g=r_{g\\circ f}.
\\]
Hence, for every calculus \\(\\mathbf{M}\\),
\\[
(\\mathbf{M}_f)_g=\\mathbf{M}_{g\\circ f},
\\]
and, more generally,
\\[
(\\mathbf{L}\\cup\\mathbf{M}_f)_g
=
\\mathbf{L}_g\\cup\\mathbf{M}_{g\\circ f}.
\\]
Sound translations compose, faithful translations compose, and therefore sound-and-faithful translations compose. The identity pair is sound and faithful, and componentwise composition is associative. Thus arbitrary calculi with sound translations form a category, while sound-and-faithful translations form a wide subcategory.

In particular, any finite chain of sound-and-faithful conservation translations can be replaced by the single componentwise composite. The iterated translated rule package is unchanged literally, and the equivalence of derivability supplied by soundness plus faithfulness is unchanged.

## Assumptions and scope

A calculus is a set of rule schemata in Fellin's sense. For a set \\(S\\), sequents are pairs of finite lists in \\(S^*\\). A sequent translation is a pair of functions \\(f=(\\ell,\\rho)\\) with \\(\\ell,\\rho:S^*\\to T^*\\), acting independently on antecedents and succedents.

The statement is completely structural: it assumes neither cut nor reflexivity, and it does not require structural consequence relations. It applies to multi-succedent calculi and therefore also to the single-succedent special case. No logical connectives, substitution properties beyond those already built into the rule schemata, or same-language assumption are needed.

## Proof

Let \\(r\\) be an arbitrary rule schema of \\(\\mathbf{M}\\), with premises
\\[
\\{\\Gamma_i\\Rightarrow\\Delta_i:i\\in I\\}
\\]
and conclusion \\(\\Gamma\\Rightarrow\\Delta\\). Translating by \\(f=(\\ell,\\rho)\\) gives the rule whose premises are
\\[
\\{\\ell(\\Gamma_i)\\Rightarrow\\rho(\\Delta_i):i\\in I\\}
\\]
and whose conclusion is \\(\\ell(\\Gamma)\\Rightarrow\\rho(\\Delta)\\).

Now translate this rule by \\(g=(p,q)\\). Its premises become
\\[
\\{p(\\ell(\\Gamma_i))\\Rightarrow q(\\rho(\\Delta_i)):i\\in I\\},
\\]
and its conclusion becomes
\\[
p(\\ell(\\Gamma))\\Rightarrow q(\\rho(\\Delta)).
\\]
These are exactly the premises and conclusion obtained by translating \\(r\\) once with \\(g\\circ f=(p\\circ\\ell,q\\circ\\rho)\\). Thus
\\[
(r_f)_g=r_{g\\circ f}
\\]
as rule schemata, not merely up to derivability. Applying this equality elementwise to every rule of \\(\\mathbf{M}\\) gives
\\[
(\\mathbf{M}_f)_g=\\mathbf{M}_{g\\circ f}.
\\]
Since rule translation is elementwise over unions, the same calculation gives
\\[
(\\mathbf{L}\\cup\\mathbf{M}_f)_g
=
\\mathbf{L}_g\\cup\\mathbf{M}_{g\\circ f}.
\\]

For soundness, suppose \\(f:\\mathbf{M}\\to\\mathbf{L}\\) and \\(g:\\mathbf{L}\\to\\mathbf{K}\\) are sound. If
\\[
\\mathbf{M}\\vdash\\Gamma\\Rightarrow\\Delta,
\\]
then soundness of \\(f\\) yields
\\[
\\mathbf{L}\\vdash\\ell(\\Gamma)\\Rightarrow\\rho(\\Delta),
\\]
and soundness of \\(g\\) yields
\\[
\\mathbf{K}\\vdash p(\\ell(\\Gamma))\\Rightarrow q(\\rho(\\Delta)).
\\]
This is precisely soundness of \\(g\\circ f\\).

For faithfulness, suppose instead that both translations are faithful. From
\\[
\\mathbf{K}\\vdash p(\\ell(\\Gamma))\\Rightarrow q(\\rho(\\Delta))
\\]
faithfulness of \\(g\\) gives
\\[
\\mathbf{L}\\vdash\\ell(\\Gamma)\\Rightarrow\\rho(\\Delta),
\\]
and faithfulness of \\(f\\) then gives
\\[
\\mathbf{M}\\vdash\\Gamma\\Rightarrow\\Delta.
\\]
Hence faithfulness also composes.

The identity pair \\((\\operatorname{id}_{S^*},\\operatorname{id}_{S^*})\\) is both sound and faithful for every calculus, and associativity follows from associativity of ordinary function composition in each component. These facts give the two asserted categories. Induction on the length of a finite chain gives the flattening statement.

## Verification

The argument was checked directly against the source definitions of translated rules and of sound and faithful translations. Every step is definitional: the critical equality is obtained by expanding both sides on an arbitrary rule schema, and the soundness and faithfulness assertions are two-step implication chains.

No finite experiment, enumeration, external prover, or unproved computational certificate is used. The universal quantifiers range over arbitrary sets, arbitrary calculi on those sets, arbitrary pairs of list maps of the stated types, arbitrary rule schemata, and arbitrary sequents.

Boundary checks were made for empty premise sets, multi-succedent sequents, different source and target languages, and calculi lacking cut or reflexivity. None changes the componentwise calculation.

## Relationship to prior work

Fellin introduces translations between arbitrary calculi as pairs of functions on antecedent and succedent lists, explicitly calls such a pair a morphism, defines the translated rule package, and defines soundness and faithfulness. The paper proves one-stage soundness, faithfulness, and minimality criteria and emphasizes that no cut assumption is required.

The new statement isolates the missing two-stage algebra of that framework: translated rules commute strictly with componentwise composition, and soundness and faithfulness are closed under composition. The checked full text does not formulate a category of calculi, a functoriality theorem for translated rule packages, or the finite-chain flattening consequence.

Earlier work on conservation as translation treats abstract consequence relations and nuclei rather than the present arbitrary-calculus, two-sided rule-translation setting. A previously recorded modal-logic result computes a five-element composition monoid for a particular family of modal-to-modal translations; that specific classification neither states nor implies the general rule-schema identity proved here.

## Limitations

The result is a structural theorem about the translation framework, not a new conservation theorem for a particular logic. It does not assert that a given pair of list maps is sound or faithful; those properties must still be proved for each application.

The categorical observation may be regarded as mathematically natural once the definitions are in place, and analogous composition principles are common in other translation frameworks. The originality claim is therefore limited to the explicit strict rule-translation identity, closure theorem, and chain-flattening consequence in this recent arbitrary-calculus framework. A differently worded equivalent statement could exist outside the literature checked here.

## References

1. Giulio Fellin, *Unifying Conservation as Translation for General Calculi*, arXiv:2609.35727v1, 2026.
2. Giulio Fellin and Peter Schuster, *Conservation as Translation*, *Review of Symbolic Logic* 18 (2025), 316--348, DOI: 10.1017/S1755020324000170.
