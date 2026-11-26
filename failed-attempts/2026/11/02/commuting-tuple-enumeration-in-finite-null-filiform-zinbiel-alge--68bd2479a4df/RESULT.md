# Commuting-tuple enumeration in finite null-filiform Zinbiel algebras

## Finding
For each integer \(n\ge2\), integer \(k\ge1\), and finite field \(\mathbb F_q\) whose characteristic \(p\) satisfies \(p>n\), the null-filiform Zinbiel algebra \(Z_n\) has an exact all-arity enumeration of commuting ordered tuples. Here *commuting* means \(x\circ y=y\circ x\), not that either product vanishes. Put \(h=\lfloor n/2\rfloor\). Then
\[
N_{n,k}(q)=1+(q^k-1)\left(\sum_{r=1}^{h}q^{n-2r+rk}+\sum_{r=h+1}^{n}q^{k(n-r)}\right).
\]
For a nonzero element \(x\) whose lowest nonzero coefficient is at basis index \(r\), its commutant \(C(x)=\{y\in Z_n:x\circ y=y\circ x\}\) has dimension
\[
\dim_{\mathbb F_q}C(x)=\begin{cases}r+1,&2r\le n,\\r,&2r>n.\end{cases}
\]
In particular,
\[
N_{n,2}(q)=q^n\left[1+(q-1)\bigl(n+(q-1)h\bigr)\right].
\]
At fixed \(n,q\), as \(k\to\infty\),
\[
N_{n,k}(q)\sim \begin{cases}q^{(h+1)k},&n=2h,\\(q+1)q^{(h+1)k},&n=2h+1.\end{cases}
\]
The parity factor is a second structural consequence of the all-arity exact count.

## Assumptions and scope
The algebra has \(\mathbb F_q\)-basis \(e_1,\ldots,e_n\), with multiplication extended bilinearly from
\[
e_i\circ e_j=\begin{cases}\binom{i+j-1}{j}\,e_{i+j},&i+j\le n,\\0,&i+j>n.\end{cases}
\]
The characteristic restriction \(p>n\) ensures that every factorial through degree \(n\), and every nonzero index difference of magnitude less than \(n\), is invertible. It is essential to the following valuation argument; no claim is made here for smaller characteristic. The algebra is not assumed associative, and commutativity of two elements is distinct from zero multiplication. Define \(\operatorname{ord}(0)=\infty\) and \(\operatorname{ord}(\sum a_i e_i)=\min\{i:a_i\ne0\}\) otherwise. The tuple count includes zero coordinates and the all-zero tuple.

## Proof
First compute the coefficient of \(e_s\) in the commutator. For \(2\le s\le n\),
\[
[e_i,e_j]_{\circ}:=e_i\circ e_j-e_j\circ e_i=\frac{(s-1)!(i-j)}{i!j!}e_s\quad (i+j=s).
\]
Consequently, associating \(x=\sum_i a_i e_i\) with \(F_x(t)=\sum_i a_i t^i/i!\), two elements commute precisely when
\[
F_x'(t)F_y(t)-F_x(t)F_y'(t)\equiv0\pmod {t^n}.
\]
This *truncated Wronskian* is a test for commutation; it is not asserted to be an isomorphism of algebra products.

Fix a nonzero \(x\) of order \(r\). If \(2r\le n\), an element \(y\) commuting with \(x\) cannot have order \(s<r\), because the coefficient of \(e_{r+s}\) in their commutator would be a nonzero scalar multiple of \((r-s)a_rb_s\). Subtract \(\lambda x\) from \(y\), with \(\lambda\) chosen to remove the coefficient of \(e_r\). If the first remaining nonzero coefficient had index \(s\) with \(r<s\le n-r\), the coefficient of \(e_{r+s}\) would again be nonzero. Thus
\[
C(x)=\mathbb F_q x\oplus\operatorname{span}(e_{n-r+1},\ldots,e_n),\qquad 2r\le n.
\]
Conversely every element of the displayed sum commutes with \(x\), since the tail has product zero with every term of \(x\). The sum is direct, of dimension \(r+1\).

If \(2r>n\), a commuting element \(y\) cannot have any nonzero coefficient of index \(s\le n-r\): its lowest such coefficient would produce a nonzero commutator coefficient at \(e_{r+s}\). Conversely all terms with index \(s>n-r\) have degree sum exceeding \(n\) when paired with \(x\). Hence
\[
C(x)=\operatorname{span}(e_{n-r+1},\ldots,e_n),\qquad2r>n,
\]
which has dimension \(r\). The coefficient argument uses only field elements of index difference less than \(p\), so no cancellation at the first possible degree is missed.

