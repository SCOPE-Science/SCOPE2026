# Cyclic-class inflation for sparse-marker Toeplitz fixed points

## Finding

Fix an integer \(k\ge 2\) and write \(\varphi_k(0)=0^{k-1}1\), \(\varphi_k(1)=0^k\). Because \(\varphi_k(0)\) begins with \(0\), there is a unique one-sided infinite fixed point \(x_k=\varphi_k^\omega(0)\) beginning with \(0\). For a positive integer \(n\), let \(\mathcal F_n\) be the set of all distinct length-\(n\) contiguous factors of \(x_k\), and define \(\mathcal C_n=\mathcal F_n/\mathord\sim\), where \(u\sim v\) means that one is a cyclic rotation of the other. The elements of \(\mathcal C_n\) are sets of *factors*; rotations that never occur are not counted.

**Theorem.** At every length \(n\ge1\), substitution defines a bijection
\[
\Phi_n:\mathcal C_n\longrightarrow\mathcal C_{kn},\qquad [u]\longmapsto[\varphi_k(u)].
\]
For each \(n\ge2\) and \(C\in\mathcal C_n\), its target class contains exactly \(k|C|\) distinct factors. If every member of \(C\) contains \(t\) ones, the target class has \(n-t\) ones per factor. At \(n=1\), the target class of \(0\) has size \(k\), and that of \(1\) has size one.

In particular, with \(c(n)=|\mathcal C_n|\) and \(p(n)=|\mathcal F_n|\),
\[
c(kn)=c(n)\quad(n\ge1),\qquad p(kn)=kp(n)\quad(n\ge2).
\]
Thus \(c(k^j m)=c(m)\) for all \(j\ge0,m\ge1\). For every \(j\ge1\), at length \(k^j\) there are precisely two classes, of sizes \(k^j\) and \(k^{j-1}\), respectively; hence \(p(k^j)=k^j+k^{j-1}\). For any class with initial length \(n\ge2\), initial size \(s\), and initial ones count \(t\), after \(j\ge0\) substitutions the class has length \(k^j n\), size \(k^j s\), and ones count
\[
t_j=\frac{n(k^j-(-1)^j)}{k+1}+(-1)^j t.
\]

## Assumptions and scope

The alphabet is \(\{0,1\}\); the fixed point is one-sided and indexed from position zero. All factors are ordinary contiguous factors of the infinite word. Cyclic conjugacy is applied to finite factors only, and is not quotienting the ambient sequence by shift. Class cardinalities count *distinct factors*, not occurrences. The theorem is uniform in all integers \(k\ge2\), \(n\ge1\).

## Proof

**1. Recognizable block structure.** The fixed-point identity \(x_k=\varphi_k(x_k)\) partitions it into consecutive length-\(k\) blocks, each having \(k-1\) leading zeros. For \(u=x_k[i..i+n-1]\) and \(0\le r<k\), the factor of length \(kn\) starting at \(ki+r\) is exactly the left rotation \(\rho_r(\varphi_k(u))\). Indeed, it consists of the last \(kn-r\) symbols of \(\varphi_k(u)\), followed by the first \(r\) symbols of the next image block; those first \(r\) symbols are zero, just like the first \(r\) symbols of \(\varphi_k(u)\). Conversely, every factor of length \(kn\) starts at some \(ki+r\), so has this form. Therefore the set of all factors at length \(kn\) is precisely
\[
\mathcal F_{kn}=\bigcup_{u\in\mathcal F_n}\bigcup_{0\le r<k}\{\rho_r(\varphi_k(u))\}.
\]

**2. A residue marker prevents collisions.** Every occurrence of a one in \(\varphi_k(u)\) has an index congruent to \(k-1\) modulo \(k\). If \(u\) contains a zero, there is at least one such one. Thus if \(\varphi_k(u)\) and \(\varphi_k(v)\) are cyclically conjugate, their conjugating rotation must be a multiple of \(k\); otherwise their nonempty sets of one-positions occupy different residue classes. A rotation by \(ks\) simply rotates the source word by \(s\) full letter blocks. Hence \(u\sim v\). The word \(x_k\) has no \(11\), since every image block begins with zero and contains at most one one, at its final position. Thus every factor of length \(n\ge2\) contains at least one zero, and the marker argument applies. For \(n=1\), \(\varphi_k(0)\) has a one and \(\varphi_k(1)\) does not, so their image classes remain distinct.

**3. Bijection and exact class size.** Step 1 proves every target class lies in the image of \(\Phi_n\); Step 2 proves the map is injective. Given a source class \(C\), its target factor class consists of exactly the \(\rho_r(\varphi_k(u))\), for \(u\in C\) and \(0\le r<k\). If \(n\ge2\), all these \(k|C|\) words are distinct: distinct \(r\) give distinct residues for the nonempty one-set, and for fixed \(r\), the morphism is injective. The two exceptional length-one classes are checked directly: the \(k\) rotations of \(0^{k-1}1\) are distinct and factors, whereas \(0^k\) has just one rotation.

**4. Consequences.** Bijection immediately gives \(c(kn)=c(n)\). Summing class sizes yields \(p(kn)=kp(n)\) for \(n\ge2\). Since each source zero gives exactly one image one, the Parikh-one count transforms by \(t\mapsto n-t\). Iterating \(t_{j+1}=k^j n-t_j\) yields the stated closed formula. Finally \(\mathcal C_1\) has the two singleton source classes \([0]\), \([1]\). After the first step they have sizes \(k\) and \(1\), and later steps multiply each size by \(k\) because the lengths are at least two. This proves the special-length formula. \(\square\)

## Verification

The standalone file `verify_necklace.py` generates prefixes of the specified fixed points, computes sets of finite factors and cyclic classes, and checks the asserted class bijection, class-size multipliers, and weight transform for \(2\le k\le6\) and \(1\le n\le14\). This is a finite independent consistency check; the preceding proof supplies the all-parameter guarantee. Execute `python verify_necklace.py` with Python 3. The package records its observed `VERIFY_OK` output after extracting and replaying the embedded file.

## Relationship to prior work

Cassaigne, Fici, Sciortino and Zamboni (2014), Proposition 17, prove \(c(k^j)=2\) for the one-discrepancy substitution family \(0\mapsto u0v,1\mapsto u1v\), and explicitly include the binary period-doubling word. Their proof gives a surjection of cyclic classes after uniform inflation, but neither states the all-length bijection nor derives the exact factor-class cardinality multipliers here. The present conclusion uses the distinctive zero-marker positions of the narrower family \(0\mapsto0^{k-1}1\), \(1\mapsto0^k\); its nontrivial content is that no two distinct classes merge and that the entire within-class size profile is preserved up to multiplication. Fici and Shallit (2021) investigate another Toeplitz family (Stewart words) and different complexity/avoidance measures; their results do not imply this statement.

## Limitations

The theorem does not give a closed form for \(c(m)\) at \(k\)-coprime lengths, or any occurrence frequencies. It is not asserted for arbitrary uniform binary substitutions without the residue marker; nor does it compare the actual two-sided shifts under substitution. Previously existing or unindexed equivalent formulations cannot be completely ruled out. Independent review has not occurred.

## References

1. J. Cassaigne, G. Fici, M. Sciortino, and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, first posted 2014-02-24, especially Section 5.1 and Proposition 17. https://arxiv.org/html/1402.5843v5
2. G. Fici and J. Shallit, *Properties of a Class of Toeplitz Words*, arXiv:2112.12125, first posted 2021-12-22, especially Sections 1 and 10. https://arxiv.org/html/2112.12125v1
