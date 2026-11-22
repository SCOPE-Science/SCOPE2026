# Pairwise-independent preimage-twin distances in a nonlinear binary cellular automaton

## Finding

Fix a positive ring length \(n\) and the binary five-neighbor cellular automaton
\[
(F_nx)_i=x_{i+1}+x_{i+2}+x_i(1+x_{i+2})x_{i+3}+x_{i+1}(1+x_{i+3})x_{i+4}
\]
with subscripts modulo \(n\) and all arithmetic in \(\mathbb F_2\). Each attainable output has exactly two cyclic preimages. Choose an attainable output uniformly and write \(H_n\) for the Hamming distance between its two preimages. The following describes its full distribution and its asymptotic fluctuations.

Define \(w:\{0,1\}^3\to\{0,1\}\) by
\[
w(a,b,c)=1+a(1+b)c+(1+a)b(1+c)\pmod2.
\]
Let \(T(z)\) be the \(8\times8\) matrix indexed by binary triples \((a,b,c)\), with a directed contribution \(z^{w(a,c,d)}\) from \((a,b,c)\) to \((b,c,d)\), for each \(d\in\{0,1\}\); coincident contributions are added. For **every** \(n\ge1\),
\[
\boxed{\mathbb E[z^{H_n}]=2^{-n}\operatorname{tr}\big(T(z)^n\big).}
\]
This gives the complete finite-length probability distribution, with no asymptotic approximation. The characteristic polynomial of \(T(z)\) factors as
\[
\begin{aligned}
\chi(t,z)={}&(t^4-t^2z^2+t^2z+tz^3-tz+z^4-2z^3+z^2)\\
&\cdot(t^4-2t^3z+t^2z^2-t^2z-tz^3+2tz^2-tz+z^4-2z^3+z^2).
\end{aligned}
\]
For every \(n\ge7\), the individual indicators of whether the two preimages differ at a specified site are **pairwise independent**, each with success probability \(3/4\), but they are **not jointly independent**: for any three consecutive sites,
\[
\mathbb P(\Delta_i=\Delta_{i+1}=\Delta_{i+2}=1)=\frac7{16}\ne\left(\frac34\right)^3.
\]
Consequently, for all \(n\ge7\),
\[
\boxed{\mathbb E H_n=\frac{3n}{4},\qquad
\operatorname{Var}(H_n)=\frac{3n}{16},}
\]
and as \(n\to\infty\),
\[
\boxed{\frac{H_n-3n/4}{\sqrt{3n/16}}\ \Longrightarrow\ \mathcal N(0,1).}
\]
The mean, exact variance, and Gaussian limit quantify the *typical* preimage-twin separation left undetermined by the earlier exact minimum-distance result.

## Assumptions and scope

The configuration space is \(\{0,1\}^{\mathbb Z/n\mathbb Z}\), whose coordinates are indexed even when \(n<5\) so that neighbor indices may coincide. All maps and probabilities are finite and exact. A target \(y\) is *attainable* if \(F_n^{-1}(y)\ne\varnothing\). Uniform means each attainable target has equal probability; the two preimages of an attainable target form a single unordered pair. The automaton is the second two-to-one example in Appendix B of Haugland--Larsen--Omland--Rustad (2026). This result concerns the one-step cyclic map, not its arbitrary iterates or the locally-eventually-onto question on the bilateral full shift.

## Proof

**1. Factorization and uniform source variable.** Define the cyclic difference \((Du)_i=u_i+u_{i+1}\), shift \((\sigma u)_i=u_{i+1}\), and nonlinear involution
\[
(Ku)_i=u_i+u_{i-1}(1+u_{i+1})u_{i+2}.
\]
The Boolean identities \(K^2=\mathrm{id}\) and \(F_n=D\sigma K\) hold for every \(n\); they were established for this rule in the earlier minimum-separation result and are independently verified here by the exhaustive local Boolean checks in `verify.py`. Their universal validity follows because the second composition's output at one site depends on only seven input bits; checking all \(2^7\) assignments certifies the identity for every bilateral configuration and every cyclic ring, including repeated-index cases. The factorization identity is checked for every five-bit assignment and algebraically is immediate from expansion.

