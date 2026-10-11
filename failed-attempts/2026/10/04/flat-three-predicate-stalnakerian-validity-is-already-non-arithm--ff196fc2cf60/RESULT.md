# Flat three-predicate Stalnakerian validity is already non-arithmetical
## Finding

Consider the language of quantified conditional logic with exactly one unary predicate
\[
F
\]
and two ternary predicates
\[
A,M.
\]

Define \(\mathcal F_{\mathrm{flat}}\) to be the set of **closed** formulas such that, after expanding all displayed abbreviations, every conditional subformula
\[
\varphi>\psi
\]
has both \(\varphi\) and \(\psi\) quantifier-free and conditional-free.

Then validity restricted to this fragment is already non-arithmetical:

\[
\boxed{
\mathsf L(\mathcal{WS})\cap\mathcal F_{\mathrm{flat}}
\text{ is not arithmetical,}
}
\]
and, because weakly Stalnakerian and Stalnakerian frames have the same logic,
\[
\boxed{
\mathsf L(\mathcal S)\cap\mathcal F_{\mathrm{flat}}
\text{ is not arithmetical.}
}
\]

More precisely, true first-order arithmetic many-one reduces computably to either restricted validity set.

For every arithmetic sentence \(\alpha\), let
\[
\tau(\alpha)=\mathrm{AX}\to\alpha^*
\]
be the arithmetic translation used by Kocurek--Walsh--Weiss, with quantifiers relativized to the definable predicate \(N\). Then
\[
\mathbb N\models\alpha
\quad\Longleftrightarrow\quad
\tau(\alpha)\in\mathsf L(\mathcal{WS})
\quad\Longleftrightarrow\quad
\tau(\alpha)\in\mathsf L(\mathcal S),
\]
and every \(\tau(\alpha)\) belongs to \(\mathcal F_{\mathrm{flat}}\).

Indeed, after abbreviations are expanded, **every conditional occurrence in the whole reduction is an instance of only three templates**
\[
F(x)>\bot,
\]
\[
(F(x)\vee F(y))>\neg F(y),
\]
and
\[
(F(x)\vee F(y))>(F(x)\wedge F(y)).
\]

Thus the arithmetic obstruction survives all three simultaneous restrictions:

\[
\text{conditional nesting depth }1,
\]
\[
\text{one unary plus two ternary predicates},
\]
and
\[
\text{no quantifier inside either operand of a conditional}.
\]

This gives a concrete negative answer for a natural syntactic fragment left open by the source's question about which fragments of the quantified logic remain axiomatizable.

## Assumptions and scope

The classes \(\mathcal{WS}\) and \(\mathcal S\) are the weakly Stalnakerian and Stalnakerian selection-function frames of Kocurek--Walsh--Weiss.

The fragment \(\mathcal F_{\mathrm{flat}}\) is defined explicitly here. The word “flat” is used only as a descriptive name for the displayed syntactic condition; terminology in the conditional-logic literature is not completely uniform.

Only **arithmetic sentences** are translated. No claim about open arithmetic formulas is needed.

The source defines
\[
\Diamond\phi:=\neg(\phi>\bot)
\]
and then
\[
N(x):=\Diamond F(x),
\]
\[
x<y:=N(x)\wedge N(y)\wedge((F(x)\vee F(y))>\neg F(y)),
\]
\[
x\equiv y:=N(x)\wedge N(y)\wedge((F(x)\vee F(y))>(F(x)\wedge F(y))).
\]

It next defines \(Z\) and \(S\) using ordinary first-order quantifiers over \(N,<,\equiv\), and introduces eight axioms \(\mathrm{Ax1}\)--\(\mathrm{Ax8}\) governing the encoded natural numbers, addition \(A\), and multiplication \(M\).

The result concerns validity over all frames in the two semantic classes. It does not assert decidability, completeness, or complexity bounds for fragments obtained by also bounding first-order quantifier depth or by removing either ternary predicate.

## Proof

### The source translation is flat

Expand the modal abbreviation in \(N\):
\[
N(x)=\neg(F(x)>\bot).
\]

