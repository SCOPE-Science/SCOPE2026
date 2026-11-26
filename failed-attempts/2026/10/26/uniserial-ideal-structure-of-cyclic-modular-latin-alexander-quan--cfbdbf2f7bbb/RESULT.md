# Uniserial ideal structure of cyclic modular Latin Alexander quandle algebras

## Finding
Let \(p\) be an odd prime, \(s\geq 1\), \(m=p^s\), and let \(K\) be **any field of characteristic \(p\)**. Choose an integer \(t\) such that \(p\nmid t(1-t)\), and let \(Q_{m,t}\) denote the Alexander quandle on \(C_m=\mathbb Z/m\mathbb Z\) with operation \(a*b=ta+(1-t)b\). Its \(K\)-quandle algebra \(E=K[Q_{m,t}]\) has precisely \(m+1\) **left ideals, precisely \(m+1\) right ideals, and precisely \(m+1\) two-sided ideals**, and these three families coincide. They form one chain
\[
E=J^0\supsetneq J^1\supsetneq\cdots\supsetneq J^m=0,
\]
where the algebra is identified linearly with \(R=K[g]/(g^m-1)\), \(J=(g-1)R\) is the coefficient-sum augmentation ideal, and \(J^a\) denotes the **ordinary associative group-ring power**. For every \(0\leq a,b\leq m\), their product as subspaces of the quandle algebra is exactly
\[
\operatorname{span}_K\{u*v:u\in J^a,\ v\in J^b\}=J^{\min(m,a+b)}.
\]
Moreover \(\dim_K J^a=m-a\); hence every successive nonzero ideal quotient has dimension one, and the augmentation ideal has nilpotency index \(m\), regardless of parenthesization. In particular the algebra is left- and right-uniserial as a finite-dimensional nonassociative algebra, with a unique maximal proper ideal.

## Assumptions and scope
Here *left ideal* means a \(K\)-linear subspace \(I\) with \(E*I\subseteq I\); *right ideal* means \(I*E\subseteq I\), and two-sided means both. Associativity of \(E\) is **not** assumed. The hypotheses \(p\nmid t\) and \(p\nmid(1-t)\) make the two multipliers automorphisms of \(C_m\), so the quandle is Latin. There is no restriction on whether \(K\) is finite, perfect, or algebraically closed. The assertion does not apply to non-Latin parameters, underlying groups with a coprime-to-\(p\) factor, or general noncyclic \(p\)-groups.

## Proof
Write the basis element indexed by \(a\in C_m\) as \(g^a\). Regard \(R=K[C_m]\) first with its **ordinary associative** product, and let \(\alpha,\beta\) be the ordinary ring automorphisms induced by \(g\mapsto g^t\) and \(g\mapsto g^{1-t}\). Both are automorphisms since their exponents are units modulo \(m\). The Alexander multiplication transported to \(R\) is
\[
u*v=\alpha(u)\,\beta(v),
\]
where juxtaposition denotes the ordinary group-ring multiplication [Zhang, Proposition 2.1]. In particular, writing \(1=g^0\) for the ordinary group-ring identity, we have \(u*1=\alpha(u)\) and \(1*u=\beta(u)\). The symbol \(1\) need not be an identity for the nonassociative product.

Let \(I\) be a right ideal of \(E\). Then \(\alpha(I)=I*1\subseteq I\). Since \(I\) is finite-dimensional and \(\alpha\) is an invertible linear map, \(\alpha(I)=I\). For every \(u\in I\) and \(r\in R\), take \(v\in I\) with \(\alpha(v)=u\) and \(w\in R\) with \(\beta(w)=r\). Right ideal closure gives \(ur=v*w\in I\). Thus \(I\) is an ordinary ideal of \(R\). Similarly, if \(I\) is a left ideal, then \(\beta(I)=1*I\subseteq I\), whence \(\beta(I)=I\); surjectivity of \(\alpha\) shows that \(RI\subseteq I\), and \(I\) is again an ordinary ideal of \(R\).

