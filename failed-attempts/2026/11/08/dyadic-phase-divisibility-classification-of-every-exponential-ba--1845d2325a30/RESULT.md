# Dyadic phase-divisibility classification of every exponential basis of prime-graph transversals

## Finding
Let \(p\) be an odd prime, let \(k\ge2\), put \(q=2^k\), and let \(f:\mathbb Z_p\to\mathbb Z_q\) be any function. Define its graph in \(G=\mathbb Z_p\times\mathbb Z_q\) by
\[
A_f=\{(x,f(x)):x\in\mathbb Z_p\}.
\]
An exponential spectrum is a literal \(p\)-element subset \(B\subset\widehat G\cong G\) whose associated character restrictions form an orthogonal basis of \(\mathbb C^{A_f}\). Let
\[
h_f=\gcd\bigl(q,\{f(x)-f(y):x,y\in\mathbb Z_p\}\bigr),
\]
where the greatest common divisor is taken over any integer lifts (and \(h_f=q\) for a constant function). Define the annihilator subgroup
\[
H_f=\{v\in\mathbb Z_q:v(f(x)-f(y))=0\pmod q\text{ for all }x,y\}=\frac q{h_f}\mathbb Z_q.
\]
Then **every** exponential spectrum is exactly a graph
\[
B_{v}=\{(u,v(u)):u\in\mathbb Z_p\},
\]
where all values \(v(u)\) lie in a **single coset** of \(H_f\). Conversely every such graph is a spectrum. Consequently
\[
\boxed{\#\operatorname{Spec}(A_f)=q\,h_f^{p-1}.}
\]
In particular the possible spectrum multiplicities are exactly
\[
\boxed{2^{k+r(p-1)}\qquad (r=0,1,\ldots,k).}
\]
All occur. The exact number of functions \(f\) giving the value indexed by \(r\) is
\[
\boxed{N_r=2^r(2^{k-r})^p-2^{r+1}(2^{k-r-1})^p\quad (0\le r<k),\qquad N_k=2^k.}
\]
These counts sum to \(q^p\), and each distinct graph appears once. This gives every orthonormal exponential basis and the entire multiplicity distribution for this infinite nonsquare-free family.

For \(q=4\) the three regimes, for nonconstant parity-varying \(f\), nonconstant constant-parity \(f\), and constant \(f\), have respectively \(4\), \(2^{p+1}\), and \(4^p\) spectra. In particular these multiplicity jumps detect successive dyadic agreements among graph heights.

## Assumptions and scope
The group is the **finite abelian product** \(G=\mathbb Z_p\times\mathbb Z_{2^k}\) with \(p\) an odd prime and \(k\ge2\). Because \(p\) and \(q\) are coprime, it is abstractly cyclic of order \(pq\); the product coordinates specify which transversals are under consideration. Characters are \(\chi_{u,v}(x,y)=\exp(2\pi i(ux/p+vy/q))\). No arithmetic regularity of \(f\) is assumed, and spectra are counted as actual subsets rather than quotienting by translations, permutations, or affine equivalences. The cardinality of the graph is \(p\).

## Proof
**1. Dyadic sums of odd length cannot vanish.** For \(q=2^k\), let \(\omega=\exp(2\pi i/q)\). If a sum of \(p\) (not necessarily distinct) \(q\)-th roots vanishes, its multiplicity polynomial \(P(X)=\sum_{j=0}^{q-1}n_j X^j\), with \(n_j\ge0\) and \(\sum_j n_j=p\), is divisible over \(\mathbb Q[X]\) by \(\Phi_q(X)=X^{q/2}+1\). Since \(\deg P<q\), divisibility forces \(n_j=n_{j+q/2}\) for every \(0\le j<q/2\). Thus \(p=2\sum_{j<q/2}n_j\) is even, contradicting odd \(p\). The same argument applies to any power of \(\omega\).

**2. Every spectrum is a frequency graph.** If two distinct frequency pairs \((u,v),(u',v')\) have \(u=u'\), their inner product restricted to \(A_f\) is \(\sum_{x\in\mathbb Z_p}\omega^{(v-v')f(x)}\). It cannot vanish by Step 1. Thus the first coordinates of the \(p\) members of an orthogonal frequency set are pairwise distinct, and any spectrum is uniquely of the form \(B_v\) above.

