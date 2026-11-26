# Independent mathematical audit

## correctness

FAIL

RESULT.md lines 21–47 define an anchored realization as a pair (β,L), but assert a bijection from these pairs to injections ψ alone. Fixing ψ and translating β and every support point by a field element preserves all differences and ψ, producing 2^M distinct anchored pairs. For example the [3,1,3] repetition code in F4 has 24 realizations and only six injections; direct enumeration of every anchor and ordered allowed support gave six groups of four via python /workspace/branches/independent_reproduction.py 1. The corrected bijection is with (β,ψ), or with ψ alone at a fixed β. The proof actually uses the corrected parameterization at lines 109–174: the Goppa check map has kernel C and factors uniquely into the quotient and an injection; d(C)≥3 gives distinct nonzero coordinate classes, and the inverse field-element map returns valid distinct support points. Thus the anchored count and the obstruction M<s are correct for the stated fields. The bundled example checks generated supports/kernels for selected codes, with only the frame count at degree four; it does not rescue the false anchor-forgetting statement. No uploaded code was executed.

## originality

FAIL

The natural corrected theorem is not literally stated by Liang–Zhang, but it is a direct linear-algebra consequence of their explicit forward construction and converse kernel identity. The literal anchor-forgetting formulation is false, not a new correct claim. The absence of a matching catalogue hit does not reverse the implication from the primary source.

## value

FAIL

The multiplicity question is natural, but with coordinate labels and anchors retained there is no nontrivial enumeration left after the prior check-kernel representation: it is an ordered-frame count times an independent free parameter. Repairing the missing anchor restores a useful explanation, not a surviving distinct research claim. Orbit counts that might have independent interest are out of scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
