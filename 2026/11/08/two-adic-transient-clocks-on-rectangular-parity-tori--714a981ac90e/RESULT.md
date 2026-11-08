# Two-adic transient clocks on rectangular parity tori

## Finding

For integers \(m,n\geq3\), let \(G=C_m\square C_n\), and let \(A\) be its open-neighborhood adjacency operator over any finite field \(\mathbb F_Q\) of characteristic two. The synchronous update is \(x\mapsto Ax\): each vertex receives the sum of its four neighbors. Write
\[
m=2^a m_0,\quad n=2^b n_0,\quad m_0,n_0\ \text{odd},\quad
L=2^{\max(a,b)},\quad k=2^{\min(a,b)},\quad g=\gcd(m_0,n_0).
\]
These definitions include \(a=0\) or \(b=0\), so \(L,k\geq1\) and \(g\) is odd. The **entire nilpotent Jordan structure** of \(A\) at eigenvalue zero is
\[
\begin{cases}
(1)^{\oplus(2g-1)},&L=1,\\[3pt]
(L/2)^{\oplus 2k}\ \oplus\ L^{\oplus 2(g-1)k},&L\geq2.
\end{cases}
\]
In the second line, there are no length-\(L\) blocks when \(g=1\). The nilpotent dimension is \(z=(2g-1)kL\), and the invertible, recurrent Fitting space has dimension \(d=mn-z\).

Define the cumulative nullity for integers \(t\geq0\) by
\[
c(t)=\begin{cases}
(2g-1)\min(t,1),&L=1,\\
2k\min(t,L/2)+2(g-1)k\min(t,L),&L\geq2.
\end{cases}
\]
Then \(\dim\ker(A^t)=c(t)\) for every integer \(t\geq0\). The number of labelled configurations whose **first** entrance into a periodic orbit occurs after exactly \(t\) updates is
\[
N_0=Q^d,\qquad
N_t=Q^d\bigl(Q^{c(t)}-Q^{c(t-1)}\bigr)\quad(t\geq1).
\]
The sharp maximum first-entry time is \(T=1\) for \(L=1\); \(T=L\) for \(L\geq2\) and \(g>1\); and \(T=L/2\) for \(L\geq2\) and \(g=1\). In particular, the maximum-entry fraction of uniformly sampled initial configurations is, respectively,
\[
1-Q^{-(2g-1)},\qquad 1-Q^{-2(g-1)k},\qquad 1-Q^{-2k}.
\]
All statements hold for every finite characteristic-two alphabet, not only binary states.

## Assumptions and scope

A cycle \(C_m\) has distinct neighbors \(i-1\) and \(i+1\), hence the restriction \(m,n\geq3\). The graph has \(mn\) labelled vertices \((i,j)\) with indices taken modulo \(m\) and \(n\). There is no self-inclusive term, asynchronous update, randomness in the update, or duplicated edge. Here \(\mathbb F_Q\) has order \(Q=2^f\), \(f\geq1\). The first-periodic-entry time of \(x\) is the smallest \(t\geq0\) for which \(A^t x\) lies on a finite cycle under \(A\), whether or not the orbit is fixed. The theorem counts first-entry times, not the lengths or numbers of recurrent cycles.

## Proof

**1. Local algebra and the zero locus.** Identify the state space with the group algebra
\[
R=\mathbb F_Q[X^{\pm1},Y^{\pm1}]/(X^m-1,Y^n-1).
\]
The update is multiplication by \(P=X+X^{-1}+Y+Y^{-1}\). Extend scalars to an algebraic closure \(K\); extension preserves ranks and Jordan block dimensions over \(\mathbb F_Q\). Since \(m_0,n_0\) are odd, the separable factors of \(X^{m_0}-1\) and \(Y^{n_0}-1\) yield a direct product over all ordered roots \(\zeta^{m_0}=\eta^{n_0}=1\), whose local factors are
\[
R_{\zeta,\eta}\cong K[u,v]/(u^{2^a},v^{2^b}),
\qquad X=\zeta+u,\ Y=\eta+v.
\]
On this factor, multiplication by \(P\) is invertible unless its constant term vanishes. The equation is \(\zeta+\zeta^{-1}=\eta+\eta^{-1}\). Multiplying by \(\zeta\eta\) and factoring gives
\[
(\zeta+\eta)(\zeta\eta+1)=0.
\]
Thus \(\eta=\zeta\) or \(\eta=\zeta^{-1}\); necessarily \(\zeta^g=1\). Since \(g\) is odd, the choices comprise the single pair \((1,1)\) plus \(2(g-1)\) other ordered pairs. These are precisely the zero-eigenvalue local components.

