# Exact symmetric-tensor Hilbert series on negative elliptic scrolls

## Finding
Let \(E\) be a smooth complex elliptic curve, let \(L\) be a line bundle of degree \(-d\) on \(E\), with integer \(d\ge1\), and set \(M=\mathbb P_E(\mathcal O_E\oplus L)\), using the quotient-line convention. For **every** integer \(k\ge0\),
\[
h^0\bigl(M,\operatorname{Sym}^k T_M\bigr)=1+d\binom{k+2}{3}.
\]
Consequently the graded algebra of symmetric tensors has numerical Hilbert series
\[
\sum_{k\ge0} h^0\bigl(M,\operatorname{Sym}^kT_M\bigr)t^k
=\frac1{1-t}+\frac{dt}{(1-t)^4}.
\]
For the tautological divisor \(\xi=c_1\bigl(\mathcal O_{\mathbb P(T_M)}(1)\bigr)\) on the threefold \(\mathbb P(T_M)\),
\[
\operatorname{vol}(\xi)=d>0,
\qquad
\int_{\mathbb P(T_M)}\xi^3=0.
\]
The Hilbert function is exact in every weight, not merely asymptotic. The graded ring is known to be non-finitely generated; the rationality of its Hilbert series does **not** assert finite generation.

## Assumptions and scope
All schemes and vector bundles are over \(\mathbb C\). The base \(E\) is any smooth elliptic curve, and \(L\) is any negative-degree line bundle, of arbitrary isomorphism class and integer degree \(-d\), \(d\ge1\). There is no genericity assumption. The dimension formula holds uniformly for all \(k\in\mathbb Z_{\ge0}\). The projective bundle convention is the one for which \(f_*\mathcal O_{\mathbb P(V)}(m)=\operatorname{Sym}^mV\) for \(m\ge0\).

Write \(f:M\to E\) for the ruling, \(C_-\) for the negative section, and \(C_+\) for the disjoint section. Their divisor relations are
\[
C_+\sim C_-+f^*L^*,\quad C_-^2=-d,\quad C_+^2=d,\quad C_-\cdot C_+=0.
\]
These and the elementary transform below are established in Denisi--Höring, Section 3.

## Proof
**1. Comparison with a nef elementary transform.** Denisi--Höring, Lemma 3.3, Proposition 3.5, and the proof of Theorem 1.4, construct a rank-two bundle \(\mathcal F\) fitting into
\[
0\longrightarrow\mathcal O_M(C_+)\longrightarrow\mathcal F
\longrightarrow\mathcal O_M\longrightarrow0,
\qquad
\mathcal F|_{C_-}\simeq\mathscr F_2,
\]
where \(\mathscr F_2\) is the unique nonsplit extension of \(\mathcal O_E\) by \(\mathcal O_E\). Their divisorial Zariski-decomposition argument supplies an isomorphism of **graded section rings**
\[
\bigoplus_{k\ge0}H^0(M,\operatorname{Sym}^kT_M)
\simeq
\bigoplus_{k\ge0}H^0(M,\operatorname{Sym}^k\mathcal F).
\]
In particular, it is enough to compute the dimensions on the right in each weight. This is a previously established structural input, not a new lemma here.

**2. A vanishing filtration.** For a fixed integer \(k\ge0\), put
\(B_k=\operatorname{Sym}^k\mathcal F\otimes\mathcal O_M(-C_-)\).
The symmetric-power filtration induced by the extension in step 1 has line-bundle quotients
\[
\mathcal O_M(jC_+-C_-),\qquad j=0,1,\ldots,k.
\]
For \(j=0\), \(\mathcal O_M(-C_-)\) restricts to \(\mathcal O_{\mathbb P^1}(-1)\) on each ruling fiber, so its degree-zero and degree-one derived direct images vanish, and all its cohomology vanishes.

For every \(j\ge1\), the positive-degree fiber calculation gives
\[
\begin{aligned}
f_*\mathcal O_M(jC_+-C_-)
&\simeq f_*\mathcal O_M((j-1)C_-)\otimes(L^*)^j\\
&\simeq \bigoplus_{i=0}^{j-1}L^i\otimes(L^*)^j
\simeq \bigoplus_{\ell=1}^{j}(L^*)^\ell,
\end{aligned}
\]
with \(R^1f_*\mathcal O_M(jC_+-C_-)=0\). On an elliptic curve, for every \(\ell\ge1\), the bundle \((L^*)^\ell\) has degree \(d\ell>0\); Riemann--Roch and duality therefore yield
\(h^0(E,(L^*)^\ell)=d\ell\) and \(h^1(E,(L^*)^\ell)=0\).
Thus
\[
h^0(M,\mathcal O_M(jC_+-C_-))=d\frac{j(j+1)}2,
\qquad H^1=H^2=0.
\]
Inducting through the filtration, since each quotient has vanishing higher cohomology, gives
\[
H^1(M,B_k)=H^2(M,B_k)=0,
\qquad
h^0(M,B_k)=d\sum_{j=1}^k\frac{j(j+1)}2
=d\binom{k+2}{3}.
\]
These formulas include \(k=0\), where \(B_0=\mathcal O_M(-C_-)\) is acyclic and the sum is empty.

