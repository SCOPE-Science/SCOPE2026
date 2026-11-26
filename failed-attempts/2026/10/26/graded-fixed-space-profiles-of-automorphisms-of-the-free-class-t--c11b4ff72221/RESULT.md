# Graded fixed-space profiles of automorphisms of the free class-two Lie algebra on three generators

## Finding

Let \(q\) be any prime power, let \(V=\mathbb F_q^3\), and let \(L(V)=V\oplus\bigwedge^2V\) be the six-dimensional Lie algebra with bracket \([v+z,w+z']=v\wedge w\). For every automorphism \(\varphi\), write \(a(\varphi)\) for the fixed-space dimension of the induced map on \(L(V)/[L(V),L(V)]\), and \(b(\varphi)\) for that of its restriction to \([L(V),L(V)]\). The formulas below determine the number of automorphisms with **each** pair \((a,b)\), not merely the fixed-point-free proportion.

Define Gaussian coefficients \({n\brack k}_q\), with value zero unless \(0\le k\le n\). Set \(S_r(q)=|\operatorname{GL}_r(\mathbb F_q)|/(q-1)\) for \(r\ge1\), and \(S_0(q)=1\). Every automorphism is uniquely \(\varphi_{A,T}(v,z)=(Av,Tv+(\bigwedge^2 A)z)\), with \(A\in\operatorname{GL}_3(\mathbb F_q)\) and \(T\in\operatorname{Hom}(V,\bigwedge^2V)\). Put \(d=\det A\). Then

\[
a(\varphi)=\dim\ker(A-I),\qquad b(\varphi)=\dim\ker(A-dI).
\]

Here is an explicit finite-sum law. For determinant \(d=1\), define, for \(0\le k\le3\),

\[
F^{(1)}_k={3\brack k}_q q^{k(3-k)}\begin{cases}S_{3-k}(q),&k<3,\\1,&k=3,\end{cases}
\qquad
N^{(1)}_a=\sum_{k=a}^3(-1)^{k-a}q^{\binom{k-a}{2}}{k\brack a}_q F^{(1)}_k.
\]

For each \(d\in\mathbb F_q^\times\setminus\{1\}\), and integers \(k,l\ge0\) with \(k+l\le3\), put \(r=3-k-l\) and define

\[
F^{(d)}_{k,l}={3\brack k}_q{3-k\brack l}_q
q^{kl+(k+l)r}
\begin{cases}
S_r(q),&r\ge1,\\
\mathbf1_{\{d^l=d\}},&r=0.
\end{cases}
\]

Put \(F^{(d)}_{k,l}=0\) for \(k+l>3\). For \(0\le a,b\le3\), set

\[
N^{(d)}_{a,b}=\sum_{k=a}^3\sum_{l=b}^3
(-1)^{k-a+l-b}q^{\binom{k-a}{2}+\binom{l-b}{2}}
{k\brack a}_q{l\brack b}_q F^{(d)}_{k,l}.
\]

**The complete joint profile** is

\[
\boxed{\#\{\varphi:a(\varphi)=a,\ b(\varphi)=b\}
=q^9\left(\mathbf1_{\{a=b\}}N^{(1)}_a
+\sum_{d\in\mathbb F_q^\times\setminus\{1\}}N^{(d)}_{a,b}\right).}
\]

All parameters range over the integers \(0\le a,b\le3\), and the sum is interpreted as zero when its index set is empty. In particular, since \(\varphi-I\) is block triangular, \(\varphi\) has no nonzero fixed vector if and only if \(a=b=0\). Let \(\epsilon_q=1\) in odd characteristic and \(\epsilon_q=0\) in characteristic two. The fixed-point-free number is therefore

\[
\boxed{q^{12}\left(q^6-3q^5+q^4+4q^3+q^2-3q-8-\epsilon_q\right),}
\]

and the **proportion** in the full automorphism group equals

\[
\boxed{\frac{q^6-3q^5+q^4+4q^3+q^2-3q-8-\epsilon_q}
{(q-1)^3(q+1)(q^2+q+1)}.}
\]

Thus there are \(24576\) fixed-point-free automorphisms over \(\mathbb F_2\), whereas the free class-two Lie algebra on **two** generators (the three-dimensional Heisenberg Lie algebra) has none over that field. In rank three the coefficient-field parity contributes a genuine additive correction to the exact count, coming from determinant \(-1\).

## Assumptions and scope

The bracket is alternating over every characteristic; in characteristic two, \(\bigwedge^2V\) is still the universal alternating square, and \([v,v]=0\). The algebra is the free Lie algebra of nilpotency class at most two on three generators. The derived subspace is precisely \(\bigwedge^2V\) and is central. All counts include all automorphisms, not merely graded automorphisms: \(T\) is arbitrary. Uniform probabilities refer to the uniform measure on the finite group \(\operatorname{Aut}(L(V))\). The pair \((a,b)\) is a **graded** fixed-space profile; it is not asserted that the fixed space of the whole automorphism has dimension \(a+b\) when either entry is positive.

## Proof

**Automorphisms.** The central derived subspace is characteristic. Any automorphism induces \(A\in\operatorname{GL}(V)\) on the abelianization, and the bracket forces its action on the derived subspace to be \(\bigwedge^2 A\). Conversely, any such \(A\) and any linear \(T:V\to\bigwedge^2V\) give an invertible bracket-preserving map. Uniqueness follows from the direct sum decomposition. There are \(q^9\) choices of \(T\) for each \(A\).

**Exterior-square identification.** In dimension three, the natural isomorphism \(\bigwedge^2V\cong\det(V)\otimes V^*\) conjugates \(\bigwedge^2A\) to \(d(A^{-1})^{\mathsf T}\), where \(d=\det A\). Consequently, \(\dim\ker(\bigwedge^2 A-I)=\dim\ker(A-dI)\), including nonsemisimple matrices and all field characteristics.

**One eigenvalue.** Fix \(\det A=1\). For any prescribed \(k\)-dimensional subspace \(U\le V\), the condition \(A|_U=I\) gives, relative to a complement, an upper-block-triangular matrix \(\left(\begin{smallmatrix}I_k&C\\0&B\end{smallmatrix}\right)\). If \(r=3-k>0\), the number of invertible lower blocks with determinant one is \(S_r(q)\) and the upper block has \(q^{kr}\) possibilities. If \(r=0\), there is exactly one matrix. Summing over the \({3\brack k}_q\) subspaces yields \(F^{(1)}_k\). For a matrix with \(a\)-dimensional fixed subspace, it contributes \({a\brack k}_q\) incidences. Gaussian-binomial Möbius inversion gives \(N^{(1)}_a\). The two graded fixed-space dimensions agree when \(d=1\).

**Two distinct eigenvalues.** Now fix \(d\ne1\). A \(1\)-eigenspace and a \(d\)-eigenspace meet trivially. The number of ordered pairs of subspaces \(U,W\le V\), with \(\dim U=k\), \(\dim W=l\), and \(U\cap W=0\), is exactly \({3\brack k}_q{3-k\brack l}_q q^{kl}\): choose \(U\), a projected \(l\)-subspace of \(V/U\), and one of its \(q^{kl}\) graph lifts. Requiring \(A|_U=I\) and \(A|_W=dI\), the remaining \(r\times r\) block must have determinant \(d^{1-l}\), while the arbitrary off-diagonal block has \(q^{(k+l)r}\) possibilities. For \(r>0\), the determinant fiber has \(S_r(q)\) matrices. For \(r=0\), it exists exactly when \(d^l=d\). This is \(F^{(d)}_{k,l}\). Each matrix with two eigenspace dimensions \((a,b)\) is counted \({a\brack k}_q{b\brack l}_q\) times. The product of two Gaussian-binomial inversions gives \(N^{(d)}_{a,b}\). Specifically, the inversion identity used is

\[
\sum_{j=0}^m(-1)^j q^{\binom j2}{m\brack j}_q=\mathbf1_{\{m=0\}}.
\]

**Closed fixed-point-free polynomial.** The determinant-one contribution at \((0,0)\), after expanding the four terms \(k=0,1,2,3\), is

\[
N^{(1)}_0=q^3(q+1)(q^4-2q^3+2).
\]

For a generic \(d\ne1\), collecting the \(k+l\le3\) terms gives

\[
N^{(d)}_{0,0}=q^3(q^2+q+1)(q^3-3q^2+5)-q^3\mathbf1_{\{d=-1\ne1\}}.
\]

Indeed, in the full-dimension case \(k+l=3\), the determinant condition allows \(l=1\) universally and additionally \(l=3\) precisely when \(d=-1\ne1\); that latter term has sign \(-\) and magnitude \(q^3\). There is one such nonunit determinant value if \(q\) is odd, and none if it is even. Adding \(d=1\) and the other \(q-2\) determinant fibers yields the displayed polynomial for \(q^{-9}\) times the fixed-point-free automorphism count. Finally, \(|\operatorname{GL}_3(\mathbb F_q)|=q^3(q-1)^3(q+1)(q^2+q+1)\), giving the proportion after cancellation.

## Verification

The standalone file `verify.py` uses only Python's standard library. Running `python verify.py` enumerates every invertible three-by-three matrix for \(q=2,3,4\), constructs its exterior-square matrix independently from two-by-two minors, and computes the two kernel dimensions by finite-field Gaussian elimination. It compares **every** coefficient of the bivariate distribution to the independent subspace-incidence formula. Counts of base matrices with \((a,b)=(0,0)\) are \(48\), \(4860\), and \(98048\), respectively. It also tests determinant strata and checks the polynomial identity against the incidence formula for several further prime field orders without enumerating all matrices. The \(q=4\) test uses \(\mathbb F_2[t]/(t^2+t+1)\), so the extension-field case is exercised. The program ends with `VERIFY_OK` when all checks pass.

## Relationship to prior work

Benito and Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients* (arXiv:1911.01897, first posted November 5, 2019), describe the automorphism structure in characteristic zero. Its Proposition 1 and Remark 2 give the structural starting point but not the finite-field graded eigenspace distribution or fixed-point-free count. Burde and Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras* (arXiv:2604.27916, 2026), address existence and structural restrictions in characteristic zero, not the present enumeration. A related published result determines fixed-point-free counts for the three-dimensional Heisenberg Lie algebra; that algebra is free class-two on **two** generators, while the present six-dimensional algebra has a three-dimensional derived ideal, with genuinely different exterior-square constraints. The novelty asserted here is the bivariate finite-field law and the closed rank-three count, not the general semidirect automorphism decomposition or the identity for the exterior square.

## Limitations

No all-ranks formula for free nilpotent Lie algebras is claimed. The count treats automorphisms on the two characteristic graded pieces; when fixed spaces occur on both pieces, the actual fixed-space dimension on the nonsplit upper-triangular automorphism matrix may depend on \(T\). The finite checks are not proofs for arbitrary prime powers; the subspace-counting argument is. The closest published Heisenberg result could only be compared by its accessible research summary, and a differently presented matrix-representation census might imply parts of this exact law. Exhaustive priority over all possible sources is not asserted.

## References

1. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897v1 (November 5, 2019), full HTML of v2: https://arxiv.org/html/1911.01897v2.
2. D. Burde and K. Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916 (April 30, 2026), https://arxiv.org/abs/2604.27916.
3. *Exact fixed-point-free automorphism count for the three-dimensional Heisenberg Lie algebra*, published-finding corpus research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-fixed-point-free-automorphism-count-for-the-three-dimensio--17f0de4cb789.
