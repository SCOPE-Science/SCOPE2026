# Exact endpoint averaging amplification and spike–dust rigidity in mixed Lebesgue spaces

## Finding

Let \(X_{p,q}=L^p([0,1]_x;L^q([0,1]_y))\), with complex or real scalars and \(1\le p,q\le\infty\). For a measurable \(B\subseteq[0,1]^2\) with area \(|B|=t\in(0,1)\), let
\[
P_B f=\frac{\mathbf1_B}{t}\int_B f(x,y)\,dx\,dy,
\qquad K_{p,q}(t)=\sup_{|B|=t}\|P_B\|_{X_{p,q}\to X_{p,q}}.
\]
At every *nonreflexive boundary pair*, i.e. whenever at least one of \(p,q\) belongs to \(\{1,\infty\}\), the **exact all-area constant** is
\[
\boxed{K_{p,q}(t)=t^{-\left|1/p-1/q\right|}},\qquad 1/\infty:=0.
\]
There are three distinct attainment regimes:

1. If \((p,q)=(1,1)\) or \((\infty,\infty)\), every eligible set attains the constant \(1\).
2. If \((p,q)=(1,\infty)\) or \((\infty,1)\), a set is extremal if and only if its vertical section-length function \(m_B(x)=|\{y:(x,y)\in B\}|\) satisfies \(|\{x:m_B(x)>0\}|=1\) and \(\operatorname*{ess\,sup}_x m_B(x)=1\). Such sets exist for every \(0<t<1\).
3. At the remaining boundary pairs, where exactly one exponent is \(1\) or \(\infty\) and the other is strictly between them, **no set attains** \(K_{p,q}(t)\).

Moreover, all maximizing sequences have an explicit structural dichotomy. For \(1<q<\infty\) and \(p\in\{1,\infty\}\), a sequence of area-\(t\) sets \(B_n\) satisfies \(\|P_{B_n}\|\to K_{p,q}(t)\) if and only if
\[
\|m_{B_n}-t\|_{L^1([0,1])}\to0,
\qquad \operatorname*{ess\,sup}m_{B_n}\to1.
\]
For \(1<p<\infty\) and \(q\in\{1,\infty\}\), the corresponding equivalence is
\[
|\{m_{B_n}>0\}|\to1,
\qquad\int_0^1m_{B_n}(1-m_{B_n})\,dx\to0.
\]
Thus the two kinds of nonattainment arise respectively from vanishing-width high spikes on nearly constant sections and from vanishing-height dust on nearly binary sections.

## Assumptions and scope

All measures are normalized Lebesgue measure on \([0,1]\), and the order of the mixed norm is the displayed \(x\)-outside, \(y\)-inside order. The exponents are arbitrary within the stated boundary, including opposite corners. All sets are measurable modulo null sets; section lengths \(m_B(x)\in[0,1]\) have mean \(\int m_B=t\). The statement concerns the single-set rank-one averaging operator, **not** the conditional expectation onto a general sub-\(\sigma\)-algebra or the two-atom expectation \(P_B+P_{B^c}\). It makes no claim for interior exponents \(1<p,q<\infty\).

## Proof

**Step 1: exact rank-one norm.** The mixed-norm integral functional \(f\mapsto\int_B f\) has norm \(\|\mathbf1_B\|_{X_{p',q'}}\), using mixed Hölder and the definition of the associate norm (the latter remains valid for endpoint exponents). Thus
\[
\|P_B\|=\frac{\|\mathbf1_B\|_{p,q}\|\mathbf1_B\|_{p',q'}}{t}.
\tag{1}
\]
Every measurable \(m:[0,1]\to[0,1]\) with \(\int m=t\) occurs as the vertical section-length function of \(B_m=\{(x,y):0\le y<m(x)\}\). Put \(s=|\{m>0\}|\) and \(h=\operatorname*{ess\,sup}m\).

