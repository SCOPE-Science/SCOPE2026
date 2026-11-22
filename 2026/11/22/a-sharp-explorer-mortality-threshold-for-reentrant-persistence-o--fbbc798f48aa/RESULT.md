# A sharp explorer-mortality threshold for reentrant persistence on star habitats

## Finding

In the fast-exploration, homogeneous single-species metapopulation model with **neighbor-born propagules** and independent propagule mortality, the capacity of a star landscape is either strictly increasing with exploration rate or has exactly one finite global maximum. A sharp mortality–hub-degree condition completely separates these two regimes. This enables an explicit ecological *reentrance*: a species can invade at intermediate exploration rates but fail to invade at both sufficiently low and sufficiently high rates, with no parameter change other than exploration efficiency.

Let \(K_{1,m}\) be the unweighted undirected star with one hub, \(m\) leaves and \(m\ge 2\). Let \(A\) and \(L=\operatorname{diag}(A\mathbf 1)-A\) denote its adjacency and combinatorial Laplacian matrices. Set exploration efficiency \(f=D/\lambda>0\), explorer mortality ratio \(g=\gamma/\lambda\ge0\), \(s=1+g\), and maximal explorer-creation factor \(\xi>0\). For the source-model feasibility matrix \(C(f)=\xi f A/(1+f)\), define the effective colonization matrix and landscape capacity by
\[
K_f=\frac{\xi f}{1+f}(sI+fL)^{-1}A,\qquad \Lambda(f)=\rho(K_f).
\]
Then for all \(f>0\),
\[
\boxed{\Lambda(f)=\frac{\xi f\big[mf+\sqrt{m(s+f)(s+mf)}\big]}{(1+f)s[s+(m+1)f]}.}
\]
Put \(s_c(m)=4m(m+1)/(m-1)^2\). Exactly one of the following alternatives holds:

1. If \(1\le s\le s_c(m)\), then \(\Lambda(f)\) is strictly increasing for every finite \(f>0\) and converges to \(2m\xi/[s(m+1)]\); in particular, it has no finite maximizer. This includes the equality case \(s=s_c(m)\).
2. If \(s>s_c(m)\), there exists exactly one \(f_*\in(0,\infty)\) at which \(\Lambda(f)\) reaches its strict global maximum; it increases before \(f_*\) and decreases after \(f_*\). More explicitly, there is exactly one \(r_*\in(1,\sqrt m)\) solving
\[
\boxed{s=\frac{m(m+r_*^2)(r_*+1)^2}{(m-r_*^2)^2},\qquad f_*=\frac{s(m-r_*^2)}{m(r_*^2-1)}.}
\]
In the latter regime \(\Lambda(f_*)>\Lambda(\infty)=2m\xi/[s(m+1)]\), so every threshold strictly between these two numbers and below \(\Lambda(f_*)\) is crossed exactly twice as \(f\) increases, when it also exceeds \(\Lambda(0+)=0\).

**Exact witness.** The seventeen-patch star with \(m=16\), \(g=19\), \(\xi=1\) has \(s=20>s_c(16)=1088/225\) and its **unique** maximizing rate is \(f_*=5\), with
\[
\Lambda(5)=\frac19,\qquad \Lambda(\infty)=\frac8{85}<\frac1{10}<\frac19.
\]
For settled death-to-colonization ratio \(e/c=1/10\), the deterministic population model has a strictly positive equilibrium exactly for \(f\in(f_-,f_+)\), with unique thresholds \(f_-\in(1,7/4)\) and \(f_+\in(40,42)\) (numerically \(f_-\approx1.7055989037\), \(f_+\approx40.5833395245\)). At both endpoints and outside this interval, extinction is globally attracting. Thus it is genuinely a two-sided invasion window, not merely a reduction of an already supercritical reproduction number.

For the two-patch special case \(m=1\), direct diagonalization gives \(\Lambda(f)=\xi f/[s(1+f)]\), strictly increasing; it cannot exhibit this mechanism.

## Assumptions and scope

We take the large-patch, deterministic, fast-exploration reduction of Bernardi et al. with equal carrying capacities, positive constant settled colonization and death parameters \(c,e>0\), and explorer killing at rate \(\gamma\ge0\) in addition to attempted settling at rate \(\lambda>0\). An explorer moves on every undirected edge at rate \(D=f\lambda\); it is created only at a neighbor, with matrix \(C(f)=\xi fA/(1+f)\). All \(m+1\) patches have equal local demographic rates. The actual settled density \(p_i(t)\in[0,1]\) evolves according to
\[
\dot p_i=-e p_i+c(1-p_i)(K_f p)_i.
\]
Explorer birth scaling, movement rate, and mortality are independent parameters exactly as specified above; as \(f\) changes, the source-model birth feasibility \(C(f)\) also changes according to its stated constitutive law. This is not a fixed total-birth-budget comparison. The model is deterministic and corresponds to the fast-exploration approximation, not the fully finite-patch stochastic process.

