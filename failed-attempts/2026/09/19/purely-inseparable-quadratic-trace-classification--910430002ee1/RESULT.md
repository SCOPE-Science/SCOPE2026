# Purely inseparable correction to quadratic trace-algebra classification

## Result

Let \(E/F\) be a quadratic field extension and let \(t:E\to E\) be an \(F\)-linear trace operator in the sense
\[
t(ab)=t(ba),\qquad t(t(a)b)=t(a)t(b),
\]
with \(t(a)\) central. Since \(E\) is commutative, the first and centrality conditions are automatic.

Then exactly one of the following holds:

1. \(t(x)=\alpha x\) for some \(\alpha\in E\); or
2. \(t\) is a nonzero \(F\)-linear functional \(E\to F\).

Conversely, every map of either type is a trace operator.

If \(E/F\) is separable, the trace pairing
\[
(c,x)\longmapsto \operatorname{Tr}_{E/F}(cx)
\]
is nondegenerate, so every nonzero \(F\)-linear functional \(E\to F\) is uniquely of the form
\[
x\longmapsto \operatorname{Tr}_{E/F}(cx),\qquad c\in E^\times.
\]
Hence the dichotomy stated in Lemma 7 of Centrone--Barbosa--Yasumura, arXiv:2609.19797v1, is correct for separable quadratic extensions.

If \(E/F\) is inseparable, then necessarily \(\operatorname{char}F=2\), the extension is purely inseparable, and
\[
\operatorname{Tr}_{E/F}=0.
\]
Therefore every nonzero \(F\)-linear functional \(E\to F\) is a trace operator that is absent from the two families in Lemma 7. Equivalently:

\[
\boxed{\text{The Lemma 7 dichotomy classifies all trace operators on }E
\iff E/F\text{ is separable}.}
\]

Accordingly, in Proposition 11 of arXiv:2609.19797v1 the quadratic-field branch over an arbitrary base field should be stated as

\[
(E,t_\alpha),\qquad t_\alpha(x)=\alpha x,\quad \alpha\in E,
\]
or
\[
(E,\ell),\qquad 0\ne \ell\in \operatorname{Hom}_F(E,F).
\]

For separable \(E/F\), the second family is exactly the paper's \(\operatorname{Tr}_c\) family. For a purely inseparable quadratic extension, it is an additional family.

## Proof

Suppose first that \(t=0\). Then \(t(x)=0\cdot x\).

Now assume \(t\ne0\). Since \(\dim_F E=2\), the image of \(t\) has dimension one or two.

If \(t\) has rank two, it is surjective. Put \(\alpha=t(1)\). For any \(x\in E\), choose \(y\in E\) with \(t(y)=x\). Then
\[
t(x)=t(t(y)\cdot1)=t(y)t(1)=\alpha x.
\]
Thus \(t=\alpha\,\mathrm{id}_E\).

Suppose instead that \(t\) has rank one. Choose \(u\in E\) with \(t(u)\ne0\), and write \(y=t(u)\). Then
\[
\operatorname{im}t=Fy.
\]
Using the trace axiom,
\[
y^2=t(u)t(u)=t(t(u)u)\in Fy.
\]
Hence \(y^2=\lambda y\) for some \(\lambda\in F\). Since \(E\) is a field and \(y\ne0\), cancellation gives \(y=\lambda\in F\). Thus
\[
\operatorname{im}t=F,
\]
so \(t\) is a nonzero \(F\)-linear functional \(E\to F\).

Conversely, any multiplication map \(x\mapsto\alpha x\) satisfies the trace axioms. If \(\ell:E\to F\) is \(F\)-linear, then
\[
\ell(\ell(a)b)=\ell(a)\ell(b)
\]
because \(\ell(a)\in F\); hence every such \(\ell\) is a trace operator.

The separable case follows from nondegeneracy of the field-trace pairing. For an inseparable finite field extension the field trace is identically zero; in degree two this is the purely inseparable characteristic-two case. Thus no nonzero functional \(E\to F\) can be represented as \(x\mapsto\operatorname{Tr}_{E/F}(cx)\) there.

## Explicit counterexample

Let
\[
F=\mathbb F_2(s),\qquad E=F(u),\qquad u^2=s.
\]
Then \(E/F\) is a purely inseparable quadratic extension. Define
\[
\ell(a+bu)=b,\qquad a,b\in F.
\]
This is a nonzero \(F\)-linear map \(E\to F\), so it is a trace operator by the theorem. The underlying algebra is a field, hence \((E,\ell)\) is tr-simple and tr-prime.

But \(\ell\) is not a multiplication map: every nonzero multiplication map \(E\to E\) has rank two, whereas \(\ell\) has rank one. Also
\[
\operatorname{Tr}_{E/F}=0,
\]
so
\[
\operatorname{Tr}_{E/F}(cx)=0
\]
for all \(c,x\in E\). Thus \((E,\ell)\) is not among the quadratic-extension trace algebras listed in Proposition 11 of arXiv:2609.19797v1.

Because a purely inseparable quadratic extension has no nontrivial \(F\)-automorphisms, distinct nonzero functionals \(\ell\in E^\vee\) give pairwise nonisomorphic trace algebras. Hence the omission is an entire \(E^\vee\setminus\{0\}\) family, not a single exceptional example.

## Centroid correction

For a nonzero rank-one trace \(\ell:E\to F\), the centroid of the trace algebra is exactly \(F\). Indeed, an \(F\)-linear endomorphism commuting with all multiplications by \(E\) is multiplication by some \(c\in E\). Commuting also with \(\ell\) requires
\[
c\,\ell(x)=\ell(cx)
\]
for all \(x\). Choosing \(x\) with \(\ell(x)\ne0\) forces \(c\in F\), and every \(c\in F\) works. Therefore the central closure is \(E\) and
\[
\dim_{C(E,\ell)}Q(E,\ell)=2.
\]

By contrast, for a purely inseparable quadratic extension the paper's map
\[
\operatorname{Tr}_c(x)=\operatorname{Tr}_{E/F}(cx)
\]
is zero for every \(c\), so its centroid is \(E\) and the corresponding central-closure dimension is \(1\). Thus Remark 8 and Lemma 9(ii) of arXiv:2609.19797v1 also require a separability hypothesis when interpreted for the \(\operatorname{Tr}_c\) family.

## Scope and impact

The finite-field identity theorems in Section 4 of arXiv:2609.19797v1 are not contradicted by this correction: finite fields are perfect, so their quadratic extensions are separable. The correction concerns the paper's claimed classification over an arbitrary field and the accompanying quadratic-extension lemmas.

## References

1. L. Centrone, R. Trindade Barbosa, F. Y. Yasumura, *On the trace identities of 2-dimensional tr-prime algebras over a finite field*, arXiv:2609.19797v1 (2026).
2. The Stacks Project, Section 9.20, *Trace and norm*, especially Lemma 9.20.7: a finite field extension is separable iff its trace pairing is nondegenerate, equivalently iff its trace map is nonzero.
