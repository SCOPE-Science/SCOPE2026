# The four-level ordered-witness spectrum of cubic–symplectic Boolean forms

## Finding
Let \(m\ge1\), let \(U=\mathbb F_2^3\), and let \(W\) be a \(2m\)-dimensional \(\mathbb F_2\)-vector space with nondegenerate alternating bilinear form \(B\). Put \(V=U\oplus W\), \(Q=2^{2m}\), and \(h=(1,1,1)\). For any quadratic refinement \(q:W\to\mathbb F_2\) with polar \(B\), and any linear form \(\ell:V\to\mathbb F_2\), set
\[
\alpha(a,v)=a_1a_2a_3+q(v)+\ell(a,v).
\]
Write \(\beta(x,z)=\alpha(x+z)+\alpha(x)+\alpha(z)\) and, for ordered distinct nonzero \(x,y\in V\), let
\[
N(x,y)=\#\{z\in V:\beta(x,z)=1,\ \beta(y,z)=0\}.
\]
The complete witness-count spectrum, independent of the choice of \(q\) and \(\ell\), is
\[
\begin{array}{c|c}
N(x,y)&\#\{(x,y):x,y\ne0,\ x\ne y\}\\ \hline
Q&98Q-62\\
2Q&64(Q-1)(Q-2)\\
3Q&70(Q-1)\\
5Q&6
\end{array}.
\]
These four strata exhaust \((8Q-1)(8Q-2)\) ordered pairs. In particular, every ordered distinct nonzero pair has at least \(Q=|V|/8\) witnesses; this lower bound is attained. The six pairs of maximal witness count \(5Q\) are exactly \(((h,0),(a,0))\) for \(a\in U\setminus\{0,h\}\). For a uniformly selected ordered distinct nonzero pair, the probability of \(N(x,y)=2Q\) is
\[
\frac{64(Q-1)(Q-2)}{(8Q-1)(8Q-2)}\longrightarrow1\qquad(m\to\infty).
\]

## Assumptions and scope
All vector spaces and functions are over \(\mathbb F_2\). The quadratic refinement means \(q(v+w)+q(v)+q(w)=B(v,w)\), and \(q(0)=0\); the linear term satisfies \(\ell(0)=0\). The dimension parameter ranges over every integer \(m\ge1\); no claim is made for a degenerate symplectic form or for arbitrary cubic Boolean polynomials. The ordered-pair universe excludes both zero vertices and equal vertices, whereas witness \(z\) ranges over **all** of \(V\), including zero (which never witnesses). The result concerns the ordered, not unordered, witness relation.

## Proof
**1. Cubic seed rows.** For \(t(a)=a_1a_2a_3\) on \(U\), define \(S_a=\{u\in U:t(a+u)+t(a)+t(u)=1\}\). Direct expansion, or inspection of the eight possible \(u\), gives \(S_0=\varnothing\), \(S_h=U\setminus\{0,h\}\) (six entries), and \(S_a=\{h,h+a\}\) for all six \(a\in E=U\setminus\{0,h\}\). Consequently, over the \(8\cdot7=56\) ordered pairs \(a\ne b\) in \(U\), exactly \(42\) satisfy \(|S_a\mathbin\triangle S_b|=2\), and exactly \(14\) satisfy \(|S_a\mathbin\triangle S_b|=6\). Indeed, the symmetric-difference size is six exactly when one row is \(S_h\) and the other row is not \(S_h\), giving fourteen ordered choices. Over the \(7\cdot6=42\) ordered nonzero distinct pairs \(a,b\), \(|S_a\setminus S_b|=5\) exactly when \(a=h\) and \(b\in E\) (six choices); otherwise the difference has size one (36 choices).

**2. Independent symplectic equations.** The polar splits as
\[
\beta((a,v),(u,w))=\mathbf 1_{u\in S_a}+B(v,w).
\]
Since \(B\) is nondegenerate, the functionals \(B(v,-)\) and \(B(s,-)\) are linearly independent whenever \(v,s\) are distinct nonzero vectors. Thus, for each fixed \(u\), the two target equations in \(w\) have exactly \(Q/4\) solutions if \(v,s\ne0\) and \(v\ne s\); a single nonzero linear equation has exactly \(Q/2\) solutions. No assumption about the values of the quadratic refinement is needed beyond its polar.