## Proof

**1. Positive kernel and radial spectral reduction.** Write \(F=sI+fL\). For \(s>0,f>0\) and a connected star, \(F\) is an irreducible symmetric nonsingular \(M\)-matrix, so \(F^{-1}\) is entrywise positive. Each column of \(A\) contains a positive entry; therefore \(K_f\) is entrywise strictly positive. By star automorphisms and simplicity of the Perron eigenvalue, its positive Perron vector is constant on all leaves. On hub/leaf-constant coordinates the matrix \(F\) reduces to
\[
F_{\mathrm{rad}}=\begin{pmatrix}s+mf&-mf\\-f&s+f\end{pmatrix},
\qquad A_{\mathrm{rad}}=\begin{pmatrix}0&m\\1&0\end{pmatrix}.
\]
Consequently, using \(\det F_{\mathrm{rad}}=s[s+(m+1)f]\),
\[
K_{\mathrm{rad}}=\frac{\xi f}{(1+f)s[s+(m+1)f]}
\begin{pmatrix}mf&m(s+f)\\s+mf&mf\end{pmatrix}.
\]
The positive eigenvalue of this positive two-by-two matrix is precisely the displayed closed form for \(\Lambda(f)\), and it is the full-matrix Perron root because its eigenvector is strictly positive.

