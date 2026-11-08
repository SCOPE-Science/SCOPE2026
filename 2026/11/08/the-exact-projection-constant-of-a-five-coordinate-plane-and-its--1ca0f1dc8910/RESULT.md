# The exact projection constant of a five-coordinate plane and its higher-dimensional extensions

## Finding

Let \(V\subset\ell_\infty^5(\mathbb R)\) be the two-dimensional plane spanned by
\[
u=(1,4/5,1/4,-1/4,-4/5),\qquad v=(0,3/5,1,1,3/5).
\]
The least norm of a projection from the five-dimensional real coordinate cube onto \(V\) is exactly
\[
\boxed{\lambda(V)=845/659=1.282245827\ldots.}
\]
For each integer \(n\ge3\), the canonical extension
\[
W_n=V\oplus_\infty\mathbb R\oplus_\infty
\bigoplus_{k=1}^{n-3}\{(t,t):t\in\mathbb R\}\subset\ell_\infty^{2n}(\mathbb R)
\]
has the same exact relative projection constant, \(\lambda(W_n)=845/659\). These are the coordinate-block planes associated with the codimension-variable construction motivated by Deregowska and Lewandowska [1]; the explicit constant improves its previously exhibited projection upper bound \(13/10\).

## Assumptions and scope

All scalar fields are real. For a subspace \(E\subset X\), write
\[
\lambda_X(E)=\inf\{\|P\|:P:X\to X\text{ is linear},\;P^2=P,\;\operatorname{ran}P=E\}.
\]
We abbreviate \(\lambda_{\ell_\infty^5}(V)\) by \(\lambda(V)\) and similarly for the displayed inclusion of \(W_n\). There are no asymptotic assumptions. The term \(\{(t,t):t\in\mathbb R\}\) is one-dimensional with the inherited max norm. The result concerns this explicit family, not the maximal projection constant of all subspaces of a given dimension.

## Proof

**Symmetrization.** Put
\[
S(x_1,x_2,x_3,x_4,x_5)=(-x_1,x_5,x_4,x_3,x_2).
\]
This is a signed coordinate isometry with \(S^2=I\), \(Su=-u\), and \(Sv=v\). Any projection \(P\) onto \(V\) has the form \(Px=f(x)u+g(x)v\) with \(f(u)=g(v)=1\) and \(f(v)=g(u)=0\). Averaging \(P\) with \(SPS\) gives a projection onto \(V\) of no greater norm. Such a symmetrized projection has coefficient rows
\[
f=(a,b,c,-c,-b),\qquad g=(0,d,e,e,d).
\]
The four interpolation equations reduce to exactly
\[
a+\frac85b+\frac12c=1,\qquad\frac65d+2e=1.
\]

**Reduction to nonnegative coefficients.** The maximum absolute row sums of the matrix \(uf+vg\) are
\[
\begin{aligned}
N_1&=|a|+2|b|+2|c|,\\
N_2&=\frac45|a|+2\max\{\frac45|b|,\frac35|d|\}+2\max\{\frac45|c|,\frac35|e|\},\\
N_3&=\frac14|a|+2\max\{\frac14|b|,|d|\}+2\max\{\frac14|c|,|e|\}.
\end{aligned}
\]
The five row sums are \(N_1,N_2,N_3,N_3,N_2\). By the triangle inequality, \(A=|a|+8|b|/5+|c|/2\ge1\) and \(B=6|d|/5+2|e|\ge1\). Replacing \((a,b,c)\) by \((|a|,|b|,|c|)/A\) and \((d,e)\) by \((|d|,|e|)/B\) preserves the two interpolation equations, makes all coefficients nonnegative, and does not increase any displayed row sum. Hence the infimum may be computed with nonnegative \(a,b,c,d,e\).

**Exact dual lower bound.** For such nonnegative coefficients introduce four linear minorants of the row sums:
\[
\begin{aligned}
L_1&=a+2b+2c,\\
L_{2a}&=\tfrac45a+\tfrac65d+\tfrac65e,\\
L_{2b}&=\tfrac45a+\tfrac85b+\tfrac65e,\\
L_3&=\tfrac14a+2d+2e.
\end{aligned}
\]
From the maxima in the preceding formulas one has \(L_1\le N_1\), \(L_{2a},L_{2b}\le N_2\), and \(L_3\le N_3\). The exact rational identity
\[
104L_1+29L_{2a}+286L_{2b}+240L_3
=416\left(a+\tfrac85b+\tfrac12c\right)+429\left(\tfrac65d+2e\right)=845
\]
holds termwise. Since the positive weights total \(659\), every projection has norm at least \(845/659\).

**Attaining projection.** Take
\[
f_*=(520/659,105/1318,110/659,-110/659,-105/1318),
\]
\[
g_*=(0,70/659,575/1318,575/1318,70/659).
\]
Direct substitution gives \(f_*(u)=g_*(v)=1\) and \(f_*(v)=g_*(u)=0\); hence \(P_*(x)=f_*(x)u+g_*(x)v\) is a projection. Its five absolute row sums all equal \(845/659\), so the lower bound is attained.

**Higher-dimensional extension.** Restrict any projection from \(\ell_\infty^{2n}\) onto \(W_n\) to the first five input coordinates and then project its output onto the first five coordinates. This gives a projection onto \(V\), so the norm is at least \(845/659\). Conversely, take the direct sum of \(P_*\), the identity on the next scalar coordinate, and the norm-one averaging projection \((s,t)\mapsto((s+t)/2,(s+t)/2)\) on each additional pair. Its norm is exactly \(845/659\), establishing the equality for every \(n\ge3\).

## Verification

A standalone standard-library script, `verify_projection.py`, checks the interpolation equations, all five row norms, the exact dual polynomial identity, the strict comparison \(845/659<13/10\), and the direct-sum finite matrices at selected dimensions using rational arithmetic. The proof above is independent of finite sampling: the general lower inequality and the direct-sum construction hold symbolically for every allowed dimension.

## Relationship to prior work

Deregowska and Lewandowska [1, Section 3] introduce a finite-dimensional construction to demonstrate limitations of a proposed geometric disjoint-support splitting principle in the study of projection constants and Banach–Mazur distance. Their explicit projection estimate \(13/10\) demonstrates the relevant strict \(4/3\) threshold but does not supply an exact minimization for the indicated five-coordinate plane. Here that optimization is completed using a symmetric linear-programming reduction and a matching rational dual witness. General bounds for two-dimensional projection constants are broader but do not by themselves imply this specific rational number. The precision matters because it calibrates the smallest projection norm of the natural obstruction rather than the norm of one arbitrary retraction.

## Limitations

The theorem is specific to the displayed real plane and its explicitly defined max-norm extensions. It does not classify optimal projections for all two-dimensional planes, establish the precise Banach–Mazur distance of these extensions, or resolve the codimension-free conjecture in [1]. The article comparison is a best-knowledge literature assessment; independent publication-priority confirmation is not claimed.

## References

[1] B. Deregowska and B. Lewandowska, *Projection Constants and Banach-Mazur Distance in Codimension Two*, arXiv:2610.06141v1, publicly submitted 2026-10-05, https://arxiv.org/abs/2610.06141.

[2] H. König and N. Tomczak-Jaegermann, work on maximal projection constants of low-dimensional Banach spaces (background on two-dimensional projection constants); no exact evaluation of the present plane is attributed to this source.