Since \(m=p^s\) and \(\operatorname{char}K=p\), the binomial identity gives \(g^m-1=(g-1)^m\). Therefore \(R\cong K[z]/(z^m)\), via \(z=g-1\). Every associative ideal of this principal local Artin ring is uniquely \((z^a)=J^a\), for \(0\leq a\leq m\), with dimension \(m-a\). Both \(\alpha\) and \(\beta\) preserve the coefficient-sum augmentation map, hence preserve \(J\) and every \(J^a\). Consequently, for every \(a\),
\[
J^a*R=\alpha(J^a)\beta(R)=J^aR=J^a,
\qquad R*J^a=\alpha(R)\beta(J^a)=RJ^a=J^a.
\]
Thus every ordinary ideal is simultaneously a left and right ideal of \(E\), completing the classification. Likewise,
\[
J^a*J^b=\alpha(J^a)\beta(J^b)=J^aJ^b=J^{\min(m,a+b)},
\]
where the left side denotes the \(K\)-span of products. Induction on the binary parenthesization tree proves that **every** bracketed product of \(k\) factors from \(J\) spans \(J^k\): its two subproducts span \(J^i\) and \(J^j\) with \(i+j=k\). Since \(J^{m-1}\neq0\) but \(J^m=0\), the nilpotency index is exactly \(m\). This also proves the one-dimensional quotient assertion and uniqueness of the maximal ideal.

## Verification
The standalone `verify.py` performs exact coefficient arithmetic in the cyclic group ring of orders \(3\), \(5\), and \(9\), all with \(t=2\) and coefficient prime fields of characteristics \(3,5,3\) respectively. It verifies that each predicted chain member is simultaneously left and right invariant and that all \((m+1)^2\) ideal-product spans have the predicted dimension. For \(m=3\), it independently enumerates all \(28\) linear subspaces of \(\mathbb F_3^3\) and confirms that the only left or right ideals are the four chain members. The output is three `CHECK_OK` lines. These are checks, not the proof for arbitrary \(p,s,K,t\), which is the argument above.

Reproduce using Python 3 with `python verify.py`; the script uses only the standard library.

## Relationship to prior work
The transported multiplication identity is **not new**: it is Zhang's Proposition 2.1, and Zhang's Theorem 2.2 also determines augmentation powers in a broader coefficient setting. The present classification is about **all one-sided and two-sided ideals** under the modular Latin prime-power hypotheses; augmentation powers alone do not assert that these exhaust all ideals. The 2019 article of Elhamdadi, Fernando and Tsvelikhovskiy decomposes quandle algebra right ideals using permutation representations, giving explicit dihedral results over \(\mathbb R\) and \(\mathbb C\); those semisimple-field decompositions do not cover the defining-characteristic cyclic \(p\)-power case. Bardakov and Elhamdadi (2026) calculate augmentation powers mainly over integral coefficients. In contrast, the semisimple Fourier description of Latin Alexander quandle algebras over splitting coefficient fields of characteristic prime to the group order can yield Boolean ideal lattices; that hypothesis excludes the defining-characteristic case here. The comparison leaves a risk of an unindexed modular specialization or a representation-theoretic corollary already known elsewhere.

## Limitations
The proof is elementary once the transported product is known; it does not claim novelty for that multiplication identity, for principal ideals of truncated polynomial rings, or for general properties of modular cyclic permutation modules. The result is limited to the precise cyclic \(p\)-power Latin setting and linear ideals. It does not classify arbitrary subalgebras or the isomorphism types of these algebras. Scientific originality is based on the primary statements and searches described in the accompanying review; it is not independently certified.

## References
- Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (first posted 2026-10-06), especially Proposition 2.1 and Theorem 2.2. https://arxiv.org/abs/2610.08204
- M. Elhamdadi, N. Fernando and B. Tsvelikhovskiy, *Ring Theoretic Aspects of Quandles*, arXiv:1805.05908 (2018), especially Section 4.2 and Proposition 4.18. https://arxiv.org/abs/1805.05908
- V. Bardakov and M. Elhamdadi, *Idempotents and Powers of Ideals in Quandle Rings*, arXiv:2601.07057 (first posted 2026-01-11), Sections 4–5. https://arxiv.org/abs/2601.07057
- B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550 (first posted 2026-08-03). https://arxiv.org/abs/2608.01550
