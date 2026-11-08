# Maximal subalgebra chains of finite Kronecker path algebras: exact counts and a uniform quotient-drop law

## Finding
Let \(q\ge2\) be a prime power, \(m\ge0\) an integer, and \(A_m\) the \(\mathbb F_q\)-path algebra of the quiver with two vertices and \(m\) parallel arrows from the first vertex to the second. **Subalgebra** here means any multiplication-closed \(\mathbb F_q\)-linear subspace, possibly without the ambient identity. A *saturated chain* is \(A_m=B_{m+2}\supsetneq B_{m+1}\supsetneq\cdots\supsetneq B_0=0\) with every inclusion maximal among subalgebras.

Put \([j]_q=(q^j-1)/(q-1)\), \(f_m=\prod_{j=1}^{m}[j]_q\), and
\[
 H_m(q)=\sum_{j=0}^{m}q^{m-j}\bigl(2[j+1]_q+j+1\bigr).
\]
Then every unrefinable chain from \(A_m\) to \(0\) is saturated, has exactly \(m+2\) inclusions, and the number of such chains is precisely
\[
 \boxed{C_m(q)=f_mH_m(q).}
\]
For \(m\ge1\), choose such a chain uniformly from the \(C_m(q)\) possibilities. Project each intermediate subalgebra into \(A_m/\operatorname{rad}(A_m)\cong\mathbb F_q^2\). The projection starts at dimension two and first drops to dimension one while the radical-intersection of the preceding subalgebra has dimension \(J_m\). Then
\[
 \boxed{\Pr(J_m=j)=\frac{q^{m-j}\bigl(2[j+1]_q+j+1\bigr)}{H_m(q)}\quad(0\le j\le m).}
\]
For every fixed prime power \(q\), this law is within \(O_q(1/m)\) total variation of the discrete uniform distribution on \(\{0,\ldots,m\}\). Consequently \(J_m/m\) converges in distribution to \(\operatorname{Uniform}[0,1]\), and
\[
 C_m(q)=f_mq^m\left(\frac{2q}{q-1}(m+1)+O_q(1)\right).
\]
The uniform law concerns *a uniformly chosen complete chain*, not a process that chooses each available maximal subalgebra with equal probability at every step.

## Assumptions and scope
The multiplication is specified by a vector-space decomposition \(A_m=\mathbb F_q e\oplus\mathbb F_q f\oplus V\), \(\dim V=m\), where \(e^2=e\), \(f^2=f\), \(ef=fe=0\), \(ev=v=vf\) and \(ve=fv=V^2=0\) for \(v\in V\). Thus \(1=e+f\) and \(\operatorname{rad}(A_m)=V\). The zero-dimensional radical case \(m=0\) is included in the counting formula, where \(C_0(q)=3\). Every formula holds for arbitrary finite fields, including characteristic two.

## Proof
**1. Four algebra types and the codimension-one covers.** Write \(\pi:A_m\to\mathbb F_q e\oplus\mathbb F_q f\) for the quotient projection. A subalgebra \(B\) has \(W=B\cap V\), and \(\pi(B)\) must be one of \(0\), \(\mathbb F_q e\), \(\mathbb F_q f\), \(\mathbb F_q(e+f)\), or \(\mathbb F_q^2\). These are all subalgebras of the diagonal algebra, since any nonzero one-dimensional multiplicatively closed line is spanned by an idempotent.

If \(\pi(B)=0\), then \(B=W\), with zero product. If \(\pi(B)=\mathbb F_q e\), then \(B=\mathbb F_q(e+a)\oplus W\) for some \(a\in V/W\), and \((e+a)^2=e+a\), \((e+a)w=w\), \(w(e+a)=0\). Its opposite case arises from \(\pi(B)=\mathbb F_q f\). If \(\pi(B)=\mathbb F_q1\), any lift \(1+a\) satisfies \((1+a)^2-(1+a)=a\), so closure forces \(a\in W\), and \(B=\mathbb F_q1\oplus W\). Finally, when \(\pi(B)=\mathbb F_q^2\), choose lifts \(e+a\), \(f+b\). Their product is \(a+b\in W\), forcing \(b=-a\pmod W\), and \(B=\mathbb F_q(e+a)\oplus\mathbb F_q(f-a)\oplus W\). The last algebra is isomorphic to the same Kronecker algebra with \(\dim W\) arrows. These exhaust the possibilities, including all nonunital subalgebras.

For each \(d\ge0\), denote the four isomorphism types by \(Z_d\) (zero product, dimension \(d\)), \(T_d\) (\(\mathbb F_q1\oplus W\)), \(L_d\) (\(\mathbb F_q t\oplus W\), \(t^2=t\), \(tw=w\), \(wt=0\)), and \(K_d\) (the Kronecker type). The opposite of \(L_d\) has the same chain count. The maximal proper subalgebras of each type are exactly the following codimension-one subalgebras, with **distinct embedded copies** counted:

* \(Z_d\): \([d]_q\) copies of \(Z_{d-1}\).
* \(T_d\): one \(Z_d\), and \([d]_q\) copies of \(T_{d-1}\).
* \(L_d\): one \(Z_d\), and \(q[d]_q\) copies of \(L_{d-1}\).
* \(K_d\): one \(T_d\), one \(L_d\), one opposite \(L_d\), and \(q[d]_q\) copies of \(K_{d-1}\).

