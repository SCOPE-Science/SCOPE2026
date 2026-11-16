# Uniform Fourier nonvanishing on rank-one strictly upper-triangular cones

## Finding
Let \(q\) be any prime power and \(n\ge4\). In the additive group \(\mathfrak u_n(\mathbb F_q)\) of strictly upper-triangular matrices, consider the cone \(C_{n,q}=\{A:\operatorname{rank}A\le1\}\), including the zero matrix. For every additive Fourier frequency \(B\), the unnormalized Fourier transform \(W_{n,q}(B)=\sum_{A\in C_{n,q}}\psi(\sum_{i<j}B_{ij}A_{ij})\), with any nontrivial additive character \(\psi\), is an integer satisfying
\[
W_{n,q}(B)\equiv-q\pmod{q^2}.
\]
In particular, every coefficient is nonzero, has exactly the prime-adic valuation of \(q\), and has absolute value at least \(q\). Hence convolution by the indicator of this natural rank-one determinantal cone is invertible on functions on \(\mathfrak u_n(\mathbb F_q)\). The dimensional threshold is sharp: for \(n=2\), exactly \(q-1\) frequencies vanish, and for \(n=3\), exactly \(q^2(q-1)\) frequencies vanish.

## Assumptions and scope
The field \(\mathbb F_q\) has characteristic \(p\) and \(q=p^r\), for integers \(r\ge1\). Frequencies are identified with upper-triangular coordinate arrays using the nondegenerate coordinate pairing \(\langle B,A\rangle=\sum_{1\le i<j\le n}B_{ij}A_{ij}\). No identification with the ordinary matrix-trace pairing is intended. A nontrivial character may be written \(\psi(z)=\exp(2\pi i\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(tz)/p)\) with \(t\in\mathbb F_q^\times\). This changes frequency parametrization but not the assertions. For \(n\ge2\), \(C_{n,q}\) contains the zero matrix and all rank-one strict upper-triangular matrices, not just an individual matrix orbit.

## Proof
**1. Projective charts and the character sum.** Every nonzero rank-one matrix has an outer-product decomposition \(A=uv^{\mathsf T}\). Strict upper triangularity is equivalent to \(k=\max\operatorname{supp}u<\ell=\min\operatorname{supp}v\). For each pair \(1\le k<\ell\le n\), normalize the projective matrix line by \(u_k=v_\ell=1\). The independent variables are \(x=(u_1,\ldots,u_{k-1})\) and \(y=(v_{\ell+1},\ldots,v_n)\). Distinct pairs give disjoint projective charts of cardinality \(q^{d_{k\ell}}\), where \(d_{k\ell}=(k-1)+(n-\ell)\).

Let \(R_n=\sum_{k<\ell}q^{d_{k\ell}}=\sum_{h=0}^{n-2}(h+1)q^h\) be the number of rank-one projective lines, and let \(Z_n(B)\) be the number of such projective lines annihilated by \(\langle B,\cdot\rangle\). Multiplying a projective representative by each nonzero scalar gives a complete matrix line, whose character sum is \(q-1\) if the pairing is zero and \(-1\) otherwise. Including the zero matrix gives the **exact integer identity**
\[
W_{n,q}(B)=1-R_n+qZ_n(B).
\]

**2. Divisibility of high-dimensional charts.** On a \((k,\ell)\)-chart the pairing polynomial is separately affine-linear in \(k-1\) variables \(x\) and \(n-\ell\) variables \(y\). If either group has at least two free variables, fix the other group. The remaining equation is affine-linear in at least two variables; its zero count is either zero, or \(q^{s-1}\), or \(q^s\), where \(s\ge2\). Every possibility is divisible by \(q\). Thus only the charts \((1,n)\), \((1,n-1)\), \((2,n)\), and \((2,n-1)\) can contribute to \(Z_n(B)\bmod q\), for \(n\ge4\).

