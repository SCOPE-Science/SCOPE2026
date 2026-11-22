# Rank gaps and finite-field spectra of square-zero cubic-jet substitutions

## Finding

Fix an integer \(d\ge1\), a finite field \(k=\mathbb F_q\) (any characteristic), the cubic jet algebra
\[
A_d=k[x_1,\ldots,x_d]/(x_1,\ldots,x_d)^3,
\]
and its maximal ideal \(\mathfrak m\). Write \(\epsilon:A_d\to A_d\) for the augmentation followed by inclusion of constants. We classify all *unital, scalar-fixing algebra endomorphisms* \(f\) whose second iterate is \(\epsilon\). Let the **radical rank** mean \(\operatorname{rank}_k(f|_{\mathfrak m})\); the ordinary linear rank on \(A_d\) is exactly one greater.

Use the Gaussian coefficient \({n\brack j}_q=\prod_{i=0}^{j-1}(q^{n-i}-1)/(q^{j-i}-1)\), with the usual empty product conventions, and \(G_r(q)=\prod_{i=0}^{r-1}(q^r-q^i)\). For \(0\le r\le\lfloor d/2\rfloor\), put
\[
s=\binom{d+1}{2},\quad c_r=\binom{r+1}{2},\quad a_r=d-2r,\quad b_r=s-2c_r,\quad H_{d,r}=(d-r)s-a_rc_r.
\]
The exact radical-rank enumerator is
\[
\boxed{\mathcal P_{d,q}(z)=\sum_{r=0}^{\lfloor d/2\rfloor}{d\brack r}_q{d-r\brack r}_qG_r(q)q^{H_{d,r}-a_rb_r}\sum_{t=0}^{a_r}{a_r\brack t}_q\left(\prod_{j=0}^{t-1}(q^{b_r}-q^j)\right)z^{r+c_r+t}.}
\]
In particular the count with linear-part rank \(r\), without rank refinement, is precisely
\[
\boxed{N_{d,r}(q)={d\brack r}_q{d-r\brack r}_q G_r(q)q^{H_{d,r}}.}
\]
The *entire support* consists of the integer intervals
\[
\boxed{I_r=\{r+c_r,r+c_r+1,\ldots,d+\tbinom r2\},\quad 0\le r\le\lfloor d/2\rfloor.}
\]
Between successive intervals \(I_r\) and \(I_{r+1}\), exactly \(\max(0,3r+1-d)\) integers are absent; the nonempty gaps are disjoint. The first missing rank is \(8\) in generator dimension \(d=6\), with support \(\{0,1,\ldots,7,9\}\). In generator dimension \(d=12\), the missing ranks are \(19,23,24,25,26\).

For every fixed \(q\), if \(f\) is uniformly chosen from these endomorphisms, then
\[
\Pr(\operatorname{rank}(f\bmod\mathfrak m^2)>0)=O_q\!\left(dq^{-d(d-3)/2}\right),\quad d\to\infty.
\]
Thus composition-square roots of augmentation overwhelmingly have zero first-order action, despite allowing nonzero quadratic maps. This is a classification of actual labeled endomorphisms, not a similarity-orbit count.

## Assumptions and scope

All maps fix each element of \(k\), and every image of a variable belongs to \(\mathfrak m\). There is no restriction on the prime characteristic, including the characteristics two and three. The rank variable tracks only the restriction to \(\mathfrak m\); \(f(1)=1\) contributes one additional dimension to full rank. The equation \(f^2=\epsilon\) is **composition** of algebra maps and is distinct from the elementwise square-zero equation or the derivation equation \(D^2=0\).

## Proof

**1. Free quadratic coordinates.** Write \(V=\mathfrak m/\mathfrak m^2\) and \(W=\mathfrak m^2\cong\operatorname{Sym}^2 V\), of dimensions \(d\) and \(s\). Because all triple products vanish, an endomorphism is uniquely specified by arbitrary linear maps \(B:V\to V\) and \(Q:V\to W\), with
\[
f|_{\mathfrak m}=\begin{pmatrix}B&0\\Q&\operatorname{Sym}^2B\end{pmatrix}.
\]
Let \(R=\operatorname{Sym}^2B\). Squaring this block matrix shows that \(f^2=\epsilon\) holds if and only if
\[
B^2=0,\qquad QB+RQ=0.
\]
The remaining block \(R^2=\operatorname{Sym}^2(B^2)\) then vanishes. The calculation is valid in every characteristic and uses ordinary symmetric powers, not division by two.

