# Monoidal completion of Łukasiewicz Kripke topologies: one-cut collapse and sharp modal distortion

## Finding

Let \(W\ne\varnothing\) be any set and \(R:W\times W\to[0,1]\) a reflexive, Łukasiewicz-transitive relation. Put \(a\odot b=\max\{0,a+b-1\}\) and
\[
\tau_R=\{f\in[0,1]^W:\ R(x,y)\odot f(x)\le f(y)\quad(x,y\in W)\}.
\]
Let the **unit-degree skeleton** be the crisp relation \(S(x,y)=1\) exactly when \(R(x,y)=1\), and \(S(x,y)=0\) otherwise. Let \(\mathfrak A_R\) denote the least family containing \(\tau_R\) and closed under arbitrary pointwise suprema, arbitrary pointwise infima, and pointwise \(\odot\). Then
\[
\boxed{\mathfrak A_R=\tau_S=\{f\in[0,1]^W:S(x,y)=1\Rightarrow f(x)\le f(y)\}.}
\]
In particular, all strictly intermediate accessibility degrees disappear when the induced fuzzy Alexandroff topology is completed under strong conjunction.

Define the associated necessity interiors
\[
\Box_R f(x)=\inf_{y\in W}\min\{1,1-R(x,y)+f(y)\},\qquad
\Box_S f(x)=\inf_{y:S(x,y)=1}f(y).
\]
The worst possible pointwise change is **exactly**
\[
\boxed{\sup_{f\in[0,1]^W}\ \sup_{x\in W}(\Box_S f(x)-\Box_R f(x))
=\sup\{R(x,y):x,y\in W,\ R(x,y)<1\},}
\]
where the supremum of the empty set on the right is defined as zero. Thus a relation with an almost-unit fractional edge can undergo an almost-unit change in necessity under monoidal completion.

For finite \(W\), arbitrary-infimum closure is **unnecessary**: closure under arbitrary suprema, finite infima, and \(\odot\) already yields \(\tau_S\). More generally this holds on any \(W\) if the nonunit degrees have a uniform gap below one. Set \(\rho=\sup(\{R(x,y):R(x,y)<1\}\cup\{0\})\); if \(\rho<1\), then the exact least common exponent that turns every row \(R(x,\cdot)\) into its unit-cut indicator is
\[
\boxed{N(R)=\max\{1,\lceil(1-\rho)^{-1}\rceil\}.}
\]
For values in the finite Łukasiewicz chain \(\{0,1/m,\ldots,1\}\), the uniform bound is \(N(R)\le m\), and the bound \(m\) is attainable for every \(m\ge2\).

The finiteness/uniform-gap qualification is real. On a countable reflexive-transitive fuzzy frame with edge degrees accumulating at one, closure under arbitrary suprema, finite infima, and \(\odot\) can be **strictly smaller** than \(\tau_S\), although adding arbitrary infima restores equality.

## Assumptions and scope

All function spaces and topological completions use the full real truth-value interval \([0,1]\), except that a finite rational grid is explicitly invoked for the finite-chain cutoff and checker. The closure operator for \(\mathfrak A_R\) is closure of a *family of fuzzy opens*, not the pointwise fuzzy-set closure operator. An Alexandroff topology here means closure under arbitrary pointwise infima as well as arbitrary pointwise suprema. A monoidal Chang topology requires only arbitrary suprema, finite infima, and pointwise strong conjunction. No symmetry or finiteness is assumed in the first two boxed identities. \(\tau_R\) contains every constant fuzzy function.

## Proof

**The unit-cut bound.** If \(S(x,y)=1\), then \(R(x,y)=1\), so every \(f\in\tau_R\) satisfies \(f(x)\le f(y)\). Thus \(\tau_R\subseteq\tau_S\). The unit-degree cut \(S\) is reflexive and transitive: whenever \(S(x,y)=S(y,z)=1\), Łukasiewicz transitivity forces \(1=1\odot1\le R(x,z)\). Consequently \(\tau_S\) is the family of \(S\)-upward fuzzy functions and is closed under arbitrary suprema, arbitrary infima, and pointwise \(\odot\). Therefore \(\mathfrak A_R\subseteq\tau_S\).