**3. Four-chart cancellation.** Set \(a=B_{1n}\), \(b=B_{1,n-1}\), \(c=B_{2n}\), and \(d=B_{2,n-1}\). The equations on these four charts are, in order,
\[
a=0,\qquad b+ay=0,\qquad c+ax=0,\qquad d+bx+cy+axy=0.
\]
If \(a=0\), their zero counts modulo \(q\) are respectively \(1,0,0,0\); this includes the cases when an affine-linear polynomial vanishes identically, since such a chart then has \(q\) or \(q^2\) points. If \(a\ne0\), the counts are \(0,1,1,-1\). Indeed, completing the product gives \(a(x+c/a)(y+b/a)=bc/a-d\), which has either \(q-1\) or \(2q-1\) solutions, both congruent to \(-1\pmod q\). Consequently \(Z_n(B)\equiv1\pmod q\) for every frequency.

**4. Fourier congruence and invertibility.** For \(n\ge4\), \(R_n\equiv1+2q\pmod{q^2}\). Substituting the preceding congruence into the exact character-sum identity gives \(W_{n,q}(B)\equiv-q\pmod{q^2}\). No such integer can vanish; furthermore it is divisible by \(p^r\) and not by \(p^{r+1}\). Additive Fourier diagonalization of convolution proves invertibility, and the integer congruence implies \(|W_{n,q}(B)|\ge q\).

**5. Exact smaller-dimensional boundary.** For \(n=2\), the cone equals the one-dimensional additive matrix space, so its Fourier transform is \(q\) at the zero frequency and zero at the other \(q-1\) frequencies. For \(n=3\), the three projective charts have equations \(a=0\), \(b+ay=0\), \(c+ax=0\), with \(a=B_{13}\), \(b=B_{12}\), \(c=B_{23}\). If \(a\ne0\), exactly two projective lines have zero pairing, giving \(W=0\). If \(a=0\), the exact Fourier coefficient is \(q(-1+q\mathbf1_{b=0}+q\mathbf1_{c=0})\), which never vanishes. Thus precisely \(q^2(q-1)\) frequencies yield zero.

## Verification
The included standalone `checker.py` evaluates full Walsh transforms for binary fields through \(n=6\), projective hyperplane counts over prime fields including \(q=3,5,7\), and direct finite-field additive-character transforms over \(\mathbb F_4\). In every tested case, the zero counts and residue congruence agree with the theorem. Run with `python checker.py` in an environment with NumPy. The code tests finite cases only; the preceding proof handles all dimensions and prime powers.

## Relationship to prior work
Diaconis and Thiem (2006) develop general supercharacters for upper-unitriangular pattern groups; their nonabelian supercharacter formulas do not state this additive Fourier congruence for the union of all rank-one strictly upper-triangular matrices. Lewis et al. (2010) study rank enumerations of matrices with forbidden positions; their enumerative formulas do not supply the arbitrary-frequency transform. General rank-metric association-scheme Fourier formulas for unconstrained rectangular matrices do not specialize simply to this triangularly constrained cone, whose Fourier values depend on matrix positions. The theorem uses projective chart geometry and a four-corner cancellation, not rank-only Fourier symmetry.

## Limitations
The theorem applies to the rank-at-most-one cone in a strictly upper-triangular matrix space with the coordinate additive pairing. It does not classify higher-rank triangular cones or the exact minimum nonzero Fourier magnitude in every dimension. A broader historical literature search or independent proof review could identify an earlier equivalent formulation; no claim of priority beyond the sources listed is warranted. The finite checker is corroboration, not an infinite proof.

## References
- P. Diaconis and N. Thiem, *Supercharacter formulas for pattern groups*, arXiv:math/0610161, first made public 2006-10-04. https://arxiv.org/abs/math/0610161
- J. B. Lewis, R. I. Liu, A. H. Morales, G. Panova, S. V. Sam, and Y. X. Zhang, *Matrices with restricted entries and q-analogues of permutations*, arXiv:1011.4539, first made public 2010-11-20. https://arxiv.org/abs/1011.4539
