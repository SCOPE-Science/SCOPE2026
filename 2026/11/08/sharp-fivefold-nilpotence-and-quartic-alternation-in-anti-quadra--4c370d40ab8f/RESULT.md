# Sharp fivefold nilpotence and quartic alternation in anti-quadratic nearly associative algebras

## Finding

**Theorem.** Let \(K\) be a field of characteristic different from \(2\). Suppose a (possibly infinite-dimensional) algebra \(A\) has bilinear product, denoted by juxtaposition, obeying, for all elements,

\[
(xy)z=y(zx),\qquad (xy)z=-(xz)y,\qquad x(yz)=-y(xz).
\]

Then every fivefold product, with every placement of parentheses, vanishes. Indeed every product of five or more elements is zero. In arity four, every parenthesized multilinear monomial is equal to a signed instance of \(Q(a,b,c,d)=(((ab)c)d)\). The polynomial \(Q\) is alternating in its four arguments; its space of multilinear degree-four operations in the relatively free algebra has dimension one, carrying the sign action of \(S_4\).

In particular, for each **anti-quadratic nearly associative algebra**, where \(\omega\) is a nondegenerate alternating form satisfying \(\omega(xy,z)=-\omega(x,yz)\), the established equivalence of near associativity and the anti-left/anti-right identities supplies the displayed hypotheses. Therefore its nilpotency index is at most **five**, rather than the previously published upper bound six. This is **sharp**: an explicit dimension-thirty example with a nonzero fourfold product appears below.

## Assumptions and scope

The field need not be algebraically closed, and the upper bound does not require finite dimensionality or even a bilinear form once the three polynomial identities are assumed. The characteristic-two case is not claimed. Here the nilpotency index is the least positive integer \(n\) for which every possible bracketing of every \(n\)-fold product vanishes. The quartic assertion concerns *multilinear* operations; it does not say all fourfold products are nonzero. The example below uses exterior algebra graded pieces only in positive degrees.

## Proof

**1. A normal form under near associativity.** The first identity yields \(x(yz)=(zx)y\). For any parenthesized monomial, if the right child of the root is an internal node, apply this identity: the new root's right child has fewer leaves. Repeat until the right child is a leaf. Recursively normalize the left child. Induction on the number of leaves turns every bracketed product into some left-associated product of the same factors, possibly permuted. This works at arbitrary arity and needs no characteristic assumption.

**2. Five factors vanish by an eight-step sign cycle.** The three identities give reversible rules, valid for composite inputs and inside arbitrary contexts:

\[
((uv)w)\leftrightarrow v(wu),\quad
((uv)w)\leftrightarrow-(uw)v,\quad
u(vw)\leftrightarrow-v(uw).
\]

Encode a product as a binary tree with leaves indexed \(0,1,2,3,4\) (these are arbitrary input elements); a sign on the left records its coefficient relative to the starting product. Each consecutive line is related by **one** of the displayed substitutions at a subtree (or its inverse):

```text
+ ((((0,1),2),3),4)
- ((((0,1),2),4),3)
+ ((((0,2),1),4),3)
+ ((1,(4,(0,2))),3)
+ ((1,((2,4),0)),3)
+ (((0,1),(2,4)),3)
+ ((2,4),(3,(0,1)))
- ((2,(3,(0,1))),4)
- ((((0,1),2),3),4)
```

The last tree is the first with opposite sign. Hence twice every left-associated fivefold product is zero, so the product vanishes when \(2\) is invertible. The normal-form argument covers **every** fivefold bracketing and, since all longer left-associated products begin with five factors, every higher arity. This is a finite explicit identity proof, not an inference from finite samples.

**3. Quartic operations.** Enumerate all five planar binary parenthesizations and all \(24\) permutations of four distinct formal inputs: there are \(120\) monomials. The same reversible rewriting rules, applied at all subtrees, connect all \(120\) signed monomials into one sign-consistent component. For the canonical left-associated tree, the sign corresponding to each of its \(24\) permuted leaf orders is precisely the permutation parity. Hence the arity-four multilinear quotient has dimension at most one and transforms by the sign representation. The example in Step 4 makes the quartic operation nonzero, so the dimension is exactly one. The complete enumerator (rather than a reported search outcome) is in `verify.py`; it enumerates and tests every edge and sign. For further independent cross-checking it also enumerates all \(1680\) arity-five monomials, finding one sign-inconsistent component, in agreement with the direct eight-step proof.

**4. Sharpness in dimension thirty.** Take a four-dimensional vector space \(V\) with ordered basis \(e_1,e_2,e_3,e_4\) and put

\[
B=\Lambda^1V\oplus\Lambda^2V\oplus\Lambda^3V\oplus\Lambda^4V,
\qquad \dim B=15.
\]

Define a bilinear product \(\star\) on homogeneous elements of degrees \(p,q\) by \(u\star v=c_{p,q}\,u\wedge v\). The only nonzero constants are

