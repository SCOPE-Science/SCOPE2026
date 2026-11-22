# A cyclotomic fourth-cycle census for the reciprocal map over finite fields

## Finding
Let \(q=p^r\) be a prime power of characteristic \(p\ge 7\). On the nonzero elements of \(\mathbb F_q\), iterate the partially defined rational map \(f(x)=x+x^{-1}\), stopping if an iterate is zero. The number \(C_4(q)\) of **distinct orbits of least period four** is
\[
\boxed{C_4(q)=\mathbf 1_{\{q\equiv1,7\pmod {16}\}}+2\mathbf 1_{\{q\equiv1\pmod {30}\}}.}
\]
Thus exactly zero, one, two, or three primitive four-cycles can occur, and every possibility is realized (at prime fields \(11,7,31,151\), respectively). The two contributions arise from disjoint irreducible characteristic-zero period-four factors with splitting fields inside cyclotomic fields of conductors \(16\) and \(30\), respectively.

## Assumptions and scope
We count only finite, nonzero points for which all intermediate iterates are defined; the map is not extended to the projective line. The formula applies to every prime-power field whose characteristic is at least seven, including arbitrary extension degrees. It makes no assertion for characteristics \(2,3,5\) or about periods other than four. Indicators take values zero or one.

## Proof
Let \(N_0(X)=X\), \(D_0(X)=1\), and recursively set \(N_{j+1}=N_j^2+D_j^2\), \(D_{j+1}=N_jD_j\). Then \(f^{\circ j}(X)=N_j(X)/D_j(X)\). For any field, \(N_j,D_j\) have no common root: this holds at \(j=0\), and if a common root occurred at \(j+1\), the equation \(N_jD_j=0\) and \(N_j^2+D_j^2=0\) would force both old entries to vanish. Hence no solution of \(N_j-XD_j=0\) is a spurious pole.

Direct integer-polynomial multiplication gives
\[
N_4(X)-XD_4(X)=(2X^2+1)A(X)B(X),
\]
where
\[
A(X)=2X^4+4X^2+1,\qquad B(X)=X^8+7X^6+14X^4+8X^2+1.
\]
There are no fixed points because \(f(X)-X=1/X\); the exact period-two polynomial is \(2X^2+1\). The discriminants of \(A\) and \(B\) are \(2^{11}\) and \(2^8 3^4 5^6\), respectively, and their resultant is \(3^4\). Thus in characteristic at least seven all fourteen roots of the return equation are simple, the three factors have disjoint root sets, and the twelve roots of \(AB\) all have least period four.

To count roots of \(A\), take a primitive sixteenth root \(\xi\) in an algebraic closure of \(\mathbb Q\) and define
\[
a=\frac{\xi-\xi^{-1}}{\xi^2+\xi^{-2}}.
\]
An exact reduction modulo \(\Phi_{16}(X)=X^8+1\) proves \(A(a)=0\). For the eight automorphisms \(\xi\mapsto\xi^j\), where \(j\) is odd modulo sixteen, the stabilizer of \(a\) is exactly \(\{1,7\}\). The four conjugates are distinct and exhaust the roots of \(A\). The denominator is nonzero in characteristic at least seven because its square is \(2\). Since \(A\) has discriminant a power of two, its four conjugates remain distinct after reduction at such primes. Frobenius \(x\mapsto x^q\) fixes a root if and only if \(q\equiv1\) or \(7\pmod {16}\). In that case all four roots are rational over \(\mathbb F_q\), giving exactly one four-cycle; otherwise there are no \(A\)-cycles.

For \(B\), let \(\eta\) be a primitive thirtieth root, and define \(b=\eta^7+\eta^8\). Reduction in \(\mathbb Z[X]/(\Phi_{30}(X))\) gives \(B(b)=0\). The eight conjugates \(b_j=\eta^{7j}+\eta^{8j}\), \(j\in(\mathbb Z/30\mathbb Z)^\times\), are pairwise distinct, so they exhaust \(B\)'s roots. The splitting field is \(\mathbb Q(\eta)\) and the Galois stabilizer is trivial. The discriminant of \(B\) excludes collisions in characteristic at least seven. Frobenius fixes any root of \(B\) precisely when \(q\equiv1\pmod {30}\), in which case all eight lie in \(\mathbb F_q\). These give exactly two four-cycles. Adding the two disjoint contributions proves the formula.

## Verification
The included `verify_period4.py` independently computes the integer-polynomial fourth-return identity, reduces the proposed cyclotomic elements and all their conjugates in exact quotient rings, verifies the stabilizers and distinctness, and enumerates all nonzero states in the 248 prime fields of characteristic at least seven and order below \(1600\). Running `python3 verify_period4.py` returned `VERIFY_OK polynomial_identity=1 cyclotomic_16=1 cyclotomic_30=1 primes_checked 248`. The infinite prime-power theorem comes from the proof and Frobenius, not from the finite enumeration.

## Relationship to prior work
Matijasevick, Rodríguez and Salazar introduced the reciprocal map in a study of rational recurrence integrality (arXiv:2610.00765, public September 30, 2026). A subsequently published finite-field classification treated least periods two and three, using cyclotomic ninth roots; its complete inspected result explicitly excludes lengths exceeding three. The new contribution is a complete period-four census, whose conductors sixteen and thirty differ from the previous ninth-root mechanism. The first paper's full text was not accessible for an exhaustive comparison, so unrecognized implicit coverage remains a priority risk. An absence of search results cannot establish absolute novelty.

## Limitations
Characteristics two, three and five require separate treatment because factor collisions or repeated roots can occur. This does not classify five-cycles or longer cycles, or dynamics at the pole and projective infinity. Independent mathematical review and independent priority verification have not been performed.

## References
1. M. Matijasevick, S. Rodríguez, G. Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765v1 (first public 2026-09-30), https://arxiv.org/abs/2610.00765.
2. *Cyclotomic rigidity of the first short cycles of the reciprocal map over finite fields*, published November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclotomic-rigidity-of-the-first-short-cycles-of-the-reciprocal--0f652b36ee53.