**2. A strictly monotone scalar parameter.** Assume \(m>1\) and define
\[
r=\sqrt{\frac{m(s+f)}{s+mf}}.
\]
As \(f\) runs from zero to infinity, \(r\) decreases strictly from \(\sqrt m\) to \(1\). Solving for \(f\), and substituting in the Perron formula, gives the equivalent rational expression
\[
f=\frac{s(m-r^2)}{m(r^2-1)},\qquad
\Lambda=\frac{\xi m(r+1)(m-r^2)}{(m+r)[m(r^2-1)+s(m-r^2)]}.
\]
The denominator is strictly positive on \(1<r<\sqrt m\). Direct differentiation and cancellation show that the sign of \(d\Lambda/dr\) is the sign of
\[
s(m-r^2)^2-m(m+r^2)(r+1)^2.
\]
Equivalently, it is the sign of \(s-S_m(r)\), where
\[
S_m(r)=\frac{m(m+r^2)(r+1)^2}{(m-r^2)^2}.
\]
Its logarithmic derivative is
\[
\frac{S_m'(r)}{S_m(r)}=
\frac{2r}{m+r^2}+\frac{2}{r+1}+\frac{4r}{m-r^2}>0.
\]
Thus \(S_m\) strictly increases from \(S_m(1)=s_c(m)\) to infinity. If \(s\le s_c(m)\), then \(d\Lambda/dr<0\) everywhere, giving strict increase in \(f\). If \(s>s_c(m)\), there is exactly one critical point, at \(r_*\). Because \(r\) decreases with \(f\), \(d\Lambda/df\) changes from positive to negative there. Hence this point is the unique strict global maximum. Evaluation at \(r=\sqrt m\) and \(r=1\) yields the endpoint limits. The same sign argument gives every equality case, including \(s=s_c(m)\).

**3. Exact two-sided persistence window.** With \(m=16,s=20\), substituting \(r_*=2\) gives \(S_{16}(2)=20\), and the inversion yields \(f_*=5\). Substituting in the capacity formula gives \(1/9\), while its high-mobility limit is \(8/85\). Choosing \(e/c=1/10\) lies strictly between the high-mobility limit and the unique maximum. Since capacity starts at zero, is strictly increasing up to the maximum and strictly decreasing afterwards, the equation \(\Lambda(f)=1/10\) has precisely two positive solutions. Direct substitution at \(f=1,7/4,40,42\) rigorously brackets the two roots; exact fraction/radical comparisons appear in `check.py`.

For completeness, the extinction threshold can be justified at equality without relying on a strict-inequality statement from the source. If \(\Lambda\le e/c\), let \(w>0\) be a left Perron eigenvector for the positive kernel. For every nonzero state in the compact positive cube,
\[
\frac{d}{dt}(w^\top p)
=(c\Lambda-e)w^\top p-c\sum_i w_ip_i(K_fp)_i<0.
\]
At least one \(p_i>0\), and strict positivity of \(K_f\) makes the last term positive; compactness and the invariance principle imply convergence to extinction. If \(\Lambda>e/c\), for a positive right Perron vector \(v\), a sufficiently small \(\varepsilon v\) is a strict subsolution of the equilibrium map \(p\mapsto cK_fp/(e\mathbf1+cK_fp)\), while \(\mathbf1\) is a supersolution. Monotone iteration yields a strictly positive equilibrium. Therefore the open two-crossing capacity interval is *exactly* the strictly-positive-equilibrium regime.

## Verification

Extract `check.py` in the same directory and run `python3 check.py` with Python 3, NumPy and SymPy. The checker independently verifies the symbolic rational reduction, the factored critical derivative, both limits, the unique exact optimum, the seventeen-patch full positive matrix's exact Perron certificate, and 500 full-matrix sampled eigenvalue comparisons. It also checks strict inequalities bracketing the two crossings. These tests passed during preparation. The universal monotonicity and uniqueness for all real parameters and all star sizes rest on the analytical sign proof, not on the finite samples.

## Relationship to prior work

Bernardi, Doimo, Nicoletti et al. (2026), Sections II.1–II.3 and III.1, supply the fast-exploration kernel with explicit \(g=\gamma/\lambda\), neighbor-born feasibility \(C(f)=\xi fA/(1+f)\), and the Perron persistence criterion, together with numerical network comparisons. The new result classifies the entire mobility response for *every* star, identifies the exact explorer-mortality condition for a finite interior maximum, and gives an explicit two-sided invasion window; those formulas and classifications are not in the inspected sections or appendices.

Nicoletti et al. (2023) develop the microscopic explorer framework and say intrinsic explorer death could be included, but the inspected original model sets that additional killing rate to zero. In its zero-killing case \(s=1\), the present theorem has strictly monotone capacity for every star; the positive-killing reentrance established here is therefore not a deduction from that zero-killing specialization. General metapopulation capacity is established earlier by Hanski and Ovaskainen; neither that criterion nor the 2026 general kernel alone implies this sharp star-specific monotonicity classification. Other literature describes intermediate migration optima in different stochastic, Allee-effect, or time-varying metapopulation models; those results are not mathematically interchangeable with this spectral kernel.

A related published analysis of a star's damping ratio upon **adding a leaf corridor** treats a different, affine adjacency recruitment matrix and a different parameter change; it does not imply a star-specific optimum of \(\rho((sI+fL)^{-1}A)\) as continuous explorer mobility changes. All such comparisons concern mathematical implications, not title matches.

## Limitations

The star has uniform unweighted corridors, equal patch capacities, equal settled birth and death parameters, positive mobility, and the specific neighbor-born creation function prescribed above. A different creation function, directional corridors, heterogeneous rates, or a moving-settled population need not have the same threshold. The finite-patch microscopic process eventually becomes extinct under demographic noise even when the deterministic equilibrium is positive; the term *persistence* here means supercritical deterministic invasion and existence of positive equilibrium, not perpetual finite-population survival. The maximizer is not a universal ecological management recommendation. The 2023 precursor makes positive explorer mortality a natural extension, and undiscovered earlier algebraic treatment of this precise specialization remains a historical-priority risk. Independent mathematical audit has not been performed.

## References

1. D. Bernardi, A. Doimo, G. Nicoletti, P. Padmanabha, A. Rinaldo, S. Suweis, S. Azaele and A. Maritan, *Habitat heterogeneity and dispersal network structure as drivers of metacommunity dynamics*, arXiv:2602.06640, first publicly submitted 2026-02-06. https://arxiv.org/abs/2602.06640. Particularly §§II.1–II.3 and III.1 and Appendix A.
2. G. Nicoletti, P. Padmanabha, S. Azaele, S. Suweis, A. Rinaldo and A. Maritan, *Emergent encoding of dispersal network topologies in spatial metapopulation models*, PNAS 120 (2023), e2311548120, first journal publication 2023-11-06. https://doi.org/10.1073/pnas.2311548120. Lawful open-access full text at https://pmc.ncbi.nlm.nih.gov/articles/PMC10655566/.
3. I. Hanski and O. Ovaskainen, *The metapopulation capacity of a fragmented landscape*, Nature 404 (2000), 755–758. https://doi.org/10.1038/35008063.
4. Related published record, *A sharp star-network transition in corridor gains and damping loss*, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-star-network-transition-in-corridor-gains-and-damping-lo--f2d1da0235f6.