Count pairwise-commuting ordered tuples by their minimal finite order \(r\); add the all-zero tuple separately. When \(r\le h\), choose a tuple coordinate of order \(r\). Applying its commutant formula to each of the other coordinates, every coefficient row with degrees \(r,\ldots,n-r\) is a scalar multiple of one nonzero \(k\)-vector \(v\), and the row at degree \(r\) itself is \(v\). Conversely any choice of these proportional rows and arbitrary higher coefficient rows gives a commuting tuple: its terms are scalar multiples of a common element plus tails of degree above \(n-r\). There are \(q^k-1\) possibilities for \(v\), exactly \(n-2r\) subsequent proportional rows with \(q\) choices each, and \(r\) free upper rows with \(q^k\) choices each. This yields \((q^k-1)q^{n-2r+rk}\).

For \(r>h\), every tuple coordinate has order at least \(r\), so every pair of their products vanishes. Requiring at least one degree-\(r\) coefficient to be nonzero gives \(q^{k(n-r+1)}-q^{k(n-r)}=(q^k-1)q^{k(n-r)}\) tuples. Summing the disjoint cases proves the formula.

For \(k=2\), one may also count directly from commutant dimensions: there are \((q-1)q^{n-r}\) elements of each order \(r\), plus zero; this gives the stated simplified formula. Finally, in the exact all-arity sum the largest exponential base as \(k\to\infty\) is \(q^{h+1}\); it occurs with leading coefficient \(1\) for \(n=2h\) and with the two contributions \(q+1\) for \(n=2h+1\). This proves the parity limit.

## Verification
The accompanying standalone standard-library program `verify.py` constructs the original multiplication coefficients and tests all ordered commuting pairs and triples for \((q,n)=(3,2),(5,2),(5,3),(5,4),(7,3)\). It also checks all individual commutant dimensions and all basis triples of the defining Zinbiel identity. Invoke `python3 verify.py`. The expected terminal line is `VERIFY_OK 5 exhaustive independent pair/triple censuses and centralizer checks`. The enumeration includes \(\mathbb F_5\)-dimension \(4\), where there are \(30{,}625\) commuting pairs and \(2{,}340{,}625\) commuting triples. These tests confirm finite instances; the complete infinite-parameter result follows from the proof above, not from enumeration.

## Relationship to prior work
The standard null-filiform Zinbiel multiplication is established in Camacho–Karimjanov–Kaygorodov–Khudoyberdiyev (2020, Theorem 2), which concerns classification and central extensions. Ceballos–Towers (2022, Proposition 4.2) establishes the dimension and uniqueness of a maximal **zero-product abelian ideal** over \(\mathbb C\); this does not count finite-field tuples whose two products merely agree. Dzhumadil'daev–Ismailov–Mashurov (2018) studies the commutator construction and speciality of Tortkara algebras, rather than the finite-field commuting-tuple enumeration. The earlier Dzhumadil'daev work on Zinbiel commutators develops polynomial identities, but its complete text was not inspected. The present result does not claim the algebra model, the general commutator construction, or the earlier zero-product ideal theorem as new.

## Limitations
The formula is proved only when \(\operatorname{char}(\mathbb F_q)>n\). It does not count zero-product tuples or classify all commuting subalgebras. The same finite-field model is defined in smaller characteristics, but additional modular cancellations can invalidate the valuation proof. The exact formula and structural consequences have received a self-review; their publication priority is provisional, and independent mathematical audit has not been performed. A general commutator-enumeration result under different terminology could imply this statement.

## References
1. L. M. Camacho, I. Karimjanov, I. Kaygorodov and A. Khudoyberdiyev, *Central extensions of filiform Zinbiel algebras*, arXiv:2009.00988v1 (1 September 2020), Theorem 2. https://arxiv.org/abs/2009.00988
2. M. Ceballos and D. A. Towers, *Abelian subalgebras and ideals of maximal dimension in Zinbiel algebras*, arXiv:2202.03214v1 (7 February 2022), Proposition 4.2. https://arxiv.org/abs/2202.03214
3. A. S. Dzhumadil'daev, N. A. Ismailov and F. A. Mashurov, *On the speciality of Tortkara algebras*, arXiv:1809.10550v1 (27 September 2018), Sections 1–3. https://arxiv.org/abs/1809.10550
4. A. S. Dzhumadil'daev, *Zinbiel algebras under q-commutator*, Fundam. Prikl. Mat. 11(3) (2005), 57–78; English translation J. Math. Sci. 144 (2007), 3909–3925. https://www.mathnet.ru/eng/fpm828
