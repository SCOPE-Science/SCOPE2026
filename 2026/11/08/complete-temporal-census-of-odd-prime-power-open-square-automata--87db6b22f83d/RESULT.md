# Complete temporal census of odd-prime-power open-square automata

## Finding
Let \(p\) be any odd prime, \(r\ge 1\), \(Q=p^f\) for any \(f\ge1\), \(n=p^r-1\), and \(m=n/2\). On the open square grid \(P_n\square P_n\), let \(B\) send a configuration over \(\mathbb F_Q\) to the simultaneous sum of its existing (non-wrapping) horizontal and vertical neighbors. Write \(J_\ell(\lambda)\) for a Jordan block of size \(\ell\) with eigenvalue \(\lambda\). **The full Jordan form**, over the base field itself, is
\[
 B\sim\bigoplus_{j=1}^{m}\left(J_{2j-1}(4)\oplus J_{2j-1}(-4)\oplus J_{2j-1}(0)^{\oplus2}\right).
\]
All eigenvalues \(0,4,-4\) are interpreted in \(\mathbb F_Q\). In particular, exactly half the state-space dimension is zero-primary and half is invertible.

Set \(H(t)=\sum_{j=1}^{m}\min(t,2j-1)\) for integers \(t\ge0\). For an initial state \(x\), define its **first-periodic-entry time** \(T(x)=\min\{t\ge0:B^t x\text{ belongs to a periodic orbit}\}\). For \(0\le t\le n-1\),
\[
 \#\{x:T(x)\le t\}=Q^{2m^2+2H(t)}.
\]
Thus the sharp maximum is \(\max_xT(x)=n-1\), attained by exactly \(Q^{n^2}-Q^{n^2-2}\) states. Put \(A_0=1\) and \(A_t=Q^{2H(t)}-Q^{2H(t-1)}\) for \(1\le t\le n-1\); \(A_t=0\) for \(t>n-1\). These count zero-primary components by first-entry time.

