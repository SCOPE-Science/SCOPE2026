# Arithmetic dimension jumps for modular dihedral-quandle idempotents

## Finding

**Theorem.** Let \(p\ge 3\) be any odd prime, \(k\) any field of characteristic \(p\), and \(R_p=\mathbb Z/p\mathbb Z\) the dihedral quandle with operation \(i*j=2j-i\). Form the (generally nonassociative, nonunital) quandle algebra \(k[R_p]\) with basis \(e_i\) and multiplication \(e_i e_j=e_{2j-i}\). Write
\[
h=\operatorname{ord}_{p}(2),\qquad \ell=\operatorname{lcm}(2,h),\qquad d=(p-1)/\ell.
\]
Then the set of idempotents is precisely the disjoint union of \(\{0\}\) and an explicit affine \(k\)-space of dimension \(d\). The nonzero idempotents, under quandle-algebra multiplication, form a subquandle isomorphic to the additive core quandle \(\operatorname{Core}(k^d,+)\), whose operation is \(x*y=2y-x\).

In particular, if \(k=\mathbb F_q\) and \(q=p^e\), the **exact total number of idempotents** is
\[
1+q^d=1+q^{(p-1)/\operatorname{lcm}(2,\operatorname{ord}_p(2))}.
\]
The first arithmetically nontrivial jump occurs at \(p=17\), when \(d=2\): over \(\mathbb F_{17}\) there are \(290\) idempotents, including \(272\) nonzero idempotents that are not basis elements. For \(p=31\), \(d=3\).

**Explicit parameterization.** Introduce the *auxiliary associative* cyclic group algebra \(U=k[t]/(t^p-1)\), with augmentation ideal \(J=(t-1)\). Its underlying vector space is identified with \(k[R_p]\) by \(t^i\leftrightarrow e_i\); these two algebras have **different multiplications**. For any \(a\in\mathbb F_p^\times\), let \(\sigma_a(t^i)=t^{ai}\) be an automorphism of the *associative* algebra \(U\). For \(1\le r\le p-1\), define
\[
v_r=\sum_{i=1}^{p-1} i^{-r}(t^i-1)\in J,
\]
where coefficients \(i^{-r}\) are taken in the prime subfield. Let
\[
W=\operatorname{span}_k\{v_{1+j\ell}:0\le j<d\}.
\]
Define the truncated exponential, using multiplication only in \(U\), by
\[
\operatorname{Exp}(z)=\sum_{m=0}^{p-1}\frac{z^m}{m!}\quad (z\in J).
\]
All nonzero idempotents of \(k[R_p]\) are uniquely
\[
\operatorname{Exp}\left(\sum_{j=0}^{d-1}c_j v_{1+j\ell}\right),\qquad (c_0,\ldots,c_{d-1})\in k^d.
\]
Their quandle-algebra multiplication is the explicit rule
\[
\operatorname{Exp}(z)*\operatorname{Exp}(w)=\operatorname{Exp}(-z+2w)\quad(z,w\in W).
\]

## Assumptions and scope

The phrase “affine space” means a polynomially parameterized variety isomorphic to affine \(d\)-space, not necessarily a linear translate in the original basis coefficients. The coefficient field may be finite or infinite, but must have the same characteristic \(p\) as the odd prime number of quandle elements. The assertions concern *all* idempotents, not just integral-coefficient or bounded-support idempotents. The group algebra \(U\) is used solely as a vector-space model and auxiliary associative algebra; its ordinary idempotents are not being classified. The zero idempotent is counted separately and is not a member of the nonzero idempotent subquandle.

## Proof