**Rows and nilpotent powers.** For each \(x\in W\), the row \(r_x(y)=R(x,y)\) belongs to \(\tau_R\): the required inequality \(R(y,z)\odot R(x,y)\le R(x,z)\) is transitivity. By associativity of strong conjunction, its \(n\)-fold power satisfies
\[
r_x^{\odot n}(y)=\max\{0,1-n(1-R(x,y))\}\quad(n\ge1).
\]
Hence its infimum over all positive integers \(n\) is \(\chi_{S[x]}\), the characteristic fuzzy function of the principal unit-cut upset \(S[x]=\{y:R(x,y)=1\}\). Thus every such characteristic function lies in \(\mathfrak A_R\). This is the step requiring arbitrary infima in an unrestricted infinite frame.

**Reconstruction by joins.** Every constant fuzzy function \(c_W\) is in \(\tau_R\), because \(R(x,y)\odot c\le c\). Given \(f\in\tau_S\), the following identity holds pointwise:
\[
f(y)=\bigvee_{x\in W}\big(f(x)_W\odot\chi_{S[x]}\big)(y).
\]
The right-hand side is at least \(f(y)\), taking \(x=y\); and it is at most \(f(y)\), since \(S(x,y)=1\) implies \(f(x)\le f(y)\). The right-hand side therefore belongs to \(\mathfrak A_R\). This proves \(\mathfrak A_R=\tau_S\).

**Finite generation and sharp power cutoff.** When \(\rho<1\), choose \(N=\lceil(1-\rho)^{-1}\rceil\), with \(N=1\) if all degrees equal one. For every \(R(x,y)<1\), \(N(1-R(x,y))\ge1\), so \(r_x^{\odot N}=\chi_{S[x]}\); no arbitrary infimum is required. For any integer \(k<N\), one has \(k(1-\rho)<1\), so by the supremum property some nonunit edge has \(R(x,y)>1-1/k\) and its \(k\)-th row power remains positive at \(y\). This proves leastness even if the supremum is not attained. For finite \(W\), a largest nonunit degree exists (or none does), and hence \(\rho<1\). For grid degree \(1-1/m\), the \((m-1)\)-st power remains positive at that edge but the \(m\)-th vanishes. A reflexive two-world frame with one such directed edge and reverse edge zero realizes sharpness.

**Exact modal distortion.** Pointwise \(\Box_R f(x)\le\Box_S f(x)\), since the infimum for \(R\) includes every unit-cut successor with term \(f(y)\). Put \(\rho\) as above. Every term belonging to a nonunit edge satisfies \(R(x,y)\Rightarrow f(y)\ge1-R(x,y)\ge1-\rho\). Thus
\[
\Box_R f(x)\ge \min\{\Box_S f(x),1-\rho\},\quad
0\le\Box_S f(x)-\Box_R f(x)\le\rho.
\]
For any chosen pair \((x,y)\) with \(R(x,y)<1\), take \(f(y)=0\) and \(f(z)=1\) for all \(z\ne y\). Since \(y\) is not a unit-cut successor of \(x\), one has \(\Box_S f(x)=1\), but \(\Box_R f(x)=1-R(x,y)\); the difference is exactly \(R(x,y)\). Taking the supremum over these pairs proves the second boxed identity, including nonattained suprema and the empty-set case.

**Why infinite ordinary monoidal completion may be smaller.** Let \(W=\{o\}\cup\{v_n:n\ge2\}\). Put \(R(z,z)=1\), \(R(o,v_n)=1-1/n\), and every other off-diagonal degree zero. This relation is Łukasiewicz-transitive: its only positive off-diagonal edges leave \(o\), and all their nontrivial extensions have degree zero. Its unit-cut relation \(S\) is the identity, so \(\tau_S=[0,1]^W\). Every \(f\in\tau_R\) obeys \(f(v_n)\ge\max\{0,f(o)-1/n\}\), hence
\[
\liminf_{n\to\infty}f(v_n)\ge f(o).
\]
The family \(\mathcal P\) of functions satisfying this inequality is closed under arbitrary pointwise suprema, finite pointwise infima, and pointwise \(\odot\): use \(\liminf\sup_i a_{i,n}\ge\sup_i\liminf a_{i,n}\), finite minimum, and continuity/monotonicity of strong conjunction. Thus the ordinary monoidal Chang closure of \(\tau_R\) lies in \(\mathcal P\). But \(\chi_{\{o\}}\in\tau_S\) violates this inequality. Hence ordinary monoidal completion is proper; arbitrary-infimum closure, by the first result, recovers all of \(\tau_S\).

