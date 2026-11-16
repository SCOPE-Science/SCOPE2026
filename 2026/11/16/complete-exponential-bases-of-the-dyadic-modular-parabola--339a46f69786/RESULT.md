# Complete exponential bases of the dyadic modular parabola

## Finding

For every integer \(k\ge1\) put \(N=2^k\), \(R_k=\mathbb Z/N\mathbb Z\), and
\[
E_k=\{(t,t^2):t\in R_k\}\subset R_k^2.
\]
For a frequency \((a,b)\in R_k^2\) define the normalized restricted character
\[
\phi_{a,b}(t)=N^{-1/2}\exp\!\bigl(2\pi i(at+bt^2)/N\bigr).
\]
A *spectrum* is an unordered set of exactly \(N\) distinct frequencies whose restricted characters form an orthonormal basis of \(\ell^2(E_k)\), with counting measure. The following gives **every** spectrum and its exact enumeration.

**Base level.** At \(k=1\), the four spectra choose one element of each of the two disjoint classes \(a+b\equiv0\pmod2\) and \(a+b\equiv1\pmod2\).

**Dyadic recursion.** At every \(k\ge2\), all spectra are precisely the disjoint unions
\[
\Lambda=\{(2a,\beta_0+2b):(a,b)\in\Lambda_0\}\ \dot\cup\
\{(1+2a,\beta_1+2b):(a,b)\in\Lambda_1\},
\]
where the displayed coordinates are taken modulo \(2^k\), \(\beta_0,\beta_1\in\{0,1\}\) are arbitrary, and \(\Lambda_0,\Lambda_1\) are arbitrary, independently chosen spectra in \((\mathbb Z/2^{k-1}\mathbb Z)^2\) for the smaller modular parabola. The reconstruction is unique. In particular the exact number \(B_k\) of distinct unordered spectra satisfies \(B_1=4\), \(B_k=4B_{k-1}^2\), so
\[
\boxed{B_k=2^{2^{k+1}-2}\qquad(k\ge1).}
\]
The first values are \(4,64,16384,2^{30}\). Unlike the odd-prime-power setting, the first frequency coordinate need not be injective: for \(N=4\), the set \(\{(0,0),(0,2),(1,0),(1,2)\}\) is a spectrum.

## Assumptions and scope

The ring is \(R_k=\mathbb Z/2^k\mathbb Z\), not the finite field of order \(2^k\); both frequency coordinates are taken modulo \(2^k\). The quadratic graph has one element for each \(t\in R_k\). Frequency sets are counted literally as subsets of the dual group \(R_k^2\), without quotienting by translations, order, automorphisms, or other equivalence relations. The classification includes \(k=1\) and all higher exponents, but makes no claim for other quadratic maps or odd-modulus mixed factors.

## Proof

**1. A forced even/odd spectral split.** Fix \(k\ge2\) and let \(H=N/2\). Because
\[
(t+H)^2-t^2=Nt+H^2\equiv0\pmod N,
\]
translation \(\tau f(t)=f(t+H)\) satisfies \(\tau\phi_{a,b}=(-1)^a\phi_{a,b}\). This involution on the \(N\)-dimensional function space has even and odd eigenspaces each of dimension \(H\), because it exchanges the two points in every pair \(\{t,t+H\}\). Therefore every orthonormal basis formed from the restricted characters has exactly \(H\) frequencies with even \(a\) and exactly \(H\) with odd \(a\). The two sectors are automatically orthogonal.

**2. Within a sector the parity of the quadratic coefficient is forced.** Write the unnormalized restricted-character inner product as the quadratic Gauss sum
\[
G_N(A,B)=\sum_{t\bmod N}\exp\!\bigl(2\pi i(At+Bt^2)/N\bigr).
\]
If \(A\) is even and \(B\) is odd, choose \(c\) satisfying \(2Bc\equiv A\pmod N\), possible because \(B\) is a unit. Completing the square by translation gives
\[
|G_N(A,B)|=|G_N(0,B)|.
\]
Expanding the square and substituting \(t=s+u\), then summing the variable \(s\), yields
\[
\begin{aligned}
|G_N(0,B)|^2
&=\sum_{u,s\bmod N}\exp\!\bigl(2\pi iB(u^2+2us)/N\bigr)\\
&=N\sum_{u:2Bu\equiv0\ (\mathrm{mod}\ N)}\exp\!\bigl(2\pi iBu^2/N\bigr).
\end{aligned}
\]
The congruence has exactly two solutions \(u=0,H\). Since \(H^2\equiv0\pmod N\) for \(k\ge2\), both exponentials equal one. Hence \(|G_N(A,B)|^2=2N>0\). Thus two orthogonal restricted characters with first coordinates of the same parity necessarily also have second coordinates of the same parity.

