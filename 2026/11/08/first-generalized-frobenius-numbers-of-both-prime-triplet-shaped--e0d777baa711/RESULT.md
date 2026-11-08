# First generalized Frobenius numbers of both prime-triplet-shaped families

## Finding

For each integer \(k\ge1\), let \(r_A(n)\) be the number of ordered coefficient triples \((x,y,z)\in\mathbb Z_{\ge0}^{3}\) satisfying \(n=ax+by+cz\), where \(A=(a,b,c)\) is the ordered triple of distinct generators. Put
\[
g_1(A)=\max\{n\in\mathbb Z_{\ge0}:r_A(n)\le1\}.
\]
Then, without requiring the generators themselves to be prime,
\[
\boxed{g_1(6k+5,6k+7,6k+11)=12k^2+40k+23}
\]
and
\[
\boxed{g_1(6k+7,6k+11,6k+13)=12k^2+50k+56}.
\]
In particular these identities apply to every prime triplet of the respective shape with first term at least \(11\) or \(13\). These are **first generalized**, not ordinary, Frobenius numbers. For context the corresponding \(k=1\) values are \(75\) and \(118\), and the excluded \(k=0\) values are respectively \(24\) and \(45\).

## Assumptions and scope

All generator triples have positive coprime first two entries and hence finite generalized Frobenius numbers. Throughout \(k\) is an integer at least one, \(a\) is the smallest generator, and \(r_A(n)\) counts distinct nonnegative **coefficient vectors**, not distinct partitions or choices of unordered generators. Primality is not assumed.

## Proof

**Residue threshold lemma.** For either family, write its generators as \((a,a+2d,a+2e)\), with \((d,e)=(1,3)\) or \((2,3)\). In each representation set \(u=x+y+z\), \(t=dy+ez\); thus \(n=au+2t\) and \(u\ge y+z\). Since \(a\) is odd, for each residue of \(n\) modulo \(a\) there is a unique \(t_0\in\{0,\ldots,a-1\}\) with \(n\equiv2t_0\pmod a\), and every possible \(t\ge0\) is \(t_0+ja\), \(j\ge0\). Moreover \(r_A(n+a)\ge r_A(n)\), by injecting a representation into one whose \(x\) is increased by one. Suppose we exhibit, in every residue, an integer \(N\le M\) having at least two representations. Then every integer strictly greater than \(M-a\) has at least two: indeed the preceding integer in the same residue before \(N\) is at most \(M-a\). It therefore suffices also to exhibit one integer \(M-a\) with at most one representation.

**The \((a,a+2,a+6)\) family.** Take \(a=6k+5\). Here \(t=y+3z\); its solutions have \(0\le z\le\lfloor t/3\rfloor\), and the smallest value of \(y+z=t-2z\) is
\[
h(t)=t-2\lfloor t/3\rfloor=\lfloor t/3\rfloor+(t\bmod3).
\]
For \(t\ge3\), the two largest eligible values of \(z\) give two representations as soon as \(u\ge h(t)+2\). Set
\[
M_1=a(2k+4)+2(a-1)=12k^2+46k+28.
\]
For every \(3\le t_0\le a-1\) one has \(h(t_0)\le2k+2\), so the integer \(N=a(h(t_0)+2)+2t_0\le M_1\) has two representations using the same \(t_0\). For \(t_0=0,1,2\), instead take \(t_1=t_0+a\); at \(N=a h(t_1)+2t_1\) one representation uses \(t=t_1\), and another uses \(t=t_0\) because its corresponding total \(u\) is \(h(t_1)+2\ge h(t_0)\). Explicitly these three \(N\)'s are \(a(2k+5)\), \(a(2k+4)+2\), and \(a(2k+5)+4\); all are at most \(M_1\) for \(k\ge1\).

Now consider \(n=M_1-a\), in the residue corresponding to \(t_0=a-1\). At \(t=t_0\), the required total is \(u=h(t_0)+1\), allowing exactly one solution since the second one needs \(h(t_0)+2\). For \(t_1=t_0+a\), the required total is \(u=h(t_0)-1=2k+1\), whereas \(h(t_1)=4k+3\), so there is no solution. For higher \(t=t_1+ja\), the required \(u\) decreases by \(2j\) while \(h(t)\) increases (because \(a\ge11\)). Therefore \(r_A(M_1-a)=1\). The residue threshold lemma yields \(g_1(A)=M_1-a=12k^2+40k+23\).