Let \(o_+=\operatorname{ord}_{\mathbb F_p^\times}(4)\), \(o_-=\operatorname{ord}_{\mathbb F_p^\times}(-4)\). For \(d\ge1\), write \(d=p^{a}u\) with \(p\nmid u\), and define
\[
 E(d)=H(p^a)\left(\mathbf1_{o_+\mid d}+\mathbf1_{o_-\mid d}\right),\quad F(d)=Q^{E(d)},\quad C(d)=\sum_{e\mid d}\mu(d/e)F(e).
\]
Then \(F(d)=\#\operatorname{Fix}(B^d)\), \(C(d)\) is the number of periodic **points** of exact least period \(d\), and \(C(d)/d\) is the number of primitive periodic orbits. Furthermore, for every \(t\ge0\) and \(d\ge1\), the **joint temporal census** is
\[
 \#\{x:T(x)=t,\ \operatorname{per}(B^t x)=d\}=A_t C(d).
\]
Let \(a=\min\{s\ge0:p^s\ge n-1\}\) and \(L=p^a\operatorname{lcm}(o_+,o_-)\). Every periodic orbit has least period dividing \(L\), and at least one primitive orbit has least period exactly \(L\). In particular, \(B^{n-1+L}=B^{n-1}\); both the maximal entrance time and maximal eventual period are sharp.

## Assumptions and scope
The graph has vertices \(\{1,\ldots,n\}^2\), with an edge precisely between sites at Manhattan distance one; boundary sites have fewer neighbors, and there are no self-terms. The update is **linear over a finite field of odd characteristic**. The symbols \(p,r,f,Q,n,m\) are quantified exactly as above, so \(n\ge2\). A periodic point means a point \(y\) satisfying \(B^d y=y\) for some integer \(d\ge1\); first-entry time is not the time to become fixed. Multiplicities and configuration counts refer to *labelled* grid vertices, with no quotient by spatial symmetries. Here \(\mu\) is the number-theoretic Möbius function. If \(p=3,r=1\), then \(n-1=1\) and \(a=0\). The statement does not concern characteristic two, toroidal boundary conditions, or arbitrary square side lengths.

## Proof
**1. Path polynomial and primary splitting.** Write \(A_n\) for the open-path adjacency matrix. Its characteristic polynomials satisfy \(c_0(z)=1\), \(c_1(z)=z\), \(c_k(z)=zc_{k-1}(z)-c_{k-2}(z)\). If \(u+u^{-1}=z\), then \(c_{q-1}(z)=(u^q-u^{-q})/(u-u^{-1})\), where \(q=p^r\). In characteristic \(p\), Frobenius makes this \((u-u^{-1})^{q-1}=(z^2-4)^{(q-1)/2}\), as a polynomial identity even at coincident roots. Hence \(c_n(z)=(z-2)^m(z+2)^m\). Since the tridiagonal path matrix has a cyclic vector (successive powers of an endpoint basis vector span the space), its minimal and characteristic polynomials agree. Therefore \(A_n\sim J_m(2)\oplus J_m(-2)\). The grid operator is \(B=A_n\otimes I+I\otimes A_n\), so it is the direct sum of four size-\(m^2\) blocks whose scalar eigenvalues are \(4,0,0,-4\), with common nilpotent part \(N=J_m(0)\otimes I+I\otimes J_m(0)\).

**2. A prime-power Lefschetz lemma.** For every odd prime \(p\), every \(r\ge1\), and \(m=(p^r-1)/2\), multiplication by \(x+y\) on \(R=\mathbb F_p[x,y]/(x^m,y^m)\) has Jordan blocks of lengths \(1,3,\ldots,2m-1\), once each. Here is a direct determinant verification, not a characteristic-zero extrapolation. The homogeneous degree-\(d\) and degree-\((2m-2-d)\) pieces of \(R\) both have dimension \(d+1\) when \(0\le d\le m-1\). With \(k=m-1-d\), multiplication by \((x+y)^{2k}\) has the binomial Toeplitz determinant
\[
 D_d=\det\left[\binom{2k}{k+j-i}\right]_{0\le i,j\le d}
 =\prod_{i=0}^{d}\frac{(2k+i)!\,i!}{((k+i)!)^2}.
\]
The identity follows, for example, by elementary row/column elimination of consecutive binomial-coefficient minors; it is an identity of **integers** although its individual displayed factors need not be integers. We show \(p\nmid D_d\). For each \(h=p^s\le p^r\), Legendre's formula gives its contribution to \(v_p(D_d)\) as
\[
 \sum_{i=0}^{d}\left(\left\lfloor\frac{2k+i}{h}\right\rfloor+\left\lfloor\frac{i}{h}\right\rfloor-2\left\lfloor\frac{k+i}{h}\right\rfloor\right).
\]
Put \(b=d\bmod h\), \(c=(h-3)/2\), and \(v=(c-b)\bmod h\), choosing \(0\le v<h\). Complete blocks of \(h\) consecutive indices cancel because \(\sum_{j=0}^{h-1}\lfloor(a+j)/h\rfloor=a\) for every nonnegative integer \(a\). The remaining sum is \(\sum_{j=0}^{b}[\lfloor(2v+j)/h\rfloor-2\lfloor(v+j)/h\rfloor]\). If \(b\le c\), then \(v=c-b\) and both floor sums vanish. If \(b>c\), then \(v=h+c-b\); direct threshold counting gives \(\sum_{j=0}^{b}\lfloor(v+j)/h\rfloor=c+1\) and \(\sum_{j=0}^{b}\lfloor(2v+j)/h\rfloor=2(c+1)\). Thus every prime-power contribution is zero. Larger powers contribute zero as the factorial arguments are below \(p^r\). Consequently every middle Lefschetz determinant is a unit modulo \(p\). The symmetric unimodal Hilbert function of \(R\) is \(1,2,\ldots,m,\ldots,2,1\), so these invertible middle maps give the strong Lefschetz decomposition into chains of lengths \(2m-1,2m-3,\ldots,1\). Identifying \(N\) with multiplication by \(x+y\) proves the asserted full Jordan form.

**3. Entrance times.** In the Fitting decomposition of \(B\), the two zero-primary sectors contribute \(2H(t)\) dimensions to \(\ker B^t\), and the two nonzero-primary sectors form an invertible space of dimension \(2m^2\). A state first becomes periodic precisely when its nilpotent component becomes zero; hence the first-entry formula. The largest zero block has length \(2m-1=n-1\), with multiplicity two, so \(\dim\ker B^{n-2}=2m^2-2\). Subtraction gives the sharp extremal population.

**4. Periods.** On \(J_{\ell}(\lambda)=\lambda I+N_\ell\) with \(\lambda\ne0\), the difference \(J_\ell(\lambda)^d-I\) is invertible if \(\lambda^d\ne1\). Otherwise, writing \(d=p^a u\), \(p\nmid u\), its kernel equals \(\ker N_\ell^{p^a}\), by Frobenius followed by a polynomial factor with nonzero constant term, and has dimension \(\min(\ell,p^a)\). Summing the two nonzero eigenvalue sectors gives \(E(d)\) and \(F(d)\). Möbius inversion yields \(C(d)\), and independence of the nilpotent and invertible direct-sum components gives the joint formula. Each nonzero block's order divides \(\operatorname{ord}(\lambda)p^a\); choosing top Jordan-chain vectors in both eigenvalue sectors forces their least-common-multiple \(L\), proving its attainability. The global identity follows from annihilation of the zero-primary sectors by time \(n-1\) and periodicity of the remaining sectors by time \(L\).

## Verification
The standalone scripts `verify_grid.py`, `verify_lefschetz.py`, and `verify_determinant.py`, using only Python 3 and NumPy for the first script, provide independent finite checks. `verify_grid.py` constructs the actual grid adjacency matrix without reference to the Jordan theorem and checks the path characteristic polynomial, kernel dimensions of powers, and the fixed-point formula for temporal exponents 1 through 24 at \((p,r)=(3,1),(3,2),(5,1),(7,1)\). It also enumerates all \(3^4=81\) labelled ternary configurations on the \(2\times2\) grid. `verify_lefschetz.py` independently builds homogeneous truncated-polynomial power maps from binomial coefficients and checks every predicted nilpotent power rank at \((p,r)=(3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(7,2)\). `verify_determinant.py` separately checks 171 exact determinant identities and 64 zero valuation tests at prime-power exponents. Captured outputs are included. These finite checks corroborate, but do not replace, the all-parameter algebraic argument.

## Relationship to prior work
The path-adjacency/Chebyshev recurrence, modular Kronecker-sum Jordan methods, and positive-characteristic strong Lefschetz criteria are existing mathematics. In particular, Norman's modular Jordan-sum analysis (2008 journal volume; publisher records online posting 2010-09-22) and Cook's 2011 full-text strong Lefschetz classification supply broad algebraic background, not claimed as new. Hunziker, Machiavelo and Park (2004) study reversibility of additive square-grid automata through Chebyshev polynomials; this is a closer grid setting but not an inspected full temporal-census theorem. The contribution assessed here is the **explicit complete Jordan and joint entrance/period classification for the natural odd-prime-power open-square family**, including the sharp maximum primitive period and exact extremal-entry population. The reviewed full text of Cook contains no grid-dynamical joint-census statement. General modular block results make the spectral step derivable in principle; no earlier explicit statement of this combined dynamical classification was identified. Historical equivalence remains possible.

## Limitations
No claims are made for square side lengths other than \(p^r-1\), for composite characteristics, for nonlinear rules, or for other boundary conditions. The separate primary texts of Norman (modular Kronecker sums) and Hunziker–Machiavelo–Park (square-grid automata) were not obtained in full despite attempts through lawful access. The originality comparison for their uninspected portions remains a bounded priority risk; a mathematically equivalent treatment may exist. The supplied finite checks cannot prove the infinite family independently of the proof. The full Jordan structure is a synthesis of known algebraic tools applied to this dynamical family, not a claim to invent those tools.

## References
1. David Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979v1, first posted 2011-11-21. https://arxiv.org/abs/1111.4979 . In particular Theorem 4.9 treats strong Lefschetz existence for equal two-variable exponents.
2. C. W. Norman, *On Jordan bases for the tensor product and Kronecker sum and their elementary divisors over fields of prime characteristic*, Linear and Multilinear Algebra 56 (2008), 415–451, DOI 10.1080/03081080701395640; publisher displays online date 2010-09-22. https://doi.org/10.1080/03081080701395640 . Full text unavailable for this comparison.
3. M. Hunziker, A. Machiavelo and J. Park, *Chebyshev polynomials over finite fields and reversibility of σ-automata on square grids*, Theoretical Computer Science 320 (2004), 465–483, DOI 10.1016/j.tcs.2004.03.031. https://doi.org/10.1016/j.tcs.2004.03.031 . Full text unavailable for this comparison.
4. Jaap Scherphuis, *Lights Out Mathematics*, mathematical expository article at https://www.jaapsch.net/puzzles/lomath.htm . Its rectangular-grid polynomial and nullity methods provide background, not a temporal orbit census.
