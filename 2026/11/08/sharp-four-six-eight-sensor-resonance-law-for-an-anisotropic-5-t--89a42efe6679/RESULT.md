# Sharp four-six-eight sensor resonance law for an anisotropic \(5\times7\) Fourier torus

## Finding
Let \(G=\mathbb Z_5\times\mathbb Z_7\), with all coordinates reduced in their respective cyclic groups. For \(r>0\), define the normalized anisotropic nearest-neighbor operator
\[
(T_r f)(x,y)=\frac{r(f(x+1,y)+f(x-1,y))+f(x,y+1)+f(x,y-1)}{2(r+1)}.
\]
A fixed sensor set \(S\subset G\) recovers all initial signals when the measurements \((T_r^t f)(s)\), \(s\in S\), \(t\ge0\), uniquely determine every \(f\in\mathbb C^G\).

Write
\[
a_i=\cos(2\pi i/5)\quad(0\le i\le2),\qquad
b_j=\cos(2\pi j/7)\quad(0\le j\le3),
\]
and define the exact finite set of positive couplings
\[
\mathcal R=\left\{r_{ik;\ell j}=\frac{b_\ell-b_j}{a_i-a_k}:0\le i<k\le2,\quad0\le\ell<j\le3\right\}.
\]
**Theorem.** All 18 displayed ratios are different. The minimum possible size \(m(r)\) of a fixed vertex-sensor set satisfies
\[
m(r)=\begin{cases}
4,&r\notin\mathcal R,\\
4,&r=r_{ik;\ell j},\ i=0,\ \ell=0,\\
6,&r=r_{ik;\ell j},\ \text{exactly one of }i,\ell\text{ equals }0,\\
8,&r=r_{ik;\ell j},\ i>0,\ \ell>0.
\end{cases}
\]
There are six, nine, and three exceptional ratios in the respective four-, six-, and eight-sensor strata. In particular, this 35-vertex system needs eight sensors at three isolated positive couplings but only four at every other positive coupling outside the nine six-sensor exceptions.

The following concrete sets attain the minimum (write \(I_s=\{0,\dots,s-1\}\)):

* Off resonance: \(I_2\times I_2\).
* Four-sensor resonance: \(\{(0,0),(1,0),(0,1),(2,1)\}\).
* Six-sensor resonance with \(i=0,\ell>0\): \(I_3\times I_2\).
* Six-sensor resonance with \(i>0,\ell=0\): \(I_2\times I_3\).
* Eight-sensor resonance: \(I_4\times I_2\).

For these sets, the times \(t=0,\ldots,11\) suffice off resonance; at an exceptional coupling \(t=0,\ldots,10\) suffice. The number of distinct eigenvalues is 12 off resonance and 11 at resonance.

## Assumptions and scope
All signals may be arbitrary complex arrays, not bandlimited, sparse, or nonvanishing. The coupling \(r\) is a fixed, exactly known positive real number; the two directions carry relative weights \(r:1\). Sensors are physical vertex evaluations, used at identical locations at each time. The theorem minimizes *spatial sensor count* with unlimited time access; the displayed finite time horizons suffice but are not claimed shortest. No stability bound uniform near resonances is asserted.

## Proof
**1. Fourier reduction.** Each character \(\chi_{u,v}(x,y)=\exp(2\pi i(ux/5+vy/7))\) is an eigenvector of \(T_r\), with eigenvalue
\[
\lambda_{u,v}=\frac{r\cos(2\pi u/5)+\cos(2\pi v/7)}{r+1}.
\]
The distinct cosine levels are indexed by \(i\in\{0,1,2\}\), \(j\in\{0,1,2,3\}\). The orbit at \((i,j)\) has \((1\text{ if }i=0\text{ else }2)(1\text{ if }j=0\text{ else }2)\) independent characters. Hence there are 12 candidate eigenvalues \((ra_i+b_j)/(r+1)\).

Since each \(a_i\) and \(b_j\) decreases strictly with its index, two different levels coincide for positive \(r\) precisely when their indices move in opposite directions: \((i,j)\) coincides with \((k,\ell)\), \(i<k\), \(\ell<j\), at the displayed \(r_{ik;\ell j}\). There are \(\binom32\binom42=18\) possibilities.