**2. Every nonidentity zero pair.** Let \(f(Z)=Z+Z^{-1}\). At a nonidentity root \(\zeta\), its derivative \(f'(\zeta)=1+\zeta^{-2}\) is nonzero in characteristic two; the same holds for \(\eta\). Consequently \(U=f(X)-f(\zeta)\) and \(V=f(Y)-f(\eta)\) are valid truncated local coordinates. After interchanging the variables if necessary, the algebra becomes
\[
K[U,V]/(U^L,V^k),\qquad P=U+V,
\]
where \(L\) and \(k\) are powers of two and \(k\mid L\). Set \(W=U+V\). In characteristic two, \((W+V)^L=W^L+V^L\), and \(V^L=0\) because \(L\geq k\). Therefore the same algebra is \(K[W,V]/(W^L,V^k)\). Multiplication by \(P=W\) has exactly \(k\) independent Jordan chains of length \(L\), one for each power of \(V\). The \(2(g-1)\) components contribute \(2(g-1)k\) length-\(L\) blocks.

**3. The exceptional root \((1,1)\).** If \(L=1\), both local variables vanish and \(P=0\) on this one-dimensional component. Suppose \(L\geq2\). Arrange the local variables so \(u^L=v^k=0\). The characteristic-two identity
\[
f(1+u)=\frac{u^2}{1+u}
\]
holds because \(1+u\) is invertible in the truncated algebra. Thus
\[
P=\frac{u^2}{1+u}+\frac{v^2}{1+v},\qquad P^{L/2}=0.
\]
The latter equality follows by the Frobenius power law \((r+s)^{L/2}=r^{L/2}+s^{L/2}\) and by \(u^L=v^L=0\). For the dimension of the quotient by \(P\), put \(c=v^2/(1+v)\). The relation \(P=0\) is equivalent to \(u^2+c u+c=0\), a monic quadratic relation over \(K[v]/(v^k)\). In the resulting quadratic quotient, \(u^L=0\) follows from raising \(u^2=cu+c\) to the \(L/2\)-th power: since \(c^{L/2}=0\), both terms vanish. Hence the original relation \(u^L=0\) introduces no further quotient constraint. The quotient \(K[u,v]/(u^L,v^k,P)\) is a free rank-two module over \(K[v]/(v^k)\), so its dimension is \(2k\). Therefore the nilpotent operator \(P\) on this \(kL\)-dimensional local algebra has exactly \(2k\) Jordan blocks, all of length at most \(L/2\). Their total length is \(kL=2k(L/2)\), forcing **every** block to have length precisely \(L/2\).

**4. Fitting decomposition and exact temporal census.** Combining Steps 2 and 3 gives the stated complete zero-primary Jordan partition. Its dimension is \(kL+2(g-1)kL=(2g-1)kL\). Every other local factor is invertible, so the Fitting decomposition \(R=R_{\rm nil}\oplus R_{\rm inv}\) has respective dimensions \(z\) and \(d\). An element of this finite-dimensional finite-field dynamical system is periodic from time zero exactly when its nilpotent component is zero, because invertible maps permute finite sets. At time \(t\), it is periodic exactly when its nilpotent component lies in \(\ker A^t\). Thus the cumulative count is \(Q^{d+c(t)}\), and subtracting counts for \(t-1\) gives \(N_t\). The largest block gives the sharp maximum time. The last-layer fraction equals \(1-Q^{-[c(T)-c(T-1)]}\), yielding all three expressions above.

## Verification

The standalone standard-library program `verify_matrix.py` computes open-neighborhood matrices directly as bitsets and independently reduces every power over \(\mathbb F_2\) by Gaussian elimination. It compared all predicted cumulative nullities at **2,229** triples \((m,n,t)\), for \(3\leq m,n\leq24\) with \(mn\leq260\), including a graph with 260 vertices. The independent simulator `verify_orbits.py` exhaustively classified **102,912** labelled binary configurations across four toroidal grids, by detecting the first repeated state and tracing its periodic cycle. Both checks passed. Their executable source and captured outputs accompany this finding. Finite checks do not prove the unbounded classification: that proof is Steps 1–4.

For example, the \(4\times4\) torus has four nilpotent blocks of length two and no invertible part. Of its \(2^{16}\) binary configurations, one is periodic at time zero, 255 first enter at time one, and 65,280 first enter at time two. At \(3\times3\), there are five length-one blocks and four invertible dimensions; the entrance populations are 16 and 496. For each integer \(s\geq2\), the \(2^s\times2^s\) torus has sharp maximum entry time \(2^{s-1}\), exhibiting an unbounded transient clock on a bounded-degree graph family.

## Relationship to prior work

Algebraic analysis of additive cellular automata, including multiple spatial dimensions and periodic boundaries, is developed by Martin, Odlyzko and Wolfram (1984, especially §4D), following Wolfram (1983). The group-algebra representation and the general principle that noninvertible components generate transients are established methods, not new claims here. Peters, Goldwasser and Young (2017, Theorem 2.6) give a characteristic-polynomial gcd criterion for invertibility of open-neighborhood adjacency on arbitrary Cartesian products. This criterion decides a binary invertibility question but not the Jordan block lengths, cumulative nullities, sharp transient index, or temporal population counts here. Munter and Peters (2021, Theorem 5.1) likewise address solvability of graph-product Lights Out systems, not these first-entry statistics. The contribution assessed here is the full toroidal, arithmetic Jordan/entrance classification and the exceptional \((1,1)\)-root analysis; not a claim of new additive-automaton formalism or of a general graph-product invertibility criterion.

## Limitations

This is a result about characteristic two with open-neighborhood synchronous **linear** dynamics on simple Cartesian products of cycles, for both side lengths at least three. It makes no assertion about nonlinear excitation, self-inclusive Lights Out, other characteristics, or the orbit-length census inside the invertible part. The existence of equivalent unindexed formulations or stronger results in less accessible finite-cellular-automata literature has not been ruled out. Some historically relevant papers could only be checked through abstracts and bibliographic records; in particular the full paper by Aso and Honda (1985) could not be examined.

## References

- S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* **55** (1983), 601–644. DOI: 10.1103/RevModPhys.55.601. Published July 1, 1983.
- O. Martin, A. M. Odlyzko, S. Wolfram, “Algebraic Properties of Cellular Automata,” *Communications in Mathematical Physics* **93** (1984), 219–258. DOI: 10.1007/BF01223745. Author-hosted full text: https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf.
- T. Peters, J. Goldwasser, M. Young, “Lights Out! on Cartesian Products,” *Electronic Journal of Linear Algebra* **32** (2017), 464–474. DOI: 10.13001/1081-3810.3483. Full text: https://journals.uwyo.edu/index.php/ela/article/download/1801/1801/1801.
- A. Munter, T. Peters, “Lights Out! on graph products over the ring of integers modulo k,” *Electronic Journal of Linear Algebra* (2021). DOI: 10.13001/ela.2021.5601. Full text: https://journals.uwyo.edu/index.php/ela/article/download/5601/5583/9213.
- H. Aso, N. Honda, “Dynamical characteristics of linear cellular automata,” *Journal of Computer and System Sciences* (1985). DOI: 10.1016/0022-0000(85)90048-0. Abstract-level inspection only.
