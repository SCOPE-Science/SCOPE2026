# Period-three entropy trichotomy and sharp nontrivial extremizers for reversible elementary cellular automata

## Finding

For each Wolfram elementary binary cellular automaton rule \(r\in\{0,\ldots,255\}\) and each labelled periodic ring of length \(n\ge3\), let \(F_{r,n}\) be its simultaneous update. Its reversible second-order update is
\[
 R_{r,n}(u,v)=(v,\,u\mathbin{\oplus}F_{r,n}(v)),
\]
where \(\oplus\) denotes componentwise addition modulo two. Write \(N_r(n)=|\operatorname{Fix}(R_{r,n}^{3})|\) for the number of *states* fixed by the third iterate (not the number of primitive three-orbits). Define
\[
 h_r=\limsup_{n\to\infty}\frac1n\log\max\{1,N_r(n)\}.
\]

**Complete trichotomy.** Exactly 129 rules have \(h_r>0\); 116 rules have a nonempty but uniformly bounded sequence \(N_r(n)\); and eleven rules have \(N_r(n)=0\) for every \(n\ge3\). The eleven empty rules are 167, 173, 181, 189, 191, 229, 231, 239, 247, 253, and 255. This counts Wolfram numbers separately, without quotienting by spatial or symbol symmetries.

**Sharp extremum and gap.** Exactly rules 51 and 204 have \(N_r(n)=4^n\) for all \(n\ge3\), and hence \(h_r=\log4\). Among the other 254 rules, exactly rules 50 and 76 maximize \(h_r\), with
\[
 h_{50}=h_{76}=\log\lambda,
 \quad \lambda=3.1457354563\ldots,
 \quad \lambda^4-2\lambda^3-2\lambda^2-6\lambda+3=0.
\]
All remaining 252 rules satisfy the rigorous uniform gap \(h_r<\log(25/8)\). The polynomial has a unique root above \(1\); \(\lambda>25/8\).

**Exact extremal recurrence.** Let \(S_0=4\), \(S_1=2\), \(S_2=8\), \(S_3=38\), and for \(n\ge4\) put
\[
 S_n=2S_{n-1}+2S_{n-2}+6S_{n-3}-3S_{n-4}.
\]
Then, for every \(n\ge3\),
\[
 N_{50}(n)=N_{76}(n)=S_n+6\mathbf{1}_{3\mid n}.
\]
The first six values (ring lengths three through eight) are 44, 92, 302, 998, 3026, and 9572.

## Assumptions and scope

The periodic ring consists of \(n\) *indexed* binary sites, all updated simultaneously within each first-order map. For rule \(r\), the bit at a site with left, center, right input bits \((a,b,c)\) equals bit number \(4a+2b+c\) of the integer \(r\), the least significant bit being bit zero. The extended state is an ordered pair of whole-ring words \((u,v)\); its \(4^n\) possible values are counted individually. All assertions hold for every integer \(n\ge3\), not merely for the enumerated test lengths. The period-three condition includes states of temporal least period one; no primitive-period-three count is claimed here.

## Proof

**1. Exact temporal-column encoding.** Suppose three successive binary rows are \(A,B,C\) and repeat. The three applications of the reversible map yield precisely
\[
 F_{r,n}(A)=B\oplus C,\qquad
 F_{r,n}(B)=C\oplus A,\qquad
 F_{r,n}(C)=A\oplus B.
\]
Conversely any triple of rows satisfying these three identities defines exactly one state \((A,B)\) fixed by \(R_{r,n}^3\); thus the correspondence is bijective. Code the column \((A_i,B_i,C_i)\) as one of eight symbols \(x_i\in\{0,\ldots,7\}\), with the high, middle, and low bits representing the three temporal rows. A triple of adjacent columns \((x,y,z)\) is legal if and only if all three displayed binary equations hold at its center column. Define a directed 64-vertex graph whose vertices are ordered pairs \((x,y)\), with edge \((x,y)\to(y,z)\) exactly when the triple is legal. Let \(M_r\) be its integral adjacency matrix. The standard closed-walk correspondence is exact for indexed periodic words, including spatial periods strictly dividing \(n\):
\[
 N_r(n)=\operatorname{tr}(M_r^n) \quad(n\ge3).
\]
This proves the all-length reduction without numerical extrapolation.

**2. Exact finite all-rule classification.** The attached standalone checker constructs every one of the \(256\cdot 8^3\) possible rule/triple instances and finds all strongly connected components of each 64-vertex graph. Remove acyclic components. If no cyclic component remains then every trace is zero. If every cyclic component is a simple directed cycle, the trace for every positive length is at most 64, and some trace is nonzero. Otherwise a strongly connected component contains a branching vertex and has Perron eigenvalue strictly above one: some fixed-length directed walks expand from every starting vertex by at least a factor greater than one, so the traces grow exponentially along a subsequence. The exhaustive integer checker establishes, respectively, 11, 116, and 129 rules; it records every rule in each class and the eleven empty labels. This classification is a finite, fully specified algorithm over exactly 64 vertices per rule, not an empirical fit to small values of \(n\).

