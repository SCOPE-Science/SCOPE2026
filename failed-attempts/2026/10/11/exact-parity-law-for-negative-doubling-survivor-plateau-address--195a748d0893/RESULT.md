# Exact parity law for negative-doubling survivor-plateau address widths
## Finding
Consider the negative doubling map
\[
T_{-2}(x)=\begin{cases}-2x+1,&0\le x<1/2,\\\\-2x+2,&1/2<x\le1.\end{cases}
\]
Fix a nonempty hole \((a,b)\) with \(0<a\le 1/2<b<1\). Let \(\alpha=\tau_{-2}(a-)\) and \(\beta=\tau_{-2}(b+)\), and assume the weak-admissibility hypotheses under which Ding--Steiner--Sun classify the symbolic plateau of \(\beta\).

Let
\[
n=\min\{2j:j\ge1,\ \sigma^{2j}\beta=\beta\},\qquad
m=\min\{2j+1:j\ge0,\ \sigma^{2j+1}\beta=\alpha\},
\]
with the minimum of an empty set interpreted as \(\infty\), and put \(k=\min\{n,m\}\). When \(k<\infty\), write \(w=\beta|_k\). The source theorem gives
\[
P(\beta)=(L,\beta],
\]
where \(L=w\alpha\) if \(k\) is even and \(L=w^\infty\) if \(k\) is odd. Define the left address boundary
\[
b_*=\pi_{-2}(L),
\]
where \(\pi_{-2}\) is the source address map. Then
\[
b-b_*=2^{-k}(b-a)\qquad\text{if \(k\) is even},
\]
and
\[
b-b_*=\frac{b-a}{2^k+1}\qquad\text{if \(k\) is odd}.
\]
If \(k=\infty\), the source theorem gives \(P(\beta)=\{\beta\}\), so the address width is zero.

Equivalently, every nontrivial plateau in this finite-return class has normalized address width
\[
\frac{b-b_*}{b-a}=
\begin{cases}
2^{-k},&k\text{ even},\\\\
(2^k+1)^{-1},&k\text{ odd}.
\end{cases}
\]

## Assumptions and scope
The claim uses exactly the negative-doubling coding and plateau construction of Ding--Steiner--Sun. The boundary pair must satisfy the weak-admissibility hypotheses of their plateau theorem. The hole is taken nonempty with \(b>1/2\) to avoid the empty-hole convention. The quantity proved here is the Euclidean separation of the two coded plateau boundaries \(\pi_{-2}(\beta)=b\) and \(\pi_{-2}(L)=b_*\). At precritical points two one-sided symbolic names can represent the same coordinate; this can affect endpoint notation but not the numerical width.

## Proof
The address map is
\[
\pi_{-2}(u)=-\sum_{j\ge1}\frac{u_j}{(-2)^j},\qquad u_j\in\{1,2\}.
\]
Its one-symbol recursions are
\[
\pi_{-2}(1\xi)=\frac{1-\pi_{-2}(\xi)}2,\qquad
\pi_{-2}(2\xi)=\frac{2-\pi_{-2}(\xi)}2.
\]
Iterating these recursions through any word \(w\) of length \(k\) gives an affine prefix identity
\[
\pi_{-2}(w\xi)=A_w+\left(-\frac12\right)^k\pi_{-2}(\xi)
\]
for a constant \(A_w\) depending only on \(w\).

Suppose first that \(k\) is even. Since \(n\) is even and \(m\) is odd, \(k=n\). Hence \(\beta=w\beta\), while the source left endpoint is \(L=w\alpha\). Put \(q=2^{-k}\). Because the prefix slope is \(+q\),
\[
b=A_w+qb,\qquad b_*=A_w+qa.
\]
Subtracting yields
\[
b-b_*=q(b-a)=2^{-k}(b-a).
\]

Suppose next that \(k\) is odd. Then \(k=m\), so \(\beta=w\alpha\), while \(L=w^\infty\). With \(q=2^{-k}\), the prefix slope is \(-q\). Therefore
\[
b=A_w-qa.
\]
The periodic endpoint \(b_*=\pi_{-2}(w^\infty)\) is the fixed point of the same affine prefix map, hence
\[
b_*=A_w-qb_*.
\]
Thus \(A_w=(1+q)b_*\), and substitution into the formula for \(b\) gives
\[
b=b_*+q(b_*-a).
\]
Consequently
\[
b-a=(1+q)(b_*-a),
\]
and hence
\[
b-b_*=\frac{q}{1+q}(b-a)=\frac{b-a}{2^k+1}.
\]
This proves both finite-return formulas. The \(k=\infty\) case is the singleton case in the source theorem, so its width is zero.

## Verification
The proof is exact and symbolic; no finite experiment is used to infer an infinite statement. The only nonstandard inputs are the source's plateau theorem and its address map. The prefix identity follows directly by iterating the two displayed one-symbol recursions. The parity split is forced because \(n\) is even and \(m\) is odd. In the even case the boundary equations are \(b=A_w+2^{-k}b\) and \(b_*=A_w+2^{-k}a\). In the odd case they are \(b=A_w-2^{-k}a\) and \(b_*=A_w-2^{-k}b_*\); solving them gives the stated denominator \(2^k+1\).

No assertion is made about plateau frequencies, measures of the parameter set, or asymptotics beyond the exact width formula. Endpoint inclusion under dual precritical codings is not used.

## Relationship to prior work
Ding, Steiner and Sun classify symbolic survivor-space plateaux for \(T_{-2}\). Their finite-return theorem identifies the symbolic left endpoint as \(w\alpha\) in the even self-return case and \(w^\infty\) in the odd arrival case, and their preliminaries provide the address map \(\pi_{-2}\). They also prove a devil's-staircase result for the Hausdorff dimension of the survivor set as the right hole endpoint varies.

The present statement extracts a quantitative geometric invariant not stated in that classification: the exact coordinate separation between the symbolic plateau boundaries. The parity-sensitive formulas are not merely two presentations of one expression; the even self-return has normalized width \(2^{-k}\), whereas the odd arrival has normalized width \((2^k+1)^{-1}\).

Targeted searches for negative-doubling plateau widths, decreasing-Lorenz hole plateau lengths, negative-beta survivor plateau endpoints, and equivalent return-time formulations did not locate a published statement implying these exact formulas. Earlier Lorenz-hole work concerns increasing expansive Lorenz maps and characterizes plateau intervals qualitatively; the recent decreasing-map source is the relevant theorem for the present parity-sensitive setting.

## Limitations
The result is conditional on the weak-admissible finite-return plateau classification of the cited source and does not extend here to arbitrary hole codings outside that theorem. The \(k=\infty\) case contributes only the source's singleton conclusion. The formula measures the coordinate gap between the coded boundary addresses; isolated dual codings can alter which symbolic name is attached to an endpoint but not the gap itself.

The originality assessment is necessarily relative to the inspected source and targeted literature searches. A differently phrased folklore observation about affine negative-base coding remains a residual bibliographic risk.

## References
1. Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1 (first public 2026-10-02), especially the address-map preliminaries and the survivor-plateau theorem.
2. Y. Sun, B. Li, Y. Ding, *Topological expansive Lorenz maps with a hole at critical point*, arXiv:2311.02465 (background on plateau intervals for expansive Lorenz maps with holes).
