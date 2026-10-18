# The exponent-three group model companion fails one-variable quantifier elimination
## Finding

Let
\[
T_3=T_{\mathrm{grp}}\cup\{\forall x\,(x^3=1)\}
\]
be the universal theory of groups of exponent dividing \(3\), and let \(T_3^*\) be its model companion constructed by Ishida, Mizuno, and Takeuchi.

Then \(T_3^*\) does **not** eliminate quantifiers in the pure group language. The failure is already visible with one free variable and no parameters.

Define
\[
\varphi(x):=\forall y\,\forall z\,([x,y,z]=1),
\]
where
\[
[x,y,z]=[[x,y],z].
\]
There are models
\[
M_0,M_1\models T_3^*
\]
and nonidentity elements
\[
a_0\in M_0,
\qquad
a_1\in M_1
\]
with the same parameter-free quantifier-free one-type, but
\[
M_0\models\varphi(a_0)
\qquad\text{and}\qquad
M_1\models\neg\varphi(a_1).
\]

Consequently \(T_3^*\) is not a model completion of \(T_3\).

## Assumptions and scope

All groups are considered in the pure language
\[
\mathcal L_{\mathrm{grp}}=\{\cdot,{}^{-1},1\}.
\]

The source proves that \(T_3\) has a model companion \(T_3^*\). Thus every model of \(T_3\) embeds into a model of \(T_3^*\).

Every group of exponent dividing \(3\) is nilpotent of class at most \(3\). Hence every four-fold left-normed commutator is trivial.

The formula \(\varphi(x)\) defines membership in the second center:
\[
\varphi(x)
\quad\Longleftrightarrow\quad
x\in Z_2(M).
\]
The source's Proposition 4.12 additionally identifies
\[
Z_2(M)=\gamma_2(M)
\]
in existentially closed models, but the proof below only needs the explicit commutator behavior from Example 5.1.

## Proof

### A realization satisfying \(\varphi\)

Let
\[
G=F_{\mathcal V_3}(x,y,z)=B(3,3)
\]
and put
\[
a=[x,y],
\qquad
A=\langle a,z\rangle\le G.
\]

Example 5.1 of Ishida--Mizuno--Takeuchi states that
\[
A\cong B(2,3)
\]
and in particular \(a\ne1\).

The same example observes that for every exponent-three extension
\[
H\ge G
\]
and every
\[
b,c\in H,
\]
one has
\[
[a,b,c]=[[x,y],b,c]=1.
\]
Indeed, this is a four-fold commutator, and groups of exponent \(3\) have nilpotency class at most \(3\).

Because \(T_3^*\) is a companion of \(T_3\), embed \(G\) into some
\[
M_0\models T_3^*.
\]
Let \(a_0\) denote the image of \(a\). Then
\[
M_0\models\varphi(a_0).
\]

### A realization failing \(\varphi\)

Let
\[
F_2=F_{\mathcal V_3}(v,w)
\]
and form the coproduct in the variety of exponent-three groups,
\[
B=A*_{\mathcal V_3}F_2.
\]

Example 5.1 proves
\[
[a,v,w]\ne1
\]
in \(B\).

Again using the companion property, embed \(B\) into some
\[
M_1\models T_3^*.
\]
Let \(a_1\) be the image of \(a\). The images of \(v,w\) remain witnesses to
\[
M_1\models\neg\varphi(a_1).
\]

### The two elements have the same quantifier-free one-type

Both \(a_0\) and \(a_1\) are nonidentity elements in groups of exponent dividing \(3\). Since \(3\) is prime, each has order exactly \(3\).

Every term in one variable in the pure group language is equal, in group theory, to a power
\[
x^m
\]
for some integer \(m\). Thus every atomic formula in one variable is equivalent to
\[
x^m=x^n,
\]
or equivalently
\[
x^{m-n}=1.
\]
For a nonidentity element of an exponent-three group, the truth of this equation depends only on whether
\[
3\mid(m-n).
\]
Therefore every two nonidentity elements of exponent-three groups have the same parameter-free quantifier-free one-type. In particular,
\[
\operatorname{qftp}(a_0)=\operatorname{qftp}(a_1).
\]

If \(T_3^*\) eliminated quantifiers, \(\varphi(x)\) would be equivalent modulo \(T_3^*\) to a quantifier-free formula. Such a formula could not distinguish \(a_0\) from \(a_1\), contradicting the two displayed truth values. Hence \(T_3^*\) does not eliminate quantifiers.

Finally, \(T_3\) is universally axiomatized. A model completion of a universal theory eliminates quantifiers. Therefore the model companion \(T_3^*\) is not a model completion. This agrees with the source's explicit observation that the variety \(\mathcal V_3\) fails the amalgamation property.

## Verification

The load-bearing source statements were checked in the full primary text.

The Main Theorem states that \(T_3\) has a model companion. The model-theoretic preliminaries define companions so that every \(T_3\)-model embeds into a \(T_3^*\)-model.

The introduction states that the variety \(\mathcal V_3\) does not have the amalgamation property and recalls that exponent-three groups have nilpotency class at most \(3\).

Example 5.1 uses
\[
G=B(3,3),
\qquad
a=[x,y],
\qquad
A=\langle a,z\rangle
\]
and proves both that \(a\ne1\) and that
\[
[a,v,w]\ne1
\]
in
\[
A*_{\mathcal V_3}F_{\mathcal V_3}(v,w),
\]
while
\[
[a,b,c]=1
\]
for every \(b,c\) in every exponent-three extension of \(G\).

The quantifier-free-type comparison is elementary and was reconstructed directly from the pure group syntax: with one variable and no parameters, all terms reduce to powers of that variable.

No finite experiment or computational search is used in the proof.

## Relationship to prior work

Ishida--Mizuno--Takeuchi establish existence of the model companion and analyze its existentially closed models. They explicitly note failure of amalgamation and give Example 5.1 as a witness showing that lower-central strictness cannot be omitted from their coproduct arguments.

Their paper does not state a quantifier-elimination theorem or a model-completion theorem, and full-text searches for those phrases are negative.

A separate consequence already recorded in the literature is that the new model companion is complete and decidable. That result concerns effective axiomatizability and joint embedding; it neither implies quantifier elimination nor supplies the one-variable obstruction above.

The present observation extracts a different structural boundary from the same source example: the second-center predicate is not quantifier-free definable in \(T_3^*\), even though it has the simple parameter-free definition
\[
\forall y\,\forall z\,([x,y,z]=1).
\]
Thus the new model companion is genuinely weaker than a model completion in the original group language.

## Limitations

The theorem concerns quantifier elimination in the **pure group language**. It does not exclude quantifier elimination after adding predicates or other definitional structure.

The result proves failure with one free variable, but it does not classify the minimal quantifier alternation or the full definability complexity of the central series.

The non-model-completion conclusion uses the standard theorem that a model completion of a universal theory eliminates quantifiers; no stronger claim about possible expansions is made.

The witness is a structural corollary of the source's explicit nonamalgamation example. It does not change the existence, completeness, decidability, or effective axiomatizability of \(T_3^*\).

## References

[1] Yawara Ishida, Ryosuke Mizuno, and Kota Takeuchi, “Existence of a Model Companion for Groups of Exponent 3,” arXiv:2609.30061v1, first posted 24 September 2026.

[2] Wilfrid Hodges, *Model Theory*, Cambridge University Press, 1993. Standard model-completion and quantifier-elimination criteria.
