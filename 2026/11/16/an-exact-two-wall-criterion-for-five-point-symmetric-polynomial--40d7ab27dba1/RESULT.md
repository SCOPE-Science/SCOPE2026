# An exact two-wall criterion for five-point symmetric polynomial hypergroups

## Finding

For a strictly increasing five-state profile \((0,u,v,w,1)\), all \(125\) finite linearization coefficients of the associated symmetric orthogonal polynomials are nonnegative **if and only if** two explicit polynomial inequalities hold:

\[
A:=1-u-w\ge0,\qquad
C:=(1-w)^2-u(1-2w)-v\bigl((1-u)(1-w)+uw\bigr)\ge0.
\]

The inequalities are independent, and both are sharp. This is a complete semialgebraic description of the symmetric endpoint for the five-point family, including products beyond the terminal polynomial degree.

## Assumptions and scope

Take arbitrary real \(0<u<v<w<1\). Put \((d_0,d_1,d_2,d_3,d_4)=(0,u,v,w,1)\) and define \(R_0(x)=1\), \(R_1(x)=x\), and

\[
xR_i(x)=(1-d_i)R_{i+1}(x)+d_iR_{i-1}(x)
\quad(i=1,2,3).
\]

At the five-point spectral support use the terminal identity \(xR_4=R_3\). Equivalently, let \(J\) be the \(5\times5\) stochastic tridiagonal matrix with \(J_{i,i+1}=1-d_i\), \(J_{i,i-1}=d_i\) and zero diagonal, with indices from \(0\) through \(4\). Then \(R_m(J)\) is defined for every \(0\le m\le4\). We write

\[
R_mR_n=\sum_{k=0}^4g(m,n;k)R_k
\]

as an identity of functions on the five-point orthogonality support, not as an unrestricted polynomial identity. The theorem quantifies over all \(0\le m,n,k\le4\). Because \(J\) is irreducible and similar to a symmetric Jacobi matrix with positive off-diagonal entries, its five eigenvalues are distinct and its spectral measure at the first basis vector has positive masses; no extra assumption on the support is required.

## Proof

**Step 1: finite spectral realization.** Set \(a_i=1-d_i\). Reversibility of the tridiagonal chain gives positive numbers \(\pi_0=1\) and \(\pi_i/\pi_{i-1}=a_{i-1}/d_i\). The conjugate \(\operatorname{diag}(\sqrt{\pi_i})J\operatorname{diag}(\pi_i^{-1/2})\) is symmetric with positive off-diagonal entries. It has a cyclic first basis vector and five distinct real eigenvalues. The polynomials are orthogonal for its first-coordinate spectral measure, and multiplication by \(R_m\) in the polynomial basis is \(R_m(J)\). Therefore

\[
g(m,n;k)=[R_m(J)]_{n,k}.
\]

**Step 2: reduce to nine triple classes.** Write \(h_k=\int R_k^2\,d\mu=\prod_{i=1}^k d_i/(1-d_{i-1})>0\). Orthogonality yields \(h_k g(m,n;k)=\int R_mR_nR_k\,d\mu\), symmetric in all three indices. Hence the signs are invariant under permutations of \((m,n,k)\). The bipartite symmetry \(R_i(-x)=(-1)^iR_i(x)\) kills odd-total-degree triples, and degree orthogonality kills triples that violate a triangle inequality. Every coefficient involving index zero is zero or strictly positive. Apart from these, exactly the following nine unordered triples remain. Their entries are computed by the recurrence, with the smallest index used as first factor:

| Triple \((m,n,k)\) | \(g(m,n;k)\) |
|---|---|
| \((1,1,2)\) | \(1-u\) |
| \((1,2,3)\) | \(1-v\) |
| \((1,3,4)\) | \(1-w\) |
| \((2,2,2)\) | \((w-u+vA)/(1-u)\) |
| \((2,2,4)\) | \((1-v)(1-w)/(1-u)\) |
| \((2,3,3)\) | \((1-u-vw)/(1-u)\) |
| \((2,4,4)\) | \(A/(1-u)\) |
| \((3,3,4)\) | \((1-w)B/((1-u)(1-v))\) |
| \((4,4,4)\) | \(C/((1-u)(1-v)(1-w))\) |

