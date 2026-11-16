# Sharp graph-Fourier sparsity of signed two-vertex signals on every path

## Finding

Let \(P_n\) be the unweighted path on vertices \(0,\ldots,n-1\), with \(n\ge2\). For \(0\le u<v<n\) and \(\varepsilon\in\{-1,+1\}\), let \(f_{u,v,\varepsilon}=\delta_u+\varepsilon\delta_v\). Define its graph-Fourier support size \(\sigma(f)\) to be the number of nonzero coefficients in an orthonormal eigenbasis of the combinatorial (not normalized) path Laplacian. The eigenvalues are simple, so this count is basis-independent.

If \(n=2^tq\) is even, with \(t\ge1\) and odd \(q\), then

\[
\min_{u<v,\,\varepsilon=\pm1}\sigma(f_{u,v,\varepsilon})=\frac{n-q+1}{2}.
\]

For \(q>1\), equality occurs precisely for the reflected *sums* \(\delta_u+\delta_{n-1-u}\) with \(0\le u<n/2\) and \(\gcd(2u+1,n)=q\), giving exactly \(2^{t-1}\) distinct normalized optimizers. For \(q=1\), **both** sums and differences on all reflected vertex pairs are optimal, giving exactly \(n\) normalized optimizers.

If \(n\ge3\) is odd, let \(p\) be its least prime divisor and \(d=n/p\). Then

\[
\min_{u<v,\,\varepsilon=\pm1}\sigma(f_{u,v,\varepsilon})=\frac{n-d}{2}.
\]

Equality occurs precisely for reflected *differences* \(\delta_u-\delta_{n-1-u}\) with \(0\le u<(n-1)/2\) and \(\gcd((n-1-2u)/2,n)=d\). There are exactly \((p-1)/2\) normalized optimizers. Signals with reversed overall sign or multiplied by a nonzero scalar do not give further Fourier support patterns.

For example, \(P_6\) has a unique optimizer \(\delta_1+\delta_4\) with two nonzero Laplacian-frequency coefficients; on \(P_9\) the unique optimizer is \(\delta_1-\delta_7\), with three coefficients. On \(P_{16}\), all sixteen reflected signed pairs are optimal, each with eight coefficients.

## Assumptions and scope

All paths are simple and have unit edge weights; the graph Laplacian is \(L=D-A\), not the adjacency operator and not the degree-normalized Laplacian. Inputs have **exactly two distinct sites** and their nonzero real amplitudes have equal modulus, with the global amplitude fixed to \(1\). The optimization ranges over every pair of distinct vertices and both relative signs, not only over symmetric inputs. Fourier support counts exact zeros, not small coefficients or energy concentration. For fixed \(n\), the real orthonormal eigenvectors are

\[
\phi_0(j)=n^{-1/2},\qquad
\phi_k(j)=\sqrt{\frac2n}\cos\!\left(\frac{\pi k(j+1/2)}{n}\right)
\quad(1\le k<n).
\]

## Proof

**1. Factoring every Fourier coefficient.** Put \(A=u+v+1\) and \(B=v-u\). Then \(1\le A<2n\), \(1\le B<n\), and \(A+B=2v+1\), so exactly one of \(A,B\) is odd and the other even. Up to a nonzero normalization factor (depending on whether \(k=0\)), cosine addition and subtraction give

\[
\begin{split}
\langle f_{u,v,+1},\phi_k\rangle&\propto
\cos\!\left(\frac{\pi Ak}{2n}\right)\cos\!\left(\frac{\pi Bk}{2n}\right),\\
\langle f_{u,v,-1},\phi_k\rangle&\propto
\sin\!\left(\frac{\pi Ak}{2n}\right)\sin\!\left(\frac{\pi Bk}{2n}\right).
\end{split}
\]

The nonzero factors include the harmless constant \(2\). Thus the exact zeros are unions of congruence sets, with \(k=0,\ldots,n-1\):

\[
Z_c^{\cos}=\{k:ck\equiv n\pmod{2n}\},\qquad
Z_c^{\sin}=\{k:ck\equiv0\pmod{2n}\}.
\]

**2. Elementary zero-count lemma.** If \(c\) is odd, \(g=\gcd(c,n)\) is odd. Among \(0\le k<n\), the cosine congruence has precisely \((g-1)/2\) solutions, all \(k=(n/g)(2r+1)\), and the sine congruence has \((g+1)/2\) solutions, precisely the multiples of \(2n/g\). For arbitrary \(c\), put \(h=\gcd(c,n)\). The cosine congruence is empty when \(c/h\) is even; otherwise it has \(\lfloor h/2\rfloor\) solutions, namely odd multiples of \(n/h\). For even \(c\), put \(H=\gcd(c,2n)\), which is even; the sine congruence has \(H/2\) solutions, the multiples of \(2n/H\) in the indicated range. These descriptions follow by dividing each linear congruence by its greatest common divisor and retaining the representatives in the half-residue interval \(0\le k<n\). Every sine set includes \(k=0\).

**3. Even length.** Write \(n=2^tq\) with \(q\) odd. Denote the odd one of \(A,B\) by \(c_o\), the even one by \(c_e\). Since \(\gcd(c_o,n)\le q\), the odd cosine factor has at most \((q-1)/2\) roots and the odd sine factor at most \((q+1)/2\). The even cosine factor has at most \(n/2\) roots, with equality only if \(c_e=n\); its roots then are precisely the odd \(k\). The even sine factor has at most \(n/2\) roots, likewise with equality only if \(c_e=n\), when its roots are precisely the even \(k\).