**3. A certified gap for 252 rules.** For each \(r\notin\{50,51,76,204\}\), compute the row sums of \(M_r^{56}\) by iterating the all-ones vector 56 times using only integer additions. The certificate checks, for *all* these 252 rules, the strict integer inequality
\[
 8^{56}\max_i\sum_j (M_r^{56})_{ij}<25^{56}.
\]
By the infinity-norm spectral radius bound, \(\rho(M_r)^{56}\le\max_i\sum_j(M_r^{56})_{ij}\), and therefore \(\rho(M_r)<25/8\). Since \(N_r(n)=\operatorname{tr}(M_r^n)\) and the matrix dimension is 64, \(h_r\le\log\max\{1,\rho(M_r)\}<\log(25/8)\). The attached checker verifies the inequality by exact integers, with no floating-point eigenvalue comparisons.

**4. Exceptional rules.** For both \(r=50\) and \(r=76\), exactly two cyclic strongly connected components survive: an isolated loop and a 16-vertex component with 43 internal edges. Newton identities applied to the exact integer powers of the 16-by-16 adjacency block give the characteristic polynomial
\[
 t^7(t-1)(t^2+t+1)^2(t^4-2t^3-2t^2-6t+3).
\]
The isolated loop contributes one more eigenvalue one; all other components are acyclic. The roots of \(t^2+t+1\) contribute \(4\) to a trace when \(3\mid n\), and \(-2\) otherwise. Together with the two eigenvalues one, their total is \(6\mathbf{1}_{3\mid n}\). Newton's power-sum recurrence for the quartic roots gives precisely the sequence \(S_n\) stated above. The 16-vertex component has a self-loop and is strongly connected, hence primitive. Its Perron eigenvalue is the positive real root \(\lambda\) of the quartic; this polynomial has exactly one real root larger than one by Descartes' rule of signs, and its value at \(25/8\) is \(-3887/4096\). Therefore \(\lambda>25/8\), so rules 50 and 76 strictly dominate all other nontrivial rules.

Finally the first-order rules 51 and 204 act sitewise as complement and identity, respectively. For either first-order operation, the reversible map satisfies \(R_{r,n}^3=\operatorname{id}\) on all \(4^n\) states. Since this is the absolute maximum possible count, these two rules are the unique global maximizers by the previously certified gap and \(\lambda<4\). This completes the classification and extremal assertions.

## Verification

The portable Python 3 standard-library script `verify/period3_census.py` independently constructs the 64-state transfer graph for every rule, computes every strongly connected component, certifies all 252 rational spectral-radius bounds, verifies the full 16-by-16 characteristic polynomials of the two extremizers using exact Newton identities, and checks the complete trichotomy. Its recorded deterministic output is `verify/period3_census_output.json`. The separate brute-force script `verify/direct_reversible_simulation.py` iterates the original reversible update over every one of the \(4^n\) states for all 256 rules and every \(n\in\{3,4,5,6\}\); its complete-result digest and selected check values are in `verify/direct_reversible_simulation_output.json`. The two exhaustive methods agree at every one of these cases. No finite simulation is used as the proof of the infinitely many ring lengths: those follow from the exact transfer graph and integer spectral certificate.

## Relationship to prior work

Wolfram supplies the original 256 binary elementary rules; Toffoli and Margolus give the second-order reversible construction. Takesue treats ergodic and thermodynamic properties of elementary reversible cellular automata. Formenti and Kamilya (2024) classify equivalences and study broad dynamical types of reversible elementary second-order automata; its publicly readable abstract and publisher-hosted appendix develop other dynamical properties, including blocking words and transitivity. The later single-rule study (2026) analyzes periodicity of finite-support Rule 115 configurations. These are materially related objects, but none of the material actually inspected states the particular all-rule third-iterate trichotomy, extremizers, integer spectral gap, or quartic count. The 2024 and 1989 full papers were not accessible and might contain relevant uninspected results; their absence is not taken as a proof of originality. Published results on one-step images and predecessor multiplicities concern the first-order maps, and therefore do not imply the stated second-order third-iterate extremum.

## Limitations

The theorem concerns fixed points of the **third iterate** on finite periodic binary rings, not all temporal periods, asymptotic behavior of arbitrary infinite configurations, or a full entropy classification across periods. The proof's finite integer certificate is reproducible but is not an independently audited formal proof. Although related published statements were compared, inaccessible archival full texts leave residual historical-priority uncertainty. The reported numerical growth constant is for orientation only; all strict comparisons use exact integer or rational calculations.

## References

1. S. Wolfram, *Statistical mechanics of cellular automata*, Rev. Mod. Phys. 55 (1983), 601–644, https://doi.org/10.1103/RevModPhys.55.601.
2. T. Toffoli and N. Margolus, *Cellular Automata Machines*, MIT Press (1987), section 14.2, https://people.csail.mit.edu/nhm/cam-book.pdf.
3. S. Takesue, *Ergodic properties and thermodynamic behavior of elementary reversible cellular automata. I. Basic properties*, J. Stat. Phys. 56 (1989), https://doi.org/10.1007/BF01044442.
4. E. Formenti and S. Kamilya, *On Elementary Second Order Cellular Automata*, ASCAT 2024, pp. 204–218, https://doi.org/10.1007/978-3-031-56943-2_16.
5. E. Formenti and S. Kamilya, *The Curious Case of Reversible Elementary Second Order Cellular Automaton 115*, 2026, https://arxiv.org/abs/2606.13159.