Here \(B=1-u-v+uv-vw\). All denominators displayed above are strictly positive in the declared domain. Necessity follows at once from the last and third-to-last table entries.

**Step 3: two inequalities suffice.** Define \(D=(1-u)(1-w)+uw=1-u-w+2uw>0\). Direct expansion gives the exact identity

\[
DB=(1+w-u)C+w^2A.
\]

If \(A\ge0\), then \(w-u+vA>0\), and \(1-u-vw\ge1-u-w=A\ge0\). If also \(C\ge0\), the identity forces \(B\ge0\). Every entry in the table is then nonnegative, and triple permutation plus the zero-index cases establish the property for every product, including those of degree sum exceeding four. This proves sufficiency.

**Step 4: distinct sharp boundaries.** At \((u,v,w)=(1/6,1/4,11/12)\) one has \(A=-1/12\) and \(C=13/144>0\); at \((1/12,5/12,2/3)\) one has \(A=1/4>0\) and \(C=-5/432\). Hence neither inequality follows from the other on the profile domain.

The second wall has the equivalent useful form

\[
C=D(w-v)+(1-u)(1-w)(1-2w).
\]

In particular, all strictly increasing profiles with \(w\le1/2\) automatically have nonnegative linearization; at \(w>1/2\) the necessary and sufficient second-wall condition is \(D(w-v)\ge(1-u)(1-w)(2w-1)\), together with \(u+w\le1\).

**Step 5: an exact log-concavity gap.** For \((u,v,w)=(1/20,3/20,7/20)\), \(A=3/5\), \(C=1249/4000\) and the four nonzero Newton coefficients of \(d\) are \((1/20,1/20,1/20,3/10)\). Thus all are positive, but \(\nu_3^2=1/400<3/200=\nu_2\nu_4\). The theorem nevertheless yields every linearization coefficient nonnegative.

## Verification

The accompanying standalone script `CHECK.py` constructs the exact symbolic recurrence matrices in SymPy, checks all nine table formulas and the elimination identities, tests the complete \(125\)-entry coefficient tensor against the nine symmetric classes, verifies the three rational boundary profiles, and independently evaluates \(200\) fixed-seed rational profiles. The symbolic identities and inequalities above, not the finite random tests, establish the theorem for infinitely many real profiles. Run with `python CHECK.py` in an environment with SymPy installed.

## Relationship to prior work

Polzer's 2026 log-concave Newton-profile criterion guarantees nonnegative linearization for all constant downward/diagonal ratios and asks for sharper boundaries; the present result determines the **entire symmetric-ratio endpoint** for the first five-state nontrivial parameter family. It is neither a proof of the general all-ratios open problem nor a restatement of log-concavity: the given rational profile violates log-concavity. Szwarc's earlier discrete-hyperbolic characterization and Miclo's spectral hypergroup criterion can test general recurrences abstractly, but do not in the inspected materials provide these two explicit polynomial walls. Previous four-point criteria do not determine the extra five-state terminal interaction.

## Limitations

The theorem is restricted to \(d=(0,u,v,w,1)\) with \(0<u<v<w<1\) and the symmetric diagonal-free recurrence \(b_i=0\), \(c_i=d_i\). It does not classify unequal diagonal/downward ratios, systems with more than five support points, or the entire endpoint-free family. The matrices are finite, but proof validity is exact for all permitted real parameters. An older specialized five-point table might contain the same two-inequality reduction; the novelty assessment remains provisional pending external review. No independent mathematical audit has been performed.

## References

1. L. P. Polzer, *A log-concavity criterion for finite nonnegative linearization*, arXiv:2611.01561v1 (first posted 2026-11-01), https://arxiv.org/html/2611.01561v1.
2. L. P. Polzer, *Exact and perturbative criteria for finite nonnegative linearization*, companion manuscript (2026), https://github.com/skypher/szkraw/blob/v1.0.6/papers/p3.tex.
3. R. Szwarc, *A necessary and sufficient condition for nonnegative product linearization of orthogonal polynomials*, Constructive Approximation 19 (2003), 565–573, https://www.math.uni.wroc.pl/~szwarc/ps/newnote.pdf.
4. L. Miclo, *On the hypergroup property*, Ann. Fac. Sci. Toulouse 26 (2017), https://doi.org/10.5802/afst.1539.
