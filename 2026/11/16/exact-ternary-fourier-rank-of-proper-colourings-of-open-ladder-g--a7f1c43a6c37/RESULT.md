# Exact ternary Fourier rank of proper colourings of open ladder graphs

## Finding
Let \(L_n=P_n\square K_2\) be the open ladder with \(n\ge 2\) rungs. Give its \(2n\) labelled vertices colours in \(\mathbb F_3\). Write \(f_n\) for the indicator of proper three-colourings on the additive group \(G_n=\mathbb F_3^{2n}\), and define the **unnormalized** Fourier transform by
\[
\widehat f_n(\xi)=\sum_{x\in G_n}f_n(x)\exp\!\left(\frac{2\pi i}{3}\langle\xi,x\rangle\right).
\]
The convolution operator \(h\mapsto f_n*h\) on \(\mathbb C^{G_n}\) has exactly
\[
\boxed{\operatorname{rank}(f_n*)=\frac{3\cdot 9^n-24n+45}{16}}.
\]
The complete zero set is characterized by the first and last nonzero cumulative rung frequencies as described below. Exactly \(3^{2n-1}\) frequencies satisfy the necessary total-frequency balance; among these, precisely
\[
\boxed{\frac{7\cdot9^n+72n-135}{48}}
\]
are additional zeros. In particular, the proportion of balanced frequencies which survive tends to \(9/16\), while the rank divided by \(|G_n|\) tends to \(3/16\). This is a nontrivial persistent loss of Fourier information, not merely the kernel forced by global colour translation.

## Assumptions and scope
Vertices are \((i,0),(i,1)\), \(1\le i\le n\); edges join each rung pair and consecutive vertices within each row. There are no longitudinal wraparound edges. We identify the colours with \(\mathbb F_3\), and use the coordinatewise additive Fourier transform (not a transform under permutations of the three colour names). All counts refer to individual labelled frequencies; the multiplier at each frequency is \(\widehat f_n(\xi)\).

Write the frequency at rung \(i\) as \((\alpha_i,\beta_i)\). Put \(\gamma_i=\alpha_i+\beta_i\) and \(\delta_i=\beta_i\). If \(\sum_i\gamma_i\ne0\) in \(\mathbb F_3\), then \(\widehat f_n(\xi)=0\) by translation symmetry. For a balanced frequency define \(s_j=\sum_{i=j+1}^n\gamma_i\) for \(1\le j<n\). The coordinates \((s_1,\ldots,s_{n-1},\delta_1,\ldots,\delta_n)\) range independently over \(\mathbb F_3^{2n-1}\) as balanced frequencies vary.

Here is an explicit **if-and-only-if** test for a balanced frequency. If every \(s_j=0\), its Fourier coefficient vanishes exactly when, for some \(1\le j<n\), the \(\delta\)-word has all zeros except for \(\delta_j=\delta_{j+1}\in\{1,2\}\). Otherwise let \(a\) and \(b\) be the first and last indices with \(s_j\ne0\). Its coefficient vanishes exactly when at least one of these two independent endpoint conditions holds:
\[
\begin{array}{ll}
\text{left:} & \delta_1=\cdots=\delta_{a-1}=0,\quad \delta_a=s_a,\\
\text{right:} & \delta_{b+1}=-s_b,\quad\delta_{b+2}=\cdots=\delta_n=0.
\end{array}
\]
All displayed identities are in \(\mathbb F_3\). There is no additional interior cancellation.

