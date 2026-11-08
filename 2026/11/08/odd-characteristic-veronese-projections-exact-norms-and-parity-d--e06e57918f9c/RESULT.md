# Odd-characteristic Veronese projections: exact norms and parity-dependent finite-size bias

## Finding

Fix an odd prime power \(q\) and \(m\ge1\). Put \(V_m=\operatorname{Sym}_m(\mathbb F_q)\), let \(\psi\) be any nontrivial additive character, and set
\[
C_m=\{vv^{\mathsf T}:v\in\mathbb F_q^m\},\qquad
N=q^{m(m+1)/2}.
\]
Let \(P_m\) denote the convolution Fourier projection with multiplier \(1_{C_m}\), where the duality is \((A,B)\mapsto\psi(\operatorname{tr}(AB))\). Define
\[
L_m(q)=\|P_m\|_{\ell^1\to\ell^1}
       =\|P_m\|_{\ell^\infty\to\ell^\infty}.
\]
For \(0\le r\le m\), let \(N_{m,r}\) count rank-\(r\) symmetric matrices. The explicit integer formulas are
\[
N_{m,2h}=\left(\prod_{i=1}^h\frac{q^{2i}}{q^{2i}-1}\right)
 \prod_{i=0}^{2h-1}(q^{m-i}-1),
\quad
N_{m,2h+1}=\left(\prod_{i=1}^h\frac{q^{2i}}{q^{2i}-1}\right)
 \prod_{i=0}^{2h}(q^{m-i}-1).
\]
Empty products equal one. Put \(T_{m,r}=q^{m-r/2}\) and
\[
F_q(T)=\begin{cases}T,&q\equiv1\pmod4,\\
\sqrt{1+T^2},&q\equiv3\pmod4.
\end{cases}
\]
**Exact endpoint formula (all odd prime powers, all dimensions):**
\[
\boxed{L_m(q)=\frac1{2N}\left[
\sum_{\substack{0\le r\le m\\r\,\mathrm{even}}}
 N_{m,r}\bigl(T_{m,r}+q^{-r/2}\bigr)
+\sum_{\substack{0\le r\le m\\r\,\mathrm{odd}}}
 N_{m,r}F_q(T_{m,r})\right].}
\]

For the two-term large-dimension law, define
\[
Q=q^{-1},\quad t=\sqrt q,\quad
D_k=\prod_{i=1}^k(1-Q^i),\quad
c_q=\prod_{j=1}^{\infty}(1-Q^{2j-1}),\quad
p_k=c_q\frac{Q^{k(k+1)/2}}{D_k}.
\]
The numbers \(p_k\) form a probability distribution. Define
\[
S_q=\sum_{k\ge0}p_kt^k
=c_q\sum_{k\ge0}\frac{q^{-k^2/2}}{D_k},\qquad
A_\epsilon=\sum_{k\equiv\epsilon\ (2)}p_kt^k,\quad
B_\epsilon=\sum_{k\not\equiv\epsilon\ (2)}p_kt^k,
\]
\[
J_\epsilon=\sum_{k\not\equiv\epsilon\ (2)}p_kt^{-k},\qquad
d_q=\frac{q}{(\sqrt q+1)(q+1)}.
\]
For \(\epsilon\in\{0,1\}\), set
\[
\boxed{C_{q,\epsilon}=(1-d_q)A_\epsilon-d_qq^{-1}B_\epsilon
+\frac{\mathbf1_{q\equiv3\ (4)}}2J_\epsilon.}
\]
Then \(C_{q,0}>0\) and \(C_{q,1}>0\), and for fixed \(q\), as \(m\to\infty\),
\[
\boxed{H_m(q):=2q^{-m/2}L_m(q)
=S_q+C_{q,m\bmod2}q^{-m}+O_q(q^{-2m}).}
\]
In particular \(H_m(q)\to S_q\) from above for all sufficiently large \(m\), and the sharp endpoint norm satisfies
\[
L_m(q)=\frac{S_q}{2}q^{m/2}
+\frac{C_{q,m\bmod2}}{2}q^{-m/2}+O_q(q^{-3m/2}).
\]
The coefficients need not have the same order across the two congruence classes of \(q\); no all-dimension monotonicity is asserted. For instance, the computed \((S_q,C_{q,0},C_{q,1})\) are approximately \((1.320367825823,0.591643933656,0.663975555193)\) for \(q=3\) and \((1.278890815298,0.596842254861,0.286849564560)\) for \(q=5\).

## Assumptions and scope

All matrices and vectors are over \(\mathbb F_q\), with \(q\) odd, and all function spaces use counting measure. The additive duality through matrix trace is nondegenerate because the off-diagonal coordinates contribute a factor of two, which is invertible in odd characteristic. A Fourier multiplier of a subset acts by convolution with \(K(A)=N^{-1}\sum_{B\in C_m}\psi(\operatorname{tr}(AB))\); its exact \(\ell^1\) and \(\ell^\infty\) norm is \(\sum_{A\in V_m}|K(A)|\). The matrix cone includes zero. Its size is \((q^m+1)/2\), because \(vv^{\mathsf T}=ww^{\mathsf T}\ne0\) forces \(w=\pm v\).