Thus every conditional inside \(N\) has quantifier-free, conditional-free antecedent and consequent.

The definition of \(<\) adds only
\[
(F(x)\vee F(y))>\neg F(y).
\]

The definition of \(\equiv\) adds only
\[
(F(x)\vee F(y))>(F(x)\wedge F(y)).
\]

These three displays are the only places where the conditional connective occurs in the arithmetic encoding.

Now inspect the remaining definitions and axioms.

The formulas
\[
Z(x)=N(x)\wedge\neg\exists y(y<x)
\]
and
\[
S(x,y)=x<y\wedge\neg\exists z(x<z\wedge z<y)
\]
place first-order quantifiers **outside** occurrences of \(N\) and \(<\). They do not insert any quantifier into an antecedent or consequent of \(>\).

Likewise, \(\mathrm{Ax1}\)--\(\mathrm{Ax8}\) are formed from \(N,Z,S,\equiv,A,M\) using first-order quantification and the ordinary Boolean connectives. They introduce no new conditional occurrence.

Finally, the standard arithmetic translation \(\alpha\mapsto\alpha^*\) replaces arithmetic relations and operations by the encoded relations and relativizes quantifiers to \(N\). This process can add ordinary quantifiers around translated subformulas, but it never changes the internal shape of the three displayed conditional templates.

An induction on the construction of the arithmetic sentence therefore gives
\[
\tau(\alpha)=\mathrm{AX}\to\alpha^*\in\mathcal F_{\mathrm{flat}}.
\]

The map
\[
\alpha\longmapsto\tau(\alpha)
\]
is computable.

### Arithmetic truth reduces to weak Stalnakerian validity

Kocurek--Walsh--Weiss prove that whenever a weakly Stalnakerian model satisfies \(\mathrm{AX}\) at a world, the quotient of its \(N\)-objects by \(\equiv\), equipped with the induced \(<,A,M\), is isomorphic to
\[
\langle\mathbb N,<,+,\times\rangle.
\]

For arithmetic sentences this gives
\[
\mathbb N\models\alpha
\quad\Longleftrightarrow\quad
(\mathrm{AX}\to\alpha^*)\in\mathsf L(\mathcal{WS}).
\]

For completeness of the reverse direction, the concrete model used in the source can be checked directly.

Take
\[
W=D=\mathbb N,
\qquad
R=W^2,
\]
constant local domain \(D\), and
\[
f(X,n)=
\begin{cases}
\{\min(X\cap\{m:m\ge n\})\},&
X\cap\{m:m\ge n\}\ne\varnothing,\\
\varnothing,&
\text{otherwise}.
\end{cases}
\]

This \(f\) satisfies Success and Uniqueness immediately. If \(n\in X\), then \(n\) is the least member of \(X\) at or above \(n\), giving Weak Centering.

For Uniformity, suppose
\[
f(P,n)\subseteq Q
\quad\text{and}\quad
f(Q,n)\subseteq P.
\]
If one selected set is empty, the corresponding tail is empty; the second inclusion then forces the other tail to be empty as well. If both are nonempty, let their selected minima be \(p\) and \(q\). The inclusions give
\[
q\le p
\quad\text{and}\quad
p\le q,
\]
hence
\[
p=q.
\]
So \(f(P,n)=f(Q,n)\).

Interpret
\[
I(F,k)=\{k\}
\]
and interpret \(A,M\) as ordinary addition and multiplication.

At world \(0\),
\[
[F(a)]=\{a\},
\]
so \(N(a)\) holds for every \(a\). The conditional defining \(<\) selects the smaller of \(a,b\), and therefore recovers ordinary strict order. The conditional defining \(\equiv\) holds exactly when \(a=b\). Consequently \(Z\) is \(0\), \(S\) is ordinary successor, and the stipulated \(A,M\) satisfy \(\mathrm{Ax1}\)--\(\mathrm{Ax8}\).

Hence false arithmetic sentences have flat translated countermodels, while true arithmetic sentences translate to flat validities.

### From the reduction to non-arithmeticity