**The \((a,a+4,a+6)\) family.** Take \(a=6k+7\). Here \(t=2y+3z\) and eligible nonnegative \(z\)'s have \(z\equiv t\pmod2\) and \(z\le\lfloor t/3\rfloor\). Except for \(t=1\), all \(t\ge0\) are represented. Denote by \(h(t)\) the least \(y+z\) for a representation of \(t\). For \(t=6q+r\), \(0\le r\le5\), the exact formula (apart from \(t=1\)) is
\[
h(6q+r)=2q+\beta_r,\qquad (\beta_0,\ldots,\beta_5)=(0,1,1,1,2,2).
\]
There are two distinct \((y,z)\) representations for every \(t\ge6\) except \(t=7\); for these values the second requires \(u\ge h(t)+1\). The values \(0,2,3,4,5,7\) have exactly one eligible \((y,z)\), while \(1\) has none. Put
\[
M_2=a(2k+7)+14=12k^2+56k+63.
\]
For \(t_0\in\{6\}\cup[8,a-1]\), \(h(t_0)\le2k+2\), so \(N=a(h(t_0)+1)+2t_0\le M_2\) has two representations. For \(t_0\in\{0,2,3,4,5,7\}\), put \(t_1=t_0+a\) and \(N=a h(t_1)+2t_1\). The first representation uses \(t_1\), and another uses \(t_0\) with the larger total \(u=h(t_1)+2\). The six values \(h(t_1)\), in that order, are \(2k+3,2k+3,2k+4,2k+4,2k+4,2k+5\). Consequently \(N\le M_2\), with equality for \(t_0=7\). For \(t_0=1\), use two distinct representations at \(t_1=a+1\): the integer \(N=a(h(t_1)+1)+2t_1=a(2k+6)+2\) is less than \(M_2\).

At \(n=M_2-a\), the residue corresponds to \(t_0=7\). This \(t_0\) has exactly one \((y,z)=(2,1)\); the total \(u=h(a+7)+1=2k+6\) makes it feasible. At \(t_1=a+7\), however, the required total is \(u=h(t_1)-1\), which gives no representation. Every later \(t=t_1+ja\) requires a smaller \(u\) and has a larger minimum \(h(t)\), so it also gives none. Hence \(r_A(M_2-a)=1\), proving \(g_1(A)=M_2-a=12k^2+50k+56\). This proves both formulas for every \(k\ge1\).

## Verification

Run `python3 verify_prime_triplets.py` from the directory containing the program, using Python 3 and no third-party packages. Its unbounded-coin dynamic program counts nonnegative coefficient vectors, saturating each count at two (enough to decide the first generalized Frobenius number). It checks \(66\) values of \(k\) independently in each of the two families, including all \(1\le k\le60\) and selected \(k\) up to \(127\). It enumerates all nonnegative integers through \(4a^2\) for each tested triple and checks the complete terminal run of values with at least two representations, as well as the \(k=0\) exceptions. Output is preserved in `verification_output.txt`. These finite computations corroborate but do **not** replace the infinite proof above.

## Relationship to prior work

Robles-Pérez and Rosales, arXiv:2112.05501, Sections 3.1–3.2, calculate the ordinary Frobenius numbers, Apéry sets, genera and pseudo-Frobenius spectra for exactly these two families, and Remark 2.4 proposes investigating their generalized \(p\)-Frobenius numbers. Ordinary Frobenius numbers (the case \(p=0\)) do not determine the first generalized numbers (\(p=1\)) without a denumerant analysis. Komatsu and Ying, arXiv:2206.13052, obtain generalized formulas for arithmetic-progression triples, which neither of these offset sets forms. Hwang and Song's 2023 study of *sexy prime triplets* concerns three-term progressions with offsets \(0,6,12\) and classical \(p=0\) Frobenius invariants; its full text does not cover these \(p=1\) formulas. Direct literature searches and a semantic mathematical-record search did not locate a statement implying the two formulas here. Non-discovery is not a proof of global novelty.

## Limitations

The polynomial identities concern only \(p=1\), only the two specified triple families, and only \(k\ge1\). They do not solve arbitrary \(p\), arbitrary admissible constellations, or other families of triples, and do not assert existence of infinitely many actual prime triplets. An unindexed equivalent formula remains a literature risk. Independent external review has not been performed.

## References

1. A. M. Robles-Pérez and J. C. Rosales, *A Frobenius problem suggested by prime k-tuplets (extended version)*, arXiv:2112.05501 (first posted 2021-12-10), especially Remark 2.4 and Section 3. https://arxiv.org/abs/2112.05501
2. T. Komatsu and H. Ying, *The p-Numerical Semigroup of the Triple of Arithmetic Progressions*, arXiv:2206.13052 (first posted 2022-06-27); *Symmetry* 15 (2023), 1328. https://arxiv.org/abs/2206.13052
3. W. T. Hwang and K. Song, *The Frobenius problems for sexy prime triplets*, *International Journal of Mathematics and Computer Science* 18 (2023), 321–333. https://future-in-tech.net/18.2/R-Song-Hwang.pdf
