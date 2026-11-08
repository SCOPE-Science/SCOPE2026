# The exact regular-set spectrum of the quartic circulant \(C_n(1,3)\)

## Finding

Let \(G_n=\operatorname{Cay}(\mathbb Z_n,\{\pm1,\pm3\})\), where \(n\ge7\). An \((a,b)\)-regular set is a nonempty proper subset \(S\) for which every vertex of \(S\) has exactly \(a\) neighbours in \(S\) and every vertex outside \(S\) has exactly \(b\) neighbours in \(S\). Let \(R_n(a,b)\) be the number of distinct such subsets on the fixed labelled vertex set \(\mathbb Z_n\).

**Theorem (complete cardinality and structure).** For every \(n\ge7\), the only nonzero entries of \(R_n(a,b)\) are as follows. All periodic descriptions use ordinary residues of the labelled vertices.

| Type | Condition | Exact count | All the sets |
|---|---|---|---|
| \((0,4)\) | \(2\mid n\) | \(2\) | One parity class. |
| \((b-1,b)\), \(1\le b\le4\) | \(5\mid n\) | \(\binom{5}{b}\) | Any \(b\) residue classes modulo \(5\). |
| \((b+1,b)\), \(1\le b\le2\) | \(3\mid n\) | \(\binom{3}{b}\) | Any \(b\) residue classes modulo \(3\). |
| \((t,t)\), \(1\le t\le3\) | \(8\mid n\) | \(\binom{4}{t}^2\) | Exactly \(t\) of the four even and \(t\) of the four odd classes modulo \(8\). |
| \((2,2)\) | \(n\equiv4\pmod8\) | \(4\) | Exactly one even and one odd residue class modulo \(4\). |

An entry whose divisibility condition fails is zero. The fourth and fifth rows are mutually exclusive, and all rows specify distinct \((a,b)\)-types. There are no additional \((a,b)\)-regular sets.

In particular the number of *all* nonempty proper regular sets, independently of their parameter pair, is
\[
T(n)=2\mathbf1_{2\mid n}+6\mathbf1_{3\mid n}+30\mathbf1_{5\mid n}+68\mathbf1_{8\mid n}
+4\mathbf1_{n\equiv4\;(\mathrm{mod}\;8)}.
\]
It follows that \(T(n)\le106\) for all \(n\ge7\), with equality **if and only if** \(120\mid n\).

## Assumptions and scope

Graphs are finite, simple, undirected and labelled by \(\mathbb Z_n\). The four generators are distinct because \(n\ge7\); thus each vertex has degree four. The generator \(1\) makes the graph connected. All counts concern subsets, not equivalence classes under graph automorphisms. The empty and full sets are excluded. In the displayed formula \(\mathbf1_E\) is \(1\) when \(E\) holds and \(0\) otherwise.

## Proof

**1. The eigenvalue constraint.** Let \(x_i\in\{0,1\}\) indicate membership in \(S\). By regularity,
\[
x_{i-3}+x_{i-1}+x_{i+1}+x_{i+3}=b+(a-b)x_i\qquad(i\in\mathbb Z_n).
\]
Since \(G_n\) is connected and \(S\) is nonempty and proper, an edge leaves \(S\), whence \(b\ge1\); similarly a selected vertex has a neighbour outside, so \(a\le3\). Counting edges into \(S\) yields
\[
|S|/n=\frac b{4-a+b}.
\]
Set \(\lambda=a-b\). On subtracting the constant mean, the nonzero Fourier modes of \(x\) have adjacency eigenvalue \(\lambda\). If \(z\) is the corresponding nontrivial \(n\)-th root of unity, it obeys
\[
z^{-3}+z^{-1}+z+z^3=\lambda,
\qquad P_\lambda(z)=z^6+z^4+z^2+1-\lambda z^3=0.
\]
Every root-of-unity zero of this degree-six integral polynomial has order \(d\) with \(\varphi(d)\le6\). Exhaustively testing the monic cyclotomic divisors \(\Phi_d\) for
\(d\in\{1,2,3,4,5,6,7,8,9,10,12,14,18\}\) gives exactly
\[
\begin{array}{c|ccccccccc}
\lambda&-4&-3&-2&-1&0&1&2&3&4\\\hline
\text{cyclotomic orders}&2&\varnothing&\varnothing&5,6&4,8&3,10&\varnothing&\varnothing&1.
\end{array}
\]
The attached `verify.py` reproduces the finite *exact integer-polynomial divisibility* calculation. The constant-only mode \(d=1\) cannot occur as a nonzero Fourier mode after mean subtraction. Accordingly, only \(\lambda\in\{-4,-1,0,1\}\) can occur for a nontrivial regular set.

**2. A binary-separability lemma.** Suppose \(r,s\) are coprime and a binary function on \(\mathbb Z_r\times\mathbb Z_s\) can be written \(f(u,v)=U(u)+V(v)\). Then at least one of \(U,V\) is constant. Indeed, if \(U(u)\ne U(u')\), binary-valuedness of both \(U(u)+V(v)\) and \(U(u')+V(v)\) for each \(v\) forces their nonzero difference to be \(+1\) or \(-1\) and both binary values to be the same ordered pair \((0,1)\) or \((1,0)\) for all \(v\). Hence \(V\) is constant. The other case is symmetric. The same lemma applies to the sum of Fourier components with relatively prime periods \(r,s\), since Chinese remaindering identifies each pair of residues and the constant mode can be absorbed into either summand.

**3. The four eigenvalue cases.** For \(\lambda=-4\), only Fourier order \(2\) is allowed, so the binary word is \(2\)-periodic. Its mean is \(1/2\) and the two alternating possibilities give exactly the parity classes, which are \((0,4)\)-regular. They exist precisely when \(2\mid n\).