## Proof
Let \(\omega=\exp(2\pi i/3)\), and write the colours of rung \(i\) as \((a_i,b_i)=(a_i,a_i+d_i)\), where \(d_i\in\{1,-1\}\subset\mathbb F_3\). Set \(u_i=a_{i+1}-a_i\). Proper horizontal edges require \(u_i\ne0\) and \(u_i+d_{i+1}-d_i\ne0\). For a balanced frequency, summing over the freely translated starting colour gives a factor three; the remaining character phase is \(\omega^{\sum_j s_ju_j+\sum_i\delta_id_i}\). Consequently
\[
\frac{\widehat f_n(\xi)}3=\boldsymbol1^{\mathsf T}D_{\delta_1}T_{s_1}D_{\delta_2}\cdots T_{s_{n-1}}D_{\delta_n}\boldsymbol1,
\]
where \(\boldsymbol1=(1,1)^{\mathsf T}\), \(D_d=\operatorname{diag}(\omega^d,\omega^{-d})\), and direct enumeration of the three possible transitions between proper rungs gives
\[
T_0=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
T_s=\begin{pmatrix}-1&\omega^s\\\omega^{-s}&-1\end{pmatrix}
=-\begin{pmatrix}1\\-\omega^{-s}\end{pmatrix}
\begin{pmatrix}1&-\omega^s\end{pmatrix}\quad(s\in\{1,2\}).
\]
This is an exact identity in the Eisenstein integers \(\mathbb Z[\omega]\), not an approximation by complex floating point arithmetic.

**Endpoint lemma.** For a row vector \((A,B)=\boldsymbol1^{\mathsf T}D_{d_1}T_0D_{d_2}\cdots T_0D_{d_k}\), the ratio \(A/B\) is a cube root of unity if and only if \(d_1=\cdots=d_{k-1}=0\). In that case \(A/B=\omega^{-d_k}\). Moreover \(A+B=0\) holds for exactly \(2(k-1)\) strings of \(k\) digits: the strings whose only nonzero digits form a consecutive equal-sign pair.

To prove the lemma, let \(P=A+B\), \(Q=A-B\), and \(t=Q/P\), allowing \(t=\infty\) when \(P=0\). Work at the prime \(\lambda=1-\omega\) of \(\mathbb Z[\omega]\), with \(v_\lambda(3)=2\). Multiplication by \(T_0\) changes \((P,Q)\) into \((3P,Q)\), hence divides \(t\) by three. Multiplication by \(D_d\) changes \((P,Q)\) into \((c_dP+e_dQ,e_dP+c_dQ)\), with \(c_d=(\omega^d+\omega^{-d})/2\), \(e_d=(\omega^d-\omega^{-d})/2\). If \(d\ne0\), then \(v_\lambda(c_d)=0\) and \(v_\lambda(e_d)=1\). Thus, if \(v_\lambda(t)<0\), the new ratio \((e_d+c_dt)/(c_d+e_dt)\) also has negative valuation; for \(d=0\) it is unchanged. A first nonzero \(d_j\) gives \(v_\lambda(t)=1\), and a following \(T_0\) changes this to \(-1\), which cannot return to a positive valuation. But a cube-root ratio \(A/B\in\{1,\omega,\omega^2\}\) has \(v_\lambda((A-B)/(A+B))\ge1\) (including infinity). This proves the first assertion, since with earlier digits zero one has \((A,B)=3^{k-1}(\omega^{d_k},\omega^{-d_k})\).

For the second assertion, the first nonzero digit \(d_j\) gives \(v_\lambda(t)=-1\) immediately after the next \(T_0\). The only way the next \(D\) can make \(P=0\) is \(d_{j+1}=d_j\); the resulting ratio \(A/B=-1\) stays there under later \(T_0\)'s if all subsequent digits are zero. If this immediate cancellation does not occur, the next \(T_0\) makes \(v_\lambda(t)\le-3\); subsequent steps never allow \(P=0\). If it does occur, any later nonzero digit destroys \(P=0\) irreversibly. Therefore the stated equal-sign adjacent pairs are exactly the solutions, giving \(2(k-1)\).

**No interior zeros.** Each nonzero \(s\) makes \(T_s\) rank one. The scalar connecting two such rank-one factors, separated by any number of \(T_0\)'s and any intervening \(D\)'s, is nonzero: modulo \(\lambda\), all \(D\)'s become the identity, every \((1,-\omega^s)\) becomes \((1,-1)\), and \(T_0(1,-1)^{\mathsf T}=(1,-1)^{\mathsf T}\). The connecting scalar is consequently congruent to \(2\not\equiv0\pmod\lambda\). Thus the two boundary factors alone govern vanishing.