**3. Disjoint exhaustive cases.** Write \(x=(a,v)\) and \(y=(b,s)\). The following cases are disjoint and exhaust the allowed ordered pairs.

| Symplectic coordinates | Counts of pairs by witness number |
| --- | --- |
| \(v,s\ne0\), \(v\ne s\) | \(2Q:\ 64(Q-1)(Q-2)\) |
| \(v=s\ne0\), so \(a\ne b\) | \(Q:\ 42(Q-1)\); \(3Q:\ 14(Q-1)\) |
| \(v=0\), \(s\ne0\), so \(a\ne0\) | \(Q:\ 48(Q-1)\); \(3Q:\ 8(Q-1)\) |
| \(v\ne0\), \(s=0\), so \(b\ne0\) | \(Q:\ 8(Q-1)\); \(3Q:\ 48(Q-1)\) |
| \(v=s=0\), so \(a,b\ne0\), \(a\ne b\) | \(Q:\ 36\); \(5Q:\ 6\) |

To obtain the entries, in the second case the admissible \(u\) are exactly \(S_a\triangle S_b\), each with \(Q/2\) admissible \(w\); in the third, they are \(S_a\) with \(Q/2\) choices each; in the fourth they are \(U\setminus S_b\) with \(Q/2\) choices each; in the fifth they are \(S_a\setminus S_b\) with \(Q\) choices each. Summing the rows proves all four multiplicities and the six maximum pairs. Since the first stratum contains many pairs with count \(Q\), the bound \(Q\) is sharp.

**4. Asymptotic concentration.** The generic stratum has cardinality \(64(Q-1)(Q-2)\), whereas the pair universe has \((8Q-1)(8Q-2)\) elements. Their ratio tends to one as \(Q=4^m\to\infty\). The complementary probability is \(O(Q^{-1})\), so concentration is exponentially rapid in \(m\).

## Verification
The included standalone `checker.py` evaluates the defining cubic-plus-quadratic polynomial directly as a bit function, computes its polar for every ordered pair, and counts every witness. Executing `python3 checker.py` requires only the Python standard library. It checks \(m=1,2,3\) with exact histograms:

- \(Q=4\): \(\{4:330,8:384,12:210,20:6\}\).
- \(Q=16\): \(\{16:1506,32:13440,48:1050,80:6\}\).
- \(Q=64\): \(\{64:6210,128:249984,192:4410,320:6\}\).

The finite computations corroborate, but do not replace, the all-\(m\) proof above.

## Relationship to prior work
Pineda Montoya (2026) constructs this cubic–symplectic family to refute a cubic ordered-nondegeneracy conjecture, exhibiting a qualifying witness for each ordered distinct nonzero pair. The same work gives seed-polar supports and an existential symplectic linear-system argument; it does not state the complete four-level ordered-witness multiplicities or the quantitative \(|V|/8\) sharp bound. Morier-Genoud and Ovsienko (2011) introduce the ordered condition in the twisted-algebra setting and analyze different, more symmetric examples. Kreusch and Morier-Genoud (2015) classify real forms of their octonionic families rather than the pairwise quantitative witness spectrum of the present cubic–symplectic family. This result refines existence into a uniform robustness statement and an exact infinite-family histogram; it does not assert any new existence threshold.

## Limitations
The theorem applies only to the displayed cubic seed tensored with a nondegenerate binary symplectic quadratic form. It is not a universal lower bound for every ordered-nondegenerate cubic, nor a classification of all cubic forms. The closest motivating paper contains the seed support table, from which an additional counting argument derives this result; no claim of conceptual independence from that source is made. Historical novelty beyond inspected literature remains a qualified literature assessment. Only a self-review has been performed; no independent audit or formal proof certification is claimed.

## References
1. S. Pineda Montoya, *Counterexamples to a Cubic Nondegeneracy Conjecture*, arXiv:2611.02544v1, publicly submitted 2026-11-02. https://arxiv.org/html/2611.02544v1 .
2. S. Morier-Genoud and V. Ovsienko, *A series of algebras generalizing the octonions and Hurwitz–Radon identity*, arXiv:1003.0429v4; published 2011. https://arxiv.org/html/1003.0429v4 .
3. C. Kreusch and S. Morier-Genoud, *Classification of the algebras \(\mathbb O_{p,q}\)*, 2015. https://orbi.uliege.be/bitstream/2268/161797/1/Article19.pdf .
