# Degree two is the minimal algebraic obstruction to dividing extension

## Finding

For a complete theory \(T\), consider a failure of algebraic extension for dividing independence
\[
a\mathrel{\perp^d_C} b
\qquad\text{but}\qquad
a\not\mathrel{\perp^d_C}be,
\]
where \(e\in\operatorname{{acl}}(Cb)\) is a finite tuple. Measure the algebraic size of the added parameter by its orbit degree
\[
\deg(e/Cb):=|\operatorname{{Aut}}(\mathbb M/Cb)\cdot e|.
\]
Then every finite such witness has
\[
\boxed{{\deg(e/Cb)\ge 2}}.
\]
Moreover this lower bound is attained, even when the base is a model. In the Conant--Kruckman theory \(T_f^{{\rm eq}}\) from the generic binary function,
\[
\boxed{{\min \deg(e/Mb)=2}}
\]
over every small model \(M\), where the minimum ranges over finite algebraic tuples that destroy a nondividing extension.

Thus the qualitative failure of algebraic extension can occur at the smallest algebraic complexity not already covered by definable closure: a two-point algebraic orbit.

## Assumptions and scope

The degree above is model-theoretic orbit size, not a field-extension degree. The lower bound applies to any complete theory and any finite algebraic tuple witnessing failure. The sharpness statement uses the imaginary expansion \(T_f^{{\rm eq}}\) of the model completion of the empty theory with one binary function symbol, exactly as in Section 3.2 of Conant and Kruckman.

The result does not claim that every failure of algebraic extension has a finite witness of degree two. It identifies the universal minimum among finite algebraic witnesses and shows that this minimum is realized in a natural published counterexample.

## Proof

First, degree one cannot work. If \(\deg(e/Cb)=1\), then every automorphism fixing \(Cb\) fixes \(e\), hence \(e\in\operatorname{{dcl}}(Cb)\). Dividing independence always preserves definable closure: from \(a\mathrel{\perp^d_C}b\) one gets \(a\mathrel{\perp^d_C}\operatorname{{dcl}}(Cb)\). Therefore adjoining a degree-one algebraic tuple cannot create dividing. This gives the universal lower bound \(2\).

For sharpness, fix any small model \(M\models T_f^{{\rm eq}}\). Conant and Kruckman choose distinct home-sort elements \(d_1,d_2\notin M\) and put
\[
b=q(d_1,d_2),
\]
where \(q\) names the unordered pair. Their construction has
\[
\operatorname{{acl}}^O(Mb)=M^O\cup\{{d_1,d_2\}},
\]
and swapping \(d_1,d_2\) while fixing \(M\) is a partial automorphism. By quantifier elimination/homogeneity it extends to an automorphism fixing \(Mb\). Consequently the ordered tuple
\[
e=(d_1,d_2)
\]
has exactly two conjugates over \(Mb\): \((d_1,d_2)\) and \((d_2,d_1)\). Hence \(\deg(e/Mb)=2\).

The same construction supplies a home-sort element \(a\) satisfying
\[
f(a,d_1)=a,\qquad f(a,d_2)=d_1,
\]
and Claim 3.2 of the source proves
\[
a\mathrel{\perp^d_M} b.
\]
It remains only to see directly that adjoining \(e\) creates dividing. Consider
\[
\varphi(x;y_1,y_2):=\bigl(f(x,y_1)=x\bigr)\wedge\bigl(f(x,y_2)=y_1\bigr).
\]
Then \(\varphi(a;d_1,d_2)\) holds.

Choose over \(M\) an indiscernible sequence
\[
((d_1^i,d_2))_{i<\omega}
\]
with the \(d_1^i\) pairwise distinct and with the same finite-function pattern as \((d_1,d_2)\). Such a sequence exists by compactness in the model completion; one may prescribe the left-zero pattern among the \(d_1^i\)'s and the same interactions with \(M\) and \(d_2\). Quantifier elimination makes the resulting sequence \(M\)-indiscernible. But for \(i\ne j\), the two formulas
\[
\varphi(x;d_1^i,d_2),\qquad \varphi(x;d_1^j,d_2)
\]
are inconsistent, since they force the single value \(f(x,d_2)\) to equal two distinct elements. Hence \(\varphi(x;d_1,d_2)\) divides over \(M\), so
\[
a\not\mathrel{\perp^d_M}be.
\]
This realizes the universal lower bound.

## Verification

The lower bound is a direct consequence of preservation of definable closure, explicitly recorded by Conant--Kruckman. The upper bound uses only the source's Section 3.2 configuration plus the displayed two-inconsistency argument.

The bundled verifier checks the finite combinatorial core: an unordered two-set has exactly two ordered lifts under its setwise stabilizer, and a family of formulas of the form \(f(x,c)=u_i\) with fixed \(c\) and distinct \(u_i\) is pairwise inconsistent. It also checks, on finite left-zero function patterns, that every permutation of the varying \(u_i\)'s is an automorphism fixing the common parameter. The computation is a sanity check, not a substitute for compactness or quantifier elimination.

## Relationship to prior work

Conant and Kruckman prove that dividing need not have algebraic extension and give the generic-binary-function example over every small model. They also explicitly note that dividing always preserves definable closure. Their Section 3.2 identifies the unordered-pair algebraic configuration \(\operatorname{{acl}}^O(Mb)=M^O\cup\{{d_1,d_2\}}\) and the swap symmetry.

The present statement extracts the exact boundary between those two facts: degree one is impossible because it is definable, while their unordered pair already yields degree two. Targeted searches for “minimal algebraic degree”, “orbit size two”, and equivalent formulations found the qualitative counterexample but no published statement of this sharp minimality result.

## Limitations

The sharpness proof uses imaginaries and a two-element algebraic orbit. It does not show that a real singleton of orbit size two suffices in the same theory, nor that every theory failing algebraic extension has a degree-two witness. The originality risk is nontrivial because the deduction is short once the source construction and definable-closure observation are placed side by side.

## References

- Gabriel Conant and Alex Kruckman, *Three surprising instances of dividing*, arXiv:2311.00609 (first public version 2023-11-01); Journal of Symbolic Logic, DOI 10.1017/jsl.2024.20. Section 2 records preservation of definable closure; Section 3.2 gives the generic-binary-function unordered-pair counterexample.
- Alex Kruckman and Nicholas Ramsey, *Generic expansion and Skolemization in NSOP1 theories*, Annals of Pure and Applied Logic 169 (2018), 755--774, for the model completion and quantifier-elimination background used by the source.
