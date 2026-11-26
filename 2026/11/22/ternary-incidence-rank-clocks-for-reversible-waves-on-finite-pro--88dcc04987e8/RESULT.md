# Ternary incidence-rank clocks for reversible waves on finite projective planes

## Finding

Let \(\Pi\) be a finite projective plane of order \(s\) divisible by \(3\), let \(v=s^2+s+1\), and write \(B\) for its point-by-line incidence matrix. Put
\[
A=\begin{pmatrix}0&B\\ B^{\mathsf T}&0\end{pmatrix},\qquad \rho=\operatorname{rank}_{\mathbb F_3} B.
\]
On ordered pairs \((u,w)\in K^{2v}\times K^{2v}\) over any \(K=\mathbb F_Q\) with \(Q=3^f,\ f\ge1\), the reversible update \(T(u,w)=(Au-w,u)\) has exact order \(12\). For every positive integer \(t\), its fixed-state count is \(Q^{E(t)}\), where
\[
E(t)= (1+\mathbf1_{2\mid t})\min(3^{\nu_3(t)},2)
 +\begin{cases}
 0,&4\nmid t,\\
 4(v-\rho),&4\mid t,\ 3\nmid t,\\
 4(v-1),&12\mid t.
 \end{cases}
\]
Here \(\nu_3(t)\) is the exponent of three in \(t\). The realized least periods are exactly \(1,2,3,4,6,12\); for each \(d\mid12\) there are \(P_d=\sum_{e\mid d}\mu(d/e)Q^{E(e)}\) states of least period \(d\), or \(P_d/d\) directed temporal cycles of that period, with \(\mu\) the Möbius function.

The fourth iterate is the first whose fixed population involves the incidence rank. In particular, the complete temporal census determines \(\rho\) and is determined by it (for fixed \(s,Q\)):
\[
\boxed{\ \rho=v+\frac12-\frac14\log_Q|\operatorname{Fix}(T^4)|\ }. 
\]

## Assumptions and scope

The plane need not be Desarguesian. All matrices in the wave are reduced to characteristic three, and incidence rank is unchanged by extension from \(\mathbb F_3\) to \(K\). Both time levels are labeled and ordered; states are not taken modulo graph automorphisms or time shifts. The all-zero state is included. Temporal cycles are counted with their phases identified. The finding requires \(3\mid s\); the other plane orders are not part of the new claim.

## Proof

Counting common incident lines of two points and common incident points of two lines gives \(BB^{\mathsf T}=B^{\mathsf T}B=sI+J\), with \(J=\mathbf1\mathbf1^{\mathsf T}\). Row and column sums of \(B\) are \(s+1\). In characteristic three, \(s=0\) and \(v=1\) as field scalars. Thus each shore splits into its constant direction \(U\) and the sum-zero space \(W\); both \(B\) and \(B^{\mathsf T}\) preserve the splitting between the shores. The restrictions to the constant directions are the identity maps. On \(W\), \(J=0\), so the adjacency restricted to the two sum-zero shores satisfies \(A_W^2=0\). The rank of \(A_W\) is \(2(\rho-1)\), since each direction of incidence on the sum-zero shores has rank \(\rho-1\). This is positive: if \(B\) vanished on \(W\) then it would annihilate each difference of two line coordinate vectors, making distinct incidence columns equal modulo three, which is impossible for distinct binary columns.

The wave is invertible, with \(T^{-1}(u,w)=(w,Aw-u)\); it preserves the two-time-level constant and sum-zero sectors. On the constant shores \(A\) swaps the two constant directions, so it has a line at each adjacency eigenvalue \(c=1,-1\). Each line gives a two-dimensional companion block with polynomial \(X^2-cX+1=(X+c)^2\) in characteristic three. Its off-diagonal entry is nonzero, so the temporal eigenvalue \(-c\) has a single Jordan block of length two. For such a block write it as \(\lambda(I+M)\), where \(M^2=0\) and \(\operatorname{rank}M=1\). The fixed dimension of its \(t\)-th power is zero if \(\lambda^t\ne1\), is one if \(\lambda^t=1\) and \(3\nmid t\), and is two if \(\lambda^t=1\) and \(3\mid t\). This gives the first term in \(E(t)\).