These counts follow by choosing a codimension-one subspace of \(W\), then choosing the lift of its quotient idempotent modulo the chosen subspace; such a lift has \(q\) choices for the \(L\) and \(K\) branches. Every other proper subalgebra is contained in one of the displayed codimension-one subalgebras, by enlarging its radical intersection or its projected diagonal subalgebra. Therefore all maximal inclusions drop dimension one.

**2. Recurrences and exact census.** Let \(z_d,t_d,\ell_d,c_d\) count complete saturated chains from the four types to zero. With \(z_0=t_0=\ell_0=1\), and \(c_0=3\), the cover list gives
\[
 z_d=[d]_qz_{d-1},\quad
 t_d=z_d+[d]_qt_{d-1},\quad
 \ell_d=z_d+q[d]_q\ell_{d-1},\quad
 c_d=2\ell_d+t_d+q[d]_qc_{d-1}.
\]
Thus \(z_d=f_d\), \(t_d=(d+1)f_d\), and \(\ell_d=[d+1]_qf_d\). Dividing the final recurrence by \(f_d\) yields
\[
 \frac{c_d}{f_d}=q\frac{c_{d-1}}{f_{d-1}}+2[d+1]_q+d+1,
\]
whose solution is \(c_m=f_mH_m(q)\), as claimed.

**3. First quotient-dimension drop.** Before the first projection-dimension reduction, each chain passes through some sequence of full-quotient Kronecker types \(K_m,K_{m-1},\ldots,K_j\). The number of choices for this initial segment is \(\prod_{k=j+1}^{m}q[k]_q=q^{m-j}f_m/f_j\). At \(K_j\), the first quotient drop has three alternatives: two one-sided types each with \(\ell_j\) continuation chains, and the central type with \(t_j\) continuation chains. Hence its exact contribution is
\[
 \left(q^{m-j}f_m/f_j\right)(2\ell_j+t_j)
 =f_mq^{m-j}(2[j+1]_q+j+1).
\]
Summing over \(j\) gives \(C_m(q)\), proving the probability formula.

**4. Uniform limit and quantitative error.** Set \(a_q=2q/(q-1)\). A direct identity is
\[
 q^{-m}H_m(q)=\sum_{j=0}^{m}\left[a_q+q^{-j}\left(j+1-\frac2{q-1}\right)\right]
 =a_q(m+1)+O_q(1).
\]
The total absolute deviation of the bracketed summands from \(a_q\) is bounded by \(\sum_{j\ge0}q^{-j}(j+1+2/(q-1))<\infty\). Normalizing gives total-variation distance \(O_q(1/(m+1))\) from discrete uniformity, and the continuous limit follows by Riemann sums. The same identity yields the stated total-chain asymptotic.

## Verification
The standalone `verify.py` generates every reduced-row-echelon subspace in \(\mathbb F_q^{m+2}\) for small prime fields, directly checks multiplication closure, enumerates dimension-one inclusion steps, and computes saturated-chain totals without using the structural recurrence. It then compares those totals against the theorem. Executed checks were \((q,m)=(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(5,1)\); the results included \(C_3(2)=2604\), \(C_2(3)=344\), and \(C_1(5)=29\). All checks ended with `VERIFY_OK`. These experiments confirm finitely many cases; the general theorem follows from the proof above.

## Relationship to prior work
Iovanov and Sistko (2017) classify maximal subalgebras of general finite-dimensional associative algebras, including quiver examples. Sistko (2018) studies maximal-subalgebra varieties and automorphism orbits of Kronecker path algebras. Sercombe and Shalev (2020) show that split basic finite-dimensional algebras have equal chain length and depth, so the fact that all chains here have full dimension is already covered. The contribution established here is the exact number of **embedded, complete, non-necessarily-unital** chains and the first semisimple-quotient-drop distribution with its quantitative uniform limit. General maximal-subalgebra classification informs the cover analysis but does not state these enumerative and probabilistic conclusions.

## Limitations
The statement concerns the two-vertex parallel-arrow path algebra and counts all linear multiplicatively closed subalgebras, not just subalgebras containing the ambient identity. The asymptotic is for fixed field order. Finite brute-force checks do not replace the abstract proof and do not by themselves verify arbitrary prime-power fields. Publication priority is provisional, especially relative to potential uninspected chain-enumeration or poset-zeta literature.

## References
1. M. C. Iovanov and A. Sistko, *Maximal Subalgebras of Finite-Dimensional Algebras*, arXiv:1705.00762, first publicly available 2017-05-02, https://arxiv.org/abs/1705.00762.
2. A. H. Sistko, *Automorphism Groups of Finite-Dimensional Algebras Acting on Subalgebra Varieties*, arXiv:1809.09760, first publicly available 2018-09-25, https://arxiv.org/abs/1809.09760.
3. D. Sercombe and A. Shalev, *The Length and Depth of Associative Algebras*, arXiv:2004.06920, first publicly available 2020-04-15, https://arxiv.org/abs/2004.06920.
