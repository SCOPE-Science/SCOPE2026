# Three-coset Fourier-rank dichotomy in \(C_p\rtimes C_3\)

## Finding
Let \(p\equiv1\pmod3\) be a prime, necessarily \(p\ge7\), and let \(G=C_p\rtimes_t C_3\) with nontrivial order-three multiplier \(t\). For any exact three-point coefficient-one convolution on \(\mathbb C[G]\), the *complete rank diagram* is

| Support geometry | Complex rank | Number of unordered supports |
|---|---:|---:|
| All three points occupy at most two cosets of \(C_p\) | \(3p\) | \(p(p-1)(7p-2)/2\) |
| One point per coset, not a coset of an order-three subgroup | \(3p-2\) | \(p^2(p-1)\) |
| A coset of an order-three subgroup | \(p\) | \(p^2\) |

All three ranks occur for every such prime, all supports are included (even nongenerating ones), and no other rank is possible. Thus a transversal of the three quotient cosets has exactly two invisible complex convolution directions, except when its points themselves form a subgroup coset; that exceptional geometry loses \(2p\) directions. The rank \(p\) meets the sharp nonabelian uncertainty lower bound \(3\operatorname{rank}(T_S)\ge3p\).

## Assumptions and scope
Fix \(t\in\mathbb F_p^\times\) satisfying \(t^3=1\) and \(t\ne1\), so \(1+t+t^2=0\) in \(\mathbb F_p\). Write
\[
G=\{a^u b^j:u\in\mathbb F_p,\ j\in\{0,1,2\}\},\quad
b a b^{-1}=a^t,\quad a^p=b^3=e.
\]
Set \(N=\langle a\rangle\). For \(S\subset G\) of three **distinct** elements let \(T_S f=\sum_{s\in S}L_sf\), where \((L_sf)(x)=f(s^{-1}x)\). We count unordered supports, not coefficient tuples; all three coefficients are \(1\). Multiplying the group-algebra element by a group element preserves its convolution rank. This permits normalization without assuming inversion symmetry or that the support generates \(G\). The claim does not cover arbitrary complex weights or primes \(p\not\equiv1\pmod3\).

## Proof
**Irreducibles and rank normalization.** Put \(\omega=e^{2\pi i/3}\) and \(\zeta=e^{2\pi i/p}\). The irreducibles of \(G\) are the three linear characters \(\chi_j(a)=1\), \(\chi_j(b)=\omega^j\), for \(j=0,1,2\), together with \((p-1)/3\) inequivalent representations \(\rho_k\) of dimension three, indexed by the orbits of \(k\in\mathbb F_p^\times\) under multiplication by \(\{1,t,t^2\}\). An explicit model is
\[
\rho_k(a)=D_k=\operatorname{diag}(\zeta^{k},\zeta^{kt},\zeta^{kt^2}),\qquad
\rho_k(b)=P=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.
\]
Indeed \(P D_kP^{-1}=D_k^t\) and \(\sum \dim(\rho)^2=3+(p-1)3=3p\), so these are all irreducibles. A \(d\)-dimensional representation occurs \(d\) times in the left-regular decomposition, whence
\[
\operatorname{rank}T_S=\sum_{j=0}^{2}\operatorname{rank}\sum_{s\in S}\chi_j(s)
 +3\sum_{k\in\mathbb F_p^\times/\langle t\rangle}
  \operatorname{rank}\sum_{s\in S}\rho_k(s).
\]

**Case I: one quotient coset.** Left translation puts \(S\) into the form \(\{e,a^u,a^v\}\), with \(u,v\) distinct nonzero residues. All three linear blocks equal \(3\). Every three-dimensional block is diagonal with entries
\(1+\zeta^{k t^i u}+\zeta^{k t^i v}\), for \(i=0,1,2\). These never vanish: a polynomial with exactly three coefficients equal to one and all other coefficients zero, in degrees \(0,\ldots,p-1\), is not a scalar multiple of \(\Phi_p(X)=1+X+\cdots+X^{p-1}\), the minimal polynomial of \(\zeta\) over \(\mathbb Q\). Hence \(\operatorname{rank}T_S=3p\).

