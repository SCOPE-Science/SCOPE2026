# Derivation Lie algebras of non-dihedral prime Alexander quandles in defining characteristic

## Finding
Let \(p\ge5\) be prime, \(K\) any field of characteristic \(p\), and \(a\in\mathbb F_p\setminus\{0,1,-1\}\). Put \(b=1-a\), and let \(A=K[Q_{p,a}]\) be the nonassociative algebra with basis \(\{e_x:x\in\mathbb F_p\}\) and multiplication \(e_x\star e_y=e_{ax+by}\). Let
\[
L=\operatorname{lcm}(\operatorname{ord}_p(a),\operatorname{ord}_p(b)),\quad m=(p-1)/L,
\qquad D=\{1\le d<p:a^d+b^d=1\}.
\]
All powers and equalities defining \(D\) are taken in \(\mathbb F_p\). Write \(R=K[T]/(T^p)\) with its **ordinary associative multiplication** and \(\partial=d/dT\). Under the group-ring transport described below, every quandle-algebra derivation is uniquely
\[
\boxed{\delta=\sum_{d\in D}c_dM_{T^d}+\sum_{j=0}^{m-1}z_jT^{1+jL}\partial,\qquad c_d,z_j\in K.}
\]
Consequently
\[
\boxed{\dim_K\operatorname{Der}(A)=|D|+m.}
\]
For \(K=\mathbb F_q\), there are precisely \(q^{|D|+m}\) \(K\)-linear derivations. If \(H_d=M_{T^d}\) and \(V_j=T^{1+jL}\partial\), all Lie brackets are
\[
[H_d,H_e]=0,\quad
[V_i,V_j]=\begin{cases}(j-i)L V_{i+j},&i+j<m,\\0,&i+j\ge m,\end{cases}
\quad
[V_j,H_d]=\begin{cases}dH_{d+jL},&d+jL<p,\\0,&d+jL\ge p.\end{cases}
\]
Thus the derivation algebra is a semidirect product of an abelian multiplication ideal with a truncated polynomial-vector-field Lie algebra. This is a complete description of the Lie structure, not only a dimension calculation.

For \(p=7\), the non-dihedral parameters \(a=2,3,4\) give respectively \((D,L,m)=(\{1\},6,1)\), \((\{1,5\},6,1)\), and \((\{1,4\},3,2)\). The dimensions are \(2,3,4\) over **every** field of characteristic seven.

## Assumptions and scope
The coefficient field has characteristic \(p\), and \(a,b\) are both nonzero. This makes both scalar actions invertible and the underlying Alexander quandle Latin. We exclude \(a=-1\): its dihedral specialization has already been studied and is not asserted to be new. We do not assume that \(K\) is finite or algebraically closed. The identification with \(R\) is an identification of vector spaces, **not** an assertion that the quandle algebra is associative.

Let \(X\) denote the generator of the ordinary group algebra \(K[C_p]=K[X]/(X^p-1)\). Put \(t=X-1\). Since \(t^p=0\), define the truncated logarithm
\[
T=\log(1+t)=\sum_{r=1}^{p-1}(-1)^{r+1}t^r/r.
\]
Then \(T=t+O(t^2)\), so \(R=K[T]/(T^p)\). The inverse change of variables is the truncated exponential \(X=\exp(T)=\sum_{r=0}^{p-1}T^r/r!\). The denominators are invertible because all relevant indices are less than \(p\).

## Proof
**1. Transport and a general derivation splitting.** Under \(e_x\mapsto X^x\), the quandle multiplication transports to
\[
u\star v=\alpha(u)\,\beta(v),\]
where ordinary multiplication is used on the right, \(\alpha(X)=X^a\), and \(\beta(X)=X^b\). The maps \(\alpha,\beta\) are commuting automorphisms of \(R\). For \(h\in R\), denote ordinary multiplication by \(h\) by \(M_h\).

Let \(\delta\) be any \(K\)-linear derivation for \(\star\), and let \(h=\delta(1)\), where \(1=X^0=e_0\). Since \(1\star1=1\), the Leibniz rule gives
\[
h=\alpha(h)+\beta(h).
\]
Conversely, whenever this equality holds, \(M_h\) is a derivation of the transported quandle multiplication, because
\[
M_h(u\star v)=h\alpha(u)\beta(v)
=(\alpha(h)+\beta(h))\alpha(u)\beta(v)
=M_h(u)\star v+u\star M_h(v).
\]
Put \(\varepsilon=\delta-M_h\). Then \(\varepsilon(1)=0\). Applying the derivation rule to \(u\star1=\alpha(u)\) and \(1\star v=\beta(v)\) gives \(\varepsilon\alpha=\alpha\varepsilon\) and \(\varepsilon\beta=\beta\varepsilon\). For arbitrary \(r,s\in R\), write \(r=\alpha(u)\), \(s=\beta(v)\), possible because both automorphisms are onto. The \(\star\)-Leibniz rule becomes
\[
\varepsilon(rs)=\varepsilon(r)s+r\varepsilon(s).
\]
Therefore \(\varepsilon\) is an **ordinary associative** derivation of \(R\), commuting with both \(\alpha\) and \(\beta\). The converse follows by reversing the argument. We have proved the unique splitting
\[
\operatorname{Der}(A)
=\{M_h:h=\alpha(h)+\beta(h)\}
\oplus\{\varepsilon\in\operatorname{Der}_K(R):\varepsilon\alpha=\alpha\varepsilon,\ \varepsilon\beta=\beta\varepsilon\}.
\]
Uniqueness follows from the value at \(1\); all ordinary ring derivations kill \(1\).