It follows that a *sum* has at most \((n+q-1)/2\) zero coefficients. Equality forces \(c_e=n\); because \(B<n\), necessarily \(A=n\), i.e. \(v=n-1-u\). Its other factor is \(B\) odd. The zeros of this odd cosine factor are even \(k\), so disjoint from the odd zeros of the first factor, and equality is equivalent to \(\gcd(B,n)=q\).

For a *difference*, the two sine-zero sets meet at \(k=0\). If \(c_e\ne n\), the even-factor zero count is at most \(n/2-1\), so the union has at most \((n+q-3)/2\) roots. If \(c_e=n\), again \(A=n\), the even-factor sine zeros are all even indices and the odd-factor sine zeros are an even-index subset (since \(2n/\gcd(B,n)\) is even), giving exactly \(n/2\) roots. Consequently no difference attains the sum optimum when \(q>1\), while all reflected differences tie when \(q=1\). Counting reflected pairs with odd separation \(B=q r\), \(1\le r<2^t\) odd, gives \(2^{t-1}\) pairs for \(q>1\); when \(q=1\), all \(n/2\) reflected pairs admit both signs.

**4. Odd length.** Let \(p\) be the least prime factor of \(n\) and \(d=n/p\), the largest proper divisor of \(n\). Since \(c_e\) is even and \(n\) odd, \(c_e/\gcd(c_e,n)\) is even; hence the even cosine factor has **no roots**. The odd cosine factor has at most \((n-1)/2\) roots; no sum can attain the proposed \((n+d)/2\) zero count.

For a difference, write \(H=\gcd(c_e/2,n)\). As \(0<c_e<2n\), one has \(H<n\), hence \(H\le d\), and the even sine factor has exactly \(H\) roots. If \(c_o\ne n\), then \(\gcd(c_o,n)\le d\), so the odd sine factor has at most \((d+1)/2\) roots. Their intersection contains zero, giving a union of at most \((3d-1)/2<(n+d)/2\), because \(n\ge3d\).

Therefore equality forces \(c_o=n\), hence \(A=n\) and \(v=n-1-u\). Now \(B\) is even. Let \(H=\gcd(B/2,n)\). The sine zeros of \(A=n\) are all even \(k\), of which there are \((n+1)/2\); the sine zeros of \(B\) are exactly the \(H\) multiples of the odd number \(n/H\), including \((H+1)/2\) even values. Their union has exactly \((n+H)/2\) elements, so the Fourier support is \((n-H)/2\). The least support occurs precisely at \(H=d\). As \(B/2=(n-1)/2-u\) runs once through \(1,\ldots,(n-1)/2\), the values satisfying \(\gcd(B/2,n)=d\) are \(d,2d,\ldots,((p-1)/2)d\), giving exactly \((p-1)/2\) optimizers. This proves all assertions for every \(n\ge2\).

## Verification

The deductive proof above establishes every dimension without relying on a finite experiment. The included standalone `check_exact.py` performs integer-only enumeration for every \(2\le n\le80\), all \(170{,}640\) unordered-location/sign combinations, independently checking the sharp minimum, every optimizer, and the number of optimizers. The second checker, `check_dct.py`, evaluates the original cosine eigenvectors at 90-decimal-digit precision for \(2\le n\le22\), covering \(3{,}542\) cases, and independently matches every Fourier zero against the congruence formula. Run using `python check_exact.py` and, with the standard `mpmath` package installed, `python check_dct.py`. Neither finite check substitutes for the universal proof.

## Relationship to prior work

Rebrova and Salanevich, *On Graph Uncertainty Principle and Eigenvector Delocalization* (first public June 27, 2023), motivate sharp vertex-versus-spectrum support questions in graph Fourier analysis and establish general uncertainty results, not this equal-amplitude path two-site minimum. Parlangeli and Notarstefano, *On the Reachability and Observability of Path and Cycle Graphs* (first public September 16, 2011), give an important arithmetic classification of reachable/observable node sets; their multi-input result treats independent inputs at the chosen nodes and does not directly assert the rank/support of one *signed combined input* or optimize it across all locations and signs. The present complete minimum and equality classification concerns that different fixed-weight one-vector question. Standard cosine eigenvectors and elementary congruence facts are not claimed as original.

## Limitations

The theorem is restricted to the combinatorial Laplacian of an unweighted path and to two equal-modulus **real** amplitudes. It does not address arbitrary complex relative phases, unequal magnitudes, weighted paths, multiple independent sensors, normalized-Laplacian eigenvectors, noise stability, or graph families beyond paths. Historical priority is assessed against identified sources but unindexed work on simultaneous two-node actuation or discrete cosine sparsity may exist; independent mathematical review has not been performed.

## References

1. E. Rebrova and P. Salanevich, *On Graph Uncertainty Principle and Eigenvector Delocalization*, arXiv:2306.15810, first submitted June 27, 2023. https://arxiv.org/abs/2306.15810
2. G. Parlangeli and G. Notarstefano, *On the Reachability and Observability of Path and Cycle Graphs*, arXiv:1109.3556, first submitted September 16, 2011. https://arxiv.org/abs/1109.3556
3. G. Strang, *The Discrete Cosine Transform*, SIAM Review 41 (1999), 135–147. https://doi.org/10.1137/S0036144598336745
