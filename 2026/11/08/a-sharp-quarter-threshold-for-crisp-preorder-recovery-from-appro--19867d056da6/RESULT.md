# A sharp quarter-threshold for crisp preorder recovery from approximate Łukasiewicz modal S4

## Finding

On any nonempty **finite** world set \(W\), let \(R:W\times W\to[0,1]\) be a fuzzy accessibility relation. Interpret \(\Box\) by the standard Łukasiewicz residuated Kripke operation, and let \(\delta_K,\delta_T,\delta_4\) be the largest truth-value deficits of the modal axioms \(K,T,4\), respectively, over every world and every valuation. Put \(\Delta(R)=\max\{\delta_K,\delta_T,\delta_4\}\). Then

\[
\begin{aligned}
\delta_K(R)&=\max_{u,v\in W}\min\{R(u,v),1-R(u,v)\},\\
\delta_T(R)&=\max_{u\in W}(1-R(u,u)),\\
\delta_4(R)&=\max_{u,v,z\in W}\bigl(R(u,v)\odot R(v,z)-R(u,z)\bigr)_+.
\end{aligned}
\]

Let \(\mathcal P_W\) denote the reflexive transitive Boolean relations on \(W\) and let \(d_\infty(R,\mathcal P_W)\) be their smallest entrywise uniform distance from \(R\). Always \(\Delta(R)\le d_\infty(R,\mathcal P_W)\). More strongly, if \(\Delta(R)<1/4\), then rounding every entry at \(1/2\) produces the **unique nearest crisp preorder** \(P\), and

\[
\boxed{d_\infty(R,\mathcal P_W)=\Delta(R)=\delta_K(R).}
\]

The strict threshold is optimal: a three-world fuzzy frame has \(\Delta=1/4\), nontransitive nearest Boolean rounding, and \(d_\infty=3/4\).

## Assumptions and scope

Use the standard algebra on \([0,1]\): \(a\odot b=\max(0,a+b-1)\), \(a\Rightarrow b=\min(1,1-a+b)\), and \((x)_+=\max(0,x)\). For \(p:W\to[0,1]\), define

\[
(\Box_Rp)(u)=\min_{v\in W}\bigl(R(u,v)\Rightarrow p(v)\bigr).
\]

The three schema instances are \(K:\Box(p\Rightarrow q)\Rightarrow(\Box p\Rightarrow\Box q)\), \(T:\Box p\Rightarrow p\), and \(4:\Box p\Rightarrow\Box\Box p\). For each, \(\delta\) is \(1\) minus the infimum of the formula's value over all interpretations of its propositional variables and all worlds. No discreteness of truth values is assumed. The result concerns these three individual schema deficits, not arbitrary formulas in S4 or arbitrary fuzzy topological interior operators. A crisp preorder means a reflexive and transitive relation, without antisymmetry.

## Proof

**Exact normality deficit.** For each fuzzy predicate \(a\), set \(D_Ra(u)=\max_v(R(u,v)-a(v))_+\). Then \(\Box_Ra=1-D_Ra\). The deficit of \(K\) at \(u\) is

\[
\bigl(D_Rq(u)-D_Rp(u)-D_R(p\Rightarrow q)(u)\bigr)_+.
\]

Choose an index \(v\) maximizing \(D_Rq(u)\), and abbreviate \(r=R(u,v)\), \(h=(p(v)-q(v))_+\). Since

\[
(r-q(v))_+-(r-p(v))_+\le\min\{h,r\},
\quad
(r-(p(v)\Rightarrow q(v)))_+=(h-(1-r))_+,
\]

this deficit is at most \(\min\{h,r\}-(h-(1-r))_+\le\min\{r,1-r\}\), and hence no more than the displayed maximum. Conversely, choose an entry \(r\) attaining that maximum, put \(q(v)=0\), \(p(v)=\min\{r,1-r\}\), and put \(p=q=1\) elsewhere. The resulting deficit at \(u\) is exactly \(\min\{r,1-r\}\). Thus the normality identity holds even for non-reflexive, non-transitive \(R\).

**Exact reflexivity deficit.** Since \(\Box_Rp(u)\le R(u,u)\Rightarrow p(u)\), the deficit of \(T\) is at most \(1-R(u,u)\). Set \(p(u)=0\) and \(p(v)=1\) at all other worlds to attain equality. Maximize over \(u\).

**Exact transitivity deficit.** Define the max–Łukasiewicz composite \(S(u,z)=\max_v(R(u,v)\odot R(v,z))\). By residuation and finite interchange of minima, \(\Box_R\Box_Rp=\Box_Sp\). Hence the deficit of \(4\) at \(u\) is \((D_Sp(u)-D_Rp(u))_+\), which is at most \(\max_z(S(u,z)-R(u,z))_+\). To attain the bound at \((u,z)\), set \(p(z)=R(u,z)\) and \(p(y)=1\) for every other \(y\). This yields the displayed identity for \(\delta_4\).