**2. Linear-part strata.** Suppose \(\operatorname{rank}B=r\). Since \(B^2=0\), \(0\le r\le\lfloor d/2\rfloor\), and its Jordan decomposition has \(r\) blocks of size two and \(a_r=d-2r\) blocks of size one. Choosing \(\operatorname{im}B\), then \(\ker B\supset\operatorname{im}B\), then an isomorphism \(V/\ker B\to\operatorname{im}B\), gives exactly \({d\brack r}_q{d-r\brack r}_qG_r(q)\) possible \(B\)'s.

**3. Symmetric-square Jordan structure.** Choose a basis with \(B(w_i)=u_i\) for \(i=1,\ldots,r\), and \(B\) zero on the remaining basis vectors. On \(W\), the operator \(R=\operatorname{Sym}^2B\) maps \(w_iw_j\mapsto u_iu_j\) and kills all monomials involving a \(u\) or an additional kernel vector. Hence it has precisely \(c_r=\binom{r+1}{2}\) independent two-step blocks and \(b_r=s-2c_r\) one-step blocks. This statement holds even in characteristic two: diagonal monomials \(w_i^2\) map to distinct \(u_i^2\) and no averaging is used.

**4. Intertwiner fibers.** Regard \((V,B)\) and \((W,-R)\) as modules over \(k[\tau]/(\tau^2)\). The relation \(QB+RQ=0\) states exactly that \(Q\) is a module map. The dimensions of module homomorphism spaces between blocks \(J_2\to J_2\), \(J_2\to J_1\), \(J_1\to J_2\), \(J_1\to J_1\) are \(2,1,1,1\). Consequently the vector-space dimension of allowable \(Q\)'s is
\[
2rc_r+rb_r+a_rc_r+a_rb_r=(d-r)s-a_rc_r=H_{d,r}.
\]
This yields the unrefined count. Every such \(Q\) induces a well-defined map
\[
\overline Q:\ker B/\operatorname{im}B\longrightarrow\ker R/\operatorname{im}R,
\]
from an \(a_r\)-space to a \(b_r\)-space. This map is arbitrary (choose compatible Jordan bases and lift any linear map on the one-step direct summands), and every prescribed map has exactly \(q^{H_{d,r}-a_rb_r}\) lifts. The radical rank satisfies
\[
\operatorname{rank}(f|_{\mathfrak m})=r+c_r+\operatorname{rank}\overline Q,
\]
since the image projection onto \(V\) has dimension \(r\) and its intersection with \(W\) is \(Q(\ker B)+\operatorname{im}R\). Counting arbitrary rank-\(t\) maps between spaces of dimensions \(a_r,b_r\) gives \({a_r\brack t}_q\prod_{j=0}^{t-1}(q^{b_r}-q^j)\), proving the rank polynomial.

**5. Exact attainable ranks and gaps.** Directly from the dimensions, \(b_r\ge a_r\) for \(r\le d/2\): indeed \(b_r-a_r=d(d-1)/2-r(r-1)\ge0\). Therefore the rank \(t\) above can be any integer from \(0\) to \(a_r\), giving precisely the stated intervals \(I_r\). Their left endpoints strictly increase, and their right endpoints are nondecreasing. The difference between the next left endpoint and the preceding right endpoint, minus one, equals
\[
\left((r+1)+\binom{r+2}{2}\right)-\left(d+\binom r2\right)-1=3r+1-d.
\]
Positive differences are exactly the missing-rank gap lengths. Their count grows without bound as \(d\) grows, as witnessed for instance by choosing any \(r\) in the interval \(d/3\le r<d/2\).

