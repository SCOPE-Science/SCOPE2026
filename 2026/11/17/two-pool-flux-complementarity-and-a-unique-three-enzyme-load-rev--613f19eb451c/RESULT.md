# Two-pool flux complementarity and a unique three-enzyme load reversal in HMM cycles

## Finding
Consider a closed, directed substrate-transformation cycle in which each transformation is realized by a reversible-binding, irreversible-catalysis Henri–Michaelis–Menten (HMM) module. Hold the conserved total substrate amount \(T\) and all kinetic rate constants fixed, and regard distinct *total enzyme pools* \(E_a\) as independent parameters. The common stationary catalytic current \(J\) is a smooth, strictly increasing function of every \(E_a\).

**Two-pool theorem.** If exactly two nonempty enzyme pools catalyze all transformations (either pool may serve multiple reactions), then at every strictly positive stationary state
\[
\frac{\partial^2 J}{\partial E_1\,\partial E_2}>0.
\]
This strict additive complementarity is independent of the number of transformations, binding/unbinding constants, turnover constants, and how the transformations are assigned to these two pools.

**Sharp failure with three pools.** For a three-transformation cycle with three distinct enzymes, there are positive rational rates and fixed enzyme totals for which the same mixed response changes sign *exactly once* as the conserved substrate total \(T\) increases from zero to infinity. Specifically, set all catalytic and dissociation constants to \(1\), the three association constants to \((2,2,100)\), and the enzyme totals to \((3,3,11/10)\). There is exactly one \(T_*>0\) such that
\[
\frac{\partial^2 J}{\partial E_1\,\partial E_2}
\begin{cases}>0,&0<T<T_*,\\=0,&T=T_*,\\<0,&T>T_*.
\end{cases}
\]
Here \(T_*\approx4.03960898375\), specified exactly below as an algebraic function of the unique root of a degree-six polynomial in \((0,11/10)\). At \(T=23/12\) the mixed derivative is exactly \(71805312/33856161185>0\); at \(T=21/5\) it is \(-4675/1203052<0\). Therefore three is the smallest possible number of distinct enzyme pools for negative mixed stationary-flux curvature in this family. The three-pool example has a unique globally attracting equilibrium for every positive \(T\), so the reversal is not caused by a stability bifurcation.

## Assumptions and scope
Let \(m\ge2\) and let the substrates \(X_i\), indexed cyclically modulo \(m\), undergo \(X_i\to X_{i+1}\). Every step \(i\) uses precisely one enzyme pool \(a(i)\in\{1,\ldots,q\}\) in the mass-action reactions
\[
E_{a(i)}+X_i\mathrel{\mathop{\rightleftarrows}^{k_i^+}_{k_i^-}} C_i
\xrightarrow{k_i}E_{a(i)}+X_{i+1}.
\]
All \(k_i^+,k_i^-,k_i\) are strictly positive. Each pool catalyzes at least one step; pools are disjoint biochemical species, and distinct complexes \(C_i\) are retained even when their enzyme is shared. There are no input/output reactions and no enzyme-free steps. The total substrate is \(T=\sum_i(x_i+c_i)>0\), and enzyme totals are \(E_a=e_a+\sum_{i:a(i)=a}c_i>0\). The response derivatives vary the two named enzyme *totals* independently, holding all other enzyme totals, the substrate total and all rate constants fixed. They are not derivatives in the free-enzyme concentrations, catalytic rates, or a normalized genetic epistasis metric.

Define strictly positive constants
\[
\alpha=\sum_i\frac1{k_i},\quad
s_a=\sum_{i:a(i)=a}\frac1{k_i},\quad
b_a=\sum_{i:a(i)=a}\frac{k_i^-+k_i}{k_i^+k_i}.
\]
In particular \(\alpha=\sum_a s_a\). All statements concern the unique positive equilibrium within each positive compatibility class; no statement about transient enzyme-perturbation response is made.