## Proof

**Step 1: Fourier kernel and Gaussian phases.** Let \(G(A)=\sum_{v\in\mathbb F_q^m}\psi(v^{\mathsf T}Av)\). Counting the two preimages of each nonzero cone point and the single preimage of zero gives
\[
\sum_{B\in C_m}\psi(\operatorname{tr}(AB))=\frac{1+G(A)}2.
\]
If \(A\) has rank \(r\), diagonalization of its nondegenerate part gives
\[
G(A)=q^{m-r}\gamma_q^r\eta(\det A_{\mathrm{nd}}),\qquad
|G(A)|=T_{m,r},\quad\gamma_q^2=\eta(-1)q.
\]
Here \(\eta\) is the quadratic character, \(\gamma_q=\sum_{x\in\mathbb F_q}\psi(x^2)\), and the determinant is taken on any nonsingular complement of the radical; only the resulting quadratic-form type matters. The phase is real in even rank; in odd rank it is real for \(q\equiv1\pmod4\) and imaginary for \(q\equiv3\pmod4\). Every \(T_{m,r}\ge1\).

**Step 2: discriminant imbalance.** In odd rank, the two discriminant types have equal size. For rank \(r=2h>0\), the two type counts have difference
\[
\sum_{\operatorname{rank}A=2h}\eta(\det A_{\mathrm{nd}})
=\eta((-1)^h)q^{-h}N_{m,2h}.
\]
One direct derivation is to count nondegenerate symmetric forms as \(\operatorname{GL}_{2h}(\mathbb F_q)\)-orbits. The split/nonsplit stabilizers have orders
\[
2q^{h(h-1)}(q^h\mp1)\prod_{i=1}^{h-1}(q^{2i}-1),
\]
so their size difference divided by their size sum is \(q^{-h}\), and the split determinant class has character \(\eta((-1)^h)\). Adjoining radicals multiplies both counts equally. In even rank the Gaussian phase is \(\eta(-1)^h\eta(\det A_{\rm nd})\), hence the *weighted sign imbalance is always* \(q^{-h}N_{m,2h}\), irrespective of \(q\bmod4\). Since \(|1\pm T|=T\pm1\) for \(T\ge1\), averaging \(|1+G(A)|\) over rank-\(2h\) matrices gives \(N_{m,2h}(T_{m,2h}+q^{-h})\). In odd rank the two phases cancel in the real case, giving \(N_{m,r}T_{m,r}\), and have common magnitude \(\sqrt{1+T_{m,r}^2}\) in the imaginary case. The zero-rank term is \(q^m+1\). Division by \(2N\) proves the exact norm formula.

**Step 3: nullity distribution and limiting constant.** Let \(K_m\) be the nullity of a uniform symmetric matrix. Write \(P_m(k)=\Pr(K_m=k)=N_{m,m-k}/N\). The displayed rank formulas can be rearranged exactly as
\[
P_m(k)=\frac{Q^{k(k+1)/2}}{D_k}
\left(\prod_{i=m-k+1}^{m}(1-Q^i)\right)
\left(\prod_{j=1}^{\lceil(m-k)/2\rceil}(1-Q^{2j-1})\right).
\]
For fixed \(k\), this tends to \(p_k\). The same exact formula supplies a uniform \(O_q(Q^{k(k+1)/2})\) majorant, so all the moments used below converge absolutely. Normalization of \(p_k\) follows either by passage to the limit or the symmetric-rank probability formula.

For \(r=m-k\), direct normalization of the exact norm gives
\[
H_m=\sum_{k=0}^{m}P_m(k)t^k
\left[1+Q^m\mathbf1_{r\,\mathrm{even}}+
\mathbf1_{q\equiv3\ (4)}\mathbf1_{r\,\mathrm{odd}}
\left(\sqrt{1+Q^{m+k}}-1\right)\right].
\]
(The last term is interpreted inside the square bracket; multiplying by \(t^k\) is essential.) Thus the leading term is \(S_q\).

**Step 4: parity coefficient and remainder.** Fix \(\epsilon=m\bmod2\). For \(k\le m/2\), expand the two finite products relative to their infinite limits. Uniformly in such \(k\),
\[
\frac{P_m(k)}{p_k}=1+Q^{m-k+1}
\left(\frac{\mathbf1_{m-k\,\mathrm{even}}+Q\mathbf1_{m-k\,\mathrm{odd}}}{1-Q^2}
-\frac{1-Q^k}{1-Q}\right)
+O_q(Q^{2(m-k+1)}).
\]
This uses the full geometric tail of omitted odd Euler factors, not only its first term. Terms with \(k>m/2\) are smaller than every fixed exponential rate after weighting by any fixed power of \(q^k\), since \(p_k=O_q(Q^{k(k+1)/2})\). Summing gives a remainder \(O_q(Q^{2m})\). The imaginary odd-rank correction has the uniform expansion \(\sqrt{1+Q^{m+k}}-1=\tfrac12Q^{m+k}+O(Q^{2m+2k})\).

