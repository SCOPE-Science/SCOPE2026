# Exact three-language approximation gap for strong fuzzy disjunction

## Finding
For every integer \(n\ge 2\), let \(F_n(x_1,\ldots,x_n)=\min\{1,\sum_{i=1}^n x_i\}\) on \([0,1]^n\), the Łukasiewicz strong disjunction of \(n\) propositional variables. Among formulas interpreted in *all pointed fuzzy Kripke models* with the Zadeh propositional basis and its usual fuzzy diamond, the sharp worst-case uniform error in approximating \(F_n\) is
\[
 E_{\mathrm Z}(n)=1-\frac1n.
\]
Among formulas in the non-expansive fuzzy modal language (admitting rational truncated shifts), the sharp error is
\[
 E_{\mathrm{NE}}(n)=\frac12\left(1-\frac1n\right).
\]
The bounds are attained by the propositional formulas \(G_{\mathrm Z}=p_1\vee\cdots\vee p_n\) and \(G_{\mathrm{NE}}=(p_1\vee\cdots\vee p_n)\oplus\frac{n-1}{2n}\), respectively, where \(a\oplus c=\min\{a+c,1\}\). The full Łukasiewicz language expresses \(F_n\) exactly (error zero). Thus allowing arbitrarily deep fuzzy modalities does not improve the worst-case approximation in either restricted language.

Furthermore, for any optimal non-expansive formula \(G\), its value \(g(t)\) on the one-world model with every \(p_i\) valued \(t\) and loop weight one satisfies the rigid identity \(g(t)=t+(n-1)/(2n)\) for every \(0\le t\le1/n\).

## Assumptions and scope
Models are \(\mathcal M=(W,R,V)\), with \(W\ne\varnothing\), \(R:W\times W\to[0,1]\), and \(V(p_i,w)\in[0,1]\) free and independent. The modal diamond has value \(\sup_{v\in W}\min\{R(w,v),V(\varphi,v)\}\). All errors are suprema over every model, world, and assignment; evaluation of \(F_n\) uses the \(n\) atomic truth values at that world. Only the indicated atoms are used in comparison formulas.

The **plain Zadeh language** is generated from the atoms, \(0,1\), min/max, involutive negation \(1-a\), and the diamond; no intermediate truth constants or truncated shifts are allowed. The **non-expansive language** adds rational truth constants and truncated shifts \(a\mapsto\max\{a-c,0\}\), equivalently \(a\mapsto\min\{a+c,1\}\), with the same modal semantics. The target \(F_n\) is the strong disjunction connective of the full Łukasiewicz propositional language. These explicit language choices are essential: adding truth constants changes the plain-Zadeh statement.

## Proof
Put \(M(x)=\max_i x_i\), \(S(x)=\sum_i x_i\), and \(d_n=1-1/n\). On every \(x\in[0,1]^n\),
\[
0\le F_n(x)-M(x)\le d_n.
\]
Indeed, when \(S\le1\), \(F_n-M=S-M\le S(1-1/n)\le d_n\), since \(M\ge S/n\); when \(S\ge1\), \(F_n-M=1-M\le d_n\), since \(M\ge S/n\ge1/n\). Thus \(M\) gives Zadeh error at most \(d_n\). With \(c_n=d_n/2\), let \(H(x)=\min\{M(x)+c_n,1\}\). When \(M+c_n\le1\), \(|H-F_n|=|c_n-(F_n-M)|\le c_n\); otherwise \(|H-F_n|=1-F_n\le1-M<c_n\). This proves the claimed constructive upper bounds at every pointed model, without any restriction on modal accessibility.

For the non-expansive lower bound, consider a single world \(w\) with \(R(w,w)=1\), so \(\Diamond\) is the identity operator. Every formula of the non-expansive language now induces a map \(g:[0,1]^n\to[0,1]\) that is \(1\)-Lipschitz for the sup norm. This is by structural induction: atoms, constants, negation, min, max, and unary truncated shifts are all \(1\)-Lipschitz, and the diamond is the identity. At \(a=(0,\ldots,0)\) and \(b=(1/n,\ldots,1/n)\), one has \(F_n(a)=0\), \(F_n(b)=1\), and \(\|a-b\|_\infty=1/n\). If \(g\) has uniform error \(e\), then \(1\le2e+1/n\), so \(e\ge c_n\). If equality holds, all inequalities at the endpoints are equalities, implying \(g(a)=c_n\), \(g(b)=1-c_n\). For \(0\le t\le1/n\), the two Lipschitz inequalities against \(a,b\) force \(g(t,\ldots,t)=t+c_n\). This proves rigidity as well.

For the Zadeh lower bound, restrict again to the one-world reflexive model. On the diagonal \((t,\ldots,t)\) with \(0<t<1/2\), every Zadeh formula is, identically throughout that interval, exactly one of the four functions \(0,t,1-t,1\). This follows by induction from the fixed strict order \(0<t<1-t<1\); negation permutes the four choices and min/max always select one, while the diamond remains the identity. At \(t=0\), its value is either \(0\) or \(1\). A formula whose error is strictly below \(d_n<1\) must therefore have value \(0\) at \(t=0\), and continuity implies that its branch on \((0,1/2)\) is \(0\) or \(t\). When \(n>2\), take \(t=1/n<1/2\): the target is \(1\), but the formula has value at most \(1/n\), giving error at least \(d_n\). When \(n=2\), let \(t\uparrow1/2\): continuity yields formula value at most \(1/2\), while the target tends to \(1\), giving error at least \(d_2=1/2\). This contradiction proves the sharp Zadeh lower bound for all \(n\ge2\). Finally, full Łukasiewicz disjunction is by definition the target connective, so its approximation error is zero.

## Verification
The inequalities and the lower bounds above are analytic, covering all integers \(n\ge2\), all formula depths, and every fuzzy Kripke model. The standalone `checker.py` evaluates the two proposed approximants on rational grids for small \(n\) and checks the pair of endpoint certificates; finite grids are corroboration only, not the proof of the unrestricted theorem. Run `python checker.py` with Python 3, with no third-party dependencies.

## Relationship to prior work
Gebhart–Schröder–Wild (2026) formulate the three propositional bases and prove uniform interpolation for the non-expansive fuzzy modal language; they do not give a minimax error profile for an excluded \(n\)-ary Łukasiewicz connective. Gebhart–Schröder–Wild (2025) introduce non-expansive fuzzy description logic and discuss the expressive/complexity tradeoff, rather than these sharp numerical approximation thresholds. The present calculation supplements the qualitative language comparison with precise best errors and an equality-rigidity statement. General Lipschitz endpoint arguments are classical ingredients; originality is claimed only for this combined exact modal-language minimax classification, not for the elementary inequality in isolation.

## Limitations
The result concerns the specified min/max/negation and truncated-shift languages over unrestricted fuzzy Kripke models. It is not an approximation theorem for other t-norm modalities, restricted model classes, added truth constants in plain Zadeh, or any metric weaker than the supremum over all models. The evidence does not establish historical uniqueness in unindexed literature; a related general approximation theorem could imply some part of the sharp constants. No independent audit has been performed.

## References
1. Stefan Gebhart, Lutz Schröder and Paul Wild, *Non-Expansive Fuzzy Modal Logic Has Uniform Interpolation*, arXiv:2610.32335v1 (first public 2026-10-23). https://arxiv.org/html/2610.32335v1
2. Stefan Gebhart, Lutz Schröder and Paul Wild, *Non-expansive Fuzzy ALC*, arXiv:2505.09416v3 (2025). https://arxiv.org/html/2505.09416v3