**Step 1: Transform the nonassociative product.** In the cyclic group algebra \(U\), an equality on basis elements gives
\[
(t^i)*(t^j)=t^{2j-i}=\sigma_{-1}(t^i)\,\sigma_2(t^j).
\]
The juxtaposition on the right is ordinary associative multiplication in \(U\). Bilinearity therefore implies
\[
x*y=\sigma_{-1}(x)\,\sigma_2(y)\qquad(x,y\in U).
\]
The usual augmentation \(\varepsilon:U\to k\) satisfies \(\varepsilon(x*y)=\varepsilon(x)\varepsilon(y)\). Thus any idempotent \(x*x=x\) has \(\varepsilon(x)=0\) or \(1\).

**Step 2: Exclude nonzero augmentation-zero solutions.** Since \(t^p-1=(t-1)^p\) in characteristic \(p\), the ideal \(J=(t-1)\) has \(J^p=0\). If \(x*x=x\) and \(x\in J\), then \(x=\sigma_{-1}(x)\sigma_2(x)\in J^2\). As each \(\sigma_a\) preserves every \(J^s\), induction gives \(x\in J^{2^m}\) for all nonnegative integers \(m\). Choosing \(2^m\ge p\) yields \(x=0\).

**Step 3: Linearize all augmentation-one solutions.** The elements of augmentation one are \(1+J\), a multiplicative group of the *associative* algebra \(U\). Because \(J^p=0\), the finite polynomials
\[
\operatorname{Log}(1+z)=\sum_{m=1}^{p-1}\frac{(-1)^{m+1}z^m}{m},\qquad
\operatorname{Exp}(z)=\sum_{m=0}^{p-1}\frac{z^m}{m!}
\]
are mutual inverses between \(1+J\) and \(J\). In fact, they are group isomorphisms from associative multiplication on \(1+J\) to addition on \(J\): for commuting \(z,w\in J\), terms of total degree \(\ge p\) vanish and the standard truncated exponential identity gives \(\operatorname{Exp}(z)\operatorname{Exp}(w)=\operatorname{Exp}(z+w)\). All denominators shown are invertible since their integers are less than \(p\). Both functions commute with \(\sigma_a\).

For \(x=\operatorname{Exp}(z)\), the idempotence equation becomes
\[
\operatorname{Exp}(z)=\sigma_{-1}(\operatorname{Exp}(z))\,\sigma_2(\operatorname{Exp}(z))
=\operatorname{Exp}(\sigma_{-1}(z)+\sigma_2(z)).
\]
Injectivity of \(\operatorname{Exp}\) makes this equivalent to the *linear* equation
\[
(\sigma_{-1}+\sigma_2-I)z=0\qquad(z\in J).
\]

**Step 4: Diagonalize the kernel.** The \(p-1\) elements \(t^i-1\), for \(1\le i\le p-1\), form a \(k\)-basis of \(J\). Multiplication of their indices by \(a\in\mathbb F_p^\times\) permutes this basis regularly. Character orthogonality (or the Vandermonde determinant on the nonzero residues) proves that \(v_1,\ldots,v_{p-1}\) form a basis of \(J\) and satisfy
\[
\sigma_a(v_r)=a^r v_r.
\]
Consequently, the linear idempotence operator sends \(v_r\) to
\[
\left((-1)^r+2^r-1\right)v_r.
\]
For even \(r\), the scalar is \(2^r\ne0\). For odd \(r\), it vanishes exactly when \(2^{r-1}=1\) in \(\mathbb F_p\), i.e. \(h\mid r-1\). Since \(r\) is odd, both \(h\mid r-1\) and \(2\mid r-1\) hold exactly when \(\ell=\operatorname{lcm}(2,h)\) divides \(r-1\). There are exactly \(d=(p-1)/\ell\) such integers \(r\) in the range \(1\le r\le p-1\). Thus the kernel is exactly \(W\), establishing the complete parameterization and affine-space dimension.