Write \(A_\epsilon\), \(B_\epsilon\), \(J_\epsilon\) as in the statement. The limiting probability ratio \(p_{k-1}=p_k(q^k-1)\), for \(k\ge1\), yields
\[
\sum_{k\ge0}p_kq^kt^k=(1+t)S_q,
\quad
\sum_{k\equiv\epsilon\ (2)}p_kq^kt^k=A_\epsilon+tB_\epsilon.
\]
Substituting into the first-order coefficient of the preceding expansion reduces its contribution from \(P_m-p\) to \(-d_q(A_\epsilon+Q B_\epsilon)\). The even-rank sign imbalance contributes \(A_\epsilon\), and the odd-rank imaginary correction contributes \(J_\epsilon/2\) when \(q\equiv3\pmod4\). This is exactly the displayed \(C_{q,\epsilon}\).

**Step 5: strict positivity.** The elementary bound \(0<d_q<1/3\) holds for every odd \(q\ge3\). Put \(E=A_0\), \(O=A_1\). From \(p_{k+1}/p_k=(q^{k+1}-1)^{-1}\), pairing even and odd indices gives
\[
O\le\frac{\sqrt q}{q-1}E,\qquad
E\le\left(\frac{q-1}{\sqrt q}+\frac{\sqrt q}{q^2-1}\right)O.
\]
For \(\epsilon=0\), the non-imaginary portion of \(C_{q,0}\) is at least \(E[1-d_q(1+q^{-1/2}/(q-1))]>0\). For \(\epsilon=1\), it is at least
\[
O\left[1-d_q\left(1+\frac{q-1}{q^{3/2}}+
\frac1{\sqrt q(q^2-1)}\right)\right]>0.
\]
Both brackets are positive already using \(q\ge3\) and \(d_q<1/3\). The remaining imaginary-sector term is nonnegative. This proves both strict inequalities and completes the asymptotic theorem.

## Verification

The standalone file `check_veronese.py` independently enumerates the cone, all additive characters and symmetric-matrix ranks over the prime fields \(q=3,5,7,11\) in the stated small dimensions. It compares complete root-of-unity transforms and exact orbit counts with the formula. The program additionally tests the parity asymptotics for \(q=3,5,7,9,11,13,19\), with \(q=9\) evaluated by the universal prime-power rank formula rather than full field-element enumeration. A successful run prints `ODD_VERONESE_ENDPOINT_AND_PARITY_CHECKS_PASS`.

The proofs above are valid for all odd prime powers and all \(m\ge1\); numerical tests are not used to infer infinite-dimension limits.

## Relationship to prior work

Quadratic Gauss sums and their basic magnitude are classical; Iosevich and Koh (2008) use related sums for finite-field restriction/extension estimates. Fulman and Goldstein (2012 preprint, 2015 journal) give the exact nullity distribution and limit for uniform symmetric matrices, which is explicitly used here. Green and Sanders (2006) provide the harmonic-analysis idempotent perspective, not this arithmetic endpoint norm. Classical symmetric-matrix exponential-sum work by Hodges (1955) is particularly relevant; its complete original text was not accessible for comparison. Previously described spectral results for coordinate-restricted Veronese frames have different operators and do not by their stated claims determine a full-cone multiplier's absolute kernel norm. The new contribution is the exact endpoint norm assembled with type signs, plus its positive two-parity finite-size correction. These classical ingredients should not be read as new.

## Limitations

This theorem concerns the *full homogeneous rank-one cone* in odd characteristic, not an affine slice, not characteristic two, and not general rank-\(r\) determinantal cones. The parity expansion is for fixed \(q\) as \(m\to\infty\), with an implicit constant depending on \(q\). It does not assert strict monotonicity at every finite dimension. Independent mathematical validation and exhaustive historical priority are not established. The unavailable full text of the 1955 symmetric-matrix exponential-sum article leaves a residual priority risk.

## References

- B. Green and T. Sanders, *A quantitative version of the idempotent theorem in harmonic analysis*, arXiv:math/0611286v1, publicly posted 2006-11-09.
- A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, publicly posted 2008-04-28, particularly Section 2.
- J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504v1, publicly posted 2012-11-02; Section 4 (exact symmetric-matrix nullities and limit). *Ann. Probab.* 43 (2015), 1274–1314.
- J. H. Hodges, *Exponential Sums for Symmetric Matrices in a Finite Field*, *Math. Nachr.* 14 (1955), 331–339, DOI:10.1002/mana.19550140411 (potentially relevant full text inaccessible).