\[
c_{1,1}=c_{1,2}=c_{2,1}=c_{2,2}=1,\qquad c_{1,3}=c_{3,1}=-1.
\]

All other degree pairs have coefficient zero, including every pair with total degree more than four. In each possible triple of homogeneous degrees, direct substitution using wedge skew-commutation gives the three stated relations. If the sum of degrees exceeds four, both sides vanish. The included checker independently evaluates the relations on every ordered triple of the fifteen exterior-basis elements.

For \(u\in B\), define \(L_u(w)=u\star w\) and \(R_u(w)=w\star u\). On the thirty-dimensional \(D=B\oplus B^*\) define

\[
(u+f)\diamond(v+g)=u\star v-f\circ L_v-g\circ R_u,
\qquad \omega(u+f,v+g)=f(v)-g(u).
\]

The bilinear form is nondegenerate and alternating. Direct expansion, or the published zero-cocycle cotangent-extension theorem, shows that \(D\) is nearly associative and satisfies \(\omega(x\diamond y,z)=-\omega(x,y\diamond z)\). The checker tests all \(30^3=27000\) ordered basis triples for both identities, with exact integer structure constants. The nested fourfold product in the embedded subalgebra \(B\) is

\[
(((e_1\diamond e_2)\diamond e_3)\diamond e_4)
=-e_1\wedge e_2\wedge e_3\wedge e_4\ne0.
\]

Therefore the nilpotency index is **exactly five** for this algebra. The example works over every field of characteristic different from two.

## Verification

Run `python3 verify.py` from the directory containing that standalone file. Expected output is in `verification_output.txt`. The executable checks the signed identity graphs in arities three through five (\(12,120,1680\) formal monomials), the quartic sign representation, the fifteen-dimensional wedge base (\(3375\) basis triples), and the thirty-dimensional anti-quadratic extension (\(27000\) basis triples). It also checks a nonzero fourfold product and a concrete obstruction to applying the different symmetric-metric theorem. Exact integer computations suffice since all structure constants are \(0,1,-1\). The eight-step derivation and multilinear normal-form argument are symbolic proofs; enumeration is an independently reproducible exhaustive check of the finite formal-identity component.

## Relationship to prior work

Bouarroudj and El Ouali, arXiv:2610.41465v1, October 30, 2026, Theorems 3.2 and 3.4 give the anti-left/anti-right equivalence and **the weaker upper bound six**, while their cotangent-extension theorem supplies the general method used for the example. Their full accessible primary text was inspected in the relevant theorem, proof, and extension sections. The present improvement is the sharp upper bound five, its eight-step polynomial certificate, the quartic alternating structure, and the explicit nonvanishing witness; none is asserted to be in their paper.

Barreiro, Benayadi, El Ouali and Rizzo, arXiv:2608.01329v1, August 2, 2026, Theorem 3.3 independently proves a **fivefold bound for the different class** of anti-left-invariant pseudo-Euclidean nearly associative algebras, with a symmetric metric. Its crucial Lemma 3.1 requires \((uv)w=-(vu)w\). The explicit anti-quadratic example above violates this condition: for \(u=e_1\wedge e_2\), \(v=e_3\), and \(w=e_4\), the two products \((uv)w\) and \((vu)w\) are **equal and nonzero**. Thus the earlier theorem does not contain the present statement under a change of terminology or an immediate reduction. The entire relevant section and proof were inspected.

Dassoundo and Silvestrov, arXiv:2101.12377v1, supply general nearly associative identities and the underlying representation theory, but the inspected Sections 2 and 4 do not provide this sharp nilpotence theorem in the anti-quadratic class.

## Limitations

The bound is not asserted in characteristic two. The dimension-thirty example proves sharpness of the **nilpotency index**, not minimality of the dimension required for sharpness. The quartic calculation concerns the multilinear quotient of the three-identity variety; no claims are made about a complete classification of anti-quadratic algebras. A hidden equivalent in broader algebraic operad literature is a residual priority risk; searches do not prove absolute originality. No independent mathematical audit has been performed.

## References

1. S. Bouarroudj and H. El Ouali, *Anti-quadratic nearly associative algebras*, arXiv:2610.41465v1 (first submitted 2026-10-30). https://arxiv.org/html/2610.41465v1
2. E. Barreiro, S. Benayadi, H. El Ouali and C. Rizzo, *On anti-left-invariant and left-invariant pseudo-Euclidean nearly associative algebras*, arXiv:2608.01329v1 (first submitted 2026-08-02). https://arxiv.org/abs/2608.01329
3. M. L. Dassoundo and S. Silvestrov, *Nearly associative and nearly Hom-associative algebras and bialgebras*, arXiv:2101.12377v1 (first submitted 2021-01-29). https://arxiv.org/abs/2101.12377
