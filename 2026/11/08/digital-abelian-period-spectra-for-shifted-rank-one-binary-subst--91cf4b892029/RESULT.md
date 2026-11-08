# Digital Abelian-period spectra for shifted rank-one binary substitutions

## Finding

Let \(a,b\ge 1\) be integers, let \(L=a+b\), and define the constant-length binary substitution
\[
\varphi(0)=0^a1^b,\qquad \varphi(1)=1^b0^a.
\]
Let \(X=\varphi^\omega(0)\), indexed from zero. For a shift \(c\ge0\), a positive integer \(p\) is a *pure Abelian period at shift* \(c\) if all the consecutive length-\(p\) factors of \(X[c:]\), beginning at \(c+jp\) for \(j\ge0\), have equal Parikh vectors.

Put \(C=\{\min(a,b),\ldots,\max(a,b)-1\}\) (empty if \(a=b\)). Write \(c=qL+r\) with \(q\ge0\) and \(0\le r<L\), and write the nonnegative integer \(q\) in base \(L\), padding with leading zero digits when needed.

**Theorem.** The following assertions hold simultaneously for every \(a,b\ge1\), \(c\ge0\), and \(t\ge1\).

1. When \(r=0\), the entire pure Abelian-period set is precisely \(\{mL:m\ge1\}\).
2. When \(1\le r<L\), the length \(L^t\) is a pure Abelian period at shift \(c\) **if and only if** at least one of the lowest \(t-1\) base-\(L\) digits of \(q\) belongs to \(C\). In particular, if the least such digit occurs in position \(h\) (position zero is the units digit), then the least pure Abelian period of the restricted form \(L^t\) is \(L^{h+2}\). If no such digit occurs, no power of \(L\) is a pure Abelian period at that shift.
3. The exact number of shifts \(c\in\{0,\ldots,L^t-1\}\) at which \(L^t\) is a pure Abelian period equals
\[
\boxed{L^t-(L-1)(2\min(a,b))^{t-1}.}
\]
Thus if \(a\ne b\), the proportion of such shifts tends to one as \(t\to\infty\), whereas if \(a=b\), it equals \(1/L\) at every \(t\).

## Assumptions and scope

Both run lengths are strictly positive. The word \(X\) exists since \(\varphi(0)\) begins with \(0\), and each substitution image has length \(L\) and exactly \(b\) ones. The spectrum in assertion 2 is restricted to substitution-power lengths \(L^t\); the theorem does not classify arbitrary lengths for nonaligned shifts. The aligned-shift assertion 1, by contrast, classifies *all* positive lengths.

## Proof

**1. Prefix discrepancy and its zeros.** Define \(P(N)=\sum_{i=0}^{N-1}X_i\) for \(N\ge0\), and \(D(N)=LP(N)-bN\). Each block \(\varphi(X_j)\) has exactly \(b\) ones, so \(P(qL)=qb\) and \(D(qL)=0\) for every \(q\ge0\). For \(0<r<L\), the substitution fixed-point property gives
\[
D(qL+r)=H_r(X_q),\qquad
H_r(s)=L\,|\operatorname{pref}_r(\varphi(s))|_1-br.
\]
If \(s=0\), then
\[
H_r(0)=\begin{cases}-br,&1\le r\le a,\\a(r-L),&a<r<L;\end{cases}
\]
while if \(s=1\), then
\[
H_r(1)=\begin{cases}ar,&1\le r\le b,\\b(L-r),&b<r<L.\end{cases}
\]
Hence \(H_r(0)<0<H_r(1)\) for every \(0<r<L\). In particular, the discrepancy \(D\) is bounded, and \(D(N)=0\) exactly when \(L\mid N\).

**2. Periods are horizontal arithmetic progressions.** Suppose the blocks starting at \(c+jp\), \(j\ge0\), all contain \(s\) ones. Then
\[
D(c+kp)=D(c)+k(Ls-bp)\qquad(k\ge0).
\]
The left-hand side is bounded, so \(Ls=bp\), and consequently \(D(c+kp)=D(c)\) for all \(k\ge0\). Conversely, if these discrepancy values are equal, subtracting consecutive values shows that the corresponding length-\(p\) blocks have exactly \(bp/L\) ones and hence equal Parikh vectors. Thus pure Abelian periodicity is equivalent to constancy of \(D\) on the progression \(c+p\mathbb N_0\).