On a cyclic ring, \(D\) has kernel \(\{0^n,1^n\}\) and image the even-parity subspace, so every attainable target of \(D\sigma K\) has exactly two preimages. Because \(K\) is a bijection, the two preimages associated to any \(u\in\{0,1\}^n\) are
\[
x=K(u),\qquad x'=K(\mathbf1+u).
\]
As \(u\) ranges uniformly over the ring, each unordered preimage pair is counted twice. Hence sampling uniform \(u\) produces exactly the required uniform target distribution.

**2. Local difference function.** Subtract the two displayed preimages over \(\mathbb F_2\). At site \(i\),
\[
\Delta_i=x_i+x'_i=w(u_{i-1},u_{i+1},u_{i+2}),\quad
H_n=\sum_{i=0}^{n-1}\Delta_i.
\]
The truth table of \(w\) has value zero exactly at \((0,1,0)\) and \((1,0,1)\), and value one at the other six triples. This implies \(\mathbb P(\Delta_i=1)=3/4\) whenever the three inputs are distinct, in particular for \(n\ge7\). More strongly, conditioning on **any one** argument of \(w\), exactly three of the remaining four pairs yield \(w=1\). Thus \(w\) is independent of each of its individual input coordinates.

For distinct sites \(i,j\) on rings \(n\ge7\), the sets \(\{i-1,i+1,i+2\}\) and \(\{j-1,j+1,j+2\}\) meet in at most one site. If disjoint, their outputs are independent. If they meet, conditional independence given their unique shared input, together with the preceding independence of each output from that input, proves unconditional independence. Therefore all distinct \(\Delta_i,\Delta_j\) are pairwise independent Bernoulli\((3/4)\). Adding their variances yields the mean and variance formulas. Enumeration of the six distinct input coordinates needed for three consecutive indicators gives \(\mathbb P(\Delta_i=\Delta_{i+1}=\Delta_{i+2}=1)=7/16\); there are at most six such inputs and the same fraction holds for every \(n\ge7\). Since \(7/16\ne27/64\), three-wise independence fails.

**3. Exact finite distribution.** A cyclic word \(u\in\{0,1\}^n\) corresponds bijectively to a closed walk of length \(n\) in the order-three binary de Bruijn graph: at step \(i\), use state \((u_{i-1},u_i,u_{i+1})\), next state \((u_i,u_{i+1},u_{i+2})\), and weight \(z^{\Delta_i}\). The product of edge weights equals \(z^{H_n}\). Taking the trace of \(T(z)^n\) sums exactly once over all indexed cyclic words, including for \(n=1,2\), when graph walks repeat vertices or edges. Divide by \(2^n\) to obtain the probability generating function. The displayed characteristic polynomial is an exact determinant identity; the standalone checker verifies it on all \(9^2\) pairs of integers \((z,t)\in\{0,\ldots,8\}^2\). Both polynomials have degree at most eight separately in \(z\) and in \(t\), so bivariate interpolation makes that finite check an exhaustive proof of the polynomial identity.

**4. Gaussian limit.** Consider an infinite independent fair Bernoulli sequence \((U_j)_{j\in\mathbb Z}\) and the stationary local sequence \(Z_i=w(U_{i-1},U_{i+1},U_{i+2})\). This sequence is three-dependent, since sets of variables with indices separated by at least four are disjoint. The local pairwise-independence argument gives variance \(3/16\) per term and zero off-diagonal covariances. To see the central limit theorem without invoking an external theorem, split a long interval into blocks of length \(\lfloor n^{1/3}\rfloor\) separated by three discarded indices. The sums on retained blocks are independent, uniformly bounded by a quantity \(o(\sqrt n)\), and have aggregate variance asymptotic to \(3n/16\); therefore their normalized sum obeys the Lindeberg central limit theorem. The discarded terms have variance \(O(n^{2/3})\) by pairwise uncorrelatedness and vanish after normalization. Coupling the cyclic input to the first \(n\) letters of the infinite sequence changes at most three boundary indicators, so the cyclic and linear centered, scaled sums differ by \(O(n^{-1/2})\). This proves the stated limit.