**2. No two collisions have the same positive coupling.** The real cyclotomic fields \(K_5=\mathbb Q(\cos(2\pi/5))\) and \(K_7=\mathbb Q(\cos(2\pi/7))\) have degrees 2 and 3, respectively, so their intersection is \(\mathbb Q\). If two ratios agree, dividing their numerator and denominator differences implies that a ratio of two positive \(a\)-differences equals a ratio of two positive \(b\)-differences, and belongs to \(K_5\cap K_7=\mathbb Q\).

The three positive \(a\)-differences are
\[
a_0-a_1=\frac{5-\sqrt5}{4},\qquad
a_0-a_2=\frac{5+\sqrt5}{4},\qquad
a_1-a_2=\frac{\sqrt5}{2}.
\]
No quotient of two *distinct* entries is rational. Similarly, in \(K_7\), the three nontrivial cosine values \(b_1,b_2,b_3\) form a Galois three-cycle with sum \(-\tfrac12\). The traces of all differences \(1-b_j\), \(j>0\), equal \(7/2\), whereas differences \(b_j-b_k\) with \(j,k>0\) have trace zero. Thus a rational quotient of two differences cannot mix these types; between differences \(1-b_j\), equal traces force quotient 1 and the same index. Finally, let \(d_1=b_1-b_2\), \(d_2=b_2-b_3\), \(d_3=b_3-b_1\). A Galois automorphism cyclically permutes \(d_1,d_2,d_3\). If two distinct ones had rational ratio \(c\), iterating the automorphism would imply \(c^3=1\); over \(\mathbb Q\), this gives \(c=1\), forcing all three differences equal and hence zero, a contradiction. The three positive interior differences differ only by orientations of these \(d\)'s, so their pairwise ratios are irrational. Therefore the original equal coupling ratios have the same numerator and denominator pairs, proving distinctness. In particular there can be no triple collision.

**3. Lower bounds.** On any eigenspace of dimension \(d\), evolution is multiplication by one scalar; if fewer than \(d\) vertex sensors are observed, some nonzero vector of that eigenspace vanishes at all those sensors for every time. Thus at least the largest eigenspace dimension is necessary. Away from \(\mathcal R\) that dimension is 4. At the unique collision \((i,j)\sim(k,\ell)\), the dimensions of the two merged character orbits add. Because \(i<k\), \(\ell<j\), this yields precisely 4 when \(i=\ell=0\), 6 when exactly one vanishes, and 8 otherwise. All unaffected eigenspaces have dimension at most 4.

**4. Explicit upper bounds.** Set \(z=\exp(2\pi i a/5)\) for each nonzero spatial frequency in the first factor and \(w=\exp(2\pi i b/7)\) in the second factor. All Fourier matrices with distinct character frequencies and consecutive powers are ordinary Vandermonde matrices, hence full column rank.

Off resonance, \(I_2\times I_2\) separates each \(\{\pm a\}\times\{\pm b\}\) character orbit by the tensor product of two invertible \(2\times2\) Vandermonde matrices (or their single-frequency submatrices).

At four-sensor resonance, the colliding space has the form \(f(x,y)=g(y)+h(x)\), with \(g\in\operatorname{span}\{w^y,w^{-y}\}\) and \(h\in\operatorname{span}\{z^x,z^{-x}\}\), with \(z\ne1\), \(w\ne1\). If this vanishes on \(\{(0,0),(1,0),(0,1),(2,1)\}\), then \(h(0)=h(1)=h(2)\). The \(3\times3\) Vandermonde matrix for frequencies \(1,z,z^{-1}\) at \(x=0,1,2\) forces \(h=0\). Then \(g(0)=g(1)=0\), and the \(2\times2\) Vandermonde matrix for \(w,w^{-1}\) forces \(g=0\). For an unaffected four-dimensional orbit, the two samples at \(y=0\) with \(x=0,1\) and the two at \(y=1\) with \(x=0,2\) each resolve the \(z^{\pm x}\) components, because \(z^2\ne z^{-2}\) for nontrivial fifth roots. The recovered two \(y\)-levels then resolve \(w^{\pm y}\). All smaller orbits are separated likewise.