**Step 5: Identify the induced quandle.** Every basis vector of \(W\) has an odd index \(r\) satisfying \(2^r=2\), so on \(W\) the operators act as \(\sigma_{-1}=-I\) and \(\sigma_2=2I\). Therefore, for \(z,w\in W\),
\[
\operatorname{Exp}(z)*\operatorname{Exp}(w)
=\operatorname{Exp}(\sigma_{-1}(z)+\sigma_2(w))
=\operatorname{Exp}(-z+2w).
\]
Since \(\operatorname{Exp}\) is bijective, the nonzero idempotents form the additive core quandle on \(W\cong k^d\). When \(k=\mathbb F_q\), the vector space has exactly \(q^d\) elements, and there is one further idempotent, zero. This proves the theorem.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. Its `action_rank` calculation constructs \(\sigma_{-1}+\sigma_2-I\) on the actual augmentation-ideal basis for eleven odd primes through \(41\) and verifies the predicted kernel dimensions by finite-field row reduction. It constructs the predicted idempotents by truncated exponential and directly checks the original quandle product. For \(p=17\), it constructs all \(289\) distinct nonzero idempotents, checks idempotence and augmentation, identifies \(272\) nonbasis elements, and tests the core-quandle law. Independently, it exhaustively enumerates all coefficient tuples for \(\mathbb F_3[R_3]\), \(\mathbb F_9[R_3]\), and \(\mathbb F_5[R_5]\), finding respectively \(4\), \(10\), and \(6\) total idempotents. Successful execution prints `VERIFY_OK_MODULAR_QUANDLE`. Finite checks support but do not replace the all-primes proof.

Run with `python3 verify.py` from the extracted package directory.

## Relationship to prior work

Elhamdadi, Nunez, Singh, and Swain (arXiv:2204.11288, 2022) study idempotents in quandle rings, including coefficient rings with noninvertible quandle order, and prove several structural results and bounded-support restrictions for odd dihedral quandles (notably Proposition 3.13). Their results do not provide a complete modular idempotent parameterization for every odd prime. Narayanan and Panja (arXiv:2206.10386, 2022) investigate **integral** dihedral quandle rings, including order five. Bardakov, Passi, and Singh (arXiv:2001.06843, 2020) analyze quandle-ring idempotents for certain small quandles. Their ordinary integral-coefficient settings and finite specific classifications do not imply the modular formula here.

A previously available special-case result gives an affine idempotent line for the dihedral quandle of order three over characteristic three, which agrees with the case \(p=3\), \(d=1\) of this theorem. The present claim does not take that special case as new. More recent treatments of Fourier analysis and idempotents in quandle algebras (arXiv:2609.03799) and of core quandles (arXiv:2608.09149) were considered: the former establishes integral-ring phenomena rather than the modular prime-order count, while the latter studies certain core quandles over general domains and solves integer-coefficient questions for \(R_5\). The modular count and its dimension jumps are not stated in the inspected relevant sections. This comparison is provisional, and a yet-unidentified stronger theorem could imply the result.

## Limitations

The proof requires an odd prime quandle order **equal to** the characteristic of the coefficient field. It does not give the complete idempotents for composite quandle orders, characteristic two, or coefficient fields with characteristic distinct from the quandle size. It counts elements, not orbit classes under all algebra automorphisms. The classification is a same-author mathematical proof with computational corroboration, not independent verification; priority is provisional.

## References

1. M. Elhamdadi, B. Nunez, M. Singh, D. Swain, *Idempotents, free products and quandle coverings*, arXiv:2204.11288 (first posted 2022-04-24), https://arxiv.org/abs/2204.11288 .
2. P. Narayanan, S. Panja, *Idempotents in integral ring of dihedral quandle*, arXiv:2206.10386 (first posted 2022-06-17), https://arxiv.org/abs/2206.10386 .
3. V. Bardakov, I. B. S. Passi, M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843 (first posted 2020-01-19), https://arxiv.org/abs/2001.06843 .
4. M. Elhamdadi, L. Ta, B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799 (2026), https://arxiv.org/abs/2609.03799 .
5. G. Churchill, I. R. Churchill, N. Fernando, B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149 (2026), https://arxiv.org/abs/2608.09149 .
