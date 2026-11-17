# Subalgebra permutability of standard filiform Lie algebras over finite fields

## Finding

Let \(q\) be any prime power and \(m\ge3\). The standard \((m+1)\)-dimensional filiform Lie algebra \(L_{m+1}(q)\) over \(\mathbb F_q\) has basis \(x,y_1,\ldots,y_m\) and brackets
\[
[x,y_i]=y_{i+1}\quad(1\le i<m),
\]
with all other basis brackets zero apart from alternating bilinearity. Its **subalgebra permutability probability** is the proportion of ordered pairs \((A,B)\) of Lie subalgebras for which \(A+B\) is itself a Lie subalgebra (equivalently, \([A,B]\subseteq A+B\)). This samples subalgebras, not individual elements.

Use the Gaussian coefficient \({a\brack b}_q\), with value zero unless \(0\le b\le a\), and define
\[
\begin{aligned}
G_m(q)&=\sum_{d=0}^m{m\brack d}_q,\\
B_m(q)&=\sum_{j=0}^m q^{m-j},\\
F_q(j,\ell)&=\sum_{s=0}^j{j\brack s}_q q^{(\ell-j)(j-s)}\quad(0\le j\le\ell\le m),\\
R_m(q)&=\sum_{j=0}^m q^{m-j}\sum_{\ell=j}^m F_q(j,\ell),\\
Q_m(q)&=1+\sum_{u=1}^m\bigl((2u-1)q^{u+1}+2q^u\bigr).
\end{aligned}
\]
Then the total number of Lie subalgebras and the number of ordered permuting subalgebra pairs are, respectively,
\[
\boxed{T_m(q)=G_m(q)+B_m(q)},\qquad
\boxed{P_m(q)=G_m(q)^2+2R_m(q)+Q_m(q)}.
\]
Consequently the exact subalgebra commutativity degree is
\[
\boxed{\operatorname{sd}(L_{m+1}(q))=\frac{G_m(q)^2+2R_m(q)+Q_m(q)}{(G_m(q)+B_m(q))^2}}.
\]
For fixed \(m\), as the prime power \(q\) tends to infinity, there is a sharp dimension transition:
\[
\boxed{
\lim_{q\to\infty}\operatorname{sd}(L_{m+1}(q))=
\begin{cases}
0,&m=3,\\
1/4,&m=4,\\
1,&m\ge5.
\end{cases}}
\]
For every fixed prime power \(q\), \(\lim_{m\to\infty}\operatorname{sd}(L_{m+1}(q))=1\).

## Assumptions and scope

All subalgebras are \(\mathbb F_q\)-linear and include the zero and whole Lie algebra. Pairs are ordered; a pair of equal subalgebras is counted. No restriction on field characteristic is used. Set \(V=\langle y_1,\ldots,y_m\rangle\). The map \(J=\operatorname{ad}_x|_V\) is one regular nilpotent Jordan block, and \(W_j=\ker J^j\) is its unique \(J\)-stable subspace of dimension \(j\), for \(0\le j\le m\). The originality domain is \(m\ge3\); the three-dimensional \(m=2\) case is known as the Heisenberg example and is only a consistency check.

## Proof

**Classification of subalgebras.** Any subspace \(U\le V\) is a Lie subalgebra, accounting for \(G_m(q)\) choices. If a Lie subalgebra \(S\) is not contained in \(V\), projection along \(V\) onto \(\mathbb F_q x\) is nonzero. Hence uniquely
\[
S=\mathbb F_q(x+v)\oplus W,
\]
where \(W=S\cap V\) and \(v\) is defined modulo \(W\). Closure under brackets is equivalent to \(JW\subseteq W\), because \([x+v,w]=Jw\). A single Jordan block has just the stable subspaces \(W_j\), so \(W=W_j\) and there are exactly \(q^{m-j}\) choices of \(v\bmod W_j\). These account for \(B_m(q)\) subalgebras. The two classes are disjoint and exhaustive.

**One subalgebra inside the abelian ideal.** Let \(A=U\le V\) and \(B=\mathbb F_q(x+v)\oplus W_j\). Their sum is a Lie subalgebra exactly when \(J(U+W_j)\subseteq U+W_j\). Since the only stable superspaces of \(W_j\) are \(W_\ell\), \(j\le\ell\le m\), we must count \(U\) with \(U+W_j=W_\ell\). Put \(X=U\cap W_j\), \(\dim X=s\). There are \({j\brack s}_q\) choices of \(X\). Once \(X\) is fixed, \(U/X\) is the graph of a linear map from a fixed \((\ell-j)\)-dimensional complement of \(W_j\) in \(W_\ell\) to \(W_j/X\), of dimension \(j-s\). Thus the number of choices of \(U\) is exactly \(F_q(j,\ell)\). The choice of \(v\) contributes \(q^{m-j}\) independently. Summing gives \(R_m(q)\) ordered pairs with first subalgebra inside \(V\) and second outside; reversing the order gives another \(R_m(q)\).