**3. Exact cross-frequency criterion.** For \(w=u-u'\ne0\pmod p\) and \(d=v(u)-v(u')\), the relevant inner product is
\[
F_f(w,d)=\sum_{x=0}^{p-1}\zeta^{wx}\omega^{df(x)},\qquad \zeta=\exp(2\pi i/p).
\]
Because \(\gcd(p,q)=1\), the cyclotomic polynomial \(\Phi_p(X)=1+X+\cdots+X^{p-1}\) remains irreducible over \(\mathbb Q(\omega)\): the cyclotomic fields \(\mathbb Q(\zeta)\) and \(\mathbb Q(\omega)\) have coprime conductors and trivial intersection. Reindexing by multiplication by \(w\), we see that \(F_f(w,d)=0\) if and only if all its \(p\) coefficients in \(\mathbb Q(\omega)\) are equal. Explicitly,
\[
F_f(w,d)=0\quad\Longleftrightarrow\quad
\omega^{d(f(x)-f(y))}=1\ \text{for every }x,y
\quad\Longleftrightarrow\quad d\in H_f.
\]
The forward implication follows since a degree-at-most-\(p-1\) polynomial vanishing at a primitive \(p\)-th root must be a scalar multiple of \(\Phi_p\), and the reverse follows from \(\sum_{x}\zeta^{wx}=0\). This criterion is independent of the nonzero first-coordinate difference \(w\).

**4. Spectrum classification and count.** All pairwise frequency differences \(v(u)-v(u')\) must therefore belong to \(H_f\). This is equivalent to the values of \(v\) belonging to one coset of \(H_f\). The group \(H_f\) has cardinality \(h_f\): if the integer differences and \(q\) have gcd \(h_f\), the solutions \(d\) to all their annihilation congruences are the multiples of \(q/h_f\). There are \(q/h_f\) possible cosets, and for each coset exactly \(h_f^p\) functions \(v\). Hence the number of distinct spectra is \((q/h_f)h_f^p=q h_f^{p-1}\), proving both directions and the exact formula.

**5. Entire multiplicity distribution.** For \(0\le r\le k\), the condition \(2^r\mid h_f\) means that all \(p\) values of \(f\) are congruent modulo \(2^r\). The number of such functions is exactly \(T_r=2^r(2^{k-r})^p\), by choosing the common residue and then the \(p\) lifts independently. The number with \(h_f=2^r\) is \(T_r-T_{r+1}\) when \(r<k\), and \(T_k=q\) when \(r=k\). This yields the displayed formulas. Positivity for every \(r\) follows from odd \(p\ge3\), and telescoping gives total \(T_0=q^p\).

## Verification
The standalone `CHECK.py` independently evaluates exact cyclotomic Fourier sums using integer-vector arithmetic in \(\mathbb Z[X]/(\Phi_{pq})\). It tests every graph \(f\) and every possible first-coordinate-injective frequency graph \(B_v\) for \((p,q)=(3,4),(3,8),(5,4)\), checks every orthogonality condition, and compares the complete resulting multiplicity histograms with the theorem. Expected output begins with exact counts \(\{4:48,16:12,64:4\}\) for \((3,4)\), \(\{8:384,32:96,128:24,512:8\}\) for \((3,8)\), and \(\{4:960,64:60,1024:4\}\) for \((5,4)\). It ends with `CHECK_OK exact_cyclotomic=True`. These are finite corroborations; the proof above handles every odd prime and every dyadic modulus \(q\ge4\).

## Relationship to prior work
Tan and Zhang (2026) characterize spectrality in square-free cyclic groups, a relevant setting when the dyadic factor is only two. The present result instead treats **all dyadic factors \(2^k\) for \(k\ge2\)**, where the ambient cyclic order is not square-free, and counts every spectrum rather than merely establishing spectral existence. The published *Exact spectrum multiplicities for four-point spectral sets in \(\mathbb Z_{4p}\)* classifies spectral **four-element** transversals modulo four; the present objects are **\(p\)-element** transversals modulo \(p\). The earlier classification of prime-fiber graph spectra counts graph sets where the *codomain* is a prime group; its boundary \(q=2\) is not asserted as new here. The dyadic gcd hierarchy and formula \(q h_f^{p-1}\) for composite 2-power codomains are the distinguishing result.

## Limitations
This theorem assumes that the domain is of **odd prime** cardinality and the codomain has **power-of-two** cardinality. If the domain is composite, \(\Phi_p\) no longer describes all primitive frequencies; if the codomain is divisible by odd primes, a sum of an odd number of its roots of unity can vanish, invalidating the frequency-graph argument. No classification is claimed in those regimes. An older result in Hadamard-pair or mask-polynomial terminology may imply the same formula; the comparison cannot certify absolute publication priority. No independent mathematical audit has been performed.

## References
1. H. Tan and Y. Zhang, *Fuglede's Conjecture for Cyclic Groups of Square-free Order*, arXiv:2610.02218v1, first public 9 September 2026, https://arxiv.org/abs/2610.02218.
2. *Exact spectrum multiplicities for four-point spectral sets in \(\mathbb Z_{4p}\)*, published-finding corpus, 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-spectrum-multiplicities-for-four-point-spectral-sets-in-ma--41b784251307.
3. *Period rigidity and exact spectrum multiplicities for cyclic prime-fiber graphs*, recent mathematical research record; its prime-codomain hypothesis is not satisfied when \(q=2^k\), \(k\ge2\).
4. R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, arXiv:2005.05800, https://arxiv.org/abs/2005.05800.
