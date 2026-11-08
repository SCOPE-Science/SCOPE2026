# A plastic-constant entropy law and exact orbit census for binary \((1,3)\)-pseudoperiodicity

## Finding
Let \(X\subseteq\{0,1\}^{\mathbb Z}\) be the binary subshift specified by
\[
\forall i\in\mathbb Z,\qquad x_i=x_{i+1}\quad\text{or}\quad x_i=x_{i+3}.
\]
For every \(n\ge1\), write \(N_n=|\operatorname{Fix}(\sigma^n)|\) for the number of position-indexed binary length-\(n\) circular words whose two-sided periodic extension satisfies this condition. Then the dynamical zeta function is exactly
\[
\zeta_X(z)=\exp\left(\sum_{n\ge1}\frac{N_n}{n}z^n\right)
=\frac{1}{(1-z)^2(1-z^2-z^3)(1+z^2-z^3)}.
\]
Equivalently, for every positive integer \(n\),
\[
N_n=2+u_n+v_n,
\]
where \(u_0=3,u_1=0,u_2=2\), \(v_0=3,v_1=0,v_2=-2\), and for every \(n\ge3\),
\[
u_n=u_{n-2}+u_{n-3},\qquad v_n=-v_{n-2}+v_{n-3}.
\]
The number of primitive shift orbits of least period \(n\) is
\[
P_n=\frac1n\sum_{d\mid n}\mu(d)N_{n/d}.
\]
The topological entropy is
\[
h_{\rm top}(X)=\log\rho,
\qquad \rho^3-\rho-1=0,\quad \rho>1,
\]
so \(\rho=1.324717957244\ldots\) (the plastic constant), \(N_n\sim\rho^n\), and \(P_n\sim\rho^n/n\).

A direct combinatorial characterization holds without any restriction on the positive period \(n\): the periodic extension of a nonconstant circular binary word lies in \(X\) precisely if **each maximal cyclic constant run has length one or two and no pair of neighboring cyclic runs are both singletons**. The two constant circular words always lie in \(X\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), and pseudoperiods are the two fixed positive shifts \(1\) and \(3\). A circular word is a binary function on \(\mathbb Z/n\mathbb Z\), not a necklace; phase-indexed words are distinct when their coordinate strings differ. The notation \(\operatorname{Fix}(\sigma^n)\) counts points of period dividing \(n\). In contrast, \(P_n\) counts orbits with least period exactly \(n\). Cyclic runs are counted across the boundary between positions \(n-1\) and \(0\). The run characterization is made for periodic points, not for arbitrary aperiodic words with infinite one-sided constant tails.

## Proof
**Step 1: the cyclic run criterion.** Fix a nonconstant periodic binary word. An index interior to a constant run automatically satisfies the condition because the next letter agrees. At an index \(i\) finishing a constant run, the letter at \(i+1\) is opposite. Thus the condition forces the letter at \(i+3\) to agree with the letter at \(i\). If the immediately following run has length at least three, that letter is still opposite, so the condition fails. If its length is two, \(i+3\) is the first letter of the next run and agrees. If the following run has length one, then \(i+3\) agrees if and only if the run after it has length at least two. Applying this at every run end proves exactly the claimed lengths-one-or-two rule with adjacent singleton runs forbidden. This argument is valid even when \(n\in\{1,2,3\}\), interpreting positions modulo \(n\). Constant words satisfy the relation immediately.

**Step 2: an explicit finite graph.** The local condition fails exactly at one of the four consecutive binary factors \(0101,0111,1000,1010\). Form the order-three de Bruijn transfer graph with the eight states \(abc\in\{0,1\}^3\); permit an edge \(abc\to bcd\) exactly when \(a=b\) or \(a=d\). Its complete edge list is

```
000 -> 000, 001
001 -> 010, 011
010 -> 100
011 -> 110
100 -> 001
101 -> 011
110 -> 100, 101
111 -> 110, 111
```

Every directed closed walk of length \(n\) corresponds bijectively to a phase-indexed period-dividing-\(n\) binary sequence, including \(n=1,2\): its states give overlapping triples, and the original binary symbols uniquely determine those triples. Therefore \(N_n=\operatorname{tr}(A^n)\) for the displayed eight-by-eight adjacency matrix \(A\).