**Case II: two quotient cosets.** Left translation and renaming put \(S=\{e,a^u,a^v b^j\}\), where \(u\ne0\), \(j\in\{1,2\}\). Its linear blocks equal \(2+\omega^{j\ell}\), never zero. For every \(k\ne0\), its three-dimensional multiplier is
\(M_k=I+D_k^u+D_k^vP^j\). Since \(P^j\) is a single three-cycle, only the identity and cycle permutations contribute to its determinant, yielding
\[
\det M_k=\prod_{h\in\{1,t,t^2\}}(1+\zeta^{khu})+1
=3+\sum_{h\in\{1,t,t^2\}}(\zeta^{khu}+\zeta^{-khu}).
\]
To see the last equality, expand the product, use \(1+t+t^2=0\), and pair each two-factor exponent with the negative of the omitted one. The seven residues \(0,\pm ku,\pm ktu,\pm kt^2u\) are pairwise distinct, since the odd-order subgroup \(\langle t\rangle\) does not contain \(-1\). The polynomial representing this determinant has constant coefficient \(3\), six coefficients \(1\), and all remaining coefficients \(0\); it cannot be a scalar multiple of \(\Phi_p\), including at \(p=7\). Thus every block is invertible, and \(\operatorname{rank}T_S=3p\). The invertibility in this occupancy case also follows from the earlier affine three-tap result identified below; this case is included only to complete the diagram.

**Case III: one point in each coset.** Left translation by a normal-subgroup element gives \(S=\{e,a^u b,a^v b^2\}\) with unique \(u,v\in\mathbb F_p\). The linear character sums are \(3,0,0\), contributing rank one. The three-dimensional block is
\[
M_k=I+D_k^uP+D_k^vP^2
 =\begin{pmatrix}
1&\zeta^{ku}&\zeta^{kv}\\
\zeta^{ktv}&1&\zeta^{ktu}\\
\zeta^{kt^2u}&\zeta^{kt^2v}&1
\end{pmatrix}.
\]
Its determinant is
\[
\det M_k=3-\sum_{h\in\{1,t,t^2\}}\zeta^{kh(u+tv)}.
\]
Let \(d=u+tv\). If \(d\ne0\), the three displayed roots of unity are distinct. Their sum has modulus strictly less than \(3\), so no \(M_k\) is singular; the total rank is \(1+3(p-1)=3p-2\). If \(d=0\), then \(v=(1+t)u\), and \(a^v b^2=(a^u b)^2\). Therefore \(S=\{e,h,h^2\}\), where \(h=a^u b\) has order exactly three. For each three-dimensional representation, \(\rho_k(h)\) has eigenvalues \(1,\omega,\omega^2\) (its weighted cyclic permutation has characteristic polynomial \(X^3-1\)); consequently \(I+\rho_k(h)+\rho_k(h)^2\) has rank one. The two nontrivial one-dimensional character sums are zero, giving total rank \(1+3(p-1)/3=p\). More generally, without the normalization, these exceptional supports are exactly the left cosets of order-three subgroups.

**Exact global multiplicities.** The one-coset supports number \(3\binom p3\). The two-coset supports number \(3\cdot2\binom p2 p=3p^2(p-1)\). Their sum is \(p(p-1)(7p-2)/2\). There are \(p^3\) transversals. A transversal with representative \(\{a^x,a^y b,a^z b^2\}\) is exceptional precisely when \(y-x+t(z-x)=0\), which gives exactly one \(z\) for each of the \(p^2\) choices of \(x,y\). The remaining \(p^2(p-1)\) transversals have rank \(3p-2\). Independently, there are \(p\) different order-three subgroups (the \(2p\) elements outside \(N\) all have order three, two per subgroup), each with \(p\) cosets, again \(p^2\) exceptional supports. The three multiplicities sum to \(\binom{3p}{3}\), proving the stated exhaustive classification.

