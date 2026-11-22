# Parity and square-class fibers of squaring on the principal torus of a cyclic Nakayama radical

## Finding

Let \(k=\mathbb F_q\), \(n\ge3\), and \(A=kQ_n/J^4\), where \(Q_n\) is the uniformly oriented cycle, \(J\) its arrow ideal, and path indices are in \(\mathbb Z/n\mathbb Z\). For each element
\[
Z=\sum_i (u_i p_{i,2}+v_i p_{i,3})\in J^2
\]
with **every** \(u_i\in k^\times\), this theorem gives the exact number \(F(Z)=|\{X\in A:X^2=Z\}|\). It consequently gives the complete image cardinality on the principal torus \(\mathcal T=\{Z\in J^2:\prod_i u_i\ne0\}\).

Write \(g=\gcd(2,q-1)\), and put \(s_0=1\), \(s_{i+1}=u_i/s_i\) for \(0\le i<n\). All divisions below are in \(k\).

**Odd cycle, odd characteristic.** If \(n\) and \(q\) are odd, then
\[
F(Z)=\begin{cases}2q^n,&s_n\in(k^\times)^2,\\0,&s_n\notin(k^\times)^2.\end{cases}
\]
The value is independent of \(v\). Exactly \(\frac12(q-1)^nq^n\) targets in \(\mathcal T\) are squares.

**Odd cycle, characteristic two.** If \(n\) is odd and \(q\) is even, there is a unique \(t\in k^\times\) satisfying \(t^2=s_n\). Set \(a_i=s_it\) for even \(i\), and \(a_i=s_i/t\) for odd \(i\). Then
\[
F(Z)=\begin{cases}q^{n+1},&\displaystyle\sum_{i=0}^{n-1}\frac{v_i}{a_i a_{i+1}a_{i+2}}=0,\\0,&\text{otherwise.}\end{cases}
\]
Exactly \((q-1)^nq^{n-1}\) targets in \(\mathcal T\) are squares.

**Even cycle, every characteristic.** If \(n\) is even and \(s_n\ne1\), then \(F(Z)=0\). Otherwise put \(d_i=s_i s_{i+1}s_{i+2}\), with cyclic indices (so \(s_n=s_0\) and \(s_{n+1}=s_1\)), and
\[
P=\sum_{i\text{ even}}\frac{v_i}{d_i},\qquad Q=\sum_{i\text{ odd}}\frac{v_i}{d_i}.
\]
Then
\[
F(Z)=q^{n+1}\begin{cases}
q-1,&P=Q=0,\\
g,&PQ\ne0\text{ and }P/Q\in(k^\times)^2,\\
0,&\text{otherwise.}
\end{cases}
\]
The total number of square targets in \(\mathcal T\) is
\[
(q-1)^{n-1}q^{n-2}\left(1+\frac{(q-1)^2}{g}\right).
\]
The two positive fiber formulas coincide for the small fields \(\mathbb F_2\) and \(\mathbb F_3\), and are distinct for every larger finite field.

In particular the density of the square image **within** \(\mathcal T\) is \(1/2\) for odd \(n\), odd \(q\); \(1/q\) for odd \(n\), even \(q\); and
\[
\frac{1+(q-1)^2/g}{(q-1)q^2}
\]
for even \(n\). Hence as \(q\) increases, odd cycles in odd characteristic retain density \(1/2\), whereas even cycles have density asymptotic to \(1/(2q)\) in odd characteristic. This parity distinction is invisible in a count of only square-zero elements.

## Assumptions and scope

The basis vector \(p_{i,j}\) denotes the length-\(j\) directed path starting at vertex \(i\), for \(0\le j\le3\). Products are concatenation when endpoint and start match, and vanish if the combined length is at least four. Thus \(\dim_k J=3n\) and \(\dim_k J^2=2n\). An element of \(A\) with square in \(J^2\) must itself lie in \(J\), since its degree-zero image in \(A/J\cong k^n\) has square zero. The theorem therefore counts **all** algebra roots, not only roots pre-restricted to \(J\). The principal torus \(\mathcal T\) is the natural dense open locus defined by nonvanishing of all length-two coefficients, not a claim about the full image where some \(u_i=0\).

## Proof

**Step 1: the exact path equations.** Each potential root has the unique expansion
\[
X=\sum_i(a_i p_{i,1}+b_i p_{i,2}+c_i p_{i,3}).
\]
Concatenating paths gives \(X^2=Z\) precisely when, for all cyclic \(i\),
\[
a_i a_{i+1}=u_i,\qquad a_i b_{i+1}+b_i a_{i+2}=v_i.
\]
The \(n\) coefficients \(c_i\) are arbitrary, contributing \(q^n\) to every nonempty fiber. Because all \(u_i\ne0\), every \(a_i\ne0\).

**Step 2: solve the multiplicative cycle exactly.** Fix \(a_0=t\in k^\times\). The first equations force
\[
a_i=s_i\,t^{(-1)^i}\quad(0\le i<n),\qquad s_0=1,\quad s_{i+1}=u_i/s_i.
\]
For even \(n\), the closing equation requires \(s_n=1\), and then **every** \(t\in k^\times\) gives one solution. Equivalently, \(\prod_{i\text{ even}}u_i=\prod_{i\text{ odd}}u_i\). For odd \(n\), the closing equation requires \(t^2=s_n\), with \(s_n=(\prod_{i\text{ even}}u_i)/(\prod_{i\text{ odd}}u_i)\). There are \(g\) roots if \(s_n\) belongs to the subgroup of nonzero squares, and none otherwise. In even characteristic \(g=1\), so there is always a unique root.