If no \(s\) is nonzero, the endpoint lemma gives precisely \(2(n-1)\) zeros among \(3^n\) \(\delta\)-vectors. Otherwise take the first and last nonzero indices \(a\le b\). The endpoint lemma, applied from either end, gives the two conditions stated in the scope section. They constrain disjoint sets of \(a\) and \(n-b\) digits, respectively; the number of \(\delta\)-vectors avoiding both is
\[
3^n-3^{n-a}-3^b+3^{b-a}.
\]
If \(a=b\), there are two choices of \(s\); if \(a<b\), there are \(4\cdot3^{b-a-1}\) choices (including arbitrary intermediate digits). Therefore the exact rank is
\[
R_n=3^n-2(n-1)+\sum_{a=1}^{n-1}2(3^n-3^{n-a}-3^a+1)
+\sum_{1\le a<b\le n-1}4\cdot3^{b-a-1}(3^n-3^{n-a}-3^b+3^{b-a}).
\]
Evaluating the two finite geometric sums gives \(R_n=(3\cdot9^n-24n+45)/16\). Subtracting from the balanced frequency count \(3^{2n-1}\) proves the additional-nullity formula. Fourier diagonalization of convolution proves the operator-rank statement. The limiting proportions follow immediately.

## Verification
The accompanying standalone `verify_fft.py` independently enumerates anchored proper colourings and performs an **exact Eisenstein-integer ternary Fourier transform** on their indicator for \(1\le n\le7\), checking all balanced frequencies, their nonzero counts and the closed rank formula. The separately implemented `verify_direct.py` enumerates the same finite state spaces in a different order and counts exponents modulo three by direct dot products, without a Fourier butterfly or transfer-matrix multiplication. It independently checks all balanced frequencies for \(1\le n\le5\). Both scripts passed locally using Python 3 and NumPy. Finite checks corroborate but do not replace the all-length proof above.

| Rungs \(n\) | Proper three-colourings | Balanced frequencies | Nonzero multipliers | Extra balanced zeros |
|---:|---:|---:|---:|---:|
| 2 | 18 | 27 | 15 | 12 |
| 3 | 54 | 243 | 135 | 108 |
| 4 | 162 | 2,187 | 1,227 | 960 |
| 5 | 486 | 19,683 | 11,067 | 8,616 |
| 6 | 1,458 | 177,147 | 99,639 | 77,508 |
| 7 | 4,374 | 1,594,323 | 896,799 | 697,524 |

## Relationship to prior work
Shrock's archived 2000 treatment of square-lattice ladders provides the exact zero-field Potts partition function and the chromatic count \(q(q-1)(q^2-3q+3)^{n-1}\) for the open ladder. At \(q=3\), this is \(6\cdot3^{n-1}\) and is consistent with our elementary transition count, but does not give the additive-character zero support or convolution rank. Ellis-Monaghan and Moffatt (2010) supply a general vertex-dependent external-field Potts framework, which can specialize to character-weighted counting and thus formally encompasses individual Fourier coefficient evaluations; the exact simultaneous-zero classification and closed rank across the whole frequency space are additional statements not supplied by their general polynomial representation. Related harmonic sampling results on cycles, bicliques, and trees concern other graphs or restricted Fourier bands and do not imply the complete open-ladder rank classification.

## Limitations
The theorem concerns only the open ladder and the additive group of three colours. It does not give the full nonzero magnitude multiset, sharp inverse norm, cyclic-ladder Fourier rank, or higher-palette formula. General weighted-Potts expansions could yield an alternative derivation; the accessible comparisons do not establish historical uniqueness. No independent mathematical audit has been performed.

## References
1. R. Shrock, *Exact Potts Model Partition Functions on Ladder Graphs*, arXiv:cond-mat/0001389, first posted 2000-01-26, especially section V, equations (83)–(87). https://arxiv.org/abs/cond-mat/0001389
2. J. A. Ellis-Monaghan and I. Moffatt, *The Tutte-Potts connection in the presence of an external magnetic field*, arXiv:1005.5470, first posted 2010-05-29, especially theorem 4.2 and corollary 4.3. https://arxiv.org/abs/1005.5470