**3. Exact reduction to half the modulus.** Consequently the \(H\) frequencies in each first-coordinate parity class \(\alpha\in\{0,1\}\) share a unique quadratic-coordinate parity \(\beta_\alpha\). Write them as \((\alpha+2a,\beta_\alpha+2b)\), uniquely with \(a,b\in R_{k-1}\). The corresponding characters factor as
\[
\phi_{\alpha+2a,\beta_\alpha+2b}(t)
=N^{-1/2}\exp\!\bigl(2\pi i(\alpha t+\beta_\alpha t^2)/N\bigr)
\exp\!\bigl(2\pi i(at+bt^2)/H\bigr).
\]
The first exponential is a common unit-modulus factor within the sector. The second factor is \(H\)-periodic in \(t\), and its normalized inner products on the \(N\) points equal the normalized inner products of the corresponding \(H\)-point restricted characters for \(E_{k-1}\). Thus orthogonality of the \(H\) vectors in that sector is equivalent to the reduced \(H\)-element frequency set being a full spectrum of \(E_{k-1}\). By Step 1, the two sectors are mutually orthogonal. This proves necessity and sufficiency of the recursion. The parity bits, parity sectors and halved coordinates are read uniquely from any spectrum, so there is no overcount.

**4. Base and count.** In \(R_1\) one has \(t^2=t\), so \(\phi_{a,b}(t)=2^{-1/2}(-1)^{(a+b)t}\). Of the four frequencies, two induce the constant character and two induce the alternating character; any orthonormal basis chooses one from each class. Thus \(B_1=2\cdot2=4\). The unique recursive decomposition permits four independent parity-bit pairs and two freely chosen smaller spectra, giving \(B_k=4B_{k-1}^2\). Setting \(B_k=2^{c_k}\) yields \(c_1=2\), \(c_k=2+2c_{k-1}\), and therefore \(c_k=2^{k+1}-2\). This proves the claimed classification and exact count for every \(k\ge1\).

## Verification

Run the included standalone standard-library checker with `python3 check_spectra.py`. It uses the **exact** cyclotomic equality criterion for sums of \(2^k\)-th roots of unity: an integer-coefficient sum vanishes iff the coefficient counts at exponents \(j\) and \(j+2^{k-1}\) agree for every \(j<2^{k-1}\). For every \((A,B)\bmod2^k\) it confirms the essential parity and reduction lemmas at \(k=2,3,4,5\) (and checks the base). Independently, it constructs full pairwise-orthogonality graphs and counts all cliques of size \(2^k\) for \(k=1,2,3\), obtaining \(4,64,16384\). Integer enumeration verifies only these finite cases; the infinite classification follows from the proof above.

## Relationship to prior work

Iosevich and Koh (2008) study Fourier restriction and extension estimates for quadratic surfaces **over finite fields**. Their inequalities do not classify exponential bases for the modular curve over \(\mathbb Z/2^k\mathbb Z\). Fan, Fan and Shi (2015) characterize spectral subsets of **one-dimensional** cyclic prime-power groups and their related \(p\)-adic analogues by homogeneous trees, but do not evaluate spectra of this polynomial graph in the two-dimensional product ring. The later result *Complete exponential spectra of the parabola over odd prime-power rings* classifies the corresponding problem for **odd** primes by strictly contracting frequency graphs. Its crucial Gauss-sum argument uses invertibility of two, and its graph structure and enumeration do not cover the present dyadic case. The present theorem is the even-prime counterpart with a different, two-sector recursive structure and a different count, rather than a renamed odd-prime formula.

## Limitations

The theorem classifies literal frequency sets, not their orbits under any symmetry group. It is specific to the dyadic ring and the graph of the square map. It does not claim novelty of elementary quadratic-Gauss-sum identities, finite cyclic spectral-set definitions, or orthogonality constructions in general. An older equivalent dyadic quadratic-graph basis enumeration not discovered in bounded literature comparison remains a historical-priority risk. Independent mathematical validation has not been performed.

## References

- Alex Iosevich and Doowon Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first posted 2008-04-28, https://arxiv.org/abs/0804.4505.
- Aihua Fan, Shilei Fan and Ruxi Shi, *Compact Open Spectral Sets in \(\mathbb Q_p\)*, arXiv:1511.04837v1, first posted 2015-11-16, https://arxiv.org/abs/1511.04837.
- *Complete exponential spectra of the parabola over odd prime-power rings*, public research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-complete-exponential-spectra-of-the-parabola-over-odd-prime-powe--2cf08dd7e325/RESULT.md. (Odd-prime-only theorem; used for a direct noncoverage comparison.)