**3. Restriction to the negative section.** Because \(\mathcal F|_{C_-}\simeq\mathscr F_2\), restriction of symmetric powers gives an exact sequence
\[
0\longrightarrow B_k\longrightarrow\operatorname{Sym}^k\mathcal F
\longrightarrow\operatorname{Sym}^k\mathscr F_2\longrightarrow0.
\]
Over \(\mathbb C\), the symmetric powers of the nonsplit Atiyah rank-two bundle have exactly one global section:
\[
h^0(E,\operatorname{Sym}^k\mathscr F_2)=1
\qquad(k\ge0).
\]
This standard Atiyah-bundle fact is also stated for every symmetric power in Denisi--Höring, Example 2.5, through the projective-bundle section calculation. Since \(H^1(M,B_k)=0\), the long exact cohomology sequence makes the restriction map onto this one-dimensional space surjective. Therefore
\[
h^0(M,\operatorname{Sym}^k\mathcal F)
=h^0(M,B_k)+1
=1+d\binom{k+2}{3}.
\]
The graded-ring isomorphism of step 1 proves the first asserted formula for \(T_M\).

**4. Hilbert series and cubic volume.** The elementary formal identity
\[
\sum_{k\ge0}\binom{k+2}{3}t^k=\frac{t}{(1-t)^4}
\]
gives the Hilbert series. By the projective bundle formula,
\(h^0(\mathbb P(T_M),\mathcal O(k))=h^0(M,\operatorname{Sym}^kT_M)\).
Since \(\dim\mathbb P(T_M)=3\), the leading coefficient \(d/6\) implies
\[
\operatorname{vol}(\xi)
=\limsup_{k\to\infty}\frac{3!\,h^0(\mathbb P(T_M),\mathcal O(k))}{k^3}=d.
\]
On the other hand the quotient-projective-bundle pushforward gives
\[
\int_{\mathbb P(T_M)}\xi^3
=\int_M\bigl(c_1(T_M)^2-c_2(T_M)\bigr).
\]
For a smooth \(\mathbb P^1\)-bundle over an elliptic curve, \(c_1(T_M)^2=K_M^2=0\), and \(\int_M c_2(T_M)=e(M)=e(\mathbb P^1)e(E)=0\). Hence this intersection number is zero, as claimed.

## Verification
The standalone standard-library program `VERIFY.py` checks, using exact integer arithmetic, the nested-filtration sum, closed binomial formula, generating-series coefficients, degree-one boundary, and successive differences for degrees \(1\le d\le12\) and weights \(0\le k\le80\). Running `python3 VERIFY.py` prints `VERIFY_OK: 12 degrees, weights 0..80, coefficients and boundaries`.

The infinite assertions are proved by the sheaf exact sequences, elliptic-curve cohomology, and the graded-ring identification in the preceding proof, **not** by this finite computation.

## Relationship to prior work
Denisi--Höring, arXiv:2610.03048v1, prove the bigness and non-finite generation of the symmetric-tensor ring of precisely these elliptic ruled surfaces, develop the elementary transform \(\mathcal F\), and prove the ring identification used in step 1. Their results imply qualitative cubic growth but do not give the displayed exact dimension of every graded piece or its numerical Hilbert series. These structural results and the fact of non-finite generation are credited to them.

Beauville--Liu, arXiv:2309.12888v4, study symmetric-tensor algebras, including a different class of ruled surfaces over curves of genus at least two with stable rank-two bundles. Kim, arXiv:2206.15413v2, studies bigness for projective bundles over curves, including unstable cases; neither inspected work gives the exact formula above. The claim here is only this numerical Hilbert-function determination and its stated consequences; it does not claim the pre-existing bigness or non-finite-generation theorem as new.

## Limitations
The statement concerns the split ruled surfaces \(\mathbb P_E(\mathcal O_E\oplus L)\) with \(\deg L<0\) in characteristic zero. It does not assert the same formula for nonsplit ruled surfaces, degree-zero bundles, positive-characteristic elliptic curves, or arbitrary higher-dimensional bundles. The displayed rational Hilbert series does not imply that the section ring is finitely generated; in fact Denisi--Höring prove that it is not. The source identification of graded sections is a cited mathematical input, not independently reproved here. General bibliographic searches cannot exclude an older equivalent calculation not indexed under these terms.

## References
1. F. A. Denisi and A. Höring, *Canonical extensions of ruled surfaces over elliptic curves*, arXiv:2610.03048v1 (first public October 2, 2026), https://arxiv.org/html/2610.03048v1, especially Example 2.5, Lemma 3.3, Proposition 3.5, and proof of Theorem 1.4.
2. A. Beauville and J. Liu, *The algebra of symmetric tensors on smooth projective varieties*, arXiv:2309.12888v4, https://arxiv.org/html/2309.12888v4, especially Section 2.8.
3. J.-S. Kim, *Bigness of the tangent bundles of projective bundles over curves*, arXiv:2206.15413v2, https://arxiv.org/html/2206.15413v2.
4. M. F. Atiyah, *Vector Bundles Over an Elliptic Curve*, Proceedings of the London Mathematical Society (1957), DOI:10.1112/plms/s3-7.1.414.
