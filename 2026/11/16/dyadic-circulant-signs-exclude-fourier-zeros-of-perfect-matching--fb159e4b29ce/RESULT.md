# Dyadic circulant signs exclude Fourier zeros of perfect matchings

## Finding

For each integer \(k\ge1\), let \(n=2^k\). Every real circulant sign matrix
\[
 C_s=(s_{(j-i)\bmod n})_{0\le i,j<n},\qquad s_r\in\{+1,-1\},
\]
satisfies
\[
 \boxed{\operatorname{per}(C_s)\equiv n!\pmod{2^n}},
 \qquad
 \boxed{\nu_2(\operatorname{per}(C_s))=n-1}.
\]
In particular, its permanent is nonzero with absolute value at least \(2^{n-1}\), uniformly over all \(2^n\) sign patterns. The statement is a congruence for every signed circulant of the given order, not a probabilistic assertion.

Define a displacement-parity vector for a perfect matching \(\pi\in S_n\) by
\[
 d_r(\pi)=\#\{i\in\mathbb Z/n\mathbb Z:\ \pi(i)-i\equiv r\pmod n\}\pmod2
 \quad(r\in\mathbb Z/n\mathbb Z).
\]
Define \(f_n(v)=\#\{\pi\in S_n:d(\pi)=v\}\) on the additive binary group \(\mathbb F_2^n\). Its unnormalized Walsh transform has no zero:
\[
 \widehat f_n(a)=\sum_{v\in\mathbb F_2^n}f_n(v)(-1)^{a\cdot v}
 =\operatorname{per}(C_{((-1)^{a_r})_{r=0}^{n-1}})\ne0.
\]
Thus convolution \(T_n:g\mapsto f_n*g\) on \(\ell^2(\mathbb F_2^n)\) is invertible and
\[
 \|T_n^{-1}\|_{2\to2}\le2^{1-n}.
\]
This inequality is an upper bound, not a claimed equality.

The symmetry restriction changes invertibility decisively. Without the displacement reduction, the full Walsh transform of the indicator of perfect matchings on \(K_{n,n}\) vanishes whenever \(n\ge2\) is even: choose \(n/2\) negative and \(n/2\) positive edges in one row, with all other edges positive.

## Assumptions and scope

All indexing is modulo \(n\), with \(n=2^k\) for an integer \(k\ge1\). The permanent of a matrix \(A\) is \(\operatorname{per}(A)=\sum_{\pi\in S_n}\prod_{i=0}^{n-1}A_{i,\pi(i)}\). The \(2\)-adic valuation \(\nu_2(m)\) of a nonzero integer is the largest exponent \(e\) for which \(2^e\mid m\). No assertion is made for arbitrary non-dyadic orders. The Fourier normalization is unnormalized; inverses use this exact convention.

## Proof

Let \(J\) denote the all-ones matrix, and let \(B\) be the zero-one circulant whose \((i,j)\) entry is one precisely when \(s_{j-i}=-1\). Then \(C_s=J-2B\). Write \(m_j(B)\) for the number of ways of selecting \(j\) nonzero entries of \(B\), with at most one selected entry in each row and each column, and \(m_0(B)=1\). Expanding the permanent by which negative positions were selected gives the exact rook expansion
\[
 \operatorname{per}(J-2B)
 =\sum_{j=0}^n(-2)^j(n-j)!\,m_j(B).\tag{1}
\]
Indeed a fixed nonattacking set of \(j\) selected negative positions lies in precisely \((n-j)!\) permutations.

**Cyclic-orbit divisibility.** Simultaneously translate every row and column index by one. This cyclic group of order \(n=2^k\) acts on the size-\(j\) rook placements of \(B\). For any such placement with \(1\le j<n\), its stabilizer is a subgroup of order \(h\), a power of two. Each individual board cell has a free orbit under the stabilizer, because a nontrivial common index translation fixes no cell. Therefore its size \(j\) is a union of size-\(h\) edge-orbits; consequently \(h\mid j\), hence \(h\le 2^{\nu_2(j)}\). Every orbit of placements has size at least \(2^{k-\nu_2(j)}\) and is a power of two. Thus
\[
 2^{k-\nu_2(j)}\mid m_j(B) \qquad(1\le j<n).\tag{2}
\]
When no placements exist, the corresponding summand in (1) is zero; otherwise the following valuation calculation applies.

**Valuations of the remaining summands.** For any nonnegative integer \(t\), Legendre's formula reads \(\nu_2(t!)=t-s_2(t)\), where \(s_2(t)\) counts the ones in the binary expansion. Fix \(1\le j<n\) and put \(u=\nu_2(j)\). Then \(n-j\) is a positive multiple of \(2^u\) smaller than \(2^k\), so \(s_2(n-j)\le k-u\). Combining this with (2),
\[
 \begin{aligned}
 \nu_2\bigl(2^j(n-j)!m_j(B)\bigr)
 &\ge j+(n-j)-s_2(n-j)+k-u\\
 &\ge n.
 \end{aligned}
\]
The final summand \(j=n\) in (1) has a factor \(2^n\) as well. Consequently, all nonconstant terms in (1) vanish modulo \(2^n\), leaving
\[
 \operatorname{per}(C_s)\equiv n!\pmod{2^n}.
\]
Since \(n=2^k\), Legendre's formula gives \(\nu_2(n!)=n-s_2(n)=n-1\). Hence every possible permanent is an odd multiple of \(2^{n-1}\), proving the nonvanishing and magnitude bound.

**Fourier consequences.** In each product \(\prod_i(-1)^{a_{\pi(i)-i}}\), the exponent modulo two is \(a\cdot d(\pi)\), giving the Walsh/permanent identity above. Fourier diagonalization of convolution on the finite abelian group gives eigenvalues \(\widehat f_n(a)\), and hence the asserted inverse norm bound. For the unrestricted full edge-character group, a sign matrix with all entries positive outside its first row has permanent \((n-1)!\sum_j s_j\); a balanced first row makes this zero. This is a distinct operator and shows that cyclic reduction, not mere parity of \(n\), excludes all vanishing multipliers.

## Verification

The accompanying `checker.py` evaluates signed circulant permanents exactly using subset dynamic programming with integer arithmetic. It tests every sign pattern up to a global sign flip at orders \(n=2,4,8\) and four further, deliberately different sign patterns at \(n=16\). It confirms both the congruence modulo \(2^n\) and the exact \(2\)-adic valuation. It separately checks the balanced-row construction for full Walsh zeros. Run `python3 checker.py`; the expected marker is `CIRCULANT_SIGN_PERMANENT_EXACT_PASS cases= 142`. These finite tests illustrate, but do not replace, the proof for every \(k\ge1\).

## Relationship to prior work

The foundational permanent-of-circulant literature includes Minc's 1972 study of special circulants. Tao and Vu (first public preprint 2008-04-15) study nonvanishing for an independent random Bernoulli sign matrix with high probability; independence assumptions do not imply nonvanishing for every deterministic circulant sign pattern. The present argument uses a cyclic orbit-divisibility mechanism absent from such a probabilistic theorem. General congruences for circulant permanents were subsequently studied by Sburlati (2017). Because its full text was not accessible for examination, earlier coverage of this exact congruence is a genuine unresolved historical-priority risk; the abstract alone does not resolve the implication comparison. This work does not claim to originate rook expansions or the general theory of circulant permanents.

## Limitations

The result applies only to dyadic orders and circulant binary sign patterns, and it does not give a complete magnitude spectrum or sharp minimum absolute permanent. The bound on the inverse operator norm may be nonsharp. The 2017 circulant-congruences article and other restricted signed-permanent results require further full-text historical-priority checking. The mathematical proof is supplied here but has not undergone independent expert validation.

## References

1. H. Minc, *On permanents of circulants*, Pacific Journal of Mathematics **42** (1972), 477–484, https://msp.org/pjm/1972/42-2/pjm-v42-n2-p15-p.pdf.
2. T. Tao and V. Vu, *On the permanent of random Bernoulli matrices*, arXiv:0804.2362, first posted 2008-04-15, https://arxiv.org/abs/0804.2362.
3. G. Sburlati, *Congruences for permanents and determinants of circulants*, Linear Algebra and its Applications **531** (2017), 257–267, doi:10.1016/j.laa.2017.06.004 (full text not examined).
4. G. Sburlati, *On the parity of permanents of circulant matrices*, Linear Algebra and its Applications **428** (2008), 1949–1955, doi:10.1016/j.laa.2007.11.002 (abstract consulted).
