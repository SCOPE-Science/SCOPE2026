# Joint element-order and conjugacy census for null-filiform Leibniz automorphisms

## Finding
Let \(k=\mathbb F_q\) have characteristic \(p\), let \(n\ge2\), and let \(L_n\) be the left Leibniz algebra described below. For any divisor \(d\mid q-1\) and \(t\ge0\), let \(N_{d,t}\) denote the number of automorphisms of **exact** order \(dp^t\), and let \(K_{d,t}\) denote the number of their conjugacy classes. Set
\[
 m_{d,e}=\left\lfloor\frac{n-1}{\operatorname{lcm}(d,e)}\right\rfloor,\qquad
 h_{d,t}=\left\lfloor\frac{n-1}{dp^t}\right\rfloor.
\]
Then the complete order spectrum is
\[
 N_{d,0}=\varphi(d)q^{n-1-h_{d,0}},\qquad
 N_{d,t}=\varphi(d)\left(q^{n-1-h_{d,t}}-q^{n-1-h_{d,t-1}}\right)\quad(t\ge1).
\]
The complete conjugacy-class spectrum, resolved by the exact element order, is
\[
 K_{d,0}=\varphi(d),
\]
\[
 K_{d,t}=\frac{\varphi(d)}{q-1}\sum_{e\mid q-1}\varphi(e)
 \left(q^{m_{d,e}-\lfloor(n-1)/(p^t\operatorname{lcm}(d,e))\rfloor}
 -q^{m_{d,e}-\lfloor(n-1)/(p^{t-1}\operatorname{lcm}(d,e))\rfloor}\right)\quad(t\ge1).
\]
All other element orders and conjugacy classes are absent. In particular the total class number is
\[
 k(\operatorname{Aut}_k L_n)=\frac{1}{q-1}\sum_{d,e\mid q-1}\varphi(d)\varphi(e)q^{m_{d,e}}.
\]
Every class admits an explicit representative and centralizer size, described in the proof. The group exponent is \((q-1)p^E\), where \(E\) is the smallest nonnegative integer with \(p^E\ge n\); an automorphism attaining that order exists **if and only if** \((q-1)p^{E-1}<n\). Thus the group exponent can fail to be an element order.

## Assumptions and scope
Take the \(n\)-dimensional left Leibniz algebra with basis \(e_1,\ldots,e_n\) and the only nonzero products \([e_1,e_j]=e_{j+1}\) for \(1\le j<n\). The bracket has the left Leibniz identity \([x,[y,z]]=[[x,y],z]+[y,[x,z]]\). Automorphisms are \(k\)-linear and bracket preserving; element order and conjugacy refer to the abstract finite group \(\operatorname{Aut}_k L_n\). The arithmetic functions \(\varphi\), \(\operatorname{lcm}\) and floor have their usual meanings. For \(t=0\), no \(t-1\) term is used. The statements hold in every characteristic, including characteristic two, for all prime powers \(q\) and all \(n\ge2\).

## Proof
**1. Group law, reconstructed.** Any automorphism is determined by
\[
 f_A(e_1)=\sum_{i=1}^{n}a_i e_i,\quad a_1\ne0,
\]
and induction on the defining bracket gives
\[
 f_A(e_j)=a_1^{j-1}\sum_{i=1}^{n-j+1}a_i e_{i+j-1}.
\]
Conversely these maps preserve the bracket and have an invertible triangular matrix. Encode \(A(x)=\sum_{i=1}^n a_i x^{i-1}\in k[x]/(x^n)\). Then \(f_A\circ f_B=f_{A(x)B(a_1x)}\). Writing \(A=a u\) with \(a=a_1\in k^\times\) and \(u\in U=1+xk[x]/(x^n)\) yields
\[
 \operatorname{Aut}_k(L_n)\cong U\rtimes k^\times,
 \quad (u,a)(v,b)=(u(x)v(ax),ab).
\]
Here \(U\) is an abelian \(p\)-group of order \(q^{n-1}\), with scalar action \(\rho_a(u)(x)=u(ax)\). This group description is established in the cited 2021 literature; its short reconstruction is included to fix conventions.

**2. Norm decomposition and orders.** Fix \(a\in k^\times\) of order \(d\mid q-1\). Its fixed subgroup is
\[
 U^{\rho_a}=1+\sum_{1\le j\le \lfloor(n-1)/d\rfloor}c_j x^{dj},
 \qquad |U^{\rho_a}|=q^{\lfloor(n-1)/d\rfloor}.
\]
Multiplication is understood modulo \(x^n\), so the displayed expression parametrizes a subgroup but does not identify its group law with coefficientwise addition. Define the multiplicative norm \(\mathcal N_a(u)=\prod_{i=0}^{d-1}\rho_a^i(u)\). Since \(d\) is coprime to \(p\), taking the unique \(d\)-th root in the finite abelian \(p\)-group \(U\) yields a projection \(\pi_a(u)=\mathcal N_a(u)^{1/d}\) onto \(U^{\rho_a}\), whose restriction to the fixed subgroup is the identity. Its kernel equals \(\{w/\rho_a(w):w\in U\}\): inclusion is immediate from the norm, and equality follows from the coprime-action decomposition, equivalently by counting the fibers of the homomorphism \(w\mapsto w/\rho_a(w)\). Therefore \(U\) splits as the product of this kernel and \(U^{\rho_a}\).