## Verification

The self-contained standard-library `verify.py` checks for each \(n\in\{1,\ldots,11\}\) every cyclic input, the factorization-based partner and its common image, the exact transfer-matrix trace at four values of \(z\), and the local Hamming expression. For \(n\ge7\) it checks the exact means, variances and consecutive-triple law by integer arithmetic. It further verifies the universal local involution identity on all seven-bit neighborhoods; the factorization on all five-bit neighborhoods; the conditional one-bit balance of \(w\); and the characteristic polynomial on the complete \(9\times9\) interpolation grid using an integer determinant. The extracted script prints `VERIFY_OK checks= 4403`. The Gaussian limit and pairwise-independence for arbitrary \(n\) follow from the proof and are not inferred from finite sampling.

## Relationship to prior work

Haugland, Larsen, Omland and Rustad (2026) introduced and tabulated this two-to-one five-neighbor rule. The earlier published published-finding corpus finding *Sharp mod-three separation of cyclic preimage twins for a nonlinear five-neighbor automaton* proves that every ring fiber has two points and exactly determines the **minimum**, over targets, of their Hamming separation; it supplies a 64-state weighted collision graph, from which a finite-ring distance enumerator could in principle be computed. The present finding does **not** claim the previously established two-to-one fact, the nonlinear involution, a generic transfer-graph method, or the minimum distance as new. Its contribution is the explicitly simplified **distributional law** and the surprising exact pairwise independence despite strictly nontrivial triple correlations, yielding exact typical mean/variance and a Gaussian fluctuation theorem for uniformly sampled fibers. The earlier published-finding corpus result *Exact cyclic image obstructions for two open five-neighbor binary automata* addresses the **first and third** rules' image membership, not these probabilities for the second rule. The general 2024 work on almost liftings studies inverse multiplicity and cryptographic structure, not this pairwise-independent distance law.

## Limitations

The pairwise-independence and finite mean/variance formulas require \(n\ge7\), while the transfer-matrix probability formula is valid for **all** positive lengths. The Gaussian limit describes the uniform distribution on attainable finite-ring targets, not a prescribed target or the bi-infinite measure-theoretic fiber. The result does not solve the LEO question, establish cryptographic security, or claim a new central limit theorem for generic dependent variables. The prior weighted collision automaton supplies an implicit way to calculate finite-length distance counts, and independent historical priority validation has not occurred.

## References

1. J. K. Haugland, N. S. Larsen, T. Omland and H. G. Rustad, *Locally eventually onto cellular automata*, arXiv:2610.33131v1, first public 2026-10-23, especially Appendix B, https://arxiv.org/abs/2610.33131 .
2. *Sharp mod-three separation of cyclic preimage twins for a nonlinear five-neighbor automaton*, published published-finding corpus research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-mod-three-separation-of-cyclic-preimage-twins-for-a-nonlin--8e3c21dab42f .
3. *Exact cyclic image obstructions for two open five-neighbor binary automata*, published published-finding corpus research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-cyclic-image-obstructions-for-two-open-five-neighbor-binar--b4fa1671dcc9 .
4. J. K. Haugland and T. Omland, *Shift-invariant transformations and almost liftings*, arXiv:2407.11931v1, first public 2024-07-16, https://arxiv.org/abs/2407.11931 .
5. W. Hoeffding and H. Robbins, *The central limit theorem for dependent random variables*, Duke Mathematical Journal **15** (1948), 773–780, https://doi.org/10.1215/S0012-7094-48-01568-3 .