## Proof
**1. Exact scalar stationary equation.** Conservation of each substrate plus the stationary complex balances forces the same positive catalytic flux through all steps, \(k_i c_i=J\). Thus \(c_i=J/k_i\), \(e_a=E_a-s_aJ\), and the binding balance gives
\[
x_i=\frac{k_i^-+k_i}{k_i^+k_i}\,\frac{J}{E_{a(i)}-s_{a(i)}J}.
\]
Consequently the unique equilibrium current is characterized by
\[
F(J;E,T)=\alpha J+\sum_{a=1}^{q}\frac{b_aJ}{E_a-s_aJ}-T=0,
\qquad 0<J<\min_a E_a/s_a. \tag{1}
\]
Conversely every root in this interval determines strictly positive substrate, enzyme and complex concentrations satisfying all mass-action balances and conserved totals. The left-hand side is continuous and strictly increasing in \(J\), begins at \(-T\), and diverges to \(+\infty\) at the first enzyme-capacity boundary. It therefore has exactly one root. Set \(u_a=E_a-s_aJ\) and
\[
H=F_J=\alpha+\sum_a\frac{b_a E_a}{u_a^2}>0,\qquad
K=F_{JJ}=\sum_a\frac{2b_a s_aE_a}{u_a^3}>0.\tag{2}
\]
The implicit-function theorem gives smoothness and \(J_{E_a}=b_aJ/(u_a^2H)>0\).

**2. Mixed curvature formula.** For distinct pools \(a\ne b\), differentiating (1) twice and simplifying yields the exact identity
\[
J_{E_aE_b}=J_{E_a}J_{E_b}
\left[\frac{E_a+s_aJ}{Ju_a}+\frac{E_b+s_bJ}{Ju_b}-\frac{K}{H}\right].\tag{3}
\]
The bracket is equivalently \(2/J+2s_a/u_a+2s_b/u_b-K/H\). By (2), \(K/H\) is a weighted average of the numbers \(0,2s_1/u_1,\ldots,2s_q/u_q\), with strictly positive weights proportional to \(\alpha\) and \(b_c E_c/u_c^2\). If \(q=2\), the weighted average is strictly less than \(\max(2s_1/u_1,2s_2/u_2)\), whereas the two other summands in (3) exceed this maximum. Hence the bracket is strictly positive everywhere: the two-pool result follows.