Conjugation by \((w,1)\) changes the \(U\)-coordinate of \((u,a)\) by a factor in \(\ker\pi_a\). Thus \((u,a)\) is conjugate to \((\pi_a(u),a)\), and every fixed element has exactly \(q^{n-1-\lfloor(n-1)/d\rfloor}\) preimages under \(\pi_a\). For \(v\in U^{\rho_a}\), \((v,a)^d=(v^d,1)\), so its order equals \(d\) times the order of \(v\), which is a power of \(p\). In characteristic \(p\),
\[
 v^{p^t}=1\pmod{x^n}\quad\Longleftrightarrow\quad
 c_j=0\ \text{whenever }djp^t<n.
\]
Consequently \(\#\{v\in U^{\rho_a}:v^{p^t}=1\}=q^{\lfloor(n-1)/d\rfloor-\lfloor(n-1)/(dp^t)\rfloor}\). Multiplying by fiber size and by the \(\varphi(d)\) choices of \(a\) gives \(\varphi(d)q^{n-1-h_{d,t}}\) elements whose scalar component has exact order \(d\) and whose \(p\)-part has order dividing \(p^t\). Differences between consecutive \(t\) prove the formula for \(N_{d,t}\).

**3. Conjugacy and centralizers.** The scalar component \(a\) is unchanged by conjugation. Once an element is reduced to \((v,a)\) with \(v\in U^{\rho_a}\), conjugation by \((w,b)\) acts on the fixed coordinate as \(v\mapsto \rho_b(v)\). Hence conjugacy classes with scalar \(a\) are precisely the \(k^\times\)-orbits on \(U^{\rho_a}\). The representative \((v,a)\) has centralizer size
\[
 |C_G(v,a)|=q^{\lfloor(n-1)/d\rfloor}\bigl|\{b\in k^\times:\rho_b(v)=v\}\bigr|.
\]
If \(b\) has order \(e\), an element fixed by both scalars is an element of \(U^{\rho_a}\cap U^{\rho_b}\), represented by multiples of \(\operatorname{lcm}(d,e)\). For such fixed units, the \(p^t\)-torsion count is
\[
 q^{m_{d,e}-\lfloor(n-1)/(p^t\operatorname{lcm}(d,e))\rfloor}.
\]
Apply Burnside's lemma to the subset of fixed units of exact order \(p^t\), and then multiply by the \(\varphi(d)\) possible scalars \(a\). The resulting difference of two fixed-point sums is precisely \(K_{d,t}\). For \(t=0\), the subset is the singleton \(v=1\), so \(K_{d,0}=\varphi(d)\). Summing the unrestricted Burnside counts yields the total class-number formula.

**4. Element-order versus exponent gap.** All automorphism orders divide \((q-1)p^E\) since \(U\) has exponent \(p^E\); elements of \(U\) attain \(p^E\), and the scalar quotient has exponent \(q-1\), proving the group-exponent formula. The formula for \(N_{q-1,E}\) is positive exactly when \(\lfloor(n-1)/((q-1)p^{E-1})\rfloor\ge1\), equivalent to the stated strict inequality. For example \(q=5,n=3\) yields group exponent \(20\) but no element of order \(20\); the exact element-order counts are \(1,5,50,24,20\) for orders \(1,2,4,5,10\) respectively.

## Verification
A standalone standard-library Python script, \(\texttt{verification/verify.py}\), enumerates all automorphisms by their triangular coefficient vectors and computes exact orders using direct multiplication. Over prime fields, it tests \(p\in\{2,3,5,7\}\) and the listed small dimensions; over \(\mathbb F_4\) and \(\mathbb F_9\) it independently implements extension-field arithmetic and tests the full order spectrum. It also counts conjugacy classes directly from centralizer counts for nine prime-field configurations and checks the predicted class-order multiplicities. Selected matrix-composition identities are checked exhaustively, so both the parametrization and multiplication used in the enumeration are corroborated. These are finite tests only; the proof above establishes the all-field and all-dimension theorem.

## Relationship to prior work
Kurdachenko, Pypka and Subbotin give the semidirect automorphism-group structure for finite-dimensional cyclic Leibniz algebras, which is the starting point rather than a newly claimed ingredient. The subsequent group-theoretic norm splitting, exact order-distribution and conjugacy-class arithmetic above are additional explicit evaluations of this structure. Calderón, Camacho, Kaygorodov and Omirov et al. study abelian gradings and tori of null-filiform Leibniz algebras, not the finite-field joint conjugacy and element-order census. Related finite-field results on algebra-element orbits and on derivation ranks concern other actions or operators. No claim of exhaustive literature priority or independent mathematical certification is made.

## Limitations
The theorem concerns the specified left null-filiform Leibniz algebra, not arbitrary filiform, right-convention, or solvable Leibniz algebras. It does not classify representations or modular character degrees of the automorphism group. The finite computational checks do not replace the proof and do not establish novelty. Existing general automorphism-group descriptions may provide an indirect route to the formulas; the novelty assessment is qualified by the inspected sources and by possible broader group-theoretic enumeration results.

## References
1. L. A. Kurdachenko, A. A. Pypka and I. Ya. Subbotin, *On the automorphism groups of some Leibniz algebras*, arXiv:2108.06794v1 (first public 2021-08-15), https://arxiv.org/abs/2108.06794. Relevant automorphism-group structure: Section 2, Theorem 2.11.
2. L. A. Kurdachenko, A. A. Pypka and I. Ya. Subbotin, *The description of the automorphism groups of finite-dimensional cyclic Leibniz algebras*, 2022, https://doi.org/10.15407/dopovidi2022.02.012.
3. A. J. Calderón, L. M. Camacho, I. Kaygorodov et al., *Abelian groups gradings on null-filiform and one-parametric filiform Leibniz algebras*, Journal of Geometry and Physics 170 (2021), 104384, https://doi.org/10.1016/j.geomphys.2021.104384.