**Step 2: all endpoint inequalities.** If \(p=1\), \(1<q<\infty\), then (1) is exactly
\[
\|P_B\|=t^{-1}\Big(\int m^{1/q}\Big)h^{1/q'}\le t^{-1/q'}.
\tag{2}
\]
For \(p=\infty\), \(1<q<\infty\), it is
\[
\|P_B\|=t^{-1}h^{1/q}\Big(\int m^{1/q'}\Big)\le t^{-1/q}.
\tag{3}
\]
Both bounds follow from concavity of \(u\mapsto u^a\) for \(0<a<1\), Jensen, and \(h\le1\).

For \(q=1\), \(1<p<\infty\), (1) becomes
\[
\|P_B\|=t^{-1}\Big(\int m^p\Big)^{1/p}s^{1/p'}\le t^{-1/p'},
\tag{4}
\]
and for \(q=\infty\), \(1<p<\infty\),
\[
\|P_B\|=t^{-1}s^{1/p}\Big(\int m^{p'}\Big)^{1/p'}\le t^{-1/p}.
\tag{5}
\]
Here \(u^r\le u\) on \([0,1]\) for \(r>1\), and \(s\le1\). For \((p,q)=(1,\infty)\) and \((\infty,1)\), (1) gives the exact fixed-set formula
\[
\|P_B\|=\frac{sh}{t}\le\frac1t.
\tag{6}
\]
For \((1,1)\) and \((\infty,\infty)\), the products in (1) equal \(t\) for every \(B\). These inequalities give the asserted upper bounds.

**Step 3: sharpness and corner attainment.** Fix \(0<t<1\). For (2) and (3), use the two-height section profile
\[
m_\varepsilon(x)=\begin{cases}1&0\le x<\varepsilon,\\ (t-\varepsilon)/(1-\varepsilon)&\varepsilon\le x\le1,\end{cases}
\qquad0<\varepsilon<t.
\]
It has mean \(t\), supremum \(1\), and \(\int m_\varepsilon^a\to t^a\) for every \(0<a<1\), so (2)–(3) approach equality. For (4)–(5), use
\[
n_\varepsilon(x)=\begin{cases}1&0\le x<t-\varepsilon,\\\varepsilon/(1-t+\varepsilon)&t-\varepsilon\le x\le1,\end{cases}
\qquad0<\varepsilon<t.
\]
This has mean \(t\), support of full outer measure, and \(\int n_\varepsilon^r\to t\) for \(r>1\). Thus (4)–(5) approach equality. In (6), choose any area-\(t\) profile with \(s=h=1\), for instance \(m=1\) on an interval of length \(a\in(0,t)\) and \(m=(t-a)/(1-a)>0\) elsewhere. This attains \(1/t\). The matching-exponent corners have norm \(1\) for every \(B\).

**Step 4: nonattainment.** Equality in (2) or (3) requires both \(h=1\) and equality in strict Jensen, forcing \(m=t\) almost everywhere. Since \(0<t<1\), these conditions conflict. Equality in (4) or (5) forces \(s=1\) and \(m\in\{0,1\}\) almost everywhere (because \(m^r=m\) only at the endpoints). Those conditions imply \(t=1\), again a contradiction. In (6), both factors are at most one, so the stated corner characterization is necessary and sufficient.

**Step 5: rigidity of near extremizers.** In (2) and (3), the ratio of the left side to its sharp bound is the product of two factors in \([0,1]\): a Jensen ratio and a power of \(h\). Convergence to one forces \(h\to1\) and \(\int m^a\to t^a\). By strict concavity, laws of \(m\in[0,1]\) with fixed mean \(t\) and near-maximal \(a\)-moment converge weakly to the point mass at \(t\); compactness and boundedness give \(\|m-t\|_1\to0\). The converse follows by continuity of \(u^a\) and the exact formulas. In (4) and (5), convergence is equivalent to \(s\to1\) and \(\int m^r\to t\) for the appropriate \(r>1\). On \([0,1]\), \(u-u^r\) and \(u(1-u)\) are comparable above and below by positive constants depending only on \(r\). Hence the latter moment condition is equivalent to \(\int m(1-m)\to0\), and the converse follows. This proves both equivalences.

## Verification

The proof uses exact norm identities and elementary one-variable inequalities for arbitrary measurable sections, not finite enumeration. A standalone supplementary script, `check_endpoints.py`, evaluates the exact indicator-norm formula on 3,000 random finite-grid profiles across all twelve boundary parameter pairs, probes eight two-height families approaching the claimed constants, and checks exact equality in the two opposite corners. The script's output is recorded in `VERIFICATION.md`; its finite probes are not used as proof for arbitrary measurable sets. The proof covers all \(t\in(0,1)\) and both real and complex scalars.

## Relationship to prior work

Krasikova–Popov–Randrianantoanina introduce uniformly bounded single-set averaging projections as an essential hypothesis for disjointness-preserving operator theorems on Köthe–Banach spaces [1, Definition 2.1], and discuss mixed \(L^p(L^q)\) spaces [1, §4]. Their results do not give sharp fixed-area endpoint projection norms or an extremizing-sequence classification. Lü–van Neerven [2, Examples 2.5–2.7] demonstrate noncontractive or unbounded conditional expectations on mixed-norm spaces for suitable sub-\(\sigma\)-algebras; their operators differ from the single-set rank-one projections treated here. An accessible comparison result computes sharp *small-area asymptotics* for this averaging problem with \(1<p,q<\infty\), but it does not include the endpoint exponents, all-area equality, or near-extremizer rigidity established here. The present theorem is therefore confined to these missing nonreflexive boundary cases.

## Limitations

This theorem does not determine the optimal \(K_{p,q}(t)\) for interior exponents, nor any general two-atom conditional-expectation norm. For the nonattaining pairs, \(K_{p,q}(t)\) is a supremum rather than a maximum. Originality relative to unindexed older treatments of endpoint mixed-norm indicator functions cannot be established exhaustively from the checked sources. The structural assertions are exact for the fixed-area sequences specified above; no stability rate is claimed.

## References

[1] I. Krasikova, M. Popov, B. Randrianantoanina, *Disjointness preserving operators on Köthe-Banach spaces*, arXiv:2611.08960v1, submitted 6 November 2026. https://arxiv.org/html/2611.08960v1

[2] Q. Lü and J. van Neerven, *On conditional expectations in \(L^p(\mu;L^q(\nu;X))\)*, *Positivity* **23** (2019), 11–19, published online 11 June 2018. https://doi.org/10.1007/s11117-018-0589-y
