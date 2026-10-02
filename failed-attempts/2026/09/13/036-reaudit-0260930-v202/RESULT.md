# T_inv (DLO with order-reversing involution) is not of presheaf type

## Context
The presheaf-type program (Beke; Caramello) asks which geometric theories are
classified by a presheaf topos Psh(fpMod(Set)). Plain linear orders are of
presheaf type. The admitted target asks whether this survives adding an
order-reversing involution. This record resolves the fixed theory T_inv.

## Definitions
T_inv is the single-sorted coherent theory of dense linear orders without
endpoints (strict total order + density + no endpoints) extended by a unary
function symbol f with coherent axioms: f(f(x))=x,
forall x,y (x<y -> f(y)<f(x)), and forall x (x<f(x) \/ x=f(x) \/ f(x)<x).
E = Sh(C_inv, J_inv) is its Grothendieck classifying topos. fpMod(Set) is the
category of finitely presentable Set-models (M with Hom(M,-) preserving
filtered colimits). T is of presheaf type if E ~= Psh(fpMod(Set)) via the
flat-functor / finitely-presentable-model presentation.

## Result
T_inv is NOT of presheaf type. No nonempty Set-model is finitely presentable,
so fpMod(Set) is trivial (terminal category 1 in the empty-allowed convention;
empty category in the nonempty convention), while T_inv has at least two
non-isomorphic infinite Set-models. Hence E cannot be equivalent to
Psh(fpMod(Set)) under either convention.

## Proof / Evidence
Lemma 1 (term bound): with sole function symbol f and f(f(x))=x provable,
every term in x1..xn equals some xi or f(xi); an n-generated model has <=2n
elements.
Lemma 2: no finite nonempty total order satisfies no-upper-endpoint, so no
finite nonempty T_inv-model exists; the empty structure vacuously satisfies
the coherent axioms.
Lemma 3 (fp-triviality): let M nonempty, a<f(a), I(a)=(a,f(a)) with induced
order and f. Then I(a) is f-closed since a<x<f(a) gives
f(a)>f(x)>a; it is a T-submodel since density/endpoints witnesses in M lie
strictly inside (a,f(a)); it is proper since a not in I(a). With
S={a:a<f(a)}, every b lies in some I(a) by choosing a<min(b,f(b)), so
M=union_a I(a); the family is directed via c=min(a,b) with the smaller
endpoint giving the larger interval. Thus M is a directed union of proper
T-submodels, so id_M cannot factor through any stage and Hom(M,-) does not
preserve this directed colimit: no nonempty M is finitely presentable.
Lemma 4 (two points): (Q,<,q|->-q) is a model with fixed point 0; a
fixed-point-free model on Q exists by splitting A={q<sqrt(2)}, B={q>sqrt(2)}
(two countable DLOs without endpoints) and gluing an order-reversing
bijection phi:A->B with its inverse. Fixed-point existence is isomorphism
invariant, so these are non-isomorphic.
Contradiction: in the empty-allowed convention Psh(1)~=Set has one point up
to isomorphism while E has >=2; in the nonempty convention Psh(empty)~=1
(terminal topos) has one point while E has >=2. Either way E~=Psh(fpMod(Set))
fails. Nothing about plain linear orders is assumed.

## Limitations
Classical Set-models are used for the two exhibited points. No claim is made
about which larger site does classify T_inv. The empty-model statement is
convention-dependent; both conventions are treated and both give the same
negative verdict.

## Reproducibility
output/artifacts/check.py certifies bounded instances only: finite-chain
maxima for n<=6, antitone involutions f(i)=n-1-i for n<=6, and 2n-bound
instances. General facts are proved in Lemmas 1-4 above. Rerun: python3
output/artifacts/check.py (prints OK).

## References
- T. Beke, Theories of presheaf type, JSL 2004.
- O. Caramello, Theories of presheaf type (book Ch. 8; concrete-examples page
  listing linear orders as presheaf type with fp-conservativity criteria).
- nLab, theory of presheaf type; classifying topos.
- Fused literature search (SerpBase/OpenAlex/Crossref/OpenAIRE, full coverage)
  returned no source on DLO with order-reversing involution presheaf status.