**Step 3: normalize the additive equation and compute its rank.** For any admissible \(a\), set \(b_i=a_i a_{i+1}h_i\) and \(D_i=a_i a_{i+1}a_{i+2}\in k^\times\). The second equation becomes
\[
h_i+h_{i+1}=v_i/D_i,\qquad i\in\mathbb Z/n\mathbb Z.
\]
The cyclic operator \(I+S\) (where \((Sh)_i=h_{i+1}\)) has kernel dimension zero when \(n\) and \(q\) are odd and dimension one otherwise. Indeed the kernel relation \(h_{i+1}=-h_i\) gives \(h_n=(-1)^n h_0=h_0\). When the kernel dimension is one, the image is the hyperplane
\[
\sum_i(-1)^i\,v_i/D_i=0.
\]
For odd \(n\) in characteristic two, this is the indicated unsigned sum. For odd \(n\) in odd characteristic, every \(v\) is attainable and the solution \(b\) is unique. For even \(n\), since parity is compatible with cyclic indexing, \(D_i=t^{(-1)^i}d_i\). The signed sum is exactly \(P/t-tQ\); thus the condition is \(P=t^2Q\). Its number of nonzero solutions in \(t\) is \(q-1\) if \(P=Q=0\), \(g\) if \(PQ\ne0\) and \(P/Q\) is a square, and zero in every other case. Every admissible \(t\) contributes \(q\) solutions for \(b\), together with \(q^n\) choices for \(c\). This proves all fiber formulas.

**Step 4: image cardinalities and boundary checks.** In odd characteristic and odd length, exactly half of \((k^\times)^n\) has square alternating product \(s_n\), and for each admissible \(u\) every one of the \(q^n\) vectors \(v\) occurs. In characteristic two and odd length, all \(u\) occur and each affords a hyperplane with \(q^{n-1}\) choices for \(v\). In even length, \(s_n=1\) holds for exactly \((q-1)^{n-1}\) tuples \(u\). The two linear forms \(P,Q\) use disjoint nonempty sets of variables, so the map \(v\mapsto(P,Q)\) is surjective with fibers \(q^{n-2}\). There is one attainable pair \((P,Q)=(0,0)\), and \((q-1)^2/g\) pairs with \(PQ\ne0\) and square ratio. Multiplication yields the asserted image cardinality. As a check, summing all nonzero fibers over \(\mathcal T\) in each case gives \((q-1)^nq^{2n}\), the number of roots whose degree-one coefficients are all nonzero; there is no hidden root multiplicity.

## Verification

The standalone Python program `square_torus_verify.py` constructs all length-one and length-two path coefficients and performs independent path-concatenation multiplication, then compares every resulting **nonzero-length-two** target fiber against the theorem, after accounting for the \(q^n\) free length-three coefficients. It checks all targets for cycle lengths \(n=3,4,5,6\) over several fields of orders \(2,3,4,5\), including actual extension-field arithmetic for \(\mathbb F_4\), and checks all predicted image sizes. It prints `NAKAYAMA_SQUARE_TORUS_OK`. These finite tests support implementation but do not replace the preceding proof for all \(n\) and finite fields.

## Relationship to prior work

Dawei Shen's publicly available articles on cyclic Nakayama algebras and resolution quivers (2012, 2014) provide a structural representation-theoretic context, but their principal theorems concern cycle sizes, weights, singularity categories and duality, not power-map fibers of individual elements. A separate published exact square-zero census for the same Loewy-length-four algebras gives a fourth-order recurrence for \(\#\{X:X^2=0\}\) by examining supports with **no adjacent nonzero arrows**. Here all arrow coefficients are **nonzero** and the target is constrained to an open stratum with all degree-two coefficients nonzero. The previous zero-target recurrence cannot imply these prescribed nonzero fibers or their parity and square-class distinctions. The equations for squaring follow directly from the standard path algebra multiplication, whose general mechanism is not claimed to be new; the asserted contribution is their exact all-field generic nonzero-fiber classification and image-density transition.

## Limitations

Only the principal torus \(\prod_i u_i\ne0\) is classified. No assertion is made about fibers at targets with one or more zero degree-two coordinates, about scheme-theoretic multiplicities, or about a complete square-image count for the algebra. In particular, the odd/even image-density comparison applies to the relative density inside \(\mathcal T\), not all of \(J^2\). The finite checker uses small fields and lengths, while the proof uses only field algebra and applies in every finite extension field. A historical paper with an equivalent generic nonzero-root classification could exist beyond the inspected full texts; independent validation has not been performed.

## References

- Dawei Shen, *A note on resolution quivers*, arXiv:1211.5831, first public submission 2012-11-26, https://arxiv.org/abs/1211.5831 (2010 MSC primary 16G20).
- Dawei Shen, *The singularity category of a Nakayama algebra*, arXiv:1404.2451, first public submission 2014-04-09, https://arxiv.org/abs/1404.2451 (2010 MSC primary 16G10).
- *Square-zero elements in Loewy-length-four cyclic Nakayama algebras: a universal fourth-order recurrence*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-square-zero-elements-in-loewy-length-four-cyclic-nakayama-algebr--25984f72c584/RESULT.md.