**Both subalgebras outside.** Write
\[
A=\mathbb F_q(x+v)\oplus W_j,\quad
B=\mathbb F_q(x+w)\oplus W_k,\quad d=\min(j,k),\quad s=\max(j,k).
\]
Then \(A+B=\mathbb F_q(x+v)+(W_s+\mathbb F_q(w-v))\). If \(s=m\), this equals the whole Lie algebra, so all \(q^{m-j+m-k}=q^{m-d}\) ordered choices of representatives modulo \(W_j,W_k\) work. If \(s<m\), closure is equivalent to the line spanned by \(w-v+W_s\) (if nonzero) being \(J\)-stable in \(V/W_s\). That quotient is another regular nilpotent Jordan block; its unique stable line is \(W_{s+1}/W_s\). Therefore closure is equivalent to
\[
w-v\in W_{s+1}.
\]
The residue classes of \(v\) and \(w\) modulo \(W_{s+1}\) are independently uniform, with \(q^{m-s-1}\) possibilities. Exactly a fraction \(q^{-(m-s-1)}\) of all pairs agree. Hence the number is \(q^{m-d+1}\). Among \(j,k\in\{0,\ldots,m-1\}\), the number with \(m-d=u\) is \(2u-1\). Summing these counts, then adding the cases \(j=m\) or \(k=m\), yields
\[
\sum_{u=1}^m(2u-1)q^{u+1}+2\sum_{u=1}^m q^u+1=Q_m(q).
\]
All pairs inside \(V\) automatically permute and contribute \(G_m(q)^2\). The three disjoint cases prove the formula for \(P_m(q)\) and hence for the probability.

**Asymptotic transition.** The polynomial \(G_m(q)\) has degree \(\lfloor m^2/4\rfloor\) and leading coefficient one for even \(m\), two for odd \(m\); \(B_m(q)\) has degree \(m\) and leading coefficient one. Each term of \(R_m(q)\) has polynomial degree at most
\[
m+a(m-1-a),\qquad 0\le a\le m,
\]
by setting \(a=j-s\) and choosing \(\ell=m\) in the expression above. Thus \(\deg R_3\le4\), \(\deg R_4\le6\), while \(\deg Q_m=m+1\). For \(m=3\), the numerator has degree at most four whereas the denominator has degree six, giving limit zero. For \(m=4\), \(G_4\) and \(B_4\) both have leading term \(q^4\), while \(R_4\) and \(Q_4\) have degrees below eight; the limit is one quarter. For \(m\ge5\), \(G_m/B_m\to\infty\), and every pair of subalgebras inside \(V\) permutes; consequently \((G_m/(G_m+B_m))^2\le\operatorname{sd}\le1\) gives limit one. For fixed \(q\ge2\) and \(m\to\infty\), the inequalities \(G_m(q)\ge q^{\lfloor m^2/4\rfloor}\) and \(B_m(q)<q^{m+1}/(q-1)\) give the same limit one.

## Verification

The standalone `verify.py` enumerates **all vector subspaces** in reduced row-echelon form over the prime fields \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), and tests the original Lie bracket for every subalgebra and every ordered pair. It does not construct the subalgebra list from the theorem's classification. For \((m,q)=(3,2),(4,2),(5,2),(3,3),(4,3),(3,5)\), the numbers of Lie subalgebras and permuting ordered pairs are respectively
\[
(31,633),\quad(98,6108),\quad(437,149009),\quad(68,2086),\quad(333,54891),\quad(220,11400).
\]
The checker also tests the familiar \(m=2\) Heisenberg boundary over all three prime fields. All nine cases match both formulas; exact outputs are in `verify_output.txt`. Run with `python verify.py`. Prime-power extension fields beyond prime fields were not exhaustively enumerated; the proof holds for every finite field.

## Relationship to prior work

Adimi and Makhlouf (arXiv:1212.1650v1, first made public 7 December 2012) describe the standard naturally graded filiform family and calculate its Lie index, not subalgebra-pair statistics. Towers (1981) studied modular and permutable pairs in Lie-subalgebra lattices, but this work is not being credited with the new finite-field invariant. Avetisyan (arXiv:1610.05365v1, 17 October 2016), Proposition 4, **already classifies all subalgebras of general almost-Abelian Lie algebras**; the subalgebra parametrization above is explicitly an application of that known principle. The claimed contribution lies in the exact incidence count of pairwise *permutability* for a single regular nilpotent Jordan block and its dimension-dependent large-field transition, neither supplied by that structural classification.

Muhie, Otera and Russo (arXiv:2609.19086v1, 16 September 2026) introduce the *subalgebra commutativity degree* and compute the three-dimensional Heisenberg case and a simple Lie-algebra case; the present claim excludes that Heisenberg case. Towers, Zuleta and Gutierrez (arXiv:2608.16575v1, 17 August 2026) study **comaximal graphs**, whose edge relation is joint generation of the entire Lie algebra, not closure of the vector-space sum; their four-dimensional filiform discussion therefore counts a different relation. Earlier work on the element commutativity degree and adjoint-rank spectra of standard filiform Lie algebras counts *elements*, not subalgebra pairs; a full accessible treatment of that result was compared. General results on the lattice of subalgebras may yield a shorter alternative derivation; comprehensive historical priority remains unverified.

## Limitations

The theorem treats the single standard filiform family, not all maximal-class or all almost-Abelian Lie algebras. It gives a scalar pair-incidence count, not the entire dimension-by-dimension adjacency matrix or automorphism orbits. Independent mathematical validation and comprehensive historical-priority verification have not been performed. Prior structural classification supplies a major input; only the new finite-field permutability enumeration and its consequences are asserted as the result.

## References

1. H. Adimi and A. Makhlouf, *Index of Graded Filiform and Quasi Filiform Lie Algebras*, arXiv:1212.1650v1, 2012-12-07, https://arxiv.org/html/1212.1650v1.
2. D. A. Towers, *On Lie algebras in which modular pairs of subalgebras are permutable*, Journal of Algebra **68** (1981), 369–377, DOI:10.1016/0021-8693(81)90269-6.
3. Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365v1, 2016-10-17, https://arxiv.org/abs/1610.05365 (Proposition 4).
4. S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1, 2026-09-16, https://arxiv.org/abs/2609.19086.
5. D. Towers, Y. Zuleta, I. Gutierrez, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants*, arXiv:2608.16575v1, 2026-08-17, https://arxiv.org/abs/2608.16575.