Let
\[
V_{\mathrm{flat}}^{WS}
=
\mathsf L(\mathcal{WS})\cap\mathcal F_{\mathrm{flat}}.
\]

If \(V_{\mathrm{flat}}^{WS}\) were arithmetical, then its computable preimage under \(\tau\) would be arithmetical. But that preimage is exactly the set of true first-order arithmetic sentences, which is not arithmetical.

Therefore
\[
V_{\mathrm{flat}}^{WS}
\]
is not arithmetical.

The source proves
\[
\mathsf L(\mathcal{WS})=\mathsf L(\mathcal S),
\]
so the same conclusion holds for Stalnakerian validity.

In particular, neither restricted validity set is recursively enumerable, co-recursively enumerable, or recursively axiomatizable.

## Verification

The argument was checked against the source at four load-bearing points.

First, the three formulas \(N,<,\equiv\) were expanded literally, yielding exactly the three conditional templates displayed above.

Second, \(\mathrm{Ax1}\)--\(\mathrm{Ax8}\) and the standard translation were inspected to verify that all first-order quantifiers occur outside those conditional operands and that no nested conditional is introduced.

Third, the reverse-direction model was reconstructed rather than accepted as an unchecked exercise. Success, Weak Centering, Uniformity, and Uniqueness were verified directly, and at world \(0\) the definitions reduce to the standard natural-number order, equality, zero, successor, addition, and multiplication.

Fourth, the reduction is stated only for arithmetic sentences. This is the form needed for the non-arithmeticity argument and avoids any assignment-dependent issue concerning open arithmetic formulas.

No finite experiment is used to establish the arbitrary-formula or non-arithmeticity conclusions.

## Relationship to prior work

Kocurek--Walsh--Weiss prove that the full first-order logic of weakly Stalnakerian frames is not arithmetical by interpreting arithmetic. They also observe that the construction needs only one unary and two ternary predicates, and they explicitly leave open which natural fragments of the logic are axiomatizable.

The source does not isolate the syntactic shape of the conditional occurrences. Its arithmetic encoding nevertheless has a stronger property: every conditional has depth one, every conditional operand is quantifier-free, and only three conditional templates are used.

Flat fragments are a standard proof-theoretic object in conditional logic. Olivetti--Pozzato, for example, give an analytic calculus and theorem prover for a flat propositional fragment of a normal conditional logic. That makes the quantified flat restriction a mathematically natural boundary to test rather than an ad hoc syntactic slice.

Earlier quantified-modal arithmetic encodings, including Cresswell's work used by the source as inspiration, establish incompleteness phenomena in modal predicate logics. They do not state the present three-template flat-fragment theorem for Stalnakerian selection semantics.

Targeted searches for Stalnakerian validity together with “flat fragment,” conditional nesting depth, and quantifier-free conditional scopes did not locate an equivalent result.

## Limitations

The result does not determine the exact analytical or projective complexity of the restricted validity set; it proves only that the set is not arithmetical.

The signature still contains two ternary predicates, which are used to encode addition and multiplication. Nothing here shows that the same hardness survives a purely monadic language.

First-order quantifier depth is unbounded in translations of arbitrary arithmetic sentences. Thus the theorem does not settle fragments with bounded quantifier rank.

The word “flat” is defined by the explicit syntactic condition above; other papers sometimes use that word for slightly different propositional restrictions.

The theorem deliberately uses only sentence instances of the arithmetic translation. No open-form translation claim is required.

## References

[1] Alexander W. Kocurek, James Walsh, and Yale Weiss, “Stalnaker's Logical Problem of Conditionals is Unsolvable,” arXiv:2608.07387, first posted 7 August 2026.

[2] Nicola Olivetti and Gian Luca Pozzato, “Nested sequent calculi and theorem proving for normal conditional logics: The theorem prover NESCOND,” *Intelligenza Artificiale* 9(2) (2015), 109--125. DOI:10.3233/IA-150082.

[3] M. J. Cresswell, “Some incompletable modal predicate logics,” *Logique et Analyse* 160 (1997), 321--334.
