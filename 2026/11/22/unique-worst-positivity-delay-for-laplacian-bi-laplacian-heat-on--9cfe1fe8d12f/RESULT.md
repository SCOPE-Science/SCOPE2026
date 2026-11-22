# Unique worst positivity delay for Laplacian–bi-Laplacian heat on every star

## Finding
Let \(K_{1,m}\) be the simple unweighted star with one hub and \(m\ge2\) leaves. Denote its combinatorial Laplacian by \(L\) and, for \(\eta>0\), consider the self-adjoint constant-preserving semigroup
\[
S_{m,\eta}(t)=e^{-t(L+\eta L^2)},\qquad t\ge0.
\]
There is one exact positivity-recovery time \(\tau_m(\eta)>0\). All matrix entries are nonnegative exactly at \(t=0\) or \(t\ge\tau_m(\eta)\), and all entries are strictly positive for \(t>\tau_m(\eta)\). The time is uniquely determined as the positive root of
\[
m-(m+1)e^{-(1+\eta)t}+e^{-(m+1)(1+(m+1)\eta)t}=0.
\]

More sharply, define
\[
h_m=\log\frac{m+2}{m+1},\qquad
r_m=1+\frac{\log(m+1)}{h_m},\qquad
\eta_m^*=\frac{r_m-(m+1)}{(m+1)^2-r_m}.
\]
Then \(\eta_m^*>0\) is the **unique** strength maximizing the finite-time lack of positivity, with attained sharp value
\[
\boxed{\max_{\eta>0}\tau_m(\eta)=\tau_m^*
=\frac{m(m+2)\log\frac{m+2}{m+1}-\log(m+1)}{m(m+1)},\quad
\text{attained only at }\eta=\eta_m^*.}
\]
In the growing-star limit,
\[
\frac{m\eta_m^*}{\log m}\longrightarrow1,\qquad m\tau_m^*\longrightarrow1.
\]
For \(m=2\) the optimal strength is approximately \(0.435009042901945\) and maximum delay approximately \(0.200474048491023\). The two-vertex path cannot exhibit this positivity failure.

## Assumptions and scope
The graph has one hub, \(m\ge2\) equivalent leaves, and unit conductances. We use the **unnormalized** combinatorial Laplacian on counting \(\ell^2\) and the usual coordinatewise nonnegative cone. Matrix entrywise nonnegativity is equivalent to preservation of nonnegative data and, because the rows sum to one, to preservation of the input-value range. A time \(t=0\) is included separately: the identity is entrywise nonnegative even when all sufficiently small positive times fail positivity. No claim is made for a normalized Laplacian, directed star, general graph, or a discrete-time integrator.

## Proof
**1. Exact decomposition.** The three invariant orthogonal subspaces are the constants (eigenvalue \(0\)), the leaf-difference subspace of dimension \(m-1\) (eigenvalue \(1\)), and the hub-versus-leaves subspace (eigenvalue \(m+1\)). The corresponding nonzero decay rates of \(L+\eta L^2\) are
\[
a=1+\eta,\qquad b=(m+1)[1+(m+1)\eta],\qquad b>(m+1)a.
\]
Let \(x=e^{-at}\), \(y=e^{-bt}\), and use index \(0\) for the hub. Orthogonal spectral projection gives
\[
S_{00}=\frac{1+my}{m+1},\qquad S_{0i}=S_{i0}=\frac{1-y}{m+1}\quad(i\ge1),
\]
\[
S_{ii}=\frac1{m+1}+\frac{m-1}{m}x+\frac{y}{m(m+1)},\quad
S_{ij}=\frac1{m+1}-\frac{x}{m}+\frac{y}{m(m+1)}\quad(1\le i\ne j\le m).
\]
All diagonal entries are strictly positive and all hub-to-leaf entries are positive for \(t>0\). Consequently the only possibly negative entries are those between distinct leaves, all equal to \(w(t)=[m-(m+1)e^{-at}+e^{-bt}]/[m(m+1)]\).