For \(\lambda=-1\), \(a=b-1\) and \(1\le b\le4\); the density equals \(b/5\). Orders \(5\) and \(6\) show that the word is \(30\)-periodic and splits as a sum of a \(5\)-periodic component and a \(6\)-periodic component. The binary-separability lemma makes it \(5\)-periodic or \(6\)-periodic. A \(6\)-periodic binary word cannot have the requisite density \(b/5\), because \(6b/5\) is not integral for \(1\le b\le4\). Hence \(x\) is \(5\)-periodic. Since it is nonconstant and also \(n\)-periodic, \(5\mid n\). Modulo \(5\), the four neighbours occupy all other residue classes; choosing any \(b\) classes therefore gives precisely \((b-1,b)\). This proves both completeness and the binomial count.

For \(\lambda=1\), \(a=b+1\), so \(b\in\{1,2\}\), with density \(b/3\). Orders \(3,10\), the same binary-separability lemma, and the nonintegrality of \(10b/3\) imply that the word is nonconstant and \(3\)-periodic; hence \(3\mid n\). Modulo \(3\), two generators leave the residue unchanged and one reaches each other class. Thus selecting exactly \(b\) residue classes gives \((b+1,b)\), in exactly \(\binom{3}{b}\) ways.

For \(\lambda=0\), \(a=b=t\in\{1,2,3\}\). Orders \(4,8\) force \(8\)-periodicity. If \(8\mid n\), each residue class modulo \(8\) has its four neighbours exactly in the four classes of the opposite parity. The regularity equations say that precisely \(t\) even and \(t\) odd classes are chosen; the count is \(\binom{4}{t}^2\). If \(8\nmid n\), any nonconstant \(8\)-periodic and \(n\)-periodic word whose Fourier frequencies have orders only \(4,8\) is necessarily \(4\)-periodic, requiring \(4\mid n\). Each vertex then has two neighbours in each of the two opposite-parity classes modulo \(4\), making \(t\) even. As \(1\le t\le3\), it follows that \(t=2\), and one class from each parity is selected, in precisely four ways. These cases exhaust all possibilities.

**4. The uniform bound.** Adding the disjoint counts yields \(T(n)\). The three \(8\)-periodic entries sum to \(16+36+16=68\), whereas the exceptional \(4\)-periodic case contributes only four. The terms have maximal aggregate \(2+6+30+68=106\), attained exactly when \(2,3,5,8\) all divide \(n\), or equivalently when \(120\mid n\). This proves the theorem.

## Verification

The standalone `verify.py` uses only the Python standard library. It computes \(\Phi_d\) via exact monic polynomial division, checks every allowable \(\lambda\in[-4,4]\), and then directly enumerates all nonempty proper subsets for each \(7\le n\le18\), testing the original neighbour-count definition independently and comparing each \((a,b)\) multiplicity. Running `python verify.py` concludes with `VERIFY_OK`. In particular \(n=8\) has \(70\) regular sets and \(n=12\) has \(12\), matching the formulas. The unrestricted theorem is established by the preceding proof, not by extrapolation from exhaustive small orders.

## Relationship to prior work

Abdollahi–Bagherian–Jafari–Khatami–Shokoohi–Sobhani (first public version 2026-09-08) prove a complete **existence** classification for \((a,b)\)-regular sets on all connected quartic circulants, including this graph. Their residue-class constructions and Fourier restrictions are important antecedents. The assertion that the indicated parameters are *possible* is not new; in particular, their Lemma 4.1 already identifies exactly the two \((0,4)\)-regular sets in connected bipartite graphs. The present narrower-family result instead classifies **every** set for all parameter pairs and counts all labelled realizations, including the exact \(8\)-periodic multiplicities, the exceptional \(n\equiv4\pmod8\) count, and the global uniform ceiling of \(106\).

Deng–Ma (2026) analyze efficient dominating sets and efficient open dominating sets on circulant graphs; these specialize to \((0,1)\) and \((1,1)\), not the full enumerator. Earlier efficient-domination and efficient-total-domination papers likewise address those particular parameter types. Accordingly, the entries for the classical perfect-code cases should not be read as priority claims. No independently confirmed earlier all-parameter multiplicity theorem was found; historical priority remains provisional.

## Limitations

The theorem is specific to the quartic circulant with steps \(1\) and \(3\) and requires \(n\ge7\). It does not classify all quartic circulants with arbitrary generators or subsets modulo graph automorphisms. The exact counts are for fixed labelled vertices; multiple periodic realizations may be automorphically equivalent. The literature comparison includes one relevant 2020 paper whose abstract and quoted results were available but whose full text was not accessible; an overlapping special-case enumeration cannot be ruled out. No independent mathematical audit has been conducted.

## References

1. A. Abdollahi, J. Bagherian, F. Jafari, M. Khatami, Z. Shokoohi, R. Sobhani, *Existence of regular sets in circulant quartic graphs: a complete characterization*, arXiv:2609.09414 (v1 submitted 2026-09-08; v2 2026-10-27), https://arxiv.org/abs/2609.09414.
2. Y.-P. Deng, X. Ma, *Notes on efficient dominating sets and efficient open dominating sets in circulant graphs*, arXiv:2610.37167 (2026-10-27), https://arxiv.org/abs/2610.37167.
3. B. Obradović, J. Peters, G. Ružić, *Efficient domination in circulant graph with two chord lengths*, Information Processing Letters 102 (2007), 253–258.
4. Y. S. Kwon, M. Y. Sohn, X.-G. Chen, *Existence of efficient total dominating sets of circulant graphs of degree 4*, Discrete Mathematics 343 (2020), 111742, https://doi.org/10.1016/j.disc.2019.111742. [Only abstract-level comparison of this source was possible.]
