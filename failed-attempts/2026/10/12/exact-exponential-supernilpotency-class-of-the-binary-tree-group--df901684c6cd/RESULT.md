# Exact exponential supernilpotency class of the binary-tree groupoids
## Finding
For every integer \(n\ge 3\), consider the groupoid with zero
\[
H_n=\{0\}\cup\{a_i:1\le i\le 2^n-1\},
\]
whose only nonzero products are
\[
a_{2i}a_{2i+1}=a_i\qquad(1\le i\le 2^{n-1}-1).
\]
Its least nilpotency parameter is exactly \(n\), and its least supernilpotency parameter is exactly
\[
2^{n-1}.
\]
In particular, \(H_n\) is \(n\)-nilpotent but not \((n-1)\)-nilpotent, while it is \(2^{n-1}\)-supernilpotent but not \((2^{n-1}-1)\)-supernilpotent. Since \(|H_n|=2^n\), the latter parameter is exactly half the cardinality of the algebra.

## Assumptions and scope
The statement concerns precisely the finite nonassociative groupoids \(H_n\) from Example 5.4 of arXiv:2610.03348v1, for integers \(n\ge 3\). Nilpotency and supernilpotency are the higher-commutator notions used in that paper. The proof uses its Theorem 3.9, which characterizes \(k\)-supernilpotency by vanishing of every polynomial in \(\operatorname{Pol}^*_{k+1}\), and its Theorem 4.7, which characterizes \(k\)-nilpotency by vanishing of every polynomial term of depth at least \(k\).

## Proof
Write
\[
\ell(i)=\lfloor\log_2 i\rfloor,
\qquad
c(a_i)=2^{n-1-\ell(i)}.
\]
Call \(c(a_i)\) the leaf capacity of \(a_i\). Every nonzero product has the unique form \(a_{2i}a_{2i+1}=a_i\). The two children lie one binary-tree level below their parent, and therefore
\[
c(a_{2i})+c(a_{2i+1})=c(a_i).
\]

Consider any polynomial term whose evaluation in \(H_n\) is nonzero. If the term is a single variable or constant, it has one leaf, which is at most the capacity of its value. If its root is a multiplication and evaluates to \(a_i\), then its two immediate subterms must evaluate to \(a_{2i}\) and \(a_{2i+1}\), respectively. Induction on the term tree therefore shows that the number of leaf occurrences is at most \(c(a_i)\). Since \(c(a_i)\le c(a_1)=2^{n-1}\), every nonzero evaluated term has at most \(2^{n-1}\) leaves.

A term representing a member of \(\operatorname{Pol}^*_m(H_n)\) contains all \(m\) formal arguments, so it has at least \(m\) variable-leaf occurrences. Hence every polynomial in \(\operatorname{Pol}^*_{2^{n-1}+1}(H_n)\) vanishes. Theorem 3.9 of the source then gives that \(H_n\) is \(2^{n-1}\)-supernilpotent.

For the lower bound, take the complete balanced product of the \(2^{n-1}\) bottom-level elements
\[
a_{2^{n-1}},a_{2^{n-1}+1},\ldots,a_{2^n-1}.
\]
Pair adjacent elements, then pair the resulting products, and continue. The source records that this term has depth \(n-1\) and evaluates to \(a_1\ne0\). Replacing its leaves by distinct formal variables gives a nonvanishing polynomial in \(\operatorname{Pol}^*_{2^{n-1}}(H_n)\). By Theorem 3.9, \(H_n\) is therefore not \((2^{n-1}-1)\)-supernilpotent.

The same balanced term has depth \(n-1\) and is nonzero, so Theorem 4.7 implies that \(H_n\) is not \((n-1)\)-nilpotent. Example 5.4 proves that every product of depth \(n\) vanishes, hence that \(H_n\) is \(n\)-nilpotent. This proves both exact parameters.

## Verification
The standalone script `verify_exact_Hn_classes.py` reconstructs the multiplication table, computes the maximal leaf count and maximal nonzero term depth recursively for every nonzero element, verifies the additive-capacity identity on every nonzero multiplication, and reconstructs the complete balanced bottom product. For \(3\le n\le10\), it obtains maximal leaf count \(2^{n-1}\) and maximal depth \(n-1\), and terminates with `VERIFY_OK`. These finite checks test the structural induction and indexing; the theorem for all \(n\ge3\) is established by the written proof.

## Relationship to prior work
Đurđev and Mudrinski construct \(H_n\) to show that \(n\)-nilpotency need not imply \(n\)-supernilpotency. Their Example 5.4 gives the defining multiplication, the nonzero balanced depth-\(n-1\) term, and the proof of \(n\)-nilpotency. It does not state an upper supernilpotency parameter for this family. The capacity argument above supplies that missing upper bound and matches it to the same balanced term, giving the exact value \(2^{n-1}\).

Earlier results for associative semigroups with zero show coincidence of solvability, nilpotency and supernilpotency in that associative setting, so they do not cover these deliberately nonassociative groupoids or imply the exponential separation here.

## Limitations
The exact formula is proved only for the specific family \(H_n\) with the displayed multiplication table. It is not asserted to be extremal among all groupoids of size \(2^n\), nor does it give a general bound relating nilpotency and supernilpotency parameters for arbitrary algebras with zero. The finite verifier is corroborative and is not a substitute for the all-\(n\) proof.

## References
1. I. Đurđev and N. Mudrinski, “(Super)nilpotency and solvability in algebras with zero,” arXiv:2610.03348v1 (2026), especially Theorems 3.9 and 4.7 and Example 5.4.
2. J. Radović and N. Mudrinski, “Higher commutators in semigroups with zero,” Algebra Universalis 84 (2023), Article 12, DOI 10.1007/s00012-023-00809-5.
3. J. Radović and N. Mudrinski, “Supernilpotent semigroups,” Portugaliae Mathematica 81 (2024), 307–320, DOI 10.4171/PM/2118.