**3. An exact three-pool example.** Take \(m=q=3\), \(a(i)=i\), \(k_i=k_i^-=1\), \((k_1^+,k_2^+,k_3^+)=(2,2,100)\), and \((E_1,E_2,E_3)=(3,3,11/10)\). Then \(\alpha=3\), \(s_a=1\), \((b_1,b_2,b_3)=(1,1,1/50)\). Write \(j\) for the current. Equation (1) becomes
\[
T=\Phi(j)=3j+\frac{2j}{3-j}+\frac{j}{50(11/10-j)},
\qquad 0<j<11/10.\tag{4}
\]
Since \(\Phi\) is strictly increasing from \(0\) to infinity, classifying mixed curvature as a function of \(j\) is equivalent to classifying it as a function of \(T\). For the two named pools, the bracket from (3) simplifies to
\[
B(j)=\frac2j+\frac4{3-j}-\frac{H'(j)}{H(j)}
=\frac{-2P(j)}{j(j-3)(10j-11)Q(j)},\tag{5}
\]
where
\[
\begin{aligned}
P(j)={}&7500j^6-47250j^5+33975j^4+378862j^3\\
&-1033626j^2+991782j-331056,\\
Q(j)={}&750j^4-6150j^3+19063j^2-23628j+10032.
\end{aligned}
\]
Equation (2) gives \(H=2Q(j)/[5(j-3)^2(10j-11)^2]\), so \(Q(j)>0\) throughout the interval; both remaining linear factors in the denominator of (5) are negative. Therefore the sign of \(B\) is the negative of the sign of \(P\). Put \(j=11t/[10(1+t)]\) with \(t>0\). Direct exact expansion yields
\[
\begin{aligned}
&[10(1+t)]^6 P\!\left(\frac{11t}{10(1+t)}\right)\\
&\quad=60500\left(6859t^6+31407t^5+35967t^4-3471116t^3\\
&\qquad\qquad-12590520t^2-14799600t-5472000\right).\tag{6}
\end{aligned}
\]
The polynomial on the right has precisely one sign change in descending coefficients, has negative constant term and positive leading coefficient, so Descartes' rule of signs together with continuity gives exactly one positive root. Thus \(P\) has exactly one root \(j_*\) on \((0,11/10)\). Since \(P(0)<0\) and \(P\) is eventually positive within the interval, the sign of (3) changes exactly once, from positive to negative. The unique substrate threshold is \(T_*=\Phi(j_*)\), where \(j_*\approx0.97425729654908\).

For two explicit checks, \(j=1/2\) gives \(T=23/12\) and \(J_{E_1E_2}=71805312/33856161185>0\), whereas \(j=1\) gives \(T=21/5\) and \(J_{E_1E_2}=-4675/1203052<0\). At both equilibria, the complex concentrations are \(c_i=j\), the free enzymes are \(e_i=E_i-j\), and substrates are \((j/(3-j),j/(3-j),j/[50(11/10-j)])\); these are strictly positive and satisfy all mass-action balances. The source's global-convergence theorem for distinct-enzyme transformation cycles applies in this example; there is no instability condition or Hopf mechanism involved.

## Verification
Run `python3 check.py` from the same directory as this file. The checker uses Python's exact rational arithmetic to verify both steady states and their mass-action balances, the two exact mixed derivatives, and the entire transformed polynomial identity (6). It also checks two illustrative positive two-pool examples, which are not a substitute for the general proof in step 2. Approximate values of \(j_*\) and \(T_*\) are descriptive only: uniqueness and signs follow from exact inequalities and polynomial coefficients.

## Relationship to prior work
Joshi and Nguyen (2026), *Substrate hypergraph cycles: unique steady states and persistence for every enzyme assignment; oscillations enabled by enzyme sharing*, prove unique positive equilibria, persistence and global convergence when each step has a distinct catalyst, and shared-enzyme Hopf examples. This paper supplies the reaction mechanism and equilibrium-throughput setting; its theorems do **not** state the mixed enzyme-total derivative sign, the sharp two-pool boundary, or the three-pool load-reversal polynomial. Classical second-order metabolic control analysis (Höfer and Heinrich, 1993) provides general perturbation machinery without the present HMM-cycle-specific sign classification. Kryazhimskiy (2021) investigates epistasis under first-order kinetic metabolic modules and a normalized mutational epistasis notion, not the mixed derivative of current with respect to conserved enzyme totals in a closed HMM cycle. Noor and Liebermeister (2024) study optimal enzyme *allocation* in unbranched pathways and first-order control coefficients, not this fixed-total-substrate mixed-curvature transition.

## Limitations
The result applies to transformation cycles with one-intermediate HMM kinetics and *positive* association, dissociation and catalytic rates, not arbitrary substrate hypergraphs, enzyme-free steps, product inhibition, or open pathways. It concerns additive cross curvature in two enzyme totals; alternative definitions of genetic epistasis can assign a different sign. The theorem does not claim a general classification of the mixed sign for all three-pool parameters, nor any transient effect. Closely related older metabolic-control analyses and unindexed computations might contain an equivalent special-case calculation; independent literature and mathematical review remain outstanding.

## References
1. B. Joshi and T. D. Nguyen, *Substrate hypergraph cycles: unique steady states and persistence for every enzyme assignment; oscillations enabled by enzyme sharing*, arXiv:2611.02523v1 (first public 2026-11-02), https://arxiv.org/html/2611.02523v1 . Sections 3, 5–7 and 9.
2. T. Höfer and R. Heinrich, *A second-order approach to metabolic control analysis*, Journal of Theoretical Biology 164 (1993), 85–102, DOI:10.1006/jtbi.1993.1141.
3. S. Kryazhimskiy, *Emergence and propagation of epistasis in metabolic networks*, eLife 10 (2021), e60200, DOI:10.7554/eLife.60200, https://elifesciences.org/articles/60200 .
4. E. Noor and W. Liebermeister, *Optimal enzyme profiles in unbranched metabolic pathways*, Interface Focus 14 (2024), 20230029, DOI:10.1098/rsfs.2023.0029, https://pmc.ncbi.nlm.nih.gov/articles/PMC10853694/ .