## Verification

The supplementary standalone Python 3 checker `verify_monoidal_completion.py` uses exact integer-grid arithmetic to enumerate all reflexive Łukasiewicz-transitive labeled frames on the indicated small finite grids. It independently forms the induced fuzzy opens, saturates under strong conjunction and finite lattice operations, compares the result with the unit-cut upward family, and exhaustively maximizes the interior difference over all grid valuations. It checks one-world Boolean frames, two-world grids with denominators one through four, and three-world grids with denominators two and three; the complete three-world scans contain respectively 281 and 1,490 frames. It also checks sharp row-power cutoffs for denominators two through nineteen. All checks passed. The proof above covers arbitrary real degrees and infinite world sets; finite enumeration is supporting evidence, not an infinite proof.

## Relationship to prior work

Khan, Martins, Madeira, and Zaman (arXiv:2610.40809, publicly posted October 29, 2026) define \(\tau_R\), prove it is a fuzzy Alexandroff topology and identify its modal interior. They separately explain why monoidal closure is required for Łukasiewicz-normal topological semantics. The present result determines the **least** such monoidal extension when arbitrary infima are preserved, with a constructive representation and exact modal price. Neither a bare correspondence between fuzzy preorders and fuzzy topologies nor the ordinary crisp-preorder/Alexandrov correspondence by itself specifies this generated extension.

Fang (2007), Lai and Zhang (2006), and the 2014 fuzzy-approximation-space work establish broader fuzzy-preorder/topology correspondences but do not in the inspected material identify the specific strong-conjunction closure of \(\tau_R\) with its unit-degree cut or quantify the modal distortion. Kim and Kim (2026) develop general residuated-lattice Alexandrov pretopological constructions; full article access was constrained in this comparison, so an unrecognized stronger result there remains a priority risk. An indexed mathematical record on ordinal regradings of Gödel frames concerns the **idempotent** Gödel conjunction and does not imply the nilpotent Łukasiewicz power construction here.

## Limitations

The finite power cutoff requires a uniform gap below one; the countable example proves it cannot be dropped for the completion using only finite infima. The complete-Alexandroff monoidal extension theorem does not say that the original fuzzy \(\tau_R\) is monoidal, nor that its modal semantics remains unchanged after completion. The cutoff is the least common exponent for *the particular row-power construction*, not a claimed optimal complexity bound for all possible generating expressions. The checker samples every finite-grid frame only within its explicitly stated bounds. Literature search is not proof of global historical priority; independent audit has not been performed.

## References

1. M. A. Khan, M. A. Martins, A. Madeira, B. Zaman, *On Łukasiewicz Topological Semantics*, arXiv:2610.40809 (public version October 29, 2026), https://arxiv.org/abs/2610.40809 . See Definitions 14–17 and Propositions 1–4.
2. J. Fang, *I-fuzzy Alexandrov topologies and specialization orders*, Fuzzy Sets and Systems 158 (2007), 2359–2374, https://doi.org/10.1016/j.fss.2007.05.001 .
3. H. Lai, D. Zhang, *Fuzzy preorder and fuzzy topology*, Fuzzy Sets and Systems 157 (2006), 1865–1885, https://doi.org/10.1016/j.fss.2006.02.013 .
4. *Fuzzy Approximating Spaces*, Journal of Applied Mathematics (2014), article 405802, https://doi.org/10.1155/2014/405802 .
5. Y. C. Kim, Y.-H. Kim, *Topological Structures of Fuzzy Modal Logics Based on Residuated Lattices*, Mathematics 14 (2026), 2332, https://doi.org/10.3390/math14132332 .