**2. Exactly one positive recovery time.** Here \(w(0)=0\), \(w'(0)=-\eta<0\), and \(w(t)\to1/(m+1)>0\). Moreover
\[
w'(t)=\frac{(m+1)a e^{-at}-b e^{-bt}}{m(m+1)}.
\]
As \(b>(m+1)a\), this derivative has precisely one positive zero, at \(\log[b/((m+1)a)]/(b-a)\), and changes from negative to positive there. Hence \(w\) has exactly one positive root \(\tau_m(\eta)\), is negative for \(0<t<\tau_m(\eta)\), and positive thereafter. This proves the full time-set and sign assertions, including strict positivity for later times.

**3. Reducing optimal strength to one strictly concave scalar function.** Put \(r=b/a\). As \(\eta\) increases over \((0,\infty)\), \(r\) increases strictly over \((m+1,(m+1)^2)\), and solving for \(a\) gives
\[
a=\frac{m(m+1)}{(m+1)^2-r}.
\]
At the unique positive root define \(h=a\tau_m(\eta)>0\). Dividing its defining equation by \(e^{-h}\) gives
\[
e^{-(r-1)h}=m+1-me^h,
\quad r=1-\frac{\log(m+1-me^h)}h,\quad 0<h<\log\frac{m+1}{m}.
\]
For a fixed positive \(h\), the root function \(m-(m+1)e^{-h}+e^{-rh}\) decreases strictly with \(r\); since it has just one positive crossing, the crossing location \(h\) increases strictly with \(r\). Its lower endpoint is \(h\downarrow0\) as \(r\downarrow m+1\), and it approaches a finite upper endpoint when \(r\uparrow(m+1)^2\). Thus optimizing over \(\eta>0\) is equivalent to optimizing over this interval of \(h\).

Substituting the rate identity into \(\tau=h/a\) yields the exact scalar representation
\[
\tau_m=F_m(h):=\frac{m(m+2)h+\log(m+1-me^h)}{m(m+1)}.
\]
Its strict second derivative is
\[
F_m''(h)=-\frac{e^h}{(m+1-me^h)^2}<0.
\]
Its unique critical point solves \((m+2)(m+1-me^h)=e^h\), hence \(e^h=(m+2)/(m+1)\). This point lies in the permitted \(h\)-interval: its corresponding spectral ratio \(r_m=1+\log(m+1)/h_m\) satisfies \(m+1<r_m<(m+1)^2\). Indeed, \(m h_m<m/(m+1)<1<\log(m+1)\), while \(m(m+2)h_m>m>\log(m+1)\), by \(1/(m+2)<h_m<1/(m+1)\). Strict concavity proves it is the unique global maximizer.

At this point \(m+1-me^{h_m}=1/(m+1)\). Evaluating \(F_m(h_m)\), and solving the relation between \(r_m\) and \(\eta\), gives the two advertised exact expressions for \(\tau_m^*\) and \(\eta_m^*\). As \(\eta\downarrow0\) the root \(h\downarrow0\) and \(\tau\downarrow0\); as \(\eta\to\infty\), the corresponding \(a\to\infty\) while \(h\) stays bounded, so \(\tau\downarrow0\). Thus no boundary strength ties the unique finite optimum.

**4. Large-star limit and minimality.** The elementary expansions \(h_m=1/m+O(m^{-2})\) and \(\log(m+1)=\log m+O(m^{-1})\) in the exact expressions give \(m\tau_m^*\to1\) and \(m\eta_m^*/\log m\to1\). For a one-edge graph, \(L^2=2L\) and therefore \(e^{-t(L+\eta L^2)}=e^{-(1+2\eta)tL}\) is ordinary Markov heat and is positive for every \(t\ge0\). The three-site star is the smallest nonpositive example.

## Verification
The standalone Python 3 script `verify_mixed_star.py` constructs each star Laplacian independently, exponentiates \(-t(L+\eta L^2)\) using a matrix exponential, compares its entries to the derived projection formulas, and tests the signs on both sides of the uniquely rooted threshold. It completed 280 matrix-and-sign tests over eight star sizes and seven strengths, checked the closed-form optimizer against independently computed roots, and tested the high-degree scaling. These checks are finite corroboration; the proof above establishes all sizes and strengths.

## Relationship to prior work
The qualitative eventual-positivity framework of Daners, Glück and Kennedy [1] does not give this star-family sharp delay or its unique worst higher-order mixing strength. Gregorio and Mugnolo [2, Sections 2 and 6] give the pure \(L^2\) star/path kernel and eventual positivity, but the mixed generator \(L+\eta L^2\) and minimax optimization over \(\eta\) are not covered. A later exact positivity-cutoff result for **pure** squared-Laplacian heat on all complete multipartite graphs [3] includes stars at the pure fourth-order endpoint but not mixed heat. A published exact spectral-window envelope [4] optimizes over all symmetric generators with fixed spectral interval; it does not imply this fixed-star formula at \(m>2\), where star leaf-pair spectral weights differ from its universal envelope, nor does it optimize strength subject to the polynomial coupling \(b=(m+1)[1+(m+1)\eta]\). The claims here do not assert novelty for the star eigenvalues or pure biheat formulas.

## Limitations
The result applies to the unweighted combinatorial stars with fixed positive higher-order coefficient, not arbitrary graphs, nonuniform edges, alternative generator normalizations, or all fourth-order semigroups. Exact positivity times do not prove monotone pointwise behavior of every kernel entry, only the full sign classification. Historical priority beyond the inspected indexed and primary texts is not certified independently.

## References
[1] D. Daners, J. Glück, J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294, first made public 2015-11-17, https://arxiv.org/abs/1511.05294 .

[2] F. Gregorio and D. Mugnolo, *Bi-Laplacians on graphs and networks*, arXiv:1712.07370, first made public 2017-12-20, https://arxiv.org/abs/1712.07370 .

[3] *Sharp positivity cutoff for squared-Laplacian heat on every complete multipartite graph*, published 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-positivity-cutoff-for-squared-laplacian-heat-on-every-comp--e4f9c89a420f .

[4] *Sharp entrywise spectral-window envelopes and the exact eventual-positivity horizon*, published 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-entrywise-spectral-window-envelopes-and-the-exact-eventual--aea2a1d10bf1 .