**Step 3: split the characteristic polynomial.** The constant triples \(000\) and \(111\) each have a self-loop but cannot belong to any nonconstant directed cycle; their contributions to traces are one each. On the other six states use representatives \(001,010,011\) of the three complementary pairs \((001,110),(010,101),(011,100)\). Binary complementation commutes with \(A\), so its symmetric and antisymmetric invariant subspaces have the matrices
\[
T_+=\begin{pmatrix}0&1&1\\0&0&1\\1&0&0\end{pmatrix},
\qquad T_-=\begin{pmatrix}0&1&1\\0&0&-1\\-1&0&0\end{pmatrix}.
\]
Their characteristic polynomials are respectively \(\lambda^3-\lambda-1\) and \(\lambda^3+\lambda-1\). Consequently,
\[
\det(I-zA)=(1-z)^2(1-z^2-z^3)(1+z^2-z^3).
\]
The formal series identity \(-\log\det(I-zA)=\sum_{n\ge1}\operatorname{tr}(A^n)z^n/n\) proves the zeta formula. Cayley–Hamilton/Newton power sums on the two cubic factors give precisely the displayed initial values and recurrences for \(u_n\) and \(v_n\), establishing \(N_n\) for all \(n\).

**Step 4: primitive orbits and entropy.** A point fixed by the \(n\)-fold shift has a unique least period dividing \(n\). Thus \(N_n=\sum_{d\mid n}dP_d\); Möbius inversion yields the formula for \(P_n\). The six nonconstant states form an irreducible, aperiodic component: for example, the graph has cycles of lengths three (\(001\to010\to100\to001\)) and four (\(001\to011\to110\to100\to001\)); their gcd is one. Its Perron eigenvalue is the unique root \(\rho>1\) of \(\lambda^3-\lambda-1\), since the complementary antisymmetric block has smaller spectral radius. Indeed, the latter has the real root between zero and one and a complex-conjugate pair of modulus smaller than \(\rho\); all other eigenvalues are one or smaller in modulus. The entropy is therefore \(\log\rho\). The trace decomposition gives \(N_n=\rho^n+o(\rho^n)\); from the Möbius formula, proper-divisor contributions are \(O(n\rho^{n/2})\), so \(P_n\sim\rho^n/n\).

## Verification
The standalone Python 3 script `verify.py` implements separate binary-word enumeration, direct local tests, cyclic-run tests, forbidden-four-factor tests, an eight-state transfer graph and two cubic recurrences. Executing `python3 verify.py` compared all \(262142\) binary circular words of lengths \(1\) through \(17\), and verified the three membership descriptions agree. It independently compared the first \(100\) period counts from graph traces and cubic recurrences, including full exhaustive counts through length \(17\). The first twenty period counts are
\[
2,2,8,6,2,8,16,6,8,32,24,12,54,72,38,86,172,134,154,356.
\]
These finite tests check implementation and small boundary cases; the proof above, not enumeration, establishes the infinite identities.

## Relationship to prior work
Meleshko, Ochem, Shallit and Shan introduce and study pseudoperiodic infinite words and investigate binary pseudoperiod pairs in *Pseudoperiodic Words and a Question of Shevelev* (first publicly posted July 20, 2022). In particular, their Proposition 4 treats the different pair \((1,2)\), with essentially rigid eventual behavior, while their general definitions, examples and decision problems do not themselves give the specific complete periodic-point formula, run characterization, or entropy for \((1,3)\). The finite-type transfer-matrix and dynamical-zeta methods used here are standard, as explained in general symbolic-dynamics treatments; no novelty is claimed for those methods. The distinguishing statement is the explicit combinatorial/arithmetic classification and plastic-constant entropy of this particular pseudoperiodic constraint.

## Limitations
Only the binary alphabet and the fixed shifts \((1,3)\) are classified. The run characterization covers periodic words; the graph and entropy cover all two-sided sequences in the defined subshift. Counts distinguish indexed phase words, not rotational equivalence classes, except where primitive orbits are explicitly counted. No stronger assertion about general pseudoperiod sets, finite prefix pseudoperiods, or algorithmic complexity is proved. The originality assessment is based on inspected literature and searches, not on a proof that no unindexed equivalent has previously appeared. No independent expert audit has been performed.

## References
1. J. Meleshko, P. Ochem, J. Shallit, S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, first public preprint July 20, 2022, arXiv:2207.10171v1, https://arxiv.org/abs/2207.10171 ; *Discrete Mathematics & Theoretical Computer Science* 25:2 (2023), doi:10.46298/dmtcs.9919, https://doi.org/10.46298/dmtcs.9919.
2. D. Lind and B. Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press (1995), Chapters 2, 4 and 6 (standard finite-type presentation, entropy and periodic-point techniques), https://faculty.washington.edu/lind/symbolic-toc/.
