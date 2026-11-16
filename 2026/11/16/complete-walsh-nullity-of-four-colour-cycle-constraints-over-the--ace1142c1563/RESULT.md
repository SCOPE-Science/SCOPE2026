# Complete Walsh nullity of four-colour cycle constraints over the Klein four-group

## Finding
For each integer \(n\ge3\), label the vertices of the cycle \(C_n\) in cyclic order. Write the four colour names as the additive group \(G=\mathbb F_2^2\). Let \(A_n\) consist of all colourings \(x=(x_1,\ldots,x_n)\in G^n\) satisfying \(x_i\ne x_{i+1}\) at each edge, with indices read cyclically. Define the **unnormalized** Walsh coefficients
\[
W_n(\alpha)=\sum_{x\in A_n}(-1)^{\sum_{j=1}^n\langle\alpha_j,x_j\rangle},\qquad \alpha\in G^n.
\]
Every coefficient with \(\sum_j\alpha_j\ne0\) is zero. For \(\sum_j\alpha_j=0\), define the prefix frequencies \(\beta_j=\sum_{i=1}^j\alpha_i\) for \(1\le j<n\), and for each \(g\in G\) put \(k_g=\#\{1\le j<n:\beta_j=g\}\). Then **every** multiplier has the exact formula
\[
\boxed{W_n(\alpha)=(-1)^{n-1}\left(3(-3)^{k_0}-\sum_{g\in G\setminus\{0\}}(-3)^{k_g}\right).}
\]
A balanced frequency is an additional zero exactly when \(n=4t+1\), \(t\ge1\), and its four prefix counts have one of two forms:
\[
(k_0,k_{g_1},k_{g_2},k_{g_3})=(t,t,t,t),
\]
or \(k_0=t-1\), with the other three counts forming any permutation of \((t,t,t+1)\), where \(g_1,g_2,g_3\) are the three nonzero elements of \(G\). Thus the exact number of **additional** Fourier zeros is
\[
\boxed{E_n=\begin{cases}
\displaystyle\frac{(4t)!(4t+1)}{(t!)^4(t+1)},& n=4t+1,\ t\ge1,\\[2mm]
0,&\text{otherwise}.
\end{cases}}
\]
Consequently, if \(T_n\) denotes unnormalized convolution by \(1_{A_n}\) on functions on \(G^n\), its rank is
\[
\boxed{\operatorname{rank}T_n=4^{n-1}-E_n.}
\]
This is the complete zero-set census, not a classification of all distinct nonzero multiplier magnitudes.

## Assumptions and scope
The vertices of \(C_n\) are distinct for \(n\ge3\); the four colours are the four distinct elements of the **exponent-two** group \(G\). The pairing \(\langle u,v\rangle\) is the usual binary dot product, and all character values are real signs. The Fourier transform is unnormalized, so its values are integers. Every proper colouring is counted once. The translation \(x_i\mapsto x_i+h\) is simultaneous at all vertices and acts freely for each \(h\in G\).

## Proof
**1. Translation-forced zeros.** Simultaneously adding \(h\in G\) to all colours preserves properness. It multiplies the integrand by \((-1)^{\langle\sum_j\alpha_j,h\rangle}\). If \(\sum_j\alpha_j\ne0\), choose \(h\) with this sign negative. Pairing colourings under translation proves \(W_n(\alpha)=0\).

**2. Edge increments and an exact coefficient.** Fix a balanced frequency. Set \(\delta_j=x_{j+1}-x_j\in G\setminus\{0\}\) for \(1\le j<n\). The closing edge has \(\delta_n=\sum_{j=1}^{n-1}\delta_j\), so properness at the closing edge requires \(\sum_{j<n}\delta_j\ne0\). Every admissible increment tuple corresponds to exactly four colourings, one for each choice of \(x_1\). Since the total frequency is zero, the Walsh phase becomes \((-1)^{\sum_{j<n}\langle\beta_j,\delta_j\rangle}\).

Define \(L(u)=\sum_{d\in G\setminus\{0\}}(-1)^{\langle u,d\rangle}\). Character orthogonality gives \(L(0)=3\) and \(L(u)=-1\) for each nonzero \(u\). Removing the increment tuples whose total is zero via
\[
\mathbf1_{\sum\delta_j=0}=\frac14\sum_{h\in G}(-1)^{\langle h,\sum\delta_j\rangle}
\]
gives
\[
W_n(\alpha)=4\prod_{j<n}L(\beta_j)-\sum_{h\in G}\prod_{j<n}L(\beta_j+h).
\]
For a given \(h\), there are \(k_h\) factors equal to \(3\) and the remaining \(n-1-k_h\) factors equal to \(-1\), so the product is \((-1)^{n-1}(-3)^{k_h}\). Substitution yields the boxed multiplier formula.

**3. Exact cancellation classification.** Write \(a=k_0\) and let \(b,c,d\) be the three nonzero-element counts. The multiplier vanishes precisely when
\[
(-3)^{a+1}+(-3)^b+(-3)^c+(-3)^d=0.
\]
In any sum of four powers of \(-3\) with nonnegative exponents that is zero, let \(r\) be the smallest exponent. Divide by \((-3)^r\) and reduce modulo \(3\): the number of terms attaining the minimum is a positive multiple of three, hence exactly three. The remaining fourth term must equal \(-3\) after division; it therefore has exponent \(r+1\). In particular the four exponents are exactly \(r,r,r,r+1\). If \(a+1=r+1\), then all original prefix counts equal \(r\). If \(a+1=r\), then \(a=r-1\) and among \(b,c,d\) two are \(r\) and one is \(r+1\), with \(r\ge1\). Both cases have \(a+b+c+d=4r\), so \(n=4r+1\). Conversely each listed pattern visibly cancels. This proves the complete classification without relying on finite enumeration.

**4. Count the additional zeros and rank.** For balanced \(\alpha\), the map from the first \(n-1\) prefix frequencies \((\beta_1,\ldots,\beta_{n-1})\in G^{n-1}\) to \(\alpha\) is bijective: recover \(\alpha_1=\beta_1\), \(\alpha_j=\beta_{j-1}+\beta_j\) for \(2\le j<n\), and \(\alpha_n=\beta_{n-1}\). Thus each prefix-count composition occurs with its multinomial multiplicity. For \(n=4t+1\), the all-equal pattern contributes \((4t)!/(t!)^4\), and the exceptional pattern contributes \(3(4t)!/((t-1)!(t!)^2(t+1)!)\). Their sum simplifies to \((4t)!(4t+1)/((t!)^4(t+1))\). There are \(4^{n-1}\) balanced frequencies in total. The Fourier transform diagonalizes group convolution, and its nonzero eigenvalues are exactly the nonzero \(W_n(\alpha)\). The asserted rank follows.

## Verification
Run `python3 verify.py` with Python 3.10 or later; only the standard library is required. It constructs the proper-colouring indicator independently, computes every coefficient by an integer fast Walsh–Hadamard transform, and compares each value against the explicit prefix-count formula. Exhaustive verification covers every one of **349,504 frequency positions** for \(3\le n\le9\), including the exact ranks and additional-zero counts. Finite tests corroborate, but are not used to establish, the universal cancellation lemma.

## Relationship to prior work
The ordinary count \(\#A_n=3^n+3(-1)^n\) is classical. Babson and Beck (2012) derive group-valued graph-colouring counting expansions by Fourier analysis; their publicly visible abstract concerns aggregate colouring counts and general subgraph expansions. The full paper could not be accessed for a decisive comparison with possible character-weighted specializations, and this is a recorded historical-priority risk. The published study *Sharp universal Fourier sampling stability on proper colourings of cycles* (2026), whose theorem and proof were inspected, treats the Gram spectrum of **constant and one-coordinate Fourier characters**, not the Fourier transform at all \(4^n\) frequency vectors. Neither its restricted band nor the total chromatic count implies the stated full nullity. An earlier corresponding ternary-cycle result concerns a different colour group and has a different cancellation criterion; it does not imply the present four-colour law. The proposed contribution is specifically the complete Klein-four Fourier zero classification and exact cycle-by-cycle convolution rank.

## Limitations
No formula for the entire multiplicity distribution of **nonzero** multiplier magnitudes or their smallest magnitude at every length is claimed. The four-colour alphabet is \(\mathbb F_2^2\), not the cyclic group of order four; these yield different additive characters even though their proper-colouring sets have the same cardinality. The historical-priority check is bounded by failure to retrieve one relevant full text. Independent mathematical validation has not been carried out.

## References
1. E. Babson and M. Beck, *Counting Group Valued Graph Colorings*, arXiv:1204.1283, first publicly submitted 2012-04-05, https://arxiv.org/abs/1204.1283.
2. *Sharp universal Fourier sampling stability on proper colourings of cycles*, publicly archived 2026-11-02, published-finding corpus repository, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-universal-fourier-sampling-stability-on-proper-colourings--8dc8f90856db.
