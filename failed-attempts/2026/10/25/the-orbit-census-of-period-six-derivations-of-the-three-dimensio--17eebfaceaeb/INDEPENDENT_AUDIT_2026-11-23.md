# Independent mathematical audit

## correctness

PASS

Derivations have quotient block A, central eigenvalue tr A and a free row v; automorphisms have quotient B and central multiplier det B. The shear changes the row by -w adj(A), bijective if D is periodic. Thus full conjugacy reduces to rational similarity, with q² copies of each matrix in a class. Since T⁶-1 is separable, the exact-order filter applies to semisimple blocks with a,b,a+b in μ6. The displayed resultant can be checked without a computer: factor F=(T²-1)(T²-T+1), use G(1)=21 and G(-1)=-1, and reduce G mod T²-T+1 to 14(T-1), with root-product of (T-1) equal to 1. The resultant is -4116. For p≠7 the allowed unordered pairs are the pairs in each of the two cosets of μ3; Frobenius fixes all six for q≡1 and just the inverse pair in each coset for q≡5 mod 6. If both eigenvalues are cube roots their sum has cube -1. No possible sum of two signs is a sign in these characteristics. In p=7, choose distinct nonopposite pairs, 15-3=12, and include six scalar blocks. The sum of two different elements of {1,2,4} is never in that set, while doubling keeps it invariant, giving exactly the three scalar order-three classes and three scalar order-six classes. Centralizer orders give the table including extension fields. The uploaded code was inspected, not executed; it enumerates prime-field quotient blocks, and printed orbit histogram keys are quotient-class sizes (multiply by q² for full derivations). The reconstruction above verifies the infinite claim.

## originality

FAIL

The prior complete derivation-orbit theorem already supplies the relevant full conjugacy classification, including the exact per-class sizes for arbitrary fields. Burde–Moens supply the sixth-root-sum obstruction including precisely the resultant used in the frozen proof. The proposed exact-order census is a direct finite filter of those two results, rather than a separate orbit calculation or a new arithmetic phenomenon.

## value

FAIL

Finite-field periodicity on the smallest nonabelian Lie algebra is naturally motivated, but the submission's orbit sizes and characteristic-seven mechanism are already available. What remains is a direct enumeration of pairs among six roots and a three-element subgroup check; this does not furnish a surviving independent new classification or invariant under the scientific standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