## Verification
Run the dependency-free Python files `check_regular.py` and `check_blocks.py` in the same directory as this document. The former builds the full left-convolution matrices, independently computes their exact complex ranks using a prime-field reduction with a proved Hadamard lifting bound, and checks all \(\binom{21}{3}=1330\) supports at \(p=7\) and all \(\binom{38}{2}=703\) identity-containing normalized supports at \(p=13\). Left translation then gives exact global counts. Every matrix entry is zero or one, and the absolute value of any minor of size at most \(3p\) is at most \(3^{3p/2}\). For \(p\in\{7,13\}\), this is strictly smaller than the prime modulus \(2^{31}-1\), so a nonzero minor over the integers cannot become zero modulo this prime, and all modular ranks are exactly the complex ranks.

The second checker uses a separate direct coefficient test in \(\mathbb Q[\zeta_p]\): a reduced sum of powers of a primitive \(p\)-th root vanishes exactly when all \(p\) integer coefficients are equal. It checks the exact determinant obstructions and the complete support distributions for \(p=7,13,19,31\). The recorded programs and their actual outputs are included as `CHECK_OUTPUT.txt`. These finite checks corroborate the proof; the theorem for all eligible primes follows from the representation and cyclotomic arguments above, not from extrapolation.

## Relationship to prior work
The nonabelian rank-weighted uncertainty principle of Alagic and Russell [1] supplies the general sharp lower bound and acknowledges equality for subgroup indicators, but it does not classify the rank \(3p-2\) of noncoset transversals or their exact multiplicity. Arezoomand and Taeri [2] provide general Cayley-graph Fourier factorization; the block method is standard, not claimed as new. A published affine three-tap classification [3] establishes invertibility for precisely the two-normal-coset/one-dilation configuration: with a complement of order three, \((-2)^3\ne1\pmod p\), so the prior condition rules out singularity. The present distinguishing assertion is the transversal dichotomy and full exact support census, not that previously settled invertibility result. A published complete three-tap dihedral result [4] concerns an order-two inversion complement and does not imply the order-three Frobenius case. Bell and Minei [5] analyze spectra of particular affine graphs, but the accessible abstract does not establish or exclude the present arbitrary-transversal statement; their entire original article was not available for comparison.

## Limitations
This is an algebraic rank classification for three distinct *unit-weight* taps, not a statement about arbitrary complex weights, eigenvalue signs, numerical conditioning, or every finite group. Although the proof is valid for all prime \(p\equiv1\pmod3\), the exact matrix replay is finite. The complete original text of Bell and Minei [5] was inaccessible through the attempted lawful sources; a specialized, historically prior equivalent transversal calculation not indexed in the inspected literature remains possible. Independent mathematical audit and publication-priority certification have not been performed.

## References
1. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702 (first public 2006-08-28); https://arxiv.org/abs/math/0608702 .
2. M. Arezoomand and B. Taeri, *On the characteristic polynomial of n-Cayley digraphs*, Electronic Journal of Combinatorics 20(3) (2013), P57, DOI https://doi.org/10.37236/3105 .
3. *Affine three-tap convolution: an exact subgroup threshold for invertibility*, published research record; https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-affine-three-tap-convolution-an-exact-subgroup-threshold-for-inv--dd2fb1d76981 .
4. *Complete ternary-convolution nullity laws on finite dihedral groups*, published research record; https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-ternary-convolution-nullity-laws-on-finite-dihedral-gro--2bbf4bdce108 .
5. D. Bell and E. Minei, *Spectral analysis of the affine graph over the finite ring*, Linear Algebra and its Applications 414 (2006), 244–265, DOI https://doi.org/10.1016/j.laa.2005.09.020 ; abstract inspected, full text unavailable.