**Distance lower bound.** Fix a crisp preorder \(Q\) at uniform distance at most \(\eta\) from \(R\). Every entry of \(R\) lies within \(\eta\) of an endpoint, so \(\delta_K\le\eta\). Reflexivity of \(Q\) gives \(\delta_T\le\eta\). If \(Q(u,v)=Q(v,z)=1\), transitivity forces \(Q(u,z)=1\) and the \(4\)-defect at \((u,v,z)\) is at most \(\eta\). If either of those two edges of \(Q\) equals zero, its corresponding fuzzy weight is at most \(\eta\), so their Łukasiewicz product is at most \(\eta\). Thus \(\delta_4\le\eta\), and infimizing gives \(\Delta(R)\le d_\infty(R,\mathcal P_W)\).

**Recovery below a quarter.** Write \(e=\Delta(R)<1/4\). By the normality identity, every matrix entry belongs to \([0,e]\cup[1-e,1]\). Its uniquely closest Boolean value is therefore \(P(u,v)=1\) when \(R(u,v)>1/2\), and \(0\) otherwise; the resulting uniform error is exactly \(\delta_K\). By the \(T\) identity, \(R(u,u)\ge1-e>e\), so \(P\) is reflexive. If \(P(u,v)=P(v,z)=1\), then

\[
R(u,z)\ge R(u,v)\odot R(v,z)-e\ge1-3e>e.
\]

As \(R(u,z)\) is in the two endpoint bands, this forces \(P(u,z)=1\), proving transitivity. Since \(e<1/4\), every entry has a strictly nearer Boolean endpoint, so this is also the unique closest crisp relation and hence the unique closest crisp preorder. Its distance equals \(\delta_K\), while the global lower bound gives \(e\le\delta_K\le e\).

**Sharpness.** On \(W=\{1,2,3\}\), use

\[
R=\begin{pmatrix}
1&3/4&1/4\\
0&1&3/4\\
0&0&1
\end{pmatrix}.
\]

The exact identities give \((\delta_K,\delta_T,\delta_4)=(1/4,0,1/4)\). Nearest Boolean rounding retains \(1\to2\) and \(2\to3\) but not \(1\to3\), so it is not transitive. Every transitive Boolean relation must either insert \(1\to3\) or remove an edge on this two-step path, creating an error of at least \(3/4\). Either modification yields a reflexive transitive Boolean relation with error exactly \(3/4\). Thus the strict constant \(1/4\) cannot be increased under the stated hypothesis.

## Verification

The included `checker.py` uses exact integer arithmetic on finite truth grids. It exhaustively compares every valuation-based \(K,T,4\) deficit against the three closed formulas for all one- and two-world matrices on a five-point grid (\(5\) and \(625\) frames). It also tests \(60\) seeded three-world matrices, compares \(350\) seeded perturbations of all \(29\) three-world crisp preorders using an eighth-grid, and checks the exact boundary example against every three-world crisp preorder. It exits with `QUANTITATIVE_S4_ALL_CHECKS_OK`. These finite tests are supplementary; the proof above covers every finite cardinality and every real-valued frame.

## Relationship to prior work

Khan, Martins, Madeira, and Zaman (public preprint October 29, 2026) develop Łukasiewicz fuzzy topological semantics and a Kripke-to-topological correspondence with S4 principles. The present result works directly with arbitrary finite fuzzy accessibility matrices and quantifies the **degree** to which \(K,T,4\) fail, proving a sharp recovery threshold to a crisp preorder. Bou, Cerami, and Esteva discuss the necessity of crisp restrictions for familiar modal properties; that qualitative observation is not claimed as new. Work by Vidal concerns transitive many-valued modal logics and decidability. Fuzzy-preorder discretization by Boixader and Recasens is closely related in subject, but available bibliographic abstracts do not resolve whether it contains this particular quantitative modal stability theorem; this remains an explicit priority risk.

## Limitations

Only finite nonempty frames, standard real-valued Łukasiewicz residuation, the three specific axiom schemes, and uniform matrix distance are treated. The theorem does not establish that arbitrary fuzzy-topological S4 operators satisfy the same formulas, nor does it classify all modal axioms. The finite checker does not certify infinite quantifiers. Specialist papers on fuzzy-preorder discretization were not all accessible in full, so originality is assessed against inspected evidence rather than asserted as absolute priority. An independent mathematical audit has not been performed.

## References

1. M. A. Khan, M. A. Martins, A. Madeira, B. Zaman, *On Łukasiewicz Topological Semantics*, arXiv:2610.40809, publicly posted October 29, 2026, https://arxiv.org/abs/2610.40809.
2. F. Bou, M. Cerami, F. Esteva, *Finite-Valued Łukasiewicz Modal Logic Is PSPACE-Complete*, IJCAI 2011, https://www.ijcai.org/Proceedings/11/Papers/064.pdf.
3. A. Vidal, *On Transitive Modal Many-Valued Logics*, arXiv:1904.01407, https://arxiv.org/abs/1904.01407.
4. D. Boixader, J. Recasens, *Discretization of Fuzzy Transitive Relations*, FUZZ-IEEE 2011, DOI:10.1109/FUZZY.2011.6007635 (bibliographic abstract inspected, full text unavailable).
5. D. Boixader, J. Recasens, *Transitive Openings*, EUSFLAT 2011, DOI:10.2991/eusflat.2011.104 (open abstract inspected).