**6. Large-generator concentration.** The zero-linear-part stratum has exactly \(q^{ds}\) maps. For \(r>0\), the number of square-zero linear parts is
\[
{d\brack r}_q{d-r\brack r}_qG_r(q)
=q^{2r(d-r)}\frac{\Phi_d(q)}{\Phi_r(q)\Phi_{d-2r}(q)},
\quad \Phi_j(q)=\prod_{i=1}^j(1-q^{-i}).
\]
With \(\Phi_\infty(q)>0\), this is bounded by \(\Phi_\infty(q)^{-2}q^{2r(d-r)}\). Moreover \(ds-H_{d,r}=rs+(d-2r)c_r\ge rs\). Therefore for \(d\ge4\) the ratio of the \(r\)-th stratum to the zero-linear-part stratum is at most
\[
\Phi_\infty(q)^{-2}q^{2r(d-r)-rs}
\le\Phi_\infty(q)^{-2}q^{-rd(d-3)/2}.
\]
Summing over the at most \(d/2\) positive ranks proves the probability estimate and completes the proof.

## Verification

The standalone Python 3 program `verify.py` checks the equation on actual truncated-polynomial coordinates, not merely matrix-rank logs. It independently constructs the linear constraint matrix for \(Q\) at every canonical \(B\) of rank \(r\) for \(d=1,\ldots,6\) over the prime fields of orders \(2,3,5\), verifying its predicted nullity. It exhaustively enumerates all endomorphisms for \(d=2\), \(q=2\) and \(q=3\), evaluates the second iterate, and checks the resulting rank distributions:
\[
\mathcal P_{2,2}(z)=1+21z+66z^2,\qquad \mathcal P_{2,3}(z)=1+104z+840z^2.
\]
It also checks predicted support gaps through \(d=16\). The saved `verification_output.txt` contains the actual output; running `python3 verify.py` reproduces it. Finite checks corroborate but are not the general proof.

## Relationship to prior work

Lipyanski (2005), whose original public arXiv submission is dated 2005-11-27, develops the automorphism group of the *endomorphism semigroup* of homogeneous and nilpotent free algebras. The paper's Theorem B and Example 7.2 concern symmetries of an endomorphism semigroup; they do not give the elementwise composition-square-root count or the radical-rank support for the commutative cubic jet algebra. The published archive's primary 08A35 classification is consistent with the endomorphism-monoid setting here.

A closely related recorded result, *Retracts and idempotent endomorphisms of cube-zero truncated symmetric algebras*, treats the **same commutative algebra** but the different equation \(f^2=f\), so its projection and image-count formulas do not imply this square-zero composition census. Another recorded result, *Complete rank spectra of square-zero endomorphisms of free two-step nilpotent associative algebras*, treats the **noncommutative tensor-square algebra** \(V\oplus(V\otimes V)\), not the commutative symmetric-square quotient. Its module-intertwiner technique is acknowledged as closely analogous; neither its fiber exponents nor its rank-gap intervals specialize automatically to the symmetric algebra because the quadratic target, rank of the induced quadratic map, and homology dimensions change. A related cubic-jet result about ordinary **derivations** satisfies the Leibniz rule rather than algebra-homomorphism substitution. The theorem here is the exact all-characteristic symmetric-quotient count and its entire sharp gap geometry, not an assertion of a new general module-intertwiner principle.

## Limitations

Only total-degree-three commutative truncations and the composition equation \(f^2=\epsilon\) are treated. There is no claim for higher truncation degrees, for all nilpotency orders, for isomorphism-orbit counts, or for scheme-theoretic nonreduced structure. A closely analogous noncommutative calculation is known; broader algebra-endomorphism literature may contain an implicit equivalent symmetric quotient specialization, a residual priority risk. 

## References

1. R. Lipyanski, *Automorphisms of the semigroup of endomorphisms of free algebras of homogeneous varieties*, arXiv:math/0511654, first submitted 2005-11-27, especially Theorem B and Example 7.2. https://arxiv.org/abs/math/0511654
2. *Retracts and idempotent endomorphisms of cube-zero truncated symmetric algebras*, research record, 2026-10-13, full RESULT.md inspected: https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-retracts-and-idempotent-endomorphisms-of-cube-zero-truncated-sym--d0314edd48d9
3. *Complete rank spectra of square-zero endomorphisms of free two-step nilpotent associative algebras*, research record, 2026-11-08, full RESULT.md inspected: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-rank-spectra-of-square-zero-endomorphisms-of-free-two-s--5cd226e099e3
4. *Square-zero derivation rank spectra of quadratic-jet algebras*, research record, 2026-10-13: https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-square-zero-derivation-rank-spectra-of-quadratic-jet-algebras--7ddabb22ee5d