If \(r=0\), this progression starts at discrepancy zero. Its first increment can end at discrepancy zero only when \(L\mid c+p\), equivalently \(L\mid p\). Conversely, if \(L\mid p\), every endpoint remains aligned, with discrepancy zero. This proves assertion 1.

**3. Coincidence-column automaton.** For each column \(0\le d<L\) define the map \(g_d:\{0,1\}\to\{0,1\}\) by \(g_d(s)=\varphi(s)_d\). Comparing \(0^a1^b\) with \(1^b0^a\), one sees that \(g_d\) is constant precisely when \(d\in C\); for every other \(d\), it is a bijection. In particular \(g_0\) is the identity. By the fixed-point identity,
\[
X_{Ln+d}=g_d(X_n)\qquad(n\ge0,\ 0\le d<L).
\]
Repeatedly removing the lowest \(h\) digits of an index shows that for every \(q,h,j\ge0\),
\[
X_{q+jL^h}=g_{d_0}\circ g_{d_1}\circ\cdots\circ g_{d_{h-1}}
\bigl(X_{\lfloor q/L^h\rfloor+j}\bigr),
\]
where \(d_0,\ldots,d_{h-1}\) are the lowest \(h\) base-\(L\) digits of \(q\). The composition is constant if any listed digit is in \(C\), and otherwise it is bijective. Every tail of \(X\) contains both letters, because each of the infinitely many length-\(L\) substitution blocks contains both. Therefore \((X_{q+jL^h})_{j\ge0}\) is constant exactly when some of those \(h\) digits lies in \(C\).

**4. Shifted substitution-power periods.** For \(c=qL+r\) with \(0<r<L\) and \(p=L^t\), the progression endpoints have discrepancies
\[
D(c+jL^t)=H_r\bigl(X_{q+jL^{t-1}}\bigr)\qquad(j\ge0).
\]
The two values \(H_r(0)\) and \(H_r(1)\) are distinct; hence the endpoint discrepancies are constant exactly when the sampled sequence \((X_{q+jL^{t-1}})_{j\ge0}\) is constant. The previous step supplies exactly the asserted digit criterion, including its sharp first power \(L^{h+2}\). No finite truncation or numerical experiment enters this implication.

**5. Exact shift census.** Let \(S=L-|C|=2\min(a,b)\). Among the \(L^{t-1}\) integers \(0\le q<L^{t-1}\), exactly \(S^{t-1}\) have all their lowest \(t-1\) digits outside \(C\). Each such \(q\) supplies \(L-1\) nonaligned shifts \(c=qL+r\), \(1\le r<L\), at which \(L^t\) fails. Every aligned shift succeeds. Subtracting these \((L-1)S^{t-1}\) failures from the \(L^t\) shifts proves assertion 3. Since \(S<L\) exactly when \(a\ne b\), its two density conclusions follow. \(\square\)

## Verification

The standalone Python program `checker.py` generates explicit substitution prefixes and compares the digit criterion with equal-length block Parikh vectors for 4,200 parameter/shift/power instances. It also verifies 100 exact finite shift censuses. All checks passed. This is finite corroboration, not the basis of the proof of the infinite statements.

## Relationship to prior work

Filimonova and Puzynina (2026), Theorem 4, identify the rank-one incidence-matrix case among the uniform binary morphisms whose fixed points are Abelian periodic. In this family the common Parikh vector makes period \(L\) at shift zero immediate. The result here instead resolves the exact behavior of *each nonaligned shift* at *every substitution-power scale* and counts the successful shifts. The 2013 bounded weak-Abelian-periodicity characterization by Avgustinovich and Puzynina concerns existence for the unshifted fixed point and does not give this digital shifted-period spectrum. The proof derives the distinction directly using the two nonzero discrepancy levels and constant versus bijective substitution columns.

## Limitations

For nonaligned shifts, periods not of the form \(L^t\) are not classified. The density statement concerns the proportion of shifts in the initial interval of length \(L^t\) that admit that same power as a pure Abelian period; it does not assert ordinary periodicity or a uniform period over all shifts. The work has not undergone an independent mathematical audit. Unindexed prior specializations remain a priority risk.

## References

1. A. Filimonova and S. Puzynina, *On abelian periodicity of purely morphic words*, arXiv:2605.30306, first posted 2026-05-28. https://arxiv.org/abs/2605.30306
2. S. Avgustinovich and S. Puzynina, *Weak abelian periodicity of infinite words*, arXiv:1302.4359, first posted 2013-02-18. https://arxiv.org/abs/1302.4359