When \(i=0,\ell>0\), the six-dimensional merged space has first-factor frequencies \(\{0,\pm k\}\); each carries a pair of nonzero second-factor frequencies. The product set \(I_3\times I_2\) resolves the three first-factor frequencies at each \(y\)-level and then separates each pair in the second factor. When \(i>0,\ell=0\), the dual argument uses \(I_2\times I_3\): three second-factor frequencies \(\{0,\pm j\}\) are first resolved, then the two first-factor frequencies in each block. These six-point sets also separate every unaffected orbit.

Finally, when \(i>0,\ell>0\), the merged eigenspace consists of four distinct first-factor frequencies \(\{\pm i,\pm k\}\), each paired with two distinct second-factor frequencies. The product set \(I_4\times I_2\) resolves all four first-factor frequencies followed by the two second-factor frequencies in each block, and also resolves all unaffected eigenspaces.

**5. Time reconstruction.** For every sensor \(s\), expand its trajectory in distinct eigenvalues: \((T_r^t f)(s)=\sum_{\lambda}\lambda^t f_\lambda(s)\). The square time Vandermonde matrix for \(t=0,\ldots,K-1\), with \(K=12\) off resonance and \(K=11\) at resonance, recovers all individual \(f_\lambda(s)\). The injective restrictions from Step 4 then recover each eigenspace vector uniquely. This proves the theorem for every \(r>0\).

## Verification
The accompanying `CHECK.py` independently enumerates all 18 positive ratios and their sensor classes, verifies that the minimum separation of distinct ratio values is positive, checks full column rank of each proposed sampling matrix on every eigenspace, and constructs the complete 35-column time-space observation matrices at the exceptional ratios and an ordinary coupling. Floating-point experiments are corroboration only: the unrestricted assertion and the noncollision classification follow from the exact cyclotomic and Vandermonde arguments above. Run with Python 3 and NumPy: `python CHECK.py`.

## Relationship to prior work
General finite-dimensional dynamical sampling criteria characterize observability using restrictions of the sensor vectors to the eigenvalue eigenspaces. Bulai, Cabrelli, Cordero, Molter and Saliani (2026), Theorem 4.1, presents precisely this criterion in graph sampling, but treats finite path graphs for numerical demonstration and does not evaluate the 18 algebraic couplings or the sharp vertex-sensor geometry for the weighted \(5\times7\) cyclic product. Aldroubi, Cabrelli, Krishtal and Molter's survey discusses the general frame-of-iterations framework. Doostmohammadian (2020) addresses *structural* observability of Cartesian graph products with generic independent edge weights, a different problem from the exact single-parameter weighted adjacency considered here. The present contribution is the full arithmetic resonance stratification and explicit optimal vertex sets, not the general diagonalizable-operator criterion.

## Limitations
The result is for this smallest unequal pair of odd prime cycle lengths \(5\) and \(7\), known exact anisotropy, identical fixed sensors at each time, and noiseless recovery of all signals. It neither bounds conditioning uniformly near collisions nor proves the displayed time horizons are shortest. Exceptional parameters may be highly sensitive to perturbation. Earlier equivalent spectral-observability classifications under another terminology cannot be ruled out without independent literature verification.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley--Wiener Spaces*, first arXiv posting 2026-09-21, arXiv:2609.25472, https://arxiv.org/abs/2609.25472 . Particularly Section 4 and Theorem 4.1.
2. A. Aldroubi, C. Cabrelli, I. Krishtal, U. Molter, *Dynamical Sampling: A Survey*, arXiv:2511.10769, https://arxiv.org/html/2511.10769 . Particularly Section 2.2.1.
3. M. Doostmohammadian, *Recovering the Structural Observability of Composite Networks via Cartesian Product*, arXiv:2001.04699, https://arxiv.org/abs/2001.04699 . Particularly Section IV.