On the two-time-level sum-zero sector, of dimension \(4(v-1)\), put \(D=\operatorname{diag}(A_W,A_W)\). Direct multiplication gives \(T^2+I=TD\) on this sector, and \(D\) commutes with \(T\). Thus \((T^2+I)^2=0\). The roots of \(X^2+1\) in an algebraic closure both have order four, so if \(4\nmid t\) the polynomials \(X^t-1\) and \((X^2+1)^2\) are coprime, implying no nonzero fixed vectors in this sector by Bézout. This argument works whether or not \(X^2+1\) splits in \(K\).

Since \(-2=1\) in characteristic three,
\[
T^4-I=(T^2+I)(T^2-I)=TD(I+TD)=TD.
\]
This is a nonzero square-zero operator of rank \(4(\rho-1)\). For \(t=4m\) we have \(T^t-I=mTD\). The fixed dimension there is therefore \(4(v-\rho)\) if \(3\nmid m\) and is \(4(v-1)\) if \(3\mid m\). This proves the other term of \(E(t)\), including on extension fields, and yields the fourth-iterate rank formula.

On the sum-zero sector, a nonzero vector in \(\ker(TD)\) has period four (the kernel is nonzero since \(TD\) is square-zero), and every vector outside the kernel has period twelve. On the constant sector, the eigenline and other vectors of the length-two block at \(+1\) have periods one and three, respectively; at \(-1\) they have periods two and six. Since \(T^{12}\) is the identity and period twelve occurs, all listed periods occur and there are no others. The fixed count at time \(t\) sums the populations whose least periods divide \(t\); Möbius inversion gives the formula for \(P_d\). Dividing by \(d\) counts cycles without counting their phases separately.

## Verification

The packaged `verify_planes.py` (Python and NumPy) constructs homogeneous-coordinate examples; `verify_affine.py` (standard Python) constructs examples using affine points, slopes and points at infinity. Both contain the order-three Desarguesian plane as the example within this finding's scope. At \(s=3\) they compare the computed rank nullities of the two-level wave for divisor times \(1,2,3,4,6,12\) with \((1,2,2,26,4,52)\). The incidence rank is \(7\) with \(v=13\). The suite's other plane orders are comparisons outside the finding. Finite examples do not prove the all-plane or all-extension statement, which follows from the identities above.

## Relationship to prior work

The characteristic-three plane-order classes not divisible by three, including exact orders \(18\) and \(8\) and primitive-period populations over extension fields, are covered by *A characteristic-three clock bifurcation for reversible waves on projective-plane incidence graphs* (2026-11-17, record `6b80a5b93d97`). Its stated scope excludes the case addressed here. The finding here is the missing case \(3\mid s\), in which the sum-zero adjacency is square-zero and the census recovers the ternary incidence rank. The exact two-level reversible construction is prior work (Vlasov). The characteristic-two plane-wave classification (record `fe075b4d8619`) connects a different time evolution to the binary incidence rank; it does not give the ternary fourth-iterate formula. Lavrauw, Storme and Van de Voorde study modular incidence codes and their duals, not a temporal fixed-state count.

## Limitations

The finding does not classify possible ternary ranks for non-Desarguesian planes, or imply that equal ranks identify isomorphic planes. It is confined to the stated linear wave, not nonlinear rules or spatial quotients. The use of known second-order reversibility and projective-plane incidence identities is not claimed new. The literature comparison credits the available precise scope of the characteristic-three bifurcation record; it does not certify historical priority.

## References

1. *A characteristic-three clock bifurcation for reversible waves on projective-plane incidence graphs*, 2026-11-17. https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-a-characteristic-three-clock-bifurcation-for-reversible-waves-on--6b80a5b93d97
2. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297. https://arxiv.org/abs/1311.4297
3. M. Lavrauw, L. Storme and G. Van de Voorde, *On the code generated by the incidence matrix of points and hyperplanes in PG(n,q) and its dual*, arXiv:1201.3290. https://arxiv.org/abs/1201.3290
4. *The incidence-rank clock of reversible waves on finite projective planes*, characteristic two, 2026-11-08. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-the-incidence-rank-clock-of-reversible-waves-on-finite-projectiv--fe075b4d8619