**2. Diagonal coordinates.** Formal logarithm identities modulo \(t^p\) give \(\alpha(T)=aT\) and \(\beta(T)=bT\). This holds in characteristic \(p\) because every coefficient and denominator used below degree \(p\) is defined. Write \(h=\sum_{d=0}^{p-1}c_dT^d\). The equation \(h=\alpha(h)+\beta(h)\) forces \(c_0=0\) and permits \(c_d\) exactly when \(a^d+b^d=1\). Hence the multiplication-operator summand has basis \(H_d\), \(d\in D\).

Every ordinary associative derivation of \(K[T]/(T^p)\) is uniquely \(f(T)\partial\) for an arbitrary \(f\in R\): a derivation is determined by its value at \(T\), and the relation \(T^p=0\) imposes no constraint in characteristic \(p\). Commutation with \(\alpha\) is equivalent to \(\alpha(f)=af\), and similarly with \(\beta\) to \(\beta(f)=bf\). Thus if \(f=\sum f_dT^d\), nonzero coefficients occur exactly when \(a^{d-1}=b^{d-1}=1\). The constant term cannot occur because \(a\ne1\). Letting \(L\) be the least common multiple of the two multiplicative orders, the allowable degrees are exactly \(1+jL\), \(0\le j<m\), since \(L\mid p-1\). This proves the claimed basis, dimension, and finite-field count.

**3. Brackets.** Ordinary multiplication operators commute. For ordinary associative derivations \(E,F\) and \(h\in R\), the operator identity \([E,M_h]=M_{E(h)}\) follows from the Leibniz rule. For \(V_j=T^{1+jL}\partial\), this gives \([V_j,H_d]=dH_{d+jL}\), with truncation at exponent \(p\). The output degree still belongs to \(D\) when it is below \(p\), since \(a^L=b^L=1\). Finally the commutator of polynomial vector fields is
\[
[f\partial,g\partial]=(fg'-gf')\partial,
\]
so \([V_i,V_j]=(j-i)L V_{i+j}\) when the target degree is below \(p\), and zero otherwise. These identities exhaust the bracket table. No characteristic-zero or experimental inference is used.

## Verification
The accompanying standard-library-only program `verify.py` constructs the quandle derivation equations directly in the original \(p\)-element basis. It computes their exact nullity by modular Gaussian elimination, and separately converts each claimed multiplication or differential generator from ordinary truncated-polynomial coordinates to the original basis and checks every Leibniz equation. All allowable scalar parameters were checked for \(p=3,5,7,11\) (the smaller and dihedral choices are boundary controls), with further generator checks for \(p=17,19,31\). Brackets were checked by direct matrix commutators for selected \(p=7,11,17\) cases. The output ends `VERIFY_OK`. See `verification_output.txt` for all cases; the test domain is finite and does not constitute the infinite proof.

## Relationship to prior work
Zhang (2026) establishes the group-ring transport \(u\star v=\alpha(u)\beta(v)\) and studies augmentation powers, commutator subalgebras, integral idempotents, and Peirce spectra. **That transport is a prior result, not claimed new here.** Elhamdadi, Makhlouf, Silvestrov and Zappala (2021) give the general structure-constant derivation equations, the characteristic-zero dihedral classification, and small positive-characteristic examples, including order three in characteristic three. The dihedral defining-characteristic case has previously been treated and is explicitly excluded from the present originality claim. The claim here is the complete all-prime, non-dihedral scalar classification in defining characteristic, including its Lie bracket and parameter-dependent dimension jumps. Sangare and Ta (2026) treat automorphisms, idempotents and commutator widths, not this derivation Lie algebra. The literature comparison does not establish absolute historical priority.

## Limitations
The theorem is restricted to scalar Latin quandles on prime-order additive groups and coefficient characteristic equal to that prime. It excludes the dihedral parameter and does not classify non-scalar Alexander actions, general composite-order quandles, quandle automorphisms, or cohomology. A general older derivation theorem stated in different language could conceivably subsume the result; such historical equivalence has not been ruled out by exhaustive literature indexing.

## References
- Zhi-Lin Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1, 6 October 2026, especially Section 2.1.
- M. Elhamdadi, A. Makhlouf, S. Silvestrov and E. Zappala, *The derivation problem for quandle algebras*, arXiv:2106.08289v1, 15 June 2021, Sections 3 and 4.2.
- Birama Sangare and Luc Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v1, 3 August 2026, Sections 3–5.
